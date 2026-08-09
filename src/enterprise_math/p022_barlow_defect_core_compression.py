"""Singleton-peel compression of the N=150 pure Franel-defect certificate.

The central-binomial elimination reduces the raw 151x151 joint certificate to
an 89x89 pure Franel-defect valuation matrix.  Its nonzero support graph has a
second exact reduction: repeatedly remove any row or column with exactly one
remaining nonzero entry.

At N=150 this peels 49 valuation/defect pairs.  Every peeled pivot is +/-1, so
all 49 eliminations are unimodular.  The residual matrix is one connected
40x40 support core with no singleton row or column.  Its determinant residue is
973381 mod 1000003, equal to the original raw 151x151 certificate residue; the
89x89 defect determinant differs only by the accumulated sign.
"""

from __future__ import annotations

from collections import deque

from .p022_barlow_low_order_defect_reduction import (
    composite_indices,
    defect_valuation_matrix,
    franel_rows_from_joint_rows,
)
from .p022_barlow_low_order_identifiability import (
    CERTIFICATE_MODULUS,
    determinant_mod_prime,
)
from .p022_barlow_low_order_identifiability_150 import (
    CERTIFICATE_150_DETERMINANT_RESIDUE,
    CERTIFICATE_150_ROWS,
)

Pivot = tuple[int, int, int]  # (row index, column index, pivot value)

EXPECTED_PEELED_PIVOTS = 49
EXPECTED_CORE_SIZE = 40
EXPECTED_CORE_DETERMINANT_RESIDUE = 973_381


def _require_square(matrix: tuple[tuple[int, ...], ...]) -> None:
    if not isinstance(matrix, tuple) or not matrix:
        raise ValueError("matrix must be a nonempty tuple")
    size = len(matrix)
    if any(not isinstance(row, tuple) or len(row) != size for row in matrix):
        raise ValueError("matrix must be square")


def singleton_peel(
    matrix: tuple[tuple[int, ...], ...]
) -> tuple[tuple[Pivot, ...], tuple[int, ...], tuple[int, ...]]:
    """Deterministically peel support leaves without row arithmetic.

    Preference is given to the smallest-index singleton row; if none exists,
    the smallest-index singleton column is used.  The returned surviving row
    and column index sets define the irreducible support core for this rule.
    """
    _require_square(matrix)
    size = len(matrix)
    active_rows = set(range(size))
    active_cols = set(range(size))
    pivots: list[Pivot] = []

    while True:
        chosen: tuple[int, int] | None = None

        for row in sorted(active_rows):
            support = [col for col in active_cols if matrix[row][col] != 0]
            if len(support) == 1:
                chosen = (row, support[0])
                break

        if chosen is None:
            for col in sorted(active_cols):
                support = [row for row in active_rows if matrix[row][col] != 0]
                if len(support) == 1:
                    chosen = (support[0], col)
                    break

        if chosen is None:
            break

        row, col = chosen
        pivot = matrix[row][col]
        if pivot == 0:
            raise AssertionError("singleton pivot must be nonzero")
        pivots.append((row, col, pivot))
        active_rows.remove(row)
        active_cols.remove(col)

    return tuple(pivots), tuple(sorted(active_rows)), tuple(sorted(active_cols))


def submatrix(
    matrix: tuple[tuple[int, ...], ...],
    rows: tuple[int, ...],
    cols: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(matrix[row][col] for col in cols) for row in rows)


def defect_matrix_150() -> tuple[tuple[int, ...], ...]:
    primes = franel_rows_from_joint_rows(CERTIFICATE_150_ROWS)
    matrix = defect_valuation_matrix(150, primes)
    if len(matrix) != 89 or any(len(row) != 89 for row in matrix):
        raise AssertionError("N=150 defect matrix must be 89x89")
    return matrix


def compressed_defect_core_150() -> tuple[
    tuple[Pivot, ...],
    tuple[int, ...],
    tuple[int, ...],
    tuple[tuple[int, ...], ...],
]:
    matrix = defect_matrix_150()
    pivots, rows, cols = singleton_peel(matrix)
    core = submatrix(matrix, rows, cols)
    if len(pivots) != EXPECTED_PEELED_PIVOTS:
        raise AssertionError("N=150 singleton peel count changed")
    if len(core) != EXPECTED_CORE_SIZE or any(
        len(row) != EXPECTED_CORE_SIZE for row in core
    ):
        raise AssertionError("N=150 residual defect core must be 40x40")
    if any(abs(value) != 1 for _, _, value in pivots):
        raise AssertionError("all peeled N=150 pivots must remain unimodular")
    return pivots, rows, cols, core


def compressed_core_row_primes_150() -> tuple[int, ...]:
    primes = franel_rows_from_joint_rows(CERTIFICATE_150_ROWS)
    _, rows, _, _ = compressed_defect_core_150()
    return tuple(primes[index] for index in rows)


def compressed_core_defect_labels_150() -> tuple[int | str, ...]:
    labels: tuple[int | str, ...] = ("tail",) + composite_indices(150)
    _, _, cols, _ = compressed_defect_core_150()
    return tuple(labels[index] for index in cols)


def compressed_core_determinant_residue_150() -> int:
    _, _, _, core = compressed_defect_core_150()
    return determinant_mod_prime(core, CERTIFICATE_MODULUS)


def core_support_degrees_150() -> tuple[tuple[int, ...], tuple[int, ...]]:
    _, _, _, core = compressed_defect_core_150()
    row_degrees = tuple(sum(value != 0 for value in row) for row in core)
    col_degrees = tuple(
        sum(core[row][col] != 0 for row in range(len(core)))
        for col in range(len(core))
    )
    return row_degrees, col_degrees


def core_support_is_connected_150() -> bool:
    """Connectivity of the bipartite nonzero graph of the residual core."""
    _, _, _, core = compressed_defect_core_150()
    size = len(core)
    row_seen: set[int] = set()
    col_seen: set[int] = set()
    queue: deque[tuple[str, int]] = deque([("r", 0)])

    while queue:
        kind, index = queue.popleft()
        if kind == "r":
            if index in row_seen:
                continue
            row_seen.add(index)
            for col in range(size):
                if core[index][col] != 0 and col not in col_seen:
                    queue.append(("c", col))
        else:
            if index in col_seen:
                continue
            col_seen.add(index)
            for row in range(size):
                if core[row][index] != 0 and row not in row_seen:
                    queue.append(("r", row))

    return len(row_seen) == size and len(col_seen) == size


def verify_150_core_compression() -> bool:
    pivots, _, _, core = compressed_defect_core_150()
    if len(pivots) != 49 or len(core) != 40:
        raise AssertionError("unexpected N=150 core compression")
    if compressed_core_determinant_residue_150() != EXPECTED_CORE_DETERMINANT_RESIDUE:
        raise AssertionError("40x40 core determinant residue changed")
    if EXPECTED_CORE_DETERMINANT_RESIDUE != CERTIFICATE_150_DETERMINANT_RESIDUE:
        raise AssertionError("compressed core should retain the raw certificate residue")
    row_degrees, col_degrees = core_support_degrees_150()
    if min(row_degrees) < 2 or min(col_degrees) < 2:
        raise AssertionError("singleton peeling should leave no support leaves")
    if not core_support_is_connected_150():
        raise AssertionError("N=150 residual core should be one connected component")
    return True
