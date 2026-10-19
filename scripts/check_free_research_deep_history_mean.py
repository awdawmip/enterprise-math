#!/usr/bin/env python3
"""Exact checks for the trivial/standard split of deepest history variance.

The retained three-intermediate vector decomposes orthogonally into its common
history mean and its two-dimensional ``S_3`` standard component.  The checker
also gives an arithmetic no-go showing that internal standard curvature alone
cannot control motion of the history-mean channel.
"""

from __future__ import annotations

from bisect import bisect_right
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from typing import DefaultDict, Iterator


@lru_cache(maxsize=None)
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


@lru_cache(maxsize=None)
def prime_power_base(n: int) -> int | None:
    if n < 2:
        return None
    remaining = n
    base: int | None = None
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            if base is not None and base != divisor:
                return None
            base = divisor
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        if base is not None and base != remaining:
            return None
        base = remaining
    return base


@lru_cache(maxsize=None)
def prime_powers(limit: int) -> tuple[int, ...]:
    return tuple(
        value for value in range(2, limit + 1)
        if prime_power_base(value) is not None
    )


def weight(action: int) -> Fraction:
    base = prime_power_base(action)
    assert base is not None
    return Fraction(base, action)


def field(vertex: int) -> Fraction:
    numerator = ((41 * vertex * vertex + 13 * vertex + 7) % 127) - 63
    denominator = ((17 * vertex + 5) % 31) + 1
    return Fraction(numerator, denominator)


def product_bounded_triples(cutoff: int) -> Iterator[tuple[int, int, int]]:
    budget = cutoff**3
    actions = prime_powers(budget)
    if not actions:
        return
    least = actions[0]
    for a in actions:
        if a * least * least > budget:
            break
        for b in actions:
            if a * b * least > budget:
                break
            stop = bisect_right(actions, budget // (a * b))
            for c in actions[:stop]:
                yield a, b, c


def deepest_histories(cutoff: int) -> Iterator[tuple[tuple[int, int, int], int]]:
    for labels in product_bounded_triples(cutoff):
        uncut = [index for index, action in enumerate(labels) if action <= cutoff]
        if len(uncut) == 1:
            yield labels, uncut[0]


def pair_energy(values: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    x, y, z = values
    return (x - y) ** 2 + (y - z) ** 2 + (z - x) ** 2


def mean3(values: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    return sum(values, Fraction(0, 1)) / 3


def vector_distance(
    first: tuple[Fraction, Fraction, Fraction],
    second: tuple[Fraction, Fraction, Fraction],
) -> Fraction:
    return sum(
        ((first[index] - second[index]) ** 2 for index in range(3)),
        Fraction(0, 1),
    )


def weighted_scalar_pair_energy(
    weights: list[Fraction], values: list[Fraction]
) -> Fraction:
    return sum(
        (
            weights[i] * weights[j] * (values[i] - values[j]) ** 2
            for i in range(len(values))
            for j in range(len(values))
        ),
        Fraction(0, 1),
    )


def weighted_vector_pair_energy(
    weights: list[Fraction],
    values: list[tuple[Fraction, Fraction, Fraction]],
) -> Fraction:
    return sum(
        (
            weights[i] * weights[j] * vector_distance(values[i], values[j])
            for i in range(len(values))
            for j in range(len(values))
        ),
        Fraction(0, 1),
    )


def check_pointwise_two_channel_identity() -> None:
    samples = [
        (
            (Fraction(1), Fraction(-2), Fraction(5, 3)),
            (Fraction(7, 4), Fraction(0), Fraction(-3)),
        ),
        (
            (Fraction(11, 5), Fraction(2, 7), Fraction(-1, 3)),
            (Fraction(-4), Fraction(9, 2), Fraction(8, 11)),
        ),
    ]
    for first, second in samples:
        difference = tuple(first[i] - second[i] for i in range(3))
        lhs = vector_distance(first, second)
        rhs = 3 * (mean3(first) - mean3(second)) ** 2 + pair_energy(difference) / 3
        assert lhs == rhs


def check_arithmetic_mean_no_go() -> None:
    cutoff = 10
    n = cutoff**3
    first = (2, 13, 13)
    second = (3, 11, 11)
    assert n // (first[0] * first[1] * first[2]) == 2
    assert n // (second[0] * second[1] * second[2]) == 2
    assert tuple(n // action for action in first) == (500, 76, 76)
    assert tuple(n // action for action in second) == (333, 90, 90)

    def witness(vertex: int) -> Fraction:
        return Fraction(1) if vertex in {500, 76} else Fraction(0)

    first_values = tuple(witness(n // action) for action in first)
    second_values = tuple(witness(n // action) for action in second)
    assert first_values == (1, 1, 1)
    assert second_values == (0, 0, 0)
    assert pair_energy(first_values) == 0
    assert pair_energy(second_values) == 0
    assert mean3(first_values) == 1
    assert mean3(second_values) == 0
    assert vector_distance(first_values, second_values) == 3


def check_fiberwise_vector_anova(max_cutoff: int = 12) -> None:
    for cutoff in range(2, max_cutoff + 1):
        n = cutoff**3
        fibers: DefaultDict[
            tuple[int, int], list[tuple[int, int, int]]
        ] = defaultdict(list)
        for labels, color in deepest_histories(cutoff):
            endpoint = n // (labels[0] * labels[1] * labels[2])
            fibers[color, endpoint].append(labels)

        for histories in fibers.values():
            weights = [
                weight(labels[0]) * weight(labels[1]) * weight(labels[2])
                for labels in histories
            ]
            total = sum(weights, Fraction(0, 1))
            assert total > 0
            vectors = [
                tuple(field(n // action) for action in labels)
                for labels in histories
            ]
            means = [mean3(vector) for vector in vectors]
            centered = [
                tuple(vector[index] - means[row] for index in range(3))
                for row, vector in enumerate(vectors)
            ]

            vector_pair = weighted_vector_pair_energy(weights, vectors)
            mean_pair = weighted_scalar_pair_energy(weights, means)
            standard_pair = weighted_vector_pair_energy(weights, centered)
            assert vector_pair == 3 * mean_pair + standard_pair

            total_variance = vector_pair / (2 * total)
            mean_variance = mean_pair / (2 * total)
            standard_variance = standard_pair / (2 * total)
            assert total_variance == 3 * mean_variance + standard_variance

            internal_standard = sum(
                (
                    weights[index] * pair_energy(vectors[index])
                    for index in range(len(vectors))
                ),
                Fraction(0, 1),
            )
            # Variance is bounded by its uncentered second moment, and the
            # standard-vector norm is one third of the pair energy.
            assert standard_variance <= internal_standard / 3


def main() -> None:
    check_pointwise_two_channel_identity()
    check_arithmetic_mean_no_go()
    check_fiberwise_vector_anova()
    print("deep history-mean channel checks: PASS")


if __name__ == "__main__":
    main()
