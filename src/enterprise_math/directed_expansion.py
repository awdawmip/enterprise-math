"""Directed future-section expansion for Enterprise Math P019.

A finite directed primitive graph supplies one-step future reachability.  For a
finite cross-section A, the integer expansion is |F(A)|-|A|.  Distinct outgoing
incidences that land on the same future vertex are counted as a collision/focus
term, giving an exact branching-minus-collision decomposition.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Hashable, Iterable
from math import comb

Vertex = Hashable
DirectedEdge = tuple[Vertex, Vertex]


def _validated_graph(
    vertices: Iterable[Vertex], edges: Iterable[DirectedEdge]
) -> tuple[tuple[Vertex, ...], tuple[DirectedEdge, ...]]:
    vertex_tuple = tuple(vertices)
    if not vertex_tuple:
        raise ValueError("vertex set must be nonempty")
    if len(vertex_tuple) != len(set(vertex_tuple)):
        raise ValueError("vertices must be distinct")
    vertex_set = set(vertex_tuple)
    edge_tuple: list[DirectedEdge] = []
    seen: set[DirectedEdge] = set()
    for source, target in edges:
        if source not in vertex_set or target not in vertex_set:
            raise ValueError("directed edge endpoint is outside the vertex set")
        edge = (source, target)
        if edge not in seen:
            edge_tuple.append(edge)
            seen.add(edge)
    return vertex_tuple, tuple(edge_tuple)


def _validated_section(vertices: tuple[Vertex, ...], section: Iterable[Vertex]) -> frozenset[Vertex]:
    section_set = frozenset(section)
    if not section_set:
        raise ValueError("cross-section must be nonempty")
    if not section_set.issubset(vertices):
        raise ValueError("cross-section contains a vertex outside the graph")
    return section_set


def future_section(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
) -> frozenset[Vertex]:
    """Return the distinct one-step future vertices reachable from ``section``."""
    vertex_tuple, edge_tuple = _validated_graph(vertices, edges)
    current = _validated_section(vertex_tuple, section)
    return frozenset(target for source, target in edge_tuple if source in current)


def section_expansion(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
) -> int:
    """Return Xi(A)=|F(A)|-|A|."""
    vertex_tuple, edge_tuple = _validated_graph(vertices, edges)
    current = _validated_section(vertex_tuple, section)
    future = frozenset(target for source, target in edge_tuple if source in current)
    return len(future) - len(current)


def successor_multiplicities(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
) -> dict[Vertex, int]:
    """Count outgoing incidences from A landing on each distinct future vertex."""
    vertex_tuple, edge_tuple = _validated_graph(vertices, edges)
    current = _validated_section(vertex_tuple, section)
    counts = Counter(target for source, target in edge_tuple if source in current)
    return dict(counts)


def branching_surplus(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
) -> int:
    """Return total outgoing incidence count minus current section cardinality."""
    vertex_tuple, edge_tuple = _validated_graph(vertices, edges)
    current = _validated_section(vertex_tuple, section)
    incidences = sum(1 for source, _ in edge_tuple if source in current)
    return incidences - len(current)


def collision_excess(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
) -> int:
    """Return the number of outgoing incidences lost when targets are deduplicated."""
    multiplicities = successor_multiplicities(vertices, edges, section)
    return sum(multiplicity - 1 for multiplicity in multiplicities.values())


def local_collision_spectrum(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
    order: int,
) -> int:
    """Return sum_w binom(m_A(w), order) for the outgoing-incidence target map."""
    if not isinstance(order, int):
        raise TypeError("collision order must be an integer")
    if order < 0:
        raise ValueError("collision order must be nonnegative")
    multiplicities = successor_multiplicities(vertices, edges, section)
    return sum(
        comb(multiplicity, order)
        for multiplicity in multiplicities.values()
        if multiplicity >= order
    )


def branching_collision_decomposition(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
) -> dict[str, int]:
    """Return Xi = branching_surplus - collision_excess as exact integers."""
    expansion = section_expansion(vertices, edges, section)
    branching = branching_surplus(vertices, edges, section)
    collision = collision_excess(vertices, edges, section)
    if expansion != branching - collision:
        raise AssertionError("branching/collision decomposition failed")
    return {
        "expansion": expansion,
        "branching_surplus": branching,
        "collision_excess": collision,
    }


def union_expansion_identity(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    first: Iterable[Vertex],
    second: Iterable[Vertex],
) -> dict[str, int]:
    """Return the exact overlap defect for Xi(A union B)."""
    vertex_tuple, edge_tuple = _validated_graph(vertices, edges)
    first_set = _validated_section(vertex_tuple, first)
    second_set = _validated_section(vertex_tuple, second)
    future_first = frozenset(target for source, target in edge_tuple if source in first_set)
    future_second = frozenset(target for source, target in edge_tuple if source in second_set)
    union = first_set | second_set
    future_union = future_first | future_second
    xi_first = len(future_first) - len(first_set)
    xi_second = len(future_second) - len(second_set)
    xi_union = len(future_union) - len(union)
    state_overlap = len(first_set & second_set)
    future_overlap = len(future_first & future_second)
    expected = xi_first + xi_second + state_overlap - future_overlap
    if xi_union != expected:
        raise AssertionError("union expansion identity failed")
    return {
        "union_expansion": xi_union,
        "first_expansion": xi_first,
        "second_expansion": xi_second,
        "state_overlap": state_overlap,
        "future_overlap": future_overlap,
    }


def expansion_trajectory(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    initial_section: Iterable[Vertex],
    steps: int,
) -> tuple[tuple[frozenset[Vertex], ...], tuple[int, ...]]:
    """Iterate one-step future sections until ``steps`` or an empty future is reached."""
    if not isinstance(steps, int):
        raise TypeError("steps must be an integer")
    if steps < 0:
        raise ValueError("steps must be nonnegative")
    vertex_tuple, edge_tuple = _validated_graph(vertices, edges)
    current = _validated_section(vertex_tuple, initial_section)
    sections: list[frozenset[Vertex]] = [current]
    expansions: list[int] = []
    for _ in range(steps):
        future = frozenset(target for source, target in edge_tuple if source in current)
        expansions.append(len(future) - len(current))
        sections.append(future)
        if not future:
            break
        current = future
    return tuple(sections), tuple(expansions)


def telescoping_expansion_check(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    initial_section: Iterable[Vertex],
    steps: int,
) -> bool:
    """Verify sum_t Xi(A_t)=|A_T|-|A_0| along the generated trajectory."""
    sections, expansions = expansion_trajectory(vertices, edges, initial_section, steps)
    return sum(expansions) == len(sections[-1]) - len(sections[0])
