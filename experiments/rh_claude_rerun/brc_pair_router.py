#!/usr/bin/env python3
"""Exact rational checks for the rectangular one-pair BRC router.

Finite algebra only; not RH evidence.
"""
from fractions import Fraction


def det_q(mat):
    a = [list(map(Fraction, row)) for row in mat]
    n = len(a)
    if n == 0:
        return Fraction(1)
    sign = 1
    out = Fraction(1)
    for k in range(n):
        pivot_row = next((i for i in range(k, n) if a[i][k] != 0), None)
        if pivot_row is None:
            return Fraction(0)
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign *= -1
        pivot = a[k][k]
        out *= pivot
        for i in range(k + 1, n):
            factor = a[i][k] / pivot
            for j in range(k + 1, n):
                a[i][j] -= factor * a[k][j]
    return sign * out


def complete_h(xs, nmax):
    h = [Fraction(0)] * (nmax + 1)
    h[0] = Fraction(1)
    for x in xs:
        new = [Fraction(0)] * (nmax + 1)
        for n in range(nmax + 1):
            power = Fraction(1)
            for j in range(nmax - n + 1):
                new[n + j] += h[n] * power
                power *= x
        h = new
    return h


def schur(lam, xs):
    lam = [x for x in lam if x > 0]
    if not lam:
        return Fraction(1)
    length = len(lam)
    nmax = max(lam[i] - i + length - 1 for i in range(length))
    h = complete_h(xs, nmax)

    def H(n):
        return Fraction(0) if n < 0 else h[n]

    return det_q([[H(lam[i] - i + j) for j in range(length)] for i in range(length)])


def check_router():
    X = [Fraction(2, 5), Fraction(3, 7), Fraction(5, 11), Fraction(7, 13)]
    Y = [Fraction(2, 17), Fraction(3, 19)]
    cases = 0
    for r in range(1, 5):
        for k in range(2, 5):
            lhs = schur([r] * k, X + Y)
            rhs = Fraction(0)
            for a in range(r + 1):
                for b in range(a + 1):
                    mu = [r] * (k - 2) + [r - b, r - a]
                    rhs += schur(mu, X) * schur([a, b], Y)
            assert lhs == rhs, (r, k, lhs, rhs)
            cases += 1
    return cases


def unsafe_branch_count(r, threshold):
    return sum(r - d + 1 for d in range(threshold, r + 1)) if r >= threshold else 0


def main():
    cases = check_router()
    for r in range(1, 20):
        for threshold in range(0, 25):
            expected = 0 if r < threshold else (r - threshold + 1) * (r - threshold + 2) // 2
            assert unsafe_branch_count(r, threshold) == expected
    print("rectangular pair-router exact checks: PASS")
    print("router cases:", cases)
    print("unsafe-branch triangular count checks: PASS")
    print("RH status: NOT_CLOSED")


if __name__ == "__main__":
    main()
