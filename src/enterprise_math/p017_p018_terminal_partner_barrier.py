"""Terminal low-core residuals leave the S<k mirror hard core.

Let ``J=J_perp(k)>0`` be even and work at terminal order ``m=J-1``.  A low
terminal residual signed state has exactly J transverse small-prime directions
and complete transverse core ``C_x<k``.

Its mirror partner at the same radius is anchor-surviving as well.  Therefore:

* if the partner has empty transverse support, it is a prime in the original
  square basin and we already have a witness;
* if the partner is composite, its transverse support is nonempty and is
  disjoint from the J-prime support of the residual side (P017 centered-mirror
  separation).  Hence the union contains at least J+1 distinct transverse
  primes.

By maximality of J, the product ``P_perp(k,J+1)`` of the first J+1 transverse
odd primes is at least k.  Thus for a composite partner

    rad(C_x) * rad(C_partner) >= P_perp(k,J+1) >= k,

and therefore also

    C_x * C_partner >= k.

So a terminal low-core residual can never remain inside the two-large-tail
``S=C_x*C_partner<k`` residual hard core under the prime-free branch.  Every
such row routes either directly to a basin-prime witness or to the high-product
mirror region.  This is a bridge/dichotomy theorem, not a Legendre proof.
"""

from __future__ import annotations

from math import prod

from .cutoff_pairing import transverse_prime_support
from .legendre import anchor_product, is_prime
from .p017_p018_core_adaptive_bonferroni import complete_transverse_core
from .p017_p018_near_primorial_shell import near_primorial_replacement_profile


def _squarefree_radical_from_support(support: tuple[int, ...]) -> int:
    return prod(support) if support else 1


def terminal_residual_partner_dichotomy(
    k: int,
    signed_point: int,
) -> dict[str, object]:
    """Route one declared terminal residual row to PRIME_WITNESS or HIGH_PRODUCT."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if (
        isinstance(signed_point, bool)
        or not isinstance(signed_point, int)
        or signed_point == 0
        or abs(signed_point) >= k
    ):
        raise ValueError("signed_point must be a nonzero signed radius with |x|<k")

    profile = near_primorial_replacement_profile(k)
    j = int(profile["transverse_primorial_depth"])
    if j <= 0 or profile["J_parity"] != "EVEN":
        raise ValueError("terminal partner dichotomy requires positive even J_perp(k)")

    center = k * (k + 1)
    anchor = anchor_product(k)
    if __import__("math").gcd(abs(signed_point), center) != 1:
        raise ValueError("signed point must survive the anchor sieve")

    state = center - signed_point
    partner = center + signed_point
    support = tuple(transverse_prime_support(state, k, anchor))
    if len(support) != j:
        raise ValueError("declared residual side must have exactly J transverse support primes")
    core = complete_transverse_core(state, support)
    if core >= k:
        raise ValueError("declared terminal residual side must have complete core < k")

    partner_support = tuple(transverse_prime_support(partner, k, anchor))
    if not partner_support:
        if not is_prime(partner):
            raise AssertionError("empty partner transverse support was not a basin prime")
        return {
            "k": k,
            "signed_point": signed_point,
            "state": state,
            "complete_core": core,
            "support": support,
            "partner": partner,
            "partner_support": (),
            "partner_is_prime": True,
            "route": "PRIME_WITNESS",
            "transverse_primorial_next": int(profile["next_transverse_prime"])
            * int(profile["base_primorial_product"]),
        }

    if set(support).intersection(partner_support):
        raise AssertionError("mirror transverse supports are not disjoint")
    partner_core = complete_transverse_core(partner, partner_support)
    support_radical = _squarefree_radical_from_support(support)
    partner_radical = _squarefree_radical_from_support(partner_support)
    next_primorial = int(profile["next_transverse_prime"]) * int(
        profile["base_primorial_product"]
    )
    pair_radical_product = support_radical * partner_radical
    pair_core_product = core * partner_core

    if pair_radical_product < next_primorial:
        raise AssertionError("J+1 disjoint transverse primes fell below the next primorial")
    if next_primorial < k:
        raise AssertionError("maximality of J failed to put P_{J+1} at or above k")
    if pair_core_product < pair_radical_product:
        raise AssertionError("complete-core product fell below its squarefree radical")

    return {
        "k": k,
        "signed_point": signed_point,
        "state": state,
        "complete_core": core,
        "support": support,
        "partner": partner,
        "partner_support": partner_support,
        "partner_complete_core": partner_core,
        "partner_is_prime": False,
        "support_radical": support_radical,
        "partner_support_radical": partner_radical,
        "pair_support_radical_product": pair_radical_product,
        "pair_complete_core_product": pair_core_product,
        "transverse_primorial_next": next_primorial,
        "route": "HIGH_PRODUCT",
        "outside_residual_S_lt_k_hard_core": pair_core_product >= k,
    }
