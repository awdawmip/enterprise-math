"""Discovery-stage P017 residual hard-core geometry.

This module isolates the mirror branch left after canonical L053: both mirror
states are composite, their full k-smooth cores S_-,S_+ are nontrivial, and
S_-*S_+ < k. Canonical L020 then forces one prime tail >k on each side.

The WIP result below shows that these two large-prime tails are separated by
more than one full root scale. It is discovery evidence, not a canonical L055.
"""

from __future__ import annotations

from math import gcd

from .legendre import is_prime
from .p017_cofactor_window import square_basin_smooth_tail
from .p017_mirror import anchor_surviving_radius, mirror_center, mirror_pair


def residual_hard_core_tail_gap(k: int, radius: int) -> dict[str, int]:
    """Return the WIP hard-core tail-gap data.

    Assumptions:
    - 1 <= radius < k and the radius survives the anchor sieve;
    - both mirror states M-radius and M+radius are composite;
    - with full k-smooth cores a,b, one has a*b < k.

    Conclusion:
        abs(q_- - q_+) > k+5,
    hence, because both tails are odd primes,
        abs(q_- - q_+) >= k+6  if k is even,
        abs(q_- - q_+) >= k+7  if k is odd.
    """
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    if isinstance(radius, bool) or not isinstance(radius, int):
        raise ValueError("radius must be an integer")
    if not 1 <= radius < k:
        raise ValueError("require 1 <= radius < k")
    if not anchor_surviving_radius(k, radius):
        raise ValueError("radius must survive the anchor sieve")

    center = mirror_center(k)
    lower, upper = mirror_pair(k, radius)
    lower_data = square_basin_smooth_tail(k, lower)
    upper_data = square_basin_smooth_tail(k, upper)
    if bool(lower_data["is_prime"]) or bool(upper_data["is_prime"]):
        raise ValueError("both mirror states must be composite")

    a = int(lower_data["smooth_core"])
    b = int(upper_data["smooth_core"])
    q_minus = int(lower_data["tail"])
    q_plus = int(upper_data["tail"])
    if a <= 1 or b <= 1:
        raise AssertionError("composite hard-core state lost its smooth core")
    if a * b >= k:
        raise ValueError("residual hard-core condition requires S_-*S_+ < k")
    if gcd(a, b) != 1:
        raise AssertionError("surviving mirror cores must be coprime")
    if a % 2 == 0 or b % 2 == 0:
        raise AssertionError("anchor-surviving full cores must be odd")
    if q_minus <= k or q_plus <= k or not is_prime(q_minus) or not is_prime(q_plus):
        raise AssertionError("residual hard-core tails must be primes > k")

    gap = abs(q_minus - q_plus)
    # Distinct coprime odd cores satisfy |a-b|>=2 and a+b<=ab.
    # In the worse orientation a<b:
    #   q_- - q_+ = ((b-a)M-(a+b)r)/(ab)
    #               >= [2k(k+1)-ab(k-1)]/(ab)
    #               >= [k^2+4k-1]/(k-1) > k+5.
    if gap <= k + 5:
        raise AssertionError("hard-core large-prime tails were not k-scale separated")

    parity_bound = k + 6 if k % 2 == 0 else k + 7
    if gap < parity_bound or gap % 2:
        raise AssertionError("odd-prime parity sharpening failed")

    return {
        "k": k,
        "radius": radius,
        "center": center,
        "lower": lower,
        "upper": upper,
        "lower_core": a,
        "upper_core": b,
        "core_product": a * b,
        "lower_tail": q_minus,
        "upper_tail": q_plus,
        "tail_gap": gap,
        "parity_lower_bound": parity_bound,
    }
