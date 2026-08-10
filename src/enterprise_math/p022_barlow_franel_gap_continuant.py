"""Eliminate the moving midpoint offset from a dangerous Franel double hit.

Use either universal midpoint companion C=H or C=K.  If C_d=0 and the next
hit is e=d+g, then recurrence nonadjacency makes C_(d+1) a unit modulo the
prime and

    C_(d+g) = C_(d+1) P_g(d),

where P_0=0, P_1=1 and

    P_(j+1)(x)=-(28(x+j)^2+1)P_j(x)
                +8(2(x+j)-1)^4 P_(j-1)(x).

For the primitive/terminal geometry g=r-2 and

    q = 2d+4g+5.

Modulo q we may therefore substitute d=-(4g+5)/2.  Define

    R_r = P_(r-2)(-(4r-3)/2).

The substituted arguments are half-integers, but every recurrence coefficient
is integral: 28x^2+1 and 8(2x-1)^4 are integers there.  Hence R_r is an integer.
Any large-prime primitive terminal double hit q>4r-3 must divide both F_r and
R_r.  This turns the moving two-offset problem into the primitive part of the
fixed gcd gcd(F_r,R_r).
"""

from __future__ import annotations

from fractions import Fraction

from .p022_barlow_franel_companion_last_hit import primitive_terminal_last_hit_signature


def _continuant_a(value: Fraction) -> Fraction:
    return -(28 * value * value + 1)


def _continuant_b(value: Fraction) -> Fraction:
    return 8 * (2 * value - 1) ** 4


def companion_gap_transfer(start: int | Fraction, gap: int) -> Fraction:
    """P_gap(start) for a normalized zero followed by unit value one."""
    if isinstance(gap, bool) or not isinstance(gap, int) or gap < 0:
        raise ValueError("gap must be a non-negative integer")
    x0 = Fraction(start)
    if gap == 0:
        return Fraction(0, 1)
    previous = Fraction(0, 1)
    current = Fraction(1, 1)
    for step in range(1, gap):
        value = x0 + step
        previous, current = (
            current,
            _continuant_a(value) * current + _continuant_b(value) * previous,
        )
    return current


def eliminated_gap_transfer(rank: int) -> int:
    """Return the fixed integer R_r after eliminating the terminal offset d."""
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 3:
        raise ValueError("rank must be an integer at least three")
    gap = rank - 2
    start = Fraction(-(4 * gap + 5), 2)  # = -(4r-3)/2
    value = companion_gap_transfer(start, gap)
    if value.denominator != 1:
        raise AssertionError("half-integral specialization must be integral")
    return value.numerator


def affine_gap_mod_value(rank: int, prime: int, terminal_offset: int) -> tuple[int, int]:
    """Compare P_(r-2)(d) with R_r modulo the affine prime q.

    The identity q=2d+4(r-2)+5 makes d congruent to -(4r-3)/2 mod q.
    """
    if isinstance(prime, bool) or not isinstance(prime, int) or prime <= 2:
        raise ValueError("prime must be an odd integer greater than two")
    if isinstance(terminal_offset, bool) or not isinstance(terminal_offset, int) or terminal_offset <= 0:
        raise ValueError("terminal_offset must be positive")
    gap = rank - 2
    if prime != 2 * terminal_offset + 4 * gap + 5:
        raise ValueError("prime and terminal offset do not satisfy the affine geometry")
    moving = companion_gap_transfer(terminal_offset, gap)
    if moving.denominator != 1:
        raise AssertionError("integer start must give an integer continuant")
    fixed = eliminated_gap_transfer(rank)
    if moving.numerator % prime != fixed % prime:
        raise AssertionError("affine offset elimination failed modulo q")
    return moving.numerator % prime, fixed % prime


def primitive_terminal_double_hit_forces_fixed_divisor(rank: int, prime: int) -> int:
    """Conditional theorem: a primitive terminal double hit forces q|R_r."""
    d, e, _ = primitive_terminal_last_hit_signature(rank, prime)
    if e - d != rank - 2:
        raise AssertionError("primitive/terminal gap changed")
    moving_residue, fixed_residue = affine_gap_mod_value(rank, prime, d)
    if moving_residue != 0 or fixed_residue != 0:
        raise AssertionError("two companion hits must annihilate the gap continuant")
    return eliminated_gap_transfer(rank)
