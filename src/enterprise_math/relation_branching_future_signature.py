"""Recursive branching future signatures for finite relation-valued actions.

Terminal support traces flatten every literal relation word to a union of final
observation labels.  To make a multivalued relation itself executable on the
quotient, one needs a branching-sensitive future signature that retains the set
of successor behavioural types under each action.

For observation O and labelled relations R_a define recursively

    sigma_0(x) = O(x)

and

    sigma_(h+1)(x)
      = ( O(x), ({ sigma_h(y) : x R_a y })_a ).

The empty successor set is retained exactly.  Equality of sigma_h is precisely
the h-round support-stable/bisimulation approximant from
``relation_support_stable_refinement``.

Every literal word terminal observed-support signature is a deterministic
projection of sigma_h: follow the named action in the branching signature and
union the recursively projected terminal observations over all successor
signatures.  Therefore branching precision always refines terminal trace
precision.  The projection need not be injective for multivalued relations.

For deterministic partial relations (zero or one successor per action/source),
the projection is injective at every finite horizon: the recursive branch tree
has no sibling-correlation information to lose, so legality/terminal word traces
and branching signatures induce the same partition.

Tree unfoldings, bisimulation approximants, trace semantics and modal transition
systems are standard prior mathematics/CS.  The project value is the explicit
future-language object whose kernel equals direct relation-operation precision.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Hashable, Mapping, Sequence

from .admissible_support import Relation
from .relation_future_powerset import (
    relation_family_future_partition,
    relation_word_observed_support,
    words_through_horizon,
)
from .relation_support_stable_refinement import (
    Partition,
    coarsest_relation_support_stable_refinement,
    normalize_partition,
    partition_from_observation,
    partition_refines,
)


State = Hashable
Action = Hashable
Observation = Hashable


@dataclass(frozen=True)
class BranchingFutureSignature:
    horizon: int
    observation: Observation
    successors: tuple[tuple[Action, frozenset["BranchingFutureSignature"]], ...]

    def support_for(self, action: Action) -> frozenset["BranchingFutureSignature"]:
        for name, support in self.successors:
            if name == action:
                return support
        raise ValueError("action is not represented at this branching horizon")


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


def branching_signature_map(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
) -> dict[State, BranchingFutureSignature]:
    """Return sigma_h for every state."""
    order = _states(states)
    family = _family(order, relations)
    if isinstance(horizon, bool) or not isinstance(horizon, int):
        raise TypeError("horizon must be an integer")
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    names = tuple(sorted(family, key=repr))

    current: dict[State, BranchingFutureSignature] = {}
    for state in order:
        label = observation(state)
        hash(label)
        current[state] = BranchingFutureSignature(
            horizon=0,
            observation=label,
            successors=(),
        )

    for level in range(1, horizon + 1):
        nxt: dict[State, BranchingFutureSignature] = {}
        for state in order:
            action_supports = []
            for name in names:
                relation = family[name]
                support = frozenset(
                    current[target]
                    for source, target in relation
                    if source == state
                )
                action_supports.append((name, support))
            nxt[state] = BranchingFutureSignature(
                horizon=level,
                observation=current[state].observation,
                successors=tuple(action_supports),
            )
        current = nxt
    return current


def branching_signature_partition(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
) -> Partition:
    signatures = branching_signature_map(states, relations, observation, horizon)
    groups: dict[BranchingFutureSignature, set[State]] = {}
    for state, signature in signatures.items():
        groups.setdefault(signature, set()).add(state)
    return normalize_partition(tuple(groups.values()))


def branching_partition_sequence(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
) -> tuple[Partition, ...]:
    """Return distinct sigma_h partitions through the first permanent plateau."""
    order = _states(states)
    _family(order, relations)
    initial = partition_from_observation(order, observation)
    partitions = [initial]
    horizon = 1
    while True:
        nxt = branching_signature_partition(order, relations, observation, horizon)
        if nxt == partitions[-1]:
            return tuple(partitions)
        if not partition_refines(nxt, partitions[-1]):
            raise AssertionError("branching signature partition failed to refine with horizon")
        partitions.append(nxt)
        if len(partitions) - 1 > len(order) - len(initial):
            raise AssertionError("branching approximants exceeded finite block-growth bound")
        horizon += 1


def branching_partitions_match_support_refinement(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
) -> bool:
    """Verify sigma_h kernels equal iterative relation-support refinement stages."""
    order = _states(states)
    initial = partition_from_observation(order, observation)
    stable = coarsest_relation_support_stable_refinement(initial, relations)
    branching = branching_partition_sequence(order, relations, observation)
    if branching != stable.steps:
        raise AssertionError("recursive branching signatures disagree with support refinement")
    return True


def terminal_trace_from_branching_signature(
    signature: BranchingFutureSignature,
    word: Sequence[Action],
) -> frozenset[Observation]:
    """Project one branching signature to the terminal observed support of a word."""
    actions = tuple(word)
    if len(actions) > signature.horizon:
        raise ValueError("word exceeds branching signature horizon")
    if not actions:
        return frozenset({signature.observation})
    action = actions[0]
    remainder = actions[1:]
    support = signature.support_for(action)
    result: set[Observation] = set()
    for child in support:
        result.update(terminal_trace_from_branching_signature(child, remainder))
    return frozenset(result)


def branching_signature_trace_map(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
) -> dict[State, tuple[tuple[tuple[Action, ...], frozenset[Observation]], ...]]:
    order = _states(states)
    family = _family(order, relations)
    signatures = branching_signature_map(order, family, observation, horizon)
    words = words_through_horizon(tuple(family), horizon)
    return {
        state: tuple(
            (word, terminal_trace_from_branching_signature(signature, word))
            for word in words
        )
        for state, signature in signatures.items()
    }


def branching_trace_projection_matches_raw_words(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
) -> bool:
    order = _states(states)
    family = _family(order, relations)
    traces = branching_signature_trace_map(order, family, observation, horizon)
    for state, signature in traces.items():
        for word, projected in signature:
            raw = relation_word_observed_support(
                order,
                family,
                state,
                word,
                observation,
            )
            if projected != raw:
                raise AssertionError("branching signature trace projection disagreed with raw word")
    return True


def branching_partition_refines_trace_partition(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
) -> bool:
    branching = branching_signature_partition(states, relations, observation, horizon)
    trace = normalize_partition(
        tuple(
            relation_family_future_partition(
                states,
                relations,
                observation,
                horizon,
            )
        )
    )
    if not partition_refines(branching, trace):
        raise AssertionError("branching signature failed to refine terminal support trace")
    return True


def relation_family_is_deterministic_partial(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
) -> bool:
    order = _states(states)
    family = _family(order, relations)
    for relation in family.values():
        counts = {state: 0 for state in order}
        for source, _target in relation:
            counts[source] += 1
            if counts[source] > 1:
                return False
    return True


def deterministic_partial_branching_equals_trace(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
) -> bool:
    if not relation_family_is_deterministic_partial(states, relations):
        raise ValueError("relation family must have at most one successor per source/action")
    branching = branching_signature_partition(states, relations, observation, horizon)
    trace = normalize_partition(
        tuple(
            relation_family_future_partition(
                states,
                relations,
                observation,
                horizon,
            )
        )
    )
    if branching != trace:
        raise AssertionError("deterministic-partial branching and trace partitions diverged")
    return True
