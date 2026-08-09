"""Exact partition quotients for integer linear/affine dynamics in P019.

For a partition aggregation matrix A and integer linear dynamics c' = B c + u,
the quotient is exact iff there exists an integer coarse matrix Bbar with

    A B = Bbar A.

Because each column of A is a coarse basis vector, this is equivalent to all
fine coordinates in one coarse block having identical aggregated column-effect
signatures. Repeated signature splitting gives the coarsest refinement of an
initial partition that is stable for a declared family of linear dynamics.
"""

from __future__ import annotations


Matrix = tuple[tuple[int, ...], ...]
Partition = tuple[tuple[int, ...], ...]


def _require_square_matrix(matrix: Matrix) -> None:
    if not isinstance(matrix, tuple) or not matrix:
        raise ValueError("matrix must be a non-empty tuple")
    size = len(matrix)
    if any(not isinstance(row, tuple) or len(row) != size for row in matrix):
        raise ValueError("matrix must be square")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in matrix
        for value in row
    ):
        raise ValueError("matrix entries must be integers")


def _require_partition(size: int, partition: Partition) -> None:
    if not isinstance(partition, tuple) or not partition:
        raise ValueError("partition must be non-empty")
    flattened = []
    for group in partition:
        if not isinstance(group, tuple) or not group:
            raise ValueError("partition groups must be non-empty tuples")
        flattened.extend(group)
    if any(
        isinstance(index, bool)
        or not isinstance(index, int)
        or index < 0
        or index >= size
        for index in flattened
    ):
        raise ValueError("partition index out of range")
    if sorted(flattened) != list(range(size)):
        raise ValueError("partition must cover every coordinate exactly once")


def partition_matrix(size: int, partition: Partition) -> Matrix:
    """0-1 aggregation matrix A of a coordinate partition."""
    _require_partition(size, partition)
    return tuple(
        tuple(1 if column in group else 0 for column in range(size))
        for group in partition
    )


def _matmul(left: Matrix, right: Matrix) -> Matrix:
    if not isinstance(left, tuple) or not left or not isinstance(right, tuple) or not right:
        raise ValueError("matrices must be non-empty")
    inner = len(left[0])
    if any(len(row) != inner for row in left):
        raise ValueError("left matrix rows must have common length")
    if len(right) != inner:
        raise ValueError("matrix dimensions do not compose")
    columns = len(right[0])
    if any(len(row) != columns for row in right):
        raise ValueError("right matrix rows must have common length")
    return tuple(
        tuple(
            sum(left[row][k] * right[k][column] for k in range(inner))
            for column in range(columns)
        )
        for row in range(len(left))
    )


def descended_linear_matrix(matrix: Matrix, partition: Partition) -> Matrix:
    """Return Bbar satisfying A B = Bbar A, or raise if it does not exist."""
    _require_square_matrix(matrix)
    size = len(matrix)
    _require_partition(size, partition)
    aggregation = partition_matrix(size, partition)
    aggregated_effect = _matmul(aggregation, matrix)  # A B

    coarse_columns = []
    for source_group in partition:
        representative = source_group[0]
        signature = tuple(
            aggregated_effect[row][representative]
            for row in range(len(partition))
        )
        for source in source_group[1:]:
            if tuple(
                aggregated_effect[row][source]
                for row in range(len(partition))
            ) != signature:
                raise ValueError("linear dynamics reads distinctions erased by the partition")
        coarse_columns.append(signature)

    return tuple(
        tuple(coarse_columns[column][row] for column in range(len(partition)))
        for row in range(len(partition))
    )


def linear_matrix_descends(matrix: Matrix, partition: Partition) -> bool:
    """Whether an integer linear dynamics factors through the partition."""
    try:
        descended_linear_matrix(matrix, partition)
    except ValueError as error:
        if str(error) == "linear dynamics reads distinctions erased by the partition":
            return False
        raise
    return True


def linear_family_descends(matrices: tuple[Matrix, ...], partition: Partition) -> bool:
    """Whether every matrix in a declared linear operation family descends."""
    if not isinstance(matrices, tuple):
        raise ValueError("matrices must be a tuple")
    return all(linear_matrix_descends(matrix, partition) for matrix in matrices)


def _refinement_signatures(
    matrices: tuple[Matrix, ...], partition: Partition
) -> tuple[tuple[object, ...], ...]:
    size = len(matrices[0]) if matrices else max(max(group) for group in partition) + 1
    group_of = [0] * size
    for group_index, group in enumerate(partition):
        for coordinate in group:
            group_of[coordinate] = group_index

    signatures = []
    for source in range(size):
        effects = []
        for matrix in matrices:
            for target_group in partition:
                effects.append(sum(matrix[target][source] for target in target_group))
        signatures.append((group_of[source], *effects))
    return tuple(signatures)


def refine_partition_for_linear_family(
    matrices: tuple[Matrix, ...], initial_partition: Partition | None = None
) -> Partition:
    """Coarsest refinement of `initial_partition` stable for all matrices.

    The algorithm repeatedly splits each current block by aggregated column
    effects into every current target block under every declared matrix.
    """
    if not isinstance(matrices, tuple) or not matrices:
        raise ValueError("matrices must be a non-empty tuple")
    for matrix in matrices:
        _require_square_matrix(matrix)
    size = len(matrices[0])
    if any(len(matrix) != size for matrix in matrices):
        raise ValueError("all matrices must have the same size")
    if initial_partition is None:
        partition = (tuple(range(size)),)
    else:
        _require_partition(size, initial_partition)
        partition = initial_partition

    while True:
        signatures = _refinement_signatures(matrices, partition)
        refined = []
        for group in partition:
            buckets: dict[tuple[object, ...], list[int]] = {}
            order = []
            for source in group:
                signature = signatures[source]
                if signature not in buckets:
                    buckets[signature] = []
                    order.append(signature)
                buckets[signature].append(source)
            refined.extend(tuple(buckets[signature]) for signature in order)
        next_partition = tuple(refined)
        if next_partition == partition:
            if not linear_family_descends(matrices, partition):
                raise AssertionError("stable signature refinement must make every matrix descend")
            return partition
        partition = next_partition


def kernel_invariant_under_linear_matrix(matrix: Matrix, partition: Partition) -> bool:
    """Check B(ker A) subset ker A using a primitive within-block basis."""
    _require_square_matrix(matrix)
    size = len(matrix)
    _require_partition(size, partition)
    aggregation = partition_matrix(size, partition)
    for group in partition:
        anchor = group[0]
        for vertex in group[1:]:
            vector = [0] * size
            vector[vertex] = 1
            vector[anchor] = -1
            image = tuple(
                sum(matrix[row][column] * vector[column] for column in range(size))
                for row in range(size)
            )
            coarse = tuple(
                sum(aggregation[row][column] * image[column] for column in range(size))
                for row in range(len(partition))
            )
            if any(coarse):
                return False
    return True
