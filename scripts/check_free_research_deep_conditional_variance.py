#!/usr/bin/env python3
"""Exact checks for the colored deepest law of total variance.

The deep bundle is indexed by color and lower arithmetic endpoint.  Its total
L2 energy decomposes into energy of the three color totals plus within-color
endpoint fluctuation.  All calculations use ``Fraction``.
"""

from __future__ import annotations

from fractions import Fraction


def weighted_sum(weights: tuple[Fraction, ...], values: tuple[Fraction, ...]) -> Fraction:
    return sum(
        (weight * value for weight, value in zip(weights, values)),
        Fraction(0, 1),
    )


def weighted_second(weights: tuple[Fraction, ...], values: tuple[Fraction, ...]) -> Fraction:
    return sum(
        (weight * value**2 for weight, value in zip(weights, values)),
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


def check_one_color_decomposition() -> None:
    for size in range(1, 9):
        weights = tuple(Fraction(i + 2, 2 * i + 3) for i in range(size))
        total = sum(weights, Fraction(0, 1))
        for seed in range(1, 20):
            values = tuple(
                Fraction((seed + 1) * (i + 2) ** 2 - 7 * i - 3, 3 * i + 5)
                for i in range(size)
            )
            lhs = weighted_second(weights, values)
            rhs = (
                weighted_sum(weights, values) ** 2 / total
                + pair_energy(weights, values) / (2 * total)
            )
            assert lhs == rhs


def check_three_color_decomposition() -> None:
    for size in range(1, 8):
        weights = tuple(Fraction(i + 3, i + 4) for i in range(size))
        total = sum(weights, Fraction(0, 1))
        for seed in range(1, 16):
            channels = []
            for color in range(3):
                channels.append(
                    tuple(
                        Fraction(
                            (seed + color + 2) * (i + 1) ** 2
                            - (5 + color) * i
                            - 11,
                            (color + 2) * i + 7,
                        )
                        for i in range(size)
                    )
                )

            deep = sum(
                (weighted_second(weights, channel) for channel in channels),
                Fraction(0, 1),
            )
            color_total_energy = sum(
                (weighted_sum(weights, channel) ** 2 for channel in channels),
                Fraction(0, 1),
            )
            within = sum(
                (pair_energy(weights, channel) for channel in channels),
                Fraction(0, 1),
            )
            assert deep == color_total_energy / total + within / (2 * total)


def check_pointwise_standard_channels() -> None:
    for size in range(1, 9):
        weights = tuple(Fraction(i + 2, i + 5) for i in range(size))
        h0 = tuple(Fraction(3 * i - 7, 2 * i + 9) for i in range(size))
        h1 = tuple(Fraction(5 - 2 * i, 3 * i + 11) for i in range(size))
        h2 = tuple(-(h0[i] + h1[i]) for i in range(size))
        channels = (h0, h1, h2)

        totals = tuple(weighted_sum(weights, channel) for channel in channels)
        assert sum(totals, Fraction(0, 1)) == 0

        total_energy = sum((value**2 for value in totals), Fraction(0, 1))
        standard_pair = (
            (totals[0] - totals[1]) ** 2
            + (totals[1] - totals[2]) ** 2
            + (totals[2] - totals[0]) ** 2
        ) / 3
        assert total_energy == standard_pair


def check_endpoint_constant_limit() -> None:
    weights = (Fraction(2, 3), Fraction(5, 7), Fraction(11, 13))
    total = sum(weights, Fraction(0, 1))
    color_values = (Fraction(1), Fraction(-1), Fraction(0))
    channels = tuple(tuple(value for _ in weights) for value in color_values)

    deep = sum(
        (weighted_second(weights, channel) for channel in channels),
        Fraction(0, 1),
    )
    color_total_energy = sum(
        (weighted_sum(weights, channel) ** 2 for channel in channels),
        Fraction(0, 1),
    )
    within = sum(
        (pair_energy(weights, channel) for channel in channels),
        Fraction(0, 1),
    )
    assert within == 0
    assert deep == color_total_energy / total


def main() -> None:
    check_one_color_decomposition()
    check_three_color_decomposition()
    check_pointwise_standard_channels()
    check_endpoint_constant_limit()
    print("deep colored conditional-variance checks: PASS")


if __name__ == "__main__":
    main()
