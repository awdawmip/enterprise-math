"""Bounded CRT sign-pattern capacity for centered P017 mirror pairs.

Chinese-remainder/idempotent facts are classical. This module packages those
facts around the finite mirror-radius window 1<=r<k and keeps a strict
distinction between a prescribed sign pattern modulo D and an exact complete
transverse support.

The full-core refinement retains prime-power multiplicity from L053. It does
not introduce new CRT algebra: it replaces the squarefree support modulus by
the larger coprime product of the two observed full k-smooth cores and compares
the resulting bounded lift capacity with the canonical squarefree one.
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
from .p017_smooth_core import square_basin_smooth_core


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


def _bounded_residue_lifts(k: int, modulus: int, residue: int) -> list[int]:
    """Enumerate 1<=r<k in one nonzero residue class modulo ``modulus``."""
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    rho = residue % modulus
    if rho == 0:
        raise ValueError("a nonzero bounded-radius residue is required")
    lifts: list[int] = []
    radius = rho
    while radius < k:
        lifts.append(radius)
        radius += modulus
    return lifts


def observed_mirror_full_core_idempotent(k: int, radius: int) -> dict[str, object]:
    """Refine one observed mirror CRT cell by retaining full small-prime powers.

    Both mirror sides must be composite.  Their full k-smooth cores S_- and S_+
    are coprime for an anchor-surviving radius.  The same normalized-radius
    involution and idempotent construction works modulo S=S_-*S_+, and the gcds
    with e-1 and e recover the *full* cores rather than only squarefree support.

    The resulting bounded residue progression is a refinement of the canonical
    squarefree sign-pattern progression, so its capacity can never be larger.
    """
    if not anchor_surviving_radius(k, radius):
        raise ValueError("radius must survive the anchor sieve")
    surviving_mirror_triple(k, radius)
    lower, upper = mirror_pair(k, radius)
    lower_data = square_basin_smooth_core(k, lower)
    upper_data = square_basin_smooth_core(k, upper)
    if lower_data["state_is_prime"] or upper_data["state_is_prime"]:
        raise ValueError("both mirror states must be composite")

    lower_core = int(lower_data["smooth_core"])
    upper_core = int(upper_data["smooth_core"])
    if lower_core <= 1 or upper_core <= 1:
        raise AssertionError("composite mirror state lost its nontrivial smooth core")
    if gcd(lower_core, upper_core) != 1:
        raise AssertionError("surviving mirror full smooth cores are not coprime")

    modulus = lower_core * upper_core
    center = mirror_center(k)
    if modulus % 2 == 0 or gcd(center, modulus) != 1:
        raise AssertionError("full-core modulus must be odd and coprime to center")

    involution = (radius * pow(center, -1, modulus)) % modulus
    if involution % lower_core != 1 % lower_core:
        raise AssertionError("full-core involution lost the lower +1 sign")
    if involution % upper_core != (-1) % upper_core:
        raise AssertionError("full-core involution lost the upper -1 sign")
    if (involution * involution - 1) % modulus != 0:
        raise AssertionError("full-core normalized radius is not a square root of one")

    idempotent = ((1 + involution) * pow(2, -1, modulus)) % modulus
    if (idempotent * idempotent - idempotent) % modulus != 0:
        raise AssertionError("full-core selector is not idempotent")
    if gcd(idempotent - 1, modulus) != lower_core:
        raise AssertionError("full-core idempotent failed to recover lower core")
    if gcd(idempotent, modulus) != upper_core:
        raise AssertionError("full-core idempotent failed to recover upper core")

    residue = (center * ((2 * idempotent - 1) % modulus)) % modulus
    full_lifts = _bounded_residue_lifts(k, modulus, residue)
    if radius not in full_lifts:
        raise AssertionError("observed radius escaped its full-core progression")

    squarefree = observed_mirror_idempotent(k, radius)
    squarefree_capacity = sign_pattern_capacity(
        k, list(squarefree["support"]), int(squarefree["idempotent"])
    )
    squarefree_lifts = list(squarefree_capacity["sign_lifts"])
    if not set(full_lifts).issubset(squarefree_lifts):
        raise AssertionError("full-core progression is not a squarefree refinement")
    if len(full_lifts) > len(squarefree_lifts):
        raise AssertionError("full-core capacity exceeded squarefree sign capacity")
    if modulus >= k and len(full_lifts) > 1:
        raise AssertionError("full-core modulus >=k has multiple bounded lifts")

    return {
        "k": k,
        "radius": radius,
        "center": center,
        "lower_core": lower_core,
        "upper_core": upper_core,
        "lower_tail": int(lower_data["large_tail"]),
        "upper_tail": int(upper_data["large_tail"]),
        "modulus": modulus,
        "involution": involution,
        "idempotent": idempotent,
        "first_radius": residue,
        "full_core_lifts": full_lifts,
        "full_core_capacity": len(full_lifts),
        "squarefree_modulus": int(squarefree["modulus"]),
        "squarefree_sign_lifts": squarefree_lifts,
        "squarefree_sign_capacity": len(squarefree_lifts),
    }
