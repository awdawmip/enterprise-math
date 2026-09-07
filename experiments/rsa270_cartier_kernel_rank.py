#!/usr/bin/env python3
"""
Finite-field ternary-kernel rank experiment for the faithful twisted divisor sum
A_e(n)=sum_{d|n} chi_e(d).

This is finite evidence accompanying the exact non-3-automatic theorem in
research_notes/RSA270_CARTIER_FINITE_STATE_NOGO_20260908.md.

Researcher-ID: EM-DIRECT-66DE45
No RSA factor is used or produced.
"""
from math import gcd


def order_mod(g, p):
    x = 1
    for k in range(1, p):
        x = (x * g) % p
        if x == 1:
            return k
    raise AssertionError("no order found")


def character(e, ell, g):
    m = 3 ** e
    L = 2 * 3 ** (e - 1)
    assert order_mod(g, ell) == L

    dlog = {}
    x = 1
    for j in range(L):
        dlog[x] = j
        x = (2 * x) % m
    assert len(dlog) == L

    def chi(n):
        r = n % m
        if r % 3 == 0:
            return 0
        return pow(g, dlog[r], ell)

    return chi


def twisted_divisor_sieve(e, ell, g, Nmax):
    chi = character(e, ell, g)
    A = [0] * (Nmax + 1)
    for d in range(1, Nmax + 1):
        c = chi(d)
        if c:
            for n in range(d, Nmax + 1, d):
                A[n] = (A[n] + c) % ell
    return A


def rank_mod(rows, p):
    if not rows:
        return 0
    A = [row[:] for row in rows]
    m = len(A)
    n = len(A[0])
    rank = 0
    col = 0
    while rank < m and col < n:
        pivot = None
        for i in range(rank, m):
            if A[i][col] % p:
                pivot = i
                break
        if pivot is None:
            col += 1
            continue

        A[rank], A[pivot] = A[pivot], A[rank]
        inv = pow(A[rank][col] % p, -1, p)
        A[rank] = [(x * inv) % p for x in A[rank]]

        for i in range(m):
            if i == rank:
                continue
            f = A[i][col] % p
            if f:
                A[i] = [(x - f * y) % p for x, y in zip(A[i], A[rank])]

        rank += 1
        col += 1
    return rank


def kernel_ranks(e, ell, g, depth, vector_len):
    max_index = (3 ** depth) * vector_len + 3 ** depth
    A = twisted_divisor_sieve(e, ell, g, max_index)
    out = []
    for j in range(depth + 1):
        step = 3 ** j
        rows = [
            [A[step * n + r] for n in range(1, vector_len + 1)]
            for r in range(step)
        ]
        out.append(rank_mod(rows, ell))
    return out


def check_invariance(e, ell, g):
    A = twisted_divisor_sieve(e, ell, g, 5000)
    for n in range(1, 1500):
        assert A[3 * n] == A[n]


def main():
    cases = [
        # (e, ell, faithful generator g, depth, vector length, expected ranks)
        (2, 7, 3, 5, 270, [1, 3, 9, 27, 81, 243]),
        (3, 19, 2, 5, 270, [1, 3, 9, 27, 81, 243]),
        (4, 109, 36, 4, 120, [1, 3, 9, 27, 81]),
    ]

    for e, ell, g, depth, vec_len, expected in cases:
        check_invariance(e, ell, g)
        got = kernel_ranks(e, ell, g, depth, vec_len)
        print(f"e={e} ell={ell} g={g}: {got}")
        assert got == expected, (e, got, expected)
        assert got == [3 ** j for j in range(depth + 1)]

    print("ALL PASS")


if __name__ == "__main__":
    main()
