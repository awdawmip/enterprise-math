"""Canonical one-bit repair for unsafe multiple-collapse precision quotients."""

from __future__ import annotations

from math import gcd

from .division import multiple_collapse
from .p023_precision_compatibility import precision_project


def fiber_phase(coarse: int, ratio: int, divisor: int) -> int:
    """Return (coarse*ratio) mod divisor, the d-boundary phase of one r-fiber."""
    if coarse < 0 or ratio <= 0 or divisor <= 0:
        raise ValueError("coarse must be natural and ratio/divisor positive")
    return (coarse * ratio) % divisor


def fiber_splits(coarse: int, ratio: int, divisor: int) -> bool:
    """Whether one ratio-fiber contains two projected D_divisor outcomes."""
    phase = fiber_phase(coarse, ratio, divisor)
    if phase == 0:
        return False
    threshold = divisor - phase
    return threshold < ratio


def boundary_crossing_bit(n: int, ratio: int, divisor: int) -> int:
    """Minimal binary detail distinguishing the two possible coarse outcomes.

    The bit is nontrivial only when the current ratio-fiber crosses a positive
    multiple of ``divisor`` in its interior.  It records whether ``n`` lies on
    or beyond that boundary.  On a nonsplitting fiber the bit is canonically 0.
    """
    if n < 0 or ratio <= 0 or divisor <= 0:
        raise ValueError("n must be natural and ratio/divisor positive")
    coarse = precision_project(n, ratio)
    phase = fiber_phase(coarse, ratio, divisor)
    if phase == 0:
        return 0
    threshold = divisor - phase
    if threshold >= ratio:
        return 0
    remainder = n - coarse * ratio
    return int(remainder >= threshold)


def repaired_precision_state(n: int, ratio: int, divisor: int) -> tuple[int, int]:
    """Return the canonical one-step repaired state (coarse class, crossing bit)."""
    return precision_project(n, ratio), boundary_crossing_bit(n, ratio, divisor)


def projected_multiple_collapse(n: int, ratio: int, divisor: int) -> int:
    return precision_project(multiple_collapse(n, divisor), ratio)


def repaired_state_determines_output(
    left: int, right: int, ratio: int, divisor: int
) -> bool:
    """Check the descent implication for two fine states."""
    if repaired_precision_state(left, ratio, divisor) != repaired_precision_state(
        right, ratio, divisor
    ):
        return True
    return projected_multiple_collapse(
        left, ratio, divisor
    ) == projected_multiple_collapse(right, ratio, divisor)


def split_fiber_period(ratio: int, divisor: int) -> int:
    """Period of the fiber phase q*ratio mod divisor."""
    if ratio <= 0 or divisor <= 0:
        raise ValueError("ratio and divisor must be positive")
    return divisor // gcd(ratio, divisor)


def split_fibers_per_period(ratio: int, divisor: int) -> int:
    """Exact number of splitting coarse fibers in one phase period.

    The count is min(ratio,divisor)/gcd(ratio,divisor)-1.
    """
    if ratio <= 0 or divisor <= 0:
        raise ValueError("ratio and divisor must be positive")
    g = gcd(ratio, divisor)
    return min(ratio, divisor) // g - 1


def enumerate_split_residues(ratio: int, divisor: int) -> tuple[int, ...]:
    """Coarse q residues that require the nontrivial repair bit."""
    period = split_fiber_period(ratio, divisor)
    return tuple(
        coarse for coarse in range(period) if fiber_splits(coarse, ratio, divisor)
    )
