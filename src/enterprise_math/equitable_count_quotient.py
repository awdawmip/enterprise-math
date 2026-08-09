"""Exact witness-label erasure for non-negative integer count matrices.

A partition of exact witness states is equitable for a count/transition matrix
when every fine row inside one source cell has the same sums into every target
cell.  This is exactly the one-step block-count descent condition.  Equitable
matrices are closed under multiplication and their quotient matrices multiply
exactly, giving a future-safe state for arbitrary finite words in an equitable
operation family.

The abstract mathematics is standard equitable-partition/lumpability theory;
this module is a finite integer reference specialization for the Enterprise
Math A3/A4/P021/P023 bridge.
"""

from __future__ import annotations

IntMatrix = tuple[tuple[int, ...], ...]
Partition = tuple[tuple[int, ...], ...]


def _require_square_matrix(matrix: IntMatrix) -> None:
    if not isinstance(matrix, tuple) or not matrix:
        raise ValueError("matrix must be a non-empty tuple")
    size = len(matrix)
    if any(not isinstance(row, tuple) or len(row) != size for row in matrix):
        raise ValueError("matrix must be square")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for row in matrix
        for value in row
    ):
        raise ValueError("matrix entries must be non-negative integers")


def _require_partition(size: int, partition: Partition) -> None:
    if not isinstance(partition, tuple) or not partition:
        raise ValueError("partition must be a non-empty tuple")
    flat: list[int] = []
    for cell in partition:
        if not isinstance(cell, tuple) or not cell:
            raise ValueError("partition cells must be non-empty tuples")
        if len(set(cell)) != len(cell):
            raise ValueError("partition indices must be unique within a cell")
        if any(
            isinstance(index, bool)
            or not isinstance(index, int)
            or index < 0
            or index >= size
            for index in cell
        ):
            raise ValueError("partition index out of range")
        flat.extend(cell)
    if sorted(flat) != list(range(size)):
        raise ValueError("partition must cover every state exactly once")


def block_count_signature(
    matrix: IntMatrix, partition: Partition, state: int
) -> tuple[int, ...]:
    """Return sums from one fine state into each target partition cell."""
    _require_square_matrix(matrix)
    _require_partition(len(matrix), partition)
    if isinstance(state, bool) or not isinstance(state, int) or not 0 <= state < len(matrix):
        raise ValueError("state must index the matrix")
    return tuple(sum(matrix[state][target] for target in cell) for cell in partition)


def is_equitable(matrix: IntMatrix, partition: Partition) -> bool:
    """Whether block-count signatures are constant inside each source cell."""
    _require_square_matrix(matrix)
    _require_partition(len(matrix), partition)
    return all(
        len({block_count_signature(matrix, partition, state) for state in cell}) == 1
        for cell in partition
    )


def quotient_count_matrix(matrix: IntMatrix, partition: Partition) -> IntMatrix:
    """Return exact quotient row-count matrix for an equitable partition."""
    if not is_equitable(matrix, partition):
        raise ValueError("partition is not equitable for this matrix")
    return tuple(
        block_count_signature(matrix, partition, cell[0])
        for cell in partition
    )


def matrix_product(left: IntMatrix, right: IntMatrix) -> IntMatrix:
    """Ordinary non-negative-integer square matrix product."""
    _require_square_matrix(left)
    _require_square_matrix(right)
    if len(left) != len(right):
        raise ValueError("matrices must have the same dimension")
    size = len(left)
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(size))
            for j in range(size)
        )
        for i in range(size)
    )


def matrix_word(matrices: tuple[IntMatrix, ...]) -> IntMatrix:
    """Multiply one nonempty word of square count matrices left-to-right."""
    if not matrices:
        raise ValueError("matrix word must be nonempty")
    result = matrices[0]
    _require_square_matrix(result)
    for matrix in matrices[1:]:
        result = matrix_product(result, matrix)
    return result


def quotient_word(matrices: tuple[IntMatrix, ...], partition: Partition) -> IntMatrix:
    """Multiply quotient matrices for an equitable operation word."""
    if not matrices:
        raise ValueError("matrix word must be nonempty")
    quotients = tuple(quotient_count_matrix(matrix, partition) for matrix in matrices)
    return matrix_word(quotients)


def quotient_word_is_exact(matrices: tuple[IntMatrix, ...], partition: Partition) -> bool:
    """Audit Q_(M1...Mk)=Q_M1...Q_Mk for an equitable family word."""
    if not matrices:
        raise ValueError("matrix word must be nonempty")
    if not all(is_equitable(matrix, partition) for matrix in matrices):
        return False
    fine_product = matrix_word(matrices)
    return is_equitable(fine_product, partition) and quotient_count_matrix(
        fine_product, partition
    ) == quotient_word(matrices, partition)


def block_total_matrix(matrix: IntMatrix, partition: Partition) -> IntMatrix:
    """Aggregate exact matrix mass between source/target partition cells."""
    _require_square_matrix(matrix)
    _require_partition(len(matrix), partition)
    return tuple(
        tuple(
            sum(matrix[source][target] for source in source_cell for target in target_cell)
            for target_cell in partition
        )
        for source_cell in partition
    )


def recover_quotient_from_block_totals(
    totals: IntMatrix, cell_sizes: tuple[int, ...]
) -> IntMatrix:
    """Recover equitable quotient rows by exact division by source cell size."""
    _require_square_matrix(totals)
    if len(cell_sizes) != len(totals):
        raise ValueError("cell_sizes must match block-total dimension")
    if any(
        isinstance(size, bool) or not isinstance(size, int) or size <= 0
        for size in cell_sizes
    ):
        raise ValueError("cell sizes must be positive integers")
    rows: list[tuple[int, ...]] = []
    for source, row in enumerate(totals):
        size = cell_sizes[source]
        if any(value % size != 0 for value in row):
            raise ValueError("block totals are not divisible by source cell sizes")
        rows.append(tuple(value // size for value in row))
    return tuple(rows)


def family_is_equitable(
    matrices: tuple[IntMatrix, ...], partition: Partition
) -> bool:
    """Whether every generator in a nonempty operation family is equitable."""
    if not matrices:
        raise ValueError("matrix family must be nonempty")
    return all(is_equitable(matrix, partition) for matrix in matrices)
