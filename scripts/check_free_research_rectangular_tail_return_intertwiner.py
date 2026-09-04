#!/usr/bin/env python3
"""Exact checks for the rectangular tail-return intertwiner.

All computations use Fraction.  This script checks only finite algebraic
statements; the analytic prime-mass input and any asymptotic conclusion are
outside its scope.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable, Sequence

Q = Fraction


def qsum(values: Iterable[Q]) -> Q:
    return sum(values, Q(0))


def mass(weights: Sequence[Q]) -> Q:
    return qsum(weights)


def mean(weights: Sequence[Q], values: Sequence[Q]) -> Q:
    if len(weights) != len(values):
        raise ValueError("weights and values must have equal length")
    total = mass(weights)
    if total <= 0:
        raise ValueError("positive total mass required")
    return qsum(w * x for w, x in zip(weights, values)) / total


def center(weights: Sequence[Q], values: Sequence[Q]) -> list[Q]:
    midpoint = mean(weights, values)
    return [x - midpoint for x in values]


def mass_variance(weights: Sequence[Q], values: Sequence[Q]) -> Q:
    if mass(weights) == 0:
        return Q(0)
    centered = center(weights, values)
    return qsum(w * x * x for w, x in zip(weights, centered))


def pair_energy(weights: Sequence[Q], values: Sequence[Q]) -> Q:
    return qsum(
        wi * wj * (xi - xj) ** 2
        for wi, xi in zip(weights, values)
        for wj, xj in zip(weights, values)
    )


def coefficient_defect(
    weights: Sequence[Q],
    baseline: Q,
    coefficient: Sequence[Q],
    values: Sequence[Q],
) -> Q:
    centered = center(weights, values)
    lifted = [
        (baseline + v) * x for v, x in zip(coefficient, centered)
    ]
    product = [v * x for v, x in zip(coefficient, centered)]
    return (
        pair_energy(weights, lifted)
        - baseline**2 * pair_energy(weights, centered)
        - pair_energy(weights, product)
    )


def check_rectangular_return_lift() -> None:
    first_weights = [Q(1), Q(3, 2), Q(2)]
    suffix_weights = [Q(2, 3), Q(5, 4), Q(7, 6), Q(1, 2)]
    suffix_mass = mass(suffix_weights)
    present = [Q(-2), Q(1, 3), Q(7, 4)]
    children = [
        [Q(1), Q(-1), Q(2)],
        [Q(0), Q(3, 2), Q(-2, 3)],
        [Q(5, 4), Q(2), Q(-1)],
        [Q(-3), Q(1, 5), Q(4)],
    ]
    transport = [
        qsum(suffix_weights[k] * children[k][i] for k in range(len(children)))
        for i in range(len(first_weights))
    ]
    residual = [
        suffix_mass * present[i] + transport[i]
        for i in range(len(first_weights))
    ]

    for i in range(len(first_weights)):
        for j in range(len(first_weights)):
            weight = first_weights[i] * first_weights[j]
            present_relation = weight * (present[i] - present[j])
            transported_relation = qsum(
                suffix_weights[k]
                * weight
                * (children[k][i] - children[k][j])
                for k in range(len(children))
            )
            residual_relation = weight * (residual[i] - residual[j])
            assert (
                suffix_mass * present_relation + transported_relation
                == residual_relation
            )


def check_general_coefficient_identity() -> None:
    weights = [Q(1), Q(2), Q(3, 2), Q(5, 4)]
    baseline = Q(7, 3)  # deliberately different from total first mass
    coefficient = [Q(1, 2), Q(1), Q(3, 2), Q(2)]
    values = [Q(-2), Q(1, 3), Q(7, 4), Q(5)]
    centered = center(weights, values)
    total = mass(weights)
    defect = coefficient_defect(weights, baseline, coefficient, values)
    expected = 4 * baseline * total * qsum(
        w * v * x * x
        for w, v, x in zip(weights, coefficient, centered)
    )
    assert defect == expected
    assert defect >= 0


def check_high_density_absorption() -> None:
    weights = [Q(1), Q(3, 2), Q(2)]
    total = mass(weights)
    tail_mass = [Q(1, 2), Q(1), Q(3, 2)]
    outer_tail_mass = Q(2)
    suffix_pair_mass = [Q(1, 8), Q(3, 4), Q(2)]
    values = [Q(-2), Q(1, 3), Q(7, 4)]

    assert all(
        q <= v**2 <= outer_tail_mass * v
        for q, v in zip(suffix_pair_mass, tail_mass)
    )
    induced = [w * q for w, q in zip(weights, suffix_pair_mass)]
    defect = coefficient_defect(weights, total, tail_mass, values)
    assert mass_variance(induced, values) <= (
        outer_tail_mass * defect / (4 * total**2)
    )


def check_low_density_absorption() -> None:
    weights = [Q(2), Q(1), Q(5, 2), Q(3, 2)]
    first_mass = mass(weights)
    fixed_suffix_mass = Q(4)
    tail_mass = [Q(1, 3), Q(2, 3), Q(5, 4), Q(3, 2)]
    cross_pair_mass = [Q(1), Q(2), Q(4), Q(5)]
    values = [Q(-3), Q(1, 2), Q(7, 3), Q(5)]

    assert all(
        p <= fixed_suffix_mass * v
        for p, v in zip(cross_pair_mass, tail_mass)
    )
    induced = [w * p for w, p in zip(weights, cross_pair_mass)]
    defect = coefficient_defect(
        weights, fixed_suffix_mass, tail_mass, values
    )
    assert mass_variance(induced, values) <= defect / (4 * first_mass)


def check_adaptive_completion_and_forcing() -> None:
    weights = [Q(1), Q(2), Q(3)]
    baseline = Q(5)
    coefficient = [Q(1, 2), Q(1), Q(2)]
    present = [Q(-2), Q(1), Q(0)]  # centered for these weights
    assert mean(weights, present) == 0

    transport = [Q(1), Q(-1), Q(2)]
    tail_endpoint = [Q(2), Q(1, 2), Q(-3)]
    lifted = [
        (baseline + v) * x for v, x in zip(coefficient, present)
    ]
    complete_residual = [
        d + t + e for d, t, e in zip(lifted, transport, tail_endpoint)
    ]

    assert lifted == [
        r - e - t
        for r, e, t in zip(complete_residual, tail_endpoint, transport)
    ]
    assert pair_energy(weights, lifted) <= (
        4 * pair_energy(weights, complete_residual)
        + 4 * pair_energy(weights, tail_endpoint)
        + 2 * pair_energy(weights, transport)
    )


def check_rectangular_markov_nonexpansion() -> None:
    first_weights = [Q(1), Q(2), Q(3)]
    suffix_weights = [Q(1), Q(2), Q(3, 2)]
    suffix_mass = mass(suffix_weights)
    children = [
        [Q(-1), Q(2), Q(0)],
        [Q(3), Q(-2), Q(1)],
        [Q(1, 2), Q(4), Q(-3)],
    ]
    transport = [
        qsum(suffix_weights[k] * children[k][i] for k in range(len(children)))
        for i in range(len(first_weights))
    ]
    rhs = suffix_mass * qsum(
        suffix_weights[k] * pair_energy(first_weights, children[k])
        for k in range(len(children))
    )
    assert pair_energy(first_weights, transport) <= rhs


def check_full_high_low_bookkeeping() -> None:
    u0 = Q(5)
    u1 = Q(6)
    full_packet_mass = Q(90)

    high_residual = Q(7)
    high_tail = Q(3)
    high_transport = Q(5)
    low_residual = Q(11)
    low_tail = Q(4)
    low_transport = Q(8)

    high_bound = u1 / u0**2 * (
        high_residual + high_tail + high_transport / 2
    )
    low_bound = Q(1, 1) / u1 * (
        low_residual + low_tail + low_transport / 2
    )
    one_color = high_bound / 2 + 4 * low_bound
    normalized_three_color = 3 * one_color / full_packet_mass

    expanded = 3 / full_packet_mass * (
        u1 / (2 * u0**2)
        * (high_residual + high_tail + high_transport / 2)
        + 4 / u1
        * (low_residual + low_tail + low_transport / 2)
    )
    assert normalized_three_color == expanded
    assert normalized_three_color >= 0


def main() -> None:
    checks = [
        check_rectangular_return_lift,
        check_general_coefficient_identity,
        check_high_density_absorption,
        check_low_density_absorption,
        check_adaptive_completion_and_forcing,
        check_rectangular_markov_nonexpansion,
        check_full_high_low_bookkeeping,
    ]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")
    print("PASS all rectangular tail-return intertwiner checks")


if __name__ == "__main__":
    main()
