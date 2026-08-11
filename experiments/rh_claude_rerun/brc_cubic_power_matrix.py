#!/usr/bin/env python3
"""Exact checks for the cubic log-quadratic power-matrix frontier.

Finite synthetic algebra only. Not RH evidence.
"""
from fractions import Fraction


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
            for k in range(i, n):
                a[j][k] -= factor * a[i][k]
    out = Fraction(sign)
    for i in range(n):
        out *= a[i][i]
    return out


def power_det(xs):
    r = len(xs)
    return det_frac([[xs[i] ** j * xs[j] ** i for j in range(r)] for i in range(r)])


def logquad(A, B, r):
    return [A ** i * B ** (i * i) for i in range(r)]


def check_monotonicity_counterexample():
    xs = [Fraction(11, 12), Fraction(10, 11), Fraction(9, 10), Fraction(7, 8)]
    assert all(xs[i] > xs[i + 1] > 0 for i in range(3))
    d = power_det(xs)
    expected = Fraction(-560_198_940_167, 50_155_641_372_672_000_000)
    assert d == expected
    assert d < 0  # wrong sign relative to order-four q-Pascal baseline


def check_logquadratic_search():
    vals = sorted(
        {Fraction(n, d) for d in range(2, 10) for n in range(1, 10) if n != d},
        key=float,
    )
    checked = 0
    for r in range(2, 7):
        target = -1 if (r * (r - 1) // 2) % 2 else 1
        for A in vals:
            for B in vals:
                xs = logquad(A, B, r)
                if not all(xs[i] > xs[i + 1] > 0 for i in range(r - 1)):
                    continue
                checked += 1
                d = power_det(xs)
                sign = 1 if d > 0 else -1 if d < 0 else 0
                assert sign == target, (r, A, B, xs, d)
    return checked


def main():
    check_monotonicity_counterexample()
    checked = check_logquadratic_search()
    print("monotonicity-only counterexample: PASS")
    print("log-quadratic exact-rational instances checked:", checked)
    print("no log-quadratic sign failure found in bounded search")
    print("status: EVIDENCE_ONLY / RH_NOT_CLOSED")


if __name__ == "__main__":
    main()
