#!/usr/bin/env python3
"""Exact Newton/power-sum checks for finite BRC branch-moment completeness."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations_with_replacement


def power_sum(weights: tuple[Q, ...], order: int) -> Q:
    return sum((weight**order for weight in weights), Q(0))


def newton_elementary(power_sums: list[Q]) -> list[Q]:
    """Given p_1..p_r, return e_0..e_r exactly."""
    r = len(power_sums)
    e = [Q(1)]
    for k in range(1, r + 1):
        numerator = Q(0)
        for i in range(1, k + 1):
            numerator += ((-1) ** (i - 1)) * e[k - i] * power_sums[i - 1]
        e.append(numerator / k)
    return e


def polynomial_coefficients(weights: tuple[Q, ...]) -> tuple[Q, ...]:
    power_sums = [power_sum(weights, k) for k in range(1, len(weights) + 1)]
    e = newton_elementary(power_sums)
    r = len(weights)
    return tuple([Q(1)] + [((-1) ** k) * e[k] for k in range(1, r + 1)])


def polynomial_evaluate(coefficients: tuple[Q, ...], value: Q) -> Q:
    out = Q(0)
    for coefficient in coefficients:
        out = out * value + coefficient
    return out


def recurrent_power_sum(coefficients: tuple[Q, ...], known: list[Q], order: int) -> Q:
    """Use monic root-polynomial recurrence to generate p_order for order>r."""
    r = len(coefficients) - 1
    assert order > r
    # polynomial coefficients are [1,c1,...,cr], giving
    # p_m + c1 p_{m-1}+...+cr p_{m-r}=0.
    value = Q(0)
    for k in range(1, r + 1):
        value -= coefficients[k] * known[order - k]
    return value


def check_multiset_completeness() -> tuple[int, int]:
    alphabet = [Q(1, 4), Q(1, 3), Q(1, 2), Q(2, 3), Q(3, 4)]
    multisets = 0
    recurrence_checks = 0
    for r in range(1, 5):
        seen: dict[tuple[Q, ...], tuple[Q, ...]] = {}
        for combo in combinations_with_replacement(alphabet, r):
            weights = tuple(combo)
            signature = tuple([Q(r)] + [power_sum(weights, k) for k in range(1, r + 1)])
            assert signature not in seen or seen[signature] == weights
            seen[signature] = weights
            coefficients = polynomial_coefficients(weights)
            for weight in weights:
                assert polynomial_evaluate(coefficients, weight) == 0

            known = [power_sum(weights, k) for k in range(r + 6)]
            generated = known[: r + 1]
            # Extend list so indices align with power order.
            for order in range(r + 1, r + 6):
                predicted = recurrent_power_sum(coefficients, generated, order)
                assert predicted == known[order]
                generated.append(predicted)
                recurrence_checks += 1
            multisets += 1
    return multisets, recurrence_checks


def check_lower_prefix_collisions() -> None:
    pair_a = (Q(1, 3), Q(2, 3))
    pair_b = (Q(1, 4), Q(3, 4))
    assert power_sum(pair_a, 0) == power_sum(pair_b, 0) == 2
    assert power_sum(pair_a, 1) == power_sum(pair_b, 1) == 1
    assert power_sum(pair_a, 2) != power_sum(pair_b, 2)

    triple_a = (Q(1), Q(5), Q(6))
    triple_b = (Q(2), Q(3), Q(7))
    assert power_sum(triple_a, 0) == power_sum(triple_b, 0) == 3
    assert power_sum(triple_a, 1) == power_sum(triple_b, 1) == 12
    assert power_sum(triple_a, 2) == power_sum(triple_b, 2) == 62
    assert power_sum(triple_a, 3) != power_sum(triple_b, 3)


def cell_moment_matrices(
    vertex_count: int,
    cells: dict[tuple[int, int], tuple[Q, ...]],
    max_order: int,
) -> list[list[list[Q]]]:
    matrices: list[list[list[Q]]] = []
    for order in range(max_order + 1):
        matrix = [[Q(0) for _ in range(vertex_count)] for _ in range(vertex_count)]
        for (source, target), weights in cells.items():
            matrix[source][target] = power_sum(weights, order)
        matrices.append(matrix)
    return matrices


def check_matrix_level_completeness() -> int:
    cells: dict[tuple[int, int], tuple[Q, ...]] = {
        (0, 0): (Q(1, 3),),
        (0, 1): (Q(1, 4), Q(1, 2)),
        (1, 2): (Q(1, 5), Q(2, 5), Q(3, 5)),
        (2, 0): (Q(2, 3), Q(3, 4)),
        (2, 2): (Q(1, 7),),
    }
    r_max = max(len(weights) for weights in cells.values())
    assert r_max == 3
    matrices = cell_moment_matrices(3, cells, 8)
    checks = 0

    for i in range(3):
        for j in range(3):
            r = int(matrices[0][i][j])
            if r == 0:
                assert all(matrices[order][i][j] == 0 for order in range(9))
                continue
            p = [matrices[order][i][j] for order in range(1, r + 1)]
            e = newton_elementary(p)
            coefficients = tuple([Q(1)] + [((-1) ** k) * e[k] for k in range(1, r + 1)])
            original = cells[(i, j)]
            for weight in original:
                assert polynomial_evaluate(coefficients, weight) == 0

            generated = [matrices[order][i][j] for order in range(r + 1)]
            for order in range(r + 1, 9):
                predicted = recurrent_power_sum(coefficients, generated, order)
                assert predicted == matrices[order][i][j]
                generated.append(predicted)
                checks += 1

    # The finite global stack W^(0)..W^(R) is enough despite cells having
    # different local multiplicities: each cell uses only the prefix it needs.
    assert len(matrices[: r_max + 1]) == 4
    return checks


def main() -> int:
    multisets, recurrence_checks = check_multiset_completeness()
    check_lower_prefix_collisions()
    matrix_checks = check_matrix_level_completeness()
    print("BRC recurrent branch moment completeness checker: PASS")
    print(f"multisets={multisets}")
    print(f"higher_moment_recurrence_checks={recurrence_checks}")
    print(f"matrix_level_prediction_checks={matrix_checks}")
    print("lower_prefix_collision_witnesses=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
