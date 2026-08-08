"""Anchor-surviving transverse-support closure for P017 large-modulus hits.

L039 already identifies the unique square-basin hit of every modulus d>=2k.
This module keeps only the additional support-closure question: after a
square-free product of transverse small primes hits, does the half-scale
cofactor introduce any new transverse prime?

The smooth-closure equivalence is asserted only for anchor-surviving hits.
"""

from __future__ import annotations

from math import gcd

from .cutoff_pairing import distinct_prime_factors, transverse_prime_support
from .legendre import anchor_product, interior_hit_count, primes_up_to


def _require_k(k: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")


def transverse_primes(k: int) -> list[int]:
    """Return primes p<=k that do not divide the square-basin center k(k+1)."""
    _require_k(k)
    center = k * (k + 1)
    return [p for p in primes_up_to(k) if center % p != 0]


def _validate_support(k: int, support: list[int]) -> list[int]:
    _require_k(k)
    if not support or len(support) != len(set(support)):
        raise ValueError("support must be a nonempty list of distinct primes")
    allowed = set(transverse_primes(k))
    normalized = sorted(support)
    if any(p not in allowed for p in normalized):
        raise ValueError("every support prime must be transverse and <= k")
    return normalized


def common_center_large_hit(k: int, modulus: int) -> dict[str, int] | None:
    """Executable L039 common-center hit for the strict large-modulus range d>2k."""
    _require_k(k)
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 2 * k:
        raise ValueError("modulus must be an integer > 2k")

    center = k * (k + 1)
    residue = center % modulus
    if residue < k:
        offset = -residue
    elif residue >= modulus - k:
        offset = modulus - residue
    else:
        if interior_hit_count(k, modulus, 2) != 0:
            raise AssertionError("L039 residue miss disagrees with direct hit count")
        return None

    state = center + offset
    if not (k * k < state < (k + 1) * (k + 1)):
        raise AssertionError("L039 hit escaped the open square basin")
    if state % modulus != 0:
        raise AssertionError("L039 hit is not divisible by modulus")
    if interior_hit_count(k, modulus, 2) != 1:
        raise AssertionError("L039 residue hit disagrees with direct hit count")

    cofactor = state // modulus
    half_scale = (k + 1) // 2
    if cofactor > half_scale:
        raise AssertionError("strict d>2k hit violated the L016 half-scale bound")

    return {
        "center": center,
        "residue": residue,
        "offset": offset,
        "state": state,
        "cofactor": cofactor,
        "half_scale": half_scale,
    }


def large_support_closure(k: int, support: list[int]) -> dict[str, object] | None:
    """Return the L040 support-closure data for a transverse support product.

    For G_P=prod(P)>2k, L039 supplies at most one basin hit n=G_P*h.  If the
    hit survives the anchor sieve, every prime divisor of h is itself a
    transverse small prime (because h<=floor((k+1)/2)<=k).  Therefore the full
    transverse support is exactly P iff h is P-smooth.

    Without anchor survival this equivalence is intentionally *not* asserted:
    anchor primes may occur in h without changing transverse support.
    """
    normalized = _validate_support(k, support)
    product = 1
    for p in normalized:
        product *= p
    if product <= 2 * k:
        raise ValueError("support product must be > 2k")

    hit = common_center_large_hit(k, product)
    if hit is None:
        return None

    state = int(hit["state"])
    cofactor = int(hit["cofactor"])
    anchor = anchor_product(k)
    anchor_survives = gcd(state, anchor) == 1
    if anchor_survives != (gcd(cofactor, anchor) == 1):
        raise AssertionError("transverse support product changed anchor-survival status")

    cofactor_factors = distinct_prime_factors(cofactor)
    p_smooth = all(q in normalized for q in cofactor_factors)
    full_transverse_support = transverse_prime_support(state, k, anchor)
    exact_transverse_support = full_transverse_support == normalized

    if anchor_survives and exact_transverse_support != p_smooth:
        raise AssertionError("L040 anchor-surviving smooth-closure equivalence failed")

    return {
        **hit,
        "support": normalized,
        "support_product": product,
        "anchor_product": anchor,
        "anchor_survives": anchor_survives,
        "cofactor_prime_factors": cofactor_factors,
        "p_smooth": p_smooth,
        "full_transverse_support": full_transverse_support,
        "exact_transverse_support": exact_transverse_support,
        "closure_equivalence_applies": anchor_survives,
    }
