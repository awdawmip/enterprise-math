#!/usr/bin/env python3
"""
Exact rational regression for:
RS-PERFECT-PRIME-AP-GSTP-EXTERIOR-CONE-CERTIFICATE

This checker proves no all-m theorem by enumeration. It only verifies the finite
claims explicitly labeled as regression evidence in the research return.
"""

from fractions import Fraction
from itertools import combinations
from math import comb


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def zeros(n, m):
    return [[Fraction(0) for _ in range(m)] for _ in range(n)]


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    assert len(A[0]) == k
    C = zeros(n, m)
    for i in range(n):
        for r in range(k):
            if A[i][r] == 0:
                continue
            for j in range(m):
                C[i][j] += A[i][r] * B[r][j]
    return C


def matsub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def diag(v):
    n = len(v)
    M = zeros(n, n)
    for i, x in enumerate(v):
        M[i][i] = x
    return M


def inverse(A):
    n = len(A)
    M = [row[:] + eye(n)[i] for i, row in enumerate(A)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[pivot] = M[pivot], M[col]
        p = M[col][col]
        M[col] = [x / p for x in M[col]]
        for r in range(n):
            if r == col:
                continue
            f = M[r][col]
            if f:
                M[r] = [M[r][c] - f * M[col][c] for c in range(2 * n)]
    return [row[n:] for row in M]


def det(A):
    n = len(A)
    if n == 0:
        return Fraction(1)
    M = [row[:] for row in A]
    out = Fraction(1)
    sign = 1
    for col in range(n):
        pivot = next((r for r in range(col, n) if M[r][col] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            M[col], M[pivot] = M[pivot], M[col]
            sign *= -1
        p = M[col][col]
        out *= p
        for r in range(col + 1, n):
            if M[r][col]:
                f = M[r][col] / p
                for c in range(col + 1, n):
                    M[r][c] -= f * M[col][c]
    return out * sign


def minor(A, I, J):
    return det([[A[i][j] for j in J] for i in I])


def all_minors_positive(A, max_order=None):
    n, m = len(A), len(A[0])
    qmax = min(n, m) if max_order is None else max_order
    for q in range(1, qmax + 1):
        for I in combinations(range(n), q):
            for J in combinations(range(m), q):
                value = minor(A, I, J)
                if value <= 0:
                    return False, (q, I, J, value)
    return True, None


def pascal_t(n, t):
    return [[Fraction(comb(i, j)) * (t ** (i - j)) if j <= i else Fraction(0)
             for j in range(n)] for i in range(n)]


def ap_packet(m):
    n = m - 1
    H = zeros(m, m)
    for i in range(m):
        for j in range(m):
            H[i][j] = sum(
                (Fraction((-1) ** ell * comb(n, ell),
                          i + m * j + m * m * ell + 1)
                 for ell in range(n + 1)),
                Fraction(0),
            )
    w = [Fraction((-1) ** j * comb(n, j)) for j in range(m)]
    W = diag(w)
    e = [sum((H[i][j] * w[j] for j in range(m)), Fraction(0)) for i in range(m)]
    d = [sum((H[i][j] * w[i] for i in range(m)), Fraction(0)) for j in range(m)]
    E_inv = diag([1 / x for x in e])
    D_inv = diag([1 / x for x in d])
    A = matmul(matmul(E_inv, H), W)
    B = matmul(matmul(D_inv, list(map(list, zip(*H)))), W)
    R = [[Fraction((-1) ** j * comb(i, j)) if j <= i else Fraction(0)
          for j in range(m)] for i in range(m)]
    Ahat = matmul(A, R)
    Bhat = matmul(B, R)
    T = matmul(matmul(matmul(R, Bhat), R), Ahat)
    return R, Ahat, Bhat, T


def exact_regression():
    # The all-m half-Pascal identity is proved algebraically in the return.
    # Here it and the newly observed AP pencil patterns are regressed finitely.
    for m in range(2, 7):
        R, Ahat, Bhat, T = ap_packet(m)
        S = pascal_t(m, Fraction(1, 2))
        S_inv = pascal_t(m, Fraction(-1, 2))
        J = diag([Fraction((-1) ** i) for i in range(m)])
        assert matmul(matmul(S_inv, R), S) == J

        Astar = matmul(matmul(S_inv, Ahat), S)
        Bstar = matmul(matmul(S_inv, Bhat), S)
        Cstar = matmul(matmul(J, inverse(Bstar)), J)
        Tstar = matmul(matmul(S_inv, T), S)
        assert Tstar == matmul(inverse(Cstar), Astar)

        # Exploratory finite pattern only: not elevated to an all-m theorem.
        ok, witness = all_minors_positive(Astar)
        assert ok, ("Astar not STP", m, witness)
        ok, witness = all_minors_positive(Bstar)
        assert ok, ("Bstar not STP", m, witness)
        ok, witness = all_minors_positive(Cstar)
        assert ok, ("Cstar not STP", m, witness)

        Dstar = matsub(Cstar, Astar)
        ok, witness = all_minors_positive(Dstar, m - 1)
        assert ok, ("Dstar proper minors not positive", m, witness)
        assert det(Dstar) == 0

    # Exact operator-specific obstruction to every signed orthant transported by
    # the canonical half-Pascal midpoint S when m=2. Diagonal sign conjugation
    # preserves the product of the two off-diagonal signs.
    R, Ahat, Bhat, T = ap_packet(2)
    S = pascal_t(2, Fraction(1, 2))
    Tstar = matmul(matmul(pascal_t(2, Fraction(-1, 2)), T), S)
    assert Tstar[0][1] == Fraction(3, 28)
    assert Tstar[1][0] == Fraction(-2187, 6160)
    assert Tstar[0][1] * Tstar[1][0] < 0


if __name__ == "__main__":
    exact_regression()
    print("PASS: exact finite AP GSTP/exterior-cone regression")
