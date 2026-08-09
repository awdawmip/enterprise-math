"""Quotient-natural additive dynamics on P019 weighted relation fields.

For capacities m, totals c, and Z=c m^T-m c^T, any zero-total integer update
delta changes the relation field by

    Z' = Z + delta m^T - m delta^T.

Partition coarsening commutes exactly with this update: the coarse update is
just the partition-aggregated vector A*delta.
"""

from __future__ import annotations

from .weighted_relation_field import (
    Partition,
    WeightedField,
    coarsen_weighted_relation_field,
    weighted_relation_field_is_closed,
)


def _require_update(block_count: int, update: tuple[int, ...]) -> None:
    if not isinstance(update, tuple) or len(update) != block_count:
        raise ValueError("update must have one integer per block")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in update):
        raise ValueError("update entries must be integers")
    if sum(update) != 0:
        raise ValueError("relation dynamics update must preserve grand total")


def update_weighted_relation_field(
    block_sizes: tuple[int, ...], field: WeightedField, update: tuple[int, ...]
) -> WeightedField:
    """Apply Z' = Z + delta*m^T-m*delta^T."""
    if not weighted_relation_field_is_closed(block_sizes, field):
        raise ValueError("weighted relation field must be closed")
    _require_update(len(block_sizes), update)
    result = tuple(
        tuple(
            field[i][j]
            + update[i] * block_sizes[j]
            - block_sizes[i] * update[j]
            for j in range(len(block_sizes))
        )
        for i in range(len(block_sizes))
    )
    if not weighted_relation_field_is_closed(block_sizes, result):
        raise AssertionError("zero-total additive update must preserve weighted closure")
    return result


def primitive_transfer_update(
    block_count: int, receiver: int, donor: int
) -> tuple[int, ...]:
    """Return e_receiver-e_donor."""
    if isinstance(block_count, bool) or not isinstance(block_count, int) or block_count <= 0:
        raise ValueError("block_count must be a positive integer")
    if (
        isinstance(receiver, bool)
        or not isinstance(receiver, int)
        or not 0 <= receiver < block_count
    ):
        raise ValueError("receiver must index the blocks")
    if (
        isinstance(donor, bool)
        or not isinstance(donor, int)
        or not 0 <= donor < block_count
    ):
        raise ValueError("donor must index the blocks")
    if receiver == donor:
        return (0,) * block_count
    return tuple(
        1 if index == receiver else -1 if index == donor else 0
        for index in range(block_count)
    )


def aggregate_update(update: tuple[int, ...], partition: Partition) -> tuple[int, ...]:
    """Return the partition-aggregated update vector A*delta."""
    _require_update(len(update), update)
    flattened = [index for group in partition for index in group]
    if sorted(flattened) != list(range(len(update))):
        raise ValueError("partition must cover every update coordinate exactly once")
    return tuple(sum(update[index] for index in group) for group in partition)


def coarsening_update_naturality(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    update: tuple[int, ...],
    partition: Partition,
) -> tuple[tuple[tuple[int, ...], WeightedField], tuple[tuple[int, ...], WeightedField]]:
    """Return both sides of Q_A(T_delta Z)=T_(A delta)(Q_A Z)."""
    updated_fine = update_weighted_relation_field(block_sizes, field, update)
    left = coarsen_weighted_relation_field(block_sizes, updated_fine, partition)

    coarse_sizes, coarse_field = coarsen_weighted_relation_field(
        block_sizes, field, partition
    )
    coarse_update = aggregate_update(update, partition)
    right = (
        coarse_sizes,
        update_weighted_relation_field(coarse_sizes, coarse_field, coarse_update),
    )
    return left, right
