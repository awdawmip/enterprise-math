#!/usr/bin/env python3
"""Exact checks for BRC moment/length-safe port transfer."""

from __future__ import annotations

from fractions import Fraction as Q

Matrix = list[list[Q]]
Edge = tuple[int, int, Q]


def eye(n: int) -> Matrix:
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def zeros(rows: int, cols: int) -> Matrix:
    return [[Q(0) for _ in range(cols)] for _ in range(rows)]


def mat_add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_sub(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_scale(s: Q, a: Matrix) -> Matrix:
    return [[s * value for value in row] for row in a]


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    if not a or not b:
        return []
    assert len(a[0]) == len(b)
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
    if n == 0:
        return []
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


def determinant(matrix: Matrix) -> Q:
    if not matrix:
        return Q(1)
    work = [row[:] for row in matrix]
    n = len(work)
    out = Q(1)
    sign = 1
    for col in range(n):
        pivot = next((r for r in range(col, n) if work[r][col] != 0), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            sign *= -1
        pv = work[col][col]
        out *= pv
        for row in range(col + 1, n):
            factor = work[row][col] / pv
            for j in range(col, n):
                work[row][j] -= factor * work[col][j]
    return sign * out


def stable_star(matrix: Matrix) -> tuple[bool, Matrix | None]:
    star = inverse(mat_sub(eye(len(matrix)), matrix))
    if star is None or any(value < 0 for row in star for value in row):
        return False, None
    return True, star


def submatrix(matrix: Matrix, rows: list[int], cols: list[int]) -> Matrix:
    return [[matrix[i][j] for j in cols] for i in rows]


def boundary_block(matrix: Matrix, boundary: list[int]) -> Matrix:
    return submatrix(matrix, boundary, boundary)


def moment_matrix(vertex_count: int, edges: list[Edge], moment: int) -> Matrix:
    matrix = zeros(vertex_count, vertex_count)
    for source, target, weight in edges:
        assert weight > 0
        matrix[source][target] += weight**moment
    return matrix


def schur_kernel(kernel: Matrix, internal: list[int]) -> tuple[list[int], Matrix]:
    n = len(kernel)
    internal_set = set(internal)
    boundary = [i for i in range(n) if i not in internal_set]
    a = submatrix(kernel, internal, internal)
    x = submatrix(kernel, internal, boundary)
    y = submatrix(kernel, boundary, internal)
    b = submatrix(kernel, boundary, boundary)
    star_i = inverse(mat_sub(eye(len(a)), a))
    if star_i is None:
        raise ValueError("internal Schur denominator vanished")
    effective = mat_add(b, mat_mul(mat_mul(y, star_i), x))
    return boundary, effective


def moment_port_eval(matrix: Matrix, internal: list[int], z: Q) -> tuple[list[int], Matrix]:
    return schur_kernel(mat_scale(z, matrix), internal)


def segment_coefficients(matrix: Matrix, internal: list[int], max_length: int) -> tuple[list[int], list[Matrix]]:
    n = len(matrix)
    internal_set = set(internal)
    boundary = [i for i in range(n) if i not in internal_set]
    a = submatrix(matrix, internal, internal)
    x = submatrix(matrix, internal, boundary)
    y = submatrix(matrix, boundary, internal)
    b = submatrix(matrix, boundary, boundary)
    coeffs = [zeros(len(boundary), len(boundary)) for _ in range(max_length + 1)]
    if max_length >= 1:
        coeffs[1] = b
    for length in range(2, max_length + 1):
        coeffs[length] = mat_mul(mat_mul(y, mat_pow(a, length - 2)), x)
    return boundary, coeffs


def port_star_coefficients(segment_coeffs: list[Matrix], max_length: int) -> list[Matrix]:
    size = len(segment_coeffs[0])
    g = [zeros(size, size) for _ in range(max_length + 1)]
    g[0] = eye(size)
    # (I-E)G=I => G_n=sum_{ell=1..n} E_ell G_{n-ell}.
    for n in range(1, max_length + 1):
        total = zeros(size, size)
        for length in range(1, n + 1):
            total = mat_add(total, mat_mul(segment_coeffs[length], g[n - length]))
        g[n] = total
    return g


def check_formal_coefficient_semantics() -> tuple[int, int]:
    edges: list[Edge] = [
        (0, 0, Q(1, 5)),
        (0, 1, Q(1, 7)),
        (1, 0, Q(1, 11)),
        (1, 1, Q(1, 6)),
        (0, 2, Q(1, 3)),
        (0, 2, Q(1, 4)),
        (1, 3, Q(2, 5)),
        (2, 0, Q(1, 8)),
        (2, 1, Q(1, 9)),
        (2, 3, Q(1, 10)),
        (3, 0, Q(1, 12)),
        (3, 2, Q(1, 13)),
    ]
    internal = [0, 1]
    max_length = 7
    coefficient_checks = 0
    rational_checks = 0
    for moment in range(6):
        matrix = moment_matrix(4, edges, moment)
        boundary, segments = segment_coefficients(matrix, internal, max_length)
        assert boundary == [2, 3]
        port_coeffs = port_star_coefficients(segments, max_length)
        for length in range(max_length + 1):
            full_coeff = boundary_block(mat_pow(matrix, length), boundary)
            assert port_coeffs[length] == full_coeff
            coefficient_checks += 4

        for z in [Q(1, 20), Q(1, 10), Q(1, 5)]:
            full_kernel = mat_scale(z, matrix)
            full_star = inverse(mat_sub(eye(4), full_kernel))
            assert full_star is not None
            boundary_eval, effective = moment_port_eval(matrix, internal, z)
            assert boundary_eval == boundary
            port_star = inverse(mat_sub(eye(2), effective))
            assert port_star is not None
            assert boundary_block(full_star, boundary) == port_star
            a = submatrix(matrix, internal, internal)
            assert determinant(mat_sub(eye(4), full_kernel)) == (
                determinant(mat_sub(eye(2), mat_scale(z, a)))
                * determinant(mat_sub(eye(2), effective))
            )
            rational_checks += 1
    return coefficient_checks, rational_checks


def check_m1_z1_reduction() -> None:
    edges: list[Edge] = [
        (0, 0, Q(1, 5)),
        (0, 1, Q(1, 7)),
        (1, 0, Q(1, 11)),
        (0, 2, Q(1, 3)),
        (1, 3, Q(1, 4)),
        (2, 0, Q(1, 8)),
        (3, 1, Q(1, 9)),
        (2, 3, Q(1, 10)),
    ]
    matrix = moment_matrix(4, edges, 1)
    internal = [0, 1]
    a = submatrix(matrix, internal, internal)
    stable_a, _ = stable_star(a)
    assert stable_a
    boundary, effective = moment_port_eval(matrix, internal, Q(1))
    # Ordinary Schur W_eff is the same formula at m=1,z=1.
    boundary_again, ordinary = schur_kernel(matrix, internal)
    assert boundary == boundary_again == [2, 3]
    assert effective == ordinary


def check_count_self_loop_formal_repair() -> None:
    # state 0 hidden; boundary states 1=u, 2=v. One hidden self-loop,
    # u->hidden and hidden->v. At m=0 every explicit branch contributes 1.
    edges: list[Edge] = [
        (0, 0, Q(7, 11)),
        (1, 0, Q(2, 3)),
        (0, 2, Q(3, 5)),
    ]
    count = moment_matrix(3, edges, 0)
    boundary, segments = segment_coefficients(count, [0], 7)
    assert boundary == [1, 2]
    for length in range(2, 8):
        assert segments[length] == [[Q(0), Q(1)], [Q(0), Q(0)]]
    assert segments[1] == [[Q(0), Q(0)], [Q(0), Q(0)]]
    # Hidden count block [1] is not stable at z=1.
    assert not stable_star([[Q(1)]])[0]
    boundary_half, effective_half = moment_port_eval(count, [0], Q(1, 2))
    assert boundary_half == boundary
    assert effective_half == [[Q(0), Q(1, 2)], [Q(0), Q(0)]]
    # z^2/(1-z) at z=1/2 = 1/2.


def compose_context(
    matrix: Matrix,
    internal: list[int],
    context_weights: tuple[Q, Q, Q, Q],
    moment: int,
) -> tuple[Matrix, list[int]]:
    # One external state appended. Context weights are c(port0->port1),
    # u(port1->external), v(external->port0), r(external self-loop).
    n = len(matrix)
    internal_set = set(internal)
    boundary = [i for i in range(n) if i not in internal_set]
    assert len(boundary) == 2
    out = [row[:] + [Q(0)] for row in matrix] + [[Q(0) for _ in range(n + 1)]]
    c, u, v, r = context_weights
    out[boundary[0]][boundary[1]] += c**moment
    out[boundary[1]][n] += u**moment
    out[n][boundary[0]] += v**moment
    out[n][n] += r**moment
    return out, boundary + [n]


def reduced_context_kernel(
    effective: Matrix,
    context_weights: tuple[Q, Q, Q, Q],
    moment: int,
    z: Q,
) -> Matrix:
    c, u, v, r = context_weights
    # effective already contains z-scaled hidden-eliminated port transfer.
    return [
        [effective[0][0], effective[0][1] + z * c**moment, Q(0)],
        [effective[1][0], effective[1][1], z * u**moment],
        [z * v**moment, Q(0), z * r**moment],
    ]


def check_fixed_m_external_context() -> int:
    edges: list[Edge] = [
        (0, 0, Q(1, 8)),
        (0, 1, Q(1, 9)),
        (1, 0, Q(1, 10)),
        (0, 2, Q(1, 4)),
        (1, 3, Q(1, 5)),
        (2, 0, Q(1, 6)),
        (3, 1, Q(1, 7)),
        (2, 3, Q(1, 12)),
    ]
    internal = [0, 1]
    contexts = [
        (Q(1, 11), Q(1, 13), Q(1, 17), Q(1, 19)),
        (Q(1, 7), Q(1, 9), Q(1, 10), Q(1, 12)),
    ]
    checks = 0
    for moment in range(4):
        matrix = moment_matrix(4, edges, moment)
        for z in [Q(1, 20), Q(1, 10)]:
            boundary, effective = moment_port_eval(matrix, internal, z)
            assert boundary == [2, 3]
            for context in contexts:
                full_context_m, visible = compose_context(matrix, internal, context, moment)
                full_star = inverse(mat_sub(eye(5), mat_scale(z, full_context_m)))
                assert full_star is not None
                reduced_kernel = reduced_context_kernel(effective, context, moment, z)
                reduced_star = inverse(mat_sub(eye(3), reduced_kernel))
                assert reduced_star is not None
                assert submatrix(full_star, visible, visible) == reduced_star
                checks += 1
    return checks


def gauge_edges(edges: list[Edge], h: list[Q]) -> list[Edge]:
    return [(source, target, weight * h[target] / h[source]) for source, target, weight in edges]


def gauge_matrix(matrix: Matrix, h: list[Q]) -> Matrix:
    return [[matrix[i][j] * h[j] / h[i] for j in range(len(matrix))] for i in range(len(matrix))]


def check_moment_gauge_naturality() -> None:
    edges: list[Edge] = [
        (0, 0, Q(1, 8)),
        (0, 1, Q(1, 9)),
        (1, 0, Q(1, 10)),
        (0, 2, Q(1, 4)),
        (1, 3, Q(1, 5)),
        (2, 0, Q(1, 6)),
        (3, 1, Q(1, 7)),
        (2, 3, Q(1, 12)),
    ]
    h = [Q(2), Q(3), Q(5), Q(7)]
    gauged_edges = gauge_edges(edges, h)
    internal = [0, 1]
    for moment in range(5):
        matrix = moment_matrix(4, edges, moment)
        matrix_g = moment_matrix(4, gauged_edges, moment)
        h_m = [value**moment for value in h]
        assert matrix_g == gauge_matrix(matrix, h_m)
        for z in [Q(1, 10), Q(1, 5)]:
            boundary, effective = moment_port_eval(matrix, internal, z)
            boundary_g, effective_g = moment_port_eval(matrix_g, internal, z)
            assert boundary_g == boundary == [2, 3]
            expected = gauge_matrix(effective, [h_m[i] for i in boundary])
            assert effective_g == expected
            if moment == 0:
                assert effective_g == effective


def check_sequential_elimination() -> None:
    edges: list[Edge] = [
        (0, 0, Q(1, 10)), (0, 1, Q(1, 12)), (1, 0, Q(1, 14)),
        (1, 1, Q(1, 11)), (0, 2, Q(1, 8)), (1, 3, Q(1, 9)),
        (2, 0, Q(1, 13)), (3, 1, Q(1, 15)), (2, 3, Q(1, 17)),
        (3, 2, Q(1, 19)),
    ]
    for moment in range(4):
        matrix = moment_matrix(4, edges, moment)
        for z in [Q(1, 20), Q(1, 10)]:
            kernel = mat_scale(z, matrix)
            direct_boundary, direct = schur_kernel(kernel, [0, 1])
            first_boundary, first = schur_kernel(kernel, [0])
            assert first_boundary == [1, 2, 3]
            second_boundary, sequential = schur_kernel(first, [0])
            assert [first_boundary[i] for i in second_boundary] == direct_boundary == [2, 3]
            assert sequential == direct


def check_length_loss_witness() -> None:
    # A: direct edge u->v of mass 1; B: one hidden two-edge route product 1.
    direct = [[Q(0), Q(1)], [Q(0), Q(0)]]
    path = [
        [Q(0), Q(0), Q(1)],  # hidden -> v
        [Q(1), Q(0), Q(0)],  # u -> hidden
        [Q(0), Q(0), Q(0)],
    ]
    # path state order [hidden,u,v], internal=[0], boundary=[1,2].
    _, direct_half = moment_port_eval(direct, [], Q(1, 2)) if False else ([0, 1], mat_scale(Q(1, 2), direct))
    boundary_path, path_half = moment_port_eval(path, [0], Q(1, 2))
    assert boundary_path == [1, 2]
    assert direct_half[0][1] == Q(1, 2)
    assert path_half[0][1] == Q(1, 4)
    # At z=1 both ordinary total-mass port transfers equal 1.
    _, path_one = moment_port_eval(path, [0], Q(1))
    assert direct[0][1] == path_one[0][1] == 1


def two_route_module(weights: tuple[Q, Q], moment: int, z: Q) -> Matrix:
    # order [i1,i2,u,v], internal [0,1], no parallel primitive edges.
    w1, w2 = weights
    matrix = zeros(4, 4)
    matrix[2][0] = w1**moment
    matrix[0][3] = Q(1)  # 1^m
    matrix[2][1] = w2**moment
    matrix[1][3] = Q(1)
    _, effective = moment_port_eval(matrix, [0, 1], z)
    return effective


def check_port_moment_prefix_failure() -> None:
    a = (Q(1, 3), Q(2, 3))
    b = (Q(1, 4), Q(3, 4))
    z = Q(1, 2)
    e0_a = two_route_module(a, 0, z)
    e0_b = two_route_module(b, 0, z)
    e1_a = two_route_module(a, 1, z)
    e1_b = two_route_module(b, 1, z)
    e2_a = two_route_module(a, 2, z)
    e2_b = two_route_module(b, 2, z)
    assert e0_a == e0_b
    assert e1_a == e1_b
    assert e2_a != e2_b
    assert e0_a[0][1] == Q(1, 2)  # 2 z^2
    assert e1_a[0][1] == Q(1, 4)  # z^2
    assert e2_a[0][1] == Q(5, 36)  # (5/9) z^2
    assert e2_b[0][1] == Q(5, 32)  # (5/8) z^2


def main() -> int:
    coefficient_checks, rational_checks = check_formal_coefficient_semantics()
    check_m1_z1_reduction()
    check_count_self_loop_formal_repair()
    context_checks = check_fixed_m_external_context()
    check_moment_gauge_naturality()
    check_sequential_elimination()
    check_length_loss_witness()
    check_port_moment_prefix_failure()
    print("BRC moment/length-safe port transfer checker: PASS")
    print(f"formal_coefficient_checks={coefficient_checks}")
    print(f"rational_resolvent_checks={rational_checks}")
    print(f"external_context_checks={context_checks}")
    print("m1_z1_reduction=PASS")
    print("count_formal_repair=PASS")
    print("gauge_naturality=PASS")
    print("sequential_elimination=PASS")
    print("length_loss_boundary=PASS")
    print("port_moment_prefix_failure=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
