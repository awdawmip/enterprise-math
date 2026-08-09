"""Integer update-lattice quotients for P019 partition dynamics.

For k current blocks, total-preserving updates form the A_(k-1)-type lattice
U_k={delta in Z^k: sum delta=0}. A partition with ell coarse groups maps
updates by group summation. The map is surjective, its kernel is the direct sum
of within-group redistribution lattices, and its rank is k-ell.
"""

from __future__ import annotations

from .relation_dynamics import aggregate_update, primitive_transfer_update
from .weighted_relation_field import Partition


def _validate_partition(block_count: int, partition: Partition) -> None:
    if isinstance(block_count, bool) or not isinstance(block_count, int) or block_count <= 0:
        raise ValueError("block_count must be a positive integer")
    if not isinstance(partition, tuple) or not partition:
        raise ValueError("partition must be non-empty")
    flattened = [index for group in partition for index in group]
    if any(not isinstance(group, tuple) or not group for group in partition):
        raise ValueError("partition groups must be non-empty tuples")
    if any(
        isinstance(index, bool)
        or not isinstance(index, int)
        or index < 0
        or index >= block_count
        for index in flattened
    ):
        raise ValueError("partition index out of range")
    if sorted(flattened) != list(range(block_count)):
        raise ValueError("partition must cover each fine block exactly once")


def update_lattice_dimension(block_count: int) -> int:
    """Rank of total-preserving integer updates on block_count blocks."""
    if isinstance(block_count, bool) or not isinstance(block_count, int) or block_count <= 0:
        raise ValueError("block_count must be a positive integer")
    return block_count - 1


def partition_internal_update_rank(block_count: int, partition: Partition) -> int:
    """Rank lost by the update lattice under partition aggregation."""
    _validate_partition(block_count, partition)
    return block_count - len(partition)


def internal_update_basis(block_count: int, partition: Partition) -> tuple[tuple[int, ...], ...]:
    """Return a basis of within-group primitive transfers killed by the partition.

    In each coarse group choose its first fine index as anchor and include one
    transfer e_vertex-e_anchor for every other fine index in that group.
    """
    _validate_partition(block_count, partition)
    basis = []
    for group in partition:
        anchor = group[0]
        for vertex in group[1:]:
            basis.append(primitive_transfer_update(block_count, vertex, anchor))
    return tuple(basis)


def lift_coarse_update(
    block_count: int, partition: Partition, coarse_update: tuple[int, ...]
) -> tuple[int, ...]:
    """Construct one fine zero-total lift of a coarse zero-total update."""
    _validate_partition(block_count, partition)
    if not isinstance(coarse_update, tuple) or len(coarse_update) != len(partition):
        raise ValueError("coarse_update must match the coarse partition")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in coarse_update):
        raise ValueError("coarse update entries must be integers")
    if sum(coarse_update) != 0:
        raise ValueError("coarse update must preserve grand total")
    fine = [0] * block_count
    for group, delta in zip(partition, coarse_update):
        fine[group[0]] = delta
    result = tuple(fine)
    if aggregate_update(result, partition) != coarse_update:
        raise AssertionError("constructed fine update must lift the coarse update")
    return result


def primitive_transfer_image(
    block_count: int, partition: Partition, receiver: int, donor: int
) -> tuple[int, ...]:
    """Image of one fine primitive transfer under partition aggregation."""
    _validate_partition(block_count, partition)
    return aggregate_update(
        primitive_transfer_update(block_count, receiver, donor),
        partition,
    )
