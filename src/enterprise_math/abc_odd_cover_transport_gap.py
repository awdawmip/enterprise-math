"""Cyclotomic spectral gap for odd-prime exponent-cover transport.

For an odd cover prime r, the new quotient is Phi_r(p^m,q^m) on a difference
edge and Phi_{2r}(p^m,q^m) on a same-sign sum edge.  The exceptional prime r
can occur only on the support-resonant locus and then only to valuation one.
Every other repeated quotient prime s gives exact root order r or 2r and hence

    s == 1 (mod 2r).

Consequently the quotient multiplicity residual satisfies

    m(Q) = 1  or  m(Q) >= 2r+1.

Combining this with Stage 87 gives a qualitative transport classifier requiring
only two bits: ancestor support resonance and quotient squarefreeness.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_odd_prime_cover_transport import odd_prime_cover_transport_state
from .abc_support import prime_factorization


@dataclass(frozen=True)
class OddCoverTransportGapState:
    q: int
    p: int
    lower_exponent: int
    cover_prime: int
    mode: str
    support_resonance: bool
    quotient_squarefree: bool
    quotient_residual: int
    repeated_quotient_primes: tuple[int, ...]
    repeated_support_floor: int
    inheritance_multiplier: Fraction
    transport_class: str
    two_bit_classifier: tuple[bool, bool]


def odd_cover_transport_gap_state(
    q: int,
    p: int,
    lower_exponent: int,
    cover_prime: int,
    mode: str,
) -> OddCoverTransportGapState:
    """Return the exact two-bit qualitative transport state and spectral gap."""
    cover = odd_prime_cover_transport_state(
        q, p, lower_exponent, cover_prime, mode
    )
    r = cover_prime
    factorization = prime_factorization(cover.quotient_component)
    repeated = tuple(prime for prime, exponent in factorization if exponent >= 2)

    for prime, exponent in factorization:
        if prime == r:
            if exponent > 1:
                raise AssertionError("exceptional cover prime must remain simple in quotient")
            continue
        if exponent >= 2 and prime % (2 * r) != 1:
            raise AssertionError("repeated quotient support escaped 1 mod 2r")

    squarefree = len(repeated) == 0
    residual = cover.quotient_residual
    if squarefree != (residual == 1):
        raise AssertionError("quotient squarefree bit disagreed with residual")
    floor = 2 * r + 1
    if not squarefree and residual < floor:
        raise AssertionError("nonsquarefree quotient lost 2r+1 residual floor")

    if squarefree:
        expected_class = "resonant" if cover.resonance_support else "attenuated"
        expected_multiplier = Fraction(1, 1) if cover.resonance_support else Fraction(1, r)
        if cover.inheritance_multiplier != expected_multiplier:
            raise AssertionError("squarefree quotient lost exact gap multiplier")
    else:
        expected_class = "amplified"
        if cover.resonance_support:
            if cover.inheritance_multiplier < floor:
                raise AssertionError("resonant repeated quotient lost amplification gap")
        else:
            if cover.inheritance_multiplier < Fraction(floor, r):
                raise AssertionError("nonresonant repeated quotient lost amplification gap")

    if cover.transport_class != expected_class:
        raise AssertionError("two-bit classifier disagreed with exact transport class")

    return OddCoverTransportGapState(
        q=q,
        p=p,
        lower_exponent=lower_exponent,
        cover_prime=r,
        mode=mode,
        support_resonance=cover.resonance_support,
        quotient_squarefree=squarefree,
        quotient_residual=residual,
        repeated_quotient_primes=repeated,
        repeated_support_floor=floor,
        inheritance_multiplier=cover.inheritance_multiplier,
        transport_class=expected_class,
        two_bit_classifier=(cover.resonance_support, squarefree),
    )
