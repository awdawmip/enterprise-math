#!/usr/bin/env python3
"""Exact checks for the BRC RH critical-band rerun.

This script checks finite algebra only. It does not prove RH.
"""
from fractions import Fraction
from math import factorial


def det_frac(matrix):
    a = [list(map(Fraction, row)) for row in matrix]
    n = len(a)
    if n == 0:
        return Fraction(1)
    sign = 1
    prev = Fraction(1)
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k]), None)
            if swap is None:
                return Fraction(0)
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) / prev
        prev = pivot
    return sign * a[-1][-1]


def toeplitz_minor(seq, r, k):
    if r == 0:
        return Fraction(1)
    return det_frac([
        [Fraction(0) if k + j - i < 0 else seq[k + j - i] for j in range(r)]
        for i in range(r)
    ])


def inv_factorial_sequence(nmax):
    return [Fraction(1, factorial(n)) for n in range(nmax + 1)]


def inv_factorial_minor_formula(r, k):
    out = Fraction(1)
    for j in range(r):
        out *= Fraction(factorial(j), factorial(k + j))
    return out


def check_exponential_baseline():
    seq = inv_factorial_sequence(40)
    for r in range(1, 8):
        for k in range(0, 10):
            d = toeplitz_minor(seq, r, k)
            expected = inv_factorial_minor_formula(r, k)
            assert d == expected, (r, k, d, expected)
            if k >= 1:
                q = (
                    toeplitz_minor(seq, r, k - 1)
                    * toeplitz_minor(seq, r, k + 1)
                    / d**2
                )
                assert q == Fraction(k, k + r), (r, k, q)


def moment_counterexample():
    # Positive finite measure: 4*delta_1 + 3*delta_3 + 2*delta_4 + delta_14.
    xs = [1, 3, 4, 14]
    ws = [4, 3, 2, 1]
    moments = [
        sum(Fraction(w) * Fraction(x) ** n for x, w in zip(xs, ws))
        for n in range(40)
    ]
    a = [moments[n] / factorial(2 * n) for n in range(40)]
    d42 = toeplitz_minor(a, 4, 2)
    assert d42 == Fraction(-66408249317, 365783040)

    exact_q = [
        Fraction(74, 35),
        Fraction(14785, 9583),
        Fraction(10146325, 8743849),
    ]
    for n in range(1, 4):
        q_m = moments[n - 1] * moments[n + 1] / moments[n] ** 2
        assert q_m == exact_q[n - 1]
        assert q_m < Fraction(2 * n + 1, 2 * n - 1)

    # Analytic tail used in the report:
    # Q_n - 1 <= (195/28)(2/7)^(n-1) < 7(2/7)^(n-1)
    # and for n>=4 this is < 2/(2n-1).
    for n in range(4, 30):
        envelope = Fraction(7) * Fraction(2, 7) ** (n - 1)
        assert envelope < Fraction(2, 2 * n - 1)
        q_m = moments[n - 1] * moments[n + 1] / moments[n] ** 2
        assert q_m - 1 < envelope
        assert q_m < Fraction(2 * n + 1, 2 * n - 1)
        q_a = a[n - 1] * a[n + 1] / a[n] ** 2
        assert q_a < Fraction(n, n + 1)

    return d42


def schur_two_row(a, b, x, y):
    assert a >= b >= 0
    m = a - b
    return (x * y) ** b * sum(x ** (m - j) * y ** j for j in range(m + 1))


def schur_two_row_weyl(a, b, x, y):
    assert x != y
    return (x ** (a + 1) * y ** b - x ** b * y ** (a + 1)) / (x - y)


def check_pair_cluster_algebra():
    tests = [
        (1, 0, Fraction(2), Fraction(3)),
        (5, 2, Fraction(2, 5), Fraction(7, 11)),
        (9, 4, Fraction(5, 7), Fraction(11, 13)),
        (12, 11, Fraction(3, 2), Fraction(4, 3)),
    ]
    for a, b, x, y in tests:
        lhs = schur_two_row(a, b, x, y)
        rhs = schur_two_row_weyl(a, b, x, y)
        assert lhs == rhs, (a, b, lhs, rhs)


def main():
    check_exponential_baseline()
    d42 = moment_counterexample()
    check_pair_cluster_algebra()
    print("exponential baseline determinant/q checks: PASS")
    print("Turan+Stieltjes no-go counterexample D_{4,2}:", d42)
    print("two-variable Schur cluster algebra: PASS")
    print("RH status: NOT_CLOSED")


if __name__ == "__main__":
    main()
