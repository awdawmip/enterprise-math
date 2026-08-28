#!/usr/bin/env python3
"""Exact low-m regression for the Beta/Bernstein Route-A reduction.

This checker is evidence/regression only.  The all-m STP statements proved in the
research return are analytic; bounded-m execution here is not used as proof.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations
from math import comb


def mmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def trans(a):
    return [list(row) for row in zip(*a)]


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def diag(v):
    return [[Fraction(v[i]) if i == j else Fraction(0) for j in range(len(v))]
            for i in range(len(v))]


def msub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def det(a):
    n = len(a)
    x = [row[:] for row in a]
    out = Fraction(1)
    for c in range(n):
        p = next((r for r in range(c, n) if x[r][c]), None)
        if p is None:
            return Fraction(0)
        if p != c:
            x[c], x[p] = x[p], x[c]
            out = -out
        pivot = x[c][c]
        out *= pivot
        for r in range(c + 1, n):
            if not x[r][c]:
                continue
            f = x[r][c] / pivot
            for j in range(c + 1, n):
                x[r][j] -= f * x[c][j]
            x[r][c] = Fraction(0)
    return out


def inv(a):
    n = len(a)
    x = [a[i][:] + eye(n)[i] for i in range(n)]
    for c in range(n):
        p = next((r for r in range(c, n) if x[r][c]), None)
        if p is None:
            raise ZeroDivisionError("singular matrix")
        x[c], x[p] = x[p], x[c]
        pivot = x[c][c]
        x[c] = [z / pivot for z in x[c]]
        for r in range(n):
            if r == c or not x[r][c]:
                continue
            f = x[r][c]
            x[r] = [x[r][j] - f * x[c][j] for j in range(2 * n)]
    return [row[n:] for row in x]


def minor(a, rows, cols):
    return [[a[i][j] for j in cols] for i in rows]


def assert_stp(a, label):
    n = len(a)
    for k in range(1, n + 1):
        for rows in combinations(range(n), k):
            for cols in combinations(range(n), k):
                d = det(minor(a, rows, cols))
                if d <= 0:
                    raise AssertionError(f"{label}: nonpositive {k}-minor rows={rows} cols={cols}: {d}")


def route_a(m):
    n = m - 1
    w = [Fraction(((-1) ** i) * comb(n, i)) for i in range(m)]

    def h(q):
        den = 1
        for ell in range(m):
            den *= 1 + q + ell * m * m
        return Fraction(1, den)

    H = [[h(i + m * j) for j in range(m)] for i in range(m)]
    W = diag(w)
    e = [sum((H[i][j] * w[j] for j in range(m)), Fraction(0)) for i in range(m)]
    d = [sum((H[i][j] * w[i] for i in range(m)), Fraction(0)) for j in range(m)]
    if not all(x > 0 for x in e + d):
        raise AssertionError("signed normalizer lost positivity")
    E_inv = diag([1 / x for x in e])
    D_inv = diag([1 / x for x in d])
    A = mmul(mmul(E_inv, H), W)
    B = mmul(mmul(D_inv, trans(H)), W)
    R = [[Fraction(((-1) ** j) * comb(i, j)) if j <= i else Fraction(0)
          for j in range(m)] for i in range(m)]
    if mmul(R, R) != eye(m):
        raise AssertionError("binomial Mobius matrix is not involutive")
    Ahat = mmul(A, R)
    Bhat = mmul(B, R)
    C = mmul(mmul(W, H), W)
    P = inv(C)
    K = mmul(B, A)
    T = mmul(mmul(R, K), R)
    Q = [row[1:] for row in T[1:]]
    return H, P, Ahat, Bhat, Q


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-m", type=int, default=5)
    args = ap.parse_args()
    if args.max_m < 2:
        raise SystemExit("--max-m must be >= 2")

    for m in range(2, args.max_m + 1):
        H, P, Ahat, Bhat, Q = route_a(m)
        assert_stp(H, f"H(m={m})")
        assert_stp(P, f"C^-1(m={m})")
        assert_stp(Ahat, f"Ahat(m={m})")
        assert_stp(Bhat, f"Bhat(m={m})")
        if det(msub(eye(m - 1), Q)) == 0:
            raise AssertionError(f"finite regression found repeated fixed point at m={m}")
        print(f"m={m}: exact STP regressions PASS; det(I-Q) != 0")

    # Exact kill certificate for the naive positive-quotient / ordinary norm route.
    _, _, _, _, Q4 = route_a(4)
    q20 = Q4[2][0]
    if not q20 < 0:
        raise AssertionError("expected exact negative quotient entry at m=4")
    row0 = sum(abs(x) for x in Q4[0])
    if not row0 > 1:
        raise AssertionError("expected exact l_inf contraction failure at m=4")
    print("m=4 quotient kill certificate:")
    print(f"  Q[2,0] = {q20} < 0")
    print(f"  sum_j |Q[0,j]| = {row0} > 1")
    print("NOTE: bounded-m checks are regression/evidence only, not the all-m proof.")


if __name__ == "__main__":
    main()
