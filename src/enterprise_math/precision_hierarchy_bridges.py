"""Minimal cross-fiber bridge certificates for R004 hierarchy geometry.

Nested refinement alone induces an ultrametric but not connected local space.
This module isolates the exact additional finite data needed for connectivity:
for every parent precision class, the graph on its immediate child classes must
be connected by at least one witnessed leaf edge per quotient-graph edge.

Choosing a tree on every child quotient gives a connected leaf graph with
exactly ``|X|-1`` bridge edges, hence a globally minimal connected graph.  The
construction is ordinary finite graph/tree mathematics used as an R004 geometry
layer; it does not determine Euclidean dimension or physical locality.
"""
from __future__ import annotations

from collections import deque
from collections.abc import Mapping, Sequence
from typing import Hashable

from enterprise_math.precision_hierarchy_geometry import validate_signatures

State = Hashable
Edge = frozenset[State]


def _edge(left: State, right: State) -> Edge:
    if left == right:
        raise ValueError("bridge edge needs distinct leaves")
    return frozenset((left, right))


def _children_by_parent(
    signatures: Mapping[State, Sequence[Hashable]], level: int
) -> dict[Hashable, dict[Hashable, tuple[State, ...]]]:
    width = len(next(iter(signatures.values())))
    if not 0 <= level < width - 1:
        raise ValueError("level must have a finer child level")
    temporary: dict[Hashable, dict[Hashable, list[State]]] = {}
    for state, signature in signatures.items():
        row = tuple(signature)
        parent = row[level]
        child = row[level + 1]
        temporary.setdefault(parent, {}).setdefault(child, []).append(state)
    return {
        parent: {child: tuple(leaves) for child, leaves in children.items()}
        for parent, children in temporary.items()
    }


def _connected_vertices(vertices: Sequence[Hashable], edges: set[frozenset[Hashable]]) -> bool:
    vertex_set = set(vertices)
    if not vertex_set:
        return False
    if len(vertex_set) == 1:
        return True
    start = next(iter(vertex_set))
    seen = {start}
    queue: deque[Hashable] = deque([start])
    while queue:
        current = queue.popleft()
        for edge in edges:
            if current not in edge:
                continue
            other = next(value for value in edge if value != current)
            if other in vertex_set and other not in seen:
                seen.add(other)
                queue.append(other)
    return seen == vertex_set


def leaf_graph_connected(
    signatures: Mapping[State, Sequence[Hashable]], edges: Sequence[Edge]
) -> bool:
    validate_signatures(tuple(range(1, len(next(iter(signatures.values()))) + 1)), signatures)
    # Only the nested signatures matter here; use a simple synthetic divisibility
    # chain for validation of nesting/root/final distinction below.
    states = tuple(signatures)
    if len(states) == 1:
        return True
    edge_set = set(edges)
    if any(len(edge) != 2 or not edge.issubset(set(states)) for edge in edge_set):
        raise ValueError("every bridge edge must join two declared leaves")
    return _connected_vertices(states, edge_set)


def refinement_bridge_certificate_holds(
    scales: Sequence[int],
    signatures: Mapping[State, Sequence[Hashable]],
    edges: Sequence[Edge],
) -> bool:
    """Check connectivity of every immediate child quotient.

    For a parent class at level ``i``, only leaf edges whose endpoints lie in
    distinct children at level ``i+1`` count toward that parent's certificate.
    By nestedness such an edge has that parent as its unique first-divergence
    location and cannot simultaneously repair a different parent split.
    """
    validate_signatures(scales, signatures)
    states = set(signatures)
    edge_set = set(edges)
    if any(len(edge) != 2 or not edge.issubset(states) for edge in edge_set):
        raise ValueError("every bridge edge must join two declared leaves")

    width = len(tuple(scales))
    for level in range(width - 1):
        for parent, children in _children_by_parent(signatures, level).items():
            child_labels = tuple(children)
            if len(child_labels) <= 1:
                continue
            child_edges: set[frozenset[Hashable]] = set()
            for edge in edge_set:
                left, right = tuple(edge)
                left_row = tuple(signatures[left])
                right_row = tuple(signatures[right])
                if left_row[level] != parent or right_row[level] != parent:
                    continue
                left_child = left_row[level + 1]
                right_child = right_row[level + 1]
                if left_child != right_child:
                    child_edges.add(frozenset((left_child, right_child)))
            if not _connected_vertices(child_labels, child_edges):
                return False
    return True


def minimum_bridge_edge_count(
    scales: Sequence[int], signatures: Mapping[State, Sequence[Hashable]]
) -> int:
    """Sharp edge lower bound for an immediate-child bridge certificate."""
    validate_signatures(scales, signatures)
    required = 0
    width = len(tuple(scales))
    for level in range(width - 1):
        for children in _children_by_parent(signatures, level).values():
            required += max(len(children) - 1, 0)
    if required != len(signatures) - 1:
        raise AssertionError("nested one-root/singleton-final hierarchy must telescope to |X|-1")
    return required


def canonical_minimal_bridge_edges(
    scales: Sequence[int], signatures: Mapping[State, Sequence[Hashable]]
) -> frozenset[Edge]:
    """Choose one quotient-tree witness family using first-seen representatives."""
    validate_signatures(scales, signatures)
    edges: set[Edge] = set()
    width = len(tuple(scales))
    for level in range(width - 1):
        for children in _children_by_parent(signatures, level).values():
            groups = tuple(children.values())
            representatives = tuple(group[0] for group in groups)
            for left, right in zip(representatives, representatives[1:]):
                edges.add(_edge(left, right))
    if len(edges) != minimum_bridge_edge_count(scales, signatures):
        raise AssertionError("minimal bridge construction must have |X|-1 edges")
    if not refinement_bridge_certificate_holds(scales, signatures, tuple(edges)):
        raise AssertionError("constructed bridges must connect every child quotient")
    return frozenset(edges)


def boundary_minimal_bridge_edges(
    scales: Sequence[int], signatures: Mapping[int, Sequence[Hashable]]
) -> frozenset[Edge]:
    """Alternative minimal witness choice for ordered integer leaves.

    Child blocks are ordered by their smallest leaf; consecutive children are
    joined by ``max(left) -- min(right)``.  On interval-like binary refinement
    this produces a path-like leaf tree, demonstrating that one hierarchy plus
    the same minimal bridge count does not determine macroscopic geometry.
    """
    validate_signatures(scales, signatures)
    edges: set[Edge] = set()
    width = len(tuple(scales))
    for level in range(width - 1):
        for children in _children_by_parent(signatures, level).values():
            groups = sorted(children.values(), key=lambda group: min(group))
            for left, right in zip(groups, groups[1:]):
                edges.add(_edge(max(left), min(right)))
    if len(edges) != minimum_bridge_edge_count(scales, signatures):
        raise AssertionError("boundary bridge construction must be minimal")
    if not refinement_bridge_certificate_holds(scales, signatures, tuple(edges)):
        raise AssertionError("boundary bridges must connect every child quotient")
    return frozenset(edges)


def graph_diameter(states: Sequence[State], edges: Sequence[Edge]) -> int:
    vertices = tuple(states)
    if not vertices:
        raise ValueError("graph needs at least one vertex")
    edge_set = set(edges)
    if not _connected_vertices(vertices, edge_set):
        raise ValueError("diameter requires a connected graph")

    diameter = 0
    for source in vertices:
        distance = {source: 0}
        queue: deque[State] = deque([source])
        while queue:
            current = queue.popleft()
            for edge in edge_set:
                if current not in edge:
                    continue
                other = next(value for value in edge if value != current)
                if other not in distance:
                    distance[other] = distance[current] + 1
                    queue.append(other)
        diameter = max(diameter, max(distance.values()))
    return diameter
