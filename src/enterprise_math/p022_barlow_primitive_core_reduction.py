"""Primitive-capture reduction of the historical N=150 Franel defect core.

The historical singleton peel leaves a 40x40 core.  Two rows that were later
found by global saturation, v_73589 and v_176459, are now understood as
primitive Franel markers from prime-boundary ranks 66 and 12.

Replace the historical core row v_269 by the genuine row v_73589.  Inside this
square 40x40 matrix, 18 defect columns admit explicit primitive-capture unit
pivots.  Reordering those rows/columns first and eliminating them with integer
row operations leaves a 22x22 residual R with

    det(R) = -13311,

and two coprime 21x21 minors -69 and -70.  Therefore

    SNF(R) = diag(1^21, 13311).

Project the genuine row v_176459 through the same 18 unit pivots.  Appending it
to R gives a 23x22 integer matrix.  The original residual minor has determinant
-13311, while replacing residual row 1 by the projected row has determinant
-1585.  These are coprime, so the gcd of full-size minors is one and the
augmented residual row lattice is saturated: all 22 Smith invariants are one.

This is a finite N=150 structural certificate.  It does not prove the infinite
Franel-defect independence problem, but it explains much more of the old
40-dimensional core through local primitive-event capture geometry.
"""

from __future__ import annotations

from math import gcd, prod

from .p022_barlow_defect_core_compression import (
    compressed_core_defect_labels_150,
    compressed_core_row_primes_150,
    compressed_defect_core_150,
)
from .p022_barlow_defect_core_saturation import core_valuation_row_150
from .p022_barlow_defect_core_smith import exact_determinant_bareiss
from .p022_barlow_two_rank_primitive_coverage import two_rank_primitive_pivot

HISTORICAL_REPLACED_ROW = 269
LOCAL_CAPTURE_ROW = 73_589
RESIDUAL_SATURATION_ROW = 176_459

# (defect column, primitive source rank, valuation row prime)
CORE_CAPTURE_MARKERS_150: tuple[tuple[int, int, int], ...] = (
    (5, 4, 173),
    (8, 7, 41),
    (11, 11, 23),
    (13, 12, 29),
    (17, 17, 59),
    (18, 18, 37),
    (20, 20, 151),
    (32, 31, 421),
    (38, 37, 2417),
    (43, 43, 359),
    (44, 44, 2837),
    (58, 57, 593),
    (60, 60, 66373),
    (67, 66, 73589),
    (77, 77, 1579),
    (89, 89, 941),
    (109, 109, 92083),
    (123, 123, 7411),
)

EXPECTED_CAPTURE_COUNT = 18
EXPECTED_CAPTURE_DIAGONAL = (
    -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1
)
EXPECTED_RESIDUAL_COLUMNS = (
    14, 33, 41, 56, 59, 61, 62, 63, 73, 74, 78,
    86, 88, 92, 108, 110, 122, 124, 130, 134, 149, 150,
)
EXPECTED_RESIDUAL_DETERMINANT = -13_311
EXPECTED_RESIDUAL_MINOR_ONE = -69
EXPECTED_RESIDUAL_MINOR_TWO = -70
EXPECTED_PROJECTED_176459_ROW = (
    -1, 0, -2, 0, 0, -1, -1, 0, 1, 0, 2,
    0, 0, 0, 0, -1, 2, -4, -1, 2, 1, 0,
)
EXPECTED_AUGMENTED_REPLACEMENT_MINOR = -1_585


def _replace_core_row(
    core: tuple[tuple[int, ...], ...],
    row_primes: tuple[int, ...],
    old_prime: int,
    new_prime: int,
) -> tuple[tuple[tuple[int, ...], ...], tuple[int, ...]]:
    index = row_primes.index(old_prime)
    new_row = core_valuation_row_150(new_prime)
    rows = tuple(new_row if row == index else values for row, values in enumerate(core))
    labels = tuple(new_prime if row == index else prime for row, prime in enumerate(row_primes))
    return rows, labels


def capture_square_core_150() -> tuple[
    tuple[tuple[int, ...], ...], tuple[int, ...], tuple[int | str, ...]
]:
    """Historical 40-core with v_269 replaced by genuine v_73589."""
    _, _, _, core = compressed_defect_core_150()
    row_primes = compressed_core_row_primes_150()
    columns = compressed_core_defect_labels_150()
    square, labels = _replace_core_row(
        core, row_primes, HISTORICAL_REPLACED_ROW, LOCAL_CAPTURE_ROW
    )
    if len(square) != 40 or any(len(row) != 40 for row in square):
        raise AssertionError("capture square must remain 40x40")
    return square, labels, columns


def capture_order_150() -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Row and column permutations putting the 18 unit capture pivots first."""
    _, row_primes, columns = capture_square_core_150()
    marker_rows = tuple(prime for _, _, prime in CORE_CAPTURE_MARKERS_150)
    marker_columns = tuple(segment for segment, _, _ in CORE_CAPTURE_MARKERS_150)
    if len(set(marker_rows)) != EXPECTED_CAPTURE_COUNT:
        raise AssertionError("capture rows must be distinct")
    if len(set(marker_columns)) != EXPECTED_CAPTURE_COUNT:
        raise AssertionError("capture columns must be distinct")
    row_order = tuple(row_primes.index(prime) for prime in marker_rows) + tuple(
        index for index, prime in enumerate(row_primes) if prime not in marker_rows
    )
    col_order = tuple(columns.index(segment) for segment in marker_columns) + tuple(
        index for index, segment in enumerate(columns) if segment not in marker_columns
    )
    return row_order, col_order


def reordered_capture_core_150() -> tuple[tuple[int, ...], ...]:
    square, _, _ = capture_square_core_150()
    rows, cols = capture_order_150()
    return tuple(tuple(square[row][col] for col in cols) for row in rows)


def capture_diagonal_150() -> tuple[int, ...]:
    values = tuple(
        two_rank_primitive_pivot(segment, source_rank, prime)
        for segment, source_rank, prime in CORE_CAPTURE_MARKERS_150
    )
    if values != EXPECTED_CAPTURE_DIAGONAL:
        raise AssertionError("N=150 primitive-capture diagonal changed")
    matrix = reordered_capture_core_150()
    for row in range(EXPECTED_CAPTURE_COUNT):
        if any(matrix[row][col] != 0 for col in range(row)):
            raise AssertionError("capture block must be upper triangular")
        if matrix[row][row] != values[row]:
            raise AssertionError("capture block diagonal disagrees with primitive theorem")
    if abs(prod(values)) != 1:
        raise AssertionError("capture block must be unimodular")
    return values


def _integer_eliminate_capture_block(
    matrix: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, ...], ...]:
    values = [list(map(int, row)) for row in matrix]
    size = len(values)
    for pivot_index in range(EXPECTED_CAPTURE_COUNT):
        pivot = values[pivot_index][pivot_index]
        if abs(pivot) != 1:
            raise AssertionError("primitive capture pivot must be an integer unit")
        for row in range(pivot_index + 1, size):
            coefficient = values[row][pivot_index]
            if coefficient == 0:
                continue
            multiplier = coefficient // pivot
            for col in range(pivot_index, size):
                values[row][col] -= multiplier * values[pivot_index][col]
            if values[row][pivot_index] != 0:
                raise AssertionError("unit-pivot elimination must zero the capture column")
    return tuple(tuple(row) for row in values)


def primitive_residual_22_150() -> tuple[tuple[int, ...], ...]:
    """22x22 residual after eliminating the 18 local primitive captures."""
    capture_diagonal_150()
    eliminated = _integer_eliminate_capture_block(reordered_capture_core_150())
    residual = tuple(
        tuple(row[EXPECTED_CAPTURE_COUNT:])
        for row in eliminated[EXPECTED_CAPTURE_COUNT:]
    )
    if len(residual) != 22 or any(len(row) != 22 for row in residual):
        raise AssertionError("primitive residual must be 22x22")
    _, col_order = capture_order_150()
    columns = compressed_core_defect_labels_150()
    residual_columns = tuple(columns[index] for index in col_order[EXPECTED_CAPTURE_COUNT:])
    if residual_columns != EXPECTED_RESIDUAL_COLUMNS:
        raise AssertionError("primitive residual column labels changed")
    return residual


def primitive_residual_determinant_150() -> int:
    value = exact_determinant_bareiss(primitive_residual_22_150())
    if value != EXPECTED_RESIDUAL_DETERMINANT:
        raise AssertionError("22x22 primitive residual determinant changed")
    return value


def _delete_row_column(
    matrix: tuple[tuple[int, ...], ...], row_index: int, col_index: int
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(value for col, value in enumerate(row) if col != col_index)
        for current_row, row in enumerate(matrix)
        if current_row != row_index
    )


def primitive_residual_smith_witnesses_150() -> tuple[int, int]:
    """Coprime 21x21 minors certifying SNF diag(1^21,13311)."""
    residual = primitive_residual_22_150()
    first = exact_determinant_bareiss(_delete_row_column(residual, 17, 4))
    second = exact_determinant_bareiss(_delete_row_column(residual, 14, 8))
    if (first, second) != (EXPECTED_RESIDUAL_MINOR_ONE, EXPECTED_RESIDUAL_MINOR_TWO):
        raise AssertionError("22-residual Smith witness minors changed")
    if gcd(abs(first), abs(second)) != 1:
        raise AssertionError("residual Smith witness minors must be coprime")
    return first, second


def primitive_residual_smith_invariants_150() -> tuple[int, ...]:
    determinant = abs(primitive_residual_determinant_150())
    primitive_residual_smith_witnesses_150()
    return (1,) * 21 + (determinant,)


def projected_saturation_row_176459_150() -> tuple[int, ...]:
    """Project v_176459 through the same 18 unit pivot operations."""
    _, _, columns = capture_square_core_150()
    _, col_order = capture_order_150()
    raw = core_valuation_row_150(RESIDUAL_SATURATION_ROW)
    row = [raw[index] for index in col_order]
    pivot_matrix = reordered_capture_core_150()
    for pivot_index in range(EXPECTED_CAPTURE_COUNT):
        pivot = pivot_matrix[pivot_index][pivot_index]
        coefficient = row[pivot_index]
        if coefficient:
            multiplier = coefficient // pivot
            for col in range(pivot_index, len(row)):
                row[col] -= multiplier * pivot_matrix[pivot_index][col]
        if row[pivot_index] != 0:
            raise AssertionError("projected saturation row must clear primitive columns")
    projected = tuple(row[EXPECTED_CAPTURE_COUNT:])
    if projected != EXPECTED_PROJECTED_176459_ROW:
        raise AssertionError("projected v_176459 residual row changed")
    return projected


def augmented_residual_full_minor_witnesses_150() -> tuple[int, int]:
    """Two coprime 22x22 minors of the 23x22 residual row family."""
    residual = primitive_residual_22_150()
    base = primitive_residual_determinant_150()
    projected = projected_saturation_row_176459_150()
    replaced = tuple(
        projected if row_index == 1 else row
        for row_index, row in enumerate(residual)
    )
    second = exact_determinant_bareiss(replaced)
    if second != EXPECTED_AUGMENTED_REPLACEMENT_MINOR:
        raise AssertionError("augmented residual replacement minor changed")
    if gcd(abs(base), abs(second)) != 1:
        raise AssertionError("augmented residual full-size minors must be coprime")
    return base, second


def augmented_residual_is_saturated_150() -> bool:
    """Coprime full-size minors force all 22 Smith invariants to be one."""
    augmented_residual_full_minor_witnesses_150()
    return True
