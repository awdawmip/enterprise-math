"""Exact phase-wise quotient/remainder transport for the order-1 BRC tail.

On the certified odd-N deep tail, the order-1 increment is

    q_h(m) = floor(2*h*J_m / (4*m+h)),  h in {1,2}.

For each source residue in the exact mod-8 representative stream, h is fixed and
that residue returns every eight multipliers.  The smooth envelope of q_h has a
bounded second difference on the common tail 4*m**5 >= N.  After floor/root
noise is included, the exact integer second difference lies in [-3,99].

Therefore each of the five phases needs only two seed divmods.  Later quotients
are predicted by second-order linear extrapolation and corrected inside a fixed
103-value range.  A 10-bit normalized reciprocal table (512 logical entries,
1024 raw bytes at 16 bits/entry) determines every non-negative correction to
within at most one, followed by one exact comparison.  Negative corrections are
only -1,-2,-3 and need at most two comparisons.

This removes the full-size per-step quotient division mathematically.  It is a
large-integer stream optimization, not a factorization theorem.
"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

from .brc_linear_deep_tail import (
    common_mod8_linear_tail_sufficient,
    next_odd_n_representative_multiplier,
    odd_n_multiplier_is_representative,
)

RECIPROCAL_INDEX_BITS = 10
RECIPROCAL_FRACTION_BITS = 20
RECIPROCAL_TABLE_ENTRIES = 1 << (RECIPROCAL_INDEX_BITS - 1)
RECIPROCAL_RAW_BYTES = 2 * RECIPROCAL_TABLE_ENTRIES
PHASE_SECOND_DIFFERENCE_MIN = -3
PHASE_SECOND_DIFFERENCE_MAX = 99
_PHASE_INDEX = (0, 1, -1, 2, -1, 3, -1, 4)


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def phase_second_difference_bounds(step: int) -> tuple[int, int]:
    """Proved integer bounds for one fixed mod-8 phase on the common tail."""
    if step == 1:
        return PHASE_SECOND_DIFFERENCE_MIN, 51
    if step == 2:
        return PHASE_SECOND_DIFFERENCE_MIN, PHASE_SECOND_DIFFERENCE_MAX
    raise ValueError("step must be 1 or 2")


@lru_cache(maxsize=1)
def reciprocal_seed_table() -> tuple[int, ...]:
    """Return lower reciprocal seeds for normalized 10-bit denominators.

    Entry ``u-512`` is floor(2^20/(u+1)) for 512<=u<=1023.  Using u+1 makes
    the seed a lower reciprocal for every denominator in that mantissa bucket.
    Every value fits in 16 bits, so the logical raw payload is 1024 bytes.
    """
    scale = 1 << RECIPROCAL_FRACTION_BITS
    start = 1 << (RECIPROCAL_INDEX_BITS - 1)
    stop = 1 << RECIPROCAL_INDEX_BITS
    table = tuple(scale // (u + 1) for u in range(start, stop))
    if any(not 0 <= value < (1 << 16) for value in table):
        raise AssertionError("reciprocal seed escaped 16-bit payload")
    return table


@dataclass
class _ReciprocalBucket:
    shift: int | None = None
    lower: int = 0
    upper: int = 0
    reciprocal: int = 0

    def _refresh(self, denominator: int) -> None:
        bits = denominator.bit_length()
        if bits < RECIPROCAL_INDEX_BITS:
            self.shift = -1
            self.lower = 0
            self.upper = 1 << RECIPROCAL_INDEX_BITS
            self.reciprocal = 0
            return
        shift = bits - RECIPROCAL_INDEX_BITS
        u = denominator >> shift
        start = 1 << (RECIPROCAL_INDEX_BITS - 1)
        self.shift = shift
        self.lower = u << shift
        self.upper = (u + 1) << shift
        self.reciprocal = reciprocal_seed_table()[u - start]

    def nonnegative_floor(self, numerator: int, denominator: int) -> int:
        """Return floor(numerator/denominator) for the proved 0..99 range.

        The table estimate is a lower bound and differs from the exact quotient
        by at most one.  One comparison closes the result exactly.
        """
        if numerator < 0:
            raise ValueError("numerator must be non-negative")
        if numerator == 0:
            return 0
        if (
            self.shift is None
            or denominator < self.lower
            or denominator >= self.upper
        ):
            self._refresh(denominator)
        if self.shift == -1:
            return numerator // denominator
        estimate = (
            numerator * self.reciprocal
        ) >> (RECIPROCAL_FRACTION_BITS + self.shift)
        if numerator >= (estimate + 1) * denominator:
            estimate += 1
        return estimate


@dataclass
class _PhaseSlot:
    count: int = 0
    older_root: int = 0
    previous_root: int = 0
    older_quotient: int = 0
    previous_quotient: int = 0
    older_remainder: int = 0
    previous_remainder: int = 0

    def seed(self, root: int, quotient: int, remainder: int) -> None:
        if self.count == 0:
            self.previous_root = root
            self.previous_quotient = quotient
            self.previous_remainder = remainder
            self.count = 1
            return
        if self.count == 1:
            self.older_root, self.previous_root = self.previous_root, root
            self.older_quotient, self.previous_quotient = (
                self.previous_quotient,
                quotient,
            )
            self.older_remainder, self.previous_remainder = (
                self.previous_remainder,
                remainder,
            )
            self.count = 2
            return
        raise AssertionError("seed called after phase became recurrent")

    def advance(self, root: int, quotient: int, remainder: int) -> None:
        self.older_root, self.previous_root = self.previous_root, root
        self.older_quotient, self.previous_quotient = (
            self.previous_quotient,
            quotient,
        )
        self.older_remainder, self.previous_remainder = (
            self.previous_remainder,
            remainder,
        )


@dataclass(frozen=True)
class PhaseQuotientResult:
    quotient: int
    remainder: int
    correction: int
    mode: str


class PhaseQuotientRemainderTracker:
    """Five-phase exact tracker for ``divmod(2*h*J,4*m+h)``.

    The tracker is valid on the common order-1 deep tail and expects calls in
    increasing exact odd-N mod-8 representative order.  Each phase uses two
    direct seed divmods; later calls use the exact phase recurrence.

    ``divide_pair`` is the low-overhead kernel.  ``divide`` wraps the same result
    with diagnostic mode/correction metadata for research and testing.
    """

    def __init__(self, n: int) -> None:
        _require_positive("n", n)
        if n % 2 == 0:
            raise ValueError("phase quotient tracker requires odd n")
        self.n = n
        self._slots = [_PhaseSlot() for _ in range(5)]
        self._bucket = _ReciprocalBucket()
        self._last_multiplier = 0
        self.last_mode = "UNUSED"
        self.last_correction = 0

    @staticmethod
    def _negative_correction(rho: int, denominator: int) -> int:
        magnitude = -rho
        if magnitude <= denominator:
            return -1
        if magnitude <= 2 * denominator:
            return -2
        return -3

    def _validate_call(self, root: int, multiplier: int, step: int) -> int:
        _require_positive("multiplier", multiplier)
        if isinstance(root, bool) or not isinstance(root, int) or root < 0:
            raise ValueError("root must be a non-negative integer")
        if step not in (1, 2):
            raise ValueError("step must be 1 or 2")
        if not odd_n_multiplier_is_representative(multiplier):
            raise ValueError("multiplier must lie in the odd-N representative set")
        if next_odd_n_representative_multiplier(multiplier) - multiplier != step:
            raise ValueError("step does not match the exact mod-8 representative stream")
        if not common_mod8_linear_tail_sufficient(self.n, multiplier):
            raise ValueError("multiplier is before the common order-1 deep tail")
        if self._last_multiplier and multiplier <= self._last_multiplier:
            raise ValueError("tracker calls must use increasing multipliers")
        self._last_multiplier = multiplier
        phase_index = _PHASE_INDEX[multiplier & 7]
        if phase_index < 0:
            raise AssertionError("representative multiplier mapped to no phase")
        return phase_index

    def divide_pair(self, root: int, multiplier: int, step: int) -> tuple[int, int]:
        """Return exact quotient/remainder with only seed divmods after warmup."""
        phase_index = self._validate_call(root, multiplier, step)
        slot = self._slots[phase_index]
        denominator = 4 * multiplier + step
        numerator = 2 * step * root

        if slot.count < 2:
            quotient, remainder = divmod(numerator, denominator)
            slot.seed(root, quotient, remainder)
            self.last_mode = "SEED_DIVMOD"
            self.last_correction = 0
            return quotient, remainder

        predicted = 2 * slot.previous_quotient - slot.older_quotient
        rho = (
            2 * step * (root - 2 * slot.previous_root + slot.older_root)
            + 2 * slot.previous_remainder
            - slot.older_remainder
            + 64 * (slot.older_quotient - slot.previous_quotient)
        )

        if rho < 0:
            correction = self._negative_correction(rho, denominator)
        else:
            correction = self._bucket.nonnegative_floor(rho, denominator)

        lower, upper = phase_second_difference_bounds(step)
        if not lower <= correction <= upper:
            raise AssertionError("phase second-difference theorem failed")

        quotient = predicted + correction
        remainder = rho - correction * denominator
        if not 0 <= remainder < denominator:
            raise AssertionError("phase quotient/remainder transport failed")

        slot.advance(root, quotient, remainder)
        self.last_mode = "PHASE_RECURRENCE"
        self.last_correction = correction
        return quotient, remainder

    def divide(self, root: int, multiplier: int, step: int) -> PhaseQuotientResult:
        quotient, remainder = self.divide_pair(root, multiplier, step)
        return PhaseQuotientResult(
            quotient,
            remainder,
            self.last_correction,
            self.last_mode,
        )


__all__ = [
    "RECIPROCAL_INDEX_BITS",
    "RECIPROCAL_FRACTION_BITS",
    "RECIPROCAL_TABLE_ENTRIES",
    "RECIPROCAL_RAW_BYTES",
    "PHASE_SECOND_DIFFERENCE_MIN",
    "PHASE_SECOND_DIFFERENCE_MAX",
    "PhaseQuotientResult",
    "PhaseQuotientRemainderTracker",
    "phase_second_difference_bounds",
    "reciprocal_seed_table",
]
