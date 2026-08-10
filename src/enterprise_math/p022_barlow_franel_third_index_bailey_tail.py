"""Bailey pole-tail reduction for the Franel one-third index.

Let p=6d+5 be prime and put

    r=(p+1)/3=2d+2,     M=d+1=(p+1)/6.

Modulo p the Franel value F_r is the truncated hypergeometric sum with three
upper parameters -1/3.  A q->1 specialization of the Wang--Xu Bailey
transformation supercongruence rewrites that sum modulo p^2 as p times another
truncated hypergeometric sum.  One must not discard the latter modulo p: its
(5/6)_k denominator contains exactly one factor p once k>=d+1.

Extracting that unique pole gives the exact mod-p reduction

    F_r = - C_d H_d                              (mod p),

where C_d is a p-adic unit and

    H_d = sum_(j=0)^(d+1)
          (-1/6)_j^2 (2/3)_j
          -------------------- .
          (7/6)_j (1/2)_j j!

Consequently

    p | F_((p+1)/3)    iff    p | H_d.

This is useful because the moving Franel index has disappeared.  Moreover
M=d+1=(p+1)/6, so modulo p

    (-1/6,-1/6,2/3; 7/6,1/2)
      = (-M,-M,4M; M+1,3M).

Thus H_d is the natural terminating value

    3F2(-M,-M,4M; M+1,3M; 1),

with M=(p+1)/6.  The remaining P022 boundary problem is therefore a fixed
terminating hypergeometric nonvanishing problem rather than an arbitrary
Franel special value.

Prior-art boundary: the Bailey q-supercongruence used as input is due to
Xiaoxia Wang and Chang Xu, "New q-supercongruences from the Bailey
transformation" (2022).  The pole extraction and its identification with the
P022 third-index obstruction are the contribution recorded here.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial

from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import triple_moment_factor


def _pochhammer(value: Fraction, length: int) -> Fraction:
    result = Fraction(1, 1)
    for step in range(length):
        result *= value + step
    return result


def _fraction_mod_prime(value: Fraction, prime: int) -> int:
    denominator = value.denominator % prime
    if denominator == 0:
        raise ValueError("fraction denominator is not a p-adic unit")
    return value.numerator % prime * pow(denominator, -1, prime) % prime


def _require_third_index_prime(prime: int) -> tuple[int, int, int]:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 5
        or not _is_prime(prime)
        or prime % 6 != 5
    ):
        raise ValueError("prime must be 5 modulo 6")
    d = (prime - 5) // 6
    rank = (prime + 1) // 3
    truncation = d + 1
    if rank != 2 * truncation:
        raise AssertionError("third-index parameterization changed")
    return rank, d, truncation


def bailey_pole_tail_sum(offset: int) -> Fraction:
    """Return the universal rational H_d before reduction modulo p."""
    if isinstance(offset, bool) or not isinstance(offset, int) or offset < 0:
        raise ValueError("offset must be a non-negative integer")
    total = Fraction(0, 1)
    for j in range(offset + 2):
        total += (
            _pochhammer(Fraction(-1, 6), j) ** 2
            * _pochhammer(Fraction(2, 3), j)
            / (
                _pochhammer(Fraction(7, 6), j)
                * _pochhammer(Fraction(1, 2), j)
                * factorial(j)
            )
        )
    return total


def bailey_pole_tail_unit(offset: int) -> Fraction:
    """Return the p-adic unit C_d multiplying H_d after pole extraction."""
    if isinstance(offset, bool) or not isinstance(offset, int) or offset < 0:
        raise ValueError("offset must be a non-negative integer")
    k = offset + 1
    return (
        6
        * _pochhammer(Fraction(-1, 3), k) ** 2
        * _pochhammer(Fraction(1, 2), k)
        / (
            factorial(k)
            * _pochhammer(Fraction(1, 3), k)
            * _pochhammer(Fraction(5, 6), offset)
        )
    )


def bailey_tail_integer_parameters(prime: int) -> tuple[int, int, int, int, int]:
    """Return (-M,-M,4M;M+1,3M) for the naturally terminating tail."""
    _, _, truncation = _require_third_index_prime(prime)
    M = truncation
    residues = (-M, -M, 4 * M, M + 1, 3 * M)
    rational_parameters = (
        Fraction(-1, 6),
        Fraction(-1, 6),
        Fraction(2, 3),
        Fraction(7, 6),
        Fraction(1, 2),
    )
    for integer_parameter, rational_parameter in zip(residues, rational_parameters):
        if integer_parameter % prime != _fraction_mod_prime(rational_parameter, prime):
            raise AssertionError("terminating integer parameters do not match modulo p")
    return residues


def bailey_pole_tail_residue(prime: int) -> tuple[int, int, int, int]:
    """Return (rank,d,C_d mod p,H_d mod p) and certify F_r=-C_d H_d."""
    rank, offset, _ = _require_third_index_prime(prime)
    unit = _fraction_mod_prime(bailey_pole_tail_unit(offset), prime)
    tail = _fraction_mod_prime(bailey_pole_tail_sum(offset), prime)
    actual = triple_moment_factor(rank) % prime
    predicted = (-unit * tail) % prime
    if unit == 0:
        raise AssertionError("the extracted Bailey prefactor must be a p-adic unit")
    if actual != predicted:
        raise AssertionError("Bailey pole-tail reduction disagrees with the Franel value")
    return rank, offset, unit, tail


def third_index_zero_via_bailey_tail(prime: int) -> bool:
    """Certify p|F_((p+1)/3) iff the universal Bailey tail vanishes mod p."""
    rank, _, _, tail = bailey_pole_tail_residue(prime)
    actual = triple_moment_factor(rank) % prime == 0
    predicted = tail == 0
    if actual != predicted:
        raise AssertionError("Bailey tail zero equivalence failed")
    return actual
