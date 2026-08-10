"""Intrinsic integer geometry helpers for Enterprise Math.

The primitives in this module use graph steps and integer lattice relations.
They do not compute real Euclidean distances or use floating-point values.
"""

from __future__ import annotations

from collections import deque
from collections.abc import Mapping, Sequence, Set


Vertex = object


def _validate_endpoints(
    adjacency: Mapping[Vertex, Set[Vertex]], start: Vertex, goal: Vertex
) -> None:
    if start not in adjacency or goal not in adjacency:
        raise ValueError("start and goal must be present in adjacency")


def _validate_closed_adjacency(adjacency: Mapping[Vertex, Set[Vertex]]) -> None:
    """Require every referenced neighbor to belong to the declared vertex set."""
    for neighbors in adjacency.values():
        for neighbor in neighbors:
            if neighbor not in adjacency:
                raise ValueError("adjacency must be closed over its vertex keys")


def _validate_undirected_simple_adjacency(
    adjacency: Mapping[Vertex, Set[Vertex]],
) -> None:
    """Validate the P012 undirected-simple-graph input contract."""
    _validate_closed_adjacency(adjacency)
    for vertex, neighbors in adjacency.items():
        if vertex in neighbors:
            raise ValueError("graph_distance requires loop-free simple-graph adjacency")
        for neighbor in neighbors:
            if vertex not in adjacency[neighbor]:
                raise ValueError("graph_distance requires symmetric undirected adjacency")


def _shortest_directed_walk_distance(
    adjacency: Mapping[Vertex, Set[Vertex]], start: Vertex, goal: Vertex
) -> int:
    if start == goal:
        return 0

    queue = deque([(start, 0)])
    seen = {start}
    while queue:
        vertex, distance = queue.popleft()
        for neighbor in adjacency[vertex]:
            if neighbor == goal:
                return distance + 1
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append((neighbor, distance + 1))
    raise ValueError("goal is not reachable from start")


def directed_graph_distance(
    adjacency: Mapping[Vertex, Set[Vertex]], start: Vertex, goal: Vertex
) -> int:
    """Return the shortest directed unweighted walk length.

    ``adjacency`` is interpreted literally as outgoing-neighbor data. Every
    referenced neighbor must also be a key of the mapping. The function is not
    a metric in general: asymmetric reachability and asymmetric distances are
    allowed. Raises ValueError when an endpoint is absent, the declared vertex
    domain is not closed, or ``goal`` is not reachable from ``start``.
    """
    _validate_endpoints(adjacency, start, goal)
    _validate_closed_adjacency(adjacency)
    return _shortest_directed_walk_distance(adjacency, start, goal)


def graph_distance(adjacency: Mapping[Vertex, Set[Vertex]], start: Vertex, goal: Vertex) -> int:
    """Return P012 shortest-step distance on undirected simple-graph input.

    The stable ``graph_distance`` name is reserved for the theorem domain used
    by P012: adjacency must be closed, loop-free, and symmetric. On a connected
    graph this is the ordinary natural-number graph metric. Disconnected input
    is accepted operationally, but a query across components raises ValueError.

    Use :func:`directed_graph_distance` when outgoing adjacency is intentionally
    asymmetric.
    """
    _validate_endpoints(adjacency, start, goal)
    _validate_undirected_simple_adjacency(adjacency)
    return _shortest_directed_walk_distance(adjacency, start, goal)


def l1_distance(left: Sequence[int], right: Sequence[int]) -> int:
    """Shortest-step distance for standard-axis adjacency on Z^d."""
    if len(left) != len(right):
        raise ValueError("points must have the same dimension")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in (*left, *right)):
        raise ValueError("coordinates must be integers")
    return sum(abs(a - b) for a, b in zip(left, right, strict=True))


def lattice2_sphere(radius: int) -> set[tuple[int, int]]:
    """Exact L1 sphere of radius r around the origin in Z^2."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    return {
        (x, y)
        for x in range(-radius, radius + 1)
        for y in range(-radius, radius + 1)
        if abs(x) + abs(y) == radius
    }


def lattice2_ball(radius: int) -> set[tuple[int, int]]:
    """Exact closed L1 ball of radius r around the origin in Z^2."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    return {
        (x, y)
        for x in range(-radius, radius + 1)
        for y in range(-radius, radius + 1)
        if abs(x) + abs(y) <= radius
    }
