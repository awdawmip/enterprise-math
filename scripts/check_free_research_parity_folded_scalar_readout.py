#!/usr/bin/env python3
"""Exact finite checks for the parity-folded square scalar readout.

All theorem-level checks use ``fractions.Fraction``. No numerical prime
asymptotic is promoted to a theorem by this script.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from typing import Dict, Iterable, Tuple


Action = int
Pair = Tuple[Action, Action]


def quotient(n: int, action: int) -> int:
    if action <= 0:
        raise ValueError("actions must be positive")
    return n // action


def mass(actions: Iterable[Action], weights: Dict[Action, Fraction], cutoff: int) -> Fraction:
    return sum((weights[a] for a in actions if a <= cutoff), Fraction(0))


def residual(
    n: int,
    actions: list[Action],
    weights: Dict[Action, Fraction],
    field: Dict[int, Fraction],
) -> Fraction:
    return mass(actions, weights, n) * field[n] + sum(
        (
            weights[a] * field[quotient(n, a)]
            for a in actions
            if a <= n
        ),
        Fraction(0),
    )


def folded_endpoint(n: int, a: Action, b: Action) -> int:
    return quotient(n, a * b) if a * b <= n else quotient(n, a)


def parity(n: int, a: Action, b: Action) -> Fraction:
    return Fraction(-1 if a * b <= n else 1)


def weighted_mean_pair(
    actions: list[Action],
    probabilities: Dict[Action, Fraction],
    values: Dict[Pair, Fraction],
) -> Fraction:
    return sum(
        (
            probabilities[a] * probabilities[b] * values[a, b]
            for a, b in product(actions, repeat=2)
        ),
        Fraction(0),
    )


def weighted_variance_pair(
    actions: list[Action],
    probabilities: Dict[Action, Fraction],
    values: Dict[Pair, Fraction],
) -> Fraction:
    mean = weighted_mean_pair(actions, probabilities, values)
    return sum(
        (
            probabilities[a]
            * probabilities[b]
            * (values[a, b] - mean) ** 2
            for a, b in product(actions, repeat=2)
        ),
        Fraction(0),
    )


def pair_inner(
    actions: list[Action],
    probabilities: Dict[Action, Fraction],
    left: Dict[Pair, Fraction],
    right: Dict[Pair, Fraction],
) -> Fraction:
    return sum(
        (
            probabilities[a]
            * probabilities[b]
            * left[a, b]
            * right[a, b]
            for a, b in product(actions, repeat=2)
        ),
        Fraction(0),
    )


def pair_mixer(
    actions: list[Action],
    probabilities: Dict[Action, Fraction],
    values: Dict[Pair, Fraction],
) -> Dict[Pair, Fraction]:
    row = {
        a: sum(
            (probabilities[c] * values[a, c] for c in actions),
            Fraction(0),
        )
        for a in actions
    }
    column = {
        b: sum(
            (probabilities[c] * values[c, b] for c in actions),
            Fraction(0),
        )
        for b in actions
    }
    return {
        (a, b): (values[b, a] + row[a] + column[b]) / 3
        for a, b in product(actions, repeat=2)
    }


def pair_dirichlet(
    actions: list[Action],
    probabilities: Dict[Action, Fraction],
    values: Dict[Pair, Fraction],
) -> Fraction:
    return sum(
        (
            probabilities[a]
            * probabilities[b]
            * probabilities[c]
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


def deterministic_fixture() -> tuple[
    int,
    list[Action],
    Dict[Action, Fraction],
    Dict[int, Fraction],
]:
    n = 42
    actions = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 31, 37, 41]
    weights = {
        a: Fraction((a % 7) + 1, (a % 5) + 2)
        for a in actions
    }
    field = {
        m: Fraction(((11 * m * m + 7 * m + 3) % 43) - 21, 13)
        for m in range(n + 1)
    }
    return n, actions, weights, field


def check_quotient_composition(
    n: int, actions: list[Action]
) -> None:
    for a, b in product(actions, repeat=2):
        assert quotient(quotient(n, a), b) == quotient(n, a * b)


def check_resolvent(
    n: int,
    actions: list[Action],
    weights: Dict[Action, Fraction],
    field: Dict[int, Fraction],
) -> None:
    total = mass(actions, weights, n)
    left = total * residual(n, actions, weights, field) - sum(
        (
            weights[a]
            * residual(quotient(n, a), actions, weights, field)
            for a in actions
        ),
        Fraction(0),
    )
    folded_signed = sum(
        (
            weights[a]
            * weights[b]
            * parity(n, a, b)
            * field[folded_endpoint(n, a, b)]
            for a, b in product(actions, repeat=2)
        ),
        Fraction(0),
    )
    right = total**2 * field[n] + folded_signed
    assert left == right

    tail_minus_core = sum(
        (
            weights[a] * weights[b] * field[quotient(n, a)]
            for a, b in product(actions, repeat=2)
            if a * b > n
        ),
        Fraction(0),
    ) - sum(
        (
            weights[a] * weights[b] * field[quotient(n, a * b)]
            for a, b in product(actions, repeat=2)
            if a * b <= n
        ),
        Fraction(0),
    )
    assert folded_signed == tail_minus_core


def check_mass_and_covariance(
    n: int,
    actions: list[Action],
    weights: Dict[Action, Fraction],
    field: Dict[int, Fraction],
) -> None:
    total = mass(actions, weights, n)
    probability = {a: weights[a] / total for a in actions}
    collision_mass = sum(
        (
            weights[a] * weights[b]
            for a, b in product(actions, repeat=2)
            if a * b <= n
        ),
        Fraction(0),
    )
    epsilon = {
        (a, b): parity(n, a, b)
        for a, b in product(actions, repeat=2)
    }
    folded = {
        (a, b): field[folded_endpoint(n, a, b)]
        for a, b in product(actions, repeat=2)
    }

    epsilon_mean = weighted_mean_pair(actions, probability, epsilon)
    folded_mean = weighted_mean_pair(actions, probability, folded)
    signed_mean = sum(
        (
            probability[a]
            * probability[b]
            * epsilon[a, b]
            * folded[a, b]
            for a, b in product(actions, repeat=2)
        ),
        Fraction(0),
    )
    covariance = sum(
        (
            probability[a]
            * probability[b]
            * (epsilon[a, b] - epsilon_mean)
            * (folded[a, b] - folded_mean)
            for a, b in product(actions, repeat=2)
        ),
        Fraction(0),
    )
    epsilon_variance = weighted_variance_pair(actions, probability, epsilon)
    folded_variance = weighted_variance_pair(actions, probability, folded)

    assert epsilon_mean == 1 - 2 * collision_mass / total**2
    assert signed_mean == covariance + epsilon_mean * folded_mean
    assert covariance**2 <= epsilon_variance * folded_variance
    assert epsilon_variance <= 1


def check_odd_square_domination(
    n: int,
    actions: list[Action],
    weights: Dict[Action, Fraction],
    field: Dict[int, Fraction],
) -> None:
    total = mass(actions, weights, n)
    probability = {a: weights[a] / total for a in actions}
    folded = {
        (a, b): field[folded_endpoint(n, a, b)]
        for a, b in product(actions, repeat=2)
    }
    folded_variance = weighted_variance_pair(actions, probability, folded)

    center_energy = sum(
        (
            weights[a]
            * weights[b]
            * (folded[a, b] + field[n]) ** 2
            for a, b in product(actions, repeat=2)
        ),
        Fraction(0),
    )
    tail_energy = sum(
        (
            weights[a]
            * weights[b]
            * (field[n] + field[quotient(n, a)]) ** 2
            for a, b in product(actions, repeat=2)
            if a * b > n
        ),
        Fraction(0),
    )
    direct_core_energy = sum(
        (
            weights[a]
            * weights[b]
            * (field[n] + field[quotient(n, a * b)]) ** 2
            for a, b in product(actions, repeat=2)
            if a * b <= n
        ),
        Fraction(0),
    )
    one_step_energy = sum(
        (
            weights[a] * (field[n] + field[quotient(n, a)]) ** 2
            for a in actions
        ),
        Fraction(0),
    )

    assert total**2 * folded_variance <= center_energy
    assert center_energy == tail_energy + direct_core_energy
    assert tail_energy <= total * one_step_energy
    assert total**2 * folded_variance <= (
        total * one_step_energy + direct_core_energy
    )


def check_scalar_bound(
    n: int,
    actions: list[Action],
    weights: Dict[Action, Fraction],
    field: Dict[int, Fraction],
) -> None:
    total = mass(actions, weights, n)
    probability = {a: weights[a] / total for a in actions}
    folded = {
        (a, b): field[folded_endpoint(n, a, b)]
        for a, b in product(actions, repeat=2)
    }
    folded_variance = weighted_variance_pair(actions, probability, folded)
    collision_mass = sum(
        (
            weights[a] * weights[b]
            for a, b in product(actions, repeat=2)
            if a * b <= n
        ),
        Fraction(0),
    )
    imbalance = abs(1 - 2 * collision_mass / total**2)
    residual_bound = max(
        abs(residual(m, actions, weights, field))
        for m in range(1, n + 1)
    )
    field_bound = max(abs(field[m]) for m in range(1, n + 1))

    # Avoid irrational square roots: square the nonnegative remainder after
    # removing the two explicit linear error terms.
    remainder = max(
        Fraction(0),
        abs(field[n])
        - 2 * residual_bound / total
        - field_bound * imbalance,
    )
    assert remainder**2 <= folded_variance


def check_pair_mixer(
    actions: list[Action],
    weights: Dict[Action, Fraction],
) -> None:
    total = sum(weights.values(), Fraction(0))
    probability = {a: weights[a] / total for a in actions}
    values = {
        (a, b): Fraction(
            ((a + 2) * (b + 3) + a * a - 2 * b) % 47 - 23,
            17,
        )
        for a, b in product(actions, repeat=2)
    }
    mixed = pair_mixer(actions, probability, values)

    assert weighted_mean_pair(actions, probability, mixed) == weighted_mean_pair(
        actions, probability, values
    )
    original_variance = weighted_variance_pair(actions, probability, values)
    mixed_variance = weighted_variance_pair(actions, probability, mixed)
    assert mixed_variance <= Fraction(4, 9) * original_variance

    difference = {
        pair: values[pair] - mixed[pair]
        for pair in values
    }
    dirichlet_from_operator = pair_inner(
        actions, probability, values, difference
    )
    dirichlet_from_edges = pair_dirichlet(
        actions, probability, values
    )
    assert dirichlet_from_operator == dirichlet_from_edges
    assert original_variance <= 3 * dirichlet_from_edges


def check_pair_mixer_eigen_sectors(
    actions: list[Action],
    weights: Dict[Action, Fraction],
) -> None:
    total = sum(weights.values(), Fraction(0))
    probability = {a: weights[a] / total for a in actions}
    raw = {a: Fraction((5 * a + 7) % 19 - 9, 11) for a in actions}
    mean = sum(
        (probability[a] * raw[a] for a in actions),
        Fraction(0),
    )
    centered = {a: raw[a] - mean for a in actions}

    symmetric_additive = {
        (a, b): centered[a] + centered[b]
        for a, b in product(actions, repeat=2)
    }
    antisymmetric_additive = {
        (a, b): centered[a] - centered[b]
        for a, b in product(actions, repeat=2)
    }
    mixed_symmetric = pair_mixer(
        actions, probability, symmetric_additive
    )
    mixed_antisymmetric = pair_mixer(
        actions, probability, antisymmetric_additive
    )
    assert all(
        mixed_symmetric[a, b]
        == Fraction(2, 3) * symmetric_additive[a, b]
        for a, b in product(actions, repeat=2)
    )
    assert all(
        mixed_antisymmetric[a, b] == 0
        for a, b in product(actions, repeat=2)
    )


def symmetric_folded_values(
    n: int,
    actions: list[Action],
    field: Dict[int, Fraction],
) -> Dict[Pair, Fraction]:
    return {
        (a, b): (
            field[quotient(n, a * b)]
            if a * b <= n
            else (field[quotient(n, a)] + field[quotient(n, b)]) / 2
        )
        for a, b in product(actions, repeat=2)
    }


def check_symmetric_fold_strengthening(
    n: int,
    actions: list[Action],
    weights: Dict[Action, Fraction],
    field: Dict[int, Fraction],
) -> None:
    total = mass(actions, weights, n)
    probability = {a: weights[a] / total for a in actions}
    oriented = {
        (a, b): field[folded_endpoint(n, a, b)]
        for a, b in product(actions, repeat=2)
    }
    symmetric = symmetric_folded_values(n, actions, field)
    epsilon = {
        (a, b): parity(n, a, b)
        for a, b in product(actions, repeat=2)
    }

    oriented_signed = sum(
        (
            probability[a]
            * probability[b]
            * epsilon[a, b]
            * oriented[a, b]
            for a, b in product(actions, repeat=2)
        ),
        Fraction(0),
    )
    symmetric_signed = sum(
        (
            probability[a]
            * probability[b]
            * epsilon[a, b]
            * symmetric[a, b]
            for a, b in product(actions, repeat=2)
        ),
        Fraction(0),
    )
    assert oriented_signed == symmetric_signed
    assert weighted_variance_pair(
        actions, probability, symmetric
    ) <= weighted_variance_pair(actions, probability, oriented)
    assert all(
        symmetric[a, b] == symmetric[b, a]
        for a, b in product(actions, repeat=2)
    )

    shared_first_energy = sum(
        (
            probability[a]
            * probability[b]
            * probability[c]
            * (symmetric[a, b] - symmetric[a, c]) ** 2
            for a, b, c in product(actions, repeat=3)
        ),
        Fraction(0),
    )
    symmetric_dirichlet = pair_dirichlet(
        actions, probability, symmetric
    )
    assert symmetric_dirichlet == shared_first_energy / 3
    assert weighted_variance_pair(
        actions, probability, symmetric
    ) <= shared_first_energy

    symmetric_center_energy = sum(
        (
            weights[a]
            * weights[b]
            * (symmetric[a, b] + field[n]) ** 2
            for a, b in product(actions, repeat=2)
        ),
        Fraction(0),
    )
    oriented_tail_plus_core = sum(
        (
            weights[a]
            * weights[b]
            * (field[n] + field[quotient(n, a)]) ** 2
            for a, b in product(actions, repeat=2)
            if a * b > n
        ),
        Fraction(0),
    ) + sum(
        (
            weights[a]
            * weights[b]
            * (field[n] + field[quotient(n, a * b)]) ** 2
            for a, b in product(actions, repeat=2)
            if a * b <= n
        ),
        Fraction(0),
    )
    assert symmetric_center_energy <= oriented_tail_plus_core


def main() -> None:
    n, actions, weights, field = deterministic_fixture()
    check_quotient_composition(n, actions)
    check_resolvent(n, actions, weights, field)
    check_mass_and_covariance(n, actions, weights, field)
    check_odd_square_domination(n, actions, weights, field)
    check_scalar_bound(n, actions, weights, field)
    check_pair_mixer(actions[:7], {a: weights[a] for a in actions[:7]})
    check_pair_mixer_eigen_sectors(
        actions[:7], {a: weights[a] for a in actions[:7]}
    )
    check_symmetric_fold_strengthening(n, actions, weights, field)
    print("parity-folded square scalar readout: exact checks passed")


if __name__ == "__main__":
    main()
