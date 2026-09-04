#!/usr/bin/env python3
"""Exact finite checks for the centered fourth-order stopped gate.

All theorem-level identities and inequalities use ``fractions.Fraction``.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


Action = int
Pair = tuple[Action, Action]


def mean_pair(
    actions: list[Action],
    probability: dict[Action, Fraction],
    values: dict[Pair, Fraction],
) -> Fraction:
    return sum(
        (probability[a] * probability[b] * values[a, b]
         for a, b in product(actions, repeat=2)),
        Fraction(0),
    )


def variance_pair(
    actions: list[Action],
    probability: dict[Action, Fraction],
    values: dict[Pair, Fraction],
) -> Fraction:
    mean = mean_pair(actions, probability, values)
    return sum(
        (probability[a] * probability[b] * (values[a, b] - mean) ** 2
         for a, b in product(actions, repeat=2)),
        Fraction(0),
    )


def pair_inner(
    actions: list[Action],
    probability: dict[Action, Fraction],
    left: dict[Pair, Fraction],
    right: dict[Pair, Fraction],
) -> Fraction:
    return sum(
        (probability[a] * probability[b] * left[a, b] * right[a, b]
         for a, b in product(actions, repeat=2)),
        Fraction(0),
    )


def pair_mixer(
    actions: list[Action],
    probability: dict[Action, Fraction],
    values: dict[Pair, Fraction],
) -> dict[Pair, Fraction]:
    row = {
        a: sum((probability[c] * values[a, c] for c in actions), Fraction(0))
        for a in actions
    }
    column = {
        b: sum((probability[c] * values[c, b] for c in actions), Fraction(0))
        for b in actions
    }
    return {
        (a, b): (values[b, a] + row[a] + column[b]) / 3
        for a, b in product(actions, repeat=2)
    }


def pair_dirichlet(
    actions: list[Action],
    probability: dict[Action, Fraction],
    values: dict[Pair, Fraction],
) -> Fraction:
    return sum(
        (
            probability[a] * probability[b] * probability[c]
            * (
                (values[a, b] - values[b, a]) ** 2
                + (values[a, b] - values[c, b]) ** 2
                + (values[a, b] - values[a, c]) ** 2
            )
            / 6
            for a, b, c in product(actions, repeat=3)
        ),
        Fraction(0),
    )


def check_covariance_centering() -> None:
    actions = [2, 3, 5, 7]
    raw_weights = {2: Fraction(2), 3: Fraction(3), 5: Fraction(5), 7: Fraction(7)}
    total = sum(raw_weights.values(), Fraction(0))
    probability = {a: raw_weights[a] / total for a in actions}

    values = {
        (a, b): Fraction(((7 * a + 11 * b + a * b) % 31) - 15, 9)
        for a, b in product(actions, repeat=2)
    }
    sign = {
        (a, b): Fraction(-1 if a * b <= 18 else 1)
        for a, b in product(actions, repeat=2)
    }

    eta = mean_pair(actions, probability, sign)
    value_mean = mean_pair(actions, probability, values)
    signed_mean = pair_inner(actions, probability, sign, values)

    covariance = sum(
        (
            probability[a] * probability[b]
            * (sign[a, b] - eta)
            * (values[a, b] - value_mean)
            for a, b in product(actions, repeat=2)
        ),
        Fraction(0),
    )
    assert signed_mean == covariance + eta * value_mean

    variance_sign = variance_pair(actions, probability, sign)
    variance_value = variance_pair(actions, probability, values)
    assert covariance**2 <= variance_sign * variance_value
    assert variance_sign <= 1

    sup_value = max(abs(value) for value in values.values())
    assert signed_mean**2 <= 2 * variance_value + 2 * eta**2 * sup_value**2


def check_pair_s3_dirichlet() -> None:
    actions = [2, 3, 5, 7, 11]
    raw_weights = {a: Fraction((a % 5) + 1, (a % 3) + 2) for a in actions}
    total = sum(raw_weights.values(), Fraction(0))
    probability = {a: raw_weights[a] / total for a in actions}
    values = {
        (a, b): Fraction(((a + 3) * (b + 5) + 2 * a - b) % 43 - 21, 13)
        for a, b in product(actions, repeat=2)
    }

    mixed = pair_mixer(actions, probability, values)
    mean = mean_pair(actions, probability, values)
    assert mean_pair(actions, probability, mixed) == mean

    variance = variance_pair(actions, probability, values)
    mixed_variance = variance_pair(actions, probability, mixed)
    assert mixed_variance <= Fraction(4, 9) * variance

    difference = {pair: values[pair] - mixed[pair] for pair in values}
    dirichlet_operator = pair_inner(actions, probability, values, difference)
    dirichlet_edges = pair_dirichlet(actions, probability, values)
    assert dirichlet_operator == dirichlet_edges
    assert variance <= 3 * dirichlet_edges


def check_uniform_packet_bound() -> None:
    actions = [2, 3, 5]
    probability = {2: Fraction(1, 3), 3: Fraction(1, 3), 5: Fraction(1, 3)}
    bound = Fraction(7, 5)
    values = {
        (a, b): Fraction(((a * b + 2 * a + b) % 17) - 8, 10)
        for a, b in product(actions, repeat=2)
    }
    # Rescale the fixture so |F| <= 2B exactly.
    max_value = max(abs(value) for value in values.values())
    if max_value > 2 * bound:
        values = {pair: value * (2 * bound) / max_value for pair, value in values.items()}
    assert max(abs(value) for value in values.values()) <= 2 * bound
    assert pair_dirichlet(actions, probability, values) <= 8 * bound**2


def main() -> None:
    check_covariance_centering()
    check_pair_s3_dirichlet()
    check_uniform_packet_bound()
    print("centered fourth-order gate exact checks passed")


if __name__ == "__main__":
    main()
