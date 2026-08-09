"""E001.3 executable limits of unconstrained common-target semantics.

An arbitrary finite support family is expressive enough to encode any finite
simple graph as an intersection graph: give every graph edge its own target and
let each vertex support contain the targets of its incident edges.  Therefore
``T(a) ∩ T(b) != empty`` alone is not a physical or project-specific theory.
The admissible supports must be constrained by intrinsic geometry, finite scale,
and object structure.

The module also exposes why pairwise collision support does not determine a
higher-order common target: different support hypergraphs can have the same
2-section/intersection graph but different triple and higher intersections.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping
from itertools import combinations

Vertex = Hashable
Target = Hashable
Pair = tuple[Vertex, Vertex]


def intersection_pairs(
    supports: Mapping[Vertex, frozenset[Target]],
) -> frozenset[frozenset[Vertex]]:
    """Return unordered distinct vertex pairs whose finite supports intersect."""
    vertices = tuple(supports)
    pairs: set[frozenset[Vertex]] = set()
    for left_index, left in enumerate(vertices):
        for right in vertices[left_index + 1 :]:
            if supports[left].intersection(supports[right]):
                pairs.add(frozenset((left, right)))
    return frozenset(pairs)


def graph_as_edge_target_supports(
    vertices: Iterable[Vertex],
    edges: Iterable[tuple[Vertex, Vertex]],
) -> dict[Vertex, frozenset[tuple[str, frozenset[Vertex]]]]:
    """Encode any finite simple graph exactly as a common-target intersection graph.

    Each graph edge receives one private target.  The two endpoint supports both
    contain that target.  This construction is a deliberate *expressiveness
    warning*, not a proposed collision model.
    """
    vertex_tuple = tuple(vertices)
    vertex_set = set(vertex_tuple)
    if len(vertex_tuple) != len(vertex_set):
        raise ValueError("vertices must be distinct")

    mutable: dict[Vertex, set[tuple[str, frozenset[Vertex]]]] = {
        vertex: set() for vertex in vertex_tuple
    }
    seen_edges: set[frozenset[Vertex]] = set()
    for left, right in edges:
        if left == right:
            raise ValueError("self edges are not part of a simple graph")
        if left not in vertex_set or right not in vertex_set:
            raise ValueError("edge endpoints must belong to vertices")
        edge = frozenset((left, right))
        if edge in seen_edges:
            raise ValueError("duplicate undirected edge")
        seen_edges.add(edge)
        target = ("edge-target", edge)
        mutable[left].add(target)
        mutable[right].add(target)
    return {vertex: frozenset(targets) for vertex, targets in mutable.items()}


def common_target_count(
    supports: Mapping[Vertex, frozenset[Target]], vertices: Iterable[Vertex]
) -> int:
    """Count targets shared simultaneously by every selected vertex."""
    selected = tuple(vertices)
    if not selected:
        raise ValueError("at least one vertex is required")
    for vertex in selected:
        if vertex not in supports:
            raise ValueError("selected vertex is missing from supports")
    shared = set(supports[selected[0]])
    for vertex in selected[1:]:
        shared.intersection_update(supports[vertex])
    return len(shared)
