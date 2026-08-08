"""General precision-borrow identity for reductive integer operations (P023)."""

from __future__ import annotations

from .core import collapse
from .division import division_gap, multiple_collapse
from .p023_precision_compatibility import precision_project


def reductive_gap(n: int, transformed: int) -> int:
    """Return n-transformed for an explicitly supplied reductive result."""
    if n < 0 or transformed < 0 or transformed > n:
        raise ValueError("require natural transformed <= n")
    return n - transformed


def precision_borrow_from_gap(n: int, transformed: int, ratio: int) -> int:
    """Number of coarse ratio-blocks lost by a reductive transformation.

    If n=q*ratio+t and G=n-transformed, then

        borrow = ceil((G-t)/ratio)

    represented without true division as

        (G-t+ratio-1)//ratio.

    Because 0<=t<ratio and G>=0, this value is always a natural integer.
    """
    if ratio <= 0:
        raise ValueError("ratio must be positive")
    gap = reductive_gap(n, transformed)
    coarse = precision_project(n, ratio)
    detail = n - coarse * ratio
    return (gap - detail + ratio - 1) // ratio


def projected_reductive_identity(n: int, transformed: int, ratio: int) -> tuple[int, int, int]:
    """Return (coarse_before, borrow, coarse_after) and verify q_after=q-borrow."""
    coarse = precision_project(n, ratio)
    borrow = precision_borrow_from_gap(n, transformed, ratio)
    after = precision_project(transformed, ratio)
    if after != coarse - borrow:
        raise AssertionError("precision-borrow identity failed")
    return coarse, borrow, after


def multiple_collapse_borrow(n: int, ratio: int, divisor: int) -> int:
    """Borrow count for P007 same-space multiple collapse D_divisor."""
    transformed = multiple_collapse(n, divisor)
    return precision_borrow_from_gap(n, transformed, ratio)


def power_collapse_borrow(n: int, ratio: int, exponent: int) -> int:
    """Borrow count for perfect-power collapse C_exponent."""
    transformed = collapse(n, exponent)
    return precision_borrow_from_gap(n, transformed, ratio)


def power_collapse_gap(n: int, exponent: int) -> int:
    """P002-style perfect-power collapse gap n-C_p(n)."""
    return n - collapse(n, exponent)


def multiple_collapse_gap(n: int, divisor: int) -> int:
    """P007 Euclidean gap, exposed for the common reductive-borrow formula."""
    return division_gap(n, divisor)
