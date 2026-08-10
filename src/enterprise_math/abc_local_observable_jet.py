"""State-relative local interaction order for polynomial rank observables.

For a future node with base old-threshold rank R and c candidate thresholds that
it crosses, the local term is

    y * P(R + x_1 + ... + x_c).

The coefficient attached to y times any k distinct crossed candidate variables
is the k-th forward difference Delta^k P(R).  Hence the realized local response
order depends on the polynomial, the base rank, and the crossed-candidate count,
not just on the global polynomial degree.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb
from typing import Sequence

from .abc_polynomial_rank_observable import normalize_polynomial, polynomial_degree, polynomial_value
from .abc_rank_moment_closure import rational_candidates_between
from .abc_signed_exponent_transport import dyadic_difference_pressure_tower


@dataclass(frozen=True)
class LocalFutureJetProfile:
    coefficients: tuple[Fraction, ...]
    polynomial_degree: int
    base_rank: int
    crossed_candidate_count: int
    forward_differences: tuple[Fraction, ...]
    nonzero_difference_orders: tuple[int, ...]
    realized_action_order: int
    degree_geometry_cap: int


def forward_difference(
    coefficients: Sequence[Fraction], base_rank: int, order: int
) -> Fraction:
    coefficients = normalize_polynomial(coefficients)
    if isinstance(base_rank, bool) or not isinstance(base_rank, int) or base_rank < 0:
        raise ValueError("base_rank must be a non-negative integer")
    if isinstance(order, bool) or not isinstance(order, int) or order < 0:
        raise ValueError("order must be a non-negative integer")
    return sum(
        (
            Fraction((-1) ** (order - t) * comb(order, t), 1)
            * polynomial_value(coefficients, base_rank + t)
        )
        for t in range(order + 1)
    )


def local_future_jet_profile(
    coefficients: Sequence[Fraction], base_rank: int, crossed_candidate_count: int
) -> LocalFutureJetProfile:
    coefficients = normalize_polynomial(coefficients)
    if isinstance(crossed_candidate_count, bool) or not isinstance(crossed_candidate_count, int) or crossed_candidate_count < 0:
        raise ValueError("crossed_candidate_count must be a non-negative integer")
    degree = polynomial_degree(coefficients)
    max_difference_order = min(degree, crossed_candidate_count)
    differences = tuple(
        forward_difference(coefficients, base_rank, k)
        for k in range(max_difference_order + 1)
    )
    nonzero = tuple(k for k, value in enumerate(differences) if value != 0)
    # k crossed candidate variables plus one future-node selector y.
    realized = 0 if not nonzero else max(nonzero) + 1
    return LocalFutureJetProfile(
        coefficients=coefficients,
        polynomial_degree=degree,
        base_rank=base_rank,
        crossed_candidate_count=crossed_candidate_count,
        forward_differences=differences,
        nonzero_difference_orders=nonzero,
        realized_action_order=realized,
        degree_geometry_cap=max_difference_order + 1,
    )


def stage112_arithmetic_cancellation_fixture() -> dict[str, object]:
    """Same quadratic polynomial, different crossed-candidate geometry.

    P(r)=r(r-1).  At base rank R=0, P(0)=P(1)=0 but Delta^2 P(0)=2.
    Therefore a future node crossing only one candidate is invisible to this
    observable, while crossing two candidates activates a genuine cubic response.
    Both configurations are realized inside the same `(3,41)` dyadic edge.
    """
    coefficients = (Fraction(0), Fraction(-1), Fraction(1))
    pressures = dyadic_difference_pressure_tower(3, 41, 2, 1).pressures
    low, high = pressures
    one_candidate = rational_candidates_between(low, high, 1)
    two_candidates = rational_candidates_between(low, high, 2)
    one_profile = local_future_jet_profile(coefficients, 0, len(one_candidate))
    two_profile = local_future_jet_profile(coefficients, 0, len(two_candidates))
    if one_profile.realized_action_order != 0:
        raise AssertionError("one-candidate geometry should be invisible at base rank zero")
    if two_profile.realized_action_order != 3:
        raise AssertionError("two-candidate geometry should realize cubic order")
    return {
        "pressures": pressures,
        "coefficients": coefficients,
        "one_candidate": one_candidate,
        "two_candidates": two_candidates,
        "one_profile": one_profile,
        "two_profile": two_profile,
    }
