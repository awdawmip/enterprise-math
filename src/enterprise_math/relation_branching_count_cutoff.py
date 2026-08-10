"""Finite coefficient cutoff for exact natural-count branching precision.

For a finite raw relation family let

    Delta = max_(action,source) outdegree(action,source).

Every weighted refinement step counts how many raw successors of a source land
in one **current target partition block**.  Such a count always lies in

    {0,1,...,Delta}.

Therefore any modulus M>Delta is injective on every coefficient value that can
ever appear in one refinement step.  Starting from the same observation
partition, exact-N and mod-M weighted refinement steps are identical by
induction, hence their complete branching-signature partition sequences and
stable quotients are identical.

This gives a uniform finite arithmetic cutoff

    M_safe = max(2, Delta+1)

for exact count-branching state precision.  It is independent of future horizon
and independent of cycles.

The bound is worst-case sharp over relation families with maximum outdegree at
most Delta: for any 2<=M<=Delta, one can use two source states where one has zero
successors and the other has exactly M behaviourally equivalent successors.
Exact counts distinguish 0 from M while mod-M annihilates the difference.

For one fixed relation system, a smaller modulus may still suffice because the
critical count collisions may never occur.  The module therefore also provides
a finite search for the smallest exact modulus; Delta+1 guarantees termination.

Finite equitable refinement and modular injectivity are standard prior
mathematics/CS.  The project value is the sharp contrast with terminal path
counts: direct branching-operation state needs only one-step count precision,
not precision large enough to represent accumulated path counts.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Hashable, Mapping, Sequence

from .admissible_support import Relation
from .relation_branching_semiring import (
    modular_semiring,
    natural_semiring,
)
from .relation_semiring_stable_refinement import (
    SharedSemiringRefinementReport,
    coarsest_shared_semiring_refinement,
)
from .relation_support_stable_refinement import (
    Partition,
    normalize_partition,
    partition_from_observation,
)


State = Hashable
Action = Hashable
Observation = Hashable


def _states(values: Sequence[State]) -> tuple[State, ...]:
    result = tuple(values)
    if not result or len(set(result)) != len(result):
        raise ValueError("states must be a nonempty distinct sequence")
    return result


def _family(
    states: tuple[State, ...],
    relations: Mapping[Action, Relation],
) -> dict[Action, Relation]:
    if not relations:
        raise ValueError("relation family must be nonempty")
    state_set = set(states)
    result: dict[Action, Relation] = {}
    for name, relation in relations.items():
        if not isinstance(relation, frozenset):
            raise TypeError("every relation must be a frozenset of ordered pairs")
        if any(source not in state_set or target not in state_set for source, target in relation):
            raise ValueError("relation contains state outside declared state set")
        result[name] = relation
    return result


def relation_max_outdegree(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
) -> int:
    order = _states(states)
    family = _family(order, relations)
    maximum = 0
    for relation in family.values():
        counts = {state: 0 for state in order}
        for source, _target in relation:
            counts[source] += 1
        maximum = max(maximum, *counts.values())
    return maximum


def universal_exact_count_branching_modulus(max_outdegree: int) -> int:
    """Smallest legal integer modulus guaranteed by the Delta theorem."""
    if isinstance(max_outdegree, bool) or not isinstance(max_outdegree, int):
        raise TypeError("max_outdegree must be an integer")
    if max_outdegree < 0:
        raise ValueError("max_outdegree must be nonnegative")
    return max(2, max_outdegree + 1)


def modulus_reflects_all_block_counts(
    max_outdegree: int,
    modulus: int,
) -> bool:
    if isinstance(max_outdegree, bool) or not isinstance(max_outdegree, int):
        raise TypeError("max_outdegree must be an integer")
    if max_outdegree < 0:
        raise ValueError("max_outdegree must be nonnegative")
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 1:
        raise ValueError("modulus must exceed one")
    return modulus > max_outdegree


def _stable_report(
    states: tuple[State, ...],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    semiring,
) -> SharedSemiringRefinementReport:
    initial = partition_from_observation(states, observation)
    return coarsest_shared_semiring_refinement(
        initial,
        relations,
        (semiring,),
    )


def exact_count_and_modular_sequences_agree_above_outdegree(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    modulus: int,
) -> bool:
    order = _states(states)
    family = _family(order, relations)
    delta = relation_max_outdegree(order, family)
    if not modulus_reflects_all_block_counts(delta, modulus):
        raise ValueError("the theorem requires modulus > maximum raw outdegree")
    exact = _stable_report(
        order,
        family,
        observation,
        natural_semiring(),
    )
    modular = _stable_report(
        order,
        family,
        observation,
        modular_semiring(modulus),
    )
    if exact.steps != modular.steps:
        raise AssertionError("M>Delta failed to reproduce exact count refinement sequence")
    return True


@dataclass(frozen=True)
class CountBranchingCutoffReport:
    state_count: int
    maximum_outdegree: int
    theorem_cutoff_modulus: int
    tested_modulus: int
    theorem_guaranteed: bool
    exact_steps: tuple[Partition, ...]
    modular_steps: tuple[Partition, ...]

    @property
    def final_partitions_equal(self) -> bool:
        return self.exact_steps[-1] == self.modular_steps[-1]

    @property
    def complete_sequences_equal(self) -> bool:
        return self.exact_steps == self.modular_steps


def count_branching_cutoff_report(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    modulus: int | None = None,
) -> CountBranchingCutoffReport:
    order = _states(states)
    family = _family(order, relations)
    delta = relation_max_outdegree(order, family)
    cutoff = universal_exact_count_branching_modulus(delta)
    if modulus is None:
        tested = cutoff
    else:
        if isinstance(modulus, bool) or not isinstance(modulus, int):
            raise TypeError("modulus must be an integer")
        if modulus <= 1:
            raise ValueError("modulus must exceed one")
        tested = modulus

    exact = _stable_report(order, family, observation, natural_semiring())
    modular = _stable_report(order, family, observation, modular_semiring(tested))
    guaranteed = tested > delta
    if guaranteed and exact.steps != modular.steps:
        raise AssertionError("theorem-guaranteed modular cutoff disagreed with exact N branching")

    return CountBranchingCutoffReport(
        state_count=len(order),
        maximum_outdegree=delta,
        theorem_cutoff_modulus=cutoff,
        tested_modulus=tested,
        theorem_guaranteed=guaranteed,
        exact_steps=exact.steps,
        modular_steps=modular.steps,
    )


def minimal_exact_modulus_for_count_branching(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
) -> int:
    """Find the least M>=2 with the exact same complete refinement sequence.

    Search is finite because Delta+1 is guaranteed to work.
    """
    order = _states(states)
    family = _family(order, relations)
    delta = relation_max_outdegree(order, family)
    cutoff = universal_exact_count_branching_modulus(delta)
    exact = _stable_report(order, family, observation, natural_semiring())
    for modulus in range(2, cutoff + 1):
        modular = _stable_report(order, family, observation, modular_semiring(modulus))
        if modular.steps == exact.steps:
            return modulus
    raise AssertionError("Delta+1 cutoff failed finite minimal-modulus search")


def worst_case_modulus_collision_fixture(
    modulus: int,
    max_outdegree: int | None = None,
) -> tuple[
    tuple[str, ...],
    dict[str, Relation],
    Callable[[str], str],
]:
    """Build a constant-observation world where mod M merges 0 and M successors.

    If ``max_outdegree`` is supplied above M, an observation-isolated source is
    added with exactly that many successors so the world's declared Delta is the
    requested larger value without disturbing the sharp x/y collision.
    """
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 1:
        raise ValueError("modulus must exceed one")
    delta = modulus if max_outdegree is None else max_outdegree
    if isinstance(delta, bool) or not isinstance(delta, int):
        raise TypeError("max_outdegree must be an integer")
    if delta < modulus:
        raise ValueError("max_outdegree must be at least the collision modulus")

    targets = tuple(f"t{index}" for index in range(delta))
    sources = ("x", "y") + (("w",) if delta > modulus else ())
    states = sources + targets
    edges = {("y", target) for target in targets[:modulus]}
    if delta > modulus:
        edges.update(("w", target) for target in targets)
    relation = frozenset(edges)

    def observation(state: str) -> str:
        if state == "w":
            return "isolated-source"
        return "visible"

    return states, {"a": relation}, observation
