#!/usr/bin/env python3
"""Exact checks for finite recurrent positive Weighted-BRC mass stability.

The experiment uses only integers and Fraction arithmetic for theorem evidence.
Floating eigenvalues are deliberately absent from the decision path.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import gcd, lcm

Q = Fraction
Matrix = list[list[Fraction]]
Vector = list[Fraction]


def square_size(matrix: Matrix) -> int:
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be nonempty and square")
    return n


def validate_mass_matrix(matrix: Matrix) -> int:
    n = square_size(matrix)
    if any(value < 0 for row in matrix for value in row):
        raise ValueError("mass matrix must be non-negative")
    return n


def identity(n: int) -> Matrix:
    return [[Q(int(i == j), 1) for j in range(n)] for i in range(n)]


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    n = square_size(left)
    if square_size(right) != n:
        raise ValueError("dimension mismatch")
    return [[left[i][j] + right[i][j] for j in range(n)] for i in range(n)]


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    n = square_size(left)
    if square_size(right) != n:
        raise ValueError("dimension mismatch")
    return [[left[i][j] - right[i][j] for j in range(n)] for i in range(n)]


def matrix_mul(left: Matrix, right: Matrix) -> Matrix:
    n = square_size(left)
    if square_size(right) != n:
        raise ValueError("dimension mismatch")
    return [
        [sum((left[i][k] * right[k][j] for k in range(n)), Q(0, 1)) for j in range(n)]
        for i in range(n)
    ]


def matrix_pow(matrix: Matrix, exponent: int) -> Matrix:
    n = validate_mass_matrix(matrix)
    if exponent < 0:
        raise ValueError("exponent must be non-negative")
    result = identity(n)
    base = [row[:] for row in matrix]
    power = exponent
    while power:
        if power & 1:
            result = matrix_mul(result, base)
        base = matrix_mul(base, base)
        power >>= 1
    return result


def matrix_vec(matrix: Matrix, vector: Vector) -> Vector:
    n = square_size(matrix)
    if len(vector) != n:
        raise ValueError("dimension mismatch")
    return [sum((matrix[i][j] * vector[j] for j in range(n)), Q(0, 1)) for i in range(n)]


def left_vec_matrix(vector: Vector, matrix: Matrix) -> Vector:
    n = square_size(matrix)
    if len(vector) != n:
        raise ValueError("dimension mismatch")
    return [sum((vector[i] * matrix[i][j] for i in range(n)), Q(0, 1)) for j in range(n)]


def inverse(matrix: Matrix) -> Matrix | None:
    n = square_size(matrix)
    aug = [
        [Fraction(value) for value in matrix[i]]
        + [Q(int(i == j), 1) for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        pivot = next((row for row in range(col, n) if aug[row][col] != 0), None)
        if pivot is None:
            return None
        aug[col], aug[pivot] = aug[pivot], aug[col]
        pivot_value = aug[col][col]
        aug[col] = [entry / pivot_value for entry in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            if factor:
                aug[row] = [aug[row][j] - factor * aug[col][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def row_sums(matrix: Matrix) -> Vector:
    square_size(matrix)
    return [sum(row, Q(0, 1)) for row in matrix]


def stable_analysis(matrix: Matrix) -> tuple[bool, Vector | None, Matrix | None]:
    n = validate_mass_matrix(matrix)
    resolvent = matrix_sub(identity(n), matrix)
    star = inverse(resolvent)
    if star is None:
        return False, None, None
    potential = [sum(star[i], Q(0, 1)) for i in range(n)]
    stable = all(value > 0 for value in potential)
    if stable:
        assert all(entry >= 0 for row in star for entry in row)
        assert matrix_vec(matrix, potential) == [value - 1 for value in potential]
    return stable, potential, star


def common_denominator(matrix: Matrix) -> int:
    validate_mass_matrix(matrix)
    result = 1
    for row in matrix:
        for entry in row:
            result = lcm(result, entry.denominator)
    return result


def integer_mass_matrix(matrix: Matrix) -> tuple[int, list[list[int]]]:
    denominator = common_denominator(matrix)
    return denominator, [[int(entry * denominator) for entry in row] for row in matrix]


def primitive_integer_vector(vector: Vector) -> list[int]:
    denominator = 1
    for value in vector:
        denominator = lcm(denominator, value.denominator)
    integers = [int(value * denominator) for value in vector]
    common = 0
    for value in integers:
        common = gcd(common, abs(value))
    if common > 1:
        integers = [value // common for value in integers]
    return integers


def verify_integer_stable_certificate(matrix: Matrix, certificate: list[int]) -> bool:
    n = validate_mass_matrix(matrix)
    if len(certificate) != n or any(value <= 0 for value in certificate):
        return False
    denominator, integer_matrix = integer_mass_matrix(matrix)
    for i in range(n):
        lhs = sum(integer_matrix[i][j] * certificate[j] for j in range(n))
        if not lhs < denominator * certificate[i]:
            return False
    return True


def verify_left_divergence_certificate(matrix: Matrix, certificate: list[int]) -> bool:
    n = validate_mass_matrix(matrix)
    if len(certificate) != n or any(value < 0 for value in certificate) or not any(certificate):
        return False
    y = [Q(value, 1) for value in certificate]
    stepped = left_vec_matrix(y, matrix)
    return all(stepped[j] >= y[j] for j in range(n))


def gauge_matrix(matrix: Matrix, potential: Vector) -> Matrix:
    n = validate_mass_matrix(matrix)
    if len(potential) != n or any(value <= 0 for value in potential):
        raise ValueError("gauge potential must be positive")
    return [[matrix[i][j] * potential[j] / potential[i] for j in range(n)] for i in range(n)]


def contraction_factor(matrix: Matrix, potential: Vector) -> Fraction:
    validate_mass_matrix(matrix)
    ratios = [value / potential[i] for i, value in enumerate(matrix_vec(matrix, potential))]
    return max(ratios)


def star_bound(matrix: Matrix, potential: Vector, i: int, j: int) -> Fraction:
    alpha = contraction_factor(matrix, potential)
    if not alpha < 1:
        raise ValueError("potential is not a stability certificate")
    return (potential[i] / potential[j]) / (1 - alpha)


EdgeTable = list[list[tuple[Fraction, ...]]]


def aggregate_edges(edges: EdgeTable) -> Matrix:
    n = len(edges)
    if n == 0 or any(len(row) != n for row in edges):
        raise ValueError("edge table must be square")
    return [[sum(edges[i][j], Q(0, 1)) for j in range(n)] for i in range(n)]


def explicit_walk_mass(edges: EdgeTable, start: int, end: int, length: int) -> Fraction:
    n = len(edges)
    if length == 0:
        return Q(int(start == end), 1)
    total = Q(0, 1)

    def walk(state: int, depth: int, mass: Fraction) -> None:
        nonlocal total
        if depth == length:
            if state == end:
                total += mass
            return
        for target in range(n):
            for edge_weight in edges[state][target]:
                walk(target, depth + 1, mass * edge_weight)

    walk(start, 0, Q(1, 1))
    return total


def check_path_mass_matrix() -> None:
    edges: EdgeTable = [
        [(Q(1, 4), Q(1, 8)), (Q(1, 3),)],
        [(Q(1, 5), Q(1, 10)), (Q(1, 7),)],
    ]
    mass = aggregate_edges(edges)
    for length in range(0, 5):
        powered = matrix_pow(mass, length)
        for start in range(2):
            for end in range(2):
                assert explicit_walk_mass(edges, start, end, length) == powered[start][end]


def check_stable_raw_supercritical_example() -> None:
    mass = [[Q(0, 1), Q(1, 2)], [Q(1, 2), Q(2, 3)]]
    assert row_sums(mass) == [Q(1, 2), Q(7, 6)]

    stable, potential, star = stable_analysis(mass)
    assert stable
    assert potential == [Q(10, 1), Q(18, 1)]
    assert star == [[Q(4, 1), Q(6, 1)], [Q(6, 1), Q(12, 1)]]
    assert matrix_mul(matrix_sub(identity(2), mass), star) == identity(2)

    integer_potential = primitive_integer_vector(potential)
    assert integer_potential == [5, 9]
    assert verify_integer_stable_certificate(mass, integer_potential)

    gauged = gauge_matrix(mass, potential)
    assert row_sums(gauged) == [Q(9, 10), Q(17, 18)]
    assert [1 - row for row in row_sums(gauged)] == [Q(1, 10), Q(1, 18)]

    for i in range(2):
        for j in range(2):
            assert star[i][j] <= star_bound(mass, potential, i, j)

    for length in range(1, 7):
        for vertices in product(range(2), repeat=length + 1):
            raw = Q(1, 1)
            gauged_product = Q(1, 1)
            live = True
            for step in range(length):
                a = vertices[step]
                b = vertices[step + 1]
                if mass[a][b] == 0:
                    live = False
                    break
                raw *= mass[a][b]
                gauged_product *= gauged[a][b]
            if not live:
                continue
            assert gauged_product == raw * potential[vertices[-1]] / potential[vertices[0]]
            if vertices[-1] == vertices[0]:
                assert gauged_product == raw


def check_dominant_stable_total_unstable_example() -> None:
    mass = [[Q(3, 5), Q(3, 5)], [Q(3, 5), Q(3, 5)]]
    stable, potential, star = stable_analysis(mass)
    assert not stable
    assert star is not None
    assert potential == [Q(-5, 1), Q(-5, 1)]
    assert verify_left_divergence_certificate(mass, [1, 1])
    assert left_vec_matrix([Q(1), Q(1)], mass) == [Q(6, 5), Q(6, 5)]

    for length in range(1, 8):
        dominant = Q(3, 5) ** length
        assert dominant < 1
        total_from_state = sum(matrix_pow(mass, length)[0], Q(0, 1))
        assert total_from_state == Q(6, 5) ** length


def check_one_state_reduction() -> None:
    stable_mass = [[Q(3, 5)]]
    stable, potential, star = stable_analysis(stable_mass)
    assert stable
    assert star == [[Q(5, 2)]]
    assert potential == [Q(5, 2)]
    assert verify_integer_stable_certificate(stable_mass, [1])

    unstable_mass = [[Q(6, 5)]]
    stable, _, _ = stable_analysis(unstable_mass)
    assert not stable
    assert verify_left_divergence_certificate(unstable_mass, [1])


def search_small_integer_dual(matrix: Matrix, bound: int = 6) -> list[int] | None:
    n = len(matrix)
    for values in product(range(bound + 1), repeat=n):
        if not any(values):
            continue
        candidate = list(values)
        if verify_left_divergence_certificate(matrix, candidate):
            return candidate
    return None


def check_small_2x2_phase_dichotomy() -> None:
    values = [Q(0), Q(1, 3), Q(1, 2), Q(2, 3), Q(1)]
    total = stable_count = unstable_count = 0
    for entries in product(values, repeat=4):
        mass = [list(entries[:2]), list(entries[2:])]
        stable, potential, star = stable_analysis(mass)
        total += 1
        if stable:
            stable_count += 1
            assert potential is not None and star is not None
            integer_potential = primitive_integer_vector(potential)
            assert verify_integer_stable_certificate(mass, integer_potential)
            gauged = gauge_matrix(mass, potential)
            assert all(row < 1 for row in row_sums(gauged))
            assert search_small_integer_dual(mass) is None
        else:
            unstable_count += 1
            dual = search_small_integer_dual(mass)
            assert dual is not None
            assert verify_left_divergence_certificate(mass, dual)
    assert total == 625
    assert stable_count > 0 and unstable_count > 0
    print(f"2x2 exhaustive: total={total} stable={stable_count} unstable={unstable_count}")


def check_gauge_generated_stable_family() -> None:
    bases = [
        [
            [Q(1, 5), Q(1, 4), Q(1, 10)],
            [Q(1, 6), Q(1, 5), Q(1, 4)],
            [Q(1, 8), Q(1, 4), Q(1, 5)],
        ],
        [
            [Q(0), Q(1, 2), Q(1, 4)],
            [Q(1, 3), Q(0), Q(1, 3)],
            [Q(1, 4), Q(1, 4), Q(0)],
        ],
    ]
    potentials = [[Q(1), Q(3), Q(7)], [Q(5), Q(2), Q(9)]]
    saw_raw_supercritical = False
    for base in bases:
        assert all(row < 1 for row in row_sums(base))
        for h in potentials:
            n = len(base)
            mass = [[base[i][j] * h[i] / h[j] for j in range(n)] for i in range(n)]
            assert gauge_matrix(mass, h) == base
            if any(row >= 1 for row in row_sums(mass)):
                saw_raw_supercritical = True
            stable, canonical, star = stable_analysis(mass)
            assert stable and canonical is not None and star is not None
            assert verify_integer_stable_certificate(mass, primitive_integer_vector(canonical))
    assert saw_raw_supercritical


def check_stable_vs_dual_mutual_exclusion() -> None:
    mass = [[Q(0), Q(1, 2)], [Q(1, 2), Q(2, 3)]]
    stable, potential, _ = stable_analysis(mass)
    assert stable and potential is not None
    h = primitive_integer_vector(potential)
    assert verify_integer_stable_certificate(mass, h)
    assert search_small_integer_dual(mass, bound=20) is None


def main() -> int:
    check_path_mass_matrix()
    check_stable_raw_supercritical_example()
    check_dominant_stable_total_unstable_example()
    check_one_state_reduction()
    check_small_2x2_phase_dichotomy()
    check_gauge_generated_stable_family()
    check_stable_vs_dual_mutual_exclusion()
    print("finite recurrent BRC rational gauge stability: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
