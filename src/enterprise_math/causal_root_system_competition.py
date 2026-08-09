"""Pure-integer primitive-direction diagnostics for A/D/E root-system candidates.

The purpose is not to declare a universal lattice.  It supplies common causal
local-relation measurements for competing simply-laced root systems.  A root is
a primitive direction.  Two root directions are adjacent in the first-shell
link when their difference is again a root, equivalently when their integer dot
product is half the common squared root length.

D_n roots are +/-e_i +/-e_j.  E8 roots are represented without fractions by
multiplying the standard root system by two: either two coordinates are +/-2,
or all eight coordinates are +/-1 with an even number of minus signs.  Every
scaled E8 root then has squared length eight and primitive-link adjacency is dot=4.
"""

from __future__ import annotations

from collections import Counter, deque
from itertools import combinations, product

Vector = tuple[int, ...]
LocalContext = tuple[int, int, tuple[int, ...], tuple[tuple[int, int], ...]]


def dot(left: Vector, right: Vector) -> int:
    if len(left) != len(right):
        raise ValueError("vectors must have equal length")
    return sum(a * b for a, b in zip(left, right))


def d_roots(n: int) -> tuple[Vector, ...]:
    if isinstance(n, bool) or not isinstance(n, int) or n < 3:
        raise ValueError("D_n requires n>=3 in this research module")
    roots = []
    for i, j in combinations(range(n), 2):
        for sign_i in (-1, 1):
            for sign_j in (-1, 1):
                root = [0] * n
                root[i] = sign_i
                root[j] = sign_j
                roots.append(tuple(root))
    return tuple(roots)


def e8_roots_scaled() -> tuple[Vector, ...]:
    roots = []
    for i, j in combinations(range(8), 2):
        for sign_i in (-2, 2):
            for sign_j in (-2, 2):
                root = [0] * 8
                root[i] = sign_i
                root[j] = sign_j
                roots.append(tuple(root))
    for signs in product((-1, 1), repeat=8):
        if sum(value < 0 for value in signs) % 2 == 0:
            roots.append(tuple(signs))
    if len(roots) != 240:
        raise AssertionError("scaled E8 root construction must contain 240 roots")
    return tuple(roots)


def simply_laced_squared_length(roots: tuple[Vector, ...]) -> int:
    if not roots:
        raise ValueError("root system must be non-empty")
    lengths = {dot(root, root) for root in roots}
    if len(lengths) != 1:
        raise ValueError("all primitive roots must have equal squared length")
    length = next(iter(lengths))
    if length % 2 != 0:
        raise ValueError("squared root length must admit integer half-inner-product adjacency")
    return length


def primitive_link_adjacent(left: Vector, right: Vector, squared_length: int) -> bool:
    return left != right and dot(left, right) == squared_length // 2


def primitive_link_neighbors(roots: tuple[Vector, ...], root: Vector) -> tuple[Vector, ...]:
    if root not in roots:
        raise ValueError("root must belong to supplied root system")
    length = simply_laced_squared_length(roots)
    return tuple(
        candidate
        for candidate in roots
        if primitive_link_adjacent(root, candidate, length)
    )


def primitive_link_degree_set(roots: tuple[Vector, ...]) -> tuple[int, ...]:
    return tuple(sorted({len(primitive_link_neighbors(roots, root)) for root in roots}))


def primitive_edge_context(roots: tuple[Vector, ...], root: Vector) -> LocalContext:
    length = simply_laced_squared_length(roots)
    common = primitive_link_neighbors(roots, root)
    adjacency = {vertex: set() for vertex in common}
    edge_count = 0
    for index, left in enumerate(common):
        for right in common[index + 1 :]:
            if primitive_link_adjacent(left, right, length):
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

    degree_histogram = tuple(sorted(Counter(len(adjacency[v]) for v in common).items()))
    return len(common), edge_count, tuple(sorted(components, reverse=True)), degree_histogram


def all_primitive_edge_contexts_uniform(roots: tuple[Vector, ...]) -> bool:
    return len({primitive_edge_context(roots, root) for root in roots}) == 1


def d_direction_count(n: int) -> int:
    if n < 3:
        raise ValueError("n must be at least three")
    return 2 * n * (n - 1)


def d_direction_link_degree(n: int) -> int:
    if n < 3:
        raise ValueError("n must be at least three")
    return 4 * (n - 2)


def d_edge_context_closed(n: int) -> LocalContext:
    if n < 3:
        raise ValueError("n must be at least three")
    common = 4 * (n - 2)
    internal_degree = 2 * n - 5
    internal_edges = common * internal_degree // 2
    components = (2, 2) if n == 3 else (common,)
    return common, internal_edges, components, ((internal_degree, common),)


def e8_local_context_closed() -> LocalContext:
    return 56, 756, (56,), ((27, 56),)


def root_system_local_profile(roots: tuple[Vector, ...]) -> tuple[int, int, LocalContext, bool]:
    degrees = primitive_link_degree_set(roots)
    if len(degrees) != 1:
        raise ValueError("primitive directions are not link-degree uniform")
    context = primitive_edge_context(roots, roots[0])
    return len(roots), degrees[0], context, all_primitive_edge_contexts_uniform(roots)
