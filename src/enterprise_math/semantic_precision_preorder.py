"""Task-relative semantic precision separates state detail from safe capabilities.

A raw quotient/partition precision only records which fine states remain
indistinguishable.  It does not determine which operations, logical implications,
reflection laws or witness semantics continue to descend safely.

Represent one task-relative precision state by

    (equivalence partition, capability set).

The semantic preorder is the product order:

    P2 >=_T P1

iff

1. P2 is observationally at least as fine as P1: every P2-equivalent pair is
   P1-equivalent;
2. every declared capability safe in P1 is also safe in P2.

Raw partition refinement alone can therefore fail semantic dominance.  The safe
operation family is not monotone under partition refinement, and coefficient
quotient laws show the same phenomenon: mod p^2 has finer residues than mod p,
but loses the integral-domain branch law.

The object here is deliberately abstract.  Capability names are task-relative
semantic commitments supplied by the caller; the module does not claim one
universal capability vocabulary.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Mapping, Sequence


State = Hashable
Capability = Hashable
Operation = Mapping[State, State]
Partition = tuple[frozenset[State], ...]


def normalize_partition(blocks: Sequence[Sequence[State] | frozenset[State]]) -> Partition:
    values = tuple(frozenset(block) for block in blocks)
    if not values:
        raise ValueError("partition must contain at least one block")
    if any(not block for block in values):
        raise ValueError("partition blocks must be nonempty")
    union = set()
    for block in values:
        if union.intersection(block):
            raise ValueError("partition blocks must be disjoint")
        union.update(block)
    return tuple(sorted(values, key=lambda block: tuple(sorted(map(repr, block)))))


def partition_state_set(partition: Partition) -> frozenset[State]:
    normalized = normalize_partition(partition)
    return frozenset().union(*normalized)


def partition_refines(finer: Partition, coarser: Partition) -> bool:
    fine = normalize_partition(finer)
    coarse = normalize_partition(coarser)
    if partition_state_set(fine) != partition_state_set(coarse):
        raise ValueError("partitions must cover the same state set")
    return all(
        any(block.issubset(coarse_block) for coarse_block in coarse)
        for block in fine
    )


def operation_safe_on_partition(
    partition: Partition,
    operation: Mapping[State, State],
) -> bool:
    normalized = normalize_partition(partition)
    states = partition_state_set(normalized)
    if set(operation) != set(states):
        raise ValueError("operation must be defined on every partition state exactly once")
    if any(target not in states for target in operation.values()):
        raise ValueError("operation target lies outside the partition state set")

    block_of = {
        state: index
        for index, block in enumerate(normalized)
        for state in block
    }
    return all(
        len({block_of[operation[state]] for state in block}) <= 1
        for block in normalized
    )


def safe_operation_names(
    partition: Partition,
    operations: Mapping[Capability, Mapping[State, State]],
) -> frozenset[Capability]:
    if not operations:
        return frozenset()
    return frozenset(
        name
        for name, operation in operations.items()
        if operation_safe_on_partition(partition, operation)
    )


@dataclass(frozen=True)
class SemanticPrecisionState:
    partition: Partition
    capabilities: frozenset[Capability]
    description: str = ""

    @property
    def states(self) -> frozenset[State]:
        return partition_state_set(self.partition)


def semantic_precision_state(
    partition: Sequence[Sequence[State] | frozenset[State]],
    capabilities: Sequence[Capability] | frozenset[Capability] = (),
    *,
    description: str = "",
) -> SemanticPrecisionState:
    return SemanticPrecisionState(
        partition=normalize_partition(partition),
        capabilities=frozenset(capabilities),
        description=description,
    )


def semantically_refines(
    finer: SemanticPrecisionState,
    coarser: SemanticPrecisionState,
) -> bool:
    if not isinstance(finer, SemanticPrecisionState) or not isinstance(coarser, SemanticPrecisionState):
        raise TypeError("semantic precision values must be SemanticPrecisionState")
    if finer.states != coarser.states:
        raise ValueError("semantic precision states must share one underlying state set")
    return (
        partition_refines(finer.partition, coarser.partition)
        and coarser.capabilities.issubset(finer.capabilities)
    )


def observationally_refines_but_semantically_not(
    finer: SemanticPrecisionState,
    coarser: SemanticPrecisionState,
) -> bool:
    return (
        partition_refines(finer.partition, coarser.partition)
        and not semantically_refines(finer, coarser)
    )


def semantically_incomparable(
    left: SemanticPrecisionState,
    right: SemanticPrecisionState,
) -> bool:
    return (
        not semantically_refines(left, right)
        and not semantically_refines(right, left)
    )


@dataclass(frozen=True)
class SafeOperationRefinementSwitch:
    coarser_partition: Partition
    finer_partition: Partition
    operation_safe_coarser: bool
    operation_safe_finer: bool

    @property
    def lost_under_refinement(self) -> bool:
        return self.operation_safe_coarser and not self.operation_safe_finer

    @property
    def gained_under_refinement(self) -> bool:
        return not self.operation_safe_coarser and self.operation_safe_finer


def safe_operation_refinement_switch(
    coarser_partition: Partition,
    finer_partition: Partition,
    operation: Mapping[State, State],
) -> SafeOperationRefinementSwitch:
    coarse = normalize_partition(coarser_partition)
    fine = normalize_partition(finer_partition)
    if not partition_refines(fine, coarse):
        raise ValueError("finer_partition must refine coarser_partition")
    return SafeOperationRefinementSwitch(
        coarser_partition=coarse,
        finer_partition=fine,
        operation_safe_coarser=operation_safe_on_partition(coarse, operation),
        operation_safe_finer=operation_safe_on_partition(fine, operation),
    )
