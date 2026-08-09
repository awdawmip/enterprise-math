"""Contextual continuation types for recursive LEGO composition.

A continuation type that is sufficient only for ordinary future actions may
still be too coarse for arbitrary-dimensional composition.  If binary LEGO
composition itself is an allowed future operation, the type must also be stable
under joining with every allowed partner on the left/right.

For a finite deterministic raw composition table, this module turns every
left/right partner context into a named causal action and reuses the finite
future-refinement engine.  The stable classes are therefore the coarsest
observation-preserving classes stable under all declared composition contexts.
When the raw composition is associative, the induced operation on these classes
is well-defined and associative.  Traditional quotient-monoid language is only
a shadow of this causal contextual refinement.
"""

from __future__ import annotations

from typing import Hashable

from .causal_continuation_refinement import stable_continuation_types

State = Hashable
Observation = Hashable
Composition = dict[tuple[State, State], State]


def _validate_composition(states: tuple[State, ...], composition: Composition) -> None:
    if not isinstance(states, tuple) or not states or len(set(states)) != len(states):
        raise ValueError("states must be a non-empty tuple of unique labels")
    expected = {(left, right) for left in states for right in states}
    if set(composition) != expected:
        raise ValueError("composition must define every ordered state pair")
    if not set(composition.values()) <= set(states):
        raise ValueError("composition outputs must be declared states")


def composition_is_associative(
    states: tuple[State, ...],
    composition: Composition,
) -> bool:
    _validate_composition(states, composition)
    for first in states:
        for second in states:
            for third in states:
                left = composition[(composition[(first, second)], third)]
                right = composition[(first, composition[(second, third)])]
                if left != right:
                    return False
    return True


def composition_context_actions(
    states: tuple[State, ...],
    composition: Composition,
) -> dict[tuple[str, State], dict[State, State]]:
    """All one-step left/right join contexts as deterministic causal actions."""
    _validate_composition(states, composition)
    actions: dict[tuple[str, State], dict[State, State]] = {}
    for partner in states:
        actions[("L", partner)] = {
            state: composition[(partner, state)]
            for state in states
        }
        actions[("R", partner)] = {
            state: composition[(state, partner)]
            for state in states
        }
    return actions


def stable_contextual_types(
    states: tuple[State, ...],
    observations: dict[State, Observation],
    composition: Composition,
) -> tuple[dict[State, int], int]:
    """Coarsest finite classes preserving all future composition contexts."""
    _validate_composition(states, composition)
    if set(observations) != set(states):
        raise ValueError("observations must define every state exactly once")
    actions = composition_context_actions(states, composition)
    return stable_continuation_types(observations, actions)


def induced_type_composition(
    states: tuple[State, ...],
    composition: Composition,
    classes: dict[State, int],
) -> dict[tuple[int, int], int]:
    """Induced binary law on a composition-compatible state partition.

    Raises if the supplied classes are not a congruence for composition.
    """
    _validate_composition(states, composition)
    if set(classes) != set(states):
        raise ValueError("classes must define every state")
    class_ids = tuple(sorted(set(classes.values())))
    result: dict[tuple[int, int], int] = {}
    for left_class in class_ids:
        left_states = [state for state in states if classes[state] == left_class]
        for right_class in class_ids:
            right_states = [state for state in states if classes[state] == right_class]
            outputs = {
                classes[composition[(left, right)]]
                for left in left_states
                for right in right_states
            }
            if len(outputs) != 1:
                raise ValueError("state partition is not composition-compatible")
            result[(left_class, right_class)] = next(iter(outputs))
    return result


def type_composition_is_associative(
    type_operation: dict[tuple[int, int], int],
) -> bool:
    types = tuple(sorted({value for pair in type_operation for value in pair} | set(type_operation.values())))
    expected = {(left, right) for left in types for right in types}
    if set(type_operation) != expected:
        raise ValueError("type operation must define every ordered type pair")
    for first in types:
        for second in types:
            for third in types:
                if type_operation[(type_operation[(first, second)], third)] != type_operation[
                    (first, type_operation[(second, third)])
                ]:
                    return False
    return True


def compile_contextual_type_operation(
    states: tuple[State, ...],
    observations: dict[State, Observation],
    composition: Composition,
) -> tuple[dict[State, int], dict[tuple[int, int], int], int]:
    """Return `(raw_state_to_type, induced_type_join, refinement_rounds)`.

    If the raw composition is associative, the resulting type join is also
    associative.  The types are generated by future contextual
    indistinguishability rather than declared in advance.
    """
    classes, rounds = stable_contextual_types(states, observations, composition)
    induced = induced_type_composition(states, composition, classes)
    if composition_is_associative(states, composition) and not type_composition_is_associative(induced):
        raise AssertionError("contextual quotient of an associative composition lost associativity")
    return classes, induced, rounds
