"""Explicit weighted-radical form of the projective Wronskian resource.

For primitive ``a+b=c`` define

    S(n) = sum_{p|n} v_p(n)/p,
    R    = rad(abc).

Supplement 43's projective optimum simplifies exactly to

    sigma_proj = max(
        c / (R*(S(a)+S(b))),
        b / (R*(S(a)+S(c))),
        a / (R*(S(b)+S(c))),
    ).

Thus the weakest homogeneous Wronskian-capacity resource discovered so far is
an explicit factor/valuation quantity: no witness optimization remains.

A power-saving hypothesis ``sigma_proj < c^eta`` still implies the same
Oesterle-type abc estimate through the c-oriented term.  Conversely, Pasten's
published Oesterle->Small-Derivatives theorem implies the corresponding
projective condition because

    sigma_proj <= mu/eta_min <= mu.

The external implication is prior art; this module stores only the exact
weighted-radical arithmetic and pointwise comparisons.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_block_value_lattice import block_value_absorption_floor
from .abc_projective_efficiency import projective_wronskian_efficiency
from .abc_support import abc_support_state, prime_factorization, radical
from .abc_block_mu import exact_minimum_nondegenerate_witness_radius


@dataclass(frozen=True)
class ProjectiveCapacityConditionState:
    abc: tuple[int, int, int]
    radical_product: int
    support_loads: tuple[Fraction, Fraction, Fraction]
    cyclic_weighted_defects: tuple[Fraction, Fraction, Fraction]
    sigma_projective: Fraction
    effective_mu: Fraction
    ordinary_mu: int


def support_log_derivative_load(n: int) -> Fraction:
    """Return ``S(n)=sum v_p(n)/p`` exactly."""
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    return sum((Fraction(exponent, prime) for prime, exponent in prime_factorization(n)), Fraction(0, 1))


def projective_capacity_condition_state(
    a: int, b: int, c: int
) -> ProjectiveCapacityConditionState:
    """Return the explicit cyclic weighted-radical projective state."""
    abc_support_state(a, b, c)
    loads = tuple(support_log_derivative_load(n) for n in (a, b, c))
    S_a, S_b, S_c = loads
    R = radical(a) * radical(b) * radical(c)
    denominators = (S_a + S_b, S_a + S_c, S_b + S_c)
    if any(value <= 0 for value in denominators):
        raise ValueError("each cyclic pair must contain nontrivial support")
    defects = (
        Fraction(c, 1) / (R * denominators[0]),
        Fraction(b, 1) / (R * denominators[1]),
        Fraction(a, 1) / (R * denominators[2]),
    )
    sigma = max(defects)
    independent = projective_wronskian_efficiency(a, b, c).sigma_projective
    if sigma != independent:
        raise AssertionError("weighted-radical formula disagrees with projective LP formula")
    mu = exact_minimum_nondegenerate_witness_radius(a, b, c).mu
    eta_min = block_value_absorption_floor(a, b, c)
    effective = Fraction(mu, eta_min)
    if sigma > effective or effective > mu:
        raise AssertionError("projective <= effective <= ordinary resource chain failed")
    return ProjectiveCapacityConditionState(
        abc=(a, b, c),
        radical_product=R,
        support_loads=loads,
        cyclic_weighted_defects=defects,
        sigma_projective=sigma,
        effective_mu=effective,
        ordinary_mu=mu,
    )


def rational_projective_capacity_bound_holds(
    a: int,
    b: int,
    c: int,
    numerator: int,
    denominator: int,
) -> bool:
    """Decide ``sigma_proj < c^(p/q)`` with exact integer/rational powers."""
    if (
        isinstance(numerator, bool)
        or not isinstance(numerator, int)
        or isinstance(denominator, bool)
        or not isinstance(denominator, int)
        or not 0 < numerator < denominator
    ):
        raise ValueError("require integers 0 < numerator < denominator")
    sigma = projective_capacity_condition_state(a, b, c).sigma_projective
    return sigma.numerator**denominator < sigma.denominator**denominator * c**numerator


def projective_bound_implies_capacity_abc(
    a: int,
    b: int,
    c: int,
    numerator: int,
    denominator: int,
) -> bool:
    """Verify the exact c-oriented capacity consequence of a projective bound."""
    if not rational_projective_capacity_bound_holds(
        a, b, c, numerator, denominator
    ):
        return False
    state = projective_capacity_condition_state(a, b, c)
    S_a, S_b, _S_c = state.support_loads
    # sigma >= c/(R*(S_a+S_b)); combine with sigma < c^(p/q).
    left = c ** (denominator - numerator)
    weighted = state.radical_product * (S_a + S_b)
    # Avoid floats: left^(1/q) < weighted is equivalent to
    # c^(q-p) < weighted^q.
    if not Fraction(left, 1) < weighted**denominator:
        raise AssertionError("projective power bound failed weighted-radical consequence")
    return True
