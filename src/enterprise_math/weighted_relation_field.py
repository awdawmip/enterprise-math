"""Capacity-weighted integer relation fields for P019 contraction.

For blocks with positive capacities m_i and integer totals c_i define

    Z_ij = m_j*c_i - m_i*c_j.

Unit blocks recover ordinary differences. Coarsening a partition adds
capacities, totals, and cross-block relation entries. Binary merge is the
smallest instance of this tree-independent quotient rule.
"""

from __future__ import annotations


WeightedField = tuple[tuple[int, ...], ...]
Partition = tuple[tuple[int, ...], ...]


def _require_state(block_sizes: tuple[int, ...], totals: tuple[int, ...]) -> None:
    if not isinstance(block_sizes, tuple) or not block_sizes:
        raise ValueError("block_sizes must be a non-empty tuple")
    if any(isinstance(size, bool) or not isinstance(size, int) or size <= 0 for size in block_sizes):
        raise ValueError("block sizes must be positive integers")
    if not isinstance(totals, tuple) or len(totals) != len(block_sizes):
        raise ValueError("totals must match block_sizes")
    if any(isinstance(total, bool) or not isinstance(total, int) for total in totals):
        raise ValueError("block totals must be integers")


def _require_field(block_sizes: tuple[int, ...], field: WeightedField) -> None:
    if not isinstance(block_sizes, tuple) or not block_sizes:
        raise ValueError("block_sizes must be a non-empty tuple")
    if any(isinstance(size, bool) or not isinstance(size, int) or size <= 0 for size in block_sizes):
        raise ValueError("block sizes must be positive integers")
    size = len(block_sizes)
    if not isinstance(field, tuple) or len(field) != size:
        raise ValueError("field must match block count")
    if any(not isinstance(row, tuple) or len(row) != size for row in field):
        raise ValueError("field must be square")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in field
        for value in row
    ):
        raise ValueError("field entries must be integers")


def _require_partition(block_count: int, partition: Partition) -> None:
    if not isinstance(partition, tuple) or not partition:
        raise ValueError("partition must be a non-empty tuple of blocks")
    flattened = []
    for group in partition:
        if not isinstance(group, tuple) or not group:
            raise ValueError("each partition block must be a non-empty tuple")
        if len(set(group)) != len(group):
            raise ValueError("partition block indices must be unique")
        if any(
            isinstance(index, bool)
            or not isinstance(index, int)
            or index < 0
            or index >= block_count
            for index in group
        ):
            raise ValueError("partition index out of range")
        flattened.extend(group)
    if sorted(flattened) != list(range(block_count)):
        raise ValueError("partition must cover every current block exactly once")


def weighted_relation_field(
    block_sizes: tuple[int, ...], totals: tuple[int, ...]
) -> WeightedField:
    """Return Z_ij=m_j*c_i-m_i*c_j."""
    _require_state(block_sizes, totals)
    return tuple(
        tuple(
            block_sizes[j] * totals[i] - block_sizes[i] * totals[j]
            for j in range(len(block_sizes))
        )
        for i in range(len(block_sizes))
    )


def weighted_relation_field_is_closed(
    block_sizes: tuple[int, ...], field: WeightedField
) -> bool:
    """Check antisymmetry and weighted three-block closure.

    The closure law is

        m_k Z_ij + m_i Z_jk + m_j Z_ki = 0.
    """
    _require_field(block_sizes, field)
    count = len(block_sizes)
    for i in range(count):
        if field[i][i] != 0:
            return False
        for j in range(count):
            if field[i][j] != -field[j][i]:
                return False
            for k in range(count):
                if (
                    block_sizes[k] * field[i][j]
                    + block_sizes[i] * field[j][k]
                    + block_sizes[j] * field[k][i]
                    != 0
                ):
                    return False
    return True


def recover_totals_from_weighted_field(
    block_sizes: tuple[int, ...], field: WeightedField, grand_total: int
) -> tuple[int, ...]:
    """Recover block totals from a legal weighted relation field and total.

    Let M=sum m_i and R_i=sum_j Z_ij. Then

        M*c_i = m_i*C + R_i.
    """
    _require_field(block_sizes, field)
    if isinstance(grand_total, bool) or not isinstance(grand_total, int):
        raise ValueError("grand_total must be an integer")
    if not weighted_relation_field_is_closed(block_sizes, field):
        raise ValueError("weighted relation field is not closed")
    total_capacity = sum(block_sizes)
    totals = []
    for block_size, row in zip(block_sizes, field):
        numerator = block_size * grand_total + sum(row)
        if numerator % total_capacity != 0:
            raise ValueError("field, capacities, and grand total are not integer-compatible")
        totals.append(numerator // total_capacity)
    result = tuple(totals)
    if sum(result) != grand_total:
        raise AssertionError("recovered block totals must preserve the grand total")
    if weighted_relation_field(block_sizes, result) != field:
        raise AssertionError("recovered totals must reproduce the weighted field")
    return result


def coarsen_weighted_relation_field(
    block_sizes: tuple[int, ...], field: WeightedField, partition: Partition
) -> tuple[tuple[int, ...], WeightedField]:
    """Quotient a weighted relation field by any partition of current blocks.

    For coarse groups A,B,

        Z'_AB = sum_{i in A, j in B} Z_ij.

    This equals m'_B*c'_A-m'_A*c'_B for the aggregated capacities/totals.
    """
    _require_field(block_sizes, field)
    _require_partition(len(block_sizes), partition)
    new_sizes = tuple(
        sum(block_sizes[index] for index in group)
        for group in partition
    )
    new_field = tuple(
        tuple(
            sum(
                field[i][j]
                for i in left_group
                for j in right_group
            )
            for right_group in partition
        )
        for left_group in partition
    )
    if not weighted_relation_field_is_closed(new_sizes, new_field):
        raise AssertionError("partition coarsening must preserve weighted closure")
    return new_sizes, new_field


def merge_weighted_relation_field(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    left: int,
    right: int,
) -> tuple[tuple[int, ...], WeightedField, int]:
    """Merge two blocks using only capacities and the weighted relation field.

    The merged block is appended after all untouched blocks. Its external
    relation to an untouched block k is exactly Z_left,k + Z_right,k.

    Returns `(new_block_sizes, new_field, discarded_internal_relation)`.
    """
    _require_field(block_sizes, field)
    count = len(block_sizes)
    if isinstance(left, bool) or not isinstance(left, int) or not 0 <= left < count:
        raise ValueError("left must index a block")
    if isinstance(right, bool) or not isinstance(right, int) or not 0 <= right < count:
        raise ValueError("right must index a block")
    if left == right:
        raise ValueError("merge blocks must be distinct")

    keep = tuple(index for index in range(count) if index not in (left, right))
    partition = tuple((index,) for index in keep) + ((left, right),)
    new_sizes, result = coarsen_weighted_relation_field(
        block_sizes, field, partition
    )
    return new_sizes, result, field[left][right]


def split_two_block_totals_from_internal_relation(
    left_size: int,
    right_size: int,
    parent_total: int,
    internal_relation: int,
) -> tuple[int, int]:
    """Recover child totals from capacities, parent total, and lost relation.

    z=m_right*c_left-m_left*c_right and c_left+c_right=parent_total.
    """
    if isinstance(left_size, bool) or not isinstance(left_size, int) or left_size <= 0:
        raise ValueError("left_size must be a positive integer")
    if isinstance(right_size, bool) or not isinstance(right_size, int) or right_size <= 0:
        raise ValueError("right_size must be a positive integer")
    if isinstance(parent_total, bool) or not isinstance(parent_total, int):
        raise ValueError("parent_total must be an integer")
    if isinstance(internal_relation, bool) or not isinstance(internal_relation, int):
        raise ValueError("internal_relation must be an integer")
    total_size = left_size + right_size
    numerator = left_size * parent_total + internal_relation
    if numerator % total_size != 0:
        raise ValueError("internal relation is incompatible with capacities and parent total")
    left_total = numerator // total_size
    return left_total, parent_total - left_total


def weighted_relation_dimension(block_sizes: tuple[int, ...]) -> int:
    """Number of independent fixed-grand-total block totals/relations."""
    if not isinstance(block_sizes, tuple) or not block_sizes:
        raise ValueError("block_sizes must be a non-empty tuple")
    if any(isinstance(size, bool) or not isinstance(size, int) or size <= 0 for size in block_sizes):
        raise ValueError("block sizes must be positive integers")
    return len(block_sizes) - 1
