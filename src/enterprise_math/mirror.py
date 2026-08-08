"""Centered mirror decomposition for the Legendre pressure test."""

from __future__ import annotations

from math import gcd

from .legendre import anchor_product
from .support_incidence import transverse_prime_support


def mirror_center(k: int) -> int:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    return k * (k + 1)


def mirror_pair(k: int, radius: int) -> tuple[int, int]:
    center = mirror_center(k)
    if isinstance(radius, bool) or not isinstance(radius, int) or not (1 <= radius < k):
        raise ValueError("radius must satisfy 1 <= radius < k")
    return center - radius, center + radius


def mirror_basin_partition(k: int) -> dict[str, object]:
    """Return the k-1 mirror pairs plus the two unpaired composite states."""
    center = mirror_center(k)
    return {
        "k": k,
        "center": center,
        "pairs": [mirror_pair(k, r) for r in range(1, k)],
        "unpaired": [center, center + k],
    }


def anchor_surviving_radius(k: int, radius: int) -> bool:
    """A mirror pair survives the anchor sieve iff gcd(radius, A_k)=1."""
    mirror_pair(k, radius)
    return gcd(radius, anchor_product(k)) == 1


def mirror_transverse_supports(k: int, radius: int) -> tuple[list[int], list[int]]:
    """Return lower/upper transverse small-prime supports of a mirror pair."""
    lower, upper = mirror_pair(k, radius)
    return transverse_prime_support(k, lower), transverse_prime_support(k, upper)
