"""Explicit Gessel--Lucas first jet for copies of a forced Franel midpoint.

Let p be an odd prime in the Jarvis--Verrill forced-midpoint sector
p=5 or 7 (mod 8), put m=(p-1)/2, and assume the forced zero F_m has exact
p-adic depth one.  The p^2 reflection first-jet theorem gives

    F'_m = 2 u_m  (mod p),    u_m=F_m/p (mod p).

Straub's Gessel--Lucas congruence then specializes for every 0<a<p to

    F_(a p + m)/p = F_a (1+2a) u_m                    (mod p).

When F_a is a p-unit this shows that the unique multiplier that raises the
copied zero above depth one is a=(p-1)/2=m.  When F_a is itself divisible by p,
the displayed quotient is zero and the copy is automatically divisible by
p^2.  P022 uses this to separate copy-numerator depth from the independent
central-binomial A-support pollution problem.
"""

from __future__ import annotations

from .p022_barlow_franel_gessel_lucas_copy import franel_gessel_lucas_mod_square
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
    actual_square, predicted_square = franel_gessel_lucas_mod_square(
        midpoint,
        prime,
        multiplier,
    )
    if actual_square != predicted_square or actual_square % prime:
        raise AssertionError("midpoint copy must remain p-divisible")
    actual = (actual_square // prime) % prime
    factor = triple_moment_factor(multiplier) % prime
    predicted = factor * (1 + 2 * multiplier) * unit % prime
    if actual != predicted:
        raise AssertionError("forced-midpoint copy first jet disagrees")
    return midpoint, unit, actual, predicted


def forced_midpoint_copy_stays_simple(prime: int, multiplier: int) -> bool:
    """Certify copied depth one exactly when the first-jet residue is nonzero."""
    midpoint, _, actual, _ = forced_midpoint_copy_residue(prime, multiplier)
    factor = triple_moment_factor(multiplier) % prime
    if factor == 0 or multiplier == midpoint:
        if actual != 0:
            raise AssertionError("zero factor or exceptional multiplier must raise depth")
        return False
    if actual == 0:
        raise AssertionError("unit nonexceptional multiplier must preserve depth one")
    return True
