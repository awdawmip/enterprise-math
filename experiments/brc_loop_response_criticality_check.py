#!/usr/bin/env python3
"""Exact checks for recurrent BRC loop response and criticality geometry."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product
from math import lcm

from enterprise_math.brc_weighted_recurrent import finite_recurrent_mass_analysis

Q = Fraction
Edge = tuple[int, int, Fraction]
Matrix = list[list[Fraction]]
IntMatrix = list[list[int]]


def aggregate_matrix(n: int, edges: list[Edge]) -> Matrix:
    W = [[Q(0) for _ in range(n)] for _ in range(n)]
    for a, b, weight in edges:
        if weight <= 0:
            raise ValueError("edge weights must be positive")
        W[a][b] += weight
    return W


def star_matrix(n: int, edges: list[Edge]) -> tuple[tuple[Fraction, ...], ...]:
    result = finite_recurrent_mass_analysis(aggregate_matrix(n, edges))
    if not result.stable or result.star is None:
        raise ValueError("edge system must be stable")
    return result.star


def edge_responses(n: int, edges: list[Edge]) -> list[Fraction]:
    S = star_matrix(n, edges)
    return [weight * S[b][a] for a, b, weight in edges]


def response_hessian(n: int, edges: list[Edge]) -> Matrix:
    S = star_matrix(n, edges)
    out: Matrix = []
    for e_index, (a, b, q_e) in enumerate(edges):
        row: list[Fraction] = []
        for f_index, (c, d, q_f) in enumerate(edges):
            value = q_e * q_f * S[b][c] * S[d][a]
            if e_index == f_index:
                value += q_e * S[b][a]
            row.append(value)
        out.append(row)
    return out


def gauge_edges(edges: list[Edge], potential: list[Fraction]) -> list[Edge]:
    return [
        (a, b, weight * potential[b] / potential[a])
        for a, b, weight in edges
    ]


def mat_vec(matrix: Matrix, vector: list[Fraction]) -> list[Fraction]:
    return [
        sum((matrix[i][j] * vector[j] for j in range(len(vector))), Q(0))
        for i in range(len(matrix))
    ]


def rational_rank(matrix: Matrix) -> int:
    if not matrix:
        return 0
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0])
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if work[r][col] != 0), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][col]
        work[rank] = [value / scale for value in work[rank]]
        for r in range(rows):
            if r == rank:
                continue
            factor = work[r][col]
            if factor != 0:
                work[r] = [work[r][j] - factor * work[rank][j] for j in range(cols)]
        rank += 1
        if rank == rows:
            break
    return rank


def det_fraction(matrix: Matrix) -> Fraction:
    n = len(matrix)
    if n == 0:
        return Q(1)
    work = [row[:] for row in matrix]
    sign = 1
    det = Q(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if work[r][col] != 0), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            sign *= -1
        pivot_value = work[col][col]
        det *= pivot_value
        for r in range(col + 1, n):
            factor = work[r][col] / pivot_value
            if factor != 0:
                for j in range(col, n):
                    work[r][j] -= factor * work[col][j]
    return sign * det


def all_principal_minors_nonnegative(matrix: Matrix) -> bool:
    n = len(matrix)
    for size in range(1, n + 1):
        for indices in combinations(range(n), size):
            principal = [[matrix[i][j] for j in indices] for i in indices]
            if det_fraction(principal) < 0:
                return False
    return True


def gauge_basis(n: int, edges: list[Edge]) -> list[list[Fraction]]:
    basis: list[list[Fraction]] = []
    # Root vertex 0 fixes the additive constant.
    for vertex in range(1, n):
        phi = [Q(0)] * n
        phi[vertex] = Q(1)
        basis.append([phi[b] - phi[a] for a, b, _ in edges])
    return basis


def reachable(n: int, edges: list[Edge], start: int, target: int) -> bool:
    if start == target:
        return True
    graph = [[] for _ in range(n)]
    for a, b, _ in edges:
        graph[a].append(b)
    stack = [start]
    seen = {start}
    while stack:
        v = stack.pop()
        for w in graph[v]:
            if w == target:
                return True
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return False


def edge_on_cycle(n: int, edges: list[Edge], index: int) -> bool:
    a, b, _ = edges[index]
    return a == b or reachable(n, edges, b, a)


def trace_star_minus_identity(n: int, edges: list[Edge]) -> Fraction:
    S = star_matrix(n, edges)
    return sum((S[i][i] - 1 for i in range(n)), Q(0))


def common_denominator_edges(edges: list[Edge]) -> int:
    D = 1
    for _, _, q in edges:
        D = lcm(D, q.denominator)
    return D


def det_int(matrix: IntMatrix) -> int:
    n = len(matrix)
    if n == 0:
        return 1
    if n == 1:
        return matrix[0][0]
    result = 0
    for col in range(n):
        minor = [row[:col] + row[col + 1 :] for row in matrix[1:]]
        result += ((-1) ** col) * matrix[0][col] * det_int(minor)
    return result


def adjugate_int(matrix: IntMatrix) -> IntMatrix:
    n = len(matrix)
    if n == 1:
        return [[1]]
    return [
        [
            ((-1) ** (i + j))
            * det_int([
                [matrix[r][c] for c in range(n) if c != i]
                for r in range(n)
                if r != j
            ])
            for j in range(n)
        ]
        for i in range(n)
    ]


def integer_response_data(n: int, edges: list[Edge]) -> tuple[int, int, IntMatrix, list[int], IntMatrix]:
    D = common_denominator_edges(edges)
    A = [[0 for _ in range(n)] for _ in range(n)]
    a_values: list[int] = []
    for a, b, q in edges:
        value = int(q * D)
        a_values.append(value)
        A[a][b] += value
    B = [[D * int(i == j) - A[i][j] for j in range(n)] for i in range(n)]
    delta = det_int(B)
    C = adjugate_int(B)
    return D, delta, C, a_values, A


def integer_hessian_numerator(n: int, edges: list[Edge]) -> tuple[IntMatrix, int]:
    _, delta, C, a_values, _ = integer_response_data(n, edges)
    K: IntMatrix = []
    for e_index, (a, b, _) in enumerate(edges):
        row: list[int] = []
        for f_index, (c, d, _) in enumerate(edges):
            value = a_values[e_index] * a_values[f_index] * C[b][c] * C[d][a]
            if e_index == f_index:
                value += a_values[e_index] * C[b][a] * delta
            row.append(value)
        K.append(row)
    return K, delta


def check_edge_support_detector() -> None:
    positions = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for mask in range(16):
        edges: list[Edge] = [
            (a, b, Q(1, 10))
            for index, (a, b) in enumerate(positions)
            if (mask >> index) & 1
        ]
        if not edges:
            continue
        responses = edge_responses(2, edges)
        for index, response in enumerate(responses):
            assert (response > 0) == edge_on_cycle(2, edges, index)
        assert sum(responses, Q(0)) == trace_star_minus_identity(2, edges)


def check_strongly_connected_hessian_geometry() -> None:
    examples: list[tuple[int, list[Edge]]] = [
        (
            2,
            [
                (0, 0, Q(1, 10)),
                (0, 1, Q(1, 5)),
                (0, 1, Q(1, 10)),
                (1, 0, Q(1, 4)),
                (1, 1, Q(1, 8)),
            ],
        ),
        (
            3,
            [
                (0, 1, Q(1, 8)),
                (1, 2, Q(1, 7)),
                (2, 0, Q(1, 9)),
                (0, 2, Q(1, 12)),
                (2, 1, Q(1, 11)),
                (1, 0, Q(1, 10)),
            ],
        ),
    ]

    for n, edges in examples:
        H = response_hessian(n, edges)
        assert H == [list(row) for row in zip(*H)]
        assert all_principal_minors_nonnegative(H)
        expected_rank = len(edges) - n + 1
        assert rational_rank(H) == expected_rank
        basis = gauge_basis(n, edges)
        assert rational_rank(basis) == n - 1
        for gauge in basis:
            assert mat_vec(H, gauge) == [Q(0)] * len(edges)

        # A deliberately nonuniform rational vertex gauge must preserve every
        # edge response and every Hessian entry exactly.
        potential = [Q(2 + i, 1) for i in range(n)]
        transformed = gauge_edges(edges, potential)
        assert edge_responses(n, transformed) == edge_responses(n, edges)
        assert response_hessian(n, transformed) == H


def check_general_graph_transient_kernel() -> None:
    # SCC {0,1}, feed-forward edge 1->2, and terminal self-loop at 2.
    edges: list[Edge] = [
        (0, 1, Q(1, 5)),
        (1, 0, Q(1, 6)),
        (1, 2, Q(3, 2)),
        (2, 2, Q(1, 7)),
    ]
    responses = edge_responses(3, edges)
    assert responses[0] > 0 and responses[1] > 0
    assert responses[2] == 0
    assert responses[3] > 0
    H = response_hessian(3, edges)
    assert H[2] == [Q(0)] * len(edges)
    assert [row[2] for row in H] == [Q(0)] * len(edges)


def check_integer_response_certificates() -> None:
    n = 2
    edges: list[Edge] = [
        (0, 0, Q(1, 10)),
        (0, 1, Q(1, 5)),
        (0, 1, Q(1, 10)),
        (1, 0, Q(1, 4)),
        (1, 1, Q(1, 8)),
    ]
    H = response_hessian(n, edges)
    R = edge_responses(n, edges)
    _, delta, C, a_values, _ = integer_response_data(n, edges)
    assert delta > 0
    for index, (a, b, _) in enumerate(edges):
        assert R[index] == Q(a_values[index] * C[b][a], delta)

    K, K_delta = integer_hessian_numerator(n, edges)
    assert K_delta == delta
    assert K == [list(row) for row in zip(*K)]
    for i in range(len(edges)):
        for j in range(len(edges)):
            assert H[i][j] == Q(K[i][j], delta**2)
    assert rational_rank([[Q(value) for value in row] for row in K]) == len(edges) - n + 1


def aggregate_from_entries(entries: list[list[Fraction]]) -> Matrix:
    return [[Q(value) for value in row] for row in entries]


def polynomial_add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    out = [0] * size
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    return out


def polynomial_mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(
        int(perm[i] > perm[j])
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return -1 if inversions & 1 else 1


def criticality_polynomial(W: Matrix) -> tuple[int, list[int], IntMatrix]:
    n = len(W)
    D = 1
    for row in W:
        for value in row:
            D = lcm(D, value.denominator)
    A = [[int(W[i][j] * D) for j in range(n)] for i in range(n)]
    poly = [0]
    for perm in permutations(range(n)):
        term = [1]
        for i, j in enumerate(perm):
            # Entry of DI-tA: D*delta_ij - A_ij*t.
            term = polynomial_mul(term, [D * int(i == j), -A[i][j]])
        if permutation_sign(perm) < 0:
            term = [-value for value in term]
        poly = polynomial_add(poly, term)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return D, poly, A


def poly_eval(poly: list[int], t: Fraction) -> Fraction:
    result = Q(0)
    for coefficient in reversed(poly):
        result = result * t + coefficient
    return result


def poly_derivative(poly: list[int]) -> list[int]:
    return [i * poly[i] for i in range(1, len(poly))]


def scale_matrix(W: Matrix, t: Fraction) -> Matrix:
    return [[t * value for value in row] for row in W]


def susceptibility_from_star(W: Matrix) -> Fraction:
    analysis = finite_recurrent_mass_analysis(W)
    if not analysis.stable or analysis.star is None:
        raise ValueError("matrix is not stable")
    return sum((analysis.star[i][i] - 1 for i in range(len(W))), Q(0))


def check_criticality_polynomials() -> None:
    one = [[Q(3, 5)]]
    D, p, _ = criticality_polynomial(one)
    assert D == 5 and p == [5, -3]
    t_c = Q(5, 3)
    assert poly_eval(p, t_c) == 0
    assert finite_recurrent_mass_analysis(scale_matrix(one, Q(3, 2))).stable
    assert not finite_recurrent_mass_analysis(scale_matrix(one, t_c)).stable
    assert not finite_recurrent_mass_analysis(scale_matrix(one, Q(2))).stable

    two = [[Q(0), Q(1, 2)], [Q(1, 2), Q(2, 3)]]
    D2, p2, _ = criticality_polynomial(two)
    assert D2 == 6 and p2 == [36, -24, -9]
    assert poly_eval(p2, Q(1)) > 0
    assert poly_eval(p2, Q(6, 5)) < 0
    assert finite_recurrent_mass_analysis(two).stable
    assert not finite_recurrent_mass_analysis(scale_matrix(two, Q(6, 5))).stable

    cycle = [[Q(0), Q(2), Q(0)], [Q(0), Q(0), Q(1, 3)], [Q(1, 4), Q(0), Q(0)]]
    D3, p3, _ = criticality_polynomial(cycle)
    assert D3 == 12
    assert p3 == [12**3, 0, 0, -(24 * 4 * 3)]
    assert poly_eval(p3, Q(1)) > 0
    assert poly_eval(p3, Q(2)) < 0
    assert finite_recurrent_mass_analysis(cycle).stable
    assert not finite_recurrent_mass_analysis(scale_matrix(cycle, Q(2))).stable

    dag = [[Q(0), Q(2), Q(0)], [Q(0), Q(0), Q(3)], [Q(0), Q(0), Q(0)]]
    D4, p4, _ = criticality_polynomial(dag)
    assert D4 == 1 and p4 == [1]
    for t in [Q(0), Q(1), Q(10), Q(100)]:
        assert finite_recurrent_mass_analysis(scale_matrix(dag, t)).stable


def check_exact_susceptibility_rational_function() -> None:
    examples = [
        [[Q(3, 5)]],
        [[Q(0), Q(1, 2)], [Q(1, 2), Q(2, 3)]],
        [[Q(0), Q(2), Q(0)], [Q(0), Q(0), Q(1, 3)], [Q(1, 4), Q(0), Q(0)]],
    ]
    for W in examples:
        _, p, _ = criticality_polynomial(W)
        p_prime = poly_derivative(p)
        for t in [Q(1, 4), Q(1, 2), Q(3, 4), Q(1)]:
            scaled = scale_matrix(W, t)
            analysis = finite_recurrent_mass_analysis(scaled)
            if not analysis.stable:
                continue
            polynomial_value = poly_eval(p, t)
            assert polynomial_value > 0
            exact = -t * poly_eval(p_prime, t) / polynomial_value
            assert exact == susceptibility_from_star(scaled)

    # One-state susceptibility diverges monotonically along an exact rational
    # sequence approaching t_c=5/3 from below.
    one = [[Q(3, 5)]]
    values: list[Fraction] = []
    for n in [2, 3, 4, 5, 8, 16, 32, 64]:
        t = Q(5, 3) - Q(1, n)
        if t <= 0:
            continue
        values.append(susceptibility_from_star(scale_matrix(one, t)))
    assert all(values[i] < values[i + 1] for i in range(len(values) - 1))
    assert values[-1] > 50


def check_rational_certificate_critical_lower_bound() -> None:
    W = [[Q(0), Q(1, 2)], [Q(1, 2), Q(2, 3)]]
    analysis = finite_recurrent_mass_analysis(W)
    assert analysis.stable and analysis.canonical_potential is not None
    h = list(analysis.canonical_potential)
    stepped = [
        sum((W[i][j] * h[j] for j in range(2)), Q(0))
        for i in range(2)
    ]
    alpha = max(stepped[i] / h[i] for i in range(2))
    assert alpha == Q(17, 18)
    lower = Q(1) / alpha
    assert lower == Q(18, 17) > 1
    certified_scale = (Q(1) + lower) / 2
    assert certified_scale < lower
    assert finite_recurrent_mass_analysis(scale_matrix(W, certified_scale)).stable


def main() -> int:
    check_edge_support_detector()
    check_strongly_connected_hessian_geometry()
    check_general_graph_transient_kernel()
    check_integer_response_certificates()
    check_criticality_polynomials()
    check_exact_susceptibility_rational_function()
    check_rational_certificate_critical_lower_bound()
    print("BRC loop response / criticality exact checks: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
