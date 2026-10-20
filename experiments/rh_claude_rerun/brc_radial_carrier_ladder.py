#!/usr/bin/env python3
"""Finite checks for radial-anchor and carrier-order BRC formulas.

Checks exact/synthetic algebra and scale arithmetic only. Not RH evidence.
"""
from fractions import Fraction
from math import sqrt


def det_frac(matrix):
    a = [list(map(Fraction, row)) for row in matrix]
    n = len(a)
    if n == 0:
        return Fraction(1)
    sign = 1
    for i in range(n):
        p = next((j for j in range(i, n) if a[j][i]), None)
        if p is None:
            return Fraction(0)
        if p != i:
            a[i], a[p] = a[p], a[i]
            sign *= -1
        pivot = a[i][i]
        for j in range(i + 1, n):
            factor = a[j][i] / pivot
            for l in range(i, n):
                a[j][l] -= factor * a[i][l]
    out = Fraction(sign)
    for i in range(n):
        out *= a[i][i]
    return out


def h_from_e(e, nmax):
    h = [Fraction(0)] * (nmax + 1)
    h[0] = Fraction(1)
    for n in range(1, nmax + 1):
        total = Fraction(0)
        for j in range(1, min(n, len(e) - 1) + 1):
            total += (-1) ** j * e[j] * h[n - j]
        h[n] = -total
    return h


def hget(h, n):
    return Fraction(0) if n < 0 or n >= len(h) else h[n]


def schur2(a, b, h):
    if b == 0:
        return hget(h, a)
    return det_frac([[hget(h, a), hget(h, a + 1)], [hget(h, b - 1), hget(h, b)]])


def check_radial_pair_majorant():
    # Actual Y: roots exp(+/- i*pi/3), elementary factor 1+z+z^2.
    # r=3 is the first locally unsafe width: h_3(Y)=-1.
    actual_h = h_from_e([Fraction(1), Fraction(1), Fraction(1)], 8)
    # Radial anchor {1,1}: elementary factor 1+2z+z^2, h_n=n+1.
    radial_h = h_from_e([Fraction(1), Fraction(2), Fraction(1)], 8)
    assert actual_h[3] == -1
    assert radial_h == [Fraction(n + 1) for n in range(9)]

    for a in range(4):
        for b in range(a + 1):
            av = schur2(a, b, actual_h)
            rv = schur2(a, b, radial_h)
            if (a, b) == (3, 0):
                assert av < 0 < rv
            else:
                assert 0 <= av <= rv, (a, b, av, rv)


def residual_bound(r, k, m):
    # Conservative endpoint tau=4/k; for d>=3 each displayed term increases
    # with tau on the regime used here.
    tau = 4.0 / k
    t = 4.0 * sqrt(r * tau)
    d0 = m + 1
    rho = 80.0 * t
    assert rho < 1.0 and 80.0 * tau < 1.0
    main = (2.0 / tau) * rho**d0 / (1.0 - rho)
    d_odd = d0 if d0 % 2 else d0 + 1
    d_even = d0 if d0 % 2 == 0 else d0 + 1
    odd = 2.0 * t * 80.0**d_odd * tau**(d_odd - 2) / (1.0 - (80.0 * tau) ** 2)
    even = 2.0 * t**2 * 80.0**d_even * tau**(d_even - 3) / (1.0 - (80.0 * tau) ** 2)
    return main + odd + even


def check_exponent_ladder():
    expected = {
        2: Fraction(3, 1),
        3: Fraction(2, 1),
        4: Fraction(5, 3),
        5: Fraction(3, 2),
        6: Fraction(7, 5),
        9: Fraction(5, 4),
    }
    for m, p in expected.items():
        d = m + 1
        assert Fraction(d, d - 2) == p

    # Linear-scale illustration from the report.
    assert residual_bound(10**13, 10**19, 108) < 0.011


def main():
    check_radial_pair_majorant()
    check_exponent_ladder()
    print("radial pair coefficient majorant: PASS")
    print("carrier exponent ladder: PASS")
    print("C=1e6, r=1e13, m=108 tail illustration: <0.011")
    print("RH status: NOT_CLOSED")


if __name__ == "__main__":
    main()
