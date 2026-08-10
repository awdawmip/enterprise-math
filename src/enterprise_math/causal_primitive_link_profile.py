"""Family-independent integer profiles for primitive-direction causal links.

A primitive direction set is represented by integer displacement vectors.  Two
directions alpha,beta are locally compatible when beta-alpha is again primitive.
The induced graph on primitive directions is the first causal link around the
origin.  This module intentionally avoids Euclidean angles and packing-density
scores.

For a compatible r-flag (an r-clique in the direction link), the extension count
is the number of primitive directions that remain compatible with every member of
the flag.  Histograms of these counts are exact finite continuation signatures:
if a histogram is a singleton, all r-flags have the same one-step continuation
capacity; the first non-singleton histogram marks a genuine higher-order local
context split.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from itertools import combinations, product

Vector = tuple[int, ...]
Adjacency = dict[Vector, frozenset[Vector]]


def _subtract(left: Vector, right: Vector) -> Vector:
    return tuple(a - b for a, b in zip(left, right))


def primitive_direction_graph(roots: tuple[Vector, ...]) -> Adjacency:
    if not roots or len(set(roots)) != len(roots):
        raise ValueError("roots must be a non-empty tuple of distinct vectors")
    dimension = len(roots[0])
    if any(len(root) != dimension for root in roots):
        raise ValueError("all roots must have the same coordinate length")
    root_set = set(roots)
    adjacency = {root: set() for root in roots}
    for index, left in enumerate(roots):
        for right in roots[index + 1 :]:
            if _subtract(right, left) in root_set:
                adjacency[left].add(right)
                adjacency[right].add(left)
    return {root: frozenset(neighbors) for root, neighbors in adjacency.items()}


def component_sizes(adjacency: Adjacency) -> tuple[int, ...]:
    unseen = set(adjacency)
    sizes = []
    while unseen:
        seed = next(iter(unseen))
        unseen.remove(seed)
        queue = deque([seed])
        size = 0
        while queue:
            current = queue.popleft()
            size += 1
            for nxt in adjacency[current]:
                if nxt in unseen:
                    unseen.remove(nxt)
                    queue.append(nxt)
        sizes.append(size)
    return tuple(sorted(sizes, reverse=True))


def graph_diameter(adjacency: Adjacency) -> int | None:
    if len(component_sizes(adjacency)) != 1:
        return None
    diameter = 0
    for source in adjacency:
        distance = {source: 0}
        queue = deque([source])
        while queue:
            current = queue.popleft()
            for nxt in adjacency[current]:
                if nxt in distance:
                    continue
                distance[nxt] = distance[current] + 1
                queue.append(nxt)
        diameter = max(diameter, max(distance.values()))
    return diameter


def edge_count(adjacency: Adjacency) -> int:
    return sum(len(neighbors) for neighbors in adjacency.values()) // 2


def neighborhood_signature(adjacency: Adjacency, vertex: Vector) -> tuple:
    neighbors = tuple(adjacency[vertex])
    local = {
        neighbor: frozenset(adjacency[neighbor].intersection(neighbors))
        for neighbor in neighbors
    }
    degree_histogram = tuple(sorted(Counter(len(local[v]) for v in local).items()))
    return (
        len(neighbors),
        edge_count(local),
        degree_histogram,
        component_sizes(local),
        graph_diameter(local),
    )


def edge_context_histogram(adjacency: Adjacency) -> dict[tuple, int]:
    return dict(Counter(neighborhood_signature(adjacency, vertex) for vertex in adjacency))


def pair_context_histogram(adjacency: Adjacency) -> dict[tuple[int, int], int]:
    """Histogram of (link distance, common-neighbor count) on unordered pairs."""
    vertices = tuple(adjacency)
    histogram = Counter()
    for index, source in enumerate(vertices):
        distance = {source: 0}
        queue = deque([source])
        while queue:
            current = queue.popleft()
            for nxt in adjacency[current]:
                if nxt in distance:
                    continue
                distance[nxt] = distance[current] + 1
                queue.append(nxt)
        for target in vertices[index + 1 :]:
            d = distance.get(target)
            if d is None:
                continue
            histogram[(d, len(adjacency[source].intersection(adjacency[target])))] += 1
    return dict(sorted(histogram.items()))


def _clique_extension_histograms(adjacency: Adjacency) -> tuple[dict[int, int], ...]:
    """Extension-count histograms for all clique sizes until no larger clique exists."""
    vertices = tuple(adjacency)
    order = {vertex: index for index, vertex in enumerate(vertices)}
    cliques = [((vertex,), set(adjacency[vertex])) for vertex in vertices]
    result = []
    while cliques:
        result.append(dict(sorted(Counter(len(common) for _, common in cliques).items())))
        next_cliques = []
        for clique, common in cliques:
            last = order[clique[-1]]
            candidates = sorted((v for v in common if order[v] > last), key=order.get)
            for vertex in candidates:
                next_cliques.append((clique + (vertex,), common.intersection(adjacency[vertex])))
        cliques = next_cliques
    return tuple(result)


def first_flag_split_order(flag_histograms: tuple[dict[int, int], ...]) -> int | None:
    for size, histogram in enumerate(flag_histograms, start=1):
        if len(histogram) > 1:
            return size
    return None


@dataclass(frozen=True)
class PrimitiveLinkProfile:
    primitive_count: int
    link_degree_histogram: tuple[tuple[int, int], ...]
    link_edge_count: int
    link_component_sizes: tuple[int, ...]
    link_diameter: int | None
    edge_context_histogram: tuple[tuple[tuple, int], ...]
    pair_context_histogram: tuple[tuple[tuple[int, int], int], ...]
    flag_extension_histograms: tuple[tuple[tuple[int, int], ...], ...]
    first_flag_split_order: int | None
    maximum_flag_size: int


def primitive_link_profile(roots: tuple[Vector, ...]) -> PrimitiveLinkProfile:
    adjacency = primitive_direction_graph(roots)
    flag_histograms = _clique_extension_histograms(adjacency)
    return PrimitiveLinkProfile(
        primitive_count=len(roots),
        link_degree_histogram=tuple(sorted(Counter(len(adjacency[v]) for v in adjacency).items())),
        link_edge_count=edge_count(adjacency),
        link_component_sizes=component_sizes(adjacency),
        link_diameter=graph_diameter(adjacency),
        edge_context_histogram=tuple(sorted(edge_context_histogram(adjacency).items(), key=repr)),
        pair_context_histogram=tuple(pair_context_histogram(adjacency).items()),
        flag_extension_histograms=tuple(tuple(hist.items()) for hist in flag_histograms),
        first_flag_split_order=first_flag_split_order(flag_histograms),
        maximum_flag_size=len(flag_histograms),
    )


def a_roots(p: int) -> tuple[Vector, ...]:
    if isinstance(p, bool) or not isinstance(p, int) or p < 1:
        raise ValueError("p must be a positive integer")
    count = p + 1
    roots = []
    for tail in range(count):
        for head in range(count):
            if tail == head:
                continue
            vector = [0] * count
            vector[tail] = 1
            vector[head] = -1
            roots.append(tuple(vector))
    return tuple(roots)


def d_roots(rank: int) -> tuple[Vector, ...]:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 3:
        raise ValueError("D rank must be an integer at least three")
    roots = []
    for left, right in combinations(range(rank), 2):
        for sign_left in (-1, 1):
            for sign_right in (-1, 1):
                vector = [0] * rank
                vector[left] = sign_left
                vector[right] = sign_right
                roots.append(tuple(vector))
    return tuple(roots)


def e8_scaled_roots() -> tuple[Vector, ...]:
    """E8 roots scaled by two so every coordinate is integral."""
    roots = []
    for left, right in combinations(range(8), 2):
        for sign_left in (-2, 2):
            for sign_right in (-2, 2):
                vector = [0] * 8
                vector[left] = sign_left
                vector[right] = sign_right
                roots.append(tuple(vector))
    for signs in product((-1, 1), repeat=8):
        if sum(value == -1 for value in signs) % 2 == 0:
            roots.append(tuple(signs))
    if len(roots) != 240 or len(set(roots)) != 240:
        raise AssertionError("scaled E8 construction must contain 240 distinct roots")
    return tuple(roots)


def _dot(left: Vector, right: Vector) -> int:
    return sum(a * b for a, b in zip(left, right))


def e7_scaled_roots() -> tuple[Vector, ...]:
    roots = tuple(root for root in e8_scaled_roots() if _dot(root, (1,) * 8) == 0)
    if len(roots) != 126:
        raise AssertionError("E7 subsystem must contain 126 roots")
    return roots


def e6_scaled_roots() -> tuple[Vector, ...]:
    selector = (1, 1, 1, 1, 1, 1, -3, -3)
    roots = tuple(root for root in e7_scaled_roots() if _dot(root, selector) == 0)
    if len(roots) != 72:
        raise AssertionError("E6 subsystem must contain 72 roots")
    return roots
