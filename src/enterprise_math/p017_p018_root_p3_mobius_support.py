"""Affine Möbius + support-depth recovery at the fourth-root cutoff.

Let U=k^2+2k and z=floor(U^(1/4)).  For every z-rough state n in the square
interval, let

    c(n) = #{p prime : z<p<=k and p|n}.

The root cutoff gives Omega(n)<=3.  The possible arithmetic types and the pair
(mu(n),c(n)) are:

    prime                  (-1, 0)
    squarefree semiprime   (+1, 1)
    squarefree triple      (-1, 3)
    repeated triple p^2 q  ( 0, 2)
    cube p^3               ( 0, 1)

(A repeated semiprime p^2 cannot lie strictly between consecutive squares.)
Thus the affine weight

    2 - mu(n) - c(n)

has values 3,0,0,0,1 on the five rows.  If

    R_3 = number of fourth-root rough states,
    M_3 = sum mu(n) over those states,
    S_1 = sum c(n),
    C_3 = number of rough prime cubes p^3 in the interval,

then

    3*prime_gap(k) = 2*R_3 - M_3 - S_1 - C_3.

Moreover C_3<=1.  Indeed two distinct integer cubes a^3<b^3 in the interval
would have a^3>k^2 and hence a>k^(2/3), while

    b^3-a^3 >= 3a^2+3a+1 > 2k,

which exceeds the full square-window length.

This identity is the exact sign × factor-depth coupling requested by the
preceding parity-transport generation.  It does not supply the missing
pointwise estimate for M_3+S_1; that analytic inequality remains open.
"""

from __future__ import annotations

from math import isqrt

from .legendre import direct_square_interval_prime_count, primes_up_to
from .p017_p018_buchstab_cutoff_ladder import rough_survivor_offsets, square_interval_upper
from .p017_p018_root_p3_support_recovery import medium_prime_support, root_p3_cutoff


def mobius_value(value: int) -> int:
    """Return the Möbius function by bounded exact factorization."""
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    if value == 1:
        return 1
    remaining = value
    parity = 0
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            parity ^= 1
            if remaining % p == 0:
                return 0
            while remaining % p == 0:
                remaining //= p
            if p == 2:
                p = 3
            else:
                p += 2
            continue
        if p == 2:
            p = 3
        else:
            p += 2
    if remaining > 1:
        parity ^= 1
    return -1 if parity else 1


def affine_mobius_support_weight(k: int, value: int) -> int:
    """Return 2-mu(value)-c(value) for one fourth-root rough state."""
    z = root_p3_cutoff(k)
    if not (k * k < value <= square_interval_upper(k)):
        raise ValueError("value must lie in the square interval")
    if any(value % p == 0 for p in primes_up_to(z)):
        raise ValueError("value must survive the fourth-root pre-sieve")
    depth = len(medium_prime_support(k, value))
    return 2 - mobius_value(value) - depth


def rough_prime_cube_offsets(k: int) -> tuple[int, ...]:
    """Return rough prime-cube offsets p^3-k^2; there is at most one."""
    z = root_p3_cutoff(k)
    lower = k * k
    upper = square_interval_upper(k)
    rows = tuple(
        p**3 - lower
        for p in primes_up_to(k)
        if p > z and lower < p**3 <= upper
    )
    if len(rows) > 1:
        raise AssertionError("square interval contains more than one rough prime cube")
    return rows


def root_p3_mobius_support_profile(k: int) -> dict[str, object]:
    """Enumerate the affine Möbius-support identity for bounded research."""
    z = root_p3_cutoff(k)
    offsets = rough_survivor_offsets(k, z)
    mobius_sum = 0
    support_sum = 0
    weight_sum = 0

    for offset in offsets:
        value = k * k + offset
        mu = mobius_value(value)
        depth = len(medium_prime_support(k, value))
        weight = 2 - mu - depth
        mobius_sum += mu
        support_sum += depth
        weight_sum += weight

    cube_offsets = rough_prime_cube_offsets(k)
    prime_count = direct_square_interval_prime_count(k)
    rhs = 2 * len(offsets) - mobius_sum - support_sum - len(cube_offsets)
    if rhs != 3 * prime_count:
        raise AssertionError("affine Möbius-support recovery failed")
    if weight_sum != 3 * prime_count + len(cube_offsets):
        raise AssertionError("affine state weights failed their type decomposition")

    return {
        "k": k,
        "fourth_root_cutoff": z,
        "rough_count": len(offsets),
        "mobius_sum": mobius_sum,
        "support_moment_1": support_sum,
        "rough_prime_cube_offsets": cube_offsets,
        "rough_prime_cube_count": len(cube_offsets),
        "affine_weight_sum": weight_sum,
        "prime_count": prime_count,
        "affine_identity_rhs": rhs,
        "exact_affine_recovery": True,
    }
