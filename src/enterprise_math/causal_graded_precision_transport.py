"""Operations transport finite future precision between graded budget layers.

Let E_R be the partition of states indistinguishable by all future words of
integer cost at most R.  A generator g of cost c need not be an endomorphism of
a single E_R layer.  Instead it canonically descends as

    g_R : X/E_(R+c) -> X/E_R.

More generally, a word w of total cost C gives X/E_(R+C) -> X/E_R.  Composition
of quotient maps follows composition of raw words with exact addition of costs.
Equivalently, the distinguishing agreement depth can fall by at most the cost of
the operation already applied.
"""

from __future__ import annotations

from typing import Hashable, Mapping

from .causal_operation_language import Generators, Partition
from .causal_weighted_future import budget_partitions, distinguishing_cost

State = Hashable
Observation = Hashable


def word_cost(word: tuple[str, ...], costs: Mapping[str, int]) -> int:
    if not isinstance(word, tuple):
        raise ValueError("word must be a tuple of generator labels")
    if any(label not in costs for label in word):
        raise ValueError("word contains undeclared generator")
    return sum(costs[label] for label in word)


def apply_word(state: State, word: tuple[str, ...], generators: Generators) -> State:
    current = state
    for label in word:
        if label not in generators:
            raise ValueError("word contains undeclared generator")
        current = generators[label][current]
    return current


def layer_map_for_word(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
    word: tuple[str, ...],
    target_budget: int,
) -> dict[int, int]:
    """Canonical X/E_(R+C) -> X/E_R class map induced by a graded word."""
    if isinstance(target_budget, bool) or not isinstance(target_budget, int) or target_budget < 0:
        raise ValueError("target_budget must be a non-negative integer")
    total_cost = word_cost(word, costs)
    partitions = budget_partitions(
        states,
        observation,
        generators,
        costs,
        target_budget + total_cost,
    )
    source = partitions[target_budget + total_cost]
    target = partitions[target_budget]
    mapping: dict[int, int] = {}
    for state in states:
        source_class = source[state]
        output_class = target[apply_word(state, word, generators)]
        previous = mapping.get(source_class)
        if previous is not None and previous != output_class:
            raise AssertionError("graded operation failed to descend between budget layers")
        mapping[source_class] = output_class
    return mapping


def compose_class_maps(
    first: Mapping[int, int],
    second: Mapping[int, int],
) -> dict[int, int]:
    """Compose `first` then `second`."""
    result = {}
    for source, middle in first.items():
        if middle not in second:
            raise ValueError("second map must define every reached intermediate class")
        result[source] = second[middle]
    return result


def word_layer_composition_is_exact(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
    first_word: tuple[str, ...],
    second_word: tuple[str, ...],
    target_budget: int,
) -> bool:
    """Check quotient map of first-then-second equals composed layer maps."""
    first_cost = word_cost(first_word, costs)
    second_cost = word_cost(second_word, costs)
    # first acts from R+C2+C1 to R+C2; second acts from R+C2 to R.
    first_map = layer_map_for_word(
        states,
        observation,
        generators,
        costs,
        first_word,
        target_budget + second_cost,
    )
    second_map = layer_map_for_word(
        states,
        observation,
        generators,
        costs,
        second_word,
        target_budget,
    )
    combined = layer_map_for_word(
        states,
        observation,
        generators,
        costs,
        first_word + second_word,
        target_budget,
    )
    return compose_class_maps(first_map, second_map) == combined


def depth_loss_bound_for_word(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
    word: tuple[str, ...],
    left: State,
    right: State,
) -> bool:
    """Verify d_sep(w x,w y) >= d_sep(x,y)-cost(w), with infinity preserved."""
    before = distinguishing_cost(
        states, observation, generators, costs, left, right
    )
    after_left = apply_word(left, word, generators)
    after_right = apply_word(right, word, generators)
    after = distinguishing_cost(
        states, observation, generators, costs, after_left, after_right
    )
    cost = word_cost(word, costs)
    if before is None:
        return after is None
    lower = max(0, before - cost)
    return after is None or after >= lower


def all_depth_loss_bounds_hold(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
    words: tuple[tuple[str, ...], ...],
) -> bool:
    return all(
        depth_loss_bound_for_word(
            states, observation, generators, costs, word, left, right
        )
        for word in words
        for left in states
        for right in states
    )


def layer_transport_property(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
    word: tuple[str, ...],
    target_budget: int,
) -> bool:
    """Direct pairwise statement E_(R+C) -> E_R for one word."""
    total_cost = word_cost(word, costs)
    partitions = budget_partitions(
        states,
        observation,
        generators,
        costs,
        target_budget + total_cost,
    )
    source = partitions[target_budget + total_cost]
    target = partitions[target_budget]
    for left in states:
        for right in states:
            if source[left] != source[right]:
                continue
            if target[apply_word(left, word, generators)] != target[
                apply_word(right, word, generators)
            ]:
                return False
    return True
