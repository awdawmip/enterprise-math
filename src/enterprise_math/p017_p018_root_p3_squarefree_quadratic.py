"""Squarefree fourth-root survivors admit exact quadratic prime recovery.

Let U=k^2+2k and z=floor(U^(1/4)).  Start from the z-rough square interval and
remove every state divisible by p^2 for a prime p>z.  (No prime <=z divides a
rough state, and every square divisor of a state below (k+1)^2 has p<=k.)

Every remaining state is squarefree and has Omega<=3.  If it is composite:

* Omega=2: writing n=pq with p<=q, one must have p<=k<q, because p,q<=k would
  give n<=k^2.  Hence exactly one prime divisor lies in the medium band z<p<=k,
  so c(n)=1.
* Omega=3: if n=abc with a<=b<=c, then

      ab >= (z+1)^2 > sqrt(U),

  hence c < sqrt(U) < k+1, so all three factors lie in the medium band and
  c(n)=3.

Primes have c(n)=0.  Thus on the squarefree fourth-root survivor set the only
support depths are 0,1,3, and

    1_P(n) = 1 - c(n) + (2/3) C(c(n),2)

exactly.  If R_sf is the squarefree fourth-root rough count and S1_sf,S2_sf are
the first two medium-support binomial moments, then

    3*prime_gap(k) = 3*R_sf - 3*S1_sf + 2*S2_sf.

This is an exact residual algebra reduction from degree three to degree two.
It does not prove that the quadratic weighted sum is positive; a prime-free
squarefree incidence model with only depths 1 and 3 makes the weight vanish
identically.  The missing input remains arithmetic correlation, not another
support coordinate.
"""

from __future__ import annotations

from math import comb

from .legendre import direct_square_interval_prime_count, primes_up_to
from .p017_p018_buchstab_cutoff_ladder import rough_survivor_offsets
from .p017_p018_root_p3_support_recovery import medium_prime_support, root_p3_cutoff


def has_medium_square_factor(k: int, value: int) -> bool:
    """Return whether p^2 divides value for some z_3(k)<p<=k."""
    z = root_p3_cutoff(k)
    return any(value % (p * p) == 0 for p in primes_up_to(k) if p > z)


def squarefree_quadratic_indicator_numerator(depth: int) -> int:
    """Return 3-3c+2*C(c,2); exact for squarefree depths c in {0,1,3}."""
    if isinstance(depth, bool) or not isinstance(depth, int) or depth not in (0, 1, 3):
        raise ValueError("squarefree fourth-root depth must be one of 0,1,3")
    return 3 - 3 * depth + 2 * comb(depth, 2)


def squarefree_root_p3_profile(k: int) -> dict[str, object]:
    """Enumerate the exact squarefree quadratic recovery for bounded research."""
    z = root_p3_cutoff(k)
    offsets = rough_survivor_offsets(k, z)
    kept: list[int] = []
    removed: list[int] = []
    depth_counts = {0: 0, 1: 0, 3: 0}
    s1 = 0
    s2 = 0

    for offset in offsets:
        value = k * k + offset
        if has_medium_square_factor(k, value):
            removed.append(offset)
            continue
        support = medium_prime_support(k, value)
        depth = len(support)
        if depth not in (0, 1, 3):
            raise AssertionError("squarefree fourth-root survivor has forbidden support depth")
        kept.append(offset)
        depth_counts[depth] += 1
        s1 += depth
        s2 += comb(depth, 2)

    prime_count = direct_square_interval_prime_count(k)
    numerator = 3 * len(kept) - 3 * s1 + 2 * s2
    if numerator != 3 * prime_count:
        raise AssertionError("squarefree quadratic support recovery failed")

    return {
        "k": k,
        "fourth_root_cutoff": z,
        "squarefree_rough_offsets": tuple(kept),
        "removed_squareful_offsets": tuple(removed),
        "squarefree_rough_count": len(kept),
        "support_moment_1": s1,
        "support_moment_2": s2,
        "support_depth_counts": (depth_counts[0], depth_counts[1], depth_counts[3]),
        "quadratic_prime_numerator": numerator,
        "prime_count": prime_count,
        "exact_quadratic_recovery": True,
    }
