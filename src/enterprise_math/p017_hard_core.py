"""Discovery-stage P017 residual hard-core geometry.

This module isolates the mirror branch left after canonical L053. It records two
coupled WIP refinements:

1. the full-core congruence modulo odd S=S_-S_+ combines with anchor-forced odd
   radius parity into one class modulo 2S, so multiple bounded anchor lifts can
   occur only when 2S<k;
2. when both mirror states are composite and S<k, their canonical L020 prime
   tails are separated by more than k+5; in the actual multiple-lift region
   2S<k this strengthens to more than 3k+9.

These are discovery results, not a canonical L055.
"""

from __future__ import annotations

from math import gcd

from .legendre import is_prime
from .p017_cofactor_window import square_basin_smooth_tail
from .p017_mirror import anchor_surviving_radius, mirror_center, mirror_pair
from .p017_mirror_crt import observed_mirror_full_core_idempotent


def anchor_parity_full_core_capacity(k: int, radius: int) -> dict[str, object]:
    """Refine the canonical L053 full-core progression by mandatory odd parity.

    Canonical L053 places the observed radius in one residue class modulo the
    odd full-core modulus S. Anchor survival also forces r odd because 2 divides
    M=k(k+1). Since gcd(2,S)=1, these two conditions form one residue class
    modulo 2S. Therefore bounded parity-compatible lifts in 1<=r<k are spaced
    by 2S, and 2S>=k implies capacity at most one.
    """
    data = observed_mirror_full_core_idempotent(k, radius)
    modulus = int(data["modulus"])
    if modulus % 2 == 0:
        raise AssertionError("canonical L053 full-core modulus must be odd")
    if radius % 2 == 0:
        raise AssertionError("anchor-surviving radius must be odd")

    raw_lifts = list(data["full_core_lifts"])
    parity_lifts = [candidate for candidate in raw_lifts if candidate % 2 == 1]
    anchor_lifts = [
        candidate
        for candidate in parity_lifts
        if anchor_surviving_radius(k, candidate)
    ]
    if radius not in anchor_lifts:
        raise AssertionError("observed radius escaped its parity/anchor refinement")
    for left, right in zip(parity_lifts, parity_lifts[1:]):
        if right - left != 2 * modulus:
            raise AssertionError("parity-compatible full-core lifts are not 2S-spaced")
    if 2 * modulus >= k and len(parity_lifts) > 1:
        raise AssertionError("2S>=k should force at most one parity-compatible lift")
    if not set(anchor_lifts).issubset(parity_lifts):
        raise AssertionError("anchor filtering increased parity capacity")

    return {
        **data,
        "raw_full_core_lifts": raw_lifts,
        "parity_full_core_lifts": parity_lifts,
        "anchor_full_core_lifts": anchor_lifts,
        "parity_modulus": 2 * modulus,
        "parity_capacity": len(parity_lifts),
        "anchor_capacity": len(anchor_lifts),
    }


def residual_hard_core_tail_gap(k: int, radius: int) -> dict[str, int]:
    """Return the WIP hard-core tail-gap data under S_-*S_+<k.

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


def residual_multi_lift_tail_gap(k: int, radius: int) -> dict[str, int]:
    """Strengthen the tail gap in the only region allowing multiple parity lifts.

    The parity refinement shows that multiple candidates for one full-core cell
    require 2ab<k. Then 2ab<=k-1, so the same mirror identity gives

        |q_- - q_+|
        >= 2k(k+1)/(ab) - (k-1)
        >= 4k(k+1)/(k-1) - (k-1)
        = 3k + 9 + 8/(k-1)
        > 3k+9.
    """
    data = residual_hard_core_tail_gap(k, radius)
    core_product = int(data["core_product"])
    if 2 * core_product >= k:
        raise ValueError("multiple-lift residual condition requires 2*S_-*S_+ < k")

    gap = int(data["tail_gap"])
    if gap <= 3 * k + 9:
        raise AssertionError("multi-lift hard-core tails were not 3k-scale separated")
    parity_bound = 3 * k + 10 if k % 2 == 0 else 3 * k + 11
    if gap < parity_bound or gap % 2:
        raise AssertionError("multi-lift odd-prime parity sharpening failed")

    return {
        **data,
        "multi_lift_parity_lower_bound": parity_bound,
    }
