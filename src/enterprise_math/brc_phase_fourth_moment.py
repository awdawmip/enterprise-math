"""Exact fourth-difference BRC phase transport with lifted moment state.

This module starts earlier than the order-one ``N^(1/5)`` deep tail. On the
stronger fixed-phase condition

    m**7 >= 128*N,

four exact visits to one odd-N mod-8 phase determine a cubic root extrapolation

    C = 4*J3 - 6*J2 + 4*J1 - J0.

Its exact target residual can be evaluated from the four remainders and a lifted
quadratic moment state. The correction e=J4-C is the fourth phase difference
and satisfies

    -347 <= e <= 7.

The existing 1 KiB normalized reciprocal table from the Round-13 phase quotient
tool recovers a negative correction with at most two estimate increments and
one branch between two adjacent candidates. No new table payload is required.

After nineteen direct-root seed transitions (four visits for each of five
phases, with the initial state counting as one), the unbounded stream uses only
the exact phase recurrence. The lifted moments eliminate all unbounded
variable-by-variable products from the recurrent residual update; new
multiplications involve only the bounded correction e and fixed small integers.

This is an exact multiplier-state transport optimization. It does not shorten
the multiplier horizon or change difference-of-squares factor-search complexity.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isqrt

from .brc_linear_deep_tail import (
    next_odd_n_representative_multiplier,
    odd_n_multiplier_is_representative,
)
from .brc_phase_quotient_remainder import (
    RECIPROCAL_FRACTION_BITS,
    RECIPROCAL_INDEX_BITS,
    RECIPROCAL_RAW_BYTES,
    reciprocal_seed_table,
)
from .core import integer_nth_root

PHASE_SPACING = 8
PHASE_COUNT = 5
PHASE_SEED_TRANSITIONS = 19
FOURTH_PHASE_TAIL_FACTOR = 128
PHASE_FOURTH_DIFFERENCE_MIN = -347
PHASE_FOURTH_DIFFERENCE_MAX = 7
# 2*C > d*(d-2) for every d<=347 once C>=59858.
NEGATIVE_RECIPROCAL_CANDIDATE_MIN = 59_858
_PHASE_INDEX = (0, 1, -1, 2, -1, 3, -1, 4)


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def fourth_phase_tail_sufficient(n: int, multiplier: int) -> bool:
    """Return the exact root-free condition ``m**7 >= 128*N``."""
    _require_positive("n", n)
    _require_positive("multiplier", multiplier)
    return multiplier**7 >= FOURTH_PHASE_TAIL_FACTOR * n


def fourth_phase_tail_threshold(n: int) -> int:
    """Smallest integer m satisfying ``m**7 >= 128*N``."""
    _require_positive("n", n)
    target = FOURTH_PHASE_TAIL_FACTOR * n
    root = integer_nth_root(target, 7)
    return root if root**7 == target else root + 1


def aligned_fourth_phase_tail_threshold(n: int) -> int:
    """Smallest odd-N mod-8 representative at or above the fourth-order tail."""
    multiplier = fourth_phase_tail_threshold(n)
    while not odd_n_multiplier_is_representative(multiplier):
        multiplier += 1
    return multiplier


def phase_fourth_difference_bounds() -> tuple[int, int]:
    return PHASE_FOURTH_DIFFERENCE_MIN, PHASE_FOURTH_DIFFERENCE_MAX


def phase_fourth_candidate_gap(
    root0: int,
    remainder0: int,
    root1: int,
    remainder1: int,
    root2: int,
    remainder2: int,
    root3: int,
    remainder3: int,
) -> tuple[int, int]:
    """Return cubic root extrapolation and its exact next-phase residual."""
    values = (
        ("root0", root0),
        ("remainder0", remainder0),
        ("root1", root1),
        ("remainder1", remainder1),
        ("root2", root2),
        ("remainder2", remainder2),
        ("root3", root3),
        ("remainder3", remainder3),
    )
    for name, value in values:
        _require_nonnegative(name, value)
    if (
        remainder0 > 2 * root0
        or remainder1 > 2 * root1
        or remainder2 > 2 * root2
        or remainder3 > 2 * root3
    ):
        raise ValueError("remainder escaped its square-root BRC basin")

    first = root1 - root0
    second = root2 - 2 * root1 + root0
    third = root3 - 3 * root2 + 3 * root1 - root0
    candidate = 4 * root3 - 6 * root2 + 4 * root1 - root0
    quadratic_moment = (
        4 * first * third
        + 3 * second * second
        + 12 * second * third
        + 6 * third * third
    )
    gap = (
        -remainder0
        + 4 * remainder1
        - 6 * remainder2
        + 4 * remainder3
        - 2 * quadratic_moment
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

    def floor_ratio_at_most_346(self, numerator: int, denominator: int) -> int:
        """Exact floor using the existing reciprocal and at most two increments."""
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
            if quotient > 346:
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
                    raise AssertionError("reciprocal deficit exceeded two")
        if estimate > 346:
            raise AssertionError("negative correction quotient escaped proved range")
        return estimate


class _FourthPhaseSlot:
    __slots__ = (
        "count",
        "m0",
        "m1",
        "m2",
        "m3",
        "j0",
        "j1",
        "j2",
        "j3",
        "r0",
        "r1",
        "r2",
        "r3",
        "u",
        "v",
        "w",
        "uw",
        "v2",
        "vw",
        "w2",
    )

    def __init__(self) -> None:
        self.count = 0
        self.m0 = self.m1 = self.m2 = self.m3 = 0
        self.j0 = self.j1 = self.j2 = self.j3 = 0
        self.r0 = self.r1 = self.r2 = self.r3 = 0
        self.u = self.v = self.w = 0
        self.uw = self.v2 = self.vw = self.w2 = 0

    def _check_spacing(self, multiplier: int) -> None:
        if self.count and multiplier != self.m3 + PHASE_SPACING:
            raise ValueError("phase visits must be spaced by eight multipliers")

    def add_seed(self, multiplier: int, root: int, remainder: int) -> None:
        self._check_spacing(multiplier)
        if self.count == 0:
            self.m3, self.j3, self.r3 = multiplier, root, remainder
            self.count = 1
            return
        if self.count == 1:
            self.m2, self.m3 = self.m3, multiplier
            self.j2, self.j3 = self.j3, root
            self.r2, self.r3 = self.r3, remainder
            self.count = 2
            return
        if self.count == 2:
            self.m1, self.m2, self.m3 = self.m2, self.m3, multiplier
            self.j1, self.j2, self.j3 = self.j2, self.j3, root
            self.r1, self.r2, self.r3 = self.r2, self.r3, remainder
            self.count = 3
            return
        if self.count != 3:
            raise AssertionError("seed called after phase became recurrent")

        self.m0, self.m1, self.m2, self.m3 = self.m1, self.m2, self.m3, multiplier
        self.j0, self.j1, self.j2, self.j3 = self.j1, self.j2, self.j3, root
        self.r0, self.r1, self.r2, self.r3 = self.r1, self.r2, self.r3, remainder
        self.count = 4

        self.u = self.j1 - self.j0
        self.v = self.j2 - 2 * self.j1 + self.j0
        self.w = self.j3 - 3 * self.j2 + 3 * self.j1 - self.j0
        self.uw = self.u * self.w
        self.v2 = self.v * self.v
        self.vw = self.v * self.w
        self.w2 = self.w * self.w

    def candidate_gap(self, target_multiplier: int) -> tuple[int, int]:
        if self.count != 4 or target_multiplier != self.m3 + PHASE_SPACING:
            raise ValueError("target is not the next fully seeded phase visit")
        candidate = 4 * self.j3 - 6 * self.j2 + 4 * self.j1 - self.j0
        quadratic_moment = 4 * self.uw + 3 * self.v2 + 12 * self.vw + 6 * self.w2
        gap = (
            -self.r0
            + 4 * self.r1
            - 6 * self.r2
            + 4 * self.r3
            - 2 * quadratic_moment
        )
        return candidate, gap

    def advance(
        self,
        multiplier: int,
        root: int,
        remainder: int,
        correction: int,
    ) -> None:
        self._check_spacing(multiplier)
        if self.count != 4:
            raise AssertionError("phase moment advance before four seeds")

        u, v, w = self.u, self.v, self.w
        old_uw, old_v2, old_vw, old_w2 = self.uw, self.v2, self.vw, self.w2

        self.uw = old_uw + old_vw + correction * (u + v)
        self.v2 = old_v2 + 2 * old_vw + old_w2
        self.vw = old_vw + old_w2 + correction * (v + w)
        self.w2 = old_w2 + 2 * correction * w + correction * correction
        self.u = u + v
        self.v = v + w
        self.w = w + correction

        self.m0, self.m1, self.m2, self.m3 = self.m1, self.m2, self.m3, multiplier
        self.j0, self.j1, self.j2, self.j3 = self.j1, self.j2, self.j3, root
        self.r0, self.r1, self.r2, self.r3 = self.r1, self.r2, self.r3, remainder


@dataclass(frozen=True)
class FourthPhaseMomentState:
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


class FourthPhaseMomentTracker:
    """Exact unbounded phase stream with nineteen direct-root seed transitions."""

    __slots__ = (
        "n",
        "multiplier",
        "root",
        "remainder",
        "_slots",
        "_bucket",
        "seed_root_calls",
        "recurrent_transitions",
        "last_mode",
        "last_phase_correction",
        "last_source_multiplier",
    )

    def __init__(
        self,
        n: int,
        start_multiplier: int | None = None,
        *,
        root: int | None = None,
        remainder: int | None = None,
    ) -> None:
        _require_positive("n", n)
        if n % 2 == 0:
            raise ValueError("fourth-phase tail requires odd n")
        if start_multiplier is None:
            start_multiplier = aligned_fourth_phase_tail_threshold(n)
        _require_positive("start_multiplier", start_multiplier)
        if not odd_n_multiplier_is_representative(start_multiplier):
            raise ValueError("start multiplier must be an odd-N mod-8 representative")
        if not fourth_phase_tail_sufficient(n, start_multiplier):
            raise ValueError("start multiplier is before the fourth-order phase tail")

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
        self._slots = [_FourthPhaseSlot() for _ in range(PHASE_COUNT)]
        self._bucket = _BoundedReciprocalBucket()
        self.seed_root_calls = 0
        self.recurrent_transitions = 0
        self.last_mode = "INITIAL_ROOT"
        self.last_phase_correction = 0
        self.last_source_multiplier = start_multiplier
        self._slots[_PHASE_INDEX[start_multiplier & 7]].add_seed(
            start_multiplier,
            root,
            remainder,
        )

    def current_state(self) -> FourthPhaseMomentState:
        return FourthPhaseMomentState(
            n=self.n,
            multiplier=self.multiplier,
            root=self.root,
            remainder=self.remainder,
            source_multiplier=self.last_source_multiplier,
            mode=self.last_mode,
            phase_correction=self.last_phase_correction,
        )

    def _close_candidate(self, candidate: int, gap: int) -> tuple[int, int, int]:
        if gap >= 0:
            correction = 0
            while gap >= 2 * candidate + 1:
                gap -= 2 * candidate + 1
                candidate += 1
                correction += 1
                if correction > PHASE_FOURTH_DIFFERENCE_MAX:
                    raise AssertionError("positive fourth-phase correction bound failed")
            return candidate, gap, correction

        height = -gap
        if candidate < NEGATIVE_RECIPROCAL_CANDIDATE_MIN:
            decrement = 0
            while height > 0:
                candidate -= 1
                height -= 2 * candidate + 1
                decrement += 1
                if decrement > -PHASE_FOURTH_DIFFERENCE_MIN:
                    raise AssertionError("negative fourth-phase correction bound failed")
            return candidate, -height, -decrement

        quotient = self._bucket.floor_ratio_at_most_346(height, 2 * candidate)
        decrement = quotient + 1
        first_square_drop = decrement * (2 * candidate - decrement)
        if height > first_square_drop:
            decrement += 1
        if decrement > -PHASE_FOURTH_DIFFERENCE_MIN:
            raise AssertionError("negative fourth-phase correction escaped bound")

        remainder = decrement * (2 * candidate - decrement) - height
        candidate -= decrement
        if not 0 <= remainder <= 2 * candidate:
            raise AssertionError("table-assisted fourth-phase closure failed")
        return candidate, remainder, -decrement

    def advance_pair(self) -> tuple[int, int, int]:
        """Advance one retained multiplier and return ``(root,remainder,m)``."""
        source_multiplier = self.multiplier
        target_multiplier = next_odd_n_representative_multiplier(source_multiplier)
        slot = self._slots[_PHASE_INDEX[target_multiplier & 7]]

        if slot.count < 4:
            target = target_multiplier * self.n
            root = isqrt(target)
            remainder = target - root * root
            correction = 0
            mode = "SEED_DIRECT_ROOT"
            slot.add_seed(target_multiplier, root, remainder)
            self.seed_root_calls += 1
        else:
            candidate, gap = slot.candidate_gap(target_multiplier)
            root, remainder, correction = self._close_candidate(candidate, gap)
            mode = "FOURTH_PHASE_RECURRENCE"
            slot.advance(target_multiplier, root, remainder, correction)
            self.recurrent_transitions += 1

        self.last_source_multiplier = source_multiplier
        self.multiplier = target_multiplier
        self.root = root
        self.remainder = remainder
        self.last_mode = mode
        self.last_phase_correction = correction
        return root, remainder, target_multiplier

    def advance(self) -> FourthPhaseMomentState:
        self.advance_pair()
        return self.current_state()


def odd_n_fourth_phase_tail_states(
    n: int,
    start_multiplier: int | None,
    state_count: int,
) -> tuple[FourthPhaseMomentState, ...]:
    """Return an exact unbounded fourth-order phase tail including its start."""
    _require_positive("state_count", state_count)
    tracker = FourthPhaseMomentTracker(n, start_multiplier)
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
    "FOURTH_PHASE_TAIL_FACTOR",
    "PHASE_FOURTH_DIFFERENCE_MIN",
    "PHASE_FOURTH_DIFFERENCE_MAX",
    "NEGATIVE_RECIPROCAL_CANDIDATE_MIN",
    "FourthPhaseMomentState",
    "FourthPhaseMomentTracker",
    "fourth_phase_tail_sufficient",
    "fourth_phase_tail_threshold",
    "aligned_fourth_phase_tail_threshold",
    "phase_fourth_difference_bounds",
    "phase_fourth_candidate_gap",
    "odd_n_fourth_phase_tail_states",
    "reused_reciprocal_table_bytes",
]
