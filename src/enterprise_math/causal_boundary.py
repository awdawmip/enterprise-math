"""Coordinate-free finite causal-boundary helpers for Enterprise Math P019.

The primitive input is a finite undirected graph together with an integer-valued
outgoing expansion field xi: V -> Z.  No radial coordinate, Euclidean metric, or
continuum interpolation is assumed.
"""

from __future__ import annotations

from collections.abc import Callable, Hashable, Iterable

from .precision_system import observation_fiber, refinement_projection

Vertex = Hashable
Edge = frozenset[Vertex]


def phase(value: int) -> int:
    """Return -1, 0, or +1 for an integer expansion value."""
    if not isinstance(value, int):
        raise TypeError("expansion value must be an integer")
    return (value > 0) - (value < 0)


def normalize_edges(vertices: Iterable[Vertex], edges: Iterable[tuple[Vertex, Vertex]]) -> tuple[Edge, ...]:
    """Validate and normalize a finite simple undirected edge collection."""
    vertex_set = set(vertices)
    normalized: list[Edge] = []
    seen: set[Edge] = set()
    for left, right in edges:
        if left not in vertex_set or right not in vertex_set:
            raise ValueError("edge endpoint is outside the vertex set")
        if left == right:
            raise ValueError("self-loops are not primitive boundary edges")
        edge = frozenset((left, right))
        if edge not in seen:
            normalized.append(edge)
            seen.add(edge)
    return tuple(normalized)


def causal_boundary_complex(
    vertices: list[Vertex],
    edges: list[tuple[Vertex, Vertex]],
    expansion: Callable[[Vertex], int],
) -> dict[str, tuple[object, ...]]:
    """Return zero-expansion vertices and opposite-phase crossing edges."""
    normalized = normalize_edges(vertices, edges)
    zero_vertices = tuple(vertex for vertex in vertices if phase(expansion(vertex)) == 0)
    crossing_edges = tuple(
        edge
        for edge in normalized
        if _edge_phase_product(edge, expansion) < 0
    )
    return {"vertices": zero_vertices, "edges": crossing_edges}


def _edge_phase_product(edge: Edge, expansion: Callable[[Vertex], int]) -> int:
    endpoints = tuple(edge)
    if len(endpoints) != 2:
        raise ValueError("boundary edge must have exactly two endpoints")
    return phase(expansion(endpoints[0])) * phase(expansion(endpoints[1]))


def path_crosses_causal_boundary(
    path: list[Vertex], expansion: Callable[[Vertex], int]
) -> bool:
    """Return whether a vertex path meets a zero vertex or opposite-phase edge."""
    if not path:
        raise ValueError("path must be nonempty")
    if any(phase(expansion(vertex)) == 0 for vertex in path):
        return True
    return any(
        phase(expansion(left)) * phase(expansion(right)) < 0
        for left, right in zip(path, path[1:])
    )


def opposite_endpoint_path_has_boundary(
    path: list[Vertex], expansion: Callable[[Vertex], int]
) -> bool:
    """Verify the discrete intermediate-value boundary property for one path.

    If the endpoints have opposite nonzero phase, the path must contain a zero
    vertex or an adjacent opposite-phase crossing edge.
    """
    if not path:
        raise ValueError("path must be nonempty")
    start = phase(expansion(path[0]))
    end = phase(expansion(path[-1]))
    if start * end >= 0:
        raise ValueError("path endpoints must have opposite nonzero phase")
    return path_crosses_causal_boundary(path, expansion)


def phase_regions(
    vertices: list[Vertex], expansion: Callable[[Vertex], int]
) -> dict[int, tuple[Vertex, ...]]:
    """Partition vertices into negative, zero, and positive expansion regions."""
    return {
        sign: tuple(vertex for vertex in vertices if phase(expansion(vertex)) == sign)
        for sign in (-1, 0, 1)
    }


def phase_possibilities_on_fiber(
    states: list[Vertex],
    observation: Callable[[Vertex], Hashable],
    expansion: Callable[[Vertex], int],
    state: Vertex,
) -> frozenset[int]:
    """Return the expansion phases still compatible with one observation fiber."""
    fiber = observation_fiber(states, observation, state)
    return frozenset(phase(expansion(candidate)) for candidate in fiber)


def phase_ambiguity(
    states: list[Vertex],
    observation: Callable[[Vertex], Hashable],
    expansion: Callable[[Vertex], int],
    state: Vertex,
) -> int:
    """Return the number of distinct causal phases compatible with observation."""
    return len(phase_possibilities_on_fiber(states, observation, expansion, state))


def phase_refinement_profile(
    states: list[Vertex],
    observations: list[Callable[[Vertex], Hashable]],
    expansion: Callable[[Vertex], int],
    state: Vertex,
) -> list[int]:
    """Return a nonincreasing phase-ambiguity profile along a P018 refinement chain."""
    if not observations:
        raise ValueError("at least one observation is required")
    profile: list[int] = []
    previous = observations[0]
    last: int | None = None
    for observation in observations:
        refinement_projection(states, previous, observation)
        ambiguity = phase_ambiguity(states, observation, expansion, state)
        if last is not None and ambiguity > last:
            raise AssertionError("causal phase ambiguity increased under refinement")
        profile.append(ambiguity)
        last = ambiguity
        previous = observation
    return profile


def transported_boundary_complex(
    vertices: list[Vertex],
    edges: list[tuple[Vertex, Vertex]],
    expansion: Callable[[Vertex], int],
    automorphism: dict[Vertex, Vertex],
) -> dict[str, tuple[object, ...]]:
    """Transport the boundary through a graph automorphism candidate.

    The caller can compare this object with the boundary recomputed from the
    transported expansion field.  The helper validates bijectivity and edge
    preservation without assuming coordinates.
    """
    vertex_set = set(vertices)
    if set(automorphism) != vertex_set or set(automorphism.values()) != vertex_set:
        raise ValueError("automorphism must be a bijection of the vertex set")
    normalized = normalize_edges(vertices, edges)
    edge_set = set(normalized)
    for edge in normalized:
        mapped = frozenset(automorphism[vertex] for vertex in edge)
        if mapped not in edge_set:
            raise ValueError("map does not preserve primitive adjacency")

    boundary = causal_boundary_complex(vertices, edges, expansion)
    mapped_vertices = tuple(automorphism[vertex] for vertex in boundary["vertices"])
    mapped_edges = tuple(
        frozenset(automorphism[vertex] for vertex in edge)
        for edge in boundary["edges"]
    )
    return {"vertices": mapped_vertices, "edges": mapped_edges}
