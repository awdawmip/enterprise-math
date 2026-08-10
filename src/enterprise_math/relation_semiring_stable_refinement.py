"""Coarsest shared-state refinement for one or more semiring relation interfaces.

A K-valued relation interface on a quotient partition does not merely expose a
state readout.  For every source quotient class and action it must assign a
representative-independent K-weight to every **current target quotient class**.

For a raw relation, the K-weight of a target block C is

    (# raw successors in C) * 1_K.

Given a current partition, split each block by the complete per-action vector of
these K-weights and iterate.  The fixed point is the unique coarsest refinement
on which the K-weighted relation is directly executable on the shared quotient
state space.

For several required semiring interfaces K_1,...,K_r on the **same** quotient
state space, split by all weight vectors simultaneously.  This differs from
merely taking the common refinement of the individually stable state partitions:
raw partition refinement can make an operation that was safe on its own quotient
unsafe again because target classes have been split by another interface.

For two semirings K,L, simultaneous shared-state refinement is exactly the same
as refinement using the product semiring KxL.  Thus the direct product semiring
is the canonical coarsest join for a coupled/compositional operation interface,
even though it can be finer than the weaker task that only asks for independent
K and L readouts side by side.

Weighted equitable partitions, congruence refinement and product semirings are
standard prior mathematics/CS.  The project value is the exact distinction
between independent readout joins and shared-state compositional joins.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Mapping, Sequence

from .admissible_support import Relation
from .relation_branching_semiring import (
    SemiringSpec,
    product_semiring,
    semiring_branching_partition,
)
from .relation_support_stable_refinement import (
    Partition,
    normalize_partition,
    partition_refines,
)


State = Hashable
Action = Hashable
Coefficient = Hashable


def _states(partition: Partition) -> frozenset[State]:
    current = normalize_partition(partition)
    return frozenset().union(*current)


def _family(
    partition: Partition,
    relations: Mapping[Action, Relation],
) -> dict[Action, Relation]:
    states = _states(partition)
    if not relations:
        raise ValueError("relation family must be nonempty")
    result: dict[Action, Relation] = {}
    for name, relation in relations.items():
        if not isinstance(relation, frozenset):
            raise TypeError("every relation must be a frozenset of ordered pairs")
        if any(source not in states or target not in states for source, target in relation):
            raise ValueError("relation contains state outside partition state set")
        result[name] = relation
    return result


def semiring_target_block_weights(
    partition: Sequence[Sequence[State] | frozenset[State]],
    relation: Relation,
    source: State,
    semiring: SemiringSpec,
) -> tuple[tuple[int, Coefficient], ...]:
    current = normalize_partition(partition)
    states = _states(current)
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
    counts: dict[int, int] = {}
    for left, target in relation:
        if left == source:
            target_block = block_of[target]
            counts[target_block] = counts.get(target_block, 0) + 1
    return tuple(
        sorted(
            (
                (block, coefficient)
                for block, count in counts.items()
                if (coefficient := semiring.natural(count)) != semiring.zero
            ),
            key=lambda item: item[0],
        )
    )


def semiring_relation_stable_on_partition(
    partition: Sequence[Sequence[State] | frozenset[State]],
    relations: Mapping[Action, Relation],
    semiring: SemiringSpec,
) -> bool:
    current = normalize_partition(partition)
    family = _family(current, relations)
    names = tuple(sorted(family, key=repr))
    for block in current:
        signatures = {
            tuple(
                (
                    name,
                    semiring_target_block_weights(
                        current,
                        family[name],
                        state,
                        semiring,
                    ),
                )
                for name in names
            )
            for state in block
        }
        if len(signatures) > 1:
            return False
    return True


def multi_semiring_relation_stable_on_partition(
    partition: Sequence[Sequence[State] | frozenset[State]],
    relations: Mapping[Action, Relation],
    semirings: Sequence[SemiringSpec],
) -> bool:
    current = normalize_partition(partition)
    specs = tuple(semirings)
    if not specs:
        raise ValueError("at least one semiring interface is required")
    return all(
        semiring_relation_stable_on_partition(current, relations, semiring)
        for semiring in specs
    )


def multi_semiring_refinement_step(
    partition: Sequence[Sequence[State] | frozenset[State]],
    relations: Mapping[Action, Relation],
    semirings: Sequence[SemiringSpec],
) -> Partition:
    """Split by all required coefficient interfaces on one shared target partition."""
    current = normalize_partition(partition)
    family = _family(current, relations)
    specs = tuple(semirings)
    if not specs:
        raise ValueError("at least one semiring interface is required")
    names = tuple(sorted(family, key=repr))

    refined: list[set[State]] = []
    for block in current:
        groups: dict[tuple[object, ...], set[State]] = {}
        for state in block:
            signature = tuple(
                (
                    semiring.name,
                    tuple(
                        (
                            name,
                            semiring_target_block_weights(
                                current,
                                family[name],
                                state,
                                semiring,
                            ),
                        )
                        for name in names
                    ),
                )
                for semiring in specs
            )
            groups.setdefault(signature, set()).add(state)
        refined.extend(groups.values())

    result = normalize_partition(refined)
    if not partition_refines(result, current):
        raise AssertionError("multi-semiring refinement failed to refine current partition")
    return result


@dataclass(frozen=True)
class SharedSemiringRefinementReport:
    initial_partition: Partition
    final_partition: Partition
    semiring_names: tuple[str, ...]
    steps: tuple[Partition, ...]

    @property
    def strict_refinement_steps(self) -> int:
        return len(self.steps) - 1


def coarsest_shared_semiring_refinement(
    partition: Sequence[Sequence[State] | frozenset[State]],
    relations: Mapping[Action, Relation],
    semirings: Sequence[SemiringSpec],
) -> SharedSemiringRefinementReport:
    initial = normalize_partition(partition)
    _family(initial, relations)
    specs = tuple(semirings)
    if not specs:
        raise ValueError("at least one semiring interface is required")
    current = initial
    steps = [current]
    state_count = len(_states(initial))

    while True:
        nxt = multi_semiring_refinement_step(current, relations, specs)
        if nxt == current:
            if not multi_semiring_relation_stable_on_partition(
                current,
                relations,
                specs,
            ):
                raise AssertionError("shared semiring fixed point is not stable")
            if len(steps) - 1 > state_count - len(initial):
                raise AssertionError("shared semiring refinement exceeded block-growth bound")
            return SharedSemiringRefinementReport(
                initial_partition=initial,
                final_partition=current,
                semiring_names=tuple(semiring.name for semiring in specs),
                steps=tuple(steps),
            )
        if len(nxt) <= len(current):
            raise AssertionError("strict shared refinement did not increase block count")
        steps.append(nxt)
        current = nxt


def candidate_refines_shared_coarsest(
    report: SharedSemiringRefinementReport,
    candidate: Sequence[Sequence[State] | frozenset[State]],
    relations: Mapping[Action, Relation],
    semirings: Sequence[SemiringSpec],
) -> bool:
    current = normalize_partition(candidate)
    if not partition_refines(current, report.initial_partition):
        raise ValueError("candidate must refine initial partition")
    if not multi_semiring_relation_stable_on_partition(current, relations, semirings):
        raise ValueError("candidate must support every required semiring interface")
    if not partition_refines(current, report.final_partition):
        raise AssertionError("stable candidate failed to refine claimed coarsest shared quotient")
    return True


def product_semiring_refinement_matches_shared_pair(
    partition: Sequence[Sequence[State] | frozenset[State]],
    relations: Mapping[Action, Relation],
    left: SemiringSpec,
    right: SemiringSpec,
) -> bool:
    initial = normalize_partition(partition)
    shared = coarsest_shared_semiring_refinement(
        initial,
        relations,
        (left, right),
    )
    product_report = coarsest_shared_semiring_refinement(
        initial,
        relations,
        (product_semiring(left, right),),
    )
    if shared.steps != product_report.steps:
        raise AssertionError("product semiring did not equal coupled two-interface refinement")
    return True


def branching_signature_sequence_matches_weighted_refinement(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation,
    semiring: SemiringSpec,
) -> bool:
    order = tuple(states)
    if not order or len(set(order)) != len(order):
        raise ValueError("states must be a nonempty distinct sequence")
    groups: dict[object, set[State]] = {}
    for state in order:
        groups.setdefault(observation(state), set()).add(state)
    initial = normalize_partition(tuple(groups.values()))
    report = coarsest_shared_semiring_refinement(
        initial,
        relations,
        (semiring,),
    )

    branching_steps = [initial]
    horizon = 1
    while True:
        nxt = semiring_branching_partition(
            order,
            relations,
            observation,
            horizon,
            semiring,
        )
        if nxt == branching_steps[-1]:
            break
        branching_steps.append(nxt)
        horizon += 1
        if horizon > len(order) + 1:
            raise AssertionError("branching sequence failed finite stabilization bound")

    if tuple(branching_steps) != report.steps:
        raise AssertionError("branching signatures disagree with weighted refinement fixed point")
    return True
