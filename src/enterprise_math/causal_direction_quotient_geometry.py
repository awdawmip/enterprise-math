"""Dimension descent by quotienting a graph-derived translation module by one direction.

For a simply-laced causal primitive graph, each primitive generator is represented
by one column of the graph-derived pair matrix C.  Fix a primitive column alpha.
Two relation states are equivalent modulo the chosen direction when their
difference is an integer multiple of alpha.  Quotienting the global translation
module by Z*alpha therefore needs no original ambient coordinates.

On the A_p family, the distinct nonzero images of the primitive columns form
exactly the primitive relation geometry of A_(p-1).  This is the coordinate-free
counterpart of merging the two slots named by a root e_i-e_j.
"""

from __future__ import annotations

from collections import deque

from .causal_global_relation_geometry import causal_relation_generators
from .causal_primitive_link_profile import Adjacency, Vector

RelationState = tuple[int, ...]
QuotientDirection = frozenset[int]


def _subtract(left: RelationState, right: RelationState) -> RelationState:
    return tuple(a - b for a, b in zip(left, right))


def is_integer_multiple(vector: RelationState, direction: RelationState) -> bool:
    multiplier = None
    for value, base in zip(vector, direction):
        if base == 0:
            if value != 0:
                return False
            continue
        if value % base != 0:
            return False
        candidate = value // base
        if multiplier is None:
            multiplier = candidate
        elif candidate != multiplier:
            return False
    if multiplier is None:
        return all(value == 0 for value in vector)
    return all(value == multiplier * base for value, base in zip(vector, direction))


def equivalent_mod_direction(
    left: RelationState,
    right: RelationState,
    direction: RelationState,
) -> bool:
    return is_integer_multiple(_subtract(left, right), direction)


def quotient_primitive_classes(
    adjacency: Adjacency,
    chosen_direction: Vector,
) -> tuple[tuple[QuotientDirection, ...], tuple[RelationState, ...]]:
    vertices = tuple(adjacency)
    if chosen_direction not in adjacency:
        raise ValueError("chosen direction must belong to primitive graph")
    generators = causal_relation_generators(adjacency)
    chosen = generators[vertices.index(chosen_direction)]
    zero = (0,) * len(chosen)

    unseen = set(range(len(generators)))
    classes: list[QuotientDirection] = []
    representatives: list[RelationState] = []
    while unseen:
        seed = min(unseen)
        equivalent = frozenset(
            index
            for index in tuple(unseen)
            if equivalent_mod_direction(generators[index], generators[seed], chosen)
        )
        unseen.difference_update(equivalent)
        representative = generators[seed]
        if equivalent_mod_direction(representative, zero, chosen):
            continue
        classes.append(equivalent)
        representatives.append(representative)
    return tuple(classes), tuple(representatives)


def quotient_primitive_graph(
    adjacency: Adjacency,
    chosen_direction: Vector,
) -> dict[QuotientDirection, frozenset[QuotientDirection]]:
    classes, representatives = quotient_primitive_classes(adjacency, chosen_direction)
    vertices = tuple(adjacency)
    generators = causal_relation_generators(adjacency)
    chosen = generators[vertices.index(chosen_direction)]

    result = {cls: set() for cls in classes}
    for left_index, left_class in enumerate(classes):
        for right_index in range(left_index + 1, len(classes)):
            right_class = classes[right_index]
            difference = _subtract(representatives[right_index], representatives[left_index])
            matches = {
                class_index
                for class_index, generator_class in enumerate(classes)
                if any(
                    equivalent_mod_direction(difference, generators[generator_index], chosen)
                    for generator_index in generator_class
                )
            }
            if matches:
                # Difference must represent one nonzero primitive quotient class;
                # its identity is irrelevant to whether left/right are adjacent.
                if len(matches) != 1:
                    raise ValueError("quotient difference maps to multiple primitive classes")
                result[left_class].add(right_class)
                result[right_class].add(left_class)
    return {vertex: frozenset(neighbors) for vertex, neighbors in result.items()}


def quotient_graph_connected(adjacency: dict[QuotientDirection, frozenset[QuotientDirection]]) -> bool:
    if not adjacency:
        return True
    seed = next(iter(adjacency))
    seen = {seed}
    queue = deque([seed])
    while queue:
        current = queue.popleft()
        for nxt in adjacency[current]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return len(seen) == len(adjacency)
