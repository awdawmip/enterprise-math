#!/usr/bin/env python3
"""Exact regression for RS-PRIME-COORD-FACTOR-CRITICAL-COFACTOR-SUPPORT-COMPRESSION.

This checker verifies the finite/indexing layer of the proof:
* the Perfect Prime Table cells partition I_m exactly;
* prime visibility is equivalent to p <= U_m;
* the N-native kappa-layer covers every prime factor whenever P^+(N)^2 <= kappa*N;
* cell products agree with the polynomial P_m evaluated in Z/NZ;
* the gcd interface extracts a proper divisor on exhaustively checked covered inputs;
* an exact unbalanced counterexample lies outside the layer.

The asymptotic fast-multipoint complexity bound is proved in the return, not inferred
from this finite regression.
"""
from __future__ import annotations

import argparse
from math import gcd, isqrt


def ceil_sixth_root(x: int) -> int:
    if x < 0:
        raise ValueError("x must be nonnegative")
    if x <= 1:
        return x
    lo, hi = 0, 1
    while hi**6 < x:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**6 >= x:
            hi = mid
        else:
            lo = mid
    return hi


def layer_m(N: int, kappa: int) -> int:
    if N < 2 or kappa < 1:
        raise ValueError
    return max(2, ceil_sixth_root(kappa * N))


def bounds(m: int) -> tuple[int, int]:
    return m + 2, m**3 + m + 1


def cell_elements(m: int, i: int, j: int) -> list[int]:
    return [1 + i + m * j + k * m * m for k in range(m)]


def coord_of_x(m: int, x: int) -> tuple[int, int, int] | None:
    L, U = bounds(m)
    if not (L <= x <= U):
        return None
    u = x - (m + 1)  # 1,...,m^3
    z = u - 1
    i = 1 + (z % m)
    j = 1 + ((z // m) % m)
    k = z // (m * m)
    assert x == 1 + i + m * j + k * m * m
    return i, j, k


def visible_coord_prime(m: int, p: int) -> tuple[int, int, int] | None:
    L, U = bounds(m)
    r = ((L + p - 1) // p) * p
    if r > U:
        return None
    i, j, _ = coord_of_x(m, r)
    return i, j, r


def cell_product_mod(m: int, i: int, j: int, N: int) -> int:
    a = 1
    for x in cell_elements(m, i, j):
        a = (a * (x % N)) % N
    return a


def prime_factors_distinct(n: int) -> list[int]:
    out: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out.append(n)
    return out


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def primes_upto(n: int) -> list[int]:
    return [p for p in range(2, n + 1) if is_prime(p)]


def poly_mul(a: list[int], b: list[int], mod: int) -> list[int]:
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % mod
    return c


def P_coeffs(m: int, N: int) -> list[int]:
    M = m * m
    p = [1]
    for k in range(m):
        p = poly_mul(p, [(1 + k * M) % N, 1], N)
    return p


def eval_poly(c: list[int], x: int, N: int) -> int:
    y = 0
    for a in reversed(c):
        y = (y * x + a) % N
    return y


def extract_one_direct_verifier(m: int, N: int):
    """Verifier only: leaf scan is used after gcd=N.

    The return proves that a production implementation can replace this leaf scan
    with a binary product/gcd descent at the same cell without changing semantics.
    """
    for i in range(1, m + 1):
        for j in range(1, m + 1):
            g = gcd(cell_product_mod(m, i, j, N), N)
            if 1 < g < N:
                return g
            if g == N:
                for x in cell_elements(m, i, j):
                    h = gcd(x, N)
                    if 1 < h < N:
                        return h
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-N", type=int, default=5000)
    ap.add_argument("--partition-max-m", type=int, default=9)
    args = ap.parse_args()

    # Exact partition / mixed-radix indexing.
    partition_cases = 0
    for m in range(2, args.partition_max_m + 1):
        rows = []
        for i in range(1, m + 1):
            for j in range(1, m + 1):
                rows.extend(cell_elements(m, i, j))
        L, U = bounds(m)
        assert sorted(rows) == list(range(L, U + 1))
        assert len(rows) == len(set(rows)) == m**3
        partition_cases += 1

    # Visibility iff p <= U_m.
    visibility_cases = 0
    for m in range(2, min(args.partition_max_m, 8) + 1):
        _, U = bounds(m)
        for p in primes_upto(U + 50):
            hit = visible_coord_prime(m, p)
            assert (hit is not None) == (p <= U)
            if hit is not None:
                i, j, r = hit
                assert r % p == 0
                assert r in cell_elements(m, i, j)
                assert cell_product_mod(m, i, j, p) == 0
            visibility_cases += 1

    # Polynomial representation over composite moduli.
    poly_cases = 0
    for N in (91, 221, 1001, 2018, 10403):
        for m in range(2, 7):
            c = P_coeffs(m, N)
            for i in range(1, m + 1):
                for j in range(1, m + 1):
                    assert eval_poly(c, i + m * j, N) == cell_product_mod(m, i, j, N)
                    poly_cases += 1

    # Exact N-blind family coverage and extraction regression.
    sufficient_family_cases = 0
    visible_family_extract_cases = 0
    for N in range(4, args.max_N + 1):
        fs = prime_factors_distinct(N)
        if len(fs) == 1 and fs[0] == N:
            continue  # prime input
        pmax = max(fs)
        for kappa in (1, 2, 4):
            m = layer_m(N, kappa)
            _, U = bounds(m)
            actual = all(visible_coord_prime(m, p) is not None for p in fs)
            assert actual == (pmax <= U)

            # Proved sufficient family: P^+(N)^2 <= kappa*N.
            if pmax * pmax <= kappa * N:
                assert actual
                sufficient_family_cases += 1

            # Broader exact finite regression wherever the layer happens to cover
            # every prime factor and U<N, so a leaf cannot itself be a multiple of N.
            if actual and U < N:
                g = extract_one_direct_verifier(m, N)
                assert g is not None and 1 < g < N and N % g == 0
                visible_family_extract_cases += 1

    # Exact failure outside the kappa=4 layer.
    N, kappa = 2018, 4
    m = layer_m(N, kappa)
    L, U = bounds(m)
    assert (m, L, U) == (5, 7, 131)
    assert prime_factors_distinct(N) == [2, 1009]
    assert visible_coord_prime(m, 2) == (2, 1, 8)
    assert visible_coord_prime(m, 1009) is None

    print(
        "PCF5_SUPPORT_CHECK_PASS"
        f" partition_cases={partition_cases}"
        f" visibility_cases={visibility_cases}"
        f" polynomial_cases={poly_cases}"
        f" sufficient_family_cases={sufficient_family_cases}"
        f" visible_family_extract_cases={visible_family_extract_cases}"
        " counterexample=N2018_kappa4_q1009_outside_U131"
    )


if __name__ == "__main__":
    main()
