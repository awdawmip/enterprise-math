#!/usr/bin/env python3
"""Exact checks for the V16 odd-simplex constant-mode anchor.

All theorem-level checks use ``fractions.Fraction``.  The script verifies
quotient composition, the signed odd-triangle identity, sharp fixed-root
coercivity, its weighted aggregate, and the fixed-prime weighted Cauchy
constant.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def quotient(n: int, action: int) -> int:
    if action <= 0:
        raise ValueError("positive action required")
    return n // action


def delta(field: list[Fraction], action: int, n: int) -> Fraction:
    return field[n] + field[quotient(n, action)]


def check_quotient_composition() -> None:
    for n in range(0, 100):
        for a in range(1, 15):
            for b in range(1, 15):
                assert quotient(quotient(n, a), b) == quotient(n, a * b)


def check_odd_triangle_identity() -> None:
    for x_i, y_i, z_i in product(range(-5, 6), repeat=3):
        x = Fraction(x_i)
        y = Fraction(y_i)
        z = Fraction(z_i)
        edge_a = x + y
        edge_direct = x + z
        edge_transport = y + z
        assert 2 * x == edge_a + edge_direct - edge_transport
        assert 4 * x * x <= 3 * (
            edge_a * edge_a
            + edge_direct * edge_direct
            + edge_transport * edge_transport
        )

    # Sharpness at y=z=-x/3.
    x = Fraction(9, 7)
    y = -x / 3
    z = -x / 3
    energy = (x + y) ** 2 + (x + z) ** 2 + (y + z) ** 2
    assert 4 * x**2 == 3 * energy


def check_weighted_aggregate() -> None:
    labels = (2, 3, 4, 5)
    weights = {
        2: Fraction(2, 7),
        3: Fraction(3, 11),
        4: Fraction(5, 13),
        5: Fraction(7, 17),
    }
    field = [Fraction(((19 * n * n + 7 * n + 3) % 31) - 15, 23) for n in range(401)]

    for n in (17, 61, 173, 399):
        mass = sum((weights[a] for a in labels), Fraction(0))
        one = sum(
            (weights[a] * delta(field, a, n) ** 2 for a in labels),
            Fraction(0),
        )
        direct = sum(
            (
                weights[a]
                * weights[b]
                * delta(field, a * b, n) ** 2
                for a in labels
                for b in labels
            ),
            Fraction(0),
        )
        transported = sum(
            (
                weights[a]
                * weights[b]
                * delta(field, b, quotient(n, a)) ** 2
                for a in labels
                for b in labels
            ),
            Fraction(0),
        )
        assert 4 * mass**2 * field[n] ** 2 <= 3 * (
            mass * one + direct + transported
        )


def check_fixed_prime_weighted_constant() -> None:
    # Abstract p=2 weights omega(2)=L/2 and omega(4)=L/4.  The logarithmic
    # label L cancels, so set L=1 for the exact rational check.
    omega2 = Fraction(1, 2)
    omega4 = Fraction(1, 4)
    coefficient = Fraction(1, 4) * (
        Fraction(2, 1) / omega2 + Fraction(1, 1) / omega4
    )
    assert coefficient == 2

    for x_i, y_i, z_i in product(range(-4, 5), repeat=3):
        x = Fraction(x_i)
        y = Fraction(y_i)
        z = Fraction(z_i)
        d2_parent = x + y
        d4_parent = x + z
        d2_child = y + z
        combined_energy = (
            omega2 * d2_parent**2
            + omega4 * d4_parent**2
            + omega2 * d2_child**2
        )
        assert x**2 <= coefficient * combined_energy


def check_parity_chord() -> None:
    for x_i, y_i, z_i in product(range(-3, 4), repeat=3):
        x = Fraction(x_i)
        y = Fraction(y_i)
        z = Fraction(z_i)
        g0 = x
        g1 = -y
        g2 = z
        assert (x + y) ** 2 == (g0 - g1) ** 2
        assert (y + z) ** 2 == (g1 - g2) ** 2
        assert (x + z) ** 2 == (g0 + g2) ** 2

    c = Fraction(7, 5)
    assert (c - c) ** 2 + (c - c) ** 2 == 0
    assert (c + c) ** 2 == 4 * c**2


def main() -> None:
    check_quotient_composition()
    check_odd_triangle_identity()
    check_weighted_aggregate()
    check_fixed_prime_weighted_constant()
    check_parity_chord()
    print("odd-simplex constant-mode anchor: exact checks passed")


if __name__ == "__main__":
    main()
