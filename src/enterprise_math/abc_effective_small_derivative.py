"""Effective small-derivative normalization by intrinsic certificate index.

Let ``mu`` be the minimum norm of a relation-adapted nondegenerate arithmetic
derivative and let ``eta_min`` be the positive generator of the normalized
Wronskian image.  Since every nonzero Wronskian is a multiple of
``eta_min * M``, the minimum-norm witness satisfies the refined capacity bound

    eta_min * m(c) <= mu * K_ab,

where ``K_ab = rad(a) C(b) + rad(b) C(a)`` and
``C(n)=sum v_p(n) rad(n)/p``.

This motivates the rational effective norm

    mu_eff = mu / eta_min.

A power bound ``mu_eff < c^alpha`` is weaker than the same bound on ``mu`` but
still yields the same Wronskian/radical capacity consequence.  This module
records the exact integer arithmetic of that implication; historical novelty
of the normalization is unverified.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_block_mu import exact_minimum_nondegenerate_witness_radius
from .abc_block_value_lattice import block_value_absorption_floor
from .abc_small_derivative_block import pair_capacity_ab
from .abc_support import abc_support_state, multiplicity_residual, radical


@dataclass(frozen=True)
class EffectiveSmallDerivativeState:
    abc: tuple[int, int, int]
    mu: int
    eta_min: int
    effective_mu: Fraction
    pair_capacity_ab: int
    multiplicity_residual_c: int
    refined_mu_lower_bound: int
    refined_capacity_slack: int


def effective_small_derivative_state(
    a: int, b: int, c: int
) -> EffectiveSmallDerivativeState:
    """Return exact ``mu/eta_min`` and refined intrinsic-capacity lower bound."""
    abc_support_state(a, b, c)
    mu = exact_minimum_nondegenerate_witness_radius(a, b, c).mu
    eta = block_value_absorption_floor(a, b, c)
    capacity = pair_capacity_ab(a, b, c)
    residual_c = multiplicity_residual(c)
    numerator = eta * residual_c
    lower = (numerator + capacity - 1) // capacity
    if mu < lower:
        raise AssertionError("minimum derivative violated certificate-image capacity bound")
    slack = mu * capacity - numerator
    if slack < 0:
        raise AssertionError("refined capacity slack must be nonnegative")
    # Equivalent radical form: eta*c <= mu*rad(c)*K_ab.
    if eta * c > mu * radical(c) * capacity:
        raise AssertionError("refined effective abc capacity inequality failed")
    return EffectiveSmallDerivativeState(
        abc=(a, b, c),
        mu=mu,
        eta_min=eta,
        effective_mu=Fraction(mu, eta),
        pair_capacity_ab=capacity,
        multiplicity_residual_c=residual_c,
        refined_mu_lower_bound=lower,
        refined_capacity_slack=slack,
    )


def rational_effective_small_derivative_bound_holds(
    a: int,
    b: int,
    c: int,
    numerator: int,
    denominator: int,
) -> bool:
    """Decide ``mu/eta_min < c^(numerator/denominator)`` exactly.

    No floating-point exponentiation is used:

        (mu/eta)^q < c^p  <=>  mu^q < eta^q * c^p.
    """
    if (
        isinstance(numerator, bool)
        or not isinstance(numerator, int)
        or isinstance(denominator, bool)
        or not isinstance(denominator, int)
        or not 0 < numerator < denominator
    ):
        raise ValueError("require integers 0 < numerator < denominator")
    state = effective_small_derivative_state(a, b, c)
    return state.mu**denominator < state.eta_min**denominator * c**numerator


def effective_bound_implies_capacity_abc(
    a: int,
    b: int,
    c: int,
    numerator: int,
    denominator: int,
) -> bool:
    """Verify the exact rational-exponent consequence of an effective bound.

    If ``mu/eta < c^(p/q)``, the refined capacity inequality implies

        c^(q-p) < (rad(c)*K_ab)^q.

    Since ``rad(c)*K_ab = rad(abc)*(S_a+S_b)`` for primitive abc, this is the
    exact integer form of the corresponding Wronskian/radical capacity bound.
    The function returns False when the effective small-derivative premise does
    not hold for the supplied triple/exponent.
    """
    if not rational_effective_small_derivative_bound_holds(
        a, b, c, numerator, denominator
    ):
        return False
    state = effective_small_derivative_state(a, b, c)
    right_base = radical(c) * state.pair_capacity_ab
    if not c ** (denominator - numerator) < right_base**denominator:
        raise AssertionError("effective small-derivative implication failed")
    return True
