"""Overlap-spectrum focusing calculus for Enterprise Math P019.

This module resolves the collision/focusing excess of a future section into
k-way intersections of primitive successor sets.  Everything is finite and
integer-valued; no continuum curvature or probability measure is assumed.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable
from itertools import combinations

from .directed_expansion import (
    branching_surplus,
    collision_excess,
    future_section,
    local_collision_spectrum,
    section_expansion,
    successor_multiplicities,
)

Vertex = Hashable
DirectedEdge = tuple[Vertex, Vertex]


def _normalized_graph(
    vertices: Iterable[Vertex], edges: Iterable[DirectedEdge]
) -> tuple[tuple[Vertex, ...], tuple[DirectedEdge, ...]]:
    vertex_tuple = tuple(vertices)
    if not vertex_tuple:
        raise ValueError("vertex set must be nonempty")
    if len(vertex_tuple) != len(set(vertex_tuple)):
        raise ValueError("vertices must be distinct")
    vertex_set = set(vertex_tuple)
    normalized: list[DirectedEdge] = []
    seen: set[DirectedEdge] = set()
    for source, target in edges:
        if source not in vertex_set or target not in vertex_set:
            raise ValueError("directed edge endpoint is outside the vertex set")
        edge = (source, target)
        if edge not in seen:
            seen.add(edge)
            normalized.append(edge)
    return vertex_tuple, tuple(normalized)


def _section_set(vertices: tuple[Vertex, ...], section: Iterable[Vertex]) -> frozenset[Vertex]:
    result = frozenset(section)
    if not result:
        raise ValueError("section must be nonempty")
    if not result.issubset(set(vertices)):
        raise ValueError("section contains a vertex outside the graph")
    return result


def successor_set(
    vertices: Iterable[Vertex], edges: Iterable[DirectedEdge], source: Vertex
) -> frozenset[Vertex]:
    """Return the distinct primitive successors of one source vertex."""
    vertex_tuple, edge_tuple = _normalized_graph(vertices, edges)
    if source not in set(vertex_tuple):
        raise ValueError("source is outside the graph")
    return frozenset(target for left, target in edge_tuple if left == source)


def k_way_successor_overlap(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
    order: int,
) -> int:
    """Sum cardinalities of successor intersections over all k-subsets of A."""
    if not isinstance(order, int):
        raise TypeError("overlap order must be an integer")
    if order < 1:
        raise ValueError("overlap order must be positive")
    vertex_tuple, edge_tuple = _normalized_graph(vertices, edges)
    current = _section_set(vertex_tuple, section)
    if order > len(current):
        return 0
    successor_cache = {
        source: frozenset(target for left, target in edge_tuple if left == source)
        for source in current
    }
    total = 0
    for subset in combinations(current, order):
        intersection = successor_cache[subset[0]]
        for source in subset[1:]:
            intersection = intersection & successor_cache[source]
            if not intersection:
                break
        total += len(intersection)
    return total


def overlap_spectrum(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
) -> tuple[int, ...]:
    """Return (J_1,...,J_|A|) as k-way successor-overlap counts."""
    vertex_tuple, edge_tuple = _normalized_graph(vertices, edges)
    current = _section_set(vertex_tuple, section)
    return tuple(
        k_way_successor_overlap(vertex_tuple, edge_tuple, current, order)
        for order in range(1, len(current) + 1)
    )


def collision_from_overlap_spectrum(spectrum: Iterable[int]) -> int:
    """Return C = J_2 - J_3 + J_4 - ... from a finite overlap spectrum."""
    values = tuple(spectrum)
    if any(not isinstance(value, int) or value < 0 for value in values):
        raise ValueError("overlap spectrum must contain nonnegative integers")
    return sum(
        value if order % 2 == 0 else -value
        for order, value in enumerate(values, start=1)
        if order >= 2
    )


def expansion_from_overlap_spectrum(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
) -> int:
    """Return Xi = B - J_2 + J_3 - J_4 + ... exactly."""
    spectrum = overlap_spectrum(vertices, edges, section)
    collision = collision_from_overlap_spectrum(spectrum)
    return branching_surplus(vertices, edges, section) - collision


def pair_collision_bounds(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
) -> dict[str, int]:
    """Return exact C, pair load J2, and maximum target multiplicity mu.

    The finite inequalities are C <= J2 and 2*J2 <= mu*C whenever C>0.
    """
    multiplicities = successor_multiplicities(vertices, edges, section)
    collision = collision_excess(vertices, edges, section)
    pair_load = local_collision_spectrum(vertices, edges, section, 2)
    maximum = max(multiplicities.values(), default=0)
    if collision > pair_load:
        raise AssertionError("collision excess must not exceed pair collision load")
    if collision > 0 and 2 * pair_load > maximum * collision:
        raise AssertionError("pair load exceeds multiplicity-depth bound")
    return {
        "collision_excess": collision,
        "pair_collision_load": pair_load,
        "maximum_target_multiplicity": maximum,
    }


def marginal_expansion_increment(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
    added_vertex: Vertex,
) -> dict[str, int]:
    """Return the exact expansion increment from adding one new source vertex.

    Delta_v Xi(A) = (outdeg(v)-1) - |Succ(v) intersect F(A)|.
    """
    vertex_tuple, edge_tuple = _normalized_graph(vertices, edges)
    current = _section_set(vertex_tuple, section)
    if added_vertex not in set(vertex_tuple):
        raise ValueError("added vertex is outside the graph")
    if added_vertex in current:
        raise ValueError("added vertex must not already belong to the section")
    old_future = future_section(vertex_tuple, edge_tuple, current)
    successors = successor_set(vertex_tuple, edge_tuple, added_vertex)
    overlap = len(successors & old_future)
    branch_increment = len(successors) - 1
    predicted = branch_increment - overlap
    actual = section_expansion(
        vertex_tuple, edge_tuple, current | {added_vertex}
    ) - section_expansion(vertex_tuple, edge_tuple, current)
    if predicted != actual:
        raise AssertionError("marginal expansion decomposition failed")
    return {
        "marginal_expansion": actual,
        "branch_increment": branch_increment,
        "future_overlap_load": overlap,
    }


def diminishing_returns_check(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    smaller: Iterable[Vertex],
    larger: Iterable[Vertex],
    added_vertex: Vertex,
) -> bool:
    """Verify Delta_v Xi(A) >= Delta_v Xi(B) for A subset B and v notin B."""
    vertex_tuple, edge_tuple = _normalized_graph(vertices, edges)
    small = _section_set(vertex_tuple, smaller)
    large = _section_set(vertex_tuple, larger)
    if not small.issubset(large):
        raise ValueError("smaller section must be a subset of larger section")
    if added_vertex in large:
        raise ValueError("added vertex must lie outside the larger section")
    delta_small = marginal_expansion_increment(
        vertex_tuple, edge_tuple, small, added_vertex
    )["marginal_expansion"]
    delta_large = marginal_expansion_increment(
        vertex_tuple, edge_tuple, large, added_vertex
    )["marginal_expansion"]
    return delta_small >= delta_large


def submodularity_defect(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    first: Iterable[Vertex],
    second: Iterable[Vertex],
) -> int:
    """Return Xi(A)+Xi(B)-Xi(A union B)-Xi(A intersection B) >= 0.

    Empty intersections are handled by the natural extension Xi(empty)=0.
    """
    vertex_tuple, edge_tuple = _normalized_graph(vertices, edges)
    vertex_set = set(vertex_tuple)
    first_set = frozenset(first)
    second_set = frozenset(second)
    if not first_set or not second_set:
        raise ValueError("input sections must be nonempty")
    if not first_set.issubset(vertex_set) or not second_set.issubset(vertex_set):
        raise ValueError("section contains a vertex outside the graph")

    def xi(section: frozenset[Vertex]) -> int:
        if not section:
            return 0
        return section_expansion(vertex_tuple, edge_tuple, section)

    defect = (
        xi(first_set)
        + xi(second_set)
        - xi(first_set | second_set)
        - xi(first_set & second_set)
    )
    if defect < 0:
        raise AssertionError("future-section expansion must be submodular")
    return defect
