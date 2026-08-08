"""Centered mirror-pair tools for the Legendre pressure test.

The square basin is centered at M=k(k+1).  After anchor-prime elimination,
transverse small-prime supports of M-r and M+r are disjoint.  These are exact
cross-state constraints, not a proof of Legendre's conjecture.
"""

from __future__ import annotations

from math import gcd

from .legendre import anchor_product, is_prime, primes_up_to


def mirror_pair(k: int, r: int) -> tuple[int, int, int]:
    """Return (M-r, M+r, M) for 1<=r<=k-1."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    if isinstance(r, bool) or not isinstance(r, int) or not 1 <= r <= k - 1:
        raise ValueError("r must satisfy 1 <= r <= k-1")
    center = k * (k + 1)
    lower = center - r
    upper = center + r
    if not (k * k < lower < upper < (k + 1) * (k + 1)):
        raise AssertionError("mirror pair escaped the square basin")
    return lower, upper, center


def transverse_support(k: int, n: int) -> list[int]:
    """Return small prime divisors p<=k of n that do not divide k(k+1)."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    center = k * (k + 1)
    return [p for p in primes_up_to(k) if center % p != 0 and n % p == 0]


def anchor_pair_survival(k: int, r: int) -> dict[str, int | bool]:
    """Return the exact all-in/all-out anchor status of a mirror pair.

    For A equal to the product of small anchor primes,

        gcd(M-r,A)=gcd(r,A)=gcd(M+r,A).
    """
    lower, upper, _center = mirror_pair(k, r)
    anchor = anchor_product(k)
    radius_gcd = gcd(r, anchor)
    lower_gcd = gcd(lower, anchor)
    upper_gcd = gcd(upper, anchor)
    if not (radius_gcd == lower_gcd == upper_gcd):
        raise AssertionError("anchor mirror gcd identity failed")
    return {
        "anchor_product": anchor,
        "radius_gcd": radius_gcd,
        "lower_gcd": lower_gcd,
        "upper_gcd": upper_gcd,
        "survives": radius_gcd == 1,
    }


def mirror_support_separation(k: int, r: int) -> dict[str, object]:
    """Return transverse supports and verify that they are disjoint."""
    lower, upper, center = mirror_pair(k, r)
    lower_support = transverse_support(k, lower)
    upper_support = transverse_support(k, upper)
    shared = sorted(set(lower_support).intersection(upper_support))
    if shared:
        raise AssertionError("transverse mirror supports must be disjoint")
    return {
        "center": center,
        "lower": lower,
        "upper": upper,
        "lower_support": lower_support,
        "upper_support": upper_support,
        "shared_support": shared,
        "anchor": anchor_pair_survival(k, r),
    }


def composite_surviving_pair_certificate(k: int, r: int) -> dict[str, object]:
    """Certify the two-distinct-support requirement for a surviving composite pair.

    If the mirror pair survives the anchor sieve and both members are composite,
    root-factor horizon forces a small prime factor on each side.  Anchor
    survival makes those factors transverse, and mirror separation makes the
    two supports disjoint.
    """
    data = mirror_support_separation(k, r)
    anchor = data["anchor"]
    if not bool(anchor["survives"]):
        raise ValueError("mirror pair must survive the anchor sieve")
    lower = int(data["lower"])
    upper = int(data["upper"])
    if is_prime(lower) or is_prime(upper):
        raise ValueError("both mirror states must be composite")
    lower_support = list(data["lower_support"])
    upper_support = list(data["upper_support"])
    if not lower_support or not upper_support:
        raise AssertionError("composite basin states must have small transverse factors")
    return {
        **data,
        "distinct_small_prime_resources": len(set(lower_support + upper_support)),
        "minimum_required": 2,
    }


def mirror_basin_partition(k: int) -> dict[str, object]:
    """Partition I_k into k-1 mirror pairs plus two known composite states."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    center = k * (k + 1)
    pairs = [(center - r, center + r) for r in range(1, k)]
    top = center + k
    if center != k * (k + 1) or top != k * (k + 2):
        raise AssertionError("known composite endpoints were misidentified")
    states = [n for pair in pairs for n in pair] + [center, top]
    expected = list(range(k * k + 1, (k + 1) * (k + 1)))
    if sorted(states) != expected:
        raise AssertionError("mirror partition does not cover the square basin")
    return {
        "center": center,
        "top": top,
        "pairs": pairs,
        "known_composites": [center, top],
    }
