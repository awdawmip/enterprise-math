#!/usr/bin/env python3
"""Exact checks for the S_r first-history provenance mixer.

The history readout depends on the first action label and a common recoalesced
endpoint.  Uniform averaging over all position transpositions acts by the
character ratio ``(r-3)/(r-1)`` on the standard sector.  All checks use exact
``Fraction`` arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = 0
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            inversions += int(perm[i] > perm[j])
    return -1 if inversions % 2 else 1


def swap_positions(perm: tuple[int, ...], i: int, j: int) -> tuple[int, ...]:
    out = list(perm)
    out[i], out[j] = out[j], out[i]
    return tuple(out)


def history_readouts(values: tuple[Fraction, ...], endpoint: Fraction) -> dict[tuple[int, ...], Fraction]:
    return {
        perm: values[perm[0]] + endpoint
        for perm in permutations(range(len(values)))
    }


def transposition_mix(readout: dict[tuple[int, ...], Fraction]) -> dict[tuple[int, ...], Fraction]:
    perms = list(readout)
    r = len(perms[0])
    transpositions = list(combinations(range(r), 2))
    return {
        perm: sum(
            (
                readout[swap_positions(perm, i, j)]
                for i, j in transpositions
            ),
            Fraction(0, 1),
        )
        / len(transpositions)
        for perm in perms
    }


def check_local_representation_law(max_degree: int = 8) -> None:
    for r in range(2, max_degree + 1):
        values = tuple(
            Fraction(7 * i * i + 5 * i - 9, 3 * i + 5)
            for i in range(r)
        )
        endpoint = Fraction(11, 13)
        readout = history_readouts(values, endpoint)
        mixed = transposition_mix(readout)
        mean_value = sum(values, Fraction(0, 1)) / r
        history_mean = mean_value + endpoint
        standard_eigenvalue = Fraction(r - 3, r - 1)

        for perm, value in readout.items():
            expected = history_mean + standard_eigenvalue * (
                values[perm[0]] - mean_value
            )
            assert mixed[perm] == expected, (r, perm, mixed[perm], expected)

        # The readout is invariant under permutations of the final r-1 slots,
        # so every component outside the trivial plus standard representation vanishes.
        if r >= 3:
            alternating_projection = sum(
                (
                    permutation_sign(perm) * value
                    for perm, value in readout.items()
                ),
                Fraction(0, 1),
            )
            assert alternating_projection == 0

        standard_norm = sum(
            ((value - history_mean) ** 2 for value in readout.values()),
            Fraction(0, 1),
        )
        expected_standard_norm = factorial(r - 1) * sum(
            ((value - mean_value) ** 2 for value in values),
            Fraction(0, 1),
        )
        assert standard_norm == expected_standard_norm

        dirichlet = sum(
            (
                readout[perm] * (readout[perm] - mixed[perm])
                for perm in readout
            ),
            Fraction(0, 1),
        )
        expected_dirichlet = Fraction(2, r - 1) * standard_norm
        assert dirichlet == expected_dirichlet

        transpositions = list(combinations(range(r), 2))
        edge_energy = sum(
            (
                (
                    readout[perm]
                    - readout[swap_positions(perm, i, j)]
                )
                ** 2
                for i, j in transpositions
                for perm in readout
            ),
            Fraction(0, 1),
        )
        assert dirichlet == edge_energy / (2 * len(transpositions))


def check_cubic_standard_variance() -> None:
    values = {
        2: Fraction(5, 7),
        3: Fraction(-4, 9),
        4: Fraction(13, 11),
        5: Fraction(-8, 13),
    }
    weights = {
        2: Fraction(3, 5),
        3: Fraction(7, 8),
        4: Fraction(11, 12),
        5: Fraction(13, 17),
    }
    actions = list(values)
    total = sum(weights.values(), Fraction(0, 1))
    mean = sum(
        (weights[a] * values[a] for a in actions),
        Fraction(0, 1),
    ) / total
    variance = sum(
        (weights[a] * (values[a] - mean) ** 2 for a in actions),
        Fraction(0, 1),
    )

    global_standard_energy = Fraction(0, 1)
    global_dirichlet = Fraction(0, 1)
    for a, b, c in product(actions, repeat=3):
        tuple_values = (values[a], values[b], values[c])
        endpoint = Fraction(a * b * c, a + b + c)
        readout = history_readouts(tuple_values, endpoint)
        mixed = transposition_mix(readout)
        history_mean = sum(readout.values(), Fraction(0, 1)) / 6
        weight = weights[a] * weights[b] * weights[c]
        global_standard_energy += weight * sum(
            ((value - history_mean) ** 2 for value in readout.values()),
            Fraction(0, 1),
        )
        global_dirichlet += weight * sum(
            (
                readout[perm] * (readout[perm] - mixed[perm])
                for perm in readout
            ),
            Fraction(0, 1),
        )

    assert global_standard_energy == 4 * total * total * variance
    # For r=3 the standard eigenvalue is zero, so one transposition-average
    # step is the exact orthogonal projection onto the trivial sector.
    assert global_dirichlet == global_standard_energy


def check_all_degree_global_law(max_degree: int = 5) -> None:
    values = (Fraction(2, 3), Fraction(-5, 7), Fraction(11, 13))
    weights = (Fraction(3, 5), Fraction(7, 11), Fraction(13, 17))
    total = sum(weights, Fraction(0, 1))
    mean = sum(
        (weight * value for weight, value in zip(weights, values)),
        Fraction(0, 1),
    ) / total
    variance = sum(
        (
            weight * (value - mean) ** 2
            for weight, value in zip(weights, values)
        ),
        Fraction(0, 1),
    )

    for r in range(2, max_degree + 1):
        global_standard = Fraction(0, 1)
        global_dirichlet = Fraction(0, 1)
        for action_tuple in product(range(len(values)), repeat=r):
            tuple_values = tuple(values[index] for index in action_tuple)
            tuple_weight = Fraction(1, 1)
            for index in action_tuple:
                tuple_weight *= weights[index]
            endpoint = Fraction(sum(action_tuple) + 1, r + 3)
            readout = history_readouts(tuple_values, endpoint)
            mixed = transposition_mix(readout)
            history_mean = sum(readout.values(), Fraction(0, 1)) / factorial(r)
            global_standard += tuple_weight * sum(
                ((value - history_mean) ** 2 for value in readout.values()),
                Fraction(0, 1),
            )
            global_dirichlet += tuple_weight * sum(
                (
                    readout[perm] * (readout[perm] - mixed[perm])
                    for perm in readout
                ),
                Fraction(0, 1),
            )

        expected_standard = (
            (r - 1) * factorial(r - 1) * total ** (r - 1) * variance
        )
        expected_dirichlet = (
            2 * factorial(r - 1) * total ** (r - 1) * variance
        )
        assert global_standard == expected_standard
        assert global_dirichlet == expected_dirichlet


def main() -> None:
    check_local_representation_law()
    check_cubic_standard_variance()
    check_all_degree_global_law()
    print("S_r provenance transposition mixer checks: PASS")


if __name__ == "__main__":
    main()
