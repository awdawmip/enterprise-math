"""Bounded CRT sign-pattern capacity for centered P017 mirror pairs.

Chinese-remainder/idempotent facts are classical.  This module only packages
those facts around the finite mirror-radius window 1<=r<k and keeps a strict
distinction between a prescribed sign pattern modulo D and an *exact* complete
transverse support.
"""

from __future__ import annotations

from math import gcd, prod

from .legendre import anchor_product, primes_up_to
from .p017_mirror import (
    anchor_surviving_radius,
    mirror_center,
    mirror_pair,
    mirror_transverse_supports,
    surviving_mirror_triple,
)


def _validated_transverse_support(k: int, support: list[int]) -> list[int]:
    center = mirror_center(k)
    if not support or len(support) != len(set(support)):
        raise ValueError("support must be a nonempty list of distinct primes")
    normalized = sorted(support)
    allowed = set(primes_up_to(k))
    if any(p not in allowed or center % p == 0 for p in normalized):
        raise ValueError("every support prime must be transverse and <= k")
    return normalized


def observed_mirror_idempotent(k: int, radius: int) -> dict[str, object]:
    """Executable L046 for an observed surviving mirror pair with two nonempty supports."""
    if not anchor_surviving_radius(k, radius):
        raise ValueError("radius must survive the anchor sieve")
    surviving_mirror_triple(k, radius)
    lower_support, upper_support = mirror_transverse_supports(k, radius)
    if not lower_support or not upper_support:
        raise ValueError("both mirror sides must have nonempty transverse support")

    support = sorted(lower_support + upper_support)
    modulus = prod(support)
    center = mirror_center(k)
    if gcd(center, modulus) != 1 or modulus % 2 == 0:
        raise AssertionError("observed transverse modulus must be odd and coprime to center")

    involution = (radius * pow(center, -1, modulus)) % modulus
    if (involution * involution - 1) % modulus != 0:
        raise AssertionError("L046 normalized radius is not a square root of one")

    idempotent = ((1 + involution) * pow(2, -1, modulus)) % modulus
    if (idempotent * idempotent - idempotent) % modulus != 0:
        raise AssertionError("L046 selector is not idempotent")
    if idempotent in (0, 1):
        raise AssertionError("two nonempty sides must give a nontrivial idempotent")

    lower_product = prod(lower_support)
    upper_product = prod(upper_support)
    if gcd(idempotent - 1, modulus) != lower_product:
        raise AssertionError("idempotent failed to recover lower support product")
    if gcd(idempotent, modulus) != upper_product:
        raise AssertionError("idempotent failed to recover upper support product")

    lower, upper = mirror_pair(k, radius)
    if gcd(lower, modulus) != lower_product or gcd(upper, modulus) != upper_product:
        raise AssertionError("mirror states failed to recover the CRT side partition")

    return {
        "k": k,
        "radius": radius,
        "center": center,
        "support": support,
        "lower_support": lower_support,
        "upper_support": upper_support,
        "modulus": modulus,
        "involution": involution,
        "idempotent": idempotent,
        "lower_product": lower_product,
        "upper_product": upper_product,
    }


def _validated_pattern(k: int, support: list[int], idempotent: int) -> tuple[list[int], int, int]:
    normalized = _validated_transverse_support(k, support)
    modulus = prod(normalized)
    if isinstance(idempotent, bool) or not isinstance(idempotent, int):
        raise ValueError("idempotent must be an integer")
    e = idempotent % modulus
    if (e * e - e) % modulus != 0 or e in (0, 1):
        raise ValueError("a nontrivial idempotent modulo the support product is required")
    center = mirror_center(k)
    return normalized, modulus, e


def bounded_sign_pattern_lifts(
    k: int,
    support: list[int],
    idempotent: int,
    *,
    require_anchor_survival: bool = False,
) -> list[int]:
    """Executable L047: enumerate 1<=r<k realizing one CRT side-sign pattern."""
    _support, modulus, e = _validated_pattern(k, support, idempotent)
    center = mirror_center(k)
    involution = (2 * e - 1) % modulus
    if (involution * involution - 1) % modulus != 0:
        raise AssertionError("idempotent did not produce a square root of one")
    residue = (center * involution) % modulus
    if residue == 0:
        raise AssertionError("transverse sign-pattern residue cannot be zero")

    lifts: list[int] = []
    radius = residue
    while radius < k:
        if radius >= 1 and (
            not require_anchor_survival or anchor_surviving_radius(k, radius)
        ):
            lifts.append(radius)
        radius += modulus
    return lifts


def exact_support_lifts(k: int, support: list[int], idempotent: int) -> list[int]:
    """Return anchor-surviving sign-pattern lifts with no extra transverse primes."""
    normalized, _modulus, _e = _validated_pattern(k, support, idempotent)
    result: list[int] = []
    for radius in bounded_sign_pattern_lifts(
        k, normalized, idempotent, require_anchor_survival=True
    ):
        lower_support, upper_support = mirror_transverse_supports(k, radius)
        if sorted(lower_support + upper_support) == normalized:
            result.append(radius)
    return result


def sign_pattern_capacity(k: int, support: list[int], idempotent: int) -> dict[str, object]:
    """Executable L047-L048 capacity chain exact<=anchor<=sign."""
    normalized, modulus, e = _validated_pattern(k, support, idempotent)
    center = mirror_center(k)
    involution = (2 * e - 1) % modulus
    residue = (center * involution) % modulus
    if residue == 0:
        raise AssertionError("transverse sign-pattern residue cannot be zero")

    if residue >= k:
        formula_capacity = 0
    else:
        formula_capacity = 1 + (k - 1 - residue) // modulus

    all_lifts = bounded_sign_pattern_lifts(k, normalized, e)
    anchor_lifts = bounded_sign_pattern_lifts(
        k, normalized, e, require_anchor_survival=True
    )
    exact_lifts = exact_support_lifts(k, normalized, e)

    if len(all_lifts) != formula_capacity:
        raise AssertionError("L047 arithmetic-progression capacity formula failed")
    if not set(exact_lifts).issubset(anchor_lifts):
        raise AssertionError("L048 exact-support lifts escaped anchor-surviving sign lifts")
    if not set(anchor_lifts).issubset(all_lifts):
        raise AssertionError("anchor filtering increased sign-pattern capacity")
    if modulus >= k and len(all_lifts) > 1:
        raise AssertionError("D>=k sign pattern has more than one bounded lift")

    return {
        "k": k,
        "support": normalized,
        "modulus": modulus,
        "idempotent": e,
        "involution": involution,
        "first_radius": residue,
        "sign_capacity": len(all_lifts),
        "anchor_capacity": len(anchor_lifts),
        "exact_capacity": len(exact_lifts),
        "sign_lifts": all_lifts,
        "anchor_lifts": anchor_lifts,
        "exact_lifts": exact_lifts,
    }
