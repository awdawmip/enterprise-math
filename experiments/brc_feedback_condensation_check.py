#!/usr/bin/env python3
"""Exact checks for BRC feedback condensation and stability radii.

Only integers and fractions.Fraction are used.  No floating eigenvalue,
logarithm, determinant, or root oracle participates in theorem evidence.
"""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import product
from math import isqrt

Matrix = list[list[Q]]
Event = tuple[int, int, Q]  # source, target, inserted mass


def eye(n: int) -> Matrix:
    return [[Q(int(i == j), 1) for j in range(n)] for i in range(n)]


def sub(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[i][j] - right[i][j] for j in range(len(left))]
        for i in range(len(left))
    ]


def determinant(matrix: Matrix) -> Q:
    work = [row[:] for row in matrix]
    n = len(work)
    out = Q(1, 1)
    sign = 1
    for col in range(n):
        pivot = next((r for r in range(col, n) if work[r][col] != 0), None)
        if pivot is None:
            return Q(0, 1)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            sign *= -1
        pivot_value = work[col][col]
        out *= pivot_value
        for row in range(col + 1, n):
            factor = work[row][col] / pivot_value
            for j in range(col, n):
                work[row][j] -= factor * work[col][j]
    return sign * out


def inverse(matrix: Matrix) -> Matrix | None:
    n = len(matrix)
    aug = [
        matrix[i][:] + [Q(int(i == j), 1) for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != 0), None)
        if pivot is None:
            return None
        aug[col], aug[pivot] = aug[pivot], aug[col]
        pivot_value = aug[col][col]
        aug[col] = [value / pivot_value for value in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            if factor:
                aug[row] = [
                    aug[row][j] - factor * aug[col][j]
                    for j in range(2 * n)
                ]
    return [row[n:] for row in aug]


def stable_star(matrix: Matrix) -> tuple[bool, Matrix | None]:
    star = inverse(sub(eye(len(matrix)), matrix))
    if star is None:
        return False, None
    if any(value < 0 for row in star for value in row):
        return False, None
    return True, star


def add_events(background: Matrix, events: list[Event]) -> Matrix:
    updated = [row[:] for row in background]
    for source, target, mass in events:
        updated[source][target] += mass
    return updated


def feedback_kernel(star: Matrix, events: list[Event]) -> Matrix:
    m = len(events)
    return [
        [star[events[r][1]][events[s][0]] * events[s][2] for s in range(m)]
        for r in range(m)
    ]


def condensed_star(star: Matrix, events: list[Event]) -> Matrix | None:
    feedback = feedback_kernel(star, events)
    feedback_stable, feedback_star = stable_star(feedback)
    if not feedback_stable or feedback_star is None:
        return None
    n = len(star)
    m = len(events)
    return [
        [
            star[i][j]
            + sum(
                (
                    star[i][events[r][0]]
                    * events[r][2]
                    * feedback_star[r][s]
                    * star[events[s][1]][j]
                    for r in range(m)
                    for s in range(m)
                ),
                Q(0, 1),
            )
            for j in range(n)
        ]
        for i in range(n)
    ]


def gauge_matrix(matrix: Matrix, potential: list[Q]) -> Matrix:
    return [
        [matrix[i][j] * potential[j] / potential[i] for j in range(len(matrix))]
        for i in range(len(matrix))
    ]


def rational_square(value: Q) -> bool:
    if value <= 0:
        return False
    return (
        isqrt(value.numerator) ** 2 == value.numerator
        and isqrt(value.denominator) ** 2 == value.denominator
    )


def check_exhaustive_small_condensation() -> tuple[int, int, int]:
    values = [Q(0), Q(1, 4), Q(1, 2)]
    deltas = [Q(1, 5), Q(1, 2), Q(1), Q(2)]
    positions = [(0, 0), (0, 1), (1, 0), (1, 1)]
    stable_backgrounds = 0
    single_cases = 0
    pair_cases = 0

    for entries in product(values, repeat=4):
        background = [list(entries[:2]), list(entries[2:])]
        background_stable, star = stable_star(background)
        if not background_stable or star is None:
            continue
        stable_backgrounds += 1
        base_det = determinant(sub(eye(2), background))
        assert base_det > 0

        for source, target in positions:
            return_mass = star[target][source]

            # Branch-resolved determinant derivative P_e=-P*S_ba.
            unit_updated = add_events(background, [(source, target, Q(1))])
            p_edge = determinant(sub(eye(2), unit_updated)) - base_det
            assert p_edge == -base_det * return_mass

            for delta in deltas:
                events = [(source, target, delta)]
                feedback = feedback_kernel(star, events)
                updated = add_events(background, events)
                updated_stable, updated_star = stable_star(updated)
                feedback_stable, _ = stable_star(feedback)

                assert updated_stable == feedback_stable
                assert determinant(sub(eye(2), updated)) == (
                    base_det * determinant(sub(eye(1), feedback))
                )

                if updated_stable:
                    assert updated_star == condensed_star(star, events)
                    ratio = delta * return_mass
                    assert ratio < 1
                    assert updated_star is not None
                    new_response = delta * updated_star[target][source]
                    assert new_response == (
                        ratio / (1 - ratio) if ratio else Q(0)
                    )
                    assert 1 + new_response == 1 / (1 - ratio)

                single_cases += 1

            # Exact below/equal/above additive critical radius.
            if return_mass > 0:
                delta_c = 1 / return_mass
                assert stable_star(
                    add_events(background, [(source, target, delta_c / 2)])
                )[0]
                assert not stable_star(
                    add_events(background, [(source, target, delta_c)])
                )[0]
                assert not stable_star(
                    add_events(
                        background,
                        [(source, target, Q(3, 2) * delta_c)],
                    )
                )[0]
                assert delta_c == -base_det / p_edge
            else:
                huge = add_events(background, [(source, target, Q(100))])
                assert stable_star(huge)[0]
                assert determinant(sub(eye(2), huge)) == base_det
                assert p_edge == 0

            # Existing-edge scaling and deletion identities.
            old_weight = background[source][target]
            if old_weight > 0:
                response = old_weight * return_mass
                deleted = [row[:] for row in background]
                deleted[source][target] -= old_weight
                deleted_det = determinant(sub(eye(2), deleted))
                assert deleted_det / base_det == 1 + response

                if response > 0:
                    lambda_c = 1 + 1 / response
                    below = 1 + (lambda_c - 1) / 2
                    above = 1 + Q(3, 2) * (lambda_c - 1)
                    for scale, should_be_stable in [
                        (below, True),
                        (lambda_c, False),
                        (above, False),
                    ]:
                        scaled = [row[:] for row in background]
                        scaled[source][target] = scale * old_weight
                        assert stable_star(scaled)[0] == should_be_stable
                    assert lambda_c == 1 - base_det / (old_weight * p_edge)
                else:
                    scaled = [row[:] for row in background]
                    scaled[source][target] *= 100
                    assert stable_star(scaled)[0]

        # Two-event condensation, including parallel inserted events.
        for (a1, b1), (a2, b2) in product(positions, repeat=2):
            for d1, d2 in [
                (Q(1, 3), Q(1, 3)),
                (Q(1), Q(1)),
                (Q(2), Q(1, 2)),
            ]:
                events = [(a1, b1, d1), (a2, b2, d2)]
                feedback = feedback_kernel(star, events)
                updated = add_events(background, events)
                updated_stable, updated_star = stable_star(updated)
                feedback_stable, _ = stable_star(feedback)
                assert updated_stable == feedback_stable
                assert determinant(sub(eye(2), updated)) == (
                    base_det * determinant(sub(eye(2), feedback))
                )
                if updated_stable:
                    assert updated_star == condensed_star(star, events)
                pair_cases += 1

    assert stable_backgrounds == 80
    return stable_backgrounds, single_cases, pair_cases


def check_gauge_naturality() -> None:
    background = [
        [Q(1, 10), Q(1, 8), Q(0)],
        [Q(1, 9), Q(1, 10), Q(1, 12)],
        [Q(0), Q(1, 11), Q(1, 10)],
    ]
    stable, star = stable_star(background)
    assert stable and star is not None
    events = [
        (0, 2, Q(1, 7)),
        (2, 0, Q(1, 13)),
        (1, 1, Q(1, 17)),
    ]
    feedback = feedback_kernel(star, events)

    h = [Q(2), Q(3), Q(5)]
    gauged_background = gauge_matrix(background, h)
    stable_g, star_g = stable_star(gauged_background)
    assert stable_g and star_g is not None
    gauged_events = [
        (source, target, mass * h[target] / h[source])
        for source, target, mass in events
    ]
    gauged_feedback = feedback_kernel(star_g, gauged_events)

    for r in range(len(events)):
        for s in range(len(events)):
            expected = (
                feedback[r][s]
                * h[events[s][1]]
                / h[events[r][1]]
            )
            assert gauged_feedback[r][s] == expected

    assert determinant(sub(eye(len(events)), feedback)) == determinant(
        sub(eye(len(events)), gauged_feedback)
    )


def check_collective_feedback_synergy() -> None:
    # Old graph is a DAG: 1->2 and 3->0.  Each new edge alone is harmless,
    # but the pair 0->1 and 2->3 closes a 4-step feedback cycle.
    background = [[Q(0) for _ in range(4)] for _ in range(4)]
    background[1][2] = Q(1, 2)
    background[3][0] = Q(1, 2)
    stable, star = stable_star(background)
    assert stable and star is not None

    assert stable_star(add_events(background, [(0, 1, Q(100))]))[0]
    assert stable_star(add_events(background, [(2, 3, Q(100))]))[0]

    stable_events = [(0, 1, Q(1)), (2, 3, Q(1))]
    stable_feedback = feedback_kernel(star, stable_events)
    assert stable_feedback == [[Q(0), Q(1, 2)], [Q(1, 2), Q(0)]]
    assert stable_star(stable_feedback)[0]
    assert stable_star(add_events(background, stable_events))[0]
    assert determinant(sub(eye(2), stable_feedback)) == Q(3, 4)

    unstable_events = [(0, 1, Q(3)), (2, 3, Q(3))]
    unstable_feedback = feedback_kernel(star, unstable_events)
    assert unstable_feedback == [[Q(0), Q(3, 2)], [Q(3, 2), Q(0)]]
    assert not stable_star(unstable_feedback)[0]
    assert not stable_star(add_events(background, unstable_events))[0]

    # Delete one old bridge: feedback support becomes acyclic/nilpotent.
    nil_background = [[Q(0) for _ in range(4)] for _ in range(4)]
    nil_background[1][2] = Q(1, 2)
    stable, nil_star = stable_star(nil_background)
    assert stable and nil_star is not None
    huge_pair = [(0, 1, Q(100)), (2, 3, Q(100))]
    nil_feedback = feedback_kernel(nil_star, huge_pair)
    assert nil_feedback == [[Q(0), Q(50)], [Q(0), Q(0)]]
    assert stable_star(nil_feedback)[0]
    assert stable_star(add_events(nil_background, huge_pair))[0]
    assert determinant(sub(eye(2), nil_feedback)) == 1


def check_fixed_parity_thickness_boundary() -> None:
    # q=1/8 = 2*(1/4)^2 has squarefree skeleton 2.
    background = [[Q(1, 8)]]
    stable, star = stable_star(background)
    assert stable and star is not None
    response = background[0][0] * star[0][0]
    assert response == Q(1, 7)
    lambda_c = 1 + 1 / response
    assert lambda_c == 8

    # Thickness multiplication mu changes q by the square mu^2, preserving
    # the rational square class/squarefree skeleton.
    for mu, should_be_stable in [(Q(2), True), (Q(3), False)]:
        scaled_weight = background[0][0] * mu**2
        assert rational_square(scaled_weight / background[0][0])
        assert stable_star([[scaled_weight]])[0] == should_be_stable
        assert (mu**2 < lambda_c) == should_be_stable


def main() -> int:
    backgrounds, single_cases, pair_cases = check_exhaustive_small_condensation()
    check_gauge_naturality()
    check_collective_feedback_synergy()
    check_fixed_parity_thickness_boundary()

    print("BRC feedback condensation exact checker: PASS")
    print(f"stable_2x2_backgrounds={backgrounds}")
    print(f"single_event_cases={single_cases}")
    print(f"two_event_cases={pair_cases}")
    print("gauge_naturality=PASS")
    print("collective_feedback_synergy=PASS")
    print("fixed_parity_thickness_boundary=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
