#!/usr/bin/env python3
"""Exact Fraction checks for the parity-fold row ANOVA."""

from fractions import Fraction
from itertools import product


def q(n: int, a: int) -> int:
    return n // a


def main() -> None:
    n = 42
    actions = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 31, 37, 41]
    weight = {a: Fraction((a % 7) + 1, (a % 5) + 2) for a in actions}
    field = {
        m: Fraction(((11 * m * m + 7 * m + 3) % 43) - 21, 13)
        for m in range(n + 1)
    }

    def mass(cutoff: int) -> Fraction:
        return sum((weight[a] for a in actions if a <= cutoff), Fraction(0))

    def residual(state: int) -> Fraction:
        return mass(state) * field[state] + sum(
            (
                weight[a] * field[q(state, a)]
                for a in actions
                if a <= state
            ),
            Fraction(0),
        )

    total = mass(n)
    probability = {a: weight[a] / total for a in actions}
    fold = {
        (a, b): field[q(n, a * b)] if a * b <= n else field[q(n, a)]
        for a, b in product(actions, repeat=2)
    }

    row_mean = {}
    row_variance = {}
    for a in actions:
        lower = q(n, a)
        lower_mass = mass(lower)
        alpha = lower_mass / total

        mean = sum(
            (probability[b] * fold[a, b] for b in actions),
            Fraction(0),
        )
        variance = sum(
            (
                probability[b] * (fold[a, b] - mean) ** 2
                for b in actions
            ),
            Fraction(0),
        )
        row_mean[a] = mean
        row_variance[a] = variance

        lower_residual = residual(lower)
        assert mean == (
            (1 - 2 * alpha) * field[lower]
            + lower_residual / total
        )

        if lower_mass == 0:
            assert variance == 0
            continue

        core_probability = {
            b: weight[b] / lower_mass
            for b in actions
            if b <= lower
        }
        core_mean = sum(
            (
                core_probability[b] * field[q(lower, b)]
                for b in core_probability
            ),
            Fraction(0),
        )
        core_variance = sum(
            (
                core_probability[b]
                * (field[q(lower, b)] - core_mean) ** 2
                for b in core_probability
            ),
            Fraction(0),
        )

        assert core_mean == (
            -field[lower] + lower_residual / lower_mass
        )
        assert variance == (
            alpha * core_variance
            + alpha
            * (1 - alpha)
            * (core_mean - field[lower]) ** 2
        )

    full_mean = sum(
        (probability[a] * probability[b] * fold[a, b]
         for a, b in product(actions, repeat=2)),
        Fraction(0),
    )
    full_variance = sum(
        (
            probability[a]
            * probability[b]
            * (fold[a, b] - full_mean) ** 2
            for a, b in product(actions, repeat=2)
        ),
        Fraction(0),
    )

    aggregate_row_mean = sum(
        (probability[a] * row_mean[a] for a in actions),
        Fraction(0),
    )
    between = sum(
        (
            probability[a]
            * (row_mean[a] - aggregate_row_mean) ** 2
            for a in actions
        ),
        Fraction(0),
    )
    within = sum(
        (probability[a] * row_variance[a] for a in actions),
        Fraction(0),
    )
    assert full_mean == aggregate_row_mean
    assert full_variance == between + within

    print("parity-fold row ANOVA: exact checks passed")


if __name__ == "__main__":
    main()
