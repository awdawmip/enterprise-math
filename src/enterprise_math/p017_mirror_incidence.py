"""Basin-level transverse-prime incidence for centered P017 mirror pairs."""

from __future__ import annotations

from .legendre import is_prime, primes_up_to
from .p017_mirror import (
    anchor_surviving_radius,
    mirror_center,
    mirror_pair,
    mirror_transverse_supports,
    surviving_mirror_triple,
)


def surviving_radii(k: int) -> list[int]:
    """Return S_k, the mirror radii that survive the anchor sieve."""
    # mirror_center performs input validation.
    mirror_center(k)
    return [r for r in range(1, k) if anchor_surviving_radius(k, r)]


def double_composite_surviving_radii(k: int) -> list[int]:
    """Return surviving radii for which both mirror states are composite."""
    result: list[int] = []
    for radius in surviving_radii(k):
        lower, upper = mirror_pair(k, radius)
        if not is_prime(lower) and not is_prime(upper):
            result.append(radius)
    return result


def double_composite_resource_certificate(k: int, radius: int) -> dict[str, object]:
    """Executable L044: a surviving double-composite pair uses two disjoint supports."""
    if radius not in double_composite_surviving_radii(k):
        raise ValueError("radius must be anchor-surviving with both mirror states composite")
    lower, upper = mirror_pair(k, radius)
    lower_support, upper_support = mirror_transverse_supports(k, radius)
    if not lower_support or not upper_support:
        raise AssertionError("L044 composite basin state lacks a transverse small factor")
    if set(lower_support).intersection(upper_support):
        raise AssertionError("L044 opposite transverse supports overlap")
    return {
        "radius": radius,
        "lower": lower,
        "upper": upper,
        "lower_support": lower_support,
        "upper_support": upper_support,
        "distinct_resources": len(set(lower_support + upper_support)),
    }


def transverse_incidence_count(k: int) -> int:
    """Return J_k by summing support sizes over surviving mirror states."""
    total = 0
    for radius in surviving_radii(k):
        lower_support, upper_support = mirror_transverse_supports(k, radius)
        total += len(lower_support) + len(upper_support)
    return total


def transverse_incidence_by_prime(k: int) -> dict[int, int]:
    """Reindex J_k by transverse prime as in L045."""
    center = mirror_center(k)
    counts: dict[int, int] = {}
    radii = surviving_radii(k)
    for p in primes_up_to(k):
        if center % p == 0:
            continue
        count = 0
        for radius in radii:
            lower, upper = mirror_pair(k, radius)
            lower_hit = lower % p == 0
            upper_hit = upper % p == 0
            if lower_hit and upper_hit:
                raise AssertionError("L043 allowed one transverse prime on both mirror sides")
            if lower_hit or upper_hit:
                count += 1
        if count:
            counts[p] = count
    if sum(counts.values()) != transverse_incidence_count(k):
        raise AssertionError("L045 state-indexed and prime-indexed incidence totals disagree")
    return counts


def mirror_counterexample_capacity(k: int) -> dict[str, object]:
    """Return the L045 necessary-condition data without assuming Legendre failure."""
    center = mirror_center(k)
    radii = surviving_radii(k)
    incidence = transverse_incidence_count(k)
    by_prime = transverse_incidence_by_prime(k)

    all_mirror_composite = True
    for radius in range(1, k):
        lower, upper = mirror_pair(k, radius)
        if is_prime(lower) or is_prime(upper):
            all_mirror_composite = False
            break

    if all_mirror_composite and incidence < 2 * len(radii):
        raise AssertionError("L045 necessary incidence bound failed under all-composite basin")

    # Audit the stronger pairwise-coprime corollary for all surviving radii.
    for radius in radii:
        surviving_mirror_triple(k, radius)

    return {
        "k": k,
        "center": center,
        "surviving_radii": radii,
        "surviving_pair_count": len(radii),
        "transverse_incidence": incidence,
        "per_prime_incidence": by_prime,
        "all_mirror_composite": all_mirror_composite,
        "hypothetical_required_minimum": 2 * len(radii),
        "necessary_bound_holds": incidence >= 2 * len(radii),
    }
