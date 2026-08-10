"""Local transport law for odd-prime exponent covers m -> r*m.

Let r be an odd prime and set X=p^m, Y=q^m.  For differences,

    Q = (X^r-Y^r)/(X-Y),

and for same-sign sums (r odd),

    Q = (X^r+Y^r)/(X+Y).

In both cases the elementary congruence Q == r*Y^(r-1) modulo the ancestor
(up to an irrelevant sign) gives

    gcd(ancestor,Q) = gcd(ancestor,r).

If r divides the ancestor, LTE gives v_r(Q)=1.  Thus the radical-overlap factor
Gamma is exactly r on the resonance locus and 1 off it.  The cover multiplier is

    Lambda = m(Q)       if r | ancestor,
             m(Q) / r   otherwise.

This explains the attenuation/resonance/amplification trichotomy of Stage 84.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd

from .abc_exponent_pressure_inheritance import exponent_pressure_inheritance_state
from .abc_support import multiplicity_residual, prime_factorization, radical
from .legendre import is_prime


@dataclass(frozen=True)
class OddPrimeCoverTransportState:
    q: int
    p: int
    lower_exponent: int
    cover_prime: int
    upper_exponent: int
    mode: str
    ancestor_component: int
    quotient_component: int
    upper_component: int
    resonance_support: bool
    ancestor_quotient_gcd: int
    quotient_cover_prime_valuation: int
    overlap_factor: int
    quotient_residual: int
    inheritance_multiplier: Fraction
    normalization_cancelled: bool
    transport_class: str


def _valuation_from_factorization(n: int, prime: int) -> int:
    return next((e for r, e in prime_factorization(n) if r == prime), 0)


def odd_prime_cover_transport_state(
    q: int,
    p: int,
    lower_exponent: int,
    cover_prime: int,
    mode: str,
) -> OddPrimeCoverTransportState:
    """Compile one odd-prime Hasse cover and its exact resonance law."""
    if isinstance(cover_prime, bool) or not isinstance(cover_prime, int) or cover_prime < 3 or cover_prime % 2 == 0 or not is_prime(cover_prime):
        raise ValueError("cover_prime must be an odd prime")
    if isinstance(lower_exponent, bool) or not isinstance(lower_exponent, int) or lower_exponent < 2:
        raise ValueError("lower_exponent must be an integer >=2")
    if mode not in {"difference", "sum"}:
        raise ValueError("mode must be 'sum' or 'difference'")

    upper = lower_exponent * cover_prime
    inheritance = exponent_pressure_inheritance_state(
        q, p, lower_exponent, upper, mode
    )
    ancestor = inheritance.lower_component
    quotient = inheritance.quotient_component
    high = inheritance.upper_component

    resonance = ancestor % cover_prime == 0
    expected_gcd = cover_prime if resonance else 1
    actual_gcd = gcd(ancestor, quotient)
    if actual_gcd != expected_gcd:
        raise AssertionError("odd-prime cover gcd escaped gcd(ancestor,r) law")

    qvaluation = _valuation_from_factorization(quotient, cover_prime)
    if resonance:
        if qvaluation != 1:
            raise AssertionError("LTE resonance prime must enter the new quotient exactly once")
    elif qvaluation != 0:
        raise AssertionError("nonresonant cover prime unexpectedly entered quotient")

    gamma_numerator = radical(ancestor) * radical(quotient)
    gamma = gamma_numerator // radical(high)
    if gamma != expected_gcd:
        raise AssertionError("odd-prime cover radical overlap disagreed with gcd law")

    qres = multiplicity_residual(quotient)
    expected_multiplier = Fraction(qres, 1) if resonance else Fraction(qres, cover_prime)
    if inheritance.inheritance_multiplier != expected_multiplier:
        raise AssertionError("odd-prime local cover formula disagreed with inheritance law")

    return OddPrimeCoverTransportState(
        q=q,
        p=p,
        lower_exponent=lower_exponent,
        cover_prime=cover_prime,
        upper_exponent=upper,
        mode=mode,
        ancestor_component=ancestor,
        quotient_component=quotient,
        upper_component=high,
        resonance_support=resonance,
        ancestor_quotient_gcd=actual_gcd,
        quotient_cover_prime_valuation=qvaluation,
        overlap_factor=gamma,
        quotient_residual=qres,
        inheritance_multiplier=expected_multiplier,
        normalization_cancelled=resonance,
        transport_class=inheritance.transport_class,
    )


def cover_resonance_congruence_holds(state: OddPrimeCoverTransportState) -> bool:
    """Verify resonance is exactly x^m=+/-1 modulo the cover prime."""
    r = state.cover_prime
    x = state.p * pow(state.q, -1, r) % r
    value = pow(x, state.lower_exponent, r)
    if state.mode == "difference":
        expected = value == 1
    else:
        expected = value == r - 1
    if expected != state.resonance_support:
        raise AssertionError("cover resonance lost ratio congruence criterion")
    return True
