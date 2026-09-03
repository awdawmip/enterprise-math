"""Connectivity certificates for tetrahedral FCC chirality orientation covers.

A six-bit transition system on K4 defines an eight-state two-sheeted cover.
The cover is connected exactly when the face-holonomy class is non-flat.  In
particular, among the two fully S4-symmetric classes, the flat class is two
disjoint tetrahedra while the all-face-odd class is the cube.
"""

from __future__ import annotations

from collections import deque
from typing import Sequence

from enterprise_math.euler_fcc_chirality import (
    ALL_ODD_FACES,
    ANTIBALANCED_EDGES,
    ZERO_EDGES,
    EdgeBits,
    SignedSlice,
    edge_assignments,
    face_holonomy,
    gauge_action,
    gauges,
    globalizable,
    is_s4_fixed,
    normalize_edges,
    normalize_signed_slice,
    signed_slice_states,
    transition_cover_adjacent,
)


def cover_neighbors(edges: Sequence[int], state: Sequence[int]) -> tuple[SignedSlice, ...]:
    edge_bits = normalize_edges(edges)
    signed_state = normalize_signed_slice(state)
    return tuple(
        candidate
        for candidate in signed_slice_states()
        if transition_cover_adjacent(edge_bits, signed_state, candidate)
    )


def cover_components(edges: Sequence[int]) -> tuple[frozenset[SignedSlice], ...]:
    edge_bits = normalize_edges(edges)
    remaining = set(signed_slice_states())
    components: list[frozenset[SignedSlice]] = []

    while remaining:
        start = min(remaining)
        reached = {start}
        queue: deque[SignedSlice] = deque([start])
        while queue:
            state = queue.popleft()
            for neighbor in cover_neighbors(edge_bits, state):
                if neighbor not in reached:
                    reached.add(neighbor)
                    queue.append(neighbor)
        components.append(frozenset(reached))
        remaining.difference_update(reached)

    return tuple(sorted(components, key=lambda component: min(component)))


def cover_connected(edges: Sequence[int]) -> bool:
    return len(cover_components(edges)) == 1


def cover_distance(
    edges: Sequence[int], start: Sequence[int], target: Sequence[int]
) -> int | None:
    edge_bits = normalize_edges(edges)
    source = normalize_signed_slice(start)
    destination = normalize_signed_slice(target)
    queue: deque[tuple[SignedSlice, int]] = deque([(source, 0)])
    reached = {source}

    while queue:
        state, distance = queue.popleft()
        if state == destination:
            return distance
        for neighbor in cover_neighbors(edge_bits, state):
            if neighbor not in reached:
                reached.add(neighbor)
                queue.append((neighbor, distance + 1))
    return None


def cover_diameter(edges: Sequence[int]) -> int | None:
    edge_bits = normalize_edges(edges)
    if not cover_connected(edge_bits):
        return None
    states = tuple(signed_slice_states())
    distances = [
        cover_distance(edge_bits, left, right)
        for left in states
        for right in states
    ]
    if any(distance is None for distance in distances):
        raise AssertionError("connected cover produced an unreachable pair")
    return max(distance for distance in distances if distance is not None)


def gauge_cover_relabel(
    state: Sequence[int], gauge: Sequence[int]
) -> SignedSlice:
    slice_index, sheet = normalize_signed_slice(state)
    gauge_bits = tuple(gauge)
    if len(gauge_bits) != 4 or any(bit not in (0, 1) for bit in gauge_bits):
        raise ValueError("gauge must contain four bits")
    return slice_index, sheet ^ int(gauge_bits[slice_index])


def verify_connectivity_classification() -> dict[str, object]:
    all_edges = tuple(edge_assignments())

    for edges in all_edges:
        if cover_connected(edges) == globalizable(edges):
            raise AssertionError("cover connectivity is not the complement of flatness")
        component_sizes = tuple(sorted(len(component) for component in cover_components(edges)))
        if globalizable(edges):
            if component_sizes != (4, 4):
                raise AssertionError("flat cover is not two four-vertex components")
        elif component_sizes != (8,):
            raise AssertionError("non-flat cover is not connected")

        for gauge in gauges():
            transformed = gauge_action(edges, gauge)
            if tuple(sorted(map(len, cover_components(transformed)))) != component_sizes:
                raise AssertionError("cover component sizes changed under gauge")

    symmetric_edges = tuple(
        edges for edges in all_edges if is_s4_fixed(face_holonomy(edges))
    )
    connected_symmetric = tuple(
        edges for edges in symmetric_edges if cover_connected(edges)
    )
    if len(symmetric_edges) != 16 or len(connected_symmetric) != 8:
        raise AssertionError("unexpected symmetric connectivity counts")
    if any(face_holonomy(edges) != ALL_ODD_FACES for edges in connected_symmetric):
        raise AssertionError("connected symmetric cover did not select all-face-odd")

    if tuple(sorted(map(len, cover_components(ZERO_EDGES)))) != (4, 4):
        raise AssertionError("zero transition cover is not two tetrahedra")
    if tuple(sorted(map(len, cover_components(ANTIBALANCED_EDGES)))) != (8,):
        raise AssertionError("antibalanced transition cover is not connected")

    return {
        "edge_assignments_checked": len(all_edges),
        "flat_disconnected_assignments": sum(globalizable(edges) for edges in all_edges),
        "nonflat_connected_assignments": sum(
            not globalizable(edges) for edges in all_edges
        ),
        "flat_component_sizes": [4, 4],
        "antibalanced_component_sizes": [8],
        "antibalanced_diameter": cover_diameter(ANTIBALANCED_EDGES),
        "fully_symmetric_assignments": len(symmetric_edges),
        "connected_fully_symmetric_assignments": len(connected_symmetric),
        "selection_theorem": "full S4 symmetry plus connected cover selects face holonomy 1111",
    }


if __name__ == "__main__":
    import json

    print(json.dumps(verify_connectivity_classification(), indent=2, sort_keys=True))
