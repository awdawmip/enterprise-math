"""Exact fifth-difference BRC phase transport with lifted moments.

On the root-free fixed-phase condition

    m**9 >= 2**17 * N,

five exact visits to one odd-N mod-8 phase determine the quartic extrapolation

    C = 5*J4 - 10*J3 + 10*J2 - 5*J1 + J0.

The exact target residual is a signed remainder jet plus a quadratic form in
the first four root differences. Six lifted moments update using only
additions, fixed small coefficients, and multiplication by the bounded fifth
correction. The correction satisfies

    -15 <= e = J5-C <= 312.

The existing Round-13 1 KiB normalized reciprocal table closes the dominant
non-negative case with at most one estimate increment and one residual sign
test. No new table payload is required.

After twenty-four direct-root seed transitions, the unbounded representative
stream performs exact fifth-order phase transport with no further target square
roots and no multiplication between independently unbounded dynamic variables.

This is a state-transport optimization. It does not shorten the multiplier
horizon or change difference-of-squares factor-search complexity.
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
PHASE_SEED_TRANSITIONS = 24
FIFTH_PHASE_TAIL_FACTOR = 1 << 17
PHASE_FIFTH_DIFFERENCE_MIN = -15
PHASE_FIFTH_DIFFERENCE_MAX = 312
# 2*C+1 > 312*313-1 once C>=48828.
POSITIVE_RECIPROCAL_CANDIDATE_MIN = 48_828
_PHASE_INDEX = (0, 1, -1, 2, -1, 3, -1, 4)


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def fifth_phase_tail_sufficient(n: int, multiplier: int) -> bool:
    """Return the exact root-free condition ``m**9 >= 2**17*N``."""
    _require_positive("n", n)
    _require_positive("multiplier", multiplier)
    return multiplier**9 >= FIFTH_PHASE_TAIL_FACTOR * n


def fifth_phase_tail_threshold(n: int) -> int:
    """Smallest integer m satisfying the fifth-order tail condition."""
    _require_positive("n", n)
    target = FIFTH_PHASE_TAIL_FACTOR * n
    root = integer_nth_root(target, 9)
    return root if root**9 == target else root + 1


def aligned_fifth_phase_tail_threshold(n: int) -> int:
    """Smallest odd-N mod-8 representative at or above the fifth-order tail."""
    multiplier = fifth_phase_tail_threshold(n)
    while not odd_n_multiplier_is_representative(multiplier):
        multiplier += 1
    return multiplier


def phase_fifth_difference_bounds() -> tuple[int, int]:
    return PHASE_FIFTH_DIFFERENCE_MIN, PHASE_FIFTH_DIFFERENCE_MAX


def phase_fifth_candidate_gap(
    root0: int,
    remainder0: int,
    root1: int,
    remainder1: int,
    root2: int,
    remainder2: int,
    root3: int,
    remainder3: int,
    root4: int,
    remainder4: int,
) -> tuple[int, int]:
    """Return quartic root extrapolation and its exact next-phase residual."""
    values = (
        ("root0", root0),
        ("remainder0", remainder0),
        ("root1", root1),
        ("remainder1", remainder1),
        ("root2", root2),
        ("remainder2", remainder2),
        ("root3", root3),
        ("remainder3", remainder3),
        ("root4", root4),
        ("remainder4", remainder4),
    )
    for name, value in values:
        _require_nonnegative(name, value)
    if (
        remainder0 > 2 * root0
        or remainder1 > 2 * root1
        or remainder2 > 2 * root2
        or remainder3 > 2 * root3
        or remainder4 > 2 * root4
    ):
        raise ValueError("remainder escaped its square-root BRC basin")

    u = root1 - root0
    v = root2 - 2 * root1 + root0
    w = root3 - 3 * root2 + 3 * root1 - root0
    z = root4 - 4 * root3 + 6 * root2 - 4 * root1 + root0
    candidate = 5 * root4 - 10 * root3 + 10 * root2 - 5 * root1 + root0
    quadratic_moment = (
        u * z
        + 2 * v * w
        + 4 * v * z
        + 3 * w * w
        + 6 * w * z
        + 2 * z * z
    )
    gap = (
        remainder0
        - 5 * remainder1
        + 10 * remainder2
        - 10 * remainder3
        + 5 * remainder4
        - 10 * quadratic_moment
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

    def floor_ratio_at_most_313(self, numerator: int, denominator: int) -> int:
        """Exact floor using the existing lower reciprocal and <=1 increment."""
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
            if quotient > 313:
                raise AssertionError("small-denominator quotient escaped proved range")
            return quotient

        estimate = (
            numerator * self.reciprocal
        ) >> (RECIPROCAL_FRACTION_BITS + self.shift)
        if numerator >= (estimate + 1) * denominator:
            estimate += 1
            if numerator >= (estimate + 1) * denominator:
                raise AssertionError("reciprocal deficit exceeded one")
        if estimate > 313:
            raise AssertionError("fifth-phase quotient escaped proved range")
        return estimate


class _FifthPhaseSlot:
    __slots__ = (
        "count",
        "m0",
        "m1",
        "m2",
        "m3",
        "m4",
        "j0",
        "j1",
        "j2",
        "j3",
        "j4",
        "r0",
        "r1",
        "r2",
        "r3",
        "r4",
        "u",
        "v",
        "w",
        "z",
        "uz",
        "vw",
        "vz",
        "w2",
        "wz",
        "z2",
    )

    def __init__(self) -> None:
        self.count = 0
        self.m0 = self.m1 = self.m2 = self.m3 = self.m4 = 0
        self.j0 = self.j1 = self.j2 = self.j3 = self.j4 = 0
        self.r0 = self.r1 = self.r2 = self.r3 = self.r4 = 0
        self.u = self.v = self.w = self.z = 0
        self.uz = self.vw = self.vz = self.w2 = self.wz = self.z2 = 0

    def _check_spacing(self, multiplier: int) -> None:
        if self.count and multiplier != self.m4 + PHASE_SPACING:
            raise ValueError("phase visits must be spaced by eight multipliers")

    def add_seed(self, multiplier: int, root: int, remainder: int) -> None:
        self._check_spacing(multiplier)
        if self.count == 0:
            self.m4, self.j4, self.r4 = multiplier, root, remainder
            self.count = 1
            return
        if self.count == 1:
            self.m3, self.m4 = self.m4, multiplier
            self.j3, self.j4 = self.j4, root
            self.r3, self.r4 = self.r4, remainder
            self.count = 2
            return
        if self.count == 2:
            self.m2, self.m3, self.m4 = self.m3, self.m4, multiplier
            self.j2, self.j3, self.j4 = self.j3, self.j4, root
            self.r2, self.r3, self.r4 = self.r3, self.r4, remainder
            self.count = 3
            return
        if self.count == 3:
            self.m1, self.m2, self.m3, self.m4 = (
                self.m2,
                self.m3,
                self.m4,
                multiplier,
            )
            self.j1, self.j2, self.j3, self.j4 = self.j2, self.j3, self.j4, root
            self.r1, self.r2, self.r3, self.r4 = self.r2, self.r3, self.r4, remainder
            self.count = 4
            return
        if self.count != 4:
            raise AssertionError("seed called after phase became recurrent")

        self.m0, self.m1, self.m2, self.m3, self.m4 = (
            self.m1,
            self.m2,
            self.m3,
            self.m4,
            multiplier,
        )
        self.j0, self.j1, self.j2, self.j3, self.j4 = (
            self.j1,
            self.j2,
            self.j3,
            self.j4,
            root,
        )
        self.r0, self.r1, self.r2, self.r3, self.r4 = (
            self.r1,
            self.r2,
            self.r3,
            self.r4,
            remainder,
        )
        self.count = 5

        self.u = self.j1 - self.j0
        self.v = self.j2 - 2 * self.j1 + self.j0
        self.w = self.j3 - 3 * self.j2 + 3 * self.j1 - self.j0
        self.z = self.j4 - 4 * self.j3 + 6 * self.j2 - 4 * self.j1 + self.j0
        self.uz = self.u * self.z
        self.vw = self.v * self.w
        self.vz = self.v * self.z
        self.w2 = self.w * self.w
        self.wz = self.w * self.z
        self.z2 = self.z * self.z

    def candidate_gap(self, target_multiplier: int) -> tuple[int, int]:
        if self.count != 5 or target_multiplier != self.m4 + PHASE_SPACING:
            raise ValueError("target is not the next fully seeded phase visit")
        candidate = (
            5 * self.j4
            - 10 * self.j3
            + 10 * self.j2
            - 5 * self.j1
            + self.j0
        )
        quadratic_moment = (
            self.uz
            + 2 * self.vw
            + 4 * self.vz
            + 3 * self.w2
            + 6 * self.wz
            + 2 * self.z2
        )
        gap = (
            self.r0
            - 5 * self.r1
            + 10 * self.r2
            - 10 * self.r3
            + 5 * self.r4
            - 10 * quadratic_moment
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
        if self.count != 5:
            raise AssertionError("phase moment advance before five seeds")

        u, v, w, z = self.u, self.v, self.w, self.z
        uz, vw, vz = self.uz, self.vw, self.vz
        w2, wz, z2 = self.w2, self.wz, self.z2

        self.uz = uz + vz + correction * (u + v)
        self.vw = vw + vz + w2 + wz
        self.vz = vz + wz + correction * (v + w)
        self.w2 = w2 + 2 * wz + z2
        self.wz = wz + z2 + correction * (w + z)
        self.z2 = z2 + 2 * correction * z + correction * correction
        self.u = u + v
        self.v = v + w
        self.w = w + z
        self.z = z + correction

        self.m0, self.m1, self.m2, self.m3, self.m4 = (
            self.m1,
            self.m2,
            self.m3,
            self.m4,
            multiplier,
        )
        self.j0, self.j1, self.j2, self.j3, self.j4 = (
            self.j1,
            self.j2,
            self.j3,
            self.j4,
            root,
        )
        self.r0, self.r1, self.r2, self.r3, self.r4 = (
            self.r1,
            self.r2,
            self.r3,
            self.r4,
            remainder,
        )


@dataclass(frozen=True)
class FifthPhaseMomentState:
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


class FifthPhaseMomentTracker:
    """Exact unbounded phase stream with twenty-four direct-root seeds."""

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
            raise ValueError("fifth-phase tail requires odd n")
        if start_multiplier is None:
            start_multiplier = aligned_fifth_phase_tail_threshold(n)
        _require_positive("start_multiplier", start_multiplier)
        if not odd_n_multiplier_is_representative(start_multiplier):
            raise ValueError("start multiplier must be an odd-N mod-8 representative")
        if not fifth_phase_tail_sufficient(n, start_multiplier):
            raise ValueError("start multiplier is before the fifth-order phase tail")

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
        self._slots = [_FifthPhaseSlot() for _ in range(PHASE_COUNT)]
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

    def current_state(self) -> FifthPhaseMomentState:
        return FifthPhaseMomentState(
            n=self.n,
            multiplier=self.multiplier,
            root=self.root,
            remainder=self.remainder,
            source_multiplier=self.last_source_multiplier,
            mode=self.last_mode,
            phase_correction=self.last_phase_correction,
        )

    def _close_candidate(self, candidate: int, gap: int) -> tuple[int, int, int]:
        if gap < 0:
            decrement = 0
            while gap < 0:
                candidate -= 1
                gap += 2 * candidate + 1
                decrement += 1
                if decrement > -PHASE_FIFTH_DIFFERENCE_MIN:
                    raise AssertionError("negative fifth-phase correction bound failed")
            return candidate, gap, -decrement

        if candidate < POSITIVE_RECIPROCAL_CANDIDATE_MIN:
            correction = 0
            while gap >= 2 * candidate + 1:
                gap -= 2 * candidate + 1
                candidate += 1
                correction += 1
                if correction > PHASE_FIFTH_DIFFERENCE_MAX:
                    raise AssertionError("positive fifth-phase correction bound failed")
            return candidate, gap, correction

        width = 2 * candidate + 1
        quotient = self._bucket.floor_ratio_at_most_313(gap, width)
        residual = gap - quotient * (2 * candidate + quotient)
        if residual < 0:
            residual += 2 * candidate + 2 * quotient - 1
            quotient -= 1

        candidate += quotient
        if (
            not PHASE_FIFTH_DIFFERENCE_MIN
            <= quotient
            <= PHASE_FIFTH_DIFFERENCE_MAX
            or not 0 <= residual <= 2 * candidate
        ):
            raise AssertionError("table-assisted fifth-phase closure failed")
        return candidate, residual, quotient

    def advance_pair(self) -> tuple[int, int, int]:
        """Advance one retained multiplier and return ``(root,remainder,m)``."""
        source_multiplier = self.multiplier
        target_multiplier = next_odd_n_representative_multiplier(source_multiplier)
        slot = self._slots[_PHASE_INDEX[target_multiplier & 7]]

        if slot.count < 5:
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
            mode = "FIFTH_PHASE_RECURRENCE"
            slot.advance(target_multiplier, root, remainder, correction)
            self.recurrent_transitions += 1

        self.last_source_multiplier = source_multiplier
        self.multiplier = target_multiplier
        self.root = root
        self.remainder = remainder
        self.last_mode = mode
        self.last_phase_correction = correction
        return root, remainder, target_multiplier

    def advance(self) -> FifthPhaseMomentState:
        self.advance_pair()
        return self.current_state()


def odd_n_fifth_phase_tail_states(
    n: int,
    start_multiplier: int | None,
    state_count: int,
) -> tuple[FifthPhaseMomentState, ...]:
    """Return an exact unbounded fifth-order phase tail including its start."""
    _require_positive("state_count", state_count)
    tracker = FifthPhaseMomentTracker(n, start_multiplier)
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
    "FIFTH_PHASE_TAIL_FACTOR",
    "PHASE_FIFTH_DIFFERENCE_MIN",
    "PHASE_FIFTH_DIFFERENCE_MAX",
    "POSITIVE_RECIPROCAL_CANDIDATE_MIN",
    "FifthPhaseMomentState",
    "FifthPhaseMomentTracker",
    "fifth_phase_tail_sufficient",
    "fifth_phase_tail_threshold",
    "aligned_fifth_phase_tail_threshold",
    "phase_fifth_difference_bounds",
    "phase_fifth_candidate_gap",
    "odd_n_fifth_phase_tail_states",
    "reused_reciprocal_table_bytes",
]
