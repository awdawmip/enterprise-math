#!/usr/bin/env python3
"""Exact checks for the weighted S3 lift--transpose--project mixer.

The action value is lifted to three independently weighted labels, averaged
over the three position transpositions, then projected back to the first label.
All calculations use ``Fraction``.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import factorial


def weighted_sum(weights: tuple[Fraction, ...], values: tuple[Fraction, ...]) -> Fraction:
    return sum(
        (weight * value for weight, value in zip(weights, values)),
        Fraction(0, 1),
    )


def pair_energy(weights: tuple[Fraction, ...], values: tuple[Fraction, ...]) -> Fraction:
    return sum(
        (
            weights[i]
            * weights[j]
            * (values[i] - values[j]) ** 2
            for i in range(len(values))
            for j in range(len(values))
        ),
        Fraction(0, 1),
    )


def s3_pushback(
    weights: tuple[Fraction, ...], values: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    total = sum(weights, Fraction(0, 1))
    out = []
    for a in range(len(values)):
        numerator = sum(
            (
                weights[b]
                * weights[c]
                * (values[a] + values[b] + values[c])
                / 3
                for b in range(len(values))
                for c in range(len(values))
            ),
            Fraction(0, 1),
        )
        out.append(numerator / total**2)
    return tuple(out)


def general_pushback(
    degree: int,
    weights: tuple[Fraction, ...],
    values: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    """Lift to r labels, average all position transpositions, project slot one."""
    assert degree >= 2
    total = sum(weights, Fraction(0, 1))
    transpositions = list(combinations(range(degree), 2))
    out = []
    for first in range(len(values)):
        numerator = Fraction(0, 1)
        for partners in product(range(len(values)), repeat=degree - 1):
            labels = (first,) + partners
            tuple_weight = Fraction(1, 1)
            for label in partners:
                tuple_weight *= weights[label]
            mixed_first = sum(
                (
                    values[labels[j]] if i == 0 else values[labels[0]]
                    for i, j in transpositions
                    if True
                ),
                Fraction(0, 1),
            ) / len(transpositions)
            # In a transposition (i,j), the new first coordinate changes only
            # when i=0; otherwise it remains labels[0].
            numerator += tuple_weight * mixed_first
        out.append(numerator / total ** (degree - 1))
    return tuple(out)


def relation_field(
    weights: tuple[Fraction, ...],
    values: tuple[Fraction, ...],
) -> dict[tuple[int, int], Fraction]:
    return {
        (i, j): weights[i] * weights[j] * (values[i] - values[j])
        for i in range(len(values))
        for j in range(len(values))
    }


def check_s3_formula() -> None:
    for size in range(2, 8):
        weights = tuple(Fraction(i + 2, 2 * i + 3) for i in range(size))
        total = sum(weights, Fraction(0, 1))
        for seed in range(1, 16):
            values = tuple(
                Fraction((seed + 2) * (i + 1) ** 2 - 5 * i - 7, 3 * i + 5)
                for i in range(size)
            )
            mean = weighted_sum(weights, values) / total
            pushed = s3_pushback(weights, values)
            expected = tuple((value + 2 * mean) / 3 for value in values)
            assert pushed == expected
            assert weighted_sum(weights, pushed) == weighted_sum(weights, values)
            assert pair_energy(weights, pushed) == pair_energy(weights, values) / 9

            before_field = relation_field(weights, values)
            after_field = relation_field(weights, pushed)
            for key in before_field:
                assert after_field[key] == before_field[key] / 3


def check_general_degree_formula(max_degree: int = 7) -> None:
    weights = (Fraction(2, 3), Fraction(3, 5), Fraction(5, 7), Fraction(7, 11))
    values = (Fraction(13, 17), Fraction(-11, 19), Fraction(23, 29), Fraction(-31, 37))
    total = sum(weights, Fraction(0, 1))
    mean = weighted_sum(weights, values) / total

    for degree in range(2, max_degree + 1):
        pushed = general_pushback(degree, weights, values)
        coefficient = Fraction(degree - 2, degree)
        expected = tuple(
            coefficient * value + Fraction(2, degree) * mean
            for value in values
        )
        assert pushed == expected, (degree, pushed, expected)
        assert weighted_sum(weights, pushed) == weighted_sum(weights, values)
        assert pair_energy(weights, pushed) == coefficient**2 * pair_energy(weights, values)


def check_local_global_distinction() -> None:
    values = (Fraction(2, 5), Fraction(-7, 11), Fraction(13, 17))
    local_mean = sum(values, Fraction(0, 1)) / 3

    # On one fixed triple the local S3 transposition average kills its standard sector.
    assert all(
        (values[0] + values[1] + values[2]) / 3 == local_mean
        for _ in range(3)
    )

    # After independently sampling the two partner labels and projecting back,
    # the original action-cloud standard sector is scaled by 1/3 rather than killed.
    weights = (Fraction(3, 7), Fraction(5, 9), Fraction(11, 13))
    mean = weighted_sum(weights, values) / sum(weights, Fraction(0, 1))
    pushed = s3_pushback(weights, values)
    for i, value in enumerate(values):
        assert pushed[i] - mean == (value - mean) / 3


def check_total_state_update() -> None:
    masses = (Fraction(2, 3), Fraction(5, 7), Fraction(11, 13), Fraction(17, 19))
    totals = (Fraction(7, 5), Fraction(-3, 11), Fraction(23, 17), Fraction(-29, 31))
    mass_total = sum(masses, Fraction(0, 1))
    grand_total = sum(totals, Fraction(0, 1))
    mean = grand_total / mass_total
    mixed_totals = tuple(
        total / 3 + Fraction(2, 3) * mass * mean
        for mass, total in zip(masses, totals)
    )
    assert sum(mixed_totals, Fraction(0, 1)) == grand_total

    before = {
        (i, j): masses[j] * totals[i] - masses[i] * totals[j]
        for i in range(len(masses))
        for j in range(len(masses))
    }
    after = {
        (i, j): masses[j] * mixed_totals[i] - masses[i] * mixed_totals[j]
        for i in range(len(masses))
        for j in range(len(masses))
    }
    for key in before:
        assert after[key] == before[key] / 3


def main() -> None:
    check_s3_formula()
    check_general_degree_formula()
    check_local_global_distinction()
    check_total_state_update()
    print("weighted S3 lift-project mixer checks: PASS")


if __name__ == "__main__":
    main()
