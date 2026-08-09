"""Pure integer primitive-direction diagnostics for the E8 root system.

Scale the standard E8 roots by two to avoid half-integers.  The 240 scaled roots
are:

- 112 vectors with exactly two nonzero coordinates, each +/-2;
- 128 vectors with all coordinates +/-1 and an even number of minus signs.

Two root directions are adjacent when their difference is another scaled root.
The resulting E8 root link has 240 vertices, degree 56, and 6720 edges.  For a
fixed primitive edge, the 56 common neighbors induce a connected 27-regular graph
with 756 edges.  All computations are exact integer membership tests.

The existence and 240-root structure of E8 are established prior art.  The use
here is a pressure test showing that A_p local-isotropy diagnostics do not select
the A-family universally.
"""

from __future__ import annotations

from collections import Counter, deque
from itertools import combinations, product

Vector = tuple[int, ...]


def e8_scaled_roots() -> tuple[Vector, ...]:
    roots = []
    for first, second in combinations(range(8), 2):
        for first_value in (-2, 2):
            for second_value in (-2, 2):
                vector = [0] * 8
                vector[first] = first_value
                vector[second] = second_value
                roots.append(tuple(vector))
    for signs in product((-1, 1), repeat=8):
        if sum(1 for value in signs if value == -1) % 2 == 0:
            roots.append(tuple(signs))
    result = tuple(roots)
    if len(result) != 240 or len(set(result)) != 240:
        raise AssertionError("scaled E8 root construction must produce 240 unique roots")
    return result


def _subtract(left: Vector, right: Vector) -> Vector:
    return tuple(a - b for a, b in zip(left, right))


def e8_root_count() -> int:
    return 240


def e8_direction_link_degree() -> int:
    roots = e8_scaled_roots()
    root_set = set(roots)
    fixed = roots[0]
    return sum(1 for root in roots if root != fixed and _subtract(root, fixed) in root_set)


def e8_direction_link_edge_count() -> int:
    return e8_root_count() * e8_direction_link_degree() // 2


def e8_direction_link_connected() -> bool:
    roots = e8_scaled_roots()
    root_set = set(roots)
    adjacency = {root: set() for root in roots}
    for index, left in enumerate(roots):
        for right in roots[index + 1 :]:
            if _subtract(right, left) in root_set:
                adjacency[left].add(right)
                adjacency[right].add(left)
    seen = {roots[0]}
    queue = deque([roots[0]])
    while queue:
        current = queue.popleft()
        for nxt in adjacency[current]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return len(seen) == len(roots)


def e8_edge_common_neighbor_signature(
    direction: Vector | None = None,
) -> tuple[int, int, tuple[int, ...], tuple[tuple[int, int], ...]]:
    """(#common, #internal edges, component sizes, induced-degree histogram)."""
    roots = e8_scaled_roots()
    root_set = set(roots)
    if direction is None:
        direction = roots[0]
    if direction not in root_set:
        raise ValueError("direction must be a scaled E8 root")
    common = tuple(
        root
        for root in roots
        if root != direction and _subtract(root, direction) in root_set
    )
    adjacency = {root: set() for root in common}
    edge_count = 0
    for index, left in enumerate(common):
        for right in common[index + 1 :]:
            if _subtract(right, left) in root_set:
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
    degree_histogram = tuple(sorted(Counter(len(adjacency[root]) for root in common).items()))
    return (
        len(common),
        edge_count,
        tuple(sorted(component_sizes, reverse=True)),
        degree_histogram,
    )


def e8_all_edge_contexts_uniform() -> bool:
    signatures = {
        e8_edge_common_neighbor_signature(root)
        for root in e8_scaled_roots()
    }
    return len(signatures) == 1
