"""Pairwise integer-dispersion tools for P019 square-layer contraction.

The main observable is

    P(x_1,...,x_N) = sum_{i<j} (x_i-x_j)^2,

which satisfies P = N*sum(x_i^2) - (sum x_i)^2 and admits an exact
fraction-free merge recursion driven by the contraction imbalance tag.
"""

from __future__ import annotations

from .contraction_trace import square_split_imbalance


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def _require_integer_tuple(name: str, values: tuple[int, ...]) -> None:
    if not isinstance(values, tuple) or not values:
        raise ValueError(f"{name} must be a non-empty tuple")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in values):
        raise ValueError(f"{name} entries must be integers")


def pair_dispersion(values: tuple[int, ...]) -> int:
    """Return sum_{i<j}(x_i-x_j)^2 using integers only."""
    _require_integer_tuple("values", values)
    return sum(
        (values[i] - values[j]) ** 2
        for i in range(len(values))
        for j in range(i + 1, len(values))
    )


def pair_dispersion_identity(values: tuple[int, ...]) -> tuple[int, int]:
    """Return both sides of P=N*sum(x_i^2)-(sum x_i)^2."""
    _require_integer_tuple("values", values)
    direct = pair_dispersion(values)
    total = sum(values)
    algebraic = len(values) * sum(value * value for value in values) - total * total
    return direct, algebraic


def merge_pair_dispersion_identity(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[int, int]:
    """Return both sides of the fraction-free two-block merge law.

    For block sizes m,n, total size M, and z=n*a-m*b:

        m*n*P_parent = n*M*P_left + m*M*P_right + z^2.
    """
    _require_integer_tuple("left", left)
    _require_integer_tuple("right", right)
    m = len(left)
    n = len(right)
    total_size = m + n
    left_total = sum(left)
    right_total = sum(right)
    imbalance = square_split_imbalance(m, n, left_total, right_total)
    left_side = m * n * pair_dispersion(left + right)
    right_side = (
        n * total_size * pair_dispersion(left)
        + m * total_size * pair_dispersion(right)
        + imbalance * imbalance
    )
    return left_side, right_side


def reassociate_imbalances(
    left_size: int,
    middle_size: int,
    right_size: int,
    left_middle_imbalance: int,
    parent_imbalance: int,
) -> tuple[int, int]:
    """Rotate `((A,B),C)` to `(A,(B,C))` using imbalance tags only.

    If `u=n*a-m*b` and `v=k*(a+b)-(m+n)*c`, the rotated tags satisfy

        (m+n)u' = n*v-k*u
        (m+n)v' = (m+n+k)u+m*v.

    Legal tags make both divisions exact.
    """
    _require_positive("left_size", left_size)
    _require_positive("middle_size", middle_size)
    _require_positive("right_size", right_size)
    _require_integer("left_middle_imbalance", left_middle_imbalance)
    _require_integer("parent_imbalance", parent_imbalance)

    denominator = left_size + middle_size
    total_size = denominator + right_size
    middle_right_numerator = (
        middle_size * parent_imbalance
        - right_size * left_middle_imbalance
    )
    rotated_parent_numerator = (
        total_size * left_middle_imbalance
        + left_size * parent_imbalance
    )
    if (
        middle_right_numerator % denominator != 0
        or rotated_parent_numerator % denominator != 0
    ):
        raise ValueError("imbalance tags are incompatible with the requested tree rotation")
    return (
        middle_right_numerator // denominator,
        rotated_parent_numerator // denominator,
    )


def reassociation_quadratic_identity(
    left_size: int,
    middle_size: int,
    right_size: int,
    left_middle_imbalance: int,
    parent_imbalance: int,
) -> tuple[int, int]:
    """Return both sides of the fraction-free quadratic invariant under rotation."""
    middle_right_imbalance, rotated_parent_imbalance = reassociate_imbalances(
        left_size,
        middle_size,
        right_size,
        left_middle_imbalance,
        parent_imbalance,
    )
    total_size = left_size + middle_size + right_size
    old_weighted = (
        right_size * total_size * left_middle_imbalance**2
        + left_size * middle_size * parent_imbalance**2
    )
    new_weighted = (
        left_size * total_size * middle_right_imbalance**2
        + middle_size * right_size * rotated_parent_imbalance**2
    )
    left_side = (middle_size + right_size) * old_weighted
    right_side = (left_size + middle_size) * new_weighted
    return left_side, right_side


def zero_sum_quadratic_separation(values: tuple[int, ...]) -> int:
    """Recover q=(1/2)sum x_i^2 from pair dispersion for a zero-sum state.

    The exact relation is P=2*N*q. The integer division below is exact on the
    declared zero-sum integer domain.
    """
    _require_integer_tuple("values", values)
    if sum(values) != 0:
        raise ValueError("values must have zero total")
    divisor = 2 * len(values)
    dispersion = pair_dispersion(values)
    if dispersion % divisor != 0:
        raise AssertionError("zero-sum integer pair dispersion must be divisible by 2N")
    return dispersion // divisor
