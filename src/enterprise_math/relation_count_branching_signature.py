"""Count-sensitive branching future signatures for finite relations.

The support branching signature stores, for each action, the **set** of successor
behavioural types.  If the future language can observe branch multiplicity, the
correct successor aggregator is instead a finite counting measure / multiset.

For a raw relation R_a (a set of source-target pairs), define recursively

    mu_0(x) = O(x)

and

    mu_(h+1)(x)
      = ( O(x), ( Counter(mu_h(y) for x R_a y) )_a ).

Thus targets with the same h-behavioural type contribute an integer multiplicity.
The equality kernel is the finite count-stable/equitable refinement: equivalent
sources must have the same number of successors in every current behavioural
class for every action.

There is a canonical coefficient erasure

    N -> B,  n |-> [n>0],

implemented recursively by dropping multiplicities and retaining only the set
of erased successor types.  This maps count branching signatures to the support
branching signatures of the parent generation.  Hence count precision always
refines support precision and can be strictly finer.

Terminal natural path-count traces are another projection.  Follow a word
through the count signature and sum child terminal counts weighted by successor
multiplicity.  This forgets how the contributing count behaviours are grouped
among individual successor types, so count branching can also be strictly finer
than terminal path-count trace semantics.

Weighted bisimulation/equitable partitions, multisets, path counts and the
N->Boolean support quotient are standard prior mathematics/CS.  The project
value is the explicit branching-operation precision layer between support and
full witness provenance.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Callable, Hashable, Mapping, Sequence

from .admissible_support import Relation
from .relation_branching_future_signature import (
    BranchingFutureSignature,
    branching_signature_map,
)
from .relation_support_stable_refinement import (
    Partition,
    normalize_partition,
    partition_from_observation,
    partition_refines,
)


State = Hashable
Action = Hashable
Observation = Hashable


@dataclass(frozen=True)
class CountBranchingFutureSignature:
    horizon: int
    observation: Observation
    successors: tuple[
        tuple[Action, frozenset[tuple["CountBranchingFutureSignature", int]]],
        ...,
    ]

    def counts_for(
        self,
        action: Action,
    ) -> frozenset[tuple["CountBranchingFutureSignature", int]]:
        for name, counts in self.successors:
            if name == action:
                return counts
        raise ValueError("action is not represented at this count-branching horizon")


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


def count_branching_signature_map(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
) -> dict[State, CountBranchingFutureSignature]:
    order = _states(states)
    family = _family(order, relations)
    if isinstance(horizon, bool) or not isinstance(horizon, int):
        raise TypeError("horizon must be an integer")
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    names = tuple(sorted(family, key=repr))

    current: dict[State, CountBranchingFutureSignature] = {}
    for state in order:
        label = observation(state)
        hash(label)
        current[state] = CountBranchingFutureSignature(
            horizon=0,
            observation=label,
            successors=(),
        )

    for level in range(1, horizon + 1):
        nxt: dict[State, CountBranchingFutureSignature] = {}
        for state in order:
            action_counts = []
            for name in names:
                relation = family[name]
                counter = Counter(
                    current[target]
                    for source, target in relation
                    if source == state
                )
                action_counts.append(
                    (
                        name,
                        frozenset((signature, count) for signature, count in counter.items()),
                    )
                )
            nxt[state] = CountBranchingFutureSignature(
                horizon=level,
                observation=current[state].observation,
                successors=tuple(action_counts),
            )
        current = nxt
    return current


def count_branching_signature_partition(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
) -> Partition:
    signatures = count_branching_signature_map(states, relations, observation, horizon)
    groups: dict[CountBranchingFutureSignature, set[State]] = {}
    for state, signature in signatures.items():
        groups.setdefault(signature, set()).add(state)
    return normalize_partition(tuple(groups.values()))


def count_branching_partition_sequence(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
) -> tuple[Partition, ...]:
    order = _states(states)
    _family(order, relations)
    initial = partition_from_observation(order, observation)
    result = [initial]
    horizon = 1
    while True:
        nxt = count_branching_signature_partition(order, relations, observation, horizon)
        if nxt == result[-1]:
            return tuple(result)
        if not partition_refines(nxt, result[-1]):
            raise AssertionError("count branching partition failed to refine with horizon")
        result.append(nxt)
        if len(result) - 1 > len(order) - len(initial):
            raise AssertionError("count branching exceeded finite block-growth bound")
        horizon += 1


def erase_count_signature_to_support(
    signature: CountBranchingFutureSignature,
) -> BranchingFutureSignature:
    if signature.horizon == 0:
        return BranchingFutureSignature(
            horizon=0,
            observation=signature.observation,
            successors=(),
        )
    action_supports = []
    for action, counts in signature.successors:
        support = frozenset(
            erase_count_signature_to_support(child)
            for child, count in counts
            if count > 0
        )
        action_supports.append((action, support))
    return BranchingFutureSignature(
        horizon=signature.horizon,
        observation=signature.observation,
        successors=tuple(action_supports),
    )


def count_erasure_matches_support_signature(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
) -> bool:
    order = _states(states)
    counts = count_branching_signature_map(order, relations, observation, horizon)
    support = branching_signature_map(order, relations, observation, horizon)
    for state in order:
        if erase_count_signature_to_support(counts[state]) != support[state]:
            raise AssertionError("N->Boolean branching erasure disagreed with support signature")
    return True


def count_branching_refines_support_partition(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
) -> bool:
    count_partition = count_branching_signature_partition(
        states,
        relations,
        observation,
        horizon,
    )
    support_map = branching_signature_map(states, relations, observation, horizon)
    groups: dict[BranchingFutureSignature, set[State]] = {}
    for state, signature in support_map.items():
        groups.setdefault(signature, set()).add(state)
    support_partition = normalize_partition(tuple(groups.values()))
    if not partition_refines(count_partition, support_partition):
        raise AssertionError("count branching failed to refine support branching")
    return True


def terminal_count_trace_from_signature(
    signature: CountBranchingFutureSignature,
    word: Sequence[Action],
) -> dict[Observation, int]:
    """Project one count branching signature to natural terminal path counts."""
    actions = tuple(word)
    if len(actions) > signature.horizon:
        raise ValueError("word exceeds count branching signature horizon")
    if not actions:
        return {signature.observation: 1}
    action = actions[0]
    remainder = actions[1:]
    result: dict[Observation, int] = {}
    for child, multiplicity in signature.counts_for(action):
        if multiplicity <= 0:
            raise AssertionError("count signature stored a nonpositive multiplicity")
        child_counts = terminal_count_trace_from_signature(child, remainder)
        for observation, count in child_counts.items():
            result[observation] = result.get(observation, 0) + multiplicity * count
    return result


def count_branching_terminal_trace_signature(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    source: State,
    horizon: int,
    words: Sequence[Sequence[Action]],
) -> tuple[tuple[tuple[Action, ...], frozenset[tuple[Observation, int]]], ...]:
    order = _states(states)
    if source not in order:
        raise ValueError("source lies outside declared state set")
    signature = count_branching_signature_map(
        order,
        relations,
        observation,
        horizon,
    )[source]
    result = []
    for word in words:
        literal = tuple(word)
        counts = terminal_count_trace_from_signature(signature, literal)
        result.append((literal, frozenset(counts.items())))
    return tuple(result)
