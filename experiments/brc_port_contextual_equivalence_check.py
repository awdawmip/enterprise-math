#!/usr/bin/env python3
"""Exact checks for BRC port contextual equivalence and minimal signatures."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import product

Matrix = list[list[Q]]


def eye(n: int) -> Matrix:
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def mat_sub(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    if not a or not b:
        return []
    assert len(a[0]) == len(b)
    return [
        [sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0)) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def mat_add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


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


def stable_star(matrix: Matrix) -> tuple[bool, Matrix | None]:
    star = inverse(mat_sub(eye(len(matrix)), matrix))
    if star is None or any(value < 0 for row in star for value in row):
        return False, None
    return True, star


def loop_zeta(matrix: Matrix) -> Q:
    stable, star = stable_star(matrix)
    if not stable or star is None:
        raise ValueError("loop zeta requires stable matrix")
    return determinant(star)


def block(rows: int, cols: int, value: Q = Q(0)) -> Matrix:
    return [[value for _ in range(cols)] for _ in range(rows)]


def effective_matrix(a: Matrix, x: Matrix, y: Matrix, b: Matrix) -> tuple[Matrix, Matrix]:
    stable_a, s_i = stable_star(a)
    if not stable_a or s_i is None:
        raise ValueError("internal block must be stable")
    return mat_add(b, mat_mul(mat_mul(y, s_i), x)), s_i


def compose_context(
    a: Matrix,
    x: Matrix,
    y: Matrix,
    b: Matrix,
    c: Matrix,
    u: Matrix,
    v: Matrix,
    r: Matrix,
) -> Matrix:
    n_i, n_b, n_e = len(a), len(b), len(r)
    assert len(x) == n_i and (not x or len(x[0]) == n_b)
    assert len(y) == n_b and (not y or len(y[0]) == n_i)
    assert len(c) == n_b and (not c or len(c[0]) == n_b)
    assert len(u) == n_b and (not u or len(u[0]) == n_e)
    assert len(v) == n_e and (not v or len(v[0]) == n_b)
    out = block(n_i + n_b + n_e, n_i + n_b + n_e)
    for i in range(n_i):
        for j in range(n_i):
            out[i][j] = a[i][j]
        for j in range(n_b):
            out[i][n_i + j] = x[i][j]
    for i in range(n_b):
        for j in range(n_i):
            out[n_i + i][j] = y[i][j]
        for j in range(n_b):
            out[n_i + i][n_i + j] = b[i][j] + c[i][j]
        for j in range(n_e):
            out[n_i + i][n_i + n_b + j] = u[i][j]
    for i in range(n_e):
        for j in range(n_b):
            out[n_i + n_b + i][n_i + j] = v[i][j]
        for j in range(n_e):
            out[n_i + n_b + i][n_i + n_b + j] = r[i][j]
    return out


def reduced_context(w_eff: Matrix, c: Matrix, u: Matrix, v: Matrix, r: Matrix) -> Matrix:
    n_b, n_e = len(w_eff), len(r)
    out = block(n_b + n_e, n_b + n_e)
    for i in range(n_b):
        for j in range(n_b):
            out[i][j] = w_eff[i][j] + c[i][j]
        for j in range(n_e):
            out[i][n_b + j] = u[i][j]
    for i in range(n_e):
        for j in range(n_b):
            out[n_b + i][j] = v[i][j]
        for j in range(n_e):
            out[n_b + i][n_b + j] = r[i][j]
    return out


def visible_star(full_star: Matrix, internal_count: int) -> Matrix:
    return [row[internal_count:] for row in full_star[internal_count:]]


def feedback_kernel(star: Matrix, events: list[tuple[int, int, Q]]) -> Matrix:
    return [[star[row[1]][col[0]] * col[2] for col in events] for row in events]


def subset_zeta(kernel: Matrix, mask: int) -> Q:
    idx = [i for i in range(len(kernel)) if mask & (1 << i)]
    if not idx:
        return Q(1)
    subkernel = [[kernel[i][j] for j in idx] for i in idx]
    return 1 / determinant(mat_sub(eye(len(idx)), subkernel))


def interaction_table(kernel: Matrix) -> dict[int, Q]:
    n = len(kernel)
    zeta = {mask: subset_zeta(kernel, mask) for mask in range(1 << n)}
    out: dict[int, Q] = {}
    for mask in range(1, 1 << n):
        value = Q(1)
        submask = mask
        while True:
            if (mask.bit_count() - submask.bit_count()) & 1:
                value /= zeta[submask]
            else:
                value *= zeta[submask]
            if submask == 0:
                break
            submask = (submask - 1) & mask
        out[mask] = value
    return out


def check_same_weff_different_hidden_zeta() -> tuple[int, int]:
    # M1 and M2 have identical effective one-port matrix 13/80 but hidden zeta 1 vs 2.
    m1 = ([[Q(0)]], [[Q(1, 4)]], [[Q(1, 4)]], [[Q(1, 10)]])
    m2 = ([[Q(1, 2)]], [[Q(1, 8)]], [[Q(1, 4)]], [[Q(1, 10)]])
    w1, _ = effective_matrix(*m1)
    w2, _ = effective_matrix(*m2)
    assert w1 == w2 == [[Q(13, 80)]]
    z_int_1 = loop_zeta(m1[0])
    z_int_2 = loop_zeta(m2[0])
    assert z_int_1 == 1 and z_int_2 == 2

    values = [Q(0), Q(1, 6), Q(1, 4)]
    contexts = 0
    stable_contexts = 0
    for c, u, v, r in product(values, repeat=4):
        context = ([[c]], [[u]], [[v]], [[r]])
        reduced = reduced_context(w1, *context)
        reduced_stable, reduced_star = stable_star(reduced)
        full1 = compose_context(*m1, *context)
        full2 = compose_context(*m2, *context)
        stable1, star1 = stable_star(full1)
        stable2, star2 = stable_star(full2)
        assert stable1 == stable2 == reduced_stable
        # Schur determinant factorization is exact even outside the stable phase.
        det_reduced = determinant(mat_sub(eye(2), reduced))
        assert determinant(mat_sub(eye(3), full1)) == determinant(mat_sub(eye(1), m1[0])) * det_reduced
        assert determinant(mat_sub(eye(3), full2)) == determinant(mat_sub(eye(1), m2[0])) * det_reduced
        if stable1:
            stable_contexts += 1
            assert star1 is not None and star2 is not None and reduced_star is not None
            assert visible_star(star1, 1) == reduced_star
            assert visible_star(star2, 1) == reduced_star
            assert loop_zeta(full2) / loop_zeta(full1) == z_int_2 / z_int_1 == 2
        contexts += 1

    assert contexts == 81
    return contexts, stable_contexts


def check_weff_necessity() -> None:
    # Same hidden zeta (=1), different effective matrices. Empty context already separates visible star.
    m1 = ([[Q(0)]], [[Q(1, 4)]], [[Q(1, 4)]], [[Q(1, 10)]])
    m3 = ([[Q(0)]], [[Q(1, 4)]], [[Q(1, 4)]], [[Q(1, 8)]])
    w1, _ = effective_matrix(*m1)
    w3, _ = effective_matrix(*m3)
    assert loop_zeta(m1[0]) == loop_zeta(m3[0]) == 1
    assert w1 != w3
    s1 = stable_star(w1)[1]
    s3 = stable_star(w3)[1]
    assert s1 is not None and s3 is not None and s1 != s3
    # Inverse of the observed stable port star recovers W_eff exactly.
    assert mat_sub(eye(1), inverse(s1)) == w1
    assert mat_sub(eye(1), inverse(s3)) == w3


def check_two_port_external_contexts_and_feedback() -> int:
    a = [[Q(1, 10), Q(1, 12)], [Q(1, 15), Q(1, 10)]]
    x = [[Q(1, 8), Q(1, 11)], [Q(1, 13), Q(1, 9)]]
    y = [[Q(1, 14), Q(1, 10)], [Q(1, 12), Q(1, 16)]]
    b = [[Q(1, 10), Q(1, 18)], [Q(1, 17), Q(1, 10)]]
    w_eff, _ = effective_matrix(a, x, y, b)

    scales = [Q(0), Q(1, 10), Q(1, 5)]
    checked = 0
    for c_scale, u_scale, v_scale, r_scale in product(scales, repeat=4):
        c = [[c_scale, Q(0)], [Q(0), c_scale / 2]]
        u = [[u_scale, u_scale / 2], [Q(0), u_scale]]
        v = [[v_scale, Q(0)], [v_scale / 2, v_scale]]
        r = [[r_scale, r_scale / 3], [Q(0), r_scale / 2]]
        full = compose_context(a, x, y, b, c, u, v, r)
        reduced = reduced_context(w_eff, c, u, v, r)
        full_stable, full_star = stable_star(full)
        reduced_stable, reduced_star = stable_star(reduced)
        assert full_stable == reduced_stable
        assert determinant(mat_sub(eye(6), full)) == determinant(mat_sub(eye(2), a)) * determinant(mat_sub(eye(4), reduced))
        if full_stable:
            assert full_star is not None and reduced_star is not None
            visible = visible_star(full_star, 2)
            assert visible == reduced_star
            # Future feedback can touch ports and external states only.
            full_events = [(2, 4, Q(1, 20)), (5, 3, Q(1, 25)), (4, 5, Q(1, 30))]
            reduced_events = [(0, 2, Q(1, 20)), (3, 1, Q(1, 25)), (2, 3, Q(1, 30))]
            full_kernel = feedback_kernel(full_star, full_events)
            reduced_kernel = feedback_kernel(reduced_star, reduced_events)
            assert full_kernel == reduced_kernel
            assert interaction_table(full_kernel) == interaction_table(reduced_kernel)
            for full_event, reduced_event in zip(full_events, reduced_events):
                kappa_full = full_star[full_event[1]][full_event[0]]
                kappa_reduced = reduced_star[reduced_event[1]][reduced_event[0]]
                assert kappa_full == kappa_reduced
                if kappa_full > 0:
                    assert 1 / kappa_full == 1 / kappa_reduced
        checked += 1
    assert checked == 81
    return checked


def schur_collapse(matrix: Matrix, internal: list[int]) -> tuple[list[int], Matrix]:
    n = len(matrix)
    internal_set = set(internal)
    boundary = [i for i in range(n) if i not in internal_set]
    a = [[matrix[i][j] for j in internal] for i in internal]
    x = [[matrix[i][j] for j in boundary] for i in internal]
    y = [[matrix[i][j] for j in internal] for i in boundary]
    b = [[matrix[i][j] for j in boundary] for i in boundary]
    eff, _ = effective_matrix(a, x, y, b)
    return boundary, eff


def check_hierarchical_two_module_substitution() -> None:
    # Ordered states I1,I2,B1,B2. Each module has one hidden state and one port.
    a1, x1, y1, b1 = Q(1, 5), Q(1, 7), Q(1, 8), Q(1, 10)
    a2, x2, y2, b2 = Q(1, 4), Q(1, 9), Q(1, 6), Q(1, 11)
    c12, c21 = Q(1, 13), Q(1, 17)
    full = [
        [a1, Q(0), x1, Q(0)],
        [Q(0), a2, Q(0), x2],
        [y1, Q(0), b1, c12],
        [Q(0), y2, c21, b2],
    ]
    direct_boundary, direct = schur_collapse(full, [0, 1])
    assert direct_boundary == [2, 3]
    w1 = b1 + y1 * (1 / (1 - a1)) * x1
    w2 = b2 + y2 * (1 / (1 - a2)) * x2
    assert direct == [[w1, c12], [c21, w2]]

    # Eliminate I1 then I2.
    retained1, after1 = schur_collapse(full, [0])
    assert retained1 == [1, 2, 3]
    retained2, seq12 = schur_collapse(after1, [0])
    assert [retained1[i] for i in retained2] == [2, 3]
    assert seq12 == direct

    # Reverse hidden elimination order.
    retained_rev1, after_rev1 = schur_collapse(full, [1])
    assert retained_rev1 == [0, 2, 3]
    retained_rev2, seq21 = schur_collapse(after_rev1, [0])
    assert [retained_rev1[i] for i in retained_rev2] == [2, 3]
    assert seq21 == direct

    assert loop_zeta(full) == loop_zeta([[a1]]) * loop_zeta([[a2]]) * loop_zeta(direct)


def permute_two_port_module(
    a: Matrix, x: Matrix, y: Matrix, b: Matrix
) -> tuple[Matrix, Matrix, Matrix, Matrix]:
    # Swap port labels 0<->1, leaving hidden-state ordering unchanged.
    x_p = [[row[1], row[0]] for row in x]
    y_p = [y[1][:], y[0][:]]
    b_p = [[b[1][1], b[1][0]], [b[0][1], b[0][0]]]
    return [row[:] for row in a], x_p, y_p, b_p


def check_port_relabeling() -> None:
    a = [[Q(1, 10), Q(1, 12)], [Q(1, 15), Q(1, 10)]]
    x = [[Q(1, 8), Q(1, 11)], [Q(1, 13), Q(1, 9)]]
    y = [[Q(1, 14), Q(1, 10)], [Q(1, 12), Q(1, 16)]]
    b = [[Q(1, 10), Q(1, 18)], [Q(1, 17), Q(1, 10)]]
    w, _ = effective_matrix(a, x, y, b)
    p_module = permute_two_port_module(a, x, y, b)
    w_p, _ = effective_matrix(*p_module)
    expected = [[w[1][1], w[1][0]], [w[0][1], w[0][0]]]
    assert w_p == expected


def main() -> int:
    contexts, stable_contexts = check_same_weff_different_hidden_zeta()
    check_weff_necessity()
    two_port_contexts = check_two_port_external_contexts_and_feedback()
    check_hierarchical_two_module_substitution()
    check_port_relabeling()
    print("BRC port contextual equivalence exact checker: PASS")
    print(f"one_port_contexts={contexts}")
    print(f"one_port_stable_contexts={stable_contexts}")
    print(f"two_port_contexts={two_port_contexts}")
    print("weff_minimality=PASS")
    print("hidden_zeta_necessity=PASS")
    print("external_feedback_compatibility=PASS")
    print("hierarchical_substitution=PASS")
    print("port_relabeling=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
