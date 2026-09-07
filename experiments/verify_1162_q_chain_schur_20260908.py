#!/usr/bin/env python3
"""Exact Fraction verifier for #1162 q-chain Schur elimination.

No floating point, Fourier diagonalization, trigonometry, or differentiation.
The checker constructs the fine cycle matrix, Schur-eliminates hidden vertices
by exact rational Gaussian elimination, and compares the result to the
continuant/Chebyshev closed form.
"""
from __future__ import annotations

from fractions import Fraction

Q = Fraction


def cycle_matrix(N: int, u: Fraction) -> list[list[Fraction]]:
    A = [[Q(0) for _ in range(N)] for __ in range(N)]
    g = N * N
    for i in range(N):
        A[i][i] += 2 * g + u
        A[i][(i + 1) % N] -= g
        A[i][(i - 1) % N] -= g
    return A


def inverse(A: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(A)
    aug = [
        [Q(A[i][j]) for j in range(n)] + [Q(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for c in range(n):
        pivot = next(r for r in range(c, n) if aug[r][c])
        aug[c], aug[pivot] = aug[pivot], aug[c]
        v = aug[c][c]
        aug[c] = [x / v for x in aug[c]]
        for r in range(n):
            if r == c or not aug[r][c]:
                continue
            f = aug[r][c]
            aug[r] = [aug[r][j] - f * aug[c][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def schur(A: list[list[Fraction]], keep: list[int]) -> list[list[Fraction]]:
    n = len(A)
    keep_set = set(keep)
    hidden = [i for i in range(n) if i not in keep_set]
    Akk = [[A[i][j] for j in keep] for i in keep]
    Akh = [[A[i][j] for j in hidden] for i in keep]
    Ahk = [[A[i][j] for j in keep] for i in hidden]
    inv_h = inverse([[A[i][j] for j in hidden] for i in hidden])

    tmp = [
        [sum(Akh[i][r] * inv_h[r][j] for r in range(len(hidden))) for j in range(len(hidden))]
        for i in range(len(keep))
    ]
    prod = [
        [sum(tmp[i][r] * Ahk[r][j] for r in range(len(hidden))) for j in range(len(keep))]
        for i in range(len(keep))
    ]
    return [[Akk[i][j] - prod[i][j] for j in range(len(keep))] for i in range(len(keep))]


def continuants(y: Fraction, q: int) -> list[Fraction]:
    if q < 2:
        raise ValueError("q must be >=2")
    U = [Q(1), 2 * y]
    for _ in range(2, q):
        U.append(2 * y * U[-1] - U[-2])
    return U


def predicted_parameters(N: int, q: int, u: Fraction) -> tuple[Fraction, Fraction]:
    g = q * q * N * N
    y = Q(1) + u / (2 * g)
    U = continuants(y, q)
    Uqm1 = U[q - 1]
    Uqm2 = U[q - 2]
    Tq = y * Uqm1 - Uqm2
    alpha = Q(q * q) / Uqm1
    uprime = 2 * N * N * (Tq - 1)
    return alpha, uprime


def scale(A: list[list[Fraction]], c: Fraction) -> list[list[Fraction]]:
    return [[c * x for x in row] for row in A]


def main() -> int:
    probes = [Q(1, 7), Q(1, 3), Q(2, 5), Q(3, 2)]
    checks = 0
    for N in range(2, 6):
        for q in range(2, 6):
            for u in probes:
                fine = cycle_matrix(q * N, u)
                actual = schur(fine, [q * i for i in range(N)])
                alpha, uprime = predicted_parameters(N, q, u)
                expected = scale(cycle_matrix(N, uprime), alpha)
                assert actual == expected, (N, q, u, actual, expected)
                checks += 1
    print(f"exact Schur checks={checks}")
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
