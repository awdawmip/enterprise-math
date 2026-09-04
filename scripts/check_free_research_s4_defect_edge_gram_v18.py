#!/usr/bin/env python3
"""Exact finite checks for the V18 S4 defect-edge Gram theorem."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product
from typing import Dict, Tuple


Edge = Tuple[int, int]
EDGES: tuple[Edge, ...] = tuple(combinations(range(4), 2))
COEFFICIENTS = (1, 2, 2, 6, 6, 6)


def probability_fixture() -> tuple[list[int], Dict[int, Fraction]]:
    points = [0, 1, 2, 3]
    raw = {0: Fraction(1), 1: Fraction(2), 2: Fraction(3), 3: Fraction(5)}
    total = sum(raw.values(), Fraction(0))
    return points, {x: raw[x] / total for x in points}


def kernel_fixture(points: list[int]) -> Dict[tuple[int, int], Fraction]:
    return {
        (x, y): Fraction(((7 * x * y + 5 * x + 5 * y + 3) % 19) - 9, 11)
        for x in points
        for y in points
    }


def mean(points, p, values) -> Fraction:
    return sum((p[x] * values[x] for x in points), Fraction(0))


def hoeffding_decomposition(points, p, h):
    m = sum(
        (p[x] * p[y] * h[x, y] for x in points for y in points),
        Fraction(0),
    )
    g = {
        x: sum((p[y] * h[x, y] for y in points), Fraction(0)) - m
        for x in points
    }
    interaction = {
        (x, y): h[x, y] - m - g[x] - g[y]
        for x in points
        for y in points
    }
    assert sum((p[x] * g[x] for x in points), Fraction(0)) == 0
    for x in points:
        assert sum((p[y] * interaction[x, y] for y in points), Fraction(0)) == 0
        assert sum((p[y] * interaction[y, x] for y in points), Fraction(0)) == 0
    return m, g, interaction


def expectation_four(points, p, function) -> Fraction:
    return sum(
        (
            p[x0] * p[x1] * p[x2] * p[x3] * function((x0, x1, x2, x3))
            for x0, x1, x2, x3 in product(points, repeat=4)
        ),
        Fraction(0),
    )


def l2_pair(points, p, h) -> Fraction:
    return sum(
        (p[x] * p[y] * h[x, y] ** 2 for x in points for y in points),
        Fraction(0),
    )


def check_pairwise_orthogonality(points, p, interaction) -> None:
    for index, edge in enumerate(EDGES):
        for other in EDGES[index + 1 :]:
            value = expectation_four(
                points,
                p,
                lambda sample, e=edge, f=other: (
                    interaction[sample[e[0]], sample[e[1]]]
                    * interaction[sample[f[0]], sample[f[1]]]
                ),
            )
            assert value == 0


def check_full_gram(points, p, h) -> None:
    m, g, interaction = hoeffding_decomposition(points, p, h)
    g_norm = sum((p[x] * g[x] ** 2 for x in points), Fraction(0))
    interaction_norm = l2_pair(points, p, interaction)
    input_norm = l2_pair(points, p, h)
    assert input_norm == m**2 + 2 * g_norm + interaction_norm

    assignment = dict(zip(EDGES, COEFFICIENTS))
    c_total = sum(COEFFICIENTS)
    degrees = {
        vertex: sum(
            coefficient
            for edge, coefficient in assignment.items()
            if vertex in edge
        )
        for vertex in range(4)
    }

    output_norm = expectation_four(
        points,
        p,
        lambda sample: (
            sum(
                assignment[edge] * h[sample[edge[0]], sample[edge[1]]]
                for edge in EDGES
            )
        )
        ** 2,
    )
    predicted = (
        c_total**2 * m**2
        + sum(degree**2 for degree in degrees.values()) * g_norm
        + sum(c**2 for c in COEFFICIENTS) * interaction_norm
    )
    assert output_norm == predicted


def check_constants() -> None:
    assert sum(COEFFICIENTS) == 23
    assert sum(c * c for c in COEFFICIENTS) == 117
    assert Fraction(117, 24**2) == Fraction(13, 64)
    assert Fraction(23**2, 24**2) == Fraction(529, 576)

    distinct_assignments = set(permutations(COEFFICIENTS))
    degree_square_values = []
    for coefficients in distinct_assignments:
        assignment = dict(zip(EDGES, coefficients))
        degrees = [
            sum(c for edge, c in assignment.items() if vertex in edge)
            for vertex in range(4)
        ]
        degree_square_values.append(sum(d * d for d in degrees))

    assert max(degree_square_values) == 586
    assert min(degree_square_values) == 546
    assert Fraction(max(degree_square_values), 2 * 24**2) == Fraction(293, 576)
    assert Fraction(293, 576) < 1


def check_centered_contraction(points, p, h) -> None:
    m, g, interaction = hoeffding_decomposition(points, p, h)
    centered = {(x, y): h[x, y] - m for x in points for y in points}
    input_norm = l2_pair(points, p, centered)

    for coefficients in set(permutations(COEFFICIENTS)):
        assignment = dict(zip(EDGES, coefficients))
        output_norm = expectation_four(
            points,
            p,
            lambda sample: (
                sum(
                    assignment[edge]
                    * centered[sample[edge[0]], sample[edge[1]]]
                    for edge in EDGES
                )
                / 24
            )
            ** 2,
        )
        assert output_norm <= Fraction(293, 576) * input_norm

    degenerate_norm = l2_pair(points, p, interaction)
    assignment = dict(zip(EDGES, COEFFICIENTS))
    degenerate_output = expectation_four(
        points,
        p,
        lambda sample: (
            sum(
                assignment[edge]
                * interaction[sample[edge[0]], sample[edge[1]]]
                for edge in EDGES
            )
            / 24
        )
        ** 2,
    )
    assert degenerate_output == Fraction(13, 64) * degenerate_norm


def main() -> None:
    points, p = probability_fixture()
    h = kernel_fixture(points)
    check_constants()
    _, _, interaction = hoeffding_decomposition(points, p, h)
    check_pairwise_orthogonality(points, p, interaction)
    check_full_gram(points, p, h)
    check_centered_contraction(points, p, h)
    print("V18 S4 defect-edge Gram: exact checks passed")


if __name__ == "__main__":
    main()
