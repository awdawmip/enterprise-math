#!/usr/bin/env python3
"""Exact regression for the Perfect Prime Beta-Bernstein oscillation lane.

This checker supports the analytic checkpoint only.  Finite-m checks are not an
all-m proof.  The analytic claims checked structurally are:

1. after removing the row normalizers, left Mobius/binomial differencing turns
   both common-measure half maps into strictly sign-regular matrices with
   signature eps_q=(-1)^(q(q-1)/2);
2. the first normalized difference is strictly negative in every nonconstant
   Bernstein column;
3. naive higher-order complete-monotonicity of the normalized row sequences is
   false in the actual AP model (already at m=5).
"""
from fractions import Fraction
from itertools import combinations
from math import comb
import argparse


def mmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def trans(a):
    return [list(row) for row in zip(*a)]


def diag(v):
    return [[Fraction(v[i]) if i == j else Fraction(0) for j in range(len(v))]
            for i in range(len(v))]


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


def minor(a, rows, cols):
    return [[a[i][j] for j in cols] for i in rows]


def route(m):
    n = m - 1
    w = [Fraction(((-1) ** i) * comb(n, i)) for i in range(m)]

    def h(q):
        den = 1
        for ell in range(m):
            den *= 1 + q + ell * m * m
        return Fraction(1, den)

    H = [[h(i + m * j) for j in range(m)] for i in range(m)]
    W = diag(w)
    e = [sum((H[i][j] * w[j] for j in range(m)), Fraction(0))
         for i in range(m)]
    d = [sum((H[i][j] * w[i] for i in range(m)), Fraction(0))
         for j in range(m)]
    Einv = diag([1 / x for x in e])
    Dinv = diag([1 / x for x in d])
    A = mmul(mmul(Einv, H), W)
    B = mmul(mmul(Dinv, trans(H)), W)
    R = [[Fraction(((-1) ** j) * comb(i, j)) if j <= i else Fraction(0)
          for j in range(m)] for i in range(m)]
    Ahat = mmul(A, R)
    Bhat = mmul(B, R)

    # Raw common-measure Bernstein moment matrices.
    MA = mmul(diag(e), Ahat)
    MB = mmul(diag(d), Bhat)
    NA = mmul(R, MA)
    NB = mmul(R, MB)
    RA = mmul(R, Ahat)
    RB = mmul(R, Bhat)
    return NA, NB, RA, RB


def assert_raw_ssr(M, label):
    n = len(M)
    for q in range(1, n + 1):
        expected = -1 if ((q * (q - 1) // 2) % 2) else 1
        for rows in combinations(range(n), q):
            for cols in combinations(range(n), q):
                value = det(minor(M, rows, cols))
                if value == 0 or (1 if value > 0 else -1) != expected:
                    raise AssertionError(
                        f"{label}: q={q} rows={rows} cols={cols} got {value}; "
                        f"expected strict sign {expected}"
                    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-m", type=int, default=6)
    args = ap.parse_args()
    if args.max_m < 2:
        raise SystemExit("--max-m must be >= 2")

    for m in range(2, args.max_m + 1):
        NA, NB, RA, RB = route(m)
        assert_raw_ssr(NA, f"R M_A(m={m})")
        assert_raw_ssr(NB, f"R M_B(m={m})")
        # r=1 is the covariance/monotone-likelihood-ratio sign theorem.
        for k in range(1, m):
            if not RA[1][k] < 0:
                raise AssertionError(f"m={m}: expected (R Ahat)[1,{k}] < 0")
            if not RB[1][k] < 0:
                raise AssertionError(f"m={m}: expected (R Bhat)[1,{k}] < 0")
        print(f"m={m}: raw SSR signature + first normalized difference PASS")

    # Exact obstruction to the tempting all-order complete-monotonicity route.
    _, _, RA5, RB5 = route(5)
    if not RA5[3][1] > 0:
        raise AssertionError("m=5 actual AP model should have (R Ahat)[3,1] > 0")
    if not RB5[3][1] > 0:
        raise AssertionError("m=5 actual AP model should have (R Bhat)[3,1] > 0")
    print("m=5 normalized higher-difference obstruction:")
    print(f"  (R Ahat)[3,1] = {RA5[3][1]} > 0")
    print(f"  (R Bhat)[3,1] = {RB5[3][1]} > 0")
    print("NOTE: bounded-m checks are exact regression only; raw SSR is proved analytically.")


if __name__ == "__main__":
    main()
