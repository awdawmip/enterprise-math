"""Finite residual-count calculus behind the P025 (3,3) cube-difference tail.

On a dyadic centered range P/2<B<=P, projective threshold T implies

    m(A) * m(D) >= T*B > T*P/2,
    D = A^2 + 3B^2 <= 4P^2.

Split at an integer H.  The radius branch m(A)>=H is counted by the elementary
large-square-divisor union bound.  The other branch has

    m(D) > T*P/(2H).

The same union bound counts candidate D values; the classical Eisenstein norm
representation bound contributes only a divisor-function P^epsilon factor.
Balancing H around sqrt(TP) yields the formal shell scale
P^(7/4+epsilon) T^(-1/4).

This module records exact finite residual union bounds and split parameters.  It
does not implement the external/classical divisor-function asymptotic.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt


@dataclass(frozen=True)
class CubeDifferenceTailSplit:
    center_height: int
    threshold: int
    split_horizon: int
    radius_residual_threshold: int
    quadratic_residual_threshold: int
    radius_value_union_bound: int
    quadratic_value_union_bound: int


def ceil_sqrt(n: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    root = isqrt(n)
    return root if root * root == n else root + 1


def large_residual_integer_union_bound(height: int, residual_threshold: int) -> int:
    """Return the exact square-divisor union bound for ``m(n)>=threshold``.

    If ``m(n)>=Y`` then the largest square-divisor root q2(n) satisfies
    ``q2(n)^2>=Y``.  Therefore n is divisible by some d^2 with
    ``d>=ceil_sqrt(Y)``.  Summing ``floor(height/d^2)`` gives a valid finite
    upper bound, with possible overcounting allowed.
    """
    if isinstance(height, bool) or not isinstance(height, int) or height < 1:
        raise ValueError("height must be a positive integer")
    if (
        isinstance(residual_threshold, bool)
        or not isinstance(residual_threshold, int)
        or residual_threshold < 1
    ):
        raise ValueError("residual_threshold must be a positive integer")
    lower = ceil_sqrt(residual_threshold)
    upper = isqrt(height)
    if lower > upper:
        return 0
    return sum(height // (d * d) for d in range(lower, upper + 1))


def balanced_cube_difference_split(center_height: int, threshold: int) -> CubeDifferenceTailSplit:
    """Return the exact finite split using ``H=ceil_sqrt(T*P)``.

    The quadratic branch uses the strict inequality
    ``m(D)>T*P/(2H)`` and therefore the integer threshold
    ``floor(T*P/(2H))+1``.
    """
    if (
        isinstance(center_height, bool)
        or not isinstance(center_height, int)
        or center_height < 2
    ):
        raise ValueError("center_height must be an integer >=2")
    if isinstance(threshold, bool) or not isinstance(threshold, int) or threshold < 1:
        raise ValueError("threshold must be an integer >=1")
    P = center_height
    T = threshold
    H = ceil_sqrt(T * P)
    quadratic_threshold = (T * P) // (2 * H) + 1
    radius_values = large_residual_integer_union_bound(P, H)
    quadratic_values = large_residual_integer_union_bound(4 * P * P, quadratic_threshold)
    return CubeDifferenceTailSplit(
        center_height=P,
        threshold=T,
        split_horizon=H,
        radius_residual_threshold=H,
        quadratic_residual_threshold=quadratic_threshold,
        radius_value_union_bound=radius_values,
        quadratic_value_union_bound=quadratic_values,
    )


def cube_difference_tail_power_profile() -> dict[str, tuple[int, int]]:
    """Return formal powers of the balanced asymptotic tail.

    ``P^(7/4+epsilon) * T^(-1/4)`` is represented by rational exponent pairs.
    """
    return {
        "center_height_power": (7, 4),
        "threshold_power": (-1, 4),
    }
