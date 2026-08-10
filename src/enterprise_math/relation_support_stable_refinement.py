"""Coarsest finite refinement making relation-valued support actions descend.

For a finite state set X, an initial observation partition E_0, and a finite
family of labelled relations R_a subseteq X x X, define the current support
signature of source x under action a to be

    { [y]_E : x R_a y }.

The empty set is retained exactly and means that the relation has no successor
from x.  Split each current block by the tuple of these target-block sets over
all declared relation actions and iterate to a fixed point.

The fixed point is the unique largest equivalence E_* contained in E_0 such
that equivalent sources have the same set of E_*-target classes under every
relation.  This is the support-level stable/bisimulation-style quotient for the
declared labelled relation family.

Important semantic boundary: this quotient is generally stronger than the
P023 partition induced only by terminal observed-support signatures of literal
relation words.  Multivalued branching can retain correlations between the
future behaviours of individual successors even when every literal word sees
only the same union of terminal observations.  In deterministic/partial
(singleton-or-empty successor) specializations, that correlation gap disappears.

Finite labelled transition-system partition refinement and bisimulation are
standard prior mathematics/computer science.  The project value is the exact
semantic routing between A4 support-level operation descent and the coarser
terminal-support future language.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Hashable, Mapping, Sequence

from .admissible_support import Relation
from .relation_boolean_future_semimodule import (
    relation_boolean_future_semimodule_report,
)


State = Hashable
Action = Hashable
Observation = Hashable
Partition = tuple[frozenset[State], ...]


def normalize_partition(
    blocks: Sequence[Sequence[State] | frozenset[State]],
) -> Partition:
    values = tuple(frozenset(block) for block in blocks)
    if not values:
        raise ValueError("partition must contain at least one block")
    if any(not block for block in values):
        raise ValueError("partition blocks must be nonempty")
    seen: set[State] = set()
    for block in values:
        if seen.intersection(block):
            raise ValueError("partition blocks must be disjoint")
        seen.update(block)
    return tuple(sorted(values, key=lambda block: tuple(sorted(map(repr, block)))))


def partition_states(partition: Partition) -> frozenset[State]:
    current = normalize_partition(partition)
    return frozenset().union(*current)


def partition_refines(finer: Partition, coarser: Partition) -> bool:
    fine = normalize_partition(finer)
    coarse = normalize_partition(coarser)
    if partition_states(fine) != partition_states(coarse):
        raise ValueError("partitions must cover the same state set")
    return all(
        any(block.issubset(coarse_block) for coarse_block in coarse)
        for block in fine
    )


def partition_from_observation(
    states: Sequence[State],
    observation: Callable[[State], Observation],
) -> Partition:
    order = tuple(states)
    if not order or len(set(order)) != len(order):
        raise ValueError("states must be a nonempty distinct sequence")
    groups: dict[Observation, set[State]] = {}
    for state in order:
        groups.setdefault(observation(state), set()).add(state)
    return normalize_partition(tuple(groups.values()))


def _relation_family(
    partition: Partition,
    relations: Mapping[Action, Relation],
) -> dict[Action, Relation]:
    states = partition_states(partition)
    if not relations:
        raise ValueError("relation family must be nonempty")
    result: dict[Action, Relation] = {}
    for name, relation in relations.items():
        if not isinstance(relation, frozenset):
            raise TypeError("every relation must be a frozenset of ordered pairs")
        if any(source not in states or target not in states for source, target in relation):
            raise ValueError("relation contains state outside the partition state set")
        result[name] = relation
    return result


def relation_target_block_support(
    partition: Sequence[Sequence[State] | frozenset[State]],
    relation: Relation,
    source: State,
) -> frozenset[int]:
    current = normalize_partition(partition)
    states = partition_states(current)
    if source not in states:
        raise ValueError("source lies outside partition state set")
    if not isinstance(relation, frozenset):
        raise TypeError("relation must be a frozenset")
    if any(left not in states or right not in states for left, right in relation):
        raise ValueError("relation contains state outside partition state set")
    block_of = {
        state: index
        for index, block in enumerate(current)
        for state in block
    }
    return frozenset(
        block_of[target]
        for left, target in relation
        if left == source
    )


def relation_support_stable_on_partition(
    partition: Sequence[Sequence[State] | frozenset[State]],
    relation: Relation,
) -> bool:
    """Whether equal source blocks have equal sets of target quotient blocks."""
    current = normalize_partition(partition)
    for block in current:
        signatures = {
            relation_target_block_support(current, relation, state)
            for state in block
        }
        if len(signatures) > 1:
            return False
    return True


def relation_family_support_stable_on_partition(
    partition: Sequence[Sequence[State] | frozenset[State]],
    relations: Mapping[Action, Relation],
) -> bool:
    current = normalize_partition(partition)
    family = _relation_family(current, relations)
    return all(
        relation_support_stable_on_partition(current, relation)
        for relation in family.values()
    )


def relation_support_refinement_step(
    partition: Sequence[Sequence[State] | frozenset[State]],
    relations: Mapping[Action, Relation],
) -> Partition:
    """One simultaneous split by per-action sets of current target blocks."""
    current = normalize_partition(partition)
    family = _relation_family(current, relations)
    names = tuple(sorted(family, key=repr))
    block_of = {
        state: index
        for index, block in enumerate(current)
        for state in block
    }

    target_supports: dict[tuple[Action, State], frozenset[int]] = {}
    for name in names:
        relation = family[name]
        targets_by_source: dict[State, set[int]] = {state: set() for state in block_of}
        for source, target in relation:
            targets_by_source[source].add(block_of[target])
        for state, support in targets_by_source.items():
            target_supports[(name, state)] = frozenset(support)

    refined_blocks: list[set[State]] = []
    for block in current:
        groups: dict[tuple[frozenset[int], ...], set[State]] = {}
        for state in block:
            signature = tuple(target_supports[(name, state)] for name in names)
            groups.setdefault(signature, set()).add(state)
        refined_blocks.extend(groups.values())

    refined = normalize_partition(refined_blocks)
    if not partition_refines(refined, current):
        raise AssertionError("relation-support refinement failed to refine current partition")
    return refined


@dataclass(frozen=True)
class RelationSupportStableRefinementReport:
    initial_partition: Partition
    final_partition: Partition
    required_relations: tuple[Action, ...]
    steps: tuple[Partition, ...]

    @property
    def strict_refinement_steps(self) -> int:
        return len(self.steps) - 1

    @property
    def added_state_distinctions(self) -> int:
        return len(self.final_partition) - len(self.initial_partition)


def coarsest_relation_support_stable_refinement(
    partition: Sequence[Sequence[State] | frozenset[State]],
    relations: Mapping[Action, Relation],
) -> RelationSupportStableRefinementReport:
    """Largest relation-support-stable equivalence below the initial partition."""
    initial = normalize_partition(partition)
    family = _relation_family(initial, relations)
    current = initial
    steps = [current]
    state_count = len(partition_states(initial))

    while True:
        nxt = relation_support_refinement_step(current, family)
        if nxt == current:
            if not relation_family_support_stable_on_partition(current, family):
                raise AssertionError("fixed point is not relation-support stable")
            if len(steps) - 1 > state_count - len(initial):
                raise AssertionError("finite relation refinement exceeded block-growth bound")
            return RelationSupportStableRefinementReport(
                initial_partition=initial,
                final_partition=current,
                required_relations=tuple(sorted(family, key=repr)),
                steps=tuple(steps),
            )
        if len(nxt) <= len(current):
            raise AssertionError("strict relation refinement did not increase block count")
        steps.append(nxt)
        current = nxt


def verify_relation_support_coarsest_against_candidate(
    report: RelationSupportStableRefinementReport,
    candidate: Sequence[Sequence[State] | frozenset[State]],
    relations: Mapping[Action, Relation],
) -> bool:
    current = normalize_partition(candidate)
    if not partition_refines(current, report.initial_partition):
        raise ValueError("candidate must refine the initial partition")
    if not relation_family_support_stable_on_partition(current, relations):
        raise ValueError("candidate must be stable for every relation")
    if not partition_refines(current, report.final_partition):
        raise AssertionError("stable candidate is not below claimed coarsest refinement")
    return True


def relation_support_stable_refines_terminal_trace_partition(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
) -> bool:
    """Verify support-stable/bisimulation-like precision refines trace precision.

    The terminal trace partition is taken from the exact Boolean-semimodule
    support compiler at its permanent fixed point.
    """
    initial = partition_from_observation(states, observation)
    stable = coarsest_relation_support_stable_refinement(initial, relations)
    trace = relation_boolean_future_semimodule_report(states, relations, observation)
    trace_partition = normalize_partition(tuple(trace.steps[-1].state_partition))
    if not partition_refines(stable.final_partition, trace_partition):
        raise AssertionError("relation-stable quotient failed to imply terminal support trace equivalence")
    return True


def support_stability_is_strictly_finer_than_terminal_trace(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
) -> bool:
    initial = partition_from_observation(states, observation)
    stable = coarsest_relation_support_stable_refinement(initial, relations)
    trace = relation_boolean_future_semimodule_report(states, relations, observation)
    trace_partition = normalize_partition(tuple(trace.steps[-1].state_partition))
    if not partition_refines(stable.final_partition, trace_partition):
        raise AssertionError("stable relation quotient must refine terminal trace quotient")
    return stable.final_partition != trace_partition
