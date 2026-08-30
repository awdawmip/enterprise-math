#!/usr/bin/env python3
"""Exact regression for the Perfect Prime Beta-Bernstein oscillation lane.

Terminal scope of this checker:
1. retain the all-m raw SSR checkpoint regression for the actual AP model;
2. retain the exact m=5 obstruction to naive normalized complete monotonicity;
3. verify the unweighted Cauchy endpoint identities used by the terminal
   oscillation-route obstruction:
   - closed normalizers;
   - K_0 = I exactly;
   - the same raw SSR finite regression;
   - strict first normalized differences;
   - exact Pascal-conjugate factorization of reciprocal normalizers;
   - total nonnegativity of those finite conjugates in the configured range.

Bounded-m checks are regression only.  The return document supplies the
all-m algebraic proofs.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial
import argparse


def mmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def trans(a):
    return [list(row) for row in zip(*a)]


def diag(v):
    return [[Fraction(v[i]) if i == j else Fraction(0) for j in range(len(v))]
            for i in range(len(v))]


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


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


def pascal(n):
    return [[Fraction(comb(i, j)) if j <= i else Fraction(0)
             for j in range(n)] for i in range(n)]


def route_from_h(m, h):
    n = m - 1
    w = [Fraction(((-1) ** i) * comb(n, i)) for i in range(m)]
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
    MA = mmul(diag(e), Ahat)
    MB = mmul(diag(d), Bhat)
    NA = mmul(R, MA)
    NB = mmul(R, MB)
    RA = mmul(R, Ahat)
    RB = mmul(R, Bhat)
    K = mmul(B, A)
    return {
        "w": w, "H": H, "e": e, "d": d, "R": R,
        "Ahat": Ahat, "Bhat": Bhat, "NA": NA, "NB": NB,
        "RA": RA, "RB": RB, "K": K,
    }


def route_ap(m):
    n = m - 1

    def h(q):
        den = 1
        for ell in range(m):
            den *= 1 + q + ell * m * m
        return Fraction(1, den)

    return route_from_h(m, h)


def route_cauchy(m):
    return route_from_h(m, lambda q: Fraction(1, q + 1))


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


def assert_tn(M, label):
    n = len(M)
    for q in range(1, n + 1):
        for rows in combinations(range(n), q):
            for cols in combinations(range(n), q):
                value = det(minor(M, rows, cols))
                if value < 0:
                    raise AssertionError(
                        f"{label}: q={q} rows={rows} cols={cols} got {value} < 0"
                    )


def scaled(M, c):
    return [[c * x for x in row] for row in M]


def add_scalar_identity(M, a):
    return [[M[i][j] + (a if i == j else 0)
             for j in range(len(M))] for i in range(len(M))]


def cauchy_closed_normalizers(m):
    n = m - 1
    e = []
    d = []
    for i in range(m):
        den = 1
        for r in range(m):
            den *= i + 1 + m * r
        e.append(Fraction(factorial(n) * (m ** n), den))
    for j in range(m):
        den = 1
        for r in range(m):
            den *= m * j + 1 + r
        d.append(Fraction(factorial(n), den))
    return e, d


def assert_cauchy_endpoint(m):
    n = m - 1
    data = route_cauchy(m)
    e0, d0 = cauchy_closed_normalizers(m)
    if data["e"] != e0 or data["d"] != d0:
        raise AssertionError(f"m={m}: closed Cauchy normalizers mismatch")
    if data["K"] != eye(m):
        raise AssertionError(f"m={m}: exact Cauchy endpoint should satisfy K0=I")

    # The same order-map raw SSR and first normalized sign survive.
    assert_raw_ssr(data["NA"], f"Cauchy R M_A(m={m})")
    assert_raw_ssr(data["NB"], f"Cauchy R M_B(m={m})")
    for k in range(1, m):
        if not data["RA"][1][k] < 0:
            raise AssertionError(f"m={m}: Cauchy (R Ahat)[1,{k}] should be < 0")
        if not data["RB"][1][k] < 0:
            raise AssertionError(f"m={m}: Cauchy (R Bhat)[1,{k}] should be < 0")

    # P = R J is the ordinary Pascal matrix and P^{-1}=J R.
    R = data["R"]
    J = diag([(-1) ** i for i in range(m)])
    P = pascal(m)
    Pinv = mmul(J, R)
    if mmul(R, J) != P or mmul(Pinv, P) != eye(m) or mmul(P, Pinv) != eye(m):
        raise AssertionError("Pascal conjugation identity failed")
    N = mmul(mmul(Pinv, diag(list(range(m)))), P)

    N_expected = [[Fraction(0) for _ in range(m)] for __ in range(m)]
    for i in range(m):
        N_expected[i][i] = Fraction(i)
        if i:
            N_expected[i][i - 1] = Fraction(i)
    if N != N_expected:
        raise AssertionError(f"m={m}: Pascal number operator mismatch")

    LE = mmul(mmul(Pinv, diag([1 / x for x in data["e"]])), P)
    LD = mmul(mmul(Pinv, diag([1 / x for x in data["d"]])), P)

    FE = eye(m)
    for r in range(m):
        FE = mmul(FE, add_scalar_identity(N, Fraction(1 + m * r)))
    FE = scaled(FE, Fraction(1, factorial(n) * (m ** n)))

    FD = eye(m)
    for r in range(m):
        FD = mmul(FD, add_scalar_identity(N, Fraction(1 + r, m)))
    FD = scaled(FD, Fraction(m ** m, factorial(n)))

    if LE != FE:
        raise AssertionError(f"m={m}: E reciprocal-normalizer factorization failed")
    if LD != FD:
        raise AssertionError(f"m={m}: D reciprocal-normalizer factorization failed")

    # Regression only; the return proves TN for all m by bidiagonal TN +
    # Cauchy-Binet closure.
    assert_tn(LE, f"Cauchy J R E^-1 R J(m={m})")
    assert_tn(LD, f"Cauchy J R D^-1 R J(m={m})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-m", type=int, default=6)
    args = ap.parse_args()
    if args.max_m < 2:
        raise SystemExit("--max-m must be >= 2")

    for m in range(2, args.max_m + 1):
        ap_data = route_ap(m)
        assert_raw_ssr(ap_data["NA"], f"AP R M_A(m={m})")
        assert_raw_ssr(ap_data["NB"], f"AP R M_B(m={m})")
        for k in range(1, m):
            if not ap_data["RA"][1][k] < 0:
                raise AssertionError(f"m={m}: expected AP (R Ahat)[1,{k}] < 0")
            if not ap_data["RB"][1][k] < 0:
                raise AssertionError(f"m={m}: expected AP (R Bhat)[1,{k}] < 0")

        assert_cauchy_endpoint(m)
        print(
            f"m={m}: AP raw SSR + first sign PASS; "
            "Cauchy K0=I + raw SSR + TN normalizer factorization PASS"
        )

    # Exact obstruction to the tempting all-order normalized complete-monotonicity route.
    ap5 = route_ap(5)
    if not ap5["RA"][3][1] > 0:
        raise AssertionError("m=5 AP model should have (R Ahat)[3,1] > 0")
    if not ap5["RB"][3][1] > 0:
        raise AssertionError("m=5 AP model should have (R Bhat)[3,1] > 0")
    print("m=5 AP normalized higher-difference obstruction:")
    print(f"  (R Ahat)[3,1] = {ap5['RA'][3][1]} > 0")
    print(f"  (R Bhat)[3,1] = {ap5['RB'][3][1]} > 0")
    print(
        "NOTE: bounded-m checks are exact regression only; "
        "all-m proofs are in the research return."
    )


if __name__ == "__main__":
    main()
