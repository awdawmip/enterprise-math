"""Explicit Gessel--Lucas first jet for copies of a forced Franel midpoint.

Let p be an odd prime in the Jarvis--Verrill forced-midpoint sector
p=5 or 7 (mod 8), put m=(p-1)/2, and assume the forced zero F_m has exact
p-adic depth one.  The p^2 reflection first-jet theorem gives

    F'_m = 2 u_m  (mod p),    u_m=F_m/p (mod p).

Straub's Gessel--Lucas congruence then specializes, for 0<a<p with F_a a
p-unit, to

    F_(a p + m)/p = F_a (1+2a) u_m                    (mod p).

Thus the unique multiplier that raises the copied zero above depth one is

    a=(p-1)/2=m.

In particular every multiplier a<m with F_a a p-unit preserves exact depth
one.  P022 uses this to separate copy-numerator depth from the independent
central-binomial A-support pollution problem.
"""

from __future__ import annotations

from .p022_barlow_franel_gessel_lucas_copy import simple_zero_copy_linear_residue
from .p022_barlow_franel_reflection_first_jet import forced_midpoint_first_jet
from .p022_barlow_low_order_identifiability import triple_moment_factor


def forced_midpoint_copy_residue(
    prime: int,
    multiplier: int,
) -> tuple[int, int, int, int]:
    """Return (m,u,actual,predicted) for F_(a*p+m)/p modulo p."""
    midpoint, unit, _ = forced_midpoint_first_jet(prime)
    if (
        isinstance(multiplier, bool)
        or not isinstance(multiplier, int)
        or not 0 < multiplier < prime
    ):
        raise ValueError("multiplier must lie in 1..p-1")
    factor = triple_moment_factor(multiplier) % prime
    if factor == 0:
        raise ValueError("multiplier Franel factor must be a p-unit")
    actual, gessel = simple_zero_copy_linear_residue(
        midpoint,
        prime,
        multiplier,
    )
    predicted = factor * (1 + 2 * multiplier) * unit % prime
    if actual != gessel or actual != predicted:
        raise AssertionError("forced-midpoint copy first jet disagrees")
    return midpoint, unit, actual, predicted


def forced_midpoint_copy_stays_simple(prime: int, multiplier: int) -> bool:
    """Certify exact copied depth one whenever a!=m and F_a is a p-unit."""
    midpoint, _, actual, _ = forced_midpoint_copy_residue(prime, multiplier)
    if multiplier == midpoint:
        if actual != 0:
            raise AssertionError("the self-midpoint multiplier must be exceptional")
        return False
    if actual == 0:
        raise AssertionError("only the midpoint multiplier can raise copied depth")
    return True
