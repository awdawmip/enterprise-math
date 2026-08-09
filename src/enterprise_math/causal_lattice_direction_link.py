"""Pure integer local-direction invariants for candidate minimum-precision lattices.

For the A_p root lattice, primitive moves are roots e_i-e_j on n=p+1 slots.
Represent a direction by the ordered pair (i,j).  Two first-shell directions are
adjacent in the induced primitive graph exactly when they share a tail or share
a head.  The resulting direction link has p(p+1) vertices, degree 2(p-1), and is
connected for p>=2.

For a fixed primitive edge 0--(e_i-e_j), its common neighbors split into two
disjoint cliques K_(p-1): roots e_i-e_k and e_k-e_j.  At p=3 this gives four
common neighbors with two disjoint bonds, the graph-theoretic 421 common-neighbor
pattern of FCC.

The standard-axis Z^p nearest-neighbor graph is a useful pressure-test baseline:
its first-shell directions are +/-e_i and no two are primitive-neighbor adjacent,
so its direction link is edgeless.

Higher-shell stabilizer orbit counts are also exposed as a pressure test.  They
do NOT favor A_p uniformly: at radius two, A_3 has three coordinate-multiset
orbit types while Z^3 has only two.  Therefore simple orbit-count minimization is
not a valid standalone isotropy principle.
"""

from __future__ import annotations

from collections import Counter, deque
from itertools import product
from math import comb

Direction = tuple[int, int]
Vector = tuple[int, ...]
Edge = tuple[Direction, Direction]


def a_directions(p: int) -> tuple[Direction, ...]:
    if isinstance(p, bool) or not isinstance(p, int) or p < 1:
        raise ValueError("p must be a positive integer")
    n = p + 1
    return tuple((tail, head) for tail in range(n) for head in range(n) if tail != head)


def a_direction_adjacent(left: Direction, right: Direction) -> bool:
    if left == right:
        return False
    return left[0] == right[0] or left[1] == right[1]


def a_direction_link_edges(p: int) -> tuple[Edge, ...]:
    directions = a_directions(p)
    edges = []
    for index, left in enumerate(directions):
        for right in directions[index + 1 :]:
            if a_direction_adjacent(left, right):
                edges.append((left, right))
    return tuple(edges)


def a_direction_link_degree(p: int) -> int:
    if p < 1:
        raise ValueError("p must be positive")
    return 2 * (p - 1)


def a_direction_link_edge_count(p: int) -> int:
    if p < 1:
        raise ValueError("p must be positive")
    return (p + 1) * p * (p - 1)


def a_direction_link_connected(p: int) -> bool:
    directions = a_directions(p)
    if len(directions) <= 1:
        return True
    adjacency = {direction: set() for direction in directions}
    for left, right in a_direction_link_edges(p):
        adjacency[left].add(right)
        adjacency[right].add(left)
    seen = {directions[0]}
    queue = deque([directions[0]])
    while queue:
        current = queue.popleft()
        for nxt in adjacency[current]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return len(seen) == len(directions)


def a_direction_link_diameter(p: int) -> int | None:
    directions = a_directions(p)
    edges = a_direction_link_edges(p)
    adjacency = {direction: set() for direction in directions}
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    if not a_direction_link_connected(p):
        return None
    diameter = 0
    for source in directions:
        distances = {source: 0}
        queue = deque([source])
        while queue:
            current = queue.popleft()
            for nxt in adjacency[current]:
                if nxt in distances:
                    continue
                distances[nxt] = distances[current] + 1
                queue.append(nxt)
        diameter = max(diameter, max(distances.values()))
    return diameter


def a_link_triangle_count(p: int) -> int:
    """Triangles in the direction link: row-cliques plus column-cliques."""
    if p < 1:
        raise ValueError("p must be positive")
    n = p + 1
    return 2 * n * comb(n - 1, 3) if n - 1 >= 3 else 0


def a_link_induced_rectangle_count(p: int) -> int:
    """Chordless row/column rectangles with disjoint row and column index pairs."""
    if p < 1:
        raise ValueError("p must be positive")
    n = p + 1
    return comb(n, 2) * comb(n - 2, 2) if n >= 4 else 0


def a_edge_common_neighbor_directions(
    p: int,
    direction: Direction,
) -> tuple[Direction, ...]:
    directions = set(a_directions(p))
    if direction not in directions:
        raise ValueError("direction must be a primitive A_p root direction")
    tail, head = direction
    n = p + 1
    return tuple(
        [(tail, k) for k in range(n) if k not in (tail, head)]
        + [(k, head) for k in range(n) if k not in (tail, head)]
    )


def a_edge_common_neighbor_graph_signature(
    p: int,
    direction: Direction,
) -> tuple[int, int, tuple[int, ...]]:
    """Return (#common neighbors, #internal edges, component sizes)."""
    common = a_edge_common_neighbor_directions(p, direction)
    adjacency = {vertex: set() for vertex in common}
    edge_count = 0
    for index, left in enumerate(common):
        for right in common[index + 1 :]:
            if a_direction_adjacent(left, right):
                adjacency[left].add(right)
                adjacency[right].add(left)
                edge_count += 1
    sizes = []
    unseen = set(common)
    while unseen:
        seed = next(iter(unseen))
        component = {seed}
        queue = deque([seed])
        unseen.remove(seed)
        while queue:
            current = queue.popleft()
            for nxt in adjacency[current]:
                if nxt in unseen:
                    unseen.remove(nxt)
                    component.add(nxt)
                    queue.append(nxt)
        sizes.append(len(component))
    return len(common), edge_count, tuple(sorted(sizes, reverse=True))


def a_all_edge_contexts_uniform(p: int) -> bool:
    signatures = {
        a_edge_common_neighbor_graph_signature(p, direction)
        for direction in a_directions(p)
    }
    return len(signatures) == 1


def z_direction_count(p: int) -> int:
    if isinstance(p, bool) or not isinstance(p, int) or p < 1:
        raise ValueError("p must be a positive integer")
    return 2 * p


def z_direction_link_edge_count(p: int) -> int:
    if p < 1:
        raise ValueError("p must be positive")
    return 0


def z_direction_link_connected(p: int) -> bool:
    return z_direction_count(p) <= 1


def _partition(values) -> tuple[int, ...]:
    return tuple(sorted((value for value in values if value > 0), reverse=True))


def z_shell_orbit_type(vector: Vector) -> tuple[int, ...]:
    return _partition(abs(value) for value in vector)


def a_shell_orbit_type(vector: Vector) -> tuple[tuple[int, ...], tuple[int, ...]]:
    if sum(vector) != 0:
        raise ValueError("A_p shell vector must have zero coordinate sum")
    positive = _partition(value for value in vector if value > 0)
    negative = _partition(-value for value in vector if value < 0)
    return tuple(sorted((positive, negative)))


def z_shell_orbit_histogram(p: int, radius: int) -> dict[tuple[int, ...], int]:
    if p < 1 or radius < 0:
        raise ValueError("p must be positive and radius non-negative")
    histogram = Counter()
    for vector in product(range(-radius, radius + 1), repeat=p):
        if sum(abs(value) for value in vector) == radius:
            histogram[z_shell_orbit_type(vector)] += 1
    return dict(histogram)


def a_shell_orbit_histogram(
    p: int,
    radius: int,
) -> dict[tuple[tuple[int, ...], tuple[int, ...]], int]:
    if p < 1 or radius < 0:
        raise ValueError("p must be positive and radius non-negative")
    n = p + 1
    histogram = Counter()
    for vector in product(range(-radius, radius + 1), repeat=n):
        if sum(vector) != 0:
            continue
        if sum(value for value in vector if value > 0) != radius:
            continue
        histogram[a_shell_orbit_type(vector)] += 1
    return dict(histogram)
