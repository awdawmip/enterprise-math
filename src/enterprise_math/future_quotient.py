"""Finite future-composition quotients for Enterprise Math research.

The algorithm refines a finite observation partition until states in each class
have the same current observation and their successors under every declared
action remain in the same classes. The stable partition is the coarsest
future-safe quotient for the supplied deterministic operation language.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from typing import TypeVar


State = TypeVar("State", bound=Hashable)
Action = TypeVar("Action", bound=Hashable)
Observation = TypeVar("Observation", bound=Hashable)


def _canonical_labels(
    states: tuple[State, ...], signatures: Mapping[State, Hashable]
) -> dict[State, int]:
    ids: dict[Hashable, int] = {}
    labels: dict[State, int] = {}
    for state in states:
        signature = signatures[state]
        if signature not in ids:
            ids[signature] = len(ids)
        labels[state] = ids[signature]
    return labels


def future_partition_sequence(
    states: tuple[State, ...],
    observations: Mapping[State, Observation],
    transitions: Mapping[Action, Mapping[State, State]],
) -> tuple[tuple[int, ...], ...]:
    """Return partitions from horizon 0 through the first stable horizon.

    Each partition is represented by one integer class ID per state, in the
    supplied state order. The final returned partition is the first partition
    that is already stable under all declared one-step operations.
    """
    if not isinstance(states, tuple) or not states:
        raise ValueError("states must be a non-empty tuple")
    if len(set(states)) != len(states):
        raise ValueError("states must be unique")
    if set(observations) != set(states):
        raise ValueError("observations must be defined on exactly the state set")

    actions = tuple(transitions)
    for action in actions:
        transition = transitions[action]
        if set(transition) != set(states):
            raise ValueError("every transition must be defined on exactly the state set")
        if any(target not in observations for target in transition.values()):
            raise ValueError("transition targets must remain inside the state set")

    labels = _canonical_labels(states, observations)
    partitions = [tuple(labels[state] for state in states)]

    while True:
        signatures = {
            state: (
                labels[state],
                tuple(labels[transitions[action][state]] for action in actions),
            )
            for state in states
        }
        refined = _canonical_labels(states, signatures)
        refined_partition = tuple(refined[state] for state in states)
        if refined_partition == partitions[-1]:
            return tuple(partitions)
        partitions.append(refined_partition)
        labels = refined


def composition_horizon(
    states: tuple[State, ...],
    observations: Mapping[State, Observation],
    transitions: Mapping[Action, Mapping[State, State]],
) -> int:
    """First horizon whose future-equivalence partition is stable."""
    return len(future_partition_sequence(states, observations, transitions)) - 1


def class_count(partition: tuple[int, ...]) -> int:
    """Number of future-equivalence classes in one encoded partition."""
    if not isinstance(partition, tuple) or not partition:
        raise ValueError("partition must be a non-empty tuple")
    return len(set(partition))


def ambiguity_multiplicities(partition: tuple[int, ...]) -> tuple[int, ...]:
    """For each state position, return the size of its current equivalence class."""
    if not isinstance(partition, tuple) or not partition:
        raise ValueError("partition must be a non-empty tuple")
    counts: dict[int, int] = {}
    for label in partition:
        counts[label] = counts.get(label, 0) + 1
    return tuple(counts[label] for label in partition)
