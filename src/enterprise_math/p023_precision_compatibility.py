"""Arithmetic compatibility examples for P023 using P007/P018 operations."""

from __future__ import annotations

from .division import integer_quotient, multiple_collapse


def precision_project(n: int, ratio: int) -> int:
    """Project a fine integer state through a positive integer precision ratio."""
    return integer_quotient(n, ratio)


def projected_quotient(n: int, ratio: int, divisor: int) -> int:
    """Project after exact quotient."""
    return precision_project(integer_quotient(n, divisor), ratio)


def quotient_on_projected_state(n: int, ratio: int, divisor: int) -> int:
    """Apply the same quotient to the already projected coarse state."""
    return integer_quotient(precision_project(n, ratio), divisor)


def quotient_projection_commutes(n: int, ratio: int, divisor: int) -> bool:
    """Q_ratio(Q_divisor(n)) = Q_divisor(Q_ratio(n))."""
    return projected_quotient(n, ratio, divisor) == quotient_on_projected_state(
        n, ratio, divisor
    )


def multiple_collapse_induced_state(coarse: int, ratio: int, divisor: int) -> int:
    """Return the induced coarse multiple-collapse state in the safe regimes.

    If divisor divides ratio, the fine multiple collapse stays inside the same
    ratio-block and induces the identity on coarse classes.

    If ratio divides divisor, divisor = ratio*s and the induced coarse map is
    the same-space multiple collapse D_s.
    """
    if ratio <= 0 or divisor <= 0:
        raise ValueError("ratio and divisor must be positive")
    if ratio % divisor == 0:
        return coarse
    if divisor % ratio == 0:
        return multiple_collapse(coarse, divisor // ratio)
    raise ValueError("multiple collapse does not descend through this projection")


def multiple_collapse_projection_compatible(ratio: int, divisor: int) -> bool:
    """Compatibility classification: exactly divisibility-comparable parameters."""
    if ratio <= 0 or divisor <= 0:
        raise ValueError("ratio and divisor must be positive")
    return ratio % divisor == 0 or divisor % ratio == 0


def incompatible_multiple_collapse_witness(
    ratio: int, divisor: int
) -> tuple[int, int] | None:
    """Return two states in one precision fiber with different coarse outcomes.

    Returns ``None`` exactly in the compatible regimes.
    """
    if ratio <= 0 or divisor <= 0:
        raise ValueError("ratio and divisor must be positive")
    if multiple_collapse_projection_compatible(ratio, divisor):
        return None
    if divisor < ratio:
        left = ratio
        right = (ratio // divisor + 1) * divisor
    else:
        left = divisor - 1
        right = divisor
    if precision_project(left, ratio) != precision_project(right, ratio):
        raise AssertionError("constructed states must share one precision fiber")
    left_out = precision_project(multiple_collapse(left, divisor), ratio)
    right_out = precision_project(multiple_collapse(right, divisor), ratio)
    if left_out == right_out:
        raise AssertionError("constructed witness must separate coarse outcomes")
    return left, right
