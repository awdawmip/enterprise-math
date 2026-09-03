#!/usr/bin/env python3
"""Exact generalized rational-turn certificate for #1160.

The native generator is a primitive integer direction pair G(b,a)=[b+a i],
not a real arctangent.  This checker verifies the five-generator rational-slope
circuit obtained by compressing two Todd pairs in Nimbran's identity, together
with its seven-term integer-reciprocal expansion.

No numerical value of pi is used.  Floating logarithms are used only for the
post-certificate generalized Lehmer readout.
"""

from __future__ import annotations

import math


def mul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def primitive(z):
    g = math.gcd(abs(z[0]), abs(z[1]))
    z = (z[0] // g, z[1] // g)
    if z[0] < 0 or (z[0] == 0 and z[1] < 0):
        z = (-z[0], -z[1])
    return z


def multiply_word(terms):
    z = (1, 0)
    for (b, a), coefficient in terms:
        factor = (b, a if coefficient > 0 else -a)
        for _ in range(abs(coefficient)):
            z = primitive(mul(z, factor))
    return z


def tangent_sheet(terms):
    z = (1, 0)
    sheet = 0
    crossings = 0
    for (b, a), coefficient in terms:
        sign = 1 if coefficient > 0 else -1
        factor = (b, sign * a)
        assert b > abs(a) > 0
        for _ in range(abs(coefficient)):
            old = z
            z = primitive(mul(z, factor))
            assert old[0] != 0 and z[0] != 0
            if (old[0] > 0) != (z[0] > 0):
                sheet += sign
                crossings += 1
    return z, sheet, crossings


def generalized_lehmer(terms):
    # one cost contribution per distinct primitive generator, independent of coefficient
    return sum(1.0 / math.log10(b / abs(a)) for (b, a), _ in terms)


def todd_tail(x: int) -> int:
    assert x >= 2
    return x * (x * x + 3) // 2


def same_turn(z, w):
    return z[0] * w[1] == z[1] * w[0] and z[0] * w[0] + z[1] * w[1] > 0


def verify_todd_compression(x: int):
    F = todd_tail(x)
    raw = mul(mul((x, 1), (x, 1)), (F, -1))
    assert same_turn(raw, (x, 2))
    return F


def main():
    # Primitive generalized generators: G(b,a)=[b+a i].
    generalized = [
        ((107, 1), 83),
        ((1710, 1), 17),
        ((207385, 2), -22),
        ((2513489, 2), -12),
        ((3235259223, 1), 22),
    ]

    endpoint = multiply_word(generalized)
    lift = tangent_sheet(generalized)
    mu_general = generalized_lehmer(generalized)

    assert endpoint == (1, 1)
    assert lift == ((1, 1), 0, 0)
    assert abs(mu_general - 1.2705512545505269) < 1e-14

    F1 = verify_todd_compression(207385)
    F2 = verify_todd_compression(2513489)
    assert F1 == 4459662850206890
    assert F2 == 7939642926390344818

    # Expand G(x,2)=U_x^2 U_F^{-1}.  The result is a pure
    # integer-reciprocal seven-term endpoint word.
    integer_expansion = [
        ((107, 1), 83),
        ((1710, 1), 17),
        ((207385, 1), -44),
        ((4459662850206890, 1), 22),
        ((2513489, 1), -24),
        ((7939642926390344818, 1), 12),
        ((3235259223, 1), 22),
    ]
    assert multiply_word(integer_expansion) == (1, 1)
    assert tangent_sheet(integer_expansion) == ((1, 1), 0, 0)
    mu_integer = generalized_lehmer(integer_expansion)
    assert abs(mu_integer - 1.3683628258403102) < 1e-14

    # Exact free Gaussian-valuation certificate for the five primitive generators.
    # Rows are p=(5,113,229,8861,42953); columns follow `generalized` above.
    valuation_rows = [
        (2, 0, 0, 12, -1),
        (0, -2, -1, -1, 0),
        (-1, -1, 0, -1, 4),
        (0, 0, 1, 0, 1),
        (0, 0, 1, 0, 1),
    ]
    coeffs = (83, 17, -22, -12, 22)
    assert all(sum(a * b for a, b in zip(row, coeffs)) == 0 for row in valuation_rows)
    eps = (7, 2, 0, 2, 7)
    assert sum(a * b for a, b in zip(eps, coeffs)) % 8 == 1

    # Fixed-total-work exponent from the already-proved generalized budget law.
    gamma = 2.0 * math.log(10.0) / mu_general
    assert abs(gamma - 3.624544991392124) < 1e-14

    print(f"generalized_mu={mu_general:.15f}")
    print(f"integer_expansion_mu={mu_integer:.15f}")
    print(f"fixed_budget_exponent={gamma:.15f}")
    print("general rational-turn endpoint / winding certificate: PASS")


if __name__ == "__main__":
    main()
