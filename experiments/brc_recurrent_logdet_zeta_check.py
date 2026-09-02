#!/usr/bin/env python3
"""Exact checks for recurrent Weighted-BRC logdet / loop-zeta candidates.

All theorem evidence below uses integers and Fraction arithmetic.  No floating
spectral routine or floating logarithm is used.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from math import gcd, lcm

from enterprise_math.brc_weighted_recurrent import (
    finite_recurrent_mass_analysis,
    gauge_recurrent_mass_matrix,
    recurrent_mass_power,
)

Q = Fraction
Matrix = list[list[Fraction]]
IntMatrix = list[list[int]]


def common_denominator(matrix: Matrix) -> int:
    result = 1
    for row in matrix:
        for value in row:
            result = lcm(result, value.denominator)
    return result


def integer_stability_matrix(matrix: Matrix) -> tuple[int, IntMatrix, IntMatrix]:
    n = len(matrix)
    D = common_denominator(matrix)
    A = [[int(matrix[i][j] * D) for j in range(n)] for i in range(n)]
    B = [[D * int(i == j) - A[i][j] for j in range(n)] for i in range(n)]
    return D, A, B


def det_int(matrix: IntMatrix) -> int:
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be nonempty and square")
    if n == 1:
        return matrix[0][0]
    work = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for k in range(n - 1):
        pivot_row = next((r for r in range(k, n) if work[r][k] != 0), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            work[k], work[pivot_row] = work[pivot_row], work[k]
            sign *= -1
        pivot = work[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = work[i][j] * pivot - work[i][k] * work[k][j]
                if numerator % previous != 0:
                    raise AssertionError("Bareiss division lost exactness")
                work[i][j] = numerator // previous
        for i in range(k + 1, n):
            work[i][k] = 0
        previous = pivot
    return sign * work[n - 1][n - 1]


def minor(matrix: IntMatrix, row: int, col: int) -> IntMatrix:
    return [
        [matrix[i][j] for j in range(len(matrix)) if j != col]
        for i in range(len(matrix))
        if i != row
    ]


def adjugate_times_one(matrix: IntMatrix) -> list[int]:
    n = len(matrix)
    if n == 1:
        return [1]
    # h_i=sum_j adj(B)_{ij}=sum_j cofactor(B)_{j i}.
    result: list[int] = []
    for i in range(n):
        value = 0
        for j in range(n):
            cofactor = det_int(minor(matrix, j, i))
            if (i + j) & 1:
                cofactor = -cofactor
            value += cofactor
        result.append(value)
    return result


def mat_vec_int(matrix: IntMatrix, vector: list[int]) -> list[int]:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def primitive(vector: list[int]) -> list[int]:
    g = 0
    for value in vector:
        g = gcd(g, abs(value))
    return [value // g for value in vector] if g > 1 else vector[:]


def det_fraction(matrix: Matrix | tuple[tuple[Fraction, ...], ...]) -> Fraction:
    rows = [[Fraction(value) for value in row] for row in matrix]
    D = common_denominator(rows)
    integer = [[int(value * D) for value in row] for row in rows]
    return Q(det_int(integer), D ** len(rows))


def loop_zeta_ratio(matrix: Matrix) -> Fraction:
    analysis = finite_recurrent_mass_analysis(matrix)
    if not analysis.stable:
        raise ValueError("loop zeta ratio is a finite positive readout only on stable matrices")
    D, _, B = integer_stability_matrix(matrix)
    detB = det_int(B)
    if detB <= 0:
        raise AssertionError("stable matrix must have positive stability determinant")
    return Q(D ** len(matrix), detB)


def has_support_cycle(matrix: Matrix) -> bool:
    n = len(matrix)
    graph = [[j for j in range(n) if matrix[i][j] > 0] for i in range(n)]
    state = [0] * n

    def visit(v: int) -> bool:
        state[v] = 1
        for w in graph[v]:
            if state[w] == 1:
                return True
            if state[w] == 0 and visit(w):
                return True
        state[v] = 2
        return False

    return any(state[v] == 0 and visit(v) for v in range(n))


def matmul(left: Matrix, right: Matrix) -> Matrix:
    n = len(left)
    return [
        [sum((left[i][k] * right[k][j] for k in range(n)), Q(0)) for j in range(n)]
        for i in range(n)
    ]


def identity(n: int) -> Matrix:
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def trace(matrix: Matrix | tuple[tuple[Fraction, ...], ...]) -> Fraction:
    return sum((Fraction(matrix[i][i]) for i in range(len(matrix))), Q(0))


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(
        int(perm[i] > perm[j])
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return -1 if inversions & 1 else 1


def poly_mul(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def det_I_minus_tW_polynomial(matrix: Matrix) -> list[Fraction]:
    n = len(matrix)
    result = [Q(0)] * (n + 1)
    for perm in permutations(range(n)):
        term = [Q(1)]
        for i, j in enumerate(perm):
            # delta_ij - t W_ij
            term = poly_mul(term, [Q(int(i == j)), -matrix[i][j]])
        sign = permutation_sign(perm)
        for degree, value in enumerate(term):
            result[degree] += sign * value
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def negative_log_derivative_series(poly: list[Fraction], order: int) -> list[Fraction]:
    if poly[0] != 1:
        raise ValueError("polynomial must have constant term one")
    derivative_negative = [-(i + 1) * poly[i + 1] for i in range(len(poly) - 1)]
    qseries: list[Fraction] = []
    for m in range(order):
        rhs = derivative_negative[m] if m < len(derivative_negative) else Q(0)
        correction = sum(
            (
                poly[i] * qseries[m - i]
                for i in range(1, min(m, len(poly) - 1) + 1)
            ),
            Q(0),
        )
        qseries.append(rhs - correction)
    return qseries


def check_formal_trace_logdet_identity(matrix: Matrix, order: int = 8) -> None:
    poly = det_I_minus_tW_polynomial(matrix)
    series = negative_log_derivative_series(poly, order)
    power = identity(len(matrix))
    for m in range(order):
        power = matmul(power, matrix)
        assert series[m] == trace(power)


def check_625_determinant_potential_phase() -> None:
    values = [Q(0), Q(1, 3), Q(1, 2), Q(2, 3), Q(1)]
    stable_count = 0
    for entries in product(values, repeat=4):
        W = [list(entries[:2]), list(entries[2:])]
        analysis = finite_recurrent_mass_analysis(W)
        D, A, B = integer_stability_matrix(W)
        detB = det_int(B)
        h0 = adjugate_times_one(B)
        determinant_stable = detB > 0 and all(value > 0 for value in h0)
        assert determinant_stable == analysis.stable
        if not analysis.stable:
            continue

        stable_count += 1
        assert mat_vec_int(B, h0) == [detB, detB]
        assert mat_vec_int(A, h0) == [D * h0[i] - detB for i in range(2)]
        assert primitive(h0) == list(analysis.primitive_integer_potential)
        expected_potential = tuple(Q(D * value, detB) for value in h0)
        assert expected_potential == analysis.canonical_potential

        zeta = Q(D**2, detB)
        assert zeta == loop_zeta_ratio(W)
        assert zeta == det_fraction(analysis.star)
        assert zeta >= 1
        assert (zeta == 1) == (not has_support_cycle(W))

    assert stable_count == 254
    print(f"2x2 determinant phase: stable={stable_count} / 625")


def check_one_state_and_simple_cycle_reductions() -> None:
    one = [[Q(3, 5)]]
    assert loop_zeta_ratio(one) == Q(5, 2)

    cycle = [
        [Q(0), Q(2), Q(0)],
        [Q(0), Q(0), Q(1, 3)],
        [Q(1, 4), Q(0), Q(0)],
    ]
    Qcycle = Q(2) * Q(1, 3) * Q(1, 4)
    assert Qcycle == Q(1, 6)
    assert finite_recurrent_mass_analysis(cycle).stable
    assert loop_zeta_ratio(cycle) == Q(1, 1) / (1 - Qcycle) == Q(6, 5)
    assert det_fraction(
        [[Q(int(i == j)) - cycle[i][j] for j in range(3)] for i in range(3)]
    ) == 1 - Qcycle


def check_gauge_invariance() -> None:
    W = [[Q(0), Q(1, 2)], [Q(1, 2), Q(2, 3)]]
    h = [Q(10), Q(18)]
    gauged_tuple = gauge_recurrent_mass_matrix(W, h)
    G = [list(row) for row in gauged_tuple]
    assert loop_zeta_ratio(W) == Q(12)
    assert loop_zeta_ratio(G) == Q(12)
    assert det_fraction(
        [[Q(int(i == j)) - W[i][j] for j in range(2)] for i in range(2)]
    ) == det_fraction(
        [[Q(int(i == j)) - G[i][j] for j in range(2)] for i in range(2)]
    )
    for k in range(1, 7):
        assert trace(recurrent_mass_power(W, k)) == trace(recurrent_mass_power(G, k))


def check_scc_additivity_and_transient_blindness() -> None:
    left = [[Q(1, 4)]]
    right = [[Q(1, 3)]]
    z_product = loop_zeta_ratio(left) * loop_zeta_ratio(right)
    assert z_product == Q(2)

    for bridge in [Q(0), Q(1, 2), Q(5), Q(17, 3)]:
        W = [[Q(1, 4), bridge], [Q(0), Q(1, 3)]]
        analysis = finite_recurrent_mass_analysis(W)
        assert analysis.stable
        assert loop_zeta_ratio(W) == z_product
        check_formal_trace_logdet_identity(W)


def check_acyclic_zero_law() -> None:
    dag = [
        [Q(0), Q(2), Q(0)],
        [Q(0), Q(0), Q(3)],
        [Q(0), Q(0), Q(0)],
    ]
    assert finite_recurrent_mass_analysis(dag).stable
    assert not has_support_cycle(dag)
    assert loop_zeta_ratio(dag) == 1
    for k in range(1, 6):
        assert trace(recurrent_mass_power(dag, k)) == 0

    recurrent = [
        [Q(0), Q(1, 2)],
        [Q(1, 3), Q(0)],
    ]
    assert finite_recurrent_mass_analysis(recurrent).stable
    assert has_support_cycle(recurrent)
    assert loop_zeta_ratio(recurrent) == Q(6, 5) > 1


def check_formal_trace_identity_examples() -> None:
    examples = [
        [[Q(3, 5)]],
        [[Q(0), Q(1, 2)], [Q(1, 2), Q(2, 3)]],
        [[Q(0), Q(2), Q(0)], [Q(0), Q(0), Q(1, 3)], [Q(1, 4), Q(0), Q(0)]],
        [[Q(0), Q(2), Q(0)], [Q(0), Q(0), Q(3)], [Q(0), Q(0), Q(0)]],
    ]
    for W in examples:
        check_formal_trace_logdet_identity(W, order=10)


def main() -> int:
    check_625_determinant_potential_phase()
    check_one_state_and_simple_cycle_reductions()
    check_gauge_invariance()
    check_scc_additivity_and_transient_blindness()
    check_acyclic_zero_law()
    check_formal_trace_identity_examples()
    print("BRC recurrent logdet / loop-zeta exact checks: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
