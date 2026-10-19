#!/usr/bin/env python3
"""Exact checks for the reduced factorial-core to deepest-chamber energy bridge.

Six permutations are grouped by first color and mapped to three constant maps.
A subprobability retention of ``1/9`` converts conditional core mass ``1/6``
into full-packet deep mass ``1/27``.  All calculations use ``Fraction``.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations


def core_energy(values: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    histories = list(permutations(range(3)))
    return sum(
        (Fraction(1, 6) * values[history[0]] ** 2 for history in histories),
        Fraction(0, 1),
    )


def mixed_core_energy(values: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    histories = list(permutations(range(3)))
    return sum(
        (
            Fraction(1, 6) * (values[history[0]] / 3) ** 2
            for history in histories
        ),
        Fraction(0, 1),
    )


def deep_energy(values: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    return sum(
        (Fraction(1, 27) * value**2 for value in values),
        Fraction(0, 1),
    )


def check_mass_pushforward() -> None:
    histories = list(permutations(range(3)))
    output_mass = [Fraction(0, 1) for _ in range(3)]
    for history in histories:
        output_mass[history[0]] += Fraction(1, 6) * Fraction(1, 9)
    assert output_mass == [Fraction(1, 27)] * 3
    assert sum(output_mass, Fraction(0, 1)) == Fraction(1, 9)


def check_energy_isometry() -> None:
    tests = [
        (Fraction(1), Fraction(-1), Fraction(0)),
        (Fraction(3, 5), Fraction(-7, 11), Fraction(2, 55)),
        (Fraction(13, 17), Fraction(-19, 23), Fraction(29, 31)),
    ]
    for values in tests:
        assert mixed_core_energy(values) == core_energy(values) / 9
        assert deep_energy(values) == core_energy(values) / 9
        assert mixed_core_energy(values) == deep_energy(values)


def check_equivariance() -> None:
    histories = list(permutations(range(3)))
    color_permutations = list(permutations(range(3)))
    for history in histories:
        for sigma in color_permutations:
            moved = tuple(sigma[color] for color in history)
            assert moved[0] == sigma[history[0]]


def check_standard_energy() -> None:
    standard_vectors = [
        (Fraction(1), Fraction(-1), Fraction(0)),
        (Fraction(1), Fraction(1), Fraction(-2)),
        (Fraction(3, 7), Fraction(-5, 11), Fraction(2, 77)),
    ]
    for values in standard_vectors:
        assert sum(values, Fraction(0, 1)) == 0
        normalized_color_energy = sum((value**2 for value in values), Fraction(0, 1)) / 3
        assert core_energy(values) == normalized_color_energy
        assert deep_energy(values) == normalized_color_energy / 9


def main() -> None:
    check_mass_pushforward()
    check_energy_isometry()
    check_equivariance()
    check_standard_energy()
    print("core-deep energy bridge checks: PASS")


if __name__ == "__main__":
    main()
