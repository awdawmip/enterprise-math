"""Exact cost of extending a causal future-operation language.

Given a current minimum future partition P_G, a new generator family H is
zero-cost exactly when every h in H already respects P_G.  Otherwise the joint
future language G∪H forces the state to refine.

Two separately minimized languages can also have a dynamic coupling defect: the
joint quotient may be strictly finer than the static common refinement P_G∧P_H
because mixed words are newly legal.  This module constructs a shortest mixed
word witness on finite state spaces.
"""

from __future__ import annotations

from collections import deque
from itertools import combinations
from typing import Hashable, Mapping

from .causal_operation_language import (
    Generators,
    Partition,
    class_count,
    common_refinement,
    minimum_future_partition,
    operation_language_is_safe,
    partition_collision_spectrum,
    partition_refines,
    same_partition,
)

State = Hashable
Observation = Hashable


def _union_generators(left: Generators, right: Generators) -> dict[str, Mapping[State, State]]:
    overlap = set(left) & set(right)
    if overlap:
        raise ValueError("generator labels must be disjoint")
    result = dict(left)
    result.update(right)
    return result


def extension_is_zero_cost(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    base_generators: Generators,
    added_generators: Generators,
) -> bool:
    """Whether added operations already descend through the minimum base state."""
    base = minimum_future_partition(states, observation, base_generators)
    return operation_language_is_safe(states, base, added_generators)


def extension_partition(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    base_generators: Generators,
    added_generators: Generators,
) -> Partition:
    return minimum_future_partition(
        states,
        observation,
        _union_generators(base_generators, added_generators),
    )


def extension_defect(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    base_generators: Generators,
    added_generators: Generators,
    maximum_order: int | None = None,
) -> tuple[int, tuple[int, ...]]:
    """State classes added and P011 collisions lost when future language grows."""
    base = minimum_future_partition(states, observation, base_generators)
    extended = extension_partition(states, observation, base_generators, added_generators)
    if not partition_refines(extended, base):
        raise AssertionError("adding future generators must refine the minimum state")
    before = partition_collision_spectrum(states, base, maximum_order)
    after = partition_collision_spectrum(states, extended, maximum_order)
    lost = tuple(old - new for old, new in zip(before, after))
    if any(value < 0 for value in lost):
        raise AssertionError("future refinement cannot increase J_k collision coordinates")
    return class_count(extended) - class_count(base), lost


def zero_cost_theorem_check(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    base_generators: Generators,
    added_generators: Generators,
) -> bool:
    """Finite audit of P_(G∪H)=P_G iff H respects P_G."""
    base = minimum_future_partition(states, observation, base_generators)
    extended = extension_partition(states, observation, base_generators, added_generators)
    return same_partition(base, extended) == operation_language_is_safe(
        states,
        base,
        added_generators,
    )


def static_common_partition(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    left_generators: Generators,
    right_generators: Generators,
) -> Partition:
    left = minimum_future_partition(states, observation, left_generators)
    right = minimum_future_partition(states, observation, right_generators)
    return common_refinement(states, left, right)


def static_common_is_joint_safe(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    left_generators: Generators,
    right_generators: Generators,
) -> bool:
    static = static_common_partition(
        states, observation, left_generators, right_generators
    )
    return operation_language_is_safe(
        states,
        static,
        _union_generators(left_generators, right_generators),
    )


def apply_operation_word(
    state: State,
    word: tuple[str, ...],
    generators: Generators,
) -> State:
    current = state
    for label in word:
        if label not in generators:
            raise ValueError("word contains undeclared generator")
        current = generators[label][current]
    return current


def shortest_mixed_operation_witness(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    left_generators: Generators,
    right_generators: Generators,
) -> tuple[State, State, tuple[str, ...]] | None:
    """Shortest word using both languages that reveals an extra joint distinction.

    Initial pairs are states merged by the static common refinement P_G∧P_H.
    A returned word uses at least one generator from each family and yields
    different declared observations.  If no dynamic coupling exists, returns None.
    """
    joint = _union_generators(left_generators, right_generators)
    static = static_common_partition(
        states, observation, left_generators, right_generators
    )
    if operation_language_is_safe(states, static, joint):
        return None

    left_labels = set(left_generators)
    right_labels = set(right_generators)
    queue = deque()
    visited: set[tuple[State, State, int]] = set()

    for first, second in combinations(states, 2):
        if static[first] != static[second]:
            continue
        key = (first, second, 0)
        visited.add(key)
        queue.append((first, second, 0, first, second, ()))

    while queue:
        current_left, current_right, mask, origin_left, origin_right, word = queue.popleft()
        if mask == 3 and observation[current_left] != observation[current_right]:
            return origin_left, origin_right, word
        for label in sorted(joint):
            generator = joint[label]
            next_left = generator[current_left]
            next_right = generator[current_right]
            next_mask = mask
            if label in left_labels:
                next_mask |= 1
            if label in right_labels:
                next_mask |= 2
            key = (next_left, next_right, next_mask)
            if key in visited:
                continue
            visited.add(key)
            queue.append(
                (
                    next_left,
                    next_right,
                    next_mask,
                    origin_left,
                    origin_right,
                    word + (label,),
                )
            )
    raise AssertionError("unsafe static common refinement must have a finite mixed witness")


def operation_coupling_depth(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    left_generators: Generators,
    right_generators: Generators,
) -> int | None:
    witness = shortest_mixed_operation_witness(
        states,
        observation,
        left_generators,
        right_generators,
    )
    return None if witness is None else len(witness[2])
