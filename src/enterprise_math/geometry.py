"""Intrinsic integer geometry helpers for Enterprise Math.

The primitives in this module use graph steps and integer lattice relations.
They do not compute real Euclidean distances or use floating-point values.
"""

from __future__ import annotations

from collections import deque
from collections.abc import Mapping, Sequence, Set


Vertex = object


def graph_distance(adjacency: Mapping[Vertex, Set[Vertex]], start: Vertex, goal: Vertex) -> int:
    """Return shortest unweighted walk length in a finite connected component.

    Raises ValueError when goal is not reachable from start.
    """
    if start == goal:
        return 0
    if start not in adjacency or goal not in adjacency:
        raise ValueError("start and goal must be present in adjacency")

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
