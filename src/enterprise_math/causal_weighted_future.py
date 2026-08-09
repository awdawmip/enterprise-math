"""Integer-graded causal operations generate both transport and precision depth.

Each primitive unary generator g has a positive integer cost c(g).  The same
primitive layer induces two different exact integer geometries:

1. transport cost: minimum word cost sending x to y;
2. distinguishing cost: minimum word cost after which the declared observation
   separates x and y.

They are not identified.  A finite budget R induces the future-equivalence
partition `x ~_R y` iff no operation word of total cost <=R distinguishes them.
The eventual infinite-budget partition depends only on the generated operation
monoid, not on the particular positive costs; costs determine when distinctions
become visible, not which distinctions are ultimately visible.
"""

from __future__ import annotations

import heapq
from itertools import count
from typing import Hashable, Mapping

from .causal_operation_language import (
    Generators,
    Partition,
    minimum_future_partition,
    same_partition,
)

State = Hashable
Observation = Hashable


def _validate(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
) -> None:
    if not states or len(set(states)) != len(states):
        raise ValueError("states must be a non-empty tuple of unique states")
    if set(observation) != set(states):
        raise ValueError("observation must define every state")
    if set(costs) != set(generators):
        raise ValueError("costs must define every generator exactly once")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in costs.values()
    ):
        raise ValueError("generator costs must be positive integers")
    state_set = set(states)
    for generator in generators.values():
        if set(generator) != state_set or not set(generator.values()) <= state_set:
            raise ValueError("every generator must be a total endomap of the state set")


def _canonical_partition(states: tuple[State, ...], signatures) -> Partition:
    ids = {}
    result = {}
    for state in states:
        signature = signatures[state]
        if signature not in ids:
            ids[signature] = len(ids)
        result[state] = ids[signature]
    return result


def budget_partitions(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
    maximum_budget: int,
) -> tuple[Partition, ...]:
    """Return exact partitions for every integer budget 0..maximum_budget."""
    _validate(states, observation, generators, costs)
    if isinstance(maximum_budget, bool) or not isinstance(maximum_budget, int) or maximum_budget < 0:
        raise ValueError("maximum_budget must be a non-negative integer")
    partitions = [_canonical_partition(states, observation)]
    labels = tuple(sorted(generators))
    for budget in range(1, maximum_budget + 1):
        previous = partitions[budget - 1]
        signatures = {}
        for state in states:
            future = []
            for label in labels:
                cost = costs[label]
                if cost <= budget:
                    future.append(
                        (label, partitions[budget - cost][generators[label][state]])
                    )
            signatures[state] = (
                observation[state],
                previous[state],
                tuple(future),
            )
        partitions.append(_canonical_partition(states, signatures))
    return tuple(partitions)


def transport_cost(
    states: tuple[State, ...],
    generators: Generators,
    costs: Mapping[str, int],
    source: State,
    target: State,
) -> int | None:
    """Minimum graded operation cost sending source to target; None if unreachable."""
    observation = {state: 0 for state in states}
    _validate(states, observation, generators, costs)
    if source not in observation or target not in observation:
        raise ValueError("source and target must belong to state set")
    serial = count()
    queue = [(0, next(serial), source)]
    best = {source: 0}
    labels = tuple(sorted(generators))
    while queue:
        distance, _, state = heapq.heappop(queue)
        if distance != best[state]:
            continue
        if state == target:
            return distance
        for label in labels:
            nxt = generators[label][state]
            candidate = distance + costs[label]
            if candidate >= best.get(nxt, candidate + 1):
                continue
            best[nxt] = candidate
            heapq.heappush(queue, (candidate, next(serial), nxt))
    return None


def distinguishing_cost(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
    left: State,
    right: State,
) -> int | None:
    """Minimum future cost that gives different observations; None if never distinguishable."""
    _validate(states, observation, generators, costs)
    if left not in observation or right not in observation:
        raise ValueError("states must belong to state set")
    serial = count()
    start = (left, right)
    queue = [(0, next(serial), start)]
    best = {start: 0}
    labels = tuple(sorted(generators))
    while queue:
        distance, _, pair = heapq.heappop(queue)
        if distance != best[pair]:
            continue
        if observation[pair[0]] != observation[pair[1]]:
            return distance
        for label in labels:
            generator = generators[label]
            nxt = (generator[pair[0]], generator[pair[1]])
            candidate = distance + costs[label]
            if candidate >= best.get(nxt, candidate + 1):
                continue
            best[nxt] = candidate
            heapq.heappush(queue, (candidate, next(serial), nxt))
    return None


def budget_partition_matches_distinguishing_costs(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
    budget: int,
) -> bool:
    partition = budget_partitions(
        states, observation, generators, costs, budget
    )[budget]
    for left in states:
        for right in states:
            distance = distinguishing_cost(
                states, observation, generators, costs, left, right
            )
            equivalent = distance is None or distance > budget
            if equivalent != (partition[left] == partition[right]):
                return False
    return True


def eventual_partition_matches_unweighted_future(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
) -> bool:
    """Positive integer grades change revelation depth but not ultimate quotient."""
    distances = []
    for left in states:
        for right in states:
            distance = distinguishing_cost(
                states, observation, generators, costs, left, right
            )
            if distance is not None:
                distances.append(distance)
    budget = max(distances, default=0)
    weighted = budget_partitions(
        states, observation, generators, costs, budget
    )[budget]
    unweighted = minimum_future_partition(states, observation, generators)
    return same_partition(weighted, unweighted)


def distinguishing_cost_strong_triangle(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
) -> bool:
    """Check d(x,z)>=min(d(x,y),d(y,z)), treating None as infinity."""
    distances = {
        (left, right): distinguishing_cost(
            states, observation, generators, costs, left, right
        )
        for left in states
        for right in states
    }
    for x in states:
        for y in states:
            for z in states:
                xy = distances[(x, y)]
                yz = distances[(y, z)]
                xz = distances[(x, z)]
                if xy is None and yz is None:
                    if xz is not None:
                        return False
                    continue
                threshold = yz if xy is None else xy if yz is None else min(xy, yz)
                if xz is not None and xz < threshold:
                    return False
    return True
