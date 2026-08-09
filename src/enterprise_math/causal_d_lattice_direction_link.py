"""Pure integer direction-link pressure test for the D_n root lattice.

D_n primitive roots are all signed coordinate pairs +/-e_i +/-e_j.  This module
uses only integer vectors and root differences: two primitive directions are
adjacent when their difference is again a primitive D_n root.

For n>=3, every root has 4(n-2) adjacent primitive directions.  D_3 reproduces
the A_3/FCC local counts.  D_4 already provides a higher-dimensional competitor
to A_4: 24 primitive directions, direction-link degree 8, and a uniform
8-common-neighbor edge context whose induced graph is connected with 12 edges.
Thus direction-link connectedness and edge-context uniformity do not uniquely
select the A_n family in higher dimension.
"""

from __future__ import annotations

from collections import deque
from itertools import combinations

Vector = tuple[int, ...]


def d_roots(n: int) -> tuple[Vector, ...]:
    if isinstance(n, bool) or not isinstance(n, int) or n < 3:
        raise ValueError("n must be an integer at least three")
    roots = []
    for first, second in combinations(range(n), 2):
        for first_sign in (-1, 1):
            for second_sign in (-1, 1):
                vector = [0] * n
                vector[first] = first_sign
                vector[second] = second_sign
                roots.append(tuple(vector))
    return tuple(roots)


def d_root_count(n: int) -> int:
    if n < 3:
        raise ValueError("n must be at least three")
    return 2 * n * (n - 1)


def _subtract(left: Vector, right: Vector) -> Vector:
    return tuple(a - b for a, b in zip(left, right))


def d_direction_adjacent(left: Vector, right: Vector, n: int) -> bool:
    if left == right:
        return False
    roots = set(d_roots(n))
    return _subtract(right, left) in roots


def d_direction_link_degree(n: int) -> int:
    if n < 3:
        raise ValueError("n must be at least three")
    return 4 * (n - 2)


def d_direction_link_edge_count(n: int) -> int:
    return d_root_count(n) * d_direction_link_degree(n) // 2


def d_direction_link_connected(n: int) -> bool:
    roots = d_roots(n)
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


def d_edge_common_neighbor_signature(
    n: int,
    direction: Vector,
) -> tuple[int, int, tuple[int, ...]]:
    roots = d_roots(n)
    root_set = set(roots)
    if direction not in root_set:
        raise ValueError("direction must be a primitive D_n root")
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
    sizes = []
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
        sizes.append(len(component))
    return len(common), edge_count, tuple(sorted(sizes, reverse=True))


def d_all_edge_contexts_uniform(n: int) -> bool:
    signatures = {
        d_edge_common_neighbor_signature(n, root)
        for root in d_roots(n)
    }
    return len(signatures) == 1


def d_expected_common_neighbor_count(n: int) -> int:
    if n < 3:
        raise ValueError("n must be at least three")
    return 4 * (n - 2)


def d_expected_common_neighbor_internal_edges(n: int) -> int:
    if n < 3:
        raise ValueError("n must be at least three")
    return 2 * (n - 2) * (2 * n - 5)
