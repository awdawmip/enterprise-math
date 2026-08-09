"""Partition-derived relation precision profiles for P019/P018 integration.

A partition has two intrinsic integer precision coordinates:

- relation rank = number of coarse blocks minus one;
- structural relation quantum = gcd of the aggregated block capacities.

Refining a partition increases relation rank and can only divide the relation
quantum.  The exact refinement profile records the added rank together with the
integer quantum-improvement factor.
"""

from __future__ import annotations

from .relation_lattice import relation_quantum, relation_translation_period
from .weighted_relation_field import Partition


def _require_capacities(capacities: tuple[int, ...]) -> None:
    if not isinstance(capacities, tuple) or not capacities:
        raise ValueError("capacities must be a non-empty tuple")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in capacities
    ):
        raise ValueError("capacities must be positive integers")


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
        raise ValueError("partition must cover every fine block exactly once")


def partition_capacities(
    fine_capacities: tuple[int, ...], partition: Partition
) -> tuple[int, ...]:
    """Aggregate fine capacities into the supplied partition."""
    _require_capacities(fine_capacities)
    _require_partition(len(fine_capacities), partition)
    return tuple(
        sum(fine_capacities[index] for index in group)
        for group in partition
    )


def relation_precision_profile(
    fine_capacities: tuple[int, ...], partition: Partition
) -> tuple[int, int, int]:
    """Return `(relation_rank, relation_quantum, translation_period)`."""
    capacities = partition_capacities(fine_capacities, partition)
    return (
        len(partition) - 1,
        relation_quantum(capacities),
        relation_translation_period(capacities),
    )


def partition_refines(refined: Partition, coarse: Partition) -> bool:
    """Whether every refined block lies inside one coarse block."""
    if not refined or not coarse:
        raise ValueError("partitions must be non-empty")
    size = sum(len(group) for group in coarse)
    _require_partition(size, coarse)
    _require_partition(size, refined)
    coarse_group_of = [0] * size
    for group_index, group in enumerate(coarse):
        for index in group:
            coarse_group_of[index] = group_index
    return all(
        len({coarse_group_of[index] for index in group}) == 1
        for group in refined
    )


def relation_refinement_cost(
    fine_capacities: tuple[int, ...],
    initial_partition: Partition,
    refined_partition: Partition,
) -> tuple[int, int, int, int]:
    """Return `(rank_gain, quantum_factor, initial_quantum, refined_quantum)`.

    `quantum_factor = initial_quantum // refined_quantum`. The same factor is
    the multiplicative increase of the field-preserving translation period.
    """
    _require_capacities(fine_capacities)
    _require_partition(len(fine_capacities), initial_partition)
    _require_partition(len(fine_capacities), refined_partition)
    if not partition_refines(refined_partition, initial_partition):
        raise ValueError("refined_partition must refine initial_partition")

    initial_rank, initial_quantum, initial_period = relation_precision_profile(
        fine_capacities, initial_partition
    )
    refined_rank, refined_quantum, refined_period = relation_precision_profile(
        fine_capacities, refined_partition
    )
    if initial_quantum % refined_quantum != 0:
        raise AssertionError("refinement quantum must divide the coarse quantum")
    quantum_factor = initial_quantum // refined_quantum
    if refined_period != initial_period * quantum_factor:
        raise AssertionError("quantum refinement and translation-period gain must be dual")
    return (
        refined_rank - initial_rank,
        quantum_factor,
        initial_quantum,
        refined_quantum,
    )
