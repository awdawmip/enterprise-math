"""Exact determinant and Smith certificate of the 40x40 Franel defect core.

The N=150 joint certificate reduces structurally to one 40x40 integer matrix.
This module proves more than nonzero determinant modulo one auxiliary prime:

    det(core) = -26622 = -2*3^3*17*29.

Two 39x39 minors have determinants -6 and -797.  Since gcd(6,797)=1, the gcd
of all 39x39 minors is one.  Standard Smith-normal-form theory then forces

    SNF(core) = diag(1,...,1,26622).

Hence the integer cokernel is cyclic of order 26622, and reduction modulo a
prime is nonsingular for every prime except 2,3,17,29.
"""

from __future__ import annotations

from math import gcd

from .p022_barlow_defect_core_compression import (
    compressed_defect_core_150,
)
from .p022_barlow_low_order_identifiability import CERTIFICATE_MODULUS
from .p022_barlow_low_order_identifiability_150 import (
    CERTIFICATE_150_DETERMINANT_RESIDUE,
)

CORE_EXACT_DETERMINANT = -26_622
CORE_MINOR_ONE = -6
CORE_MINOR_TWO = -797
CORE_SMITH_LAST_INVARIANT = 26_622
CORE_EXCEPTIONAL_PRIMES = (2, 3, 17, 29)


def exact_determinant_bareiss(matrix: tuple[tuple[int, ...], ...]) -> int:
    """Fraction-free exact determinant for an integer square matrix."""
    if not isinstance(matrix, tuple) or not matrix:
        raise ValueError("matrix must be a nonempty tuple")
    size = len(matrix)
    if any(not isinstance(row, tuple) or len(row) != size for row in matrix):
        raise ValueError("matrix must be square")
    if size == 1:
        return matrix[0][0]

    values = [list(map(int, row)) for row in matrix]
    sign = 1
    previous_pivot = 1

    for column in range(size - 1):
        pivot_row = next(
            (row for row in range(column, size) if values[row][column] != 0),
            None,
        )
        if pivot_row is None:
            return 0
        if pivot_row != column:
            values[column], values[pivot_row] = values[pivot_row], values[column]
            sign = -sign

        pivot = values[column][column]
        for row in range(column + 1, size):
            for col in range(column + 1, size):
                numerator = (
                    values[row][col] * pivot
                    - values[row][column] * values[column][col]
                )
                if column:
                    if numerator % previous_pivot:
                        raise AssertionError("Bareiss division must remain exact")
                    numerator //= previous_pivot
                values[row][col] = numerator
        previous_pivot = pivot

        for row in range(column + 1, size):
            values[row][column] = 0

    return sign * values[size - 1][size - 1]


def _delete_row_column(
    matrix: tuple[tuple[int, ...], ...], row_index: int, column_index: int
) -> tuple[tuple[int, ...], ...]:
    size = len(matrix)
    if not (0 <= row_index < size and 0 <= column_index < size):
        raise ValueError("minor indices out of range")
    return tuple(
        tuple(value for col, value in enumerate(row) if col != column_index)
        for row_index_current, row in enumerate(matrix)
        if row_index_current != row_index
    )


def exact_core_determinant_150() -> int:
    _, _, _, core = compressed_defect_core_150()
    value = exact_determinant_bareiss(core)
    if value != CORE_EXACT_DETERMINANT:
        raise AssertionError("exact 40x40 core determinant changed")
    return value


def smith_witness_minors_150() -> tuple[int, int]:
    """Two coprime 39x39 minors certifying the 39th determinantal divisor is 1."""
    _, _, _, core = compressed_defect_core_150()
    first = exact_determinant_bareiss(_delete_row_column(core, 3, 24))
    second = exact_determinant_bareiss(_delete_row_column(core, 35, 10))
    if (first, second) != (CORE_MINOR_ONE, CORE_MINOR_TWO):
        raise AssertionError("Smith witness minors changed")
    if gcd(abs(first), abs(second)) != 1:
        raise AssertionError("Smith witness minors must be coprime")
    return first, second


def smith_invariant_factors_150() -> tuple[int, ...]:
    """Certified Smith diagonal, without computing transformation matrices."""
    determinant = abs(exact_core_determinant_150())
    first, second = smith_witness_minors_150()
    if gcd(abs(first), abs(second)) != 1:
        raise AssertionError("39x39 determinantal divisor is not certified as one")
    if determinant != CORE_SMITH_LAST_INVARIANT:
        raise AssertionError("last Smith invariant changed")
    return (1,) * 39 + (determinant,)


def prime_factors_of_core_cokernel() -> tuple[int, ...]:
    """Prime characteristics in which the full-rank integer core becomes singular."""
    value = CORE_SMITH_LAST_INVARIANT
    output = []
    prime = 2
    remaining = value
    while prime * prime <= remaining:
        if remaining % prime == 0:
            output.append(prime)
            while remaining % prime == 0:
                remaining //= prime
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        output.append(remaining)
    result = tuple(output)
    if result != CORE_EXCEPTIONAL_PRIMES:
        raise AssertionError("exceptional prime set changed")
    return result


def historical_modular_residue_from_exact_determinant() -> int:
    """Recover the old 1,000,003 certificate directly from the exact integer."""
    residue = CORE_EXACT_DETERMINANT % CERTIFICATE_MODULUS
    if residue != CERTIFICATE_150_DETERMINANT_RESIDUE:
        raise AssertionError("historical modular certificate no longer matches exact determinant")
    return residue
