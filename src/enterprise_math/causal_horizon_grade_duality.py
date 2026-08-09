"""Weighted future horizon equals a maximal semantic loss grade of generated words.

For each pair with finite distinguishing depth D(x,y), Dijkstra can return a
minimum-cost operation word w separating the pair.  Such a shortest witness is
semantic-grade tight: ell(w)=cost(w)=D(x,y).  In particular, for a hardest pair
with depth H, its shortest witness has semantic grade H.  Since no operation can
lose more agreement depth than the maximum finite depth H, the weighted
composition horizon equals the maximum semantic loss grade attained by the
generated operation monoid.
"""

from __future__ import annotations

import heapq
from itertools import count
from typing import Hashable, Mapping

from .causal_operation_language import Generators
from .causal_semantic_grade import (
    distinguishing_depth_matrix,
    semantic_loss_grade,
)
from .causal_weighted_horizon import weighted_composition_horizon

State = Hashable
Observation = Hashable


def shortest_distinguishing_word(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
    left: State,
    right: State,
) -> tuple[int, tuple[str, ...]] | None:
    if set(costs) != set(generators) or any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in costs.values()
    ):
        raise ValueError("costs must be positive integers for every generator")
    serial = count()
    start = (left, right)
    queue = [(0, next(serial), start, ())]
    best = {start: 0}
    labels = tuple(sorted(generators))
    while queue:
        distance, _, pair, word = heapq.heappop(queue)
        if distance != best[pair]:
            continue
        if observation[pair[0]] != observation[pair[1]]:
            return distance, word
        for label in labels:
            generator = generators[label]
            nxt = (generator[pair[0]], generator[pair[1]])
            candidate = distance + costs[label]
            if candidate >= best.get(nxt, candidate + 1):
                continue
            best[nxt] = candidate
            heapq.heappush(
                queue,
                (candidate, next(serial), nxt, word + (label,)),
            )
    return None


def word_operation(
    states: tuple[State, ...],
    generators: Generators,
    word: tuple[str, ...],
) -> dict[State, State]:
    result = {}
    for state in states:
        current = state
        for label in word:
            current = generators[label][current]
        result[state] = current
    return result


def word_declared_cost(word: tuple[str, ...], costs: Mapping[str, int]) -> int:
    return sum(costs[label] for label in word)


def shortest_witness_is_semantic_grade_tight(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
    left: State,
    right: State,
) -> bool:
    witness = shortest_distinguishing_word(
        states, observation, generators, costs, left, right
    )
    if witness is None:
        return True
    distance, word = witness
    depth = distinguishing_depth_matrix(
        states, observation, generators, costs
    )
    operation = word_operation(states, generators, word)
    grade = semantic_loss_grade(states, depth, operation)
    return distance == word_declared_cost(word, costs) == grade


def horizon_semantic_grade_witness(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
) -> tuple[State, State, tuple[str, ...], int] | None:
    horizon = weighted_composition_horizon(
        states, observation, generators, costs
    )
    if horizon == 0:
        return None
    depth = distinguishing_depth_matrix(
        states, observation, generators, costs
    )
    for left in states:
        for right in states:
            if depth[(left, right)] != horizon:
                continue
            witness = shortest_distinguishing_word(
                states, observation, generators, costs, left, right
            )
            if witness is None:
                continue
            distance, word = witness
            operation = word_operation(states, generators, word)
            grade = semantic_loss_grade(states, depth, operation)
            if distance == horizon and grade == horizon:
                return left, right, word, horizon
    raise AssertionError("positive weighted horizon must have a grade-tight witness word")
