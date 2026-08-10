"""Exact equivalence between a large terminal Franel zero and the fixed R_r.

Let q be an odd prime, q>4r-3, and assume q|F_r.  In universal midpoint
coordinates the source zero is at e=m-r and the terminal index 2r-2 is at
 d=m-(2r-2), with e-d=r-2.

The transfer matrix from (C_d,C_(d+1)) to (C_e,C_(e+1)) is a product of
second-order recurrence matrices with determinant factors

    -8(2n-1)^4.

All these factors are q-units because e<m=(q-1)/2.  Its first-row second entry
is P_(r-2)(d).  The affine identity q=2d+4(r-2)+5 identifies this entry modulo q
with the fixed integer R_r.  Since the matrix is invertible, when C_e=0 we have

    C_d=0  iff  P_(r-2)(d)=0  iff  R_r=0  (mod q).

The universal companion dictionary converts C_d=0 back to q|F_(2r-2).
Therefore, under q|F_r and q>4r-3,

    q|F_(2r-2)  iff  q|R_r.

This is an exact replacement of the moving terminal gcd by one fixed integer.
"""

from __future__ import annotations

from fractions import Fraction

from .p022_barlow_franel_gap_continuant import (
    _continuant_a,
    _continuant_b,
    affine_gap_mod_value,
    eliminated_gap_transfer,
)
from .p022_barlow_franel_universal_companion import (
    terminal_companion_offsets,
    universal_companion_value,
)
from .p022_barlow_low_order_defect_reduction import _is_prime

Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def _matmul(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def companion_gap_transfer_matrix(start: int, gap: int) -> Matrix2:
    """Map (C_d,C_(d+1)) to (C_(d+g),C_(d+g+1))."""
    if isinstance(start, bool) or not isinstance(start, int) or start < 0:
        raise ValueError("start must be a non-negative integer")
    if isinstance(gap, bool) or not isinstance(gap, int) or gap < 0:
        raise ValueError("gap must be a non-negative integer")
    matrix: Matrix2 = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    for step in range(1, gap + 1):
        index = Fraction(start + step)
        transition: Matrix2 = (
            (Fraction(0), Fraction(1)),
            (_continuant_b(index), _continuant_a(index)),
        )
        matrix = _matmul(transition, matrix)
    return matrix


def companion_gap_transfer_determinant(start: int, gap: int) -> int:
    matrix = companion_gap_transfer_matrix(start, gap)
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if determinant.denominator != 1:
        raise AssertionError("integer-start transfer determinant must be integral")
    expected = 1
    for step in range(1, gap + 1):
        expected *= -8 * (2 * (start + step) - 1) ** 4
    if determinant.numerator != expected:
        raise AssertionError("gap transfer determinant product changed")
    return expected


def large_terminal_zero_iff_fixed_gap_divisor(rank: int, prime: int) -> bool:
    """Certify q|F_(2r-2) iff q|R_r under q|F_r and q>4r-3."""
    if isinstance(prime, bool) or not isinstance(prime, int) or prime <= 2 or not _is_prime(prime):
        raise ValueError("prime must be an odd prime")
    d, e = terminal_companion_offsets(rank, prime)
    if universal_companion_value(prime, e) % prime:
        raise ValueError("prime must divide F_r / the source companion value")
    gap = rank - 2
    if e != d + gap:
        raise AssertionError("source/terminal gap changed")
    matrix = companion_gap_transfer_matrix(d, gap)
    determinant = companion_gap_transfer_determinant(d, gap)
    if determinant % prime == 0:
        raise AssertionError("large-prime transfer matrix must be invertible modulo q")
    moving, fixed = affine_gap_mod_value(rank, prime, d)
    if matrix[0][1].denominator != 1 or matrix[0][1].numerator % prime != moving:
        raise AssertionError("first-row transfer coefficient must be the gap continuant")
    terminal_zero = universal_companion_value(prime, d) % prime == 0
    fixed_zero = eliminated_gap_transfer(rank) % prime == 0
    if fixed != 0 and fixed_zero:
        raise AssertionError("fixed residue bookkeeping changed")
    if terminal_zero != fixed_zero:
        raise AssertionError("invertible transfer makes terminal zero equivalent to q|R_r")
    return terminal_zero
