"""Exact integer close-packed contact graphs for FCC/HCP causal diagnostics.

The model uses triangular-layer coordinates scaled by three.  A layer registry
s in {0,1,2} places an in-plane site at (3u+s, 3v+s).  With layer index z,
the integer contact form

    d2 = dx^2 + dy^2 + dx*dy + 6*dz^2

has nearest-neighbor contact exactly at d2=9 for ideal close-packed layers.
No floating-point coordinates or Euclidean square roots are used.

FCC uses ABCABC... registries s=z mod 3.  HCP uses ABAB... registries s=z mod 2.
For a central site, every nearest-neighbor bond has four common neighbors and
two common-neighbor bonds.  FCC has one local relation context: two disjoint
common-neighbor edges, component sizes (2,2).  HCP splits into two contexts:
six (2,2) bonds and six (3,1) bonds.  This is the graph-theoretic distinction
behind ideal 421 versus 422 common-neighbor environments.

These are local combinatorial diagnostics only; they do not prove a unique
physical minimum-precision ontology.
"""

from __future__ import annotations

from collections import Counter, deque
from typing import Callable

Point = tuple[int, int, int]
Registry = Callable[[int], int]
BondSignature = tuple[int, int, tuple[int, ...], tuple[int, ...]]


def fcc_registry(layer: int) -> int:
    return layer % 3


def hcp_registry(layer: int) -> int:
    return layer % 2


def close_packed_point(u: int, v: int, layer: int, registry: Registry) -> Point:
    shift = registry(layer)
    return 3 * u + shift, 3 * v + shift, layer


def close_packed_distance_form(left: Point, right: Point) -> int:
    dx = left[0] - right[0]
    dy = left[1] - right[1]
    dz = left[2] - right[2]
    return dx * dx + dy * dy + dx * dy + 6 * dz * dz


def are_close_packed_neighbors(left: Point, right: Point) -> bool:
    return left != right and close_packed_distance_form(left, right) == 9


def local_close_packed_points(
    registry: Registry,
    in_plane_radius: int = 3,
    layer_radius: int = 3,
) -> tuple[Point, ...]:
    if in_plane_radius < 1 or layer_radius < 1:
        raise ValueError("local radii must be positive")
    return tuple(
        close_packed_point(u, v, layer, registry)
        for layer in range(-layer_radius, layer_radius + 1)
        for u in range(-in_plane_radius, in_plane_radius + 1)
        for v in range(-in_plane_radius, in_plane_radius + 1)
    )


def point_neighbors(point: Point, points: tuple[Point, ...]) -> tuple[Point, ...]:
    return tuple(candidate for candidate in points if are_close_packed_neighbors(point, candidate))


def bond_common_neighbor_signature(
    center: Point,
    neighbor: Point,
    points: tuple[Point, ...],
) -> BondSignature:
    if not are_close_packed_neighbors(center, neighbor):
        raise ValueError("center and neighbor must form a primitive contact bond")
    common = tuple(
        sorted(set(point_neighbors(center, points)) & set(point_neighbors(neighbor, points)))
    )
    adjacency = {point: set() for point in common}
    edge_count = 0
    for index, left in enumerate(common):
        for right in common[index + 1 :]:
            if are_close_packed_neighbors(left, right):
                adjacency[left].add(right)
                adjacency[right].add(left)
                edge_count += 1

    components = []
    unseen = set(common)
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
        components.append(size)

    degrees = tuple(sorted(len(adjacency[point]) for point in common))
    return len(common), edge_count, tuple(sorted(components, reverse=True)), degrees


def central_bond_signature_histogram(registry: Registry) -> dict[BondSignature, int]:
    points = local_close_packed_points(registry, 4, 4)
    center = close_packed_point(0, 0, 0, registry)
    neighbors = point_neighbors(center, points)
    if len(neighbors) != 12:
        raise AssertionError("ideal close-packed center must have twelve primitive contacts")
    return dict(
        Counter(
            bond_common_neighbor_signature(center, neighbor, points)
            for neighbor in neighbors
        )
    )


def fcc_bond_signature_histogram() -> dict[BondSignature, int]:
    return central_bond_signature_histogram(fcc_registry)


def hcp_bond_signature_histogram() -> dict[BondSignature, int]:
    return central_bond_signature_histogram(hcp_registry)


def fcc_bonds_are_single_context() -> bool:
    return fcc_bond_signature_histogram() == {
        (4, 2, (2, 2), (1, 1, 1, 1)): 12
    }


def hcp_bonds_split_into_two_contexts() -> bool:
    return hcp_bond_signature_histogram() == {
        (4, 2, (2, 2), (1, 1, 1, 1)): 6,
        (4, 2, (3, 1), (0, 1, 1, 2)): 6,
    }
