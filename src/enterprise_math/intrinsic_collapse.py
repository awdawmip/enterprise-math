"""E001.2 common-collapse semantics on coordinate-free finite graph geometry.

For an unweighted graph with shortest-walk metric, the finite collapse domain of
``center`` at radius ``r`` is the graph ball of vertices reachable in at most
``r`` primitive steps.  Two bodies collide exactly when those target sets
intersect.

In an unweighted shortest-path geometry this relational definition is equivalent
to ``d(a, b) <= r + s``: the forward implication is the triangle inequality;
for the reverse implication choose a vertex on a shortest path after at most
``r`` steps.  The implementation keeps the target-set definition primitive so
it also remains meaningful in later discrete geometries where a radius-sum
shortcut may not be available.
"""

from __future__ import annotations

from collections import deque
from collections.abc import Hashable, Mapping, Set

Vertex = Hashable


def graph_collapse_targets(
    adjacency: Mapping[Vertex, Set[Vertex]], center: Vertex, radius: int
) -> frozenset[Vertex]:
    """Return the exact finite unweighted graph ball used as a collapse domain."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    if center not in adjacency:
        raise ValueError("center must be present in adjacency")

    seen: set[Vertex] = {center}
    queue = deque([(center, 0)])
    while queue:
        vertex, distance = queue.popleft()
        if distance == radius:
            continue
        for neighbor in adjacency[vertex]:
            if neighbor not in adjacency:
                raise ValueError("every neighbor must be present in adjacency")
            if neighbor in seen:
                continue
            seen.add(neighbor)
            queue.append((neighbor, distance + 1))
    return frozenset(seen)


def graph_common_collapse_targets(
    adjacency: Mapping[Vertex, Set[Vertex]],
    left_center: Vertex,
    left_radius: int,
    right_center: Vertex,
    right_radius: int,
) -> frozenset[Vertex]:
    """Return every shared graph-state collapse witness for two finite bodies."""
    left = graph_collapse_targets(adjacency, left_center, left_radius)
    right = graph_collapse_targets(adjacency, right_center, right_radius)
    return frozenset(left.intersection(right))


def graph_common_collapse(
    adjacency: Mapping[Vertex, Set[Vertex]],
    left_center: Vertex,
    left_radius: int,
    right_center: Vertex,
    right_radius: int,
) -> bool:
    """Whether two graph-native collapse domains have a shared terminal state."""
    return bool(
        graph_common_collapse_targets(
            adjacency, left_center, left_radius, right_center, right_radius
        )
    )
