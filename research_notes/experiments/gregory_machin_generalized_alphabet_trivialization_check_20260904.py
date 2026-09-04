#!/usr/bin/env python3
"""Exact checker for the #1160 unrestricted rational-atom Lehmer no-go.

For each q>=2, multiply U_q until its primitive slope first crosses the diagonal.
The residual after removing the diagonal turn is a primitive rational atom whose
slope is strictly smaller than 1/q. Native assertions are exact integer arithmetic;
floating logarithms are used only for the generalized Lehmer readout afterward.
"""

from __future__ import annotations

import math


def mul_q(z: tuple[int, int], q: int) -> tuple[int, int]:
    a, b = z
    return (q * a - b, a + q * b)


def primitive(z: tuple[int, int]) -> tuple[tuple[int, int], int]:
    g = math.gcd(abs(z[0]), abs(z[1]))
    return (z[0] // g, z[1] // g), g


def first_diagonal_cross(q: int):
    assert q >= 2
    z = (1, 0)
    k = 0
    while True:
        old = z
        z = mul_q(z, q)
        k += 1
        A, B = z
        if B > A > 0:
            C, D = A + B, B - A
            (c, d), g = primitive((C, D))
            return k, old, z, (c, d), g


def main() -> None:
    rows = []
    for q in range(2, 81):
        k, old, z, residual, g = first_diagonal_cross(q)
        A0, B0 = old
        A, B = z
        c, d = residual

        # Previous state is below the diagonal and the crossing state is above it.
        assert 0 <= B0 < A0
        assert 0 < A < B

        # Purely native crossing-time bounds from the rational slope increment law.
        assert 2 * k > q - 1
        assert k <= q

        # Exact overshoot residual and strict slope bound d/c < 1/q.
        assert c > d > 0
        assert q * (B - A) < A + B
        assert q * d < c

        # tau * residual is positively proportional to the crossing direction.
        # (1+i)(c+di)=(c-d)+(c+d)i.
        left = (c - d, c + d)
        assert left[0] * B == left[1] * A
        assert left[0] > 0

        # Primitive residual norm: its odd/free split-prime part is M_q^k;
        # a primitive sum of two squares can carry at most one remaining factor 2.
        n_res = c * c + d * d
        M = (q * q + 1) // (2 if q % 2 else 1)
        assert n_res in (M**k, 2 * M**k)

        mu = 1.0 / math.log10(q) + 1.0 / math.log10(c / d)
        upper = 2.0 / math.log10(q)
        assert mu < upper

        rows.append((q, k, c, d, mu, upper, n_res.bit_length()))

    print("q k residual=(c,d) generalized_mu 2/log10(q) residual_norm_bits")
    for row in rows[:14]:
        q, k, c, d, mu, upper, bits = row
        print(f"{q:2d} {k:2d} ({c},{d}) {mu:.12f} {upper:.12f} {bits}")

    # Concrete witnesses that the unrestricted rational alphabet passes below
    # the integer-reciprocal 1.489121359... record, before tending to zero.
    q15 = next(row for row in rows if row[0] == 15)
    assert q15[4] < 1.489121359283479
    q23 = next(row for row in rows if row[0] == 23)
    assert q23[5] < 1.489121359283479

    # The analytic measure is bounded above by 2/log10(q), hence has infimum 0
    # along the exact native family as q grows.
    assert rows[-1][5] < rows[0][5]
    print("unrestricted rational-atom Lehmer trivialization regression certificate: PASS")


if __name__ == "__main__":
    main()
