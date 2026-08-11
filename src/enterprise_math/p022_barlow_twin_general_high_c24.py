"""Quadratic-linear fixed-transfer pair on the c=24 simple-high sector.

In the general simple high-digit secondary branch write a=r+h.  The target
residue class q=23 (mod 24) corresponds to c=24, hence

    q = 8(r-h)-25.

The secondary low zero simplifies to

    b = r + 8h^2 + 25h + 18.

Therefore its distance from the high zero is

    b-a = 8h^2+24h+18 = 2(2h+3)^2.

Put

    s=2h+3.

Modulo q the high zero satisfies

    a = s+1/8,

while the universal quadratic-pair remainder transfer from the existing general
high theorem has fixed gap and start

    delta = 4s+12,
    x = (4s+5)^2/32.

Thus complete simple-high escape in the c=24 sector forces the two fixed return
conditions

    q | num H_(2s^2)(s+1/8),
    q | num H_(4s+12)((4s+5)^2/32).

At h=0, s=3, these are exactly the C18 and C24 transfers that already close the
source-high affine branch.  For h>0 this is a genuine one-parameter extension;
no universal coprimality theorem is asserted here.

The Franel recurrence is classical.  The c=24 simplification and identification
of the source-high theorem as the s=3 first member are P022-local.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd

from .p022_barlow_twin_source_high_18step import forward_zero_transfer


def _require_hidden_gap(gap: int) -> None:
    if isinstance(gap, bool) or not isinstance(gap, int) or gap < 0:
        raise ValueError("gap must be a non-negative integer")
    if gap and gap % 3:
        raise ValueError("hidden twin-center gap must be divisible by three")


def c24_shift_parameter(gap: int) -> int:
    """s=2h+3."""
    _require_hidden_gap(gap)
    return 2 * gap + 3


def c24_high_to_low_gap(gap: int) -> int:
    """Exact b-a distance 2(2h+3)^2."""
    s = c24_shift_parameter(gap)
    direct = 8 * gap * gap + 24 * gap + 18
    if direct != 2 * s * s:
        raise AssertionError("c24 quadratic gap identity changed")
    return direct


def c24_fixed_transfer_parameters(
    gap: int,
) -> tuple[Fraction, int, Fraction, int]:
    """Return (high_start,quadratic_gap,quad_start,linear_gap)."""
    s = c24_shift_parameter(gap)
    high_start = Fraction(8 * s + 1, 8)  # s+1/8
    quadratic_gap = 2 * s * s
    linear_gap = 4 * s + 12
    quadratic_start = Fraction((4 * s + 5) ** 2, 32)
    if linear_gap != 8 * gap + 24:
        raise AssertionError("c24 linear transfer gap changed")
    return high_start, quadratic_gap, quadratic_start, linear_gap


def c24_fixed_transfers(gap: int) -> tuple[Fraction, Fraction]:
    """Return the quadratic-length and linear-length fixed Franel transfers."""
    high_start, quadratic_gap, quadratic_start, linear_gap = c24_fixed_transfer_parameters(gap)
    return (
        forward_zero_transfer(high_start, quadratic_gap),
        forward_zero_transfer(quadratic_start, linear_gap),
    )


def c24_fixed_numerator_gcd(gap: int) -> int:
    """Exact gcd of the two c24 fixed transfer numerators for one h."""
    left, right = c24_fixed_transfers(gap)
    return gcd(abs(left.numerator), abs(right.numerator))


def c24_source_high_specializes_to_18_24() -> bool:
    """At h=0 recover starts/gaps (25/8,18) and (289/32,24)."""
    params = c24_fixed_transfer_parameters(0)
    expected = (Fraction(25, 8), 18, Fraction(289, 32), 24)
    if params != expected:
        raise AssertionError("source-high C18/C24 specialization changed")
    return True
