"""Minimal future-safe state for deterministic weighted one-slot growth.

A raw continuation state receives a named append/action.  Each action produces a
next raw state and an integer grade increment.  A quotient is exact only when
states in the same class have the same current observation and, for every
action, the same grade increment and same next quotient class.

Iterating this signature refinement from the current-observation partition
produces the coarsest future-safe weighted state partition.  This is the unary
append/growth analogue of `causal_weighted_context_refinement.py`.
"""

from __future__ import annotations

from typing import Hashable

State = Hashable
Action = Hashable
Observation = Hashable
WeightedTransition = dict[Action, dict[State, tuple[State, int]]]


def _canonical_classes(signatures: dict[State, Hashable]) -> dict[State, int]:
    ids: dict[Hashable, int] = {}
    result: dict[State, int] = {}
    for state in sorted(signatures, key=repr):
        signature = signatures[state]
        if signature not in ids:
            ids[signature] = len(ids)
        result[state] = ids[signature]
    return result


def _validate(
    observations: dict[State, Observation],
    transitions: WeightedTransition,
) -> tuple[State, ...]:
    if not isinstance(observations, dict) or not observations:
        raise ValueError("observations must be a non-empty dict")
    if not isinstance(transitions, dict):
        raise ValueError("transitions must be a dict")
    states = tuple(observations)
    state_set = set(states)
    for action, table in transitions.items():
        try:
            hash(action)
        except TypeError as error:
            raise ValueError("actions must be hashable") from error
        if set(table) != state_set:
            raise ValueError("every action must define every raw state")
        for next_state, grade in table.values():
            if next_state not in state_set:
                raise ValueError("transition target must be a declared raw state")
            if isinstance(grade, bool) or not isinstance(grade, int):
                raise ValueError("grade increments must be integers")
    return states


def refine_weighted_transition_once(
    observations: dict[State, Observation],
    transitions: WeightedTransition,
    classes: dict[State, int],
) -> dict[State, int]:
    states = _validate(observations, transitions)
    if set(classes) != set(states):
        raise ValueError("classes must define every raw state")
    actions = tuple(sorted(transitions, key=repr))
    signatures = {
        state: (
            observations[state],
            tuple(
                (
                    grade,
                    classes[next_state],
                )
                for action in actions
                for next_state, grade in (transitions[action][state],)
            ),
        )
        for state in states
    }
    return _canonical_classes(signatures)


def stable_weighted_transition_types(
    observations: dict[State, Observation],
    transitions: WeightedTransition,
) -> tuple[dict[State, int], int]:
    """Return coarsest current-observation refinement exact for every future action word."""
    states = _validate(observations, transitions)
    classes = _canonical_classes(observations)
    rounds = 0
    while True:
        refined = refine_weighted_transition_once(observations, transitions, classes)
        rounds += 1
        same = all(
            (classes[left] == classes[right]) == (refined[left] == refined[right])
            for left in states
            for right in states
        )
        if same:
            return refined, rounds
        classes = refined
        if rounds > len(states):
            raise AssertionError("finite weighted transition refinement failed to stabilize")


def induced_weighted_transitions(
    observations: dict[State, Observation],
    transitions: WeightedTransition,
    classes: dict[State, int],
) -> dict[Action, dict[int, tuple[int, int]]]:
    """Induce exact action transitions on a weighted future-safe partition."""
    states = _validate(observations, transitions)
    if set(classes) != set(states):
        raise ValueError("classes must define every raw state")
    class_ids = tuple(sorted(set(classes.values())))
    result: dict[Action, dict[int, tuple[int, int]]] = {}
    for action, table in transitions.items():
        induced_action: dict[int, tuple[int, int]] = {}
        for class_id in class_ids:
            representatives = [state for state in states if classes[state] == class_id]
            outcomes = {
                (classes[table[state][0]], table[state][1])
                for state in representatives
            }
            if len(outcomes) != 1:
                raise ValueError("partition is not future-safe for weighted transition")
            induced_action[class_id] = next(iter(outcomes))
        result[action] = induced_action
    return result


def compile_weighted_transition_system(
    observations: dict[State, Observation],
    transitions: WeightedTransition,
) -> tuple[dict[State, int], dict[Action, dict[int, tuple[int, int]]], int]:
    classes, rounds = stable_weighted_transition_types(observations, transitions)
    induced = induced_weighted_transitions(observations, transitions, classes)
    return classes, induced, rounds
