"""Pure combinatorial nearest-neighbor graphs for FCC/HCP close-packed stacking.

Each triangular layer uses integer axial A2 coordinates.  Layer registry changes
are encoded only by the relative close-packed step +/-1 from the F/H stacking
law.  In-plane adjacency has the six A2 primitive shifts.  Between consecutive
layers, each site has three neighbors determined by the orientation of the
registry step.  No Euclidean coordinate, angle, or distance formula is used.

The resulting origin first-shell link has the same coarse statistics for ideal
FCC and HCP: 12 vertices, 24 edges, 4-regular, connected, with eight triangles.
The next local context separates them.  Every FCC origin bond has common-neighbor
signature (4,2,(2,2)); HCP has six such bonds and six (4,2,(3,1)) bonds.  In this
integer model the latter six are exactly the in-plane HCP bonds.

These signatures are the graph content traditionally labelled CNA 421 and 422,
but the derivation here is internal to the causal stacking adjacency.
"""

from __future__ import annotations

from collections import Counter, deque
from itertools import combinations

Node = tuple[int, int, int]  # (layer, axial_i, axial_j)
BondSignature = tuple[int, int, tuple[int, ...]]

TRIANGULAR_SHIFTS = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, -1),
    (-1, 1),
)

# From a lower layer to an upper layer.  Relative registry step +1 and -1 use
# opposite triangular-hole incidence patterns.
UP_PLUS = ((0, 0), (-1, 0), (0, -1))
UP_MINUS = ((0, 0), (1, 0), (0, 1))


def fcc_registry(layer: int) -> int:
    return layer % 3


def hcp_registry(layer: int) -> int:
    return layer % 2


def _relative_registry_step(registry, layer: int) -> int:
    residue = (registry(layer + 1) - registry(layer)) % 3
    if residue == 1:
        return 1
    if residue == 2:
        return -1
    raise AssertionError("adjacent close-packed layers must use distinct registries")


def close_packed_neighbors(node: Node, stacking: str) -> frozenset[Node]:
    if stacking == "fcc":
        registry = fcc_registry
    elif stacking == "hcp":
        registry = hcp_registry
    else:
        raise ValueError("stacking must be 'fcc' or 'hcp'")

    layer, first, second = node
    neighbors: set[Node] = set()
    for di, dj in TRIANGULAR_SHIFTS:
        neighbors.add((layer, first + di, second + dj))

    up_step = _relative_registry_step(registry, layer)
    up_shifts = UP_PLUS if up_step == 1 else UP_MINUS
    for di, dj in up_shifts:
        neighbors.add((layer + 1, first + di, second + dj))

    down_step = _relative_registry_step(registry, layer - 1)
    down_shifts = UP_PLUS if down_step == 1 else UP_MINUS
    # Invert the lower->upper incidence relation.
    for di, dj in down_shifts:
        neighbors.add((layer - 1, first - di, second - dj))

    if len(neighbors) != 12:
        raise AssertionError("ideal close-packed site must have twelve primitive neighbors")
    return frozenset(neighbors)


def origin_direction_link_signature(stacking: str) -> tuple[int, int, tuple[tuple[int, int], ...], int, tuple[int, ...]]:
    origin = (0, 0, 0)
    shell = set(close_packed_neighbors(origin, stacking))
    adjacency = {node: set() for node in shell}
    edge_count = 0
    triangle_count = 0

    for left, right in combinations(shell, 2):
        if right in close_packed_neighbors(left, stacking):
            adjacency[left].add(right)
            adjacency[right].add(left)
            edge_count += 1

    for first, second, third in combinations(shell, 3):
        if (
            second in adjacency[first]
            and third in adjacency[first]
            and third in adjacency[second]
        ):
            triangle_count += 1

    unseen = set(shell)
    component_sizes = []
    while unseen:
        seed = unseen.pop()
        component = {seed}
        queue = deque([seed])
        while queue:
            current = queue.popleft()
            for nxt in adjacency[current]:
                if nxt in unseen:
                    unseen.remove(nxt)
                    component.add(nxt)
                    queue.append(nxt)
        component_sizes.append(len(component))

    degree_histogram = tuple(sorted(Counter(len(adjacency[node]) for node in shell).items()))
    return (
        len(shell),
        edge_count,
        degree_histogram,
        triangle_count,
        tuple(sorted(component_sizes, reverse=True)),
    )


def origin_bond_common_neighbor_signature(neighbor: Node, stacking: str) -> BondSignature:
    origin = (0, 0, 0)
    if neighbor not in close_packed_neighbors(origin, stacking):
        raise ValueError("neighbor must be a primitive origin neighbor")
    common = set(close_packed_neighbors(origin, stacking)) & set(
        close_packed_neighbors(neighbor, stacking)
    )
    adjacency = {node: set() for node in common}
    edge_count = 0
    for left, right in combinations(common, 2):
        if right in close_packed_neighbors(left, stacking):
            adjacency[left].add(right)
            adjacency[right].add(left)
            edge_count += 1

    unseen = set(common)
    component_sizes = []
    while unseen:
        seed = unseen.pop()
        component = {seed}
        queue = deque([seed])
        while queue:
            current = queue.popleft()
            for nxt in adjacency[current]:
                if nxt in unseen:
                    unseen.remove(nxt)
                    component.add(nxt)
                    queue.append(nxt)
        component_sizes.append(len(component))

    return len(common), edge_count, tuple(sorted(component_sizes, reverse=True))


def origin_bond_context_histogram(stacking: str) -> dict[BondSignature, int]:
    origin = (0, 0, 0)
    histogram = Counter(
        origin_bond_common_neighbor_signature(neighbor, stacking)
        for neighbor in close_packed_neighbors(origin, stacking)
    )
    return dict(histogram)


def origin_bond_context_by_layer_offset(stacking: str) -> dict[tuple[int, BondSignature], int]:
    origin = (0, 0, 0)
    histogram = Counter()
    for neighbor in close_packed_neighbors(origin, stacking):
        offset = neighbor[0] - origin[0]
        histogram[(offset, origin_bond_common_neighbor_signature(neighbor, stacking))] += 1
    return dict(histogram)


def fcc_hcp_first_link_indistinguishable_by_coarse_counts() -> bool:
    return origin_direction_link_signature("fcc") == origin_direction_link_signature("hcp")


def fcc_hcp_edge_contexts_distinguish() -> bool:
    return origin_bond_context_histogram("fcc") != origin_bond_context_histogram("hcp")
