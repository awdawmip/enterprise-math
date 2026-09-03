#!/usr/bin/env python3
"""Exact checks for BRC recurrent Schur operation-safe collapse."""

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


def submatrix(matrix: Matrix, rows: list[int], cols: list[int]) -> Matrix:
    return [[matrix[i][j] for j in cols] for i in rows]


def schur_collapse(matrix: Matrix, internal: list[int]) -> tuple[list[int], Matrix, Matrix]:
    n = len(matrix)
    internal = sorted(internal)
    if not internal or len(internal) >= n or len(set(internal)) != len(internal):
        raise ValueError("internal set must be a nonempty proper state subset")
    if any(i < 0 or i >= n for i in internal):
        raise ValueError("internal index out of range")
    internal_set = set(internal)
    boundary = [i for i in range(n) if i not in internal_set]

    a = submatrix(matrix, internal, internal)
    x = submatrix(matrix, internal, boundary)
    y = submatrix(matrix, boundary, internal)
    b = submatrix(matrix, boundary, boundary)
    stable_a, s_i = stable_star(a)
    if not stable_a or s_i is None:
        raise ValueError("internal block must be stable")
    excursion = mat_mul(mat_mul(y, s_i), x)
    effective = [[b[i][j] + excursion[i][j] for j in range(len(boundary))] for i in range(len(boundary))]
    return boundary, effective, s_i


def boundary_block(star: Matrix, boundary: list[int]) -> Matrix:
    return submatrix(star, boundary, boundary)


def loop_zeta(matrix: Matrix) -> Q:
    stable, star = stable_star(matrix)
    if not stable or star is None:
        raise ValueError("zeta only formed on stable matrix")
    return determinant(star)


def add_boundary_update(matrix: Matrix, boundary: list[int], update: Matrix) -> Matrix:
    if len(update) != len(boundary) or any(len(row) != len(boundary) for row in update):
        raise ValueError("boundary update dimension mismatch")
    out = [row[:] for row in matrix]
    for i, source in enumerate(boundary):
        for j, target in enumerate(boundary):
            out[source][target] += update[i][j]
    return out


def add_matrix(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def gauge_matrix(matrix: Matrix, potential: list[Q]) -> Matrix:
    return [[matrix[i][j] * potential[j] / potential[i] for j in range(len(matrix))] for i in range(len(matrix))]


def feedback_kernel(star: Matrix, events: list[tuple[int, int, Q]]) -> Matrix:
    # endpoints are local indices in the matrix/star supplied here
    return [[star[r[1]][s[0]] * s[2] for s in events] for r in events]


def check_exhaustive_three_state_collapse() -> tuple[int, int, int]:
    values = [Q(0), Q(1, 3), Q(2, 3)]
    total = 0
    stable_full = 0
    stable_updated = 0
    updates = [
        [[Q(1, 5), Q(0)], [Q(0), Q(0)]],
        [[Q(0), Q(1, 4)], [Q(1, 6), Q(0)]],
        [[Q(1, 3), Q(0)], [Q(0), Q(1, 3)]],
    ]

    for entries in product(values, repeat=9):
        matrix = [list(entries[:3]), list(entries[3:6]), list(entries[6:])]
        boundary, effective, s_i = schur_collapse(matrix, [0])
        assert boundary == [1, 2]
        assert s_i == [[1 / (1 - matrix[0][0])]]

        full_stable, full_star = stable_star(matrix)
        eff_stable, eff_star = stable_star(effective)
        assert full_stable == eff_stable

        # Determinant factorization does not require the full system to be stable.
        det_full = determinant(mat_sub(eye(3), matrix))
        det_internal = 1 - matrix[0][0]
        det_effective = determinant(mat_sub(eye(2), effective))
        assert det_full == det_internal * det_effective

        if full_stable:
            stable_full += 1
            assert full_star is not None and eff_star is not None
            assert boundary_block(full_star, boundary) == eff_star
            assert loop_zeta(matrix) == loop_zeta([[matrix[0][0]]]) * loop_zeta(effective)

        # Boundary-only future operation safety is valid whether the update stays
        # stable or becomes unstable.
        if total % 19 == 0:
            for update in updates:
                updated_full = add_boundary_update(matrix, boundary, update)
                updated_effective = add_matrix(effective, update)
                uf_stable, uf_star = stable_star(updated_full)
                ue_stable, ue_star = stable_star(updated_effective)
                assert uf_stable == ue_stable
                assert determinant(mat_sub(eye(3), updated_full)) == (
                    det_internal * determinant(mat_sub(eye(2), updated_effective))
                )
                if uf_stable:
                    stable_updated += 1
                    assert uf_star is not None and ue_star is not None
                    assert boundary_block(uf_star, boundary) == ue_star
                    if full_stable:
                        # Gamma increment equality is equivalent to equality of
                        # exact zeta ratios, avoiding numerical logs.
                        assert loop_zeta(updated_full) / loop_zeta(matrix) == (
                            loop_zeta(updated_effective) / loop_zeta(effective)
                        )

        # Boundary feedback event kernel equality on a deterministic stable sample slice.
        if full_stable and total % 97 == 0:
            assert full_star is not None and eff_star is not None
            full_events = [(1, 2, Q(1, 7)), (2, 1, Q(1, 11))]
            local_events = [(0, 1, Q(1, 7)), (1, 0, Q(1, 11))]
            assert feedback_kernel(full_star, full_events) == feedback_kernel(eff_star, local_events)

        total += 1

    assert total == 3**9 == 19683
    assert stable_full == 9187
    return total, stable_full, stable_updated


def check_gauge_naturality() -> None:
    matrix = [
        [Q(1, 10), Q(1, 12), Q(1, 9), Q(0)],
        [Q(1, 14), Q(1, 11), Q(0), Q(1, 10)],
        [Q(1, 13), Q(0), Q(1, 10), Q(1, 12)],
        [Q(0), Q(1, 15), Q(1, 9), Q(1, 10)],
    ]
    internal = [0, 1]
    boundary, effective, _ = schur_collapse(matrix, internal)
    assert boundary == [2, 3]
    h = [Q(2), Q(3), Q(5), Q(7)]
    gauged = gauge_matrix(matrix, h)
    boundary_g, effective_g, _ = schur_collapse(gauged, internal)
    assert boundary_g == boundary
    expected = gauge_matrix(effective, [h[i] for i in boundary])
    assert effective_g == expected
    assert loop_zeta(submatrix(matrix, internal, internal)) == loop_zeta(submatrix(gauged, internal, internal))


def check_sequential_elimination() -> None:
    matrix = [
        [Q(1, 10), Q(1, 12), Q(1, 13), Q(0)],
        [Q(1, 14), Q(1, 10), Q(0), Q(1, 15)],
        [Q(1, 16), Q(0), Q(1, 10), Q(1, 12)],
        [Q(0), Q(1, 17), Q(1, 11), Q(1, 10)],
    ]
    full_stable, _ = stable_star(matrix)
    assert full_stable

    boundary_direct, direct, _ = schur_collapse(matrix, [0, 1])
    assert boundary_direct == [2, 3]

    # eliminate original state 0, then original state 1 (index 0 in [1,2,3])
    retained_0, after_0, _ = schur_collapse(matrix, [0])
    assert retained_0 == [1, 2, 3]
    retained_after, seq_01, _ = schur_collapse(after_0, [0])
    assert [retained_0[i] for i in retained_after] == [2, 3]
    assert seq_01 == direct

    # reverse order: eliminate original 1, then original 0 (index 0 in [0,2,3])
    retained_1, after_1, _ = schur_collapse(matrix, [1])
    assert retained_1 == [0, 2, 3]
    retained_after_rev, seq_10, _ = schur_collapse(after_1, [0])
    assert [retained_1[i] for i in retained_after_rev] == [2, 3]
    assert seq_10 == direct

    # Gamma/zeta offset telescopes through either order.
    z_full = loop_zeta(matrix)
    z_direct = loop_zeta(direct)
    z_internal = loop_zeta(submatrix(matrix, [0, 1], [0, 1]))
    assert z_full == z_internal * z_direct

    z_0 = loop_zeta([[matrix[0][0]]])
    z_after0_internal = loop_zeta([[after_0[0][0]]])
    assert z_internal == z_0 * z_after0_internal


def check_dag_internal_zero_offset() -> None:
    matrix = [
        [Q(0), Q(1, 2), Q(1, 5), Q(0)],
        [Q(0), Q(0), Q(0), Q(1, 4)],
        [Q(1, 7), Q(0), Q(1, 10), Q(1, 8)],
        [Q(0), Q(1, 9), Q(1, 11), Q(1, 10)],
    ]
    internal = [0, 1]
    a = submatrix(matrix, internal, internal)
    assert a == [[Q(0), Q(1, 2)], [Q(0), Q(0)]]
    assert loop_zeta(a) == 1
    boundary, effective, _ = schur_collapse(matrix, internal)
    stable_full, _ = stable_star(matrix)
    stable_eff, _ = stable_star(effective)
    assert stable_full == stable_eff
    if stable_full:
        assert loop_zeta(matrix) == loop_zeta(effective)


def check_cwm_loss_boundary() -> None:
    # Module A: one internal route of mass 1.
    one_route = [
        [Q(0), Q(1), Q(0)],  # boundary u -> internal
        [Q(0), Q(0), Q(1)],  # internal -> boundary v
        [Q(0), Q(0), Q(0)],
    ]
    boundary_one, effective_one, _ = schur_collapse(one_route, [1])
    assert boundary_one == [0, 2]
    assert effective_one == [[Q(0), Q(1)], [Q(0), Q(0)]]

    # Module B: two internal routes, each mass 1/2.
    two_routes = [
        [Q(0), Q(1, 2), Q(1, 2), Q(0)],
        [Q(0), Q(0), Q(0), Q(1)],
        [Q(0), Q(0), Q(0), Q(1)],
        [Q(0), Q(0), Q(0), Q(0)],
    ]
    boundary_two, effective_two, _ = schur_collapse(two_routes, [1, 2])
    assert boundary_two == [0, 3]
    assert effective_two == [[Q(0), Q(1)], [Q(0), Q(0)]]

    assert effective_one == effective_two
    cwm_one = (1, Q(1), Q(1))
    cwm_two = (2, Q(1), Q(1, 2))
    assert cwm_one != cwm_two


def main() -> int:
    total, stable_full, stable_updates = check_exhaustive_three_state_collapse()
    check_gauge_naturality()
    check_sequential_elimination()
    check_dag_internal_zero_offset()
    check_cwm_loss_boundary()
    print("BRC recurrent Schur collapse exact checker: PASS")
    print(f"exhaustive_3state={total}")
    print(f"stable_full={stable_full}")
    print(f"stable_boundary_updates_checked={stable_updates}")
    print("gauge_naturality=PASS")
    print("sequential_elimination=PASS")
    print("dag_internal_zero_offset=PASS")
    print("cwm_loss_boundary=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
