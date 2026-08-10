"""Finite spectrum of deterministic partial operations safe for one partition.

FQ-006 identifies a deterministic partial endomap ``F : X -> Option X`` as safe
for an observation partition exactly when each observation fiber behaves in one
of two ways:

* the operation is undefined on the entire source fiber; or
* it is defined everywhere on that fiber and all targets lie in one target
  observation fiber.

For a finite partition with block sizes ``n_1,...,n_b`` this gives an exact
closed count.  A source block of size ``n_i`` has

    1 + sum_j n_j ** n_i

safe partial behaviors: one all-undefined behavior, or a choice of target block
``j`` followed by an arbitrary pointwise map into its ``n_j`` members.  Source
blocks are independent, so

    N_partial = product_i (1 + sum_j n_j ** n_i).

For total endomaps the undefined choice is removed:

    N_total = product_i (sum_j n_j ** n_i).

The count depends only on partition shape, not on state labels.

This immediately exposes a strong non-monotonicity of safe-operation abundance.
On four states the refinement chain

    [4] -> [2,2] -> [1,1,1,1]

has partial-safe counts

    257 -> 81 -> 625

and total-safe counts

    256 -> 64 -> 256.

More strongly, safe-operation *sets* can be incomparable across one refinement.
Refining the indiscrete partition ``[4]`` to ``[2,2]`` simultaneously:

* gains a partial identity whose domain is exactly one new fine block, because
  that guard was not saturated at the coarse level;
* loses a total map that sends two members of one new fine source block to two
  different fine target blocks, because the target distinction becomes visible.

Thus refinement can add legal guards while invalidating previously safe target
behavior in the same step.  Safe partial-operation families are therefore not
ordered monotonically by representation precision.

Finite partition congruence and counting are standard prior mathematics.  The
Enterprise Math value is the exact safe-operation spectrum and the decomposition
of the observed non-monotonicity into domain-saturation and target-congruence
mechanisms.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from operator import mul
from typing import Hashable, Mapping

from .partial_operation_quotient import partial_operation_descends

Vertex = Hashable
Partition = Mapping[Vertex, Hashable]
PartialOperation = Mapping[Vertex, Vertex]


def _partition(partition: Partition) -> dict[Vertex, Hashable]:
    values = dict(partition)
    if not values:
        raise ValueError("partition must be nonempty")
    try:
        state_set = set(values)
        set(values.values())
    except TypeError as exc:
        raise ValueError("partition states and labels must be hashable") from exc
    if len(state_set) != len(values):
        raise AssertionError("mapping keys unexpectedly lost uniqueness")
    return values


def partition_block_sizes(partition: Partition) -> tuple[int, ...]:
    """Canonical sorted partition shape."""
    values = _partition(partition)
    counts: dict[Hashable, int] = {}
    for label in values.values():
        counts[label] = counts.get(label, 0) + 1
    return tuple(sorted(counts.values(), reverse=True))


def partition_block_count(partition: Partition) -> int:
    return len(partition_block_sizes(partition))


def saturated_domain_count(partition: Partition) -> int:
    """Number of domains that are unions of observation fibers."""
    return 2 ** partition_block_count(partition)


def safe_partial_endomap_count(partition: Partition) -> int:
    """Exact number of partition-compatible deterministic partial endomaps."""
    sizes = partition_block_sizes(partition)
    factors = [
        1 + sum(target_size**source_size for target_size in sizes)
        for source_size in sizes
    ]
    return reduce(mul, factors, 1)


def safe_total_endomap_count(partition: Partition) -> int:
    """Exact number of partition-compatible deterministic total endomaps."""
    sizes = partition_block_sizes(partition)
    factors = [
        sum(target_size**source_size for target_size in sizes)
        for source_size in sizes
    ]
    return reduce(mul, factors, 1)


def partial_endomap_is_safe(
    partition: Partition,
    operation: PartialOperation,
) -> bool:
    """Check one partial endomap through the FQ-006 compatibility oracle."""
    values = _partition(partition)
    states = tuple(values)
    if not set(operation) <= set(states):
        raise ValueError("partial operation domain must lie inside partition domain")
    if any(target not in values for target in operation.values()):
        raise ValueError("partial operation target must lie inside partition domain")
    return partial_operation_descends(states, operation, values)


def total_endomap_is_safe(
    partition: Partition,
    operation: Mapping[Vertex, Vertex],
) -> bool:
    values = _partition(partition)
    if set(operation) != set(values):
        raise ValueError("total operation must cover the full partition domain")
    return partial_endomap_is_safe(values, operation)


def partial_identity_on_domain(
    partition: Partition,
    enabled_states: set[Vertex] | frozenset[Vertex],
) -> dict[Vertex, Vertex]:
    """Identity update restricted to an explicit enabled subset."""
    values = _partition(partition)
    enabled = set(enabled_states)
    if not enabled <= set(values):
        raise ValueError("enabled domain must lie inside partition domain")
    return {state: state for state in enabled}


@dataclass(frozen=True)
class SafeOperationRefinementWitness:
    coarse_partition: dict[int, int]
    fine_partition: dict[int, int]
    gained_partial_operation: dict[int, int]
    lost_total_operation: dict[int, int]


def four_state_incomparable_refinement_witness() -> SafeOperationRefinementWitness:
    """One refinement that simultaneously gains and loses safe operations."""
    coarse = {0: 0, 1: 0, 2: 0, 3: 0}
    fine = {0: 0, 1: 0, 2: 1, 3: 1}

    gained = {0: 0, 1: 0}
    lost = {0: 0, 1: 2, 2: 2, 3: 2}

    if partial_endomap_is_safe(coarse, gained):
        raise AssertionError("gained guard was unexpectedly coarse-safe")
    if not partial_endomap_is_safe(fine, gained):
        raise AssertionError("gained guard failed to become fine-safe")
    if not total_endomap_is_safe(coarse, lost):
        raise AssertionError("lost total operation was not coarse-safe")
    if total_endomap_is_safe(fine, lost):
        raise AssertionError("lost total operation remained fine-safe")

    return SafeOperationRefinementWitness(
        coarse_partition=coarse,
        fine_partition=fine,
        gained_partial_operation=gained,
        lost_total_operation=lost,
    )


@dataclass(frozen=True)
class FourStateSafeSpectrum:
    partition_shapes: tuple[tuple[int, ...], ...]
    partial_counts: tuple[int, ...]
    total_counts: tuple[int, ...]
    saturated_domain_counts: tuple[int, ...]


def four_state_refinement_spectrum() -> FourStateSafeSpectrum:
    """Reference U-shaped safe-operation abundance along [4]->[2,2]->[1^4]."""
    partitions = (
        {0: 0, 1: 0, 2: 0, 3: 0},
        {0: 0, 1: 0, 2: 1, 3: 1},
        {0: 0, 1: 1, 2: 2, 3: 3},
    )
    return FourStateSafeSpectrum(
        partition_shapes=tuple(partition_block_sizes(p) for p in partitions),
        partial_counts=tuple(safe_partial_endomap_count(p) for p in partitions),
        total_counts=tuple(safe_total_endomap_count(p) for p in partitions),
        saturated_domain_counts=tuple(saturated_domain_count(p) for p in partitions),
    )
