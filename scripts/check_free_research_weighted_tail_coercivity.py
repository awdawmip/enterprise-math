#!/usr/bin/env python3
"""Exact checks for centered weighted tail-potential coercivity.

All identities use ``Fraction``.  They are finite algebraic statements and do
not use prime-distribution asymptotics.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def pair_energy(
    weights: tuple[Fraction, ...], values: tuple[Fraction, ...]
) -> Fraction:
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


def weighted_sum(
    weights: tuple[Fraction, ...], values: tuple[Fraction, ...]
) -> Fraction:
    return sum(
        (weight * value for weight, value in zip(weights, values)),
        Fraction(0, 1),
    )


def check_pair_energy_moment_identity() -> None:
    for size in range(2, 7):
        weights = tuple(Fraction(i + 2, 2 * i + 3) for i in range(size))
        total = sum(weights, Fraction(0, 1))
        for seed in range(1, 12):
            values = tuple(
                Fraction((seed + 3) * (i + 1) ** 2 - 7 * i - 5, 3 * i + 5)
                for i in range(size)
            )
            second = weighted_sum(weights, tuple(value**2 for value in values))
            first = weighted_sum(weights, values)
            assert pair_energy(weights, values) == 2 * total * second - 2 * first**2


def check_centered_coercivity_identity() -> None:
    for size in range(2, 8):
        weights = tuple(Fraction(i + 2, i + 3) for i in range(size))
        total = sum(weights, Fraction(0, 1))
        for seed in range(1, 14):
            prefix = [
                Fraction((2 * seed + 1) * (i + 1) - i * i - 3, 2 * i + 5)
                for i in range(size - 1)
            ]
            final = -sum(
                (weights[i] * prefix[i] for i in range(size - 1)),
                Fraction(0, 1),
            ) / weights[-1]
            x = tuple(prefix + [final])
            assert weighted_sum(weights, x) == 0

            potential = tuple(Fraction((seed + i * i) % 11, i + 2) for i in range(size))
            vx = tuple(potential[i] * x[i] for i in range(size))
            lifted = tuple((total + potential[i]) * x[i] for i in range(size))
            tail_quadratic = weighted_sum(
                weights,
                tuple(potential[i] * x[i] ** 2 for i in range(size)),
            )

            lhs = pair_energy(weights, lifted)
            rhs = (
                total**2 * pair_energy(weights, x)
                + 4 * total**2 * tail_quadratic
                + pair_energy(weights, vx)
            )
            assert lhs == rhs
            assert lhs >= total**2 * pair_energy(weights, x)
            assert lhs >= (
                total**2 * pair_energy(weights, x)
                + 4 * total**2 * tail_quadratic
            )


def check_near_baseline_localization() -> None:
    for size in range(3, 9):
        weights = tuple(Fraction(i + 3, 2 * i + 5) for i in range(size))
        total = sum(weights, Fraction(0, 1))
        prefix = [Fraction((-1) ** i * (i + 2), i + 5) for i in range(size - 1)]
        x = tuple(
            prefix
            + [
                -sum(
                    (weights[i] * prefix[i] for i in range(size - 1)),
                    Fraction(0, 1),
                )
                / weights[-1]
            ]
        )
        potential = tuple(Fraction(i, size - 1) * total for i in range(size))
        lifted = tuple((total + potential[i]) * x[i] for i in range(size))
        base = total**2 * pair_energy(weights, x)
        excess = pair_energy(weights, lifted) - base
        x_mass = weighted_sum(weights, tuple(value**2 for value in x))

        for numerator in range(1, 5):
            eta = Fraction(numerator, 5)
            threshold = eta * total
            high_mass = sum(
                (
                    weights[i] * x[i] ** 2
                    for i in range(size)
                    if potential[i] >= threshold
                ),
                Fraction(0, 1),
            )
            assert 4 * total**2 * threshold * high_mass <= excess

            epsilon = excess / base if base else Fraction(0, 1)
            if threshold > 0 and x_mass > 0:
                assert high_mass <= epsilon * total * x_mass / (2 * threshold)


def check_uncentered_reciprocal_kernel() -> None:
    weights = (Fraction(2, 3), Fraction(3, 5), Fraction(5, 7), Fraction(7, 11))
    total = sum(weights, Fraction(0, 1))
    potential = (Fraction(0), Fraction(1, 4), Fraction(2, 3), Fraction(5, 6))
    for constant in (Fraction(1), Fraction(-7, 9), Fraction(13, 5)):
        x = tuple(constant / (total + value) for value in potential)
        lifted = tuple((total + potential[i]) * x[i] for i in range(len(x)))
        assert all(value == constant for value in lifted)
        assert pair_energy(weights, lifted) == 0
        assert pair_energy(weights, x) > 0
        assert weighted_sum(weights, x) != 0


def main() -> None:
    check_pair_energy_moment_identity()
    check_centered_coercivity_identity()
    check_near_baseline_localization()
    check_uncentered_reciprocal_kernel()
    print("weighted tail-potential coercivity checks: PASS")


if __name__ == "__main__":
    main()
