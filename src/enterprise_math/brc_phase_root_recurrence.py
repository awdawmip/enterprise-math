"""Exact third-difference BRC root/remainder transport on fixed mod-8 phases.

On the common order-one deep tail, the exact odd-N representative stream has
five multiplier phases modulo 8. Each phase returns after multiplier spacing 8.

For three successive states of one phase,

    m_i*N = J_i**2 + R_i,  0 <= R_i <= 2*J_i,

put a=J_1-J_0, b=J_2-J_1 and use the quadratic extrapolation

    C = 3*J_2 - 3*J_1 + J_0.

The exact target residual at m_3=m_0+24 is

    G = R_0 - 3*R_1 + 3*R_2 - 6*b*(b-a).

Thus no target square root, order-one quotient, or q*(2J+q) product is needed.
On the common tail 4*m_0**5 >= N, the integer correction e=J_3-C lies in
[-3,387]. The existing 1 KiB normalized reciprocal table from the phase
quotient tool closes the non-negative case with at most two estimate increments
and one residual sign check; negative correction needs at most three downward
BRC basin steps.

``advance_pair`` is the low-allocation execution kernel. ``advance`` and
``current_state`` add diagnostic metadata.

This is an exact multiplier-state transport optimization. It does not shorten
the multiplier horizon or change difference-of-squares search complexity.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isqrt

from .brc_linear_deep_tail import (
    common_mod8_linear_tail_sufficient,
    next_odd_n_representative_multiplier,
    odd_n_multiplier_is_representative,
)
from .brc_phase_quotient_remainder import (
    RECIPROCAL_FRACTION_BITS,
    RECIPROCAL_INDEX_BITS,
    RECIPROCAL_RAW_BYTES,
    reciprocal_seed_table,
)

PHASE_SPACING = 8
PHASE_COUNT = 5
PHASE_SEED_TRANSITIONS = 14
PHASE_THIRD_DIFFERENCE_MIN = -3
PHASE_THIRD_DIFFERENCE_MAX = 387
# If C>=75078 then W=2C+1 > 387*388-1.
RECIPROCAL_CORRECTION_CANDIDATE_MIN = 75_078
_PHASE_INDEX = (0, 1, -1, 2, -1, 3, -1, 4)


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def phase_root_third_difference_bounds() -> tuple[int, int]:
    """Return the exact integer correction range on the common deep tail."""
    return PHASE_THIRD_DIFFERENCE_MIN, PHASE_THIRD_DIFFERENCE_MAX


def phase_root_candidate_gap(
    root0: int,
    remainder0: int,
    root1: int,
    remainder1: int,
    root2: int,
    remainder2: int,
) -> tuple[int, int]:
    """Return quadratic root extrapolation and its exact target residual."""
    for name, value in (
        ("root0", root0),
        ("remainder0", remainder0),
        ("root1", root1),
        ("remainder1", remainder1),
        ("root2", root2),
        ("remainder2", remainder2),
    ):
        _require_nonnegative(name, value)
    if remainder0 > 2 * root0 or remainder1 > 2 * root1 or remainder2 > 2 * root2:
        raise ValueError("remainder escaped its square-root BRC basin")

    first_increment = root1 - root0
    second_increment = root2 - root1
    candidate = 3 * root2 - 3 * root1 + root0
    gap = (
        remainder0
        - 3 * remainder1
        + 3 * remainder2
        - 6 * second_increment * (second_increment - first_increment)
    )
    return candidate, gap


class _BoundedReciprocalBucket:
    __slots__ = ("shift", "lower", "upper", "reciprocal")

    def __init__(self) -> None:
        self.shift: int | None = None
        self.lower = 0
        self.upper = 0
        self.reciprocal = 0

    def _refresh(self, denominator: int) -> None:
        bits = denominator.bit_length()
        if bits < RECIPROCAL_INDEX_BITS:
            self.shift = -1
            self.lower = 0
            self.upper = 1 << RECIPROCAL_INDEX_BITS
            self.reciprocal = 0
            return
        shift = bits - RECIPROCAL_INDEX_BITS
        mantissa = denominator >> shift
        start = 1 << (RECIPROCAL_INDEX_BITS - 1)
        self.shift = shift
        self.lower = mantissa << shift
        self.upper = (mantissa + 1) << shift
        self.reciprocal = reciprocal_seed_table()[mantissa - start]

    def floor_ratio_at_most_388(self, numerator: int, denominator: int) -> int:
        """Exact floor using the existing lower reciprocal and <=2 comparisons."""
        if numerator == 0:
            return 0
        if (
            self.shift is None
            or denominator < self.lower
            or denominator >= self.upper
        ):
            self._refresh(denominator)
        if self.shift == -1:
            quotient = numerator // denominator
            if quotient > PHASE_THIRD_DIFFERENCE_MAX + 1:
                raise AssertionError("small-denominator quotient escaped proved range")
            return quotient

        estimate = (
            numerator * self.reciprocal
        ) >> (RECIPROCAL_FRACTION_BITS + self.shift)
        if numerator >= (estimate + 1) * denominator:
            estimate += 1
            if numerator >= (estimate + 1) * denominator:
                estimate += 1
                if numerator >= (estimate + 1) * denominator:
                    raise AssertionError("reciprocal correction deficit exceeded two")
        if estimate > PHASE_THIRD_DIFFERENCE_MAX + 1:
            raise AssertionError("phase correction quotient escaped proved range")
        return estimate


class _PhaseSlot:
    __slots__ = (
        "count",
        "multiplier0",
        "multiplier1",
        "multiplier2",
        "root0",
        "root1",
        "root2",
        "remainder0",
        "remainder1",
        "remainder2",
    )

    def __init__(self) -> None:
        self.count = 0
        self.multiplier0 = self.multiplier1 = self.multiplier2 = 0
        self.root0 = self.root1 = self.root2 = 0
        self.remainder0 = self.remainder1 = self.remainder2 = 0

    def add(self, multiplier: int, root: int, remainder: int) -> None:
        if self.count and multiplier != self.multiplier2 + PHASE_SPACING:
            raise ValueError("phase visits must be spaced by eight multipliers")
        if self.count == 0:
            self.multiplier2 = multiplier
            self.root2 = root
            self.remainder2 = remainder
            self.count = 1
        elif self.count == 1:
            self.multiplier1, self.multiplier2 = self.multiplier2, multiplier
            self.root1, self.root2 = self.root2, root
            self.remainder1, self.remainder2 = self.remainder2, remainder
            self.count = 2
        elif self.count == 2:
            self.multiplier0, self.multiplier1, self.multiplier2 = (
                self.multiplier1,
                self.multiplier2,
                multiplier,
            )
            self.root0, self.root1, self.root2 = self.root1, self.root2, root
            self.remainder0, self.remainder1, self.remainder2 = (
                self.remainder1,
                self.remainder2,
                remainder,
            )
            self.count = 3
        else:
            self.multiplier0, self.multiplier1, self.multiplier2 = (
                self.multiplier1,
                self.multiplier2,
                multiplier,
            )
            self.root0, self.root1, self.root2 = self.root1, self.root2, root
            self.remainder0, self.remainder1, self.remainder2 = (
                self.remainder1,
                self.remainder2,
                remainder,
            )

    def candidate_gap(self, target_multiplier: int) -> tuple[int, int]:
        if self.count < 3 or target_multiplier != self.multiplier2 + PHASE_SPACING:
            raise ValueError("target is not the next fully seeded phase visit")
        first_increment = self.root1 - self.root0
        second_increment = self.root2 - self.root1
        candidate = 3 * self.root2 - 3 * self.root1 + self.root0
        gap = (
            self.remainder0
            - 3 * self.remainder1
            + 3 * self.remainder2
            - 6 * second_increment * (second_increment - first_increment)
        )
        return candidate, gap


@dataclass(frozen=True)
class PhaseRootRemainderState:
    n: int
    multiplier: int
    root: int
    remainder: int
    source_multiplier: int
    mode: str
    phase_correction: int

    @property
    def target_value(self) -> int:
        return self.root * self.root + self.remainder

    @property
    def ceiling_completion_gap(self) -> int:
        if self.remainder == 0:
            return 0
        return 2 * self.root + 1 - self.remainder


class PhaseRootRemainderTracker:
    """Unbounded exact phase-root stream; only fourteen seed divisions."""

    __slots__ = (
        "n",
        "multiplier",
        "root",
        "remainder",
        "_slots",
        "_bucket",
        "seed_divisions",
        "recurrent_transitions",
        "last_mode",
        "last_phase_correction",
        "last_source_multiplier",
    )

    def __init__(
        self,
        n: int,
        start_multiplier: int,
        *,
        root: int | None = None,
        remainder: int | None = None,
    ) -> None:
        _require_positive("n", n)
        _require_positive("start_multiplier", start_multiplier)
        if n % 2 == 0:
            raise ValueError("phase-root tail requires odd n")
        if not odd_n_multiplier_is_representative(start_multiplier):
            raise ValueError("start multiplier must be an odd-N mod-8 representative")
        if not common_mod8_linear_tail_sufficient(n, start_multiplier):
            raise ValueError("start multiplier is before the common order-one tail")

        target = start_multiplier * n
        if root is None:
            if remainder is not None:
                raise ValueError("remainder cannot be supplied without root")
            root = isqrt(target)
            remainder = target - root * root
        else:
            _require_nonnegative("root", root)
            if remainder is None:
                remainder = target - root * root
            _require_nonnegative("remainder", remainder)
            if root * root + remainder != target or remainder > 2 * root:
                raise ValueError("invalid initial root/remainder state")

        assert remainder is not None
        self.n = n
        self.multiplier = start_multiplier
        self.root = root
        self.remainder = remainder
        self._slots = [_PhaseSlot() for _ in range(PHASE_COUNT)]
        self._bucket = _BoundedReciprocalBucket()
        self.seed_divisions = 0
        self.recurrent_transitions = 0
        self.last_mode = "INITIAL_ROOT"
        self.last_phase_correction = 0
        self.last_source_multiplier = start_multiplier
        self._slots[_PHASE_INDEX[start_multiplier & 7]].add(
            start_multiplier,
            root,
            remainder,
        )

    def current_state(self) -> PhaseRootRemainderState:
        return PhaseRootRemainderState(
            n=self.n,
            multiplier=self.multiplier,
            root=self.root,
            remainder=self.remainder,
            source_multiplier=self.last_source_multiplier,
            mode=self.last_mode,
            phase_correction=self.last_phase_correction,
        )

    @staticmethod
    def _seed_order1(
        n: int,
        multiplier: int,
        root: int,
        remainder: int,
        target_multiplier: int,
    ) -> tuple[int, int, int]:
        h = target_multiplier - multiplier
        q = (2 * h * root) // (4 * multiplier + h)
        candidate = root + q
        gap = remainder + h * n - q * (2 * root + q)
        corrections = 0
        while gap >= 2 * candidate + 1:
            gap -= 2 * candidate + 1
            candidate += 1
            corrections += 1
            if corrections > 2:
                raise AssertionError("order-one seed correction bound failed")
        return candidate, gap, corrections

    def _close_phase_candidate(self, candidate: int, gap: int) -> tuple[int, int, int]:
        initial_candidate = candidate
        if gap < 0:
            correction = 0
            while gap < 0:
                candidate -= 1
                gap += 2 * candidate + 1
                correction -= 1
                if correction < PHASE_THIRD_DIFFERENCE_MIN:
                    raise AssertionError("negative phase correction bound failed")
            return candidate, gap, correction

        if candidate < RECIPROCAL_CORRECTION_CANDIDATE_MIN:
            correction = 0
            while gap >= 2 * candidate + 1:
                gap -= 2 * candidate + 1
                candidate += 1
                correction += 1
                if correction > PHASE_THIRD_DIFFERENCE_MAX:
                    raise AssertionError("positive phase correction bound failed")
            return candidate, gap, correction

        width = 2 * candidate + 1
        quotient = self._bucket.floor_ratio_at_most_388(gap, width)
        residual = gap - quotient * (2 * candidate + quotient)
        if residual < 0:
            residual += 2 * candidate + 2 * quotient - 1
            quotient -= 1

        candidate += quotient
        if (
            not PHASE_THIRD_DIFFERENCE_MIN
            <= quotient
            <= PHASE_THIRD_DIFFERENCE_MAX
            or not 0 <= residual <= 2 * candidate
            or candidate != initial_candidate + quotient
        ):
            raise AssertionError("table-assisted phase BRC closure failed")
        return candidate, residual, quotient

    def advance_pair(self) -> tuple[int, int, int]:
        """Advance one representative multiplier and return (root,remainder,m)."""
        source_multiplier = self.multiplier
        target_multiplier = next_odd_n_representative_multiplier(source_multiplier)
        slot = self._slots[_PHASE_INDEX[target_multiplier & 7]]

        if slot.count < 3:
            root, remainder, correction = self._seed_order1(
                self.n,
                source_multiplier,
                self.root,
                self.remainder,
                target_multiplier,
            )
            mode = "SEED_ORDER1"
            self.seed_divisions += 1
        else:
            candidate, gap = slot.candidate_gap(target_multiplier)
            root, remainder, correction = self._close_phase_candidate(candidate, gap)
            mode = "PHASE_RECURRENCE"
            self.recurrent_transitions += 1

        # Low-overhead kernel: exact reconstruction is covered by regression tests.
        # Avoid squaring the large target root on every production step.
        slot.add(target_multiplier, root, remainder)

        self.last_source_multiplier = source_multiplier
        self.multiplier = target_multiplier
        self.root = root
        self.remainder = remainder
        self.last_mode = mode
        self.last_phase_correction = correction
        return root, remainder, target_multiplier

    def advance(self) -> PhaseRootRemainderState:
        self.advance_pair()
        return self.current_state()


def odd_n_phase_root_tail_states(
    n: int,
    start_multiplier: int,
    state_count: int,
) -> tuple[PhaseRootRemainderState, ...]:
    """Return an exact unbounded representative tail including the start state."""
    _require_positive("state_count", state_count)
    tracker = PhaseRootRemainderTracker(n, start_multiplier)
    states = [tracker.current_state()]
    for _ in range(1, state_count):
        states.append(tracker.advance())
    return tuple(states)


def reused_reciprocal_table_bytes() -> int:
    return RECIPROCAL_RAW_BYTES


__all__ = [
    "PHASE_SPACING",
    "PHASE_COUNT",
    "PHASE_SEED_TRANSITIONS",
    "PHASE_THIRD_DIFFERENCE_MIN",
    "PHASE_THIRD_DIFFERENCE_MAX",
    "RECIPROCAL_CORRECTION_CANDIDATE_MIN",
    "PhaseRootRemainderState",
    "PhaseRootRemainderTracker",
    "phase_root_third_difference_bounds",
    "phase_root_candidate_gap",
    "odd_n_phase_root_tail_states",
    "reused_reciprocal_table_bytes",
]
