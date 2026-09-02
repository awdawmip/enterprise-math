#!/usr/bin/env python3
"""Exact checks for positive-rational BRC prime-valuation holonomy normal form."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from math import isqrt

Q = Fraction
Edge = tuple[int, int, Fraction]


def factor_integer(n: int) -> dict[int, int]:
    if n <= 0:
        raise ValueError("positive integer required")
    result: dict[int, int] = {}
    x = n
    p = 2
    while p * p <= x:
        while x % p == 0:
            result[p] = result.get(p, 0) + 1
            x //= p
        p = 3 if p == 2 else p + 2
    if x > 1:
        result[x] = result.get(x, 0) + 1
    return result


def valuations(q: Fraction) -> dict[int, int]:
    if q <= 0:
        raise ValueError("positive rational required")
    result = factor_integer(q.numerator)
    for p, exponent in factor_integer(q.denominator).items():
        result[p] = result.get(p, 0) - exponent
        if result[p] == 0:
            del result[p]
    return result


def reconstruct_valuations(data: dict[int, int]) -> Fraction:
    result = Q(1)
    for p, exponent in sorted(data.items()):
        if exponent >= 0:
            result *= p**exponent
        else:
            result /= p ** (-exponent)
    return result


def gauge_edges(edges: list[Edge], h: list[Fraction]) -> list[Edge]:
    return [(a, b, q * h[b] / h[a]) for a, b, q in edges]


def validate_tree(n: int, edges: list[Edge], tree_indices: list[int]) -> None:
    if len(tree_indices) != n - 1:
        raise ValueError("tree must contain n-1 edges")
    graph = [[] for _ in range(n)]
    for index in tree_indices:
        a, b, _ = edges[index]
        if a == b:
            raise ValueError("tree cannot contain self-loop")
        graph[a].append(b)
        graph[b].append(a)
    seen = {0}
    queue = deque([0])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in seen:
                seen.add(w)
                queue.append(w)
    if len(seen) != n:
        raise ValueError("tree is not connected")


def tree_normalizing_gauge(
    n: int, edges: list[Edge], tree_indices: list[int], root: int = 0
) -> list[Fraction]:
    validate_tree(n, edges, tree_indices)
    h: list[Fraction | None] = [None] * n
    h[root] = Q(1)
    remaining = set(tree_indices)
    while remaining:
        progressed = False
        for index in tuple(remaining):
            a, b, q = edges[index]
            if h[a] is not None and h[b] is None:
                h[b] = h[a] / q
                remaining.remove(index)
                progressed = True
            elif h[b] is not None and h[a] is None:
                h[a] = q * h[b]
                remaining.remove(index)
                progressed = True
            elif h[a] is not None and h[b] is not None:
                assert q * h[b] / h[a] == 1
                remaining.remove(index)
                progressed = True
        if not progressed:
            raise AssertionError("tree gauge propagation stalled")
    assert all(value is not None and value > 0 for value in h)
    return [value for value in h if value is not None]


def tree_normal_form(
    n: int, edges: list[Edge], tree_indices: list[int], root: int = 0
) -> tuple[list[Fraction], list[Edge], list[Fraction]]:
    h = tree_normalizing_gauge(n, edges, tree_indices, root)
    normalized = gauge_edges(edges, h)
    for index in tree_indices:
        assert normalized[index][2] == 1
    non_tree = [
        normalized[index][2]
        for index in range(len(edges))
        if index not in set(tree_indices)
    ]
    return h, normalized, non_tree


def tree_path(
    n: int, edges: list[Edge], tree_indices: list[int], start: int, target: int
) -> list[tuple[int, int]]:
    """Return (edge_index, orientation_sign) along underlying tree path."""
    graph: list[list[tuple[int, int, int]]] = [[] for _ in range(n)]
    for index in tree_indices:
        a, b, _ = edges[index]
        graph[a].append((b, index, +1))
        graph[b].append((a, index, -1))
    parent: dict[int, tuple[int, int, int] | None] = {start: None}
    queue = deque([start])
    while queue and target not in parent:
        v = queue.popleft()
        for w, index, sign in graph[v]:
            if w not in parent:
                parent[w] = (v, index, sign)
                queue.append(w)
    if target not in parent:
        raise ValueError("tree path missing")
    result: list[tuple[int, int]] = []
    v = target
    while v != start:
        item = parent[v]
        assert item is not None
        previous, index, sign = item
        result.append((index, sign))
        v = previous
    result.reverse()
    return result


def fundamental_cycle_holonomy(
    n: int, edges: list[Edge], tree_indices: list[int], edge_index: int
) -> Fraction:
    if edge_index in set(tree_indices):
        raise ValueError("fundamental coordinate requires non-tree edge")
    a, b, q = edges[edge_index]
    result = q
    for tree_index, sign in tree_path(n, edges, tree_indices, b, a):
        weight = edges[tree_index][2]
        result *= weight if sign > 0 else Q(1) / weight
    return result


def prime_coordinate_table(coordinates: list[Fraction]) -> dict[int, tuple[int, ...]]:
    primes = sorted({p for q in coordinates for p in valuations(q)})
    return {
        p: tuple(valuations(q).get(p, 0) for q in coordinates)
        for p in primes
    }


def squarefree_representative(q: Fraction) -> int:
    result = 1
    for p, exponent in valuations(q).items():
        if exponent % 2:
            result *= p
    return result


def is_rational_square(q: Fraction) -> bool:
    if q <= 0:
        return False
    n = isqrt(q.numerator)
    d = isqrt(q.denominator)
    return n * n == q.numerator and d * d == q.denominator


def all_relevant_primes(*edge_sets: list[Edge], gauges: list[Fraction] | None = None) -> set[int]:
    primes: set[int] = set()
    for edges in edge_sets:
        for _, _, q in edges:
            primes.update(valuations(q))
    if gauges is not None:
        for h in gauges:
            primes.update(valuations(h))
    return primes


def check_tree_normal_form_and_fundamental_cycles() -> tuple[int, list[Edge], list[int], list[Fraction]]:
    n = 4
    edges: list[Edge] = [
        (0, 1, Q(12, 5)),
        (2, 1, Q(7, 18)),
        (2, 3, Q(25, 14)),
        (3, 0, Q(9, 10)),
        (0, 2, Q(11, 6)),
        (1, 3, Q(5, 21)),
        (0, 1, Q(13, 8)),
    ]
    tree = [0, 1, 2]
    h, normalized, coordinates = tree_normal_form(n, edges, tree)
    assert h == [Q(1), Q(5, 12), Q(35, 216), Q(49, 540)]
    assert len(coordinates) == len(edges) - n + 1 == 4
    non_tree_indices = [index for index in range(len(edges)) if index not in set(tree)]
    for coordinate, index in zip(coordinates, non_tree_indices):
        assert coordinate == fundamental_cycle_holonomy(n, edges, tree, index)
    for coordinate in coordinates:
        assert reconstruct_valuations(valuations(coordinate)) == coordinate

    random_gauge = [Q(2, 3), Q(5, 7), Q(11, 13), Q(17, 19)]
    transformed = gauge_edges(edges, random_gauge)
    h2, normalized2, coordinates2 = tree_normal_form(n, transformed, tree)
    assert coordinates2 == coordinates

    # Reconstruct an explicit gauge from equality of the two normal forms.
    relative = [h[i] / h2[i] for i in range(n)]
    assert gauge_edges(edges, relative) == transformed

    # Tree-normal representative is itself a canonical representative once root/T are fixed.
    assert tree_normal_form(n, normalized, tree)[2] == coordinates
    assert tree_normal_form(n, normalized2, tree)[2] == coordinates

    return n, edges, tree, coordinates


def check_primewise_coboundary_law(n: int, edges: list[Edge]) -> None:
    gauge = [Q(2, 3), Q(5, 7), Q(11, 13), Q(17, 19)]
    transformed = gauge_edges(edges, gauge)
    primes = all_relevant_primes(edges, transformed, gauges=gauge)
    for p in primes:
        phi = [valuations(h).get(p, 0) for h in gauge]
        for (a, b, q), (_, _, q2) in zip(edges, transformed):
            lhs = valuations(q2).get(p, 0) - valuations(q).get(p, 0)
            rhs = phi[b] - phi[a]
            assert lhs == rhs
            assert lhs % 2 == rhs % 2
            assert lhs % 3 == rhs % 3


def check_complete_gauge_classification(
    n: int, edges: list[Edge], tree: list[int], coordinates: list[Fraction]
) -> None:
    gauge = [Q(7, 11), Q(13, 17), Q(19, 23), Q(29, 31)]
    equivalent = gauge_edges(edges, gauge)
    assert tree_normal_form(n, equivalent, tree)[2] == coordinates
    assert prime_coordinate_table(tree_normal_form(n, equivalent, tree)[2]) == prime_coordinate_table(coordinates)

    non_tree_indices = [index for index in range(len(edges)) if index not in set(tree)]
    altered = edges[:]
    index = non_tree_indices[1]
    a, b, q = altered[index]
    altered[index] = (a, b, 17 * q)
    altered_coordinates = tree_normal_form(n, altered, tree)[2]
    assert altered_coordinates != coordinates
    old = prime_coordinate_table(coordinates)
    new = prime_coordinate_table(altered_coordinates)
    old17 = old.get(17, (0,) * len(coordinates))
    new17 = new.get(17, (0,) * len(coordinates))
    assert new17[1] == old17[1] + 1


def check_square_classes(coordinates: list[Fraction]) -> None:
    for coordinate in coordinates:
        sf = squarefree_representative(coordinate)
        assert sf > 0
        assert is_rational_square(coordinate / sf)
        table = valuations(coordinate)
        sf_primes = set(factor_integer(sf))
        assert sf_primes == {p for p, exponent in table.items() if exponent % 2}


def build_tree_normal_lift(
    n: int,
    edge_shapes: list[tuple[int, int]],
    tree_indices: list[int],
    prime: int,
    residues: list[int],
) -> list[Edge]:
    non_tree_indices = [index for index in range(len(edge_shapes)) if index not in set(tree_indices)]
    if len(non_tree_indices) != len(residues):
        raise ValueError("residue dimension mismatch")
    weights = [Q(1) for _ in edge_shapes]
    for index, residue in zip(non_tree_indices, residues):
        weights[index] = Q(prime**residue)
    return [
        (a, b, weights[index])
        for index, (a, b) in enumerate(edge_shapes)
    ]


def check_mod_m_surjective_lifts(n: int, edges: list[Edge], tree: list[int]) -> None:
    shapes = [(a, b) for a, b, _ in edges]
    beta = len(edges) - n + 1
    parity = [1, 0, 1, 1]
    assert len(parity) == beta
    lift2 = build_tree_normal_lift(n, shapes, tree, 2, parity)
    coords2 = tree_normal_form(n, lift2, tree)[2]
    assert [valuations(q).get(2, 0) % 2 for q in coords2] == parity

    residues3 = [0, 1, 2, 1]
    lift3 = build_tree_normal_lift(n, shapes, tree, 3, residues3)
    coords3 = tree_normal_form(n, lift3, tree)[2]
    assert [valuations(q).get(3, 0) % 3 for q in coords3] == residues3


def check_feedforward_gauge_richer_than_recurrence() -> None:
    # Directed diamond: no directed cycle, but underlying graph has beta1=1.
    n = 4
    edges: list[Edge] = [
        (0, 1, Q(2)),
        (0, 2, Q(3)),
        (1, 3, Q(5)),
        (2, 3, Q(7)),
    ]
    tree = [0, 1, 2]  # underlying edges 0-1,0-2,1-3
    _, _, coords = tree_normal_form(n, edges, tree)
    assert len(coords) == 1
    # Non-tree edge 2->3 reads the cross-ratio 3*7/(2*5)=21/10.
    assert coords == [Q(21, 10)]
    assert valuations(coords[0]) != {}

    # There is no directed return path for any edge, so recurrent loop response is zero.
    for index, (a, b, _) in enumerate(edges):
        assert not (a == b or directed_reachable(n, edges, b, a))


def directed_reachable(n: int, edges: list[Edge], start: int, target: int) -> bool:
    if start == target:
        return True
    graph = [[] for _ in range(n)]
    for a, b, _ in edges:
        graph[a].append(b)
    queue = deque([start])
    seen = {start}
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w == target:
                return True
            if w not in seen:
                seen.add(w)
                queue.append(w)
    return False


def check_finite_prime_support(coordinates: list[Fraction]) -> None:
    table = prime_coordinate_table(coordinates)
    assert len(table) < 50
    for p, vector in table.items():
        assert p >= 2
        assert len(vector) == len(coordinates)
    reconstructed = []
    for coordinate_index in range(len(coordinates)):
        data = {
            p: vector[coordinate_index]
            for p, vector in table.items()
            if vector[coordinate_index] != 0
        }
        reconstructed.append(reconstruct_valuations(data))
    assert reconstructed == coordinates


def main() -> int:
    n, edges, tree, coordinates = check_tree_normal_form_and_fundamental_cycles()
    check_primewise_coboundary_law(n, edges)
    check_complete_gauge_classification(n, edges, tree, coordinates)
    check_square_classes(coordinates)
    check_mod_m_surjective_lifts(n, edges, tree)
    check_feedforward_gauge_richer_than_recurrence()
    check_finite_prime_support(coordinates)
    print("BRC prime-valuation holonomy exact checks: PASS")
    print(f"beta1={len(edges)-n+1} prime_support={len(prime_coordinate_table(coordinates))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
