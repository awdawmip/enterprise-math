"""DOMAIN-aware coarsest refinement for required finite partial unary operations.

This is a consumption bridge from the total-operation semantic refinement compiler
to the existing FQ-006/P023 partial-operation quotient semantics.  It does **not**
redefine the ownership of partial quotients.

Let X be a finite state set, E_0 an observational equivalence, and U a finite
family of partial unary operations ``u:X ⇀ X``.  A partial operation descends
through E exactly when equivalent source states have

1. the same definedness; and
2. when defined, E-equivalent targets.

Equivalently, relative to a current partition E, each state has one per-operation
signature

    UNDEFINED

or

    (DEFINED, target_block_id).

Split every current block by the joint signature over all required partial
operations, then repeat until stable.  Every strict step increases the block
count, so the procedure terminates on finite X.

The fixed point is the unique largest equivalence below E_0 through which all
required partial operations descend.  The maximality proof is the same induction
as for total operations, with definedness included in the signature.

When every operation is total, the compiler reduces exactly to the total unary
refinement in ``semantic_operation_refinement``.

The construction also matches the standard FQ-006 verification totalization:
adjoin a fresh observable ``UNDEFINED`` state, map every undefined application to
that state, keep it a singleton block, and totalize each operation by fixing the
new state.  Restricting the total-operation coarsest refinement back to X yields
the same partition.  This is an analysis/verification equivalence, not a claim
that UNDEFINED is a physical successor state.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Mapping, Sequence

from .semantic_operation_refinement import (
    coarsest_operation_safe_refinement,
)
from .semantic_precision_preorder import (
    Partition,
    normalize_partition,
    partition_refines,
    partition_state_set,
)


State = Hashable
OperationName = Hashable
PartialOperation = Mapping[State, State]


UNDEFINED = "UNDEFINED"
DEFINED = "DEFINED"


def _partial_operations(
    partition: Partition,
    operations: Mapping[OperationName, Mapping[State, State]],
) -> dict[OperationName, dict[State, State]]:
    states = partition_state_set(partition)
    result: dict[OperationName, dict[State, State]] = {}
    for name, operation in operations.items():
        mapping = dict(operation)
        if any(source not in states for source in mapping):
            raise ValueError("partial operation source lies outside the state set")
        if any(target not in states for target in mapping.values()):
            raise ValueError("partial operation target lies outside the state set")
        result[name] = mapping
    return result


def partial_operation_safe_on_partition(
    partition: Sequence[Sequence[State] | frozenset[State]],
    operation: Mapping[State, State],
) -> bool:
    """Exact FQ-006-style DOMAIN + target-quotient safety criterion."""
    current = normalize_partition(partition)
    states = partition_state_set(current)
    mapping = dict(operation)
    if any(source not in states for source in mapping):
        raise ValueError("partial operation source lies outside the state set")
    if any(target not in states for target in mapping.values()):
        raise ValueError("partial operation target lies outside the state set")

    block_of = {
        state: index
        for index, block in enumerate(current)
        for state in block
    }
    for block in current:
        defined_flags = {state in mapping for state in block}
        if len(defined_flags) > 1:
            return False
        if True in defined_flags:
            target_blocks = {block_of[mapping[state]] for state in block}
            if len(target_blocks) > 1:
                return False
    return True


def partial_operation_refinement_step(
    partition: Sequence[Sequence[State] | frozenset[State]],
    operations: Mapping[OperationName, Mapping[State, State]],
) -> Partition:
    """Split blocks by UNDEFINED / defined-target-block signatures."""
    current = normalize_partition(partition)
    required = _partial_operations(current, operations)
    if not required:
        return current

    block_of = {
        state: index
        for index, block in enumerate(current)
        for state in block
    }
    names = tuple(sorted(required, key=repr))
    refined_blocks: list[set[State]] = []

    for block in current:
        groups: dict[tuple[tuple[str, int | None], ...], set[State]] = {}
        for state in block:
            signature = tuple(
                (
                    (DEFINED, block_of[required[name][state]])
                    if state in required[name]
                    else (UNDEFINED, None)
                )
                for name in names
            )
            groups.setdefault(signature, set()).add(state)
        refined_blocks.extend(groups.values())

    refined = normalize_partition(refined_blocks)
    if not partition_refines(refined, current):
        raise AssertionError("partial-operation refinement failed to refine current partition")
    return refined


@dataclass(frozen=True)
class PartialOperationSafeRefinementReport:
    initial_partition: Partition
    final_partition: Partition
    required_operations: tuple[OperationName, ...]
    steps: tuple[Partition, ...]

    @property
    def strict_refinement_steps(self) -> int:
        return len(self.steps) - 1

    @property
    def added_state_distinctions(self) -> int:
        return len(self.final_partition) - len(self.initial_partition)


def coarsest_partial_operation_safe_refinement(
    partition: Sequence[Sequence[State] | frozenset[State]],
    operations: Mapping[OperationName, Mapping[State, State]],
) -> PartialOperationSafeRefinementReport:
    """Largest equivalence below E0 safe for every required partial operation."""
    initial = normalize_partition(partition)
    required = _partial_operations(initial, operations)
    current = initial
    steps = [current]
    state_count = len(partition_state_set(initial))

    while True:
        nxt = partial_operation_refinement_step(current, required)
        if nxt == current:
            for operation in required.values():
                if not partial_operation_safe_on_partition(current, operation):
                    raise AssertionError("partial-operation fixed point is still unsafe")
            if len(steps) - 1 > state_count - len(initial):
                raise AssertionError("finite DOMAIN-aware refinement exceeded block-growth bound")
            return PartialOperationSafeRefinementReport(
                initial_partition=initial,
                final_partition=current,
                required_operations=tuple(sorted(required, key=repr)),
                steps=tuple(steps),
            )
        if len(nxt) <= len(current):
            raise AssertionError("strict partial-operation refinement did not increase block count")
        steps.append(nxt)
        current = nxt


def partial_partition_is_safe_for_all(
    partition: Sequence[Sequence[State] | frozenset[State]],
    operations: Mapping[OperationName, Mapping[State, State]],
) -> bool:
    current = normalize_partition(partition)
    required = _partial_operations(current, operations)
    return all(
        partial_operation_safe_on_partition(current, operation)
        for operation in required.values()
    )


def verify_partial_coarsest_against_candidate(
    report: PartialOperationSafeRefinementReport,
    candidate: Sequence[Sequence[State] | frozenset[State]],
    operations: Mapping[OperationName, Mapping[State, State]],
) -> bool:
    candidate_partition = normalize_partition(candidate)
    if not partition_refines(candidate_partition, report.initial_partition):
        raise ValueError("candidate must refine the initial partition")
    if not partial_partition_is_safe_for_all(candidate_partition, operations):
        raise ValueError("candidate must make every required partial operation safe")
    if not partition_refines(candidate_partition, report.final_partition):
        raise AssertionError("safe candidate is not below the claimed coarsest partial repair")
    return True


def total_specialization_matches(
    partition: Sequence[Sequence[State] | frozenset[State]],
    operations: Mapping[OperationName, Mapping[State, State]],
) -> bool:
    """When every required operation is total, partial and total compilers agree."""
    current = normalize_partition(partition)
    states = partition_state_set(current)
    required = _partial_operations(current, operations)
    if any(set(operation) != set(states) for operation in required.values()):
        raise ValueError("total specialization requires every operation to be total")
    partial_report = coarsest_partial_operation_safe_refinement(current, required)
    total_report = coarsest_operation_safe_refinement(current, required)
    if partial_report.final_partition != total_report.final_partition:
        raise AssertionError("partial compiler disagreed with total specialization")
    return True


def _fresh_undefined_state(states: frozenset[State]) -> tuple[str, int]:
    index = 0
    while ("__UNDEFINED__", index) in states:
        index += 1
    return ("__UNDEFINED__", index)


def observable_undefined_totalization_matches(
    partition: Sequence[Sequence[State] | frozenset[State]],
    operations: Mapping[OperationName, Mapping[State, State]],
) -> bool:
    """Verify the FQ-006 observable-UNDEFINED totalization gives the same repair.

    A single fresh UNDEFINED state is added as its own visible block.  Each
    partial operation sends undefined source states to it and fixes it.  The
    total-operation coarsest refinement is then restricted back to X.
    """
    current = normalize_partition(partition)
    states = partition_state_set(current)
    required = _partial_operations(current, operations)
    undefined = _fresh_undefined_state(states)
    extended_partition = normalize_partition((*current, frozenset({undefined})))

    totalized: dict[OperationName, dict[State, State]] = {}
    for name, operation in required.items():
        mapping = {
            state: operation[state] if state in operation else undefined
            for state in states
        }
        mapping[undefined] = undefined
        totalized[name] = mapping

    total_report = coarsest_operation_safe_refinement(
        extended_partition,
        totalized,
    )
    restricted = normalize_partition(
        frozenset(state for state in block if state != undefined)
        for block in total_report.final_partition
        if any(state != undefined for state in block)
    )
    partial_report = coarsest_partial_operation_safe_refinement(current, required)
    if restricted != partial_report.final_partition:
        raise AssertionError("observable-UNDEFINED totalization changed coarsest repair")
    return True
