"""Exact target-family counterexample to one-unit half-defect valuation.

The prime

    p = 369581 = 5 (mod 24),  m=(p-1)/2=184790

lies in the infinite composite-boundary half-index family.  It is a forced
midpoint Franel divisor, but the canonical A-elimination also uses F_8 with
exponent +2.  Since

    F_8 = 739162 = 2*p,
    v_p(F_m)=1,

and no other canonical support index is zero modulo p, the pure defect has

    v_p(D_m)=1-2=-1.

Thus both global support-avoidance and the stronger conjecture v_p(D_m)=+1 are
false even inside the target residue family.  The forced witness survives, but
its valuation direction reverses: it moves from numerator to denominator.
"""

from __future__ import annotations

from .p022_barlow_half_defect_obstructions import (
    half_defect_support_zero_hits,
    half_index_lift_quotient,
)
from .p022_barlow_low_order_defect_reduction import composite_A_relation_exponents
from .p022_barlow_low_order_identifiability import triple_moment_factor

TARGET_COUNTEREXAMPLE_PRIME = 369_581
TARGET_COUNTEREXAMPLE_MIDPOINT = 184_790
TARGET_COUNTEREXAMPLE_EARLIER_INDEX = 8
TARGET_COUNTEREXAMPLE_MIDPOINT_LIFT = 153_310
TARGET_COUNTEREXAMPLE_RELATION: tuple[tuple[int, int], ...] = (
    (1, 3),
    (2, -2),
    (4, 1),
    (5, -1),
    (6, 1),
    (8, 2),
    (9, -2),
    (543, 1),
    (544, -1),
    (8799, -1),
    (8800, 1),
    (184789, 1),
)


def target_counterexample_relation() -> tuple[tuple[int, int], ...]:
    actual = composite_A_relation_exponents(TARGET_COUNTEREXAMPLE_MIDPOINT)
    if actual != TARGET_COUNTEREXAMPLE_RELATION:
        raise AssertionError("target-family counterexample A-relation changed")
    return actual


def target_counterexample_earlier_franel_identity() -> tuple[int, int, int]:
    """Return (F_8,p,F_8/p) and certify F_8=2p."""
    value = triple_moment_factor(TARGET_COUNTEREXAMPLE_EARLIER_INDEX)
    prime = TARGET_COUNTEREXAMPLE_PRIME
    if value != 2 * prime:
        raise AssertionError("F_8 must equal twice the target counterexample prime")
    return value, prime, value // prime


def target_counterexample_support_zero_hits() -> tuple[int, ...]:
    """Exact canonical support indices whose Franel values vanish modulo p."""
    hits = half_defect_support_zero_hits(TARGET_COUNTEREXAMPLE_PRIME)
    if hits != (TARGET_COUNTEREXAMPLE_EARLIER_INDEX,):
        raise AssertionError("only F_8 should contribute p-adic support correction")
    return hits


def target_counterexample_midpoint_lift() -> int:
    """F_m/p mod p; nonzero certifies v_p(F_m)=1."""
    quotient = half_index_lift_quotient(TARGET_COUNTEREXAMPLE_PRIME)
    if quotient != TARGET_COUNTEREXAMPLE_MIDPOINT_LIFT:
        raise AssertionError("target midpoint p^2 lift quotient changed")
    return quotient


def target_counterexample_support_correction() -> int:
    """Exact sum alpha_j*v_p(F_j) over the canonical support."""
    relation = dict(target_counterexample_relation())
    hits = target_counterexample_support_zero_hits()
    correction = 0
    for index in hits:
        # The only hit is F_8=2p, so its valuation is exactly one.
        value, prime, _ = target_counterexample_earlier_franel_identity()
        if value % (prime * prime) == 0:
            raise AssertionError("F_8 must have p-adic valuation exactly one")
        correction += relation[index]
    if correction != 2:
        raise AssertionError("canonical support correction must equal two")
    return correction


def target_counterexample_defect_valuation() -> int:
    """Exact v_p(D_m) reconstructed without forming the gigantic F_m."""
    midpoint_valuation = 1 if target_counterexample_midpoint_lift() else 2
    correction = target_counterexample_support_correction()
    defect = midpoint_valuation - correction
    if defect != -1:
        raise AssertionError("target-family defect valuation must reverse to -1")
    return defect


def target_counterexample_profile() -> tuple[int, int, int, int, int]:
    """Return (p,m,alpha_8,v_p(F_m),v_p(D_m))."""
    relation = dict(target_counterexample_relation())
    defect = target_counterexample_defect_valuation()
    return (
        TARGET_COUNTEREXAMPLE_PRIME,
        TARGET_COUNTEREXAMPLE_MIDPOINT,
        relation[TARGET_COUNTEREXAMPLE_EARLIER_INDEX],
        1,
        defect,
    )
