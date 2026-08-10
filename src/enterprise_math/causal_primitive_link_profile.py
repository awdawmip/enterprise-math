"""Family-independent integer profiles for primitive-direction causal links.

A primitive direction set is represented by integer displacement vectors. Two
directions alpha,beta are locally compatible when beta-alpha is again primitive.
The induced graph on primitive directions is the first causal link around the
origin. This module intentionally avoids Euclidean angles and packing-density
scores.

Compatible flags grow only by adjoining another direction compatible with every
current member. Hence their continuation language is acyclic in flag size. This
allows exact finite-horizon future signatures to be computed recursively without
introducing a continuous angle space.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from functools import lru_cache
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


def flag_extension_histograms(
    adjacency: Adjacency,
    maximum_size: int | None = None,
) -> tuple[dict[int, int], ...]:
    if maximum_size is not None and (
        isinstance(maximum_size, bool)
        or not isinstance(maximum_size, int)
        or maximum_size <= 0
    ):
        raise ValueError("maximum_size must be a positive integer or None")
    vertices = tuple(adjacency)
    order = {vertex: index for index, vertex in enumerate(vertices)}
    cliques = [((vertex,), set(adjacency[vertex])) for vertex in vertices]
    result = []
    size = 1
    while cliques and (maximum_size is None or size <= maximum_size):
        result.append(dict(sorted(Counter(len(common) for _, common in cliques).items())))
        next_cliques = []
        for clique, common in cliques:
            last = order[clique[-1]]
            candidates = sorted((v for v in common if order[v] > last), key=order.get)
            for vertex in candidates:
                next_cliques.append((clique + (vertex,), common.intersection(adjacency[vertex])))
        cliques = next_cliques
        size += 1
    return tuple(result)


def cliques_of_size(adjacency: Adjacency, size: int) -> tuple[tuple[Vector, ...], ...]:
    if isinstance(size, bool) or not isinstance(size, int) or size <= 0:
        raise ValueError("size must be a positive integer")
    vertices = tuple(adjacency)
    order = {vertex: index for index, vertex in enumerate(vertices)}
    cliques = [((vertex,), set(adjacency[vertex])) for vertex in vertices]
    current_size = 1
    while current_size < size and cliques:
        next_cliques = []
        for clique, common in cliques:
            last = order[clique[-1]]
            candidates = sorted((v for v in common if order[v] > last), key=order.get)
            for vertex in candidates:
                next_cliques.append((clique + (vertex,), common.intersection(adjacency[vertex])))
        cliques = next_cliques
        current_size += 1
    return tuple(clique for clique, _ in cliques) if current_size == size else ()


def _flag_extensions(adjacency: Adjacency, flag: tuple[Vector, ...]) -> frozenset[Vector]:
    if not flag or len(set(flag)) != len(flag):
        raise ValueError("flag must be a non-empty tuple of distinct vertices")
    if any(vertex not in adjacency for vertex in flag):
        raise ValueError("flag vertices must belong to adjacency")
    for left, right in combinations(flag, 2):
        if right not in adjacency[left]:
            raise ValueError("flag must be pairwise compatible")
    common = set(adjacency[flag[0]])
    for vertex in flag[1:]:
        common.intersection_update(adjacency[vertex])
    return frozenset(common)


def flag_future_signature(
    adjacency: Adjacency,
    flag: tuple[Vector, ...],
    lookahead: int,
) -> tuple:
    """Exact unlabeled continuation-tree signature through `lookahead` additions."""
    if isinstance(lookahead, bool) or not isinstance(lookahead, int) or lookahead < 0:
        raise ValueError("lookahead must be a non-negative integer")
    canonical_flag = tuple(sorted(flag))
    _flag_extensions(adjacency, canonical_flag)

    @lru_cache(maxsize=None)
    def signature(current: tuple[Vector, ...], remaining: int) -> tuple:
        if remaining == 0:
            return ()
        extensions = _flag_extensions(adjacency, current)
        child_signatures = []
        current_set = set(current)
        for vertex in extensions:
            child = tuple(sorted(current_set | {vertex}))
            child_signatures.append(signature(child, remaining - 1))
        return tuple(sorted(child_signatures, key=repr))

    return signature(canonical_flag, lookahead)


def flag_future_signature_histogram(
    adjacency: Adjacency,
    flag_size: int,
    lookahead: int,
) -> dict[tuple, int]:
    flags = cliques_of_size(adjacency, flag_size)
    return dict(Counter(flag_future_signature(adjacency, flag, lookahead) for flag in flags))


def first_flag_split_order(flag_histograms: tuple[dict[int, int], ...]) -> int | None:
    for size, histogram in enumerate(flag_histograms, start=1):
        if len(histogram) > 1:
            return size
    return None


def flag_uniform_through(
    flag_histograms: tuple[dict[int, int], ...],
    horizon: int,
) -> bool:
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 0:
        raise ValueError("horizon must be a non-negative integer")
    if horizon > len(flag_histograms):
        raise ValueError("requested horizon exceeds the enumerated flag depth")
    return all(len(flag_histograms[size - 1]) == 1 for size in range(1, horizon + 1))


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


def link_profile(adjacency: Adjacency, maximum_flag_size: int | None = None) -> PrimitiveLinkProfile:
    if not adjacency:
        raise ValueError("adjacency must be non-empty")
    flag_histograms = flag_extension_histograms(adjacency, maximum_flag_size)
    return PrimitiveLinkProfile(
        primitive_count=len(adjacency),
        link_degree_histogram=tuple(sorted(Counter(len(adjacency[v]) for v in adjacency).items())),
        link_edge_count=edge_count(adjacency),
        link_component_sizes=component_sizes(adjacency),
        link_diameter=graph_diameter(adjacency),
        edge_context_histogram=tuple(sorted(edge_context_histogram(adjacency).items(), key=repr)),
        pair_context_histogram=tuple(pair_context_histogram(adjacency).items()),
        flag_extension_histograms=tuple(tuple(hist.items()) for hist in flag_histograms),
        first_flag_split_order=first_flag_split_order(flag_histograms),
    )


def primitive_link_profile(roots: tuple[Vector, ...], maximum_flag_size: int | None = None) -> PrimitiveLinkProfile:
    return link_profile(primitive_direction_graph(roots), maximum_flag_size)


def primitive_isotropy_contract(profile: PrimitiveLinkProfile, flag_horizon: int) -> bool:
    """Finite causal-horizon candidate, not a physical isotropy theorem."""
    if isinstance(flag_horizon, bool) or not isinstance(flag_horizon, int) or flag_horizon < 0:
        raise ValueError("flag_horizon must be a non-negative integer")
    histograms = tuple(dict(histogram) for histogram in profile.flag_extension_histograms)
    if flag_horizon > len(histograms):
        raise ValueError("profile was not enumerated deeply enough for requested horizon")
    return (
        len(profile.link_component_sizes) == 1
        and len(profile.link_degree_histogram) == 1
        and len(profile.edge_context_histogram) == 1
        and flag_uniform_through(histograms, flag_horizon)
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


def _triangular_q(x: int, y: int) -> int:
    return x * x + x * y + y * y


def hcp_direction_graph() -> Adjacency:
    """Ideal HCP first-neighbor link from an integer close-packed layer model."""
    equatorial = (
        (3, 0, 0), (-3, 0, 0), (0, 3, 0), (0, -3, 0), (3, -3, 0), (-3, 3, 0)
    )
    projected = ((1, 1), (1, -2), (-2, 1))
    top = tuple((x, y, 1) for x, y in projected)
    bottom = tuple((x, y, -1) for x, y in projected)
    vertices = equatorial + top + bottom

    def contact(left: Vector, right: Vector) -> bool:
        dx = left[0] - right[0]
        dy = left[1] - right[1]
        layer_gap = abs(left[2] - right[2])
        if layer_gap == 0:
            return _triangular_q(dx, dy) == 9
        if layer_gap == 1:
            return _triangular_q(dx, dy) + 6 == 9
        return False

    adjacency = {vertex: set() for vertex in vertices}
    for index, left in enumerate(vertices):
        for right in vertices[index + 1 :]:
            if contact(left, right):
                adjacency[left].add(right)
                adjacency[right].add(left)
    return {vertex: frozenset(neighbors) for vertex, neighbors in adjacency.items()}
