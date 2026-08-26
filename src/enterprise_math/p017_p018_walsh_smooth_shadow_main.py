"""Exact smooth-shadow floor main for the cutoff-linear orientation-Walsh detector.

Put K=k-1 and C=floor(K/2).  Let A be the product of the effective odd anchor
primes dividing M=k(k+1).  Fix a cutoff z with

    (z+1)^2 > C.

In the upper-orientation linear Walsh minorant, every nonempty selected low-band
orientation cube has zero floor by the Walsh sign sum.  The only repeatable
floor terms are therefore:

* the constant column;
* one target-oriented transverse prime p with z<p<=C.

After anchor Mobius, the constant floor is

    B0 = #{m<=C : gcd(m,A)=1},

and the p-column floor is

    Bp = #{m<=C/p : gcd(m,A)=1}.

Since two primes strictly larger than z have product >(z+1)^2>C, an integer
m<=C can contain at most one prime factor >z.  Anchor primes are already
excluded by gcd(m,A)=1.  Hence the p-column sets are disjoint and

    B0 - sum_(z<p<=C, p transverse) Bp
      = #{m<=C : gcd(m,A)=1, P^+(m)<=z}.

Thus the exact reusable-floor main of one orientation is the finite integer
smooth shadow

    Psi_A(C,z).

No Euler-product approximation is required.  The familiar asymptotic margin
1-log 2 at z~sqrt(k) is only the large-scale density of this exact object.  At
the half cutoff z=C the shadow is the complete anchor-coprime small shadow.

All remaining terms of the cutoff-linear Walsh detector are finite boundary
terms: low-band nonconstant orientation columns have sign-cancelled floors and
high target primes p>C have period 2p>K.  Consequently the analytic frontier can
be stated exactly as bounding the signed boundary loss strictly below
Psi_A(C,z).  This module proves the floor identity only; it does not bound that
boundary loss and does not prove Legendre.
"""

from __future__ import annotations

from math import gcd, prod

from .legendre import primes_up_to
from .p017_p018_effective_anchor import effective_odd_anchor_primes


def _largest_prime_factor(value: int) -> int:
    if value < 1:
        raise ValueError("value must be positive")
    if value == 1:
        return 1
    remaining = value
    largest = 1
    while remaining % 2 == 0:
        largest = 2
        remaining //= 2
    candidate = 3
    while candidate * candidate <= remaining:
        while remaining % candidate == 0:
            largest = candidate
            remaining //= candidate
        candidate += 2
    if remaining > 1:
        largest = remaining
    return largest


def smooth_shadow_parameters(k: int, cutoff: int) -> dict[str, object]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 6:
        raise ValueError("k must be an integer >=6")
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or cutoff < 2:
        raise ValueError("cutoff must be an integer >=2")
    C = (k - 1) // 2
    if cutoff > C:
        raise ValueError("cutoff must not exceed the reusable-floor cutoff C")
    if (cutoff + 1) * (cutoff + 1) <= C:
        raise ValueError("smooth-shadow one-large-prime identity requires (z+1)^2>C")
    anchors = effective_odd_anchor_primes(k)
    anchor_product = prod(anchors, start=1)
    return {
        "k": k,
        "K": k - 1,
        "reusable_floor_cutoff_C": C,
        "cutoff": cutoff,
        "effective_odd_anchors": anchors,
        "effective_anchor_product": anchor_product,
    }


def anchor_coprime_smooth_shadow(k: int, cutoff: int) -> dict[str, object]:
    """Return B0, sum Bp and Psi_A(C,z), verifying the exact set partition."""
    params = smooth_shadow_parameters(k, cutoff)
    C = int(params["reusable_floor_cutoff_C"])
    z = int(params["cutoff"])
    A = int(params["effective_anchor_product"])
    M = k * (k + 1)

    base_rows = tuple(m for m in range(1, C + 1) if gcd(m, A) == 1)
    medium_primes = tuple(
        p for p in primes_up_to(C)
        if p > z and p % 2 == 1 and M % p != 0
    )
    prime_rows: list[dict[str, object]] = []
    large_factor_members: set[int] = set()
    for p in medium_primes:
        cofactors = tuple(m for m in range(1, C // p + 1) if gcd(m, A) == 1)
        members = tuple(p * m for m in cofactors)
        if large_factor_members.intersection(members):
            raise AssertionError("two >z prime columns overlapped below C")
        large_factor_members.update(members)
        prime_rows.append({"prime": p, "anchor_coprime_cofactors": cofactors, "members": members})

    base_set = set(base_rows)
    if not large_factor_members.issubset(base_set):
        raise AssertionError("medium-prime floor column escaped the anchor-coprime shadow")
    smooth_members = tuple(
        m for m in base_rows if _largest_prime_factor(m) <= z
    )
    complement = base_set.difference(large_factor_members)
    if complement != set(smooth_members):
        raise AssertionError("anchor-coprime shadow did not split into smooth and one-large-prime parts")

    B0 = len(base_rows)
    linear_floor = sum(len(row["anchor_coprime_cofactors"]) for row in prime_rows)
    psi = len(smooth_members)
    if B0 - linear_floor != psi:
        raise AssertionError("smooth-shadow floor identity failed")

    return {
        **params,
        "constant_anchor_floor_B0": B0,
        "repeatable_medium_primes": medium_primes,
        "linear_medium_floor_sum": linear_floor,
        "smooth_shadow_count_Psi": psi,
        "smooth_shadow_members": smooth_members,
        "medium_prime_floor_rows": tuple(prime_rows),
        "exact_floor_main_equals_smooth_shadow": True,
    }


def walsh_linear_floor_main(k: int, cutoff: int) -> dict[str, object]:
    """Expose the exact one-orientation reusable-floor main Psi_A(C,z)."""
    data = anchor_coprime_smooth_shadow(k, cutoff)
    return {
        **data,
        "one_orientation_reusable_floor_main": int(data["smooth_shadow_count_Psi"]),
        "symmetric_reusable_floor_main": 2 * int(data["smooth_shadow_count_Psi"]),
        "remaining_nonconstant_terms": "FINITE_BOUNDARY_ONLY",
        "analytic_target": "SIGNED_BOUNDARY_LOSS_STRICTLY_BELOW_SMOOTH_SHADOW_MAIN",
    }
