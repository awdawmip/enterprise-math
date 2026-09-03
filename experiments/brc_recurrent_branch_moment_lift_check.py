#!/usr/bin/env python3
"""Exact checks for the BRC recurrent explicit-branch moment lift."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import product

Matrix = list[list[Q]]
Edge = tuple[int, int, Q]


def eye(n: int) -> Matrix:
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def mat_sub(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0)) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def mat_pow(matrix: Matrix, exponent: int) -> Matrix:
    result = eye(len(matrix))
    base = [row[:] for row in matrix]
    power = exponent
    while power:
        if power & 1:
            result = mat_mul(result, base)
        base = mat_mul(base, base)
        power >>= 1
    return result


def inverse(matrix: Matrix) -> Matrix | None:
    n = len(matrix)
    aug = [matrix[i][:] + [Q(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
        if pivot is None:
            return None
        aug[col], aug[pivot] = aug[pivot], aug[col]
        pv = aug[col][col]
        aug[col] = [value / pv for value in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            if factor:
                aug[row] = [aug[row][j] - factor * aug[col][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def stable_star(matrix: Matrix) -> tuple[bool, Matrix | None]:
    star = inverse(mat_sub(eye(len(matrix)), matrix))
    if star is None or any(value < 0 for row in star for value in row):
        return False, None
    return True, star


def branch_power_sum(weights: tuple[Q, ...], moment: int) -> Q:
    assert moment >= 0
    return sum((weight**moment for weight in weights), Q(0))


def moment_matrix(vertex_count: int, edges: list[Edge], moment: int) -> Matrix:
    assert moment >= 0
    matrix = [[Q(0) for _ in range(vertex_count)] for _ in range(vertex_count)]
    for source, target, weight in edges:
        assert weight > 0
        matrix[source][target] += weight**moment
    return matrix


def explicit_walk_weights(
    vertex_count: int,
    edges: list[Edge],
    source: int,
    target: int,
    length: int,
) -> list[Q]:
    outgoing: list[list[tuple[int, Q]]] = [[] for _ in range(vertex_count)]
    for start, end, weight in edges:
        outgoing[start].append((end, weight))
    weights: list[Q] = []

    def walk(state: int, depth: int, mass: Q) -> None:
        if depth == length:
            if state == target:
                weights.append(mass)
            return
        for end, weight in outgoing[state]:
            walk(end, depth + 1, mass * weight)

    walk(source, 0, Q(1))
    return weights


def check_branch_semiring_characters() -> int:
    values = [Q(1, 2), Q(1), Q(2)]
    families = [
        tuple(combo)
        for length in [1, 2, 3]
        for combo in product(values, repeat=length)
    ]
    checks = 0
    for left in families:
        for right in families:
            union = left + right
            serial = tuple(a * b for a in left for b in right)
            for moment in range(5):
                assert branch_power_sum(union, moment) == (
                    branch_power_sum(left, moment) + branch_power_sum(right, moment)
                )
                assert branch_power_sum(serial, moment) == (
                    branch_power_sum(left, moment) * branch_power_sum(right, moment)
                )
                checks += 2
    return checks


def check_explicit_multigraph_moments() -> tuple[int, int]:
    edges: list[Edge] = [
        (0, 0, Q(1, 2)),
        (0, 0, Q(1, 3)),
        (0, 1, Q(2, 3)),
        (1, 1, Q(1, 6)),
        (1, 2, Q(3, 4)),
        (1, 2, Q(1, 4)),
        (2, 0, Q(1, 5)),
    ]
    path_checks = 0
    cwm_checks = 0
    moment_matrices = {moment: moment_matrix(3, edges, moment) for moment in range(7)}

    for length in range(5):
        powers = {moment: mat_pow(matrix, length) for moment, matrix in moment_matrices.items()}
        for source in range(3):
            for target in range(3):
                path_weights = explicit_walk_weights(3, edges, source, target, length)
                for moment in range(7):
                    explicit_sum = sum((weight**moment for weight in path_weights), Q(0))
                    assert explicit_sum == powers[moment][source][target]
                    path_checks += 1
                if not path_weights:
                    continue
                count = len(path_weights)
                total = sum(path_weights, Q(0))
                dominant = max(path_weights)
                assert powers[0][source][target] == count
                assert powers[1][source][target] == total
                for moment in range(1, 7):
                    s_m = powers[moment][source][target]
                    assert dominant**moment <= s_m <= count * dominant**moment
                    cwm_checks += 1

    # Equality controls for the sandwich.
    equal_weights = (Q(2, 5),) * 4
    for moment in range(1, 7):
        s_m = branch_power_sum(equal_weights, moment)
        assert s_m == len(equal_weights) * max(equal_weights) ** moment
    one_path = (Q(7, 11),)
    for moment in range(1, 7):
        assert branch_power_sum(one_path, moment) == max(one_path) ** moment

    return path_checks, cwm_checks


def check_mass_aggregation_nonrecoverability() -> None:
    one = [(0, 1, Q(1))]
    two = [(0, 1, Q(1, 2)), (0, 1, Q(1, 2))]
    assert moment_matrix(2, one, 1) == moment_matrix(2, two, 1)
    assert moment_matrix(2, one, 0) != moment_matrix(2, two, 0)
    assert moment_matrix(2, one, 2) != moment_matrix(2, two, 2)
    assert moment_matrix(2, one, 0)[0][1] == 1
    assert moment_matrix(2, two, 0)[0][1] == 2
    assert moment_matrix(2, one, 2)[0][1] == 1
    assert moment_matrix(2, two, 2)[0][1] == Q(1, 2)


def check_count_generating_star() -> None:
    # DAG with two parallel 0->1 branches, one 1->2 branch and one 0->2 branch.
    dag_edges: list[Edge] = [
        (0, 1, Q(1, 2)),
        (0, 1, Q(3, 4)),
        (1, 2, Q(2, 3)),
        (0, 2, Q(1, 5)),
    ]
    count = moment_matrix(3, dag_edges, 0)
    assert count == [[0, 2, 1], [0, 0, 1], [0, 0, 0]]
    stable, star = stable_star(count)
    assert stable and star is not None
    finite_sum = eye(3)
    power = eye(3)
    for _ in range(1, 3):
        power = mat_mul(power, count)
        finite_sum = [[finite_sum[i][j] + power[i][j] for j in range(3)] for i in range(3)]
    assert star == finite_sum
    assert star[0][2] == 3  # direct path plus two choices through state 1

    cycle_edges: list[Edge] = [(0, 1, Q(1, 2)), (1, 0, Q(1, 2))]
    cycle_count = moment_matrix(2, cycle_edges, 0)
    assert cycle_count == [[0, 1], [1, 0]]
    assert not stable_star(cycle_count)[0]
    scaled = [[Q(1, 2) * value for value in row] for row in cycle_count]
    stable_scaled, star_scaled = stable_star(scaled)
    assert stable_scaled and star_scaled is not None
    assert star_scaled == [[Q(4, 3), Q(2, 3)], [Q(2, 3), Q(4, 3)]]


def check_equal_loop_critical_law() -> None:
    k = 3
    q = Q(2, 5)
    for moment in range(5):
        s_m = k * q**moment
        matrix = [[s_m]]
        critical_z = 1 / s_m
        assert not stable_star([[critical_z * s_m]])[0]
        stable, star = stable_star([[critical_z * s_m / 2]])
        assert stable and star == [[Q(2)]]
        # Scalar critical polynomial after clearing denominators has this exact root.
        numerator, denominator = s_m.numerator, s_m.denominator
        assert denominator - critical_z * numerator == 0


def check_moment_phase_separation() -> None:
    edges = [(0, 0, Q(3, 5)), (0, 0, Q(3, 5))]
    first = moment_matrix(1, edges, 1)
    second = moment_matrix(1, edges, 2)
    assert first == [[Q(6, 5)]]
    assert second == [[Q(18, 25)]]
    assert not stable_star(first)[0]
    stable, star = stable_star(second)
    assert stable and star == [[Q(25, 7)]]


def main() -> int:
    semiring_checks = check_branch_semiring_characters()
    path_checks, cwm_checks = check_explicit_multigraph_moments()
    check_mass_aggregation_nonrecoverability()
    check_count_generating_star()
    check_equal_loop_critical_law()
    check_moment_phase_separation()
    print("BRC recurrent branch moment lift exact checker: PASS")
    print(f"semiring_checks={semiring_checks}")
    print(f"path_moment_checks={path_checks}")
    print(f"cwm_sandwich_checks={cwm_checks}")
    print("mass_nonrecoverability=PASS")
    print("count_generating_star=PASS")
    print("equal_loop_critical_law=PASS")
    print("moment_phase_separation=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
