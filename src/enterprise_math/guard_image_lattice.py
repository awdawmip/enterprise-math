"""Integer guard-image lattice tools for A3 future-language analysis.

For a coordinate partition A with kernel K_A and a family of integer linear
guards W, the hidden score variation inside one coarse fiber is the lattice

    L_G = W(K_A) subset Z^r.

The partition kernel has the canonical within-block basis e_i-e_anchor.  The
image generators are therefore just guard-coefficient differences inside each
coarse block.

This module keeps the analysis integer-only.  Rank is computed by fraction-free
integer row elimination; no floating point or rational arithmetic is used.
"""

from __future__ import annotations

from math import gcd

from .linear_relation_quotient import Partition


Guard = tuple[int, ...]
GuardFamily = tuple[Guard, ...]
IntMatrix = tuple[tuple[int, ...], ...]


def _require_partition(size: int, partition: Partition) -> None:
    if not isinstance(partition, tuple) or not partition:
        raise ValueError("partition must be non-empty")
    flattened = [index for group in partition for index in group]
    if any(not isinstance(group, tuple) or not group for group in partition):
        raise ValueError("partition groups must be non-empty tuples")
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


def _require_guards(guards: GuardFamily) -> int:
    if not isinstance(guards, tuple) or not guards:
        raise ValueError("guards must be a non-empty tuple")
    size = len(guards[0])
    if size == 0:
        raise ValueError("guards must have positive coordinate dimension")
    for guard in guards:
        if not isinstance(guard, tuple) or len(guard) != size:
            raise ValueError("all guards must have the same coordinate dimension")
        if any(isinstance(value, bool) or not isinstance(value, int) for value in guard):
            raise ValueError("guard coefficients must be integers")
    return size


def partition_kernel_basis(size: int, partition: Partition) -> IntMatrix:
    """Return a Z-basis of ker(A) using within-block unit differences."""
    _require_partition(size, partition)
    basis = []
    for group in partition:
        anchor = group[0]
        for coordinate in group[1:]:
            vector = [0] * size
            vector[coordinate] = 1
            vector[anchor] = -1
            basis.append(tuple(vector))
    return tuple(basis)


def guard_kernel_image_generators(
    guards: GuardFamily, partition: Partition
) -> IntMatrix:
    """Generators of W(K_A) in guard-score coordinates.

    One generator is produced for each non-anchor fine coordinate in every
    coarse block.  Its guard-space components are coefficient differences.
    """
    size = _require_guards(guards)
    _require_partition(size, partition)
    generators = []
    for group in partition:
        anchor = group[0]
        for coordinate in group[1:]:
            generators.append(
                tuple(
                    guard[coordinate] - guard[anchor]
                    for guard in guards
                )
            )
    return tuple(generators)


def _primitive_row(row: list[int]) -> list[int]:
    divisor = 0
    for value in row:
        divisor = gcd(divisor, abs(value))
    if divisor > 1:
        row = [value // divisor for value in row]
    first = next((value for value in row if value != 0), 0)
    if first < 0:
        row = [-value for value in row]
    return row


def integer_matrix_rank(rows: IntMatrix, column_count: int | None = None) -> int:
    """Rank over Q via exact integer row elimination.

    Eliminating entry b below pivot a uses

        (a/g)*row - (b/g)*pivot_row,

    where g=gcd(|a|,|b|).  This is fraction-free and preserves rational rank.
    """
    if not isinstance(rows, tuple):
        raise ValueError("rows must be a tuple")
    if rows:
        width = len(rows[0])
        if any(not isinstance(row, tuple) or len(row) != width for row in rows):
            raise ValueError("rows must have a common width")
        if any(
            isinstance(value, bool) or not isinstance(value, int)
            for row in rows
            for value in row
        ):
            raise ValueError("matrix entries must be integers")
        if column_count is not None and width != column_count:
            raise ValueError("column_count does not match row width")
    else:
        if column_count is None:
            return 0
        if isinstance(column_count, bool) or not isinstance(column_count, int) or column_count < 0:
            raise ValueError("column_count must be a non-negative integer")
        width = column_count

    data = [_primitive_row(list(row)) for row in rows]
    pivot_row = 0
    for column in range(width):
        pivot = next(
            (row for row in range(pivot_row, len(data)) if data[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        data[pivot_row], data[pivot] = data[pivot], data[pivot_row]
        data[pivot_row] = _primitive_row(data[pivot_row])
        pivot_value = data[pivot_row][column]

        for row in range(pivot_row + 1, len(data)):
            entry = data[row][column]
            if entry == 0:
                continue
            divisor = gcd(abs(pivot_value), abs(entry))
            pivot_factor = pivot_value // divisor
            row_factor = entry // divisor
            data[row] = _primitive_row(
                [
                    pivot_factor * data[row][index]
                    - row_factor * data[pivot_row][index]
                    for index in range(width)
                ]
            )
        pivot_row += 1
        if pivot_row == len(data):
            break
    return pivot_row


def guard_kernel_image_rank(
    guards: GuardFamily, partition: Partition
) -> int:
    """Rank of hidden guard-score variation W(K_A)."""
    generators = guard_kernel_image_generators(guards, partition)
    return integer_matrix_rank(generators, column_count=len(guards))


def all_guards_descend(guards: GuardFamily, partition: Partition) -> bool:
    """Whether every guard score is constant on every coarse fiber."""
    return guard_kernel_image_rank(guards, partition) == 0


def guard_image_is_full_rank(guards: GuardFamily, partition: Partition) -> bool:
    """Whether hidden motion spans a full-rank sublattice of guard-score space."""
    return guard_kernel_image_rank(guards, partition) == len(guards)
