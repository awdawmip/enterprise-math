"""First-activation normal form for monotone dyadic P025 pressure orbits.

For fixed odd primes p>q and base exponent m>=2, Supplement 86 gives

    rho_{2^(j+1)m,-} = rho_{2^j m,-} * u_j,

where every u_j=m(p^(2^j m)+q^(2^j m)) is a positive integer.  Therefore the
threshold profile [rho_j >= T] on any finite dyadic horizon is an upward-closed
suffix.  It is represented exactly by one first-activation depth j_T (or None
when the threshold is never reached).

This module stores the exact finite normal form and reconstruction.  It does not
claim generic monotone-threshold compression as new mathematics.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_signed_exponent_transport import (
    dyadic_difference_pressure_tower,
    signed_doubling_transport_state,
)


@dataclass(frozen=True)
class DyadicActivationNormalForm:
    q: int
    p: int
    base_exponent: int
    horizon_steps: int
    threshold: Fraction
    exponents: tuple[int, ...]
    pressures: tuple[Fraction, ...]
    activation_profile: tuple[bool, ...]
    first_activation_depth: int | None
    first_activation_exponent: int | None
    profile_state_count: int
    unconstrained_boolean_state_count: int
    suffix_verified: bool


def _require_threshold(threshold: Fraction) -> None:
    if not isinstance(threshold, Fraction) or threshold <= 0:
        raise ValueError("threshold must be a positive Fraction")


def suffix_profile_from_first_depth(
    horizon_steps: int, first_depth: int | None
) -> tuple[bool, ...]:
    """Reconstruct the unique upward-closed Boolean profile on depths 0..h."""
    if isinstance(horizon_steps, bool) or not isinstance(horizon_steps, int) or horizon_steps < 0:
        raise ValueError("horizon_steps must be a non-negative integer")
    if first_depth is None:
        return (False,) * (horizon_steps + 1)
    if isinstance(first_depth, bool) or not isinstance(first_depth, int) or not 0 <= first_depth <= horizon_steps:
        raise ValueError("first_depth must lie in 0..horizon_steps or be None")
    return tuple(depth >= first_depth for depth in range(horizon_steps + 1))


def dyadic_activation_normal_form(
    q: int,
    p: int,
    base_exponent: int,
    horizon_steps: int,
    threshold: Fraction = Fraction(1, 1),
) -> DyadicActivationNormalForm:
    """Return the exact first-threshold-crossing normal form on a dyadic tower."""
    _require_threshold(threshold)
    tower = dyadic_difference_pressure_tower(
        q, p, base_exponent, horizon_steps
    )
    profile = tuple(value >= threshold for value in tower.pressures)
    first = next((index for index, active in enumerate(profile) if active), None)
    reconstructed = suffix_profile_from_first_depth(horizon_steps, first)
    if profile != reconstructed:
        raise AssertionError("dyadic activation profile is not an upward-closed suffix")

    first_exponent = tower.exponents[first] if first is not None else None
    return DyadicActivationNormalForm(
        q=q,
        p=p,
        base_exponent=base_exponent,
        horizon_steps=horizon_steps,
        threshold=threshold,
        exponents=tower.exponents,
        pressures=tower.pressures,
        activation_profile=profile,
        first_activation_depth=first,
        first_activation_exponent=first_exponent,
        profile_state_count=horizon_steps + 2,
        unconstrained_boolean_state_count=1 << (horizon_steps + 1),
        suffix_verified=True,
    )


def signed_seed_activation_bound(
    q: int,
    p: int,
    base_exponent: int,
    threshold: Fraction = Fraction(1, 1),
) -> dict[str, Fraction | bool | int | None]:
    """Record how an active base sum/difference bounds first difference activation.

    Supplement 86 gives rho_{2m,-}>=max(rho_{m,-},rho_{m,+}).  Hence if either
    base sign is already above T, the dyadic difference first-activation depth is
    at most one; if the base difference is active, the depth is exactly zero.
    """
    _require_threshold(threshold)
    edge = signed_doubling_transport_state(q, p, base_exponent)
    minus_active = edge.lower_difference_ratio >= threshold
    plus_active = edge.lower_sum_ratio >= threshold
    doubled_active = edge.upper_difference_ratio >= threshold
    if (minus_active or plus_active) and not doubled_active:
        raise AssertionError("signed doubling lost active seed pressure")
    upper_bound: int | None
    if minus_active:
        upper_bound = 0
    elif plus_active:
        upper_bound = 1
    else:
        upper_bound = None
    return {
        "lower_difference_pressure": edge.lower_difference_ratio,
        "lower_sum_pressure": edge.lower_sum_ratio,
        "doubled_difference_pressure": edge.upper_difference_ratio,
        "lower_difference_active": minus_active,
        "lower_sum_active": plus_active,
        "doubled_difference_active": doubled_active,
        "first_difference_activation_depth_upper_bound": upper_bound,
    }
