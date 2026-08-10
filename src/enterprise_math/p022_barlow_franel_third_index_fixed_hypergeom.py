"""Fixed-parameter full-truncation form of the Franel one-third obstruction.

For a prime p=6M-1, the integerized Bailey tail is

    U_M = sum_{k=0}^M C(M,k) C(2M+k,k) C(4M-1,k).

Modulo p its summand is

    (-1/6)_k (1/3)_k (4/3)_k / (1)_k^3.

Moreover the transition from k=M to k=M+1 contains the factor 6M-1=p.
Hence every later term through k=p-1 vanishes modulo p, and the one-third
Franel zero is equivalent to a standard full p-1 truncated fixed-parameter
3F2 congruence.
"""

from __future__ import annotations

from fractions import Fraction

from .p022_barlow_franel_third_index_bailey_tail import (
    bailey_symmetric_integer_sum,
    third_index_zero_via_integer_sum,
)
from .p022_barlow_low_order_defect_reduction import _is_prime


def _require_third_index_prime(prime: int) -> int:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 5
        or not _is_prime(prime)
        or prime % 6 != 5
    ):
        raise ValueError("prime must be 5 modulo 6")
    return (prime + 1) // 6


def fixed_parameter_term_ratio(index: int) -> Fraction:
    """Return a_(k+1)/a_k for datum (-1/6,1/3,4/3;1,1)."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a non-negative integer")
    k = index
    return Fraction(
        (6 * k - 1) * (3 * k + 1) * (3 * k + 4),
        54 * (k + 1) ** 3,
    )


def fixed_parameter_truncation_residue(prime: int) -> tuple[int, int]:
    """Return (M,sum through M) for the fixed 3F2 datum modulo p."""
    M = _require_third_index_prime(prime)
    term = 1
    total = 1
    inv54 = pow(54, -1, prime)
    for k in range(M):
        numerator = (6 * k - 1) * (3 * k + 1) * (3 * k + 4)
        denominator_unit = pow(k + 1, 3, prime)
        term = (
            term
            * (numerator % prime)
            * inv54
            * pow(denominator_unit, -1, prime)
        ) % prime
        total = (total + term) % prime
    return M, total


def fixed_parameter_full_truncation_residue(prime: int) -> int:
    """Return the full k=0..p-1 truncation, using forced termination at M+1."""
    M, total = fixed_parameter_truncation_residue(prime)
    termination_numerator = (
        (6 * M - 1) * (3 * M + 1) * (3 * M + 4)
    )
    if termination_numerator % prime != 0:
        raise AssertionError("fixed hypergeometric tail must terminate modulo p")
    return total


def fixed_parameter_integer_bridge(prime: int) -> tuple[int, int]:
    """Return equal residues of U_M and the full fixed-parameter truncation."""
    M = _require_third_index_prime(prime)
    integer_residue = bailey_symmetric_integer_sum(M) % prime
    hypergeometric_residue = fixed_parameter_full_truncation_residue(prime)
    if integer_residue != hypergeometric_residue:
        raise AssertionError("integer sum and fixed hypergeometric datum disagree")
    return integer_residue, hypergeometric_residue


def third_index_zero_via_fixed_hypergeom(prime: int) -> bool:
    """Certify the Franel one-third zero through the full fixed 3F2 truncation."""
    residue, _ = fixed_parameter_integer_bridge(prime)
    predicted = residue == 0
    actual = third_index_zero_via_integer_sum(prime)
    if actual != predicted:
        raise AssertionError("fixed hypergeometric zero and Franel zero disagree")
    return actual
