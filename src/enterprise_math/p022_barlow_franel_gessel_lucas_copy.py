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

Write h=v_p(F_r), u=F_r/p mod p, and d=F'_r mod p.  For every nonzero
multiplier a with F_a a p-unit,

    F_(a*p+r)/p = F_a (u+a*d)                           (mod p).

If h=1 then u is nonzero, so two distinct multipliers modulo p cannot both
raise the copied depth above one.  If h>=2 then u=0: when d is nonzero every
nonzero multiplier actually gives copied depth exactly one.  The sole case not
resolved by the mod-p^2 first jet is therefore the double-stationary source

    p^2 | F_r  and  p | F'_r.

For a nontrivial twin-prime deferral center r>=6, choose a0 in {1,2} so that
3 divides 2(a0*p+r)-1, and pair it with a0+3.  Both odd boundaries are then
nontrivial multiples of three.  Since a0+3<r, both multiplier Franel factors
are p-units by primitivity.  Outside the double-stationary obstruction, at
least one of these two actual composite defect numerators has p-adic depth
exactly one.  Defect capture still requires handling canonical A-support.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, gcd

from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import p_adic_valuation, triple_moment_factor
from .p022_barlow_lucas_copy_capture import forced_copy_multiplier
from .p022_barlow_primitive_defect_criterion import is_primitive_franel_divisor
from .p022_barlow_primitive_successor_capture import is_twin_prime_deferral_center


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
    if gcd(denominator, modulus) != 1:
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


def source_first_jet_data(rank: int, prime: int) -> tuple[int, int, int]:
    """Return (source depth, F_r/p mod p, F'_r mod p) at a primitive zero."""
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at rank")
    source = triple_moment_factor(rank)
    depth = p_adic_valuation(source, prime)
    if depth <= 0:
        raise AssertionError("primitive source depth must be positive")
    source_unit = (source // prime) % prime
    derivative = _fraction_mod(franel_formal_derivative(rank), prime)
    if depth >= 2 and source_unit != 0:
        raise AssertionError("depth at least two must kill the source quotient modulo p")
    if depth == 1 and source_unit == 0:
        raise AssertionError("simple source depth must leave a nonzero quotient")
    return depth, source_unit, derivative


def copy_quotient_linear_residue(rank: int, prime: int, multiplier: int) -> tuple[int, int]:
    """Return actual/predicted F_(a*p+r)/(p F_a) modulo p.

    A nonzero result is equivalent to the copied Franel numerator having exact
    p-adic depth one.  The multiplier must have p-unit Franel value.
    """
    if not 0 < multiplier < prime:
        raise ValueError("multiplier must lie in 1..p-1")
    fa = triple_moment_factor(multiplier)
    if fa % prime == 0:
        raise ValueError("multiplier Franel factor must be a p-unit")
    _, source_unit, derivative = source_first_jet_data(rank, prime)
    actual_square, _ = franel_gessel_lucas_mod_square(rank, prime, multiplier)
    if actual_square % prime:
        raise AssertionError("p-Lucas copy must remain divisible by p")
    actual_over_p = (actual_square // prime) % prime
    actual = actual_over_p * pow(fa % prime, -1, prime) % prime
    predicted = (source_unit + multiplier * derivative) % prime
    if actual != predicted:
        raise AssertionError("copy first-jet quotient disagrees with Gessel-Lucas")
    return actual, predicted


def simple_zero_copy_linear_residue(rank: int, prime: int, multiplier: int) -> tuple[int, int]:
    """Compatibility helper returning F_(a*p+r)/p modulo p at a simple zero."""
    depth, _, _ = source_first_jet_data(rank, prime)
    if depth != 1:
        raise ValueError("source rank must have exact p-adic depth one")
    quotient, _ = copy_quotient_linear_residue(rank, prime, multiplier)
    fa = triple_moment_factor(multiplier) % prime
    actual = quotient * fa % prime
    _, predicted_square = franel_gessel_lucas_mod_square(rank, prime, multiplier)
    predicted = (predicted_square // prime) % prime
    if actual != predicted:
        raise AssertionError("simple copy compatibility normalization failed")
    return actual, predicted


def two_multipliers_cannot_both_raise_depth(
    rank: int,
    prime: int,
    first: int,
    second: int,
) -> tuple[int, int]:
    """At a simple source zero, at least one distinct copy stays depth one."""
    depth, source_unit, derivative = source_first_jet_data(rank, prime)
    if depth != 1:
        raise ValueError("source rank must have exact p-adic depth one")
    if first % prime == second % prime:
        raise ValueError("multipliers must be distinct modulo p")
    first_residue, _ = copy_quotient_linear_residue(rank, prime, first)
    second_residue, _ = copy_quotient_linear_residue(rank, prime, second)
    if first_residue == 0 and second_residue == 0:
        if ((first - second) * derivative) % prime != 0:
            raise AssertionError("two vanishing copy jets contradict subtraction")
        if derivative % prime != 0:
            raise AssertionError("distinct multipliers force derivative zero")
        if source_unit == 0:
            raise AssertionError("simple source depth gives a nonzero unit")
        raise AssertionError("two copy depths cannot both rise above one")
    return first_residue, second_residue


def copy_depth_obstruction(rank: int, prime: int) -> tuple[int, int, bool]:
    """Return (depth, derivative mod p, double-stationary obstruction flag).

    If the flag is false then suitable nonzero p-unit multipliers produce copied
    Franel numerators of exact p-adic depth one.  The only case not decided by
    the first jet is p^2|F_r together with p|F'_r.
    """
    depth, _, derivative = source_first_jet_data(rank, prime)
    return depth, derivative, depth >= 2 and derivative == 0


def forced_composite_copy_pair(
    rank: int,
    prime: int,
) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    """Two guaranteed composite copies with first-jet quotient residues.

    Returns ((a0,N0,residue0),(a1,N1,residue1)).  Outside the double-stationary
    obstruction at least one residue is nonzero; for source depth >=2 with
    nonzero derivative, both residues are nonzero.
    """
    if rank < 6 or not is_twin_prime_deferral_center(rank):
        raise ValueError("rank must be a twin-prime deferral center at least six")
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at rank")
    if rank % 3:
        raise AssertionError("nontrivial twin centers are divisible by three")

    first = forced_copy_multiplier(prime)
    second = first + 3
    if second >= rank:
        raise AssertionError("r>=6 keeps both copy multipliers below the primitive rank")

    output = []
    for multiplier in (first, second):
        segment = multiplier * prime + rank
        boundary = 2 * segment - 1
        if boundary <= 3 or boundary % 3:
            raise AssertionError("same-mod-three forced copy must have composite boundary")
        if _is_prime(boundary):
            raise AssertionError("forced copy boundary unexpectedly prime")
        if triple_moment_factor(multiplier) % prime == 0:
            raise AssertionError("preprimitive multiplier must be a p-unit")
        residue, _ = copy_quotient_linear_residue(rank, prime, multiplier)
        output.append((multiplier, segment, residue))

    depth, derivative, exceptional = copy_depth_obstruction(rank, prime)
    residues = tuple(residue for _, _, residue in output)
    if not exceptional:
        if depth == 1 and not any(residues):
            raise AssertionError("two distinct simple-source copies cannot both rise in depth")
        if depth >= 2 and derivative != 0 and not all(residues):
            raise AssertionError("nonzero derivative makes every nonzero multiplier copy simple")
    return output[0], output[1]


def forced_composite_depth_one_pair(
    rank: int,
    prime: int,
) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    """Depth-one compatibility wrapper for the forced composite copy pair."""
    depth, _, _ = source_first_jet_data(rank, prime)
    if depth != 1:
        raise ValueError("primitive source must have exact p-adic depth one")
    output = forced_composite_copy_pair(rank, prime)
    if not any(residue for _, _, residue in output):
        raise AssertionError("at least one forced composite copy must retain depth one")
    return output
