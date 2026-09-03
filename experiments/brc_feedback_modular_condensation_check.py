#!/usr/bin/env python3
"""Exact checks for modular/conditional BRC feedback condensation."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import permutations, product

Matrix = list[list[Q]]
Event = tuple[int, int, Q]


def eye(n: int) -> Matrix:
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def mat_add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_sub(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    rows, inner, cols = len(a), len(b), len(b[0])
    assert len(a[0]) == inner
    return [
        [sum((a[i][k] * b[k][j] for k in range(inner)), Q(0)) for j in range(cols)]
        for i in range(rows)
    ]


def determinant(matrix: Matrix) -> Q:
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


def add_events(background: Matrix, events: list[Event]) -> Matrix:
    out = [row[:] for row in background]
    for source, target, mass in events:
        out[source][target] += mass
    return out


def feedback_kernel(star: Matrix, events: list[Event]) -> Matrix:
    return [
        [star[e_r[1]][e_s[0]] * e_s[2] for e_s in events]
        for e_r in events
    ]


def cross_block(star: Matrix, rows: list[Event], cols: list[Event]) -> Matrix:
    return [
        [star[e_r[1]][e_s[0]] * e_s[2] for e_s in cols]
        for e_r in rows
    ]


def conditional_kernel_from_blocks(star: Matrix, group_a: list[Event], group_b: list[Event]) -> Matrix | None:
    f_a = feedback_kernel(star, group_a)
    stable_a, s_a = stable_star(f_a)
    if not stable_a or s_a is None:
        return None
    x = cross_block(star, group_a, group_b)
    y = cross_block(star, group_b, group_a)
    f_b = feedback_kernel(star, group_b)
    return mat_add(f_b, mat_mul(mat_mul(y, s_a), x))


def sequential_singletons(background: Matrix, ordered_events: tuple[Event, ...]) -> tuple[bool, Matrix | None, list[Q]]:
    current = [row[:] for row in background]
    stable, _ = stable_star(current)
    assert stable
    factors: list[Q] = []
    for event in ordered_events:
        stable_before, star_before = stable_star(current)
        assert stable_before and star_before is not None
        f = feedback_kernel(star_before, [event])
        factor = determinant(mat_sub(eye(1), f))
        updated = add_events(current, [event])
        stable_after, _ = stable_star(updated)
        factors.append(factor)
        current = updated
        if not stable_after:
            return False, None, factors
    return stable_star(current)[0], stable_star(current)[1], factors


def check_two_event_modularity() -> tuple[int, int]:
    values = [Q(0), Q(1, 4), Q(1, 2)]
    positions = [(0, 0), (0, 1), (1, 0), (1, 1)]
    mass_pairs = [(Q(1, 3), Q(1, 3)), (Q(1), Q(1)), (Q(2), Q(1, 2))]
    stable_backgrounds = 0
    ordered_checks = 0

    for entries in product(values, repeat=4):
        background = [list(entries[:2]), list(entries[2:])]
        base_stable, star = stable_star(background)
        if not base_stable or star is None:
            continue
        stable_backgrounds += 1
        base_det = determinant(mat_sub(eye(2), background))
        assert base_det > 0

        for p1, p2 in product(positions, repeat=2):
            for d1, d2 in mass_pairs:
                original_events = [(p1[0], p1[1], d1), (p2[0], p2[1], d2)]
                full = add_events(background, original_events)
                full_stable, full_star = stable_star(full)
                one_shot_f = feedback_kernel(star, original_events)
                assert stable_star(one_shot_f)[0] == full_stable

                for order in [(0, 1), (1, 0)]:
                    event_a = [original_events[order[0]]]
                    event_b = [original_events[order[1]]]
                    f_a = feedback_kernel(star, event_a)
                    a_stable, _ = stable_star(f_a)
                    background_a = add_events(background, event_a)
                    background_a_stable, star_a = stable_star(background_a)
                    assert a_stable == background_a_stable

                    if not a_stable:
                        # Positive additions cannot repair an unstable prefix.
                        assert not full_stable
                        ordered_checks += 1
                        continue

                    assert star_a is not None
                    cond_direct = feedback_kernel(star_a, event_b)
                    cond_block = conditional_kernel_from_blocks(star, event_a, event_b)
                    assert cond_block == cond_direct
                    cond_stable, _ = stable_star(cond_direct)
                    assert full_stable == cond_stable

                    f_a_factor = determinant(mat_sub(eye(1), f_a))
                    cond_factor = determinant(mat_sub(eye(1), cond_direct))
                    full_factor = determinant(mat_sub(eye(2), one_shot_f))
                    assert full_factor == f_a_factor * cond_factor

                    a_det = determinant(mat_sub(eye(2), background_a))
                    full_det = determinant(mat_sub(eye(2), full))
                    assert a_det == base_det * f_a_factor
                    assert full_det == a_det * cond_factor
                    assert full_det == base_det * full_factor

                    if full_stable:
                        assert full_star is not None
                        sequential_full = add_events(background_a, event_b)
                        seq_stable, seq_star = stable_star(sequential_full)
                        assert seq_stable and seq_star == full_star

                    ordered_checks += 1

    assert stable_backgrounds == 80
    assert ordered_checks == 7680
    return stable_backgrounds, ordered_checks


def check_order_dependent_attribution() -> None:
    background = [[Q(1, 4)]]
    a = (0, 0, Q(1, 8))
    b = (0, 0, Q(1, 16))
    base_det = determinant(mat_sub(eye(1), background))
    final = add_events(background, [a, b])
    final_det = determinant(mat_sub(eye(1), final))
    total_zeta_multiplier = base_det / final_det
    assert total_zeta_multiplier == Q(4, 3)

    stable_ab, star_ab, factors_ab = sequential_singletons(background, (a, b))
    stable_ba, star_ba, factors_ba = sequential_singletons(background, (b, a))
    assert stable_ab and stable_ba and star_ab == star_ba

    zeta_ab = [1 / factor for factor in factors_ab]
    zeta_ba = [1 / factor for factor in factors_ba]
    assert zeta_ab == [Q(6, 5), Q(10, 9)]
    assert zeta_ba == [Q(12, 11), Q(11, 9)]
    assert zeta_ab != zeta_ba
    assert zeta_ab[0] * zeta_ab[1] == total_zeta_multiplier
    assert zeta_ba[0] * zeta_ba[1] == total_zeta_multiplier


def check_risk_creation_formula() -> None:
    # Background: 1->2 (u), 3->0 (v). First feedback e:0->1 creates a
    # return path for second candidate f:2->3.
    u, v, delta1 = Q(1, 2), Q(1, 3), Q(3, 2)
    background = [[Q(0) for _ in range(4)] for _ in range(4)]
    background[1][2] = u
    background[3][0] = v
    stable, star = stable_star(background)
    assert stable and star is not None

    e = (0, 1, delta1)
    f_unit = (2, 3, Q(1))
    old_kappa = star[3][2]
    assert old_kappa == 0

    after_e = add_events(background, [e])
    stable_e, star_e = stable_star(after_e)
    assert stable_e and star_e is not None
    new_kappa = star_e[3][2]
    predicted = star[3][2] + delta1 * star[3][0] * star[1][2] / (1 - delta1 * star[1][0])
    assert star[1][0] == 0
    assert predicted == v * delta1 * u
    assert new_kappa == predicted == Q(1, 4)

    cond = feedback_kernel(star_e, [f_unit])
    assert cond == [[Q(1, 4)]]
    delta2_c = 1 / new_kappa
    assert delta2_c == 4
    assert stable_star(add_events(after_e, [(2, 3, delta2_c / 2)]))[0]
    assert not stable_star(add_events(after_e, [(2, 3, delta2_c)]))[0]


def check_three_event_associativity() -> None:
    background = [
        [Q(1, 10), Q(1, 10), Q(0)],
        [Q(1, 12), Q(1, 10), Q(1, 10)],
        [Q(0), Q(1, 12), Q(1, 10)],
    ]
    stable, _ = stable_star(background)
    assert stable
    events = (
        (0, 2, Q(1, 20)),
        (2, 0, Q(1, 25)),
        (1, 1, Q(1, 30)),
    )
    final = add_events(background, list(events))
    final_stable, final_star = stable_star(final)
    assert final_stable and final_star is not None
    base_det = determinant(mat_sub(eye(3), background))
    final_det = determinant(mat_sub(eye(3), final))
    total_factor = final_det / base_det

    factor_lists: list[list[Q]] = []
    for order in permutations(events):
        ok, star_final_seq, factors = sequential_singletons(background, order)
        assert ok and star_final_seq == final_star
        product_factor = Q(1)
        for factor in factors:
            assert factor > 0
            product_factor *= factor
        assert product_factor == total_factor
        factor_lists.append(factors)

    # Conditional attributions genuinely depend on order for this asymmetric data.
    assert len({tuple(factors) for factors in factor_lists}) > 1


def main() -> int:
    backgrounds, ordered_checks = check_two_event_modularity()
    check_order_dependent_attribution()
    check_risk_creation_formula()
    check_three_event_associativity()
    print("BRC modular feedback condensation exact checker: PASS")
    print(f"stable_2x2_backgrounds={backgrounds}")
    print(f"ordered_two_event_checks={ordered_checks}")
    print("order_dependent_attribution=PASS")
    print("risk_creation_formula=PASS")
    print("three_event_associativity=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
