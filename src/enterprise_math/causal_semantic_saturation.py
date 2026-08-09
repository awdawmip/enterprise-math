"""Semantic saturation of a required operation language is idempotent but not monotone.

For current observation O and required future generators G, let E_G be the
minimum exact future partition.  Define the semantic saturation

    Sat_O(G) = Safe(E_G),

the full set of raw endomaps that preserve E_G.

Every required generator lies in Sat_O(G), and re-minimizing with the full safe
envelope returns the same state E_G.  Hence saturation is extensive and
idempotent at the state/operation-pair level.

It is NOT a closure operator on operation-language inclusion: G subset H implies
E_H refines E_G, but Safe(E_G) and Safe(E_H) can be incomparable.  Refining the
state may both invalidate some formerly safe maps and make other maps newly safe.
"""

from __future__ import annotations

from itertools import product
from typing import Hashable, Mapping

from .causal_operation_language import (
    Generators,
    Partition,
    generator_respects_partition,
    minimum_future_partition,
    same_partition,
)

State = Hashable
Observation = Hashable


def enumerate_safe_endomaps(
    states: tuple[State, ...],
    partition: Partition,
) -> tuple[dict[State, State], ...]:
    """Exhaustive finite helper; intended only for small theorem oracles."""
    if set(partition) != set(states):
        raise ValueError("partition must cover the state set")
    result = []
    for outputs in product(states, repeat=len(states)):
        mapping = dict(zip(states, outputs))
        if generator_respects_partition(states, partition, mapping):
            result.append(mapping)
    return tuple(result)


def semantic_saturation_partition(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
) -> Partition:
    return minimum_future_partition(states, observation, generators)


def saturation_is_extensive(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
) -> bool:
    partition = semantic_saturation_partition(states, observation, generators)
    return all(
        generator_respects_partition(states, partition, generator)
        for generator in generators.values()
    )


def saturation_is_idempotent_on_small_system(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
) -> bool:
    """Exhaustively materialize Safe(E_G) and verify E_Safe(E_G)=E_G."""
    partition = semantic_saturation_partition(states, observation, generators)
    safe_maps = enumerate_safe_endomaps(states, partition)
    safe_generators = {
        f"safe:{index}": mapping
        for index, mapping in enumerate(safe_maps)
    }
    saturated_partition = minimum_future_partition(
        states, observation, safe_generators
    )
    return same_partition(partition, saturated_partition)


def safe_envelopes_incomparable_on_small_system(
    states: tuple[State, ...],
    left_partition: Partition,
    right_partition: Partition,
) -> tuple[bool, dict[State, State] | None, dict[State, State] | None]:
    """Return witnesses preserving only left and only right, if both exist."""
    left_only = None
    right_only = None
    for outputs in product(states, repeat=len(states)):
        mapping = dict(zip(states, outputs))
        left_safe = generator_respects_partition(states, left_partition, mapping)
        right_safe = generator_respects_partition(states, right_partition, mapping)
        if left_safe and not right_safe and left_only is None:
            left_only = mapping
        if right_safe and not left_safe and right_only is None:
            right_only = mapping
        if left_only is not None and right_only is not None:
            return True, left_only, right_only
    return False, left_only, right_only


def five_state_nonmonotone_example():
    """Return G subset H with finer E_H but incomparable full safe envelopes."""
    states = (0, 1, 2, 3, 4)
    observation = {0: 0, 1: 0, 2: 0, 3: 0, 4: 1}
    base: dict[str, dict[int, int]] = {}
    splitter = {0: 4, 1: 4, 2: 0, 3: 0, 4: 4}
    extended = {"h": splitter}
    base_partition = minimum_future_partition(states, observation, base)
    extended_partition = minimum_future_partition(states, observation, extended)
    return states, observation, base, extended, base_partition, extended_partition
