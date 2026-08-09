"""Centered mirror-pair structure for the P017 consecutive-square basin."""

from __future__ import annotations

from math import gcd

from .cutoff_pairing import transverse_prime_support
from .legendre import anchor_product


def _require_k(k: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")


def mirror_center(k: int) -> int:
    """Return the common center M=k(k+1)."""
    _require_k(k)
    return k * (k + 1)


def mirror_pair(k: int, radius: int) -> tuple[int, int]:
    """Return (M-r,M+r) for 1<=r<k."""
    center = mirror_center(k)
    if isinstance(radius, bool) or not isinstance(radius, int) or not (1 <= radius < k):
        raise ValueError("radius must satisfy 1 <= radius < k")
    lower = center - radius
    upper = center + radius
    if not (k * k < lower < upper < (k + 1) * (k + 1)):
        raise AssertionError("mirror pair escaped the open square basin")
    return lower, upper


def mirror_basin_partition(k: int) -> dict[str, object]:
    """Partition the open square basin into k-1 mirror pairs plus two states."""
    center = mirror_center(k)
    pairs = [mirror_pair(k, r) for r in range(1, k)]
    unpaired = [center, center + k]
    reconstructed = sorted([n for pair in pairs for n in pair] + unpaired)
    expected = list(range(k * k + 1, (k + 1) * (k + 1)))
    if reconstructed != expected:
        raise AssertionError("centered mirror partition does not equal the square basin")
    if unpaired != [k * (k + 1), k * (k + 2)]:
        raise AssertionError("unpaired composite states were misidentified")
    return {"k": k, "center": center, "pairs": pairs, "unpaired": unpaired}


def anchor_pair_gcds(k: int, radius: int) -> dict[str, int | bool]:
    """Executable L042: anchor gcd is identical on radius and both mirror states."""
    lower, upper = mirror_pair(k, radius)
    anchor = anchor_product(k)
    radius_gcd = gcd(radius, anchor)
    lower_gcd = gcd(lower, anchor)
    upper_gcd = gcd(upper, anchor)
    if not (radius_gcd == lower_gcd == upper_gcd):
        raise AssertionError("L042 anchor mirror gcd identity failed")
    return {
        "anchor_product": anchor,
        "radius_gcd": radius_gcd,
        "lower_gcd": lower_gcd,
        "upper_gcd": upper_gcd,
        "survives": radius_gcd == 1,
    }


def anchor_surviving_radius(k: int, radius: int) -> bool:
    """Return whether both sides of the mirror pair survive the anchor sieve."""
    return bool(anchor_pair_gcds(k, radius)["survives"])


def mirror_transverse_supports(k: int, radius: int) -> tuple[list[int], list[int]]:
    """Executable L043: return lower/upper transverse small-prime supports."""
    lower, upper = mirror_pair(k, radius)
    anchor = anchor_product(k)
    lower_support = transverse_prime_support(lower, k, anchor)
    upper_support = transverse_prime_support(upper, k, anchor)
    if set(lower_support).intersection(upper_support):
        raise AssertionError("L043 transverse mirror supports are not disjoint")
    return lower_support, upper_support


def surviving_mirror_triple(k: int, radius: int) -> dict[str, int]:
    """Verify the stronger corollary that a surviving mirror triple is pairwise coprime."""
    if not anchor_surviving_radius(k, radius):
        raise ValueError("radius must survive the anchor sieve")
    lower, upper = mirror_pair(k, radius)
    center = mirror_center(k)
    if gcd(lower, center) != 1 or gcd(center, upper) != 1 or gcd(lower, upper) != 1:
        raise AssertionError("surviving mirror triple is not pairwise coprime")
    return {"lower": lower, "center": center, "upper": upper}
