"""Exact defect quotient on one Franel zero alphabet.

For an odd prime q let

    Z_q={1<=s<q : q divides F_s}.

A q-adic defect row only depends on depths carried by these coordinates.  This
module restricts every composite D_n with n<q to Z_q and performs exact
Fraction RREF.  It is intentionally a research verifier, not a global rank
theorem.

The proved right-half visibility theorem supplies one exact part of the answer:
every right-half twin-center s in Z_q is an identically zero column.  Finite
experiments can then ask whether these are the only free columns and whether
the rank-of-apparition coordinate is annihilated by the defect rowspace.
"""

from __future__ import annotations

from fractions import Fraction

from .p022_barlow_franel_lucas_rank import franel_rank_of_apparition, franel_zero_digits
from .p022_barlow_low_order_defect_reduction import (
    _is_prime,
    composite_A_relation_exponents,
)
from .p022_barlow_right_half_defect_visibility import right_half_zero_column_iff_twin

Matrix = tuple[tuple[int, ...], ...]


def _require_odd_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")


def zero_alphabet_defect_matrix(prime: int) -> tuple[tuple[int, ...], Matrix]:
    """Return (Z_q,M); rows are all nonzero D_n|Z_q for 2<=n<q."""
    _require_odd_prime(prime)
    columns = franel_zero_digits(prime)
    column_index = {value: index for index, value in enumerate(columns)}
    rows: list[tuple[int, ...]] = []
    for segment in range(2, prime):
        if _is_prime(2 * segment - 1):
            continue
        row = [0] * len(columns)
        if segment in column_index:
            row[column_index[segment]] += 1
        for index, exponent in composite_A_relation_exponents(segment):
            position = column_index.get(index)
            if position is not None:
                row[position] -= exponent
        if any(row):
            rows.append(tuple(row))
    return columns, tuple(rows)


def exact_rref(matrix: Matrix) -> tuple[tuple[tuple[Fraction, ...], ...], tuple[int, ...]]:
    """Return exact Fraction RREF and pivot-column indices."""
    if not matrix:
        return (), ()
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("matrix rows must have equal width")
    work = [[Fraction(value) for value in row] for row in matrix]
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(width):
        candidate = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if candidate is None:
            continue
        work[pivot_row], work[candidate] = work[candidate], work[pivot_row]
        pivot = work[pivot_row][column]
        work[pivot_row] = [value / pivot for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or not work[row][column]:
                continue
            scale = work[row][column]
            work[row] = [
                left - scale * right
                for left, right in zip(work[row], work[pivot_row])
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(work):
            break
    nonzero = tuple(tuple(row) for row in work if any(row))
    return nonzero, tuple(pivot_columns)


def zero_alphabet_free_digits(prime: int) -> tuple[int, ...]:
    """Exact RREF free columns, reported as Franel digit indices."""
    columns, matrix = zero_alphabet_defect_matrix(prime)
    if not columns:
        return ()
    _, pivots = exact_rref(matrix)
    pivot_set = set(pivots)
    return tuple(value for index, value in enumerate(columns) if index not in pivot_set)


def right_half_twin_zero_digits(prime: int) -> tuple[int, ...]:
    """Zero digits whose columns are proved identically zero below q."""
    _require_odd_prime(prime)
    midpoint = (prime - 1) // 2
    return tuple(
        digit
        for digit in franel_zero_digits(prime)
        if digit > midpoint and right_half_zero_column_iff_twin(prime, digit)
    )


def finite_free_column_classification_holds(prime: int) -> bool:
    """Research verifier: free digits equal the proved right-half zero columns.

    This helper checks one finite prime.  Its success is evidence for, not a
    proof of, the universal left-half annihilation theorem.
    """
    actual = zero_alphabet_free_digits(prime)
    predicted = right_half_twin_zero_digits(prime)
    if actual != predicted:
        raise AssertionError("zero-alphabet quotient has an unexplained free column")
    return True


def primitive_source_is_in_defect_rowspace(prime: int) -> bool:
    """Whether the rank-of-apparition coordinate is a pivot of the quotient."""
    _require_odd_prime(prime)
    rank = franel_rank_of_apparition(prime)
    if rank is None:
        raise ValueError("prime has no nonzero Franel zero digit")
    columns, matrix = zero_alphabet_defect_matrix(prime)
    _, pivots = exact_rref(matrix)
    source_column = columns.index(rank)
    return source_column in set(pivots)
