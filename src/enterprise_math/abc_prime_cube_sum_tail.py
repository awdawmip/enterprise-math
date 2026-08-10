"""Finite radical/residual split behind the P025 (3,3) cube-sum tail.

On P/2<B<=P, cube-sum threshold T implies

    m(E) >= T*rad(B),   E=B^2+3A^2 <=4P^2.

Split at a radical horizon H.  If rad(B)<H, dyadic size forces
m(B)>P/(2H), so the center values are counted by the elementary large-residual
union bound.  If rad(B)>=H, then m(E)>=T*H and the quadratic-factor values are
counted by the same bound; classical Eisenstein norm representation contributes
only a divisor-function P^epsilon factor.  H around sqrt(P/T) balances both
branches at P^(7/4+epsilon)T^(-1/4).
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_prime_cube_difference_tail import (
    ceil_sqrt,
    large_residual_integer_union_bound,
)


@dataclass(frozen=True)
class CubeSumTailSplit:
    center_height: int
    threshold: int
    radical_horizon: int
    center_residual_threshold: int
    quadratic_residual_threshold: int
    center_value_union_bound: int
    quadratic_value_union_bound: int


def balanced_cube_sum_split(center_height: int, threshold: int) -> CubeSumTailSplit:
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
    if T > P:
        raise ValueError("balanced sum split is scoped to 1<=T<=P")

    # H ~ sqrt(P/T), implemented without floating point.
    ratio_ceiling = (P + T - 1) // T
    H = max(1, ceil_sqrt(ratio_ceiling))

    # If B>P/2 and rad(B)<H then m(B)>P/(2H).
    center_threshold = P // (2 * H) + 1
    quadratic_threshold = T * H
    center_values = large_residual_integer_union_bound(P, center_threshold)
    quadratic_values = large_residual_integer_union_bound(
        4 * P * P, quadratic_threshold
    )
    return CubeSumTailSplit(
        center_height=P,
        threshold=T,
        radical_horizon=H,
        center_residual_threshold=center_threshold,
        quadratic_residual_threshold=quadratic_threshold,
        center_value_union_bound=center_values,
        quadratic_value_union_bound=quadratic_values,
    )


def cube_sum_tail_power_profile() -> dict[str, tuple[int, int]]:
    return {
        "center_height_power": (7, 4),
        "threshold_power": (-1, 4),
    }
