"""Finite continuation-signature refinement for causal witnesses.

This is the finite deterministic specialization of future-safe quotienting.  It
takes explicit current observations and named causal actions, then repeatedly
refines witness classes by their current observation and the classes reached by
all one-step actions.  The stable partition is exactly the coarsest partition
that preserves every finite future observation word.

The result supplies the continuation-type labels used by
`causal_continuation_kernel.py` without keeping raw witness identity in the
runtime state.
"""

from __future__ import annotations

from typing import Hashable

State = Hashable
Action = Hashable
Observation = Hashable


def _canonical_classes(signatures: dict[State, Hashable]) -> dict[State, int]:
    """Assign deterministic integer class ids by first appearance in sorted repr order."""
    states = sorted(signatures, key=repr)
    ids: dict[Hashable, int] = {}
    result: dict[State, int] = {}
    for state in states:
        signature = signatures[state]
        if signature not in ids:
            ids[signature] = len(ids)
        result[state] = ids[signature]
    return result


def initial_observation_partition(
    observations: dict[State, Observation],
) -> dict[State, int]:
    if not isinstance(observations, dict) or not observations:
        raise ValueError("observations must be a non-empty dict")
    return _canonical_classes(observations)


def refine_once(
    observations: dict[State, Observation],
    actions: dict[Action, dict[State, State]],
    classes: dict[State, int],
) -> dict[State, int]:
    """Refine by current observation plus every named action's target class."""
    states = set(observations)
    if set(classes) != states:
        raise ValueError("classes must cover exactly the observed states")
    if not isinstance(actions, dict):
        raise ValueError("actions must be a dict")
    ordered_actions = tuple(sorted(actions, key=repr))
    for action in ordered_actions:
        transition = actions[action]
        if set(transition) != states or not set(transition.values()) <= states:
            raise ValueError("every action must be a total transition on the state set")
    signatures = {
        state: (
            observations[state],
            tuple(classes[actions[action][state]] for action in ordered_actions),
        )
        for state in states
    }
    return _canonical_classes(signatures)


def stable_continuation_types(
    observations: dict[State, Observation],
    actions: dict[Action, dict[State, State]],
) -> tuple[dict[State, int], int]:
    """Return `(stable_classes, refinement_rounds)`.

    Equality of final class ids is equality of complete finite-future signatures
    for the declared deterministic action/observation language.
    """
    classes = initial_observation_partition(observations)
    rounds = 0
    while True:
        refined = refine_once(observations, actions, classes)
        rounds += 1
        # Compare equivalence relations rather than raw numeric ids.
        states = tuple(observations)
        same_partition = all(
            (classes[a] == classes[b]) == (refined[a] == refined[b])
            for a in states
            for b in states
        )
        if same_partition:
            return refined, rounds
        classes = refined
        if rounds > len(states):
            raise AssertionError("finite refinement failed to stabilize")


def class_count(classes: dict[State, int]) -> int:
    if not isinstance(classes, dict) or not classes:
        raise ValueError("classes must be a non-empty dict")
    return len(set(classes.values()))


def future_equivalent(
    left: State,
    right: State,
    observations: dict[State, Observation],
    actions: dict[Action, dict[State, State]],
) -> bool:
    classes, _ = stable_continuation_types(observations, actions)
    if left not in classes or right not in classes:
        raise ValueError("states must belong to the declared system")
    return classes[left] == classes[right]
