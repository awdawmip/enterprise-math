#!/usr/bin/env python3
"""Exact checks for the BRC finite determinant cycle-interaction polynomial."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import permutations

from enterprise_math.brc_weighted_recurrent import finite_recurrent_mass_analysis

Q = Fraction
Edge = tuple[int, int, Fraction]
Poly = dict[int, int]  # bitmask of explicit edge variables -> integer coefficient


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(
        int(perm[i] > perm[j])
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return -1 if inversions & 1 else 1


def add_term(poly: Poly, mask: int, coefficient: int) -> None:
    if coefficient == 0:
        return
    poly[mask] = poly.get(mask, 0) + coefficient
    if poly[mask] == 0:
        del poly[mask]


def determinant_edge_polynomial(n: int, edges: list[tuple[int, int]]) -> Poly:
    by_pair: dict[tuple[int, int], list[int]] = {}
    for index, pair in enumerate(edges):
        by_pair.setdefault(pair, []).append(index)

    result: Poly = {}
    for perm in permutations(range(n)):
        sign = permutation_sign(perm)
        partial: Poly = {0: sign}
        for i, j in enumerate(perm):
            options: list[tuple[int, int]] = []
            if i == j:
                options.append((0, 1))
            options.extend((1 << index, -1) for index in by_pair.get((i, j), []))
            if not options:
                partial = {}
                break
            new: Poly = {}
            for mask, coefficient in partial.items():
                for option_mask, option_coefficient in options:
                    if mask & option_mask:
                        raise AssertionError("same explicit edge selected twice")
                    add_term(new, mask | option_mask, coefficient * option_coefficient)
            partial = new
        for mask, coefficient in partial.items():
            add_term(result, mask, coefficient)
    return result


def cycle_system_polynomial(n: int, edges: list[tuple[int, int]]) -> Poly:
    result: Poly = {}
    for mask in range(1 << len(edges)):
        indegree = [0] * n
        outdegree = [0] * n
        successor: dict[int, int] = {}
        selected_count = 0
        valid = True
        for index, (a, b) in enumerate(edges):
            if not ((mask >> index) & 1):
                continue
            selected_count += 1
            outdegree[a] += 1
            indegree[b] += 1
            if outdegree[a] > 1 or indegree[b] > 1:
                valid = False
                break
            successor[a] = b
        if not valid:
            continue
        if any(indegree[v] != outdegree[v] for v in range(n)):
            continue
        if selected_count == 0:
            add_term(result, 0, 1)
            continue

        involved = {v for v in range(n) if outdegree[v] == 1}
        seen: set[int] = set()
        cycles = 0
        for start in involved:
            if start in seen:
                continue
            cycles += 1
            v = start
            local: set[int] = set()
            while v not in local:
                local.add(v)
                seen.add(v)
                v = successor[v]
            if v != start:
                # In a finite functional graph with indegree=outdegree=1 on
                # involved vertices this should never happen.
                valid = False
                break
        if valid:
            add_term(result, mask, -1 if cycles & 1 else 1)
    return result


def evaluate_poly(poly: Poly, weights: list[Fraction]) -> Fraction:
    total = Q(0)
    for mask, coefficient in poly.items():
        term = Q(coefficient)
        for index, weight in enumerate(weights):
            if (mask >> index) & 1:
                term *= weight
        total += term
    return total


def partial_poly(poly: Poly, edge_index: int) -> Poly:
    bit = 1 << edge_index
    result: Poly = {}
    for mask, coefficient in poly.items():
        if mask & bit:
            add_term(result, mask ^ bit, coefficient)
    return result


def aggregate_matrix(n: int, edges: list[Edge]) -> list[list[Fraction]]:
    W = [[Q(0) for _ in range(n)] for _ in range(n)]
    for a, b, q in edges:
        W[a][b] += q
    return W


def response_data(n: int, edges: list[Edge]) -> tuple[list[Fraction], list[list[Fraction]]]:
    analysis = finite_recurrent_mass_analysis(aggregate_matrix(n, edges))
    if not analysis.stable or analysis.star is None:
        raise ValueError("stable positive system required")
    S = analysis.star
    R: list[Fraction] = []
    H: list[list[Fraction]] = []
    for a, b, q in edges:
        R.append(q * S[b][a])
    for e_index, (a, b, q_e) in enumerate(edges):
        row: list[Fraction] = []
        for f_index, (c, d, q_f) in enumerate(edges):
            value = q_e * q_f * S[b][c] * S[d][a]
            if e_index == f_index:
                value += q_e * S[b][a]
            row.append(value)
        H.append(row)
    return R, H


def edge_on_directed_cycle(n: int, edges: list[tuple[int, int]], index: int) -> bool:
    a, b = edges[index]
    if a == b:
        return True
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
    queue = deque([b])
    seen = {b}
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w == a:
                return True
            if w not in seen:
                seen.add(w)
                queue.append(w)
    return False


def has_directed_cycle(n: int, edges: list[tuple[int, int]]) -> bool:
    return any(edge_on_directed_cycle(n, edges, index) for index in range(len(edges)))


def gauge_weights(edges: list[Edge], h: list[Fraction]) -> list[Edge]:
    return [(a, b, q * h[b] / h[a]) for a, b, q in edges]


def tree_normal_coordinates(n: int, edges: list[Edge], tree: list[int]) -> tuple[list[Fraction], list[Fraction]]:
    h: list[Fraction | None] = [None] * n
    h[0] = Q(1)
    remaining = set(tree)
    while remaining:
        progress = False
        for index in tuple(remaining):
            a, b, q = edges[index]
            if h[a] is not None and h[b] is None:
                h[b] = h[a] / q
                remaining.remove(index)
                progress = True
            elif h[b] is not None and h[a] is None:
                h[a] = q * h[b]
                remaining.remove(index)
                progress = True
            elif h[a] is not None and h[b] is not None:
                assert q * h[b] / h[a] == 1
                remaining.remove(index)
                progress = True
        if not progress:
            raise ValueError("tree does not connect graph")
    gauge = [value for value in h if value is not None]
    normalized = [q * gauge[b] / gauge[a] for a, b, q in edges]
    tree_set = set(tree)
    assert all(normalized[index] == 1 for index in tree)
    coordinates = [normalized[index] for index in range(len(edges)) if index not in tree_set]
    return normalized, coordinates


def tree_reduce_polynomial(poly: Poly, edge_count: int, tree: list[int]) -> Poly:
    tree_set = set(tree)
    non_tree = [index for index in range(edge_count) if index not in tree_set]
    position = {edge_index: j for j, edge_index in enumerate(non_tree)}
    result: Poly = {}
    for mask, coefficient in poly.items():
        new_mask = 0
        for edge_index in non_tree:
            if (mask >> edge_index) & 1:
                new_mask |= 1 << position[edge_index]
        add_term(result, new_mask, coefficient)
    return result


def check_explicit_cycle_system_formula_all_three_vertex_graphs() -> None:
    possible = [(i, j) for i in range(3) for j in range(3)]
    checked = 0
    for support_mask in range(1 << len(possible)):
        edges = [pair for index, pair in enumerate(possible) if (support_mask >> index) & 1]
        det_poly = determinant_edge_polynomial(3, edges)
        cycle_poly = cycle_system_polynomial(3, edges)
        assert det_poly == cycle_poly
        assert all(coefficient in {-1, 1} for coefficient in det_poly.values())
        assert (det_poly == {0: 1}) == (not has_directed_cycle(3, edges))
        checked += 1
    assert checked == 512
    print(f"3-vertex support polynomials checked={checked}")


def check_parallel_edge_coefficient_rigidity() -> None:
    edges = [(0, 1), (0, 1), (1, 0), (0, 0), (1, 1)]
    poly = determinant_edge_polynomial(2, edges)
    assert poly == cycle_system_polynomial(2, edges)
    assert all(coefficient in {-1, 1} for coefficient in poly.values())


def check_disjoint_and_overlapping_examples() -> None:
    disjoint = [(0, 0), (1, 1)]
    P = determinant_edge_polynomial(2, disjoint)
    assert P == {0: 1, 1 << 0: -1, 1 << 1: -1, (1 << 0) | (1 << 1): 1}

    overlap = [(0, 0), (0, 1), (1, 0)]
    P2 = determinant_edge_polynomial(2, overlap)
    assert P2 == {0: 1, 1 << 0: -1, (1 << 1) | (1 << 2): -1}
    assert ((1 << 0) | (1 << 1) | (1 << 2)) not in P2

    bridge = [(0, 0), (1, 1), (0, 1)]
    P3 = determinant_edge_polynomial(2, bridge)
    assert partial_poly(P3, 2) == {}


def check_termwise_gauge_invariance() -> None:
    edges: list[Edge] = [
        (0, 0, Q(1, 7)),
        (0, 1, Q(1, 5)),
        (1, 0, Q(1, 6)),
        (1, 2, Q(1, 8)),
        (2, 1, Q(1, 9)),
    ]
    shapes = [(a, b) for a, b, _ in edges]
    poly = determinant_edge_polynomial(3, shapes)
    h = [Q(2, 3), Q(5, 7), Q(11, 13)]
    gauged = gauge_weights(edges, h)
    q = [weight for _, _, weight in edges]
    q2 = [weight for _, _, weight in gauged]
    for mask in poly:
        before = Q(1)
        after = Q(1)
        for index in range(len(edges)):
            if (mask >> index) & 1:
                before *= q[index]
                after *= q2[index]
        assert before == after
    assert evaluate_poly(poly, q) == evaluate_poly(poly, q2)


def check_tree_gauge_cycle_interaction_polynomial() -> None:
    n = 3
    edges: list[Edge] = [
        (0, 1, Q(1, 5)),
        (1, 2, Q(1, 6)),
        (2, 0, Q(1, 7)),
        (0, 2, Q(1, 10)),
        (2, 1, Q(1, 9)),
    ]
    tree = [0, 1]
    shapes = [(a, b) for a, b, _ in edges]
    P = determinant_edge_polynomial(n, shapes)
    reduced = tree_reduce_polynomial(P, len(edges), tree)
    assert all(coefficient == int(coefficient) for coefficient in reduced.values())
    normalized, coordinates = tree_normal_coordinates(n, edges, tree)
    original_value = evaluate_poly(P, [q for _, _, q in edges])
    normalized_value = evaluate_poly(P, normalized)
    reduced_value = evaluate_poly(reduced, coordinates)
    assert original_value == normalized_value == reduced_value

    analysis = finite_recurrent_mass_analysis(aggregate_matrix(n, edges))
    assert analysis.stable
    assert original_value > 0


def check_edge_response_polynomial_identities() -> None:
    n = 2
    edges: list[Edge] = [
        (0, 0, Q(1, 5)),
        (0, 1, Q(1, 4)),
        (1, 0, Q(1, 3)),
    ]
    shapes = [(a, b) for a, b, _ in edges]
    weights = [q for _, _, q in edges]
    Ppoly = determinant_edge_polynomial(n, shapes)
    P = evaluate_poly(Ppoly, weights)
    assert P > 0
    R, H = response_data(n, edges)

    first_partials = [partial_poly(Ppoly, i) for i in range(len(edges))]
    for i in range(len(edges)):
        Pe = evaluate_poly(first_partials[i], weights)
        assert R[i] == -weights[i] * Pe / P
        assert Pe < 0
        assert H[i][i] == R[i] + R[i] ** 2

    for i in range(len(edges)):
        for j in range(len(edges)):
            if i == j:
                continue
            Pe = evaluate_poly(first_partials[i], weights)
            Pf = evaluate_poly(first_partials[j], weights)
            Pef = evaluate_poly(partial_poly(first_partials[i], j), weights)
            expected = weights[i] * weights[j] * (Pe * Pf - P * Pef) / (P**2)
            assert H[i][j] == expected
            assert Pe * Pf >= P * Pef


def check_formal_derivative_recurrent_edge_support() -> None:
    positions = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for mask in range(16):
        shapes = [pair for index, pair in enumerate(positions) if (mask >> index) & 1]
        P = determinant_edge_polynomial(2, shapes)
        for index in range(len(shapes)):
            derivative_nonzero = bool(partial_poly(P, index))
            assert derivative_nonzero == edge_on_directed_cycle(2, shapes, index)


def check_parity_thickness_one_state_polynomial() -> None:
    P = determinant_edge_polynomial(1, [(0, 0)])
    assert P == {0: 1, 1: -1}
    skeleton = Q(2)
    for thickness, expected_stable in [(Q(1, 4), True), (Q(1, 2), True), (Q(1), False)]:
        q = skeleton * thickness**2
        value = evaluate_poly(P, [q])
        stable = finite_recurrent_mass_analysis([[q]]).stable
        assert stable == expected_stable
        if stable:
            assert value > 0
        else:
            assert value <= 0


def main() -> int:
    check_explicit_cycle_system_formula_all_three_vertex_graphs()
    check_parallel_edge_coefficient_rigidity()
    check_disjoint_and_overlapping_examples()
    check_termwise_gauge_invariance()
    check_tree_gauge_cycle_interaction_polynomial()
    check_edge_response_polynomial_identities()
    check_formal_derivative_recurrent_edge_support()
    check_parity_thickness_one_state_polynomial()
    print("BRC cycle-interaction polynomial exact checks: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
