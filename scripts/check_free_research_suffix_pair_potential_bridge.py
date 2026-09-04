#!/usr/bin/env python3
"""Exact checks for the suffix-pair density to tail-potential bridge."""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable, Sequence

Q = Fraction


def qsum(xs: Iterable[Q]) -> Q:
    return sum(xs, Q(0))


def mass(w: Sequence[Q]) -> Q:
    return qsum(w)


def mean(w: Sequence[Q], x: Sequence[Q]) -> Q:
    total = mass(w)
    if total <= 0:
        raise ValueError("positive mass required")
    return qsum(a * b for a, b in zip(w, x)) / total


def center(w: Sequence[Q], x: Sequence[Q]) -> list[Q]:
    midpoint = mean(w, x)
    return [value - midpoint for value in x]


def variance(w: Sequence[Q], x: Sequence[Q]) -> Q:
    if mass(w) == 0:
        return Q(0)
    centered = center(w, x)
    return qsum(weight * value * value for weight, value in zip(w, centered))


def pair_energy(w: Sequence[Q], x: Sequence[Q]) -> Q:
    return qsum(
        wi * wj * (xi - xj) ** 2
        for wi, xi in zip(w, x)
        for wj, xj in zip(w, x)
    )


def coefficient_lift(
    w: Sequence[Q], coefficient: Sequence[Q], x: Sequence[Q]
) -> list[Q]:
    total = mass(w)
    return [(total + value) * state for value, state in zip(coefficient, x)]


def product_channel(coefficient: Sequence[Q], x: Sequence[Q]) -> list[Q]:
    return [value * state for value, state in zip(coefficient, x)]


def potential_defect(
    w: Sequence[Q], coefficient: Sequence[Q], x: Sequence[Q]
) -> Q:
    centered = center(w, x)
    total = mass(w)
    lifted = coefficient_lift(w, coefficient, centered)
    product = product_channel(coefficient, centered)
    return (
        pair_energy(w, lifted)
        - total**2 * pair_energy(w, centered)
        - pair_energy(w, product)
    )


def check_potential_identity() -> None:
    w = [Q(1), Q(3, 2), Q(5, 4), Q(2)]
    coefficient = [Q(0), Q(1, 3), Q(4, 5), Q(7, 6)]
    x = [Q(-2), Q(7, 3), Q(5), Q(-1, 4)]
    centered = center(w, x)
    total = mass(w)
    lhs = potential_defect(w, coefficient, x)
    rhs = 4 * total**2 * qsum(
        weight * value * state**2
        for weight, value, state in zip(w, coefficient, centered)
    )
    assert lhs == rhs
    assert lhs >= 0


def check_high_suffix_pair_bridge() -> None:
    w = [Q(1), Q(2), Q(3, 2), Q(5, 3)]
    tail_mass = [Q(1, 2), Q(3, 4), Q(5, 4), Q(2)]
    # Each pair_mass is the mass of a subset of T_a x T_a.
    pair_mass = [Q(1, 8), Q(1, 2), Q(7, 8), Q(3)]
    assert all(value <= tail**2 for value, tail in zip(pair_mass, tail_mass))
    tail_max = max(tail_mass)
    assert all(value <= tail_max * tail for value, tail in zip(pair_mass, tail_mass))

    x = [Q(-3), Q(1, 2), Q(7, 3), Q(5)]
    centered = center(w, x)
    induced = [weight * value for weight, value in zip(w, pair_mass)]
    lhs = variance(induced, centered)
    defect = potential_defect(w, tail_mass, centered)
    rhs = tail_max * defect / (4 * mass(w) ** 2)
    assert lhs <= rhs


def check_low_cross_pair_bridge() -> None:
    w = [Q(2), Q(1), Q(5, 2), Q(7, 4)]
    small_mass = [Q(1, 3), Q(3, 4), Q(5, 6), Q(4, 3)]
    tail_mass = [Q(1, 2), Q(2, 3), Q(7, 5), Q(5, 4)]
    # Each cross_mass is the mass of a subset of A_b x C_b.
    cross_mass = [Q(1, 10), Q(2, 5), Q(1), Q(3, 2)]
    assert all(
        value <= small * tail
        for value, small, tail in zip(cross_mass, small_mass, tail_mass)
    )

    small_max = max(small_mass)
    tail_max = max(tail_mass)
    x = [Q(4), Q(-2), Q(1, 3), Q(11, 5)]
    centered = center(w, x)
    induced = [weight * value for weight, value in zip(w, cross_mass)]
    lhs = variance(induced, centered)
    defect_small = potential_defect(w, small_mass, centered)
    defect_tail = potential_defect(w, tail_mass, centered)
    rhs = (
        tail_max * defect_small + small_max * defect_tail
    ) / (8 * mass(w) ** 2)
    assert lhs <= rhs


def check_full_mean_packet_formula() -> None:
    # Abstract positive defects for one color, then three colors.
    small_base_mass = Q(5)
    tail_base_mass = Q(6)
    full_packet_mass = Q(90)
    defect_high = Q(40)
    defect_small = Q(18)
    defect_tail = Q(30)

    high_bound = (
        tail_base_mass * defect_high / (4 * small_base_mass**2)
    )
    low_bound = (
        tail_base_mass * defect_small + small_base_mass * defect_tail
    ) / (8 * tail_base_mass**2)
    one_color = Q(1, 2) * high_bound + 4 * low_bound
    full_bound = 3 * one_color / full_packet_mass

    expanded = (
        3
        / full_packet_mass
        * (
            tail_base_mass * defect_high / (8 * small_base_mass**2)
            + (
                tail_base_mass * defect_small
                + small_base_mass * defect_tail
            )
            / (2 * tail_base_mass**2)
        )
    )
    assert full_bound == expanded
    assert full_bound >= 0


def main() -> None:
    checks = [
        check_potential_identity,
        check_high_suffix_pair_bridge,
        check_low_cross_pair_bridge,
        check_full_mean_packet_formula,
    ]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")
    print("PASS all suffix-pair potential bridge checks")


if __name__ == "__main__":
    main()
