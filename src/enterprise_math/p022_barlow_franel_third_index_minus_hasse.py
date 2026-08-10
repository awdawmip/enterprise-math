"""Whipple bridge from the Franel one-third-minus value to the scalar Hasse period.

For k>=1 the Franel number at n=2k-1 is

    F_(2k-1) = 3F2(1-2k,1-2k,1-2k;1,1;-1).

Whipple's classical quadratic transformation gives the exact terminating identity

    F_(2k-1)
      = 2^(2k-1) 3F2(2k,1/2-k,1-k;1,1;1).

Now let q=6k-1 be prime.  Modulo q the three upper parameters become
1/3,1/3,5/6, while 1-k terminates the series at j=k-1.  Therefore

    F_((q-2)/3) = 2^((q-2)/3) P_q(1)  (mod q),

where P_q is the canonical rank-three Hasse polynomial already used by the
one-third-plus first-jet theorem.

For forced-midpoint primes q=5 or 7 (mod 8), the diagonal midpoint companion
K_k detects the same zero.  Hence the previously isolated diagonal companion
obstruction is exactly the canonical scalar-Hasse obstruction, up to an
explicit q-adic unit.

Whipple's transformation is classical prior art (DLMF 16.6.1).  P022 content
is the specialization q=6k-1 and the identification with the existing Hasse
coordinate and forced-midpoint companion.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial

from .p022_barlow_franel_half_index import (
    half_index,
    half_index_is_forced_zero,
)
from .p022_barlow_franel_half_integer_solution import (
    integer_midpoint_companion,
    odd_double_factorial,
)
from .p022_barlow_franel_third_index_hasse_jet import (
    canonical_period_jet_residue,
)
from .p022_barlow_half_defect_obstructions import franel_recurrence_table_mod
from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import triple_moment_factor


def _pochhammer(value: Fraction, length: int) -> Fraction:
    result = Fraction(1)
    for step in range(length):
        result *= value + step
    return result


def _require_k(k: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise ValueError("k must be a positive integer")


def _require_six_k_minus_one_prime(prime: int) -> int:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 5
        or not _is_prime(prime)
        or prime % 6 != 5
    ):
        raise ValueError("prime must be 5 modulo 6")
    return (prime + 1) // 6


def whipple_third_minus_sum(k: int) -> Fraction:
    """Return the exact transformed 3F2 value before the power-of-two factor."""
    _require_k(k)
    total = Fraction(0)
    for index in range(k):
        total += (
            _pochhammer(Fraction(2 * k), index)
            * _pochhammer(Fraction(1, 2) - k, index)
            * _pochhammer(Fraction(1 - k), index)
            / factorial(index) ** 3
        )
    return total


def whipple_third_minus_identity(k: int) -> bool:
    """Certify F_(2k-1)=2^(2k-1) times the terminating Whipple transform."""
    _require_k(k)
    index = 2 * k - 1
    transformed = 2**index * whipple_third_minus_sum(k)
    if transformed.denominator != 1:
        raise AssertionError("terminating Whipple value must be integral here")
    if transformed.numerator != triple_moment_factor(index):
        raise AssertionError("Whipple transform disagrees with the Franel number")
    return True


def third_minus_hasse_bridge(prime: int) -> tuple[int, int, int, int]:
    """Return (k,F_(2k-1),P_q(1),2^(2k-1)P_q(1)) modulo q."""
    k = _require_six_k_minus_one_prime(prime)
    index = 2 * k - 1
    _, period, _ = canonical_period_jet_residue(prime)
    franel = franel_recurrence_table_mod(prime, prime, index)[index]
    predicted = pow(2, index, prime) * period % prime
    if franel != predicted:
        raise AssertionError("one-third-minus Franel value must equal the scalar Hasse period up to 2^n")
    return k, franel, period, predicted


def third_minus_zero_iff_scalar_hasse_zero(prime: int) -> bool:
    """Exact mod-q equivalence F_((q-2)/3)=0 iff P_q(1)=0."""
    _, franel, period, _ = third_minus_hasse_bridge(prime)
    if (franel == 0) != (period == 0):
        raise AssertionError("power-of-two unit cannot change zero status")
    return franel == 0


def forced_diagonal_companion_hasse_bridge(
    prime: int,
) -> tuple[int, int, int, int]:
    """Return (k,K_k,P_q(1),unit*P_q(1)) for forced-midpoint q=6k-1."""
    k = _require_six_k_minus_one_prime(prime)
    if not half_index_is_forced_zero(prime):
        raise ValueError("prime must also lie in the forced-midpoint mod-8 sector")

    midpoint = half_index(prime)
    index = 2 * k - 1
    if midpoint - k != index:
        raise AssertionError("diagonal midpoint offset arithmetic changed")

    table = franel_recurrence_table_mod(prime, prime, midpoint)
    previous_midpoint = table[midpoint - 1]
    if previous_midpoint == 0:
        raise AssertionError("the forced midpoint cannot have an adjacent zero")

    _, franel, period, _ = third_minus_hasse_bridge(prime)
    odd_factorial = odd_double_factorial(2 * k - 1) % prime
    factor = (
        -odd_factorial
        * odd_factorial
        * pow(-8, k, prime)
        * pow(8, -1, prime)
    ) % prime
    unit = factor * pow(2, index, prime) % prime
    unit = unit * pow(previous_midpoint, -1, prime) % prime
    if unit == 0:
        raise AssertionError("all diagonal normalization factors must be q-units")

    companion = integer_midpoint_companion(k) % prime
    predicted = unit * period % prime
    direct = factor * franel % prime * pow(previous_midpoint, -1, prime) % prime
    if companion != predicted or companion != direct:
        raise AssertionError("diagonal companion and scalar Hasse coordinates disagree")
    return k, companion, period, predicted


def forced_diagonal_zero_iff_scalar_hasse_zero(prime: int) -> bool:
    """For q=5,7 mod8 and q=5 mod6, certify K_k=0 iff P_q(1)=0."""
    _, companion, period, _ = forced_diagonal_companion_hasse_bridge(prime)
    if (companion == 0) != (period == 0):
        raise AssertionError("q-unit diagonal normalization cannot change zero status")
    return companion == 0
