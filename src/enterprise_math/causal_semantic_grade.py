"""Canonical semantic operation grades derived from future distinguishability depth.

Start from a finite causal language with positive declared generator costs and
let D(x,y) be its exact distinguishing cost (infinity if never distinguishable).
For any endomap f preserving ultimate future-equivalence define

    loss(f)=max_[D(x,y)<infinity] max(0, D(x,y)-D(fx,fy)),

where an infinite image depth contributes zero loss.  This is exactly the minimum
integer C such that f descends X/E_(R+C)->X/E_R for every R.

For every primitive generator g, loss(g)<=declared_cost(g).  Regrading each
generator by its semantic loss grade, allowing zero, reproduces the entire pair
D matrix exactly.  Moreover any nonnegative generator-grade assignment that
reproduces the same D matrix must be componentwise at least these loss grades.
Thus the loss grades are the unique componentwise-minimal semantic regrading.

This is a semantic precision grade, not a claim about physical energy, time, or
spatial length.
"""

from __future__ import annotations

import heapq
from itertools import count
from typing import Hashable, Mapping

from .causal_operation_language import Generators
from .causal_weighted_future import distinguishing_cost

State = Hashable
Observation = Hashable
Depth = int | None  # None means infinity / never distinguishable.


def distinguishing_depth_matrix(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
) -> dict[tuple[State, State], Depth]:
    return {
        (left, right): distinguishing_cost(
            states, observation, generators, costs, left, right
        )
        for left in states
        for right in states
    }


def operation_preserves_ultimate_equivalence(
    states: tuple[State, ...],
    depth: Mapping[tuple[State, State], Depth],
    operation: Mapping[State, State],
) -> bool:
    return all(
        depth[(left, right)] is not None
        or depth[(operation[left], operation[right])] is None
        for left in states
        for right in states
    )


def semantic_loss_grade(
    states: tuple[State, ...],
    depth: Mapping[tuple[State, State], Depth],
    operation: Mapping[State, State],
) -> int:
    if set(operation) != set(states) or not set(operation.values()) <= set(states):
        raise ValueError("operation must be a total endomap of the state set")
    if not operation_preserves_ultimate_equivalence(states, depth, operation):
        raise ValueError("operation breaks ultimate future-equivalence and has no finite semantic grade")
    maximum = 0
    for left in states:
        for right in states:
            before = depth[(left, right)]
            if before is None:
                continue
            after = depth[(operation[left], operation[right])]
            if after is None:
                continue
            maximum = max(maximum, before - after)
    return max(0, maximum)


def semantic_loss_witness(
    states: tuple[State, ...],
    depth: Mapping[tuple[State, State], Depth],
    operation: Mapping[State, State],
) -> tuple[State, State, int, int | None] | None:
    grade = semantic_loss_grade(states, depth, operation)
    if grade == 0:
        return None
    for left in states:
        for right in states:
            before = depth[(left, right)]
            after = depth[(operation[left], operation[right])]
            if before is None or after is None:
                continue
            if before - after == grade:
                return left, right, before, after
    raise AssertionError("positive semantic grade must have a finite witness pair")


def generator_semantic_grades(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    declared_costs: Mapping[str, int],
) -> dict[str, int]:
    depth = distinguishing_depth_matrix(
        states, observation, generators, declared_costs
    )
    return {
        label: semantic_loss_grade(states, depth, generator)
        for label, generator in generators.items()
    }


def declared_costs_dominate_semantic_grades(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    declared_costs: Mapping[str, int],
) -> bool:
    semantic = generator_semantic_grades(
        states, observation, generators, declared_costs
    )
    return all(declared_costs[label] >= semantic[label] for label in generators)


def distinguishing_cost_nonnegative(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
    left: State,
    right: State,
) -> Depth:
    """Dijkstra variant allowing semantic zero-cost generators."""
    if set(costs) != set(generators):
        raise ValueError("costs must define every generator")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in costs.values()
    ):
        raise ValueError("semantic costs must be non-negative integers")
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


def semantic_regrading_preserves_depth_matrix(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    declared_costs: Mapping[str, int],
) -> bool:
    original = distinguishing_depth_matrix(
        states, observation, generators, declared_costs
    )
    semantic = {
        label: semantic_loss_grade(states, original, generator)
        for label, generator in generators.items()
    }
    for left in states:
        for right in states:
            regraded = distinguishing_cost_nonnegative(
                states,
                observation,
                generators,
                semantic,
                left,
                right,
            )
            if regraded != original[(left, right)]:
                return False
    return True


def semantic_grade_is_componentwise_necessary(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    declared_costs: Mapping[str, int],
    candidate_costs: Mapping[str, int],
) -> bool:
    """If candidate reproduces D, it must dominate every semantic loss grade.

    Returns False if the candidate does not reproduce D; otherwise verifies the
    componentwise lower bound.
    """
    if set(candidate_costs) != set(generators) or any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in candidate_costs.values()
    ):
        raise ValueError("candidate costs must be non-negative integers on all generators")
    original = distinguishing_depth_matrix(
        states, observation, generators, declared_costs
    )
    for left in states:
        for right in states:
            if distinguishing_cost_nonnegative(
                states,
                observation,
                generators,
                candidate_costs,
                left,
                right,
            ) != original[(left, right)]:
                return False
    semantic = {
        label: semantic_loss_grade(states, original, generator)
        for label, generator in generators.items()
    }
    return all(candidate_costs[label] >= semantic[label] for label in generators)


def semantic_grade_subadditivity(
    states: tuple[State, ...],
    depth: Mapping[tuple[State, State], Depth],
    first: Mapping[State, State],
    second: Mapping[State, State],
) -> bool:
    """loss(second∘first) <= loss(first)+loss(second)."""
    composed = {state: second[first[state]] for state in states}
    return semantic_loss_grade(states, depth, composed) <= (
        semantic_loss_grade(states, depth, first)
        + semantic_loss_grade(states, depth, second)
    )
