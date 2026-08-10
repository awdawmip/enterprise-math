"""Exact integer causal profiles for the laminated Lambda_9 -> Lambda_10 step.

The Gram matrices below are exact catalogue data.  Minimal vectors are enumerated
from the Gram forms by `causal_gram_lattice`, then treated only as primitive
integer displacement labels.  A pair of primitive directions u,v is adjacent
when v-u is itself minimal.

The purpose is not to reprove lattice-packing density.  It is to measure how a
laminated dimension lift preserves old primitive states, adds new primitive
states, and refines old local relation types.
"""

from __future__ import annotations

from collections import Counter

from .causal_gram_lattice import Gram, minimal_vectors
from .causal_primitive_link_profile import primitive_direction_graph

LAMBDA9_GRAM: Gram = (
    (4, -2, 0, 0, 0, 0, 0, 0, 0),
    (-2, 4, -2, 2, 0, 0, 0, 0, 0),
    (0, -2, 4, 0, 0, 2, 0, 0, 0),
    (0, 2, 0, 4, 2, 2, 0, 0, 0),
    (0, 0, 0, 2, 4, 2, 0, 0, 2),
    (0, 0, 2, 2, 2, 4, 2, 2, 1),
    (0, 0, 0, 0, 0, 2, 4, 2, 0),
    (0, 0, 0, 0, 0, 2, 2, 4, 0),
    (0, 0, 0, 0, 2, 1, 0, 0, 4),
)

LAMBDA10_GRAM: Gram = (
    (4, -2, 0, 0, 0, 0, 0, 0, 0, 0),
    (-2, 4, -2, 2, 0, 0, 0, 0, 0, 0),
    (0, -2, 4, 0, 0, 2, 0, 0, 0, 0),
    (0, 2, 0, 4, 2, 2, 0, 0, 0, 0),
    (0, 0, 0, 2, 4, 2, 0, 0, 2, 1),
    (0, 0, 2, 2, 2, 4, 2, 2, 1, 2),
    (0, 0, 0, 0, 0, 2, 4, 2, 0, 2),
    (0, 0, 0, 0, 0, 2, 2, 4, 0, 2),
    (0, 0, 0, 0, 2, 1, 0, 0, 4, 2),
    (0, 0, 0, 0, 1, 2, 2, 2, 2, 4),
)


def lambda9_minimal_vectors() -> tuple[tuple[int, ...], ...]:
    return minimal_vectors(LAMBDA9_GRAM, 4)


def lambda10_minimal_vectors() -> tuple[tuple[int, ...], ...]:
    return minimal_vectors(LAMBDA10_GRAM, 4)


def primitive_degree_histogram(vectors: tuple[tuple[int, ...], ...]) -> dict[int, int]:
    adjacency = primitive_direction_graph(vectors)
    return dict(sorted(Counter(len(adjacency[v]) for v in vectors).items()))


def layer_histogram(vectors: tuple[tuple[int, ...], ...], coordinate: int = -1) -> dict[int, int]:
    return dict(sorted(Counter(vector[coordinate] for vector in vectors).items()))


def layer_degree_histogram(
    vectors: tuple[tuple[int, ...], ...],
    coordinate: int = -1,
) -> dict[tuple[int, int], int]:
    adjacency = primitive_direction_graph(vectors)
    return dict(sorted(Counter((v[coordinate], len(adjacency[v])) for v in vectors).items()))


def embedded_degree_transition(
    old_vectors: tuple[tuple[int, ...], ...],
    new_vectors: tuple[tuple[int, ...], ...],
) -> dict[tuple[int, int], int]:
    """Degree refinement of old directions under the coordinate embedding x->(x,0)."""
    if not old_vectors or not new_vectors:
        raise ValueError("vector families must be non-empty")
    if len(new_vectors[0]) != len(old_vectors[0]) + 1:
        raise ValueError("new vectors must have exactly one additional coordinate")
    old_adjacency = primitive_direction_graph(old_vectors)
    new_adjacency = primitive_direction_graph(new_vectors)
    new_set = set(new_vectors)
    transition = Counter()
    for old in old_vectors:
        lifted = old + (0,)
        if lifted not in new_set:
            raise ValueError("new primitive shell does not contain the embedded old shell")
        transition[(len(old_adjacency[old]), len(new_adjacency[lifted]))] += 1
    return dict(sorted(transition.items()))


def layer_edge_histogram(
    vectors: tuple[tuple[int, ...], ...],
    coordinate: int = -1,
) -> dict[tuple[int, int], int]:
    adjacency = primitive_direction_graph(vectors)
    seen = set()
    counts = Counter()
    for left in vectors:
        for right in adjacency[left]:
            edge = tuple(sorted((left, right)))
            if edge in seen:
                continue
            seen.add(edge)
            layer_pair = tuple(sorted((left[coordinate], right[coordinate])))
            counts[layer_pair] += 1
    return dict(sorted(counts.items()))


def lambda9_profile() -> dict[str, object]:
    vectors = lambda9_minimal_vectors()
    return {
        "minimal_vector_count": len(vectors),
        "degree_histogram": primitive_degree_histogram(vectors),
        "layer_histogram": layer_histogram(vectors),
        "layer_degree_histogram": layer_degree_histogram(vectors),
        "layer_edge_histogram": layer_edge_histogram(vectors),
    }


def lambda10_profile() -> dict[str, object]:
    vectors = lambda10_minimal_vectors()
    return {
        "minimal_vector_count": len(vectors),
        "degree_histogram": primitive_degree_histogram(vectors),
        "layer_histogram": layer_histogram(vectors),
        "layer_degree_histogram": layer_degree_histogram(vectors),
        "layer_edge_histogram": layer_edge_histogram(vectors),
        "old_degree_transition": embedded_degree_transition(lambda9_minimal_vectors(), vectors),
    }
