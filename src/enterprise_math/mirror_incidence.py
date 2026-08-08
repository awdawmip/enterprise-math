"""Transverse-support incidence counts for centered square-basin mirror pairs."""

from __future__ import annotations

from .legendre import is_prime, primes_up_to
from .mirror import (
    anchor_surviving_radius,
    mirror_center,
    mirror_pair,
    mirror_transverse_supports,
)


def transverse_incidence_count(k: int) -> int:
    """Count state-prime transverse incidences across anchor-surviving mirror radii."""
    total = 0
    for radius in range(1, k):
        if not anchor_surviving_radius(k, radius):
            continue
        lower_support, upper_support = mirror_transverse_supports(k, radius)
        total += len(lower_support) + len(upper_support)
    return total


def transverse_incidence_count_by_prime(k: int) -> int:
    """Reindex the same incidence count by transverse prime rather than state."""
    center = mirror_center(k)
    total = 0
    for p in primes_up_to(k):
        if center % p == 0:
            continue
        for radius in range(1, k):
            if not anchor_surviving_radius(k, radius):
                continue
            lower, upper = mirror_pair(k, radius)
            if lower % p == 0 or upper % p == 0:
                total += 1
    return total


def surviving_radii(k: int) -> list[int]:
    return [r for r in range(1, k) if anchor_surviving_radius(k, r)]


def double_composite_surviving_radii(k: int) -> list[int]:
    result: list[int] = []
    for radius in surviving_radii(k):
        lower, upper = mirror_pair(k, radius)
        if not is_prime(lower) and not is_prime(upper):
            result.append(radius)
    return result


def mirror_counterexample_capacity(k: int) -> dict[str, int | bool]:
    """Return the L033 resource inequality data for one root k."""
    center = mirror_center(k)
    survivors = surviving_radii(k)
    all_basin_composite = True
    # The two unpaired states center and center+k are always composite for k>=2.
    for radius in range(1, k):
        lower, upper = mirror_pair(k, radius)
        if is_prime(lower) or is_prime(upper):
            all_basin_composite = False
            break
    incidence = transverse_incidence_count(k)
    return {
        "k": k,
        "center": center,
        "surviving_radii": len(survivors),
        "transverse_incidence": incidence,
        "all_basin_composite": all_basin_composite,
        "counterexample_necessary_bound": incidence >= 2 * len(survivors),
    }
