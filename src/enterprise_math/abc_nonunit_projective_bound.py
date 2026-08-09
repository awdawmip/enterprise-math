"""Elementary radical bound for the explicit projective resource on nonunit abc.

For every n>1,

    rad(n) * S(n) = sum_{p|n} v_p(n) rad(n)/p

is a positive integer, hence ``S(n)>=1/rad(n)``.

If all three abc blocks are nonunit, each cyclic weighted-radical defect obeys

    rho_i <= c / (2*sqrt(rad(abc))).

The implementation verifies the equivalent exact squared inequality

    4 * sigma_proj^2 * rad(abc) <= c^2.

Thus an Oesterle power bound ``c < R^M`` would directly imply a projective
power saving with exponent ``1-1/(2M)`` on the nonunit slice, without invoking
the geometry-of-numbers small-derivative reverse implication.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_projective_capacity_condition import projective_capacity_condition_state
from .abc_support import abc_support_state, radical


@dataclass(frozen=True)
class NonunitProjectiveBound:
    abc: tuple[int, int, int]
    radical_product: int
    sigma_projective: Fraction
    squared_bound_left: Fraction
    squared_bound_right: int
    cyclic_elementary_bounds: tuple[Fraction, Fraction, Fraction]


def nonunit_projective_bound(a: int, b: int, c: int) -> NonunitProjectiveBound:
    """Verify the exact elementary nonunit projective/radical bound."""
    abc_support_state(a, b, c)
    if min(a, b, c) <= 1:
        raise ValueError("nonunit projective bound requires a,b,c>1")
    state = projective_capacity_condition_state(a, b, c)
    R_a, R_b, R_c = (radical(n) for n in (a, b, c))
    R = R_a * R_b * R_c
    # S(j)+S(k) >= 1/R_j + 1/R_k, giving exact rational
    # rho_i <= n_i / [R_i(R_j+R_k)].
    bounds = (
        Fraction(c, R_c * (R_a + R_b)),
        Fraction(b, R_b * (R_a + R_c)),
        Fraction(a, R_a * (R_b + R_c)),
    )
    for defect, bound in zip(state.cyclic_weighted_defects, bounds, strict=True):
        if defect > bound:
            raise AssertionError("support-load lower bound failed cyclic projective defect")
    sigma = state.sigma_projective
    left = 4 * sigma * sigma * R
    right = c * c
    if left > right:
        raise AssertionError("nonunit sigma <= c/(2 sqrt R) failed")
    return NonunitProjectiveBound(
        abc=(a, b, c),
        radical_product=R,
        sigma_projective=sigma,
        squared_bound_left=left,
        squared_bound_right=right,
        cyclic_elementary_bounds=bounds,
    )


def oesterle_to_nonunit_projective_eta_threshold(M: Fraction) -> Fraction:
    """Return ``1-1/(2M)`` from ``c<R^M`` to the nonunit PCC exponent."""
    if not isinstance(M, Fraction) or M <= 1:
        raise ValueError("M must be a rational exponent > 1")
    return Fraction(1, 1) - Fraction(1, 1) / (2 * M)
