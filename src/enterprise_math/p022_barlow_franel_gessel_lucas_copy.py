"""First-jet control of p-Lucas copies of a Franel zero.

The Franel sequence is Zagier's sporadic Apéry-like sequence with recurrence
parameters (a,b,c)=(7,2,-8).  Straub's Gessel--Lucas theorem for sporadic
Apéry-like sequences therefore gives, for an odd prime p and 0<=k<p,

    F_(p*n+k) = F_k F_n + p*n F'_k F_n                 (mod p^2),

where F'_k is the formal derivative of the recurrence sequence.  This theorem
is prior art (Straub, 2023).

For Franel numbers the formal derivative admits the explicit harmonic form

    F'_n = 3 sum_(j=0)^n C(n,j)^3 (H_n-H_(n-j)).

It is equivalently characterized by differentiating the polynomial-coefficient
Franel recurrence.  This module checks that characterization exactly and then
packages the P022 consequence for a primitive copy N=a*p+r.

If p divides F_r simply, write u=F_r/p mod p and d=F'_r mod p.  For every
multiplier a with F_a a p-unit,

    F_(a*p+r)/p = F_a (u+a*d)                           (mod p).

Since u is nonzero, two distinct multipliers modulo p cannot both make the
right side vanish.  Thus among any two such multipliers at least one p-Lucas
copy has exact p-adic depth one.  This controls the numerator depth; defect
capture still requires handling the canonical A-support separately.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb

from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import p_adic_valuation, triple_moment_factor


def harmonic_number(index: int) -> Fraction:
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be non-negative")
    return sum((Fraction(1, j) for j in range(1, index + 1)), Fraction(0, 1))


def franel_formal_derivative(index: int) -> Fraction:
    """Exact Straub formal derivative for the Franel recurrence."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be non-negative")
    h = harmonic_number(index)
    return 3 * sum(
        (
            Fraction(comb(index, k) ** 3, 1)
            * (h - harmonic_number(index - k))
        )
        for k in range(index + 1)
    )


def franel_formal_derivative_recurrence_residual(index: int) -> Fraction:
    """Residual of the differentiated Franel recurrence at n=index>=1."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 1:
        raise ValueError("index must be positive")
    n = index
    fm1 = triple_moment_factor(n - 1) if n > 1 else 1
    f0 = triple_moment_factor(n)
    fp1 = triple_moment_factor(n + 1)
    dm1 = franel_formal_derivative(n - 1)
    d0 = franel_formal_derivative(n)
    dp1 = franel_formal_derivative(n + 1)
    return (
        (n + 1) ** 2 * dp1
        - (7 * n * n + 7 * n + 2) * d0
        - 8 * n * n * dm1
        + 2 * (n + 1) * fp1
        - (14 * n + 7) * f0
        - 16 * n * fm1
    )


def _fraction_mod(value: Fraction, modulus: int) -> int:
    denominator = value.denominator % modulus
    if denominator == 0:
        raise ValueError("fraction denominator is not a unit modulo the modulus")
    return value.numerator % modulus * pow(denominator, -1, modulus) % modulus


def franel_gessel_lucas_mod_square(rank: int, prime: int, multiplier: int) -> tuple[int, int]:
    """Return actual/predicted F_(p*a+r) residues modulo p^2.

    This is an executable specialization of Straub's prior-art theorem to the
    Franel sequence.  The helper is intended for bounded verification, not as
    an independent proof of the literature theorem.
    """
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 3
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")
    if isinstance(rank, bool) or not isinstance(rank, int) or not 0 <= rank < prime:
        raise ValueError("rank must lie in 0..p-1")
    if isinstance(multiplier, bool) or not isinstance(multiplier, int) or multiplier < 0:
        raise ValueError("multiplier must be non-negative")

    modulus = prime * prime
    derivative = _fraction_mod(franel_formal_derivative(rank), modulus)
    fr = 1 if rank == 0 else triple_moment_factor(rank)
    fa = 1 if multiplier == 0 else triple_moment_factor(multiplier)
    predicted = (fr * fa + prime * multiplier * derivative * fa) % modulus
    actual = triple_moment_factor(prime * multiplier + rank) % modulus
    if actual != predicted:
        raise AssertionError("Franel Gessel-Lucas p^2 specialization failed")
    return actual, predicted


def simple_zero_copy_linear_residue(rank: int, prime: int, multiplier: int) -> tuple[int, int]:
    """Return actual/predicted F_(a*p+r)/p residues modulo p at a simple zero."""
    if p_adic_valuation(triple_moment_factor(rank), prime) != 1:
        raise ValueError("source rank must have exact p-adic depth one")
    if not 0 < multiplier < prime:
        raise ValueError("multiplier must lie in 1..p-1")
    fa = triple_moment_factor(multiplier)
    if fa % prime == 0:
        raise ValueError("multiplier Franel factor must be a p-unit")

    actual_square, _ = franel_gessel_lucas_mod_square(rank, prime, multiplier)
    if actual_square % prime:
        raise AssertionError("p-Lucas copy must remain divisible by p")
    actual = (actual_square // prime) % prime
    source_unit = (triple_moment_factor(rank) // prime) % prime
    derivative = _fraction_mod(franel_formal_derivative(rank), prime)
    predicted = (fa % prime) * (source_unit + multiplier * derivative) % prime
    if actual != predicted:
        raise AssertionError("copy first-jet residue disagrees with Gessel-Lucas")
    return actual, predicted


def two_multipliers_cannot_both_raise_depth(
    rank: int,
    prime: int,
    first: int,
    second: int,
) -> tuple[int, int]:
    """At a simple source zero, at least one distinct copy stays depth one."""
    if first % prime == second % prime:
        raise ValueError("multipliers must be distinct modulo p")
    first_residue, _ = simple_zero_copy_linear_residue(rank, prime, first)
    second_residue, _ = simple_zero_copy_linear_residue(rank, prime, second)
    if first_residue == 0 and second_residue == 0:
        source_unit = (triple_moment_factor(rank) // prime) % prime
        derivative = _fraction_mod(franel_formal_derivative(rank), prime)
        # Subtracting the two linear equations gives (a-b)d=0.  If d=0,
        # either equation then forces source_unit=0, contradicting simplicity.
        if ((first - second) * derivative) % prime != 0:
            raise AssertionError("two vanishing copy jets contradict subtraction")
        if derivative % prime != 0:
            raise AssertionError("distinct multipliers force derivative zero")
        if source_unit == 0:
            raise AssertionError("simple source depth gives a nonzero unit")
        raise AssertionError("two copy depths cannot both rise above one")
    return first_residue, second_residue
