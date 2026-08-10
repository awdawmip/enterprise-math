"""Coarsest finite state refinement making required total unary operations safe.

Let ``E_0`` be an observational equivalence on a finite state set X and let U be
a finite family of total unary operations on X.  We seek the **largest**
equivalence ``E_*`` contained in ``E_0`` such that every operation in U preserves
``E_*``.

Iterate

    E_(k+1) = E_k intersect intersection_(u in U) (u x u)^(-1)(E_k).

At partition level, split each current block according to the vector of target
blocks reached by all required operations.  Every strict step increases the
number of blocks, so the process terminates on finite X.

The fixed point is operation-safe by construction.  It is the unique coarsest
safe refinement: any equivalence F contained in E_0 and preserved by every u in
U is contained in every E_k by induction, hence in E_*.

This is standard finite congruence/partition refinement.  The project value is
using it as a semantic precision repair: when an operation-capability join is
realizable by state splitting, this compiler returns the minimum required state
refinement rather than guessing a larger scalar precision.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Mapping, Sequence

from .semantic_precision_preorder import (
    Partition,
    normalize_partition,
    operation_safe_on_partition,
    partition_refines,
    partition_state_set,
)


State = Hashable
OperationName = Hashable
Operation = Mapping[State, State]


def _operations(
    partition: Partition,
    operations: Mapping[OperationName, Mapping[State, State]],
) -> dict[OperationName, dict[State, State]]:
    states = partition_state_set(partition)
    result = {}
    for name, operation in operations.items():
        mapping = dict(operation)
        if set(mapping) != set(states):
            raise ValueError("every required operation must be total on the state set")
        if any(target not in states for target in mapping.values()):
            raise ValueError("operation target lies outside the state set")
        result[name] = mapping
    return result


def operation_refinement_step(
    partition: Sequence[Sequence[State] | frozenset[State]],
    operations: Mapping[OperationName, Mapping[State, State]],
) -> Partition:
    """One simultaneous split by target-block signatures of all operations."""
    current = normalize_partition(partition)
    required = _operations(current, operations)
    if not required:
        return current

    block_of = {
        state: index
        for index, block in enumerate(current)
        for state in block
    }
    operation_names = tuple(sorted(required, key=repr))
    refined_blocks = []
    for block in current:
        groups: dict[tuple[int, ...], set[State]] = {}
        for state in block:
            signature = tuple(
                block_of[required[name][state]]
                for name in operation_names
            )
            groups.setdefault(signature, set()).add(state)
        refined_blocks.extend(groups.values())
    refined = normalize_partition(refined_blocks)
    if not partition_refines(refined, current):
        raise AssertionError("operation refinement failed to refine current partition")
    return refined


@dataclass(frozen=True)
class OperationSafeRefinementReport:
    initial_partition: Partition
    final_partition: Partition
    required_operations: tuple[OperationName, ...]
    steps: tuple[Partition, ...]

    @property
    def strict_refinement_steps(self) -> int:
        return len(self.steps) - 1

    @property
    def initial_block_count(self) -> int:
        return len(self.initial_partition)

    @property
    def final_block_count(self) -> int:
        return len(self.final_partition)

    @property
    def added_state_distinctions(self) -> int:
        return self.final_block_count - self.initial_block_count


def coarsest_operation_safe_refinement(
    partition: Sequence[Sequence[State] | frozenset[State]],
    operations: Mapping[OperationName, Mapping[State, State]],
) -> OperationSafeRefinementReport:
    """Return the unique largest operation-stable equivalence below the input."""
    initial = normalize_partition(partition)
    required = _operations(initial, operations)
    current = initial
    steps = [current]
    state_count = len(partition_state_set(initial))

    while True:
        nxt = operation_refinement_step(current, required)
        if nxt == current:
            for operation in required.values():
                if not operation_safe_on_partition(current, operation):
                    raise AssertionError("fixed point still contains unsafe required operation")
            if len(steps) - 1 > state_count - len(initial):
                raise AssertionError("finite partition refinement exceeded block-growth bound")
            return OperationSafeRefinementReport(
                initial_partition=initial,
                final_partition=current,
                required_operations=tuple(sorted(required, key=repr)),
                steps=tuple(steps),
            )
        if len(nxt) <= len(current):
            raise AssertionError("strict operation refinement did not increase block count")
        steps.append(nxt)
        current = nxt


def partition_is_safe_for_all(
    partition: Sequence[Sequence[State] | frozenset[State]],
    operations: Mapping[OperationName, Mapping[State, State]],
) -> bool:
    normalized = normalize_partition(partition)
    required = _operations(normalized, operations)
    return all(
        operation_safe_on_partition(normalized, operation)
        for operation in required.values()
    )


def verify_coarsest_against_candidate(
    report: OperationSafeRefinementReport,
    candidate: Sequence[Sequence[State] | frozenset[State]],
    operations: Mapping[OperationName, Mapping[State, State]],
) -> bool:
    """Verify any supplied safe candidate below E0 is finer than/equal to E*."""
    if not isinstance(report, OperationSafeRefinementReport):
        raise TypeError("report must be OperationSafeRefinementReport")
    candidate_partition = normalize_partition(candidate)
    if not partition_refines(candidate_partition, report.initial_partition):
        raise ValueError("candidate must refine the initial partition")
    if not partition_is_safe_for_all(candidate_partition, operations):
        raise ValueError("candidate must make every required operation safe")
    if not partition_refines(candidate_partition, report.final_partition):
        raise AssertionError("safe candidate is not below the claimed coarsest safe refinement")
    return True
