"""Exact local contact competition among SC, BCC, FCC and HCP in three dimensions.

The comparison is deliberately combinatorial.  It records:

* central primitive coordination;
* the induced contact graph among first-shell directions;
* local common-neighbor context of each primitive center--neighbor bond.

Two candidate filters are exposed but not promoted to physical axioms:

I1. the first-shell direction link is connected, so primitive directions already
    have relative relations at minimum resolution;
I2. every primitive center-edge has the same local common-neighbor graph context,
    so primitive relations are not split into locally distinguishable types.

On the four classical candidate contact structures used here, SC and BCC fail I1,
HCP passes I1 but fails I2, and FCC passes both.  This is a candidate-selection
result for the declared local language, not a proof that physical space is FCC.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass

from .causal_close_packed_contact import (
    BondSignature,
    close_packed_point,
    fcc_registry,
    hcp_registry,
    local_close_packed_points,
    point_neighbors,
    bond_common_neighbor_signature,
)

Point3 = tuple[int, int, int]


@dataclass(frozen=True)
class ContactProfile3D:
    coordination: int
    direction_link_degree_histogram: tuple[tuple[int, int], ...]
    direction_link_edge_count: int
    direction_link_component_sizes: tuple[int, ...]
    bond_context_histogram: tuple[tuple[BondSignature, int], ...]

    @property
    def direction_link_connected(self) -> bool:
        return len(self.direction_link_component_sizes) == 1

    @property
    def edge_context_uniform(self) -> bool:
        return len(self.bond_context_histogram) == 1


def _components(adjacency: dict[Point3, set[Point3]]) -> tuple[int, ...]:
    unseen = set(adjacency)
    sizes = []
    while unseen:
        seed = unseen.pop()
        queue = deque([seed])
        size = 1
        while queue:
            current = queue.popleft()
            for nxt in adjacency[current]:
                if nxt in unseen:
                    unseen.remove(nxt)
                    queue.append(nxt)
                    size += 1
        sizes.append(size)
    return tuple(sorted(sizes, reverse=True))


def _profile_from_points(
    center: Point3,
    points: tuple[Point3, ...],
    adjacent,
) -> ContactProfile3D:
    neighbors = tuple(point for point in points if point != center and adjacent(center, point))
    adjacency = {point: set() for point in neighbors}
    for index, left in enumerate(neighbors):
        for right in neighbors[index + 1 :]:
            if adjacent(left, right):
                adjacency[left].add(right)
                adjacency[right].add(left)
    degree_histogram = tuple(sorted(Counter(len(adjacency[p]) for p in neighbors).items()))
    link_edges = sum(len(adjacency[p]) for p in neighbors) // 2

    context_hist = Counter()
    for neighbor in neighbors:
        common = tuple(
            sorted(
                point
                for point in points
                if point not in (center, neighbor)
                and adjacent(center, point)
                and adjacent(neighbor, point)
            )
        )
        common_adjacency = {point: set() for point in common}
        common_edges = 0
        for index, left in enumerate(common):
            for right in common[index + 1 :]:
                if adjacent(left, right):
                    common_adjacency[left].add(right)
                    common_adjacency[right].add(left)
                    common_edges += 1
        signature = (
            len(common),
            common_edges,
            _components(common_adjacency) if common else (),
            tuple(sorted(len(common_adjacency[p]) for p in common)),
        )
        context_hist[signature] += 1

    return ContactProfile3D(
        coordination=len(neighbors),
        direction_link_degree_histogram=degree_histogram,
        direction_link_edge_count=link_edges,
        direction_link_component_sizes=_components(adjacency),
        bond_context_histogram=tuple(sorted(context_hist.items())),
    )


def simple_cubic_profile() -> ContactProfile3D:
    points = tuple(
        (x, y, z)
        for x in range(-2, 3)
        for y in range(-2, 3)
        for z in range(-2, 3)
    )

    def adjacent(left: Point3, right: Point3) -> bool:
        return sum((a - b) ** 2 for a, b in zip(left, right)) == 1

    return _profile_from_points((0, 0, 0), points, adjacent)


def body_centered_cubic_profile() -> ContactProfile3D:
    # Scale conventional BCC coordinates by two.  Lattice sites then have all
    # coordinates even or all coordinates odd; nearest contacts have squared
    # integer separation three.
    points = tuple(
        (x, y, z)
        for x in range(-5, 6)
        for y in range(-5, 6)
        for z in range(-5, 6)
        if (x & 1) == (y & 1) == (z & 1)
    )

    def adjacent(left: Point3, right: Point3) -> bool:
        return sum((a - b) ** 2 for a, b in zip(left, right)) == 3

    return _profile_from_points((0, 0, 0), points, adjacent)


def _close_packed_profile(registry) -> ContactProfile3D:
    points = local_close_packed_points(registry, 4, 4)
    center = close_packed_point(0, 0, 0, registry)
    neighbors = point_neighbors(center, points)
    adjacency = {point: set() for point in neighbors}
    point_set = set(points)

    from .causal_close_packed_contact import are_close_packed_neighbors

    for index, left in enumerate(neighbors):
        for right in neighbors[index + 1 :]:
            if are_close_packed_neighbors(left, right):
                adjacency[left].add(right)
                adjacency[right].add(left)

    context_hist = Counter(
        bond_common_neighbor_signature(center, neighbor, points)
        for neighbor in neighbors
    )
    return ContactProfile3D(
        coordination=len(neighbors),
        direction_link_degree_histogram=tuple(sorted(Counter(len(adjacency[p]) for p in neighbors).items())),
        direction_link_edge_count=sum(len(adjacency[p]) for p in neighbors) // 2,
        direction_link_component_sizes=_components(adjacency),
        bond_context_histogram=tuple(sorted(context_hist.items())),
    )


def face_centered_cubic_profile() -> ContactProfile3D:
    return _close_packed_profile(fcc_registry)


def hexagonal_close_packed_profile() -> ContactProfile3D:
    return _close_packed_profile(hcp_registry)


def local_candidate_table() -> dict[str, ContactProfile3D]:
    return {
        "SC": simple_cubic_profile(),
        "BCC": body_centered_cubic_profile(),
        "FCC": face_centered_cubic_profile(),
        "HCP": hexagonal_close_packed_profile(),
    }


def candidates_passing_i1_i2() -> tuple[str, ...]:
    table = local_candidate_table()
    return tuple(
        name
        for name, profile in table.items()
        if profile.direction_link_connected and profile.edge_context_uniform
    )
