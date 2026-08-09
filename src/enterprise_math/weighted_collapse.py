"""E001.3 finite integer-weight collapse domains and relational split defects.

For unit-step graph geometry, radius relations R_r compose exactly as
``R_r ; R_s = R_(r+s)`` because a shortest path can be split at an intermediate
vertex after an integer number of primitive steps.

Positive integer edge costs expose an important finite-resolution boundary.  The
triangle inequality always gives ``R_r ; R_s <= R_(r+s)``, but equality can fail
when one atomic edge has cost larger than either budget and has no representable
intermediate state.  In that case a radius-sum distance shortcut can say
``d(a,b) <= r+s`` even though the two finite collapse domains have no shared
state.

This is a structural diagnostic, not a claim that weighted shortest paths are
new mathematics.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from heapq import heappop, heappush

Vertex = Hashable
WeightedAdjacency = Mapping[Vertex, Mapping[Vertex, int]]
Relation = frozenset[tuple[Vertex, Vertex]]


def _validate_weighted_graph(adjacency: WeightedAdjacency) -> None:
    for vertex, neighbors in adjacency.items():
        for neighbor, weight in neighbors.items():
            if neighbor not in adjacency:
                raise ValueError("every weighted neighbor must be present in adjacency")
            if isinstance(weight, bool) or not isinstance(weight, int) or weight <= 0:
                raise ValueError("edge weights must be positive integers")


def weighted_shortest_distances(
    adjacency: WeightedAdjacency, center: Vertex, budget: int | None = None
) -> dict[Vertex, int]:
    """Exact non-negative integer shortest distances, optionally budget-truncated."""
    _validate_weighted_graph(adjacency)
    if center not in adjacency:
        raise ValueError("center must be present in adjacency")
    if budget is not None:
        if isinstance(budget, bool) or not isinstance(budget, int) or budget < 0:
            raise ValueError("budget must be a non-negative integer")

    distances: dict[Vertex, int] = {center: 0}
    queue: list[tuple[int, int, Vertex]] = []
    serial = 0
    heappush(queue, (0, serial, center))
    while queue:
        distance, _serial, vertex = heappop(queue)
        if distance != distances[vertex]:
            continue
        if budget is not None and distance > budget:
            continue
        for neighbor, weight in adjacency[vertex].items():
            candidate = distance + weight
            if budget is not None and candidate > budget:
                continue
            previous = distances.get(neighbor)
            if previous is None or candidate < previous:
                distances[neighbor] = candidate
                serial += 1
                heappush(queue, (candidate, serial, neighbor))
    return distances


def weighted_collapse_targets(
    adjacency: WeightedAdjacency, center: Vertex, radius: int
) -> frozenset[Vertex]:
    """Finite target domain reachable within one integer path-cost budget."""
    return frozenset(weighted_shortest_distances(adjacency, center, radius))


def weighted_common_collapse_targets(
    adjacency: WeightedAdjacency,
    left_center: Vertex,
    left_radius: int,
    right_center: Vertex,
    right_radius: int,
) -> frozenset[Vertex]:
    """Shared finite targets of two integer-weight collapse domains."""
    return frozenset(
        weighted_collapse_targets(adjacency, left_center, left_radius).intersection(
            weighted_collapse_targets(adjacency, right_center, right_radius)
        )
    )


def weighted_radius_relation(adjacency: WeightedAdjacency, radius: int) -> Relation:
    """Return R_r={(a,z): z is reachable from a within integer cost r}."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    return frozenset(
        (center, target)
        for center in adjacency
        for target in weighted_collapse_targets(adjacency, center, radius)
    )


def compose_relations(left: Relation, right: Relation) -> Relation:
    """Finite relational composition: (a,c) when some b has a-left-b-right-c."""
    right_by_source: dict[Vertex, set[Vertex]] = {}
    for source, target in right:
        right_by_source.setdefault(source, set()).add(target)
    return frozenset(
        (source, target)
        for source, middle in left
        for target in right_by_source.get(middle, ())
    )
