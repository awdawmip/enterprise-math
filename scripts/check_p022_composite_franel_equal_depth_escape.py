#!/usr/bin/env python3
"""Exact regression for the P022 composite Franel equal-depth first-jet reduction.

Proof is in the research return. This script only checks the derived congruence and
maps the finite exceptional locus; finite absence is not promoted to theorem.
"""
from math import comb


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = 3 if d == 2 else d + 2
    return True


def franel_table(limit: int) -> list[int]:
    f = [0] * (limit + 1)
    f[0] = 1
    if limit >= 1:
        f[1] = 2
    for n in range(1, limit):
        f[n + 1] = ((7*n*n + 7*n + 2) * f[n] + 8*n*n * f[n-1]) // ((n+1)**2)
    return f


def harmonic(n: int, p: int) -> int:
    return sum(pow(j, -1, p) for j in range(1, n + 1)) % p


def central_a(j: int, p: int, modulus: int) -> int:
    sign = -1 if j & 1 else 1
    return sign * pow(comb(2*j, j), 3, modulus) * pow(pow(64, j, modulus), -1, modulus) % modulus


def midpoint_first_jet(prime: int, f: list[int]) -> tuple[int, int, int, int]:
    m = (prime - 1) // 2
    mod2 = prime * prime
    S = sum(central_a(j, prime, mod2) for j in range(m + 1)) % mod2
    T = 0
    U = 0
    inv2 = pow(2, -1, prime)
    for j in range(m + 1):
        a = central_a(j, prime, prime)
        hj = harmonic(j, prime)
        h2j = harmonic(2*j, prime)
        T = (T + a * (h2j - inv2 * hj)) % prime
        U = (U + a * hj) % prime
    if f[m] % prime:
        raise AssertionError("forced midpoint is not a p-zero")
    if S % prime:
        raise AssertionError("central sum must vanish mod p in the forced sector")
    c = (S // prime) % prime
    q = (f[m] // prime) % prime
    if f[m] % mod2 != (S - 3 * prime * T) % mod2:
        raise AssertionError("midpoint p^2 expansion failed")
    if q != (c - 3*T) % prime:
        raise AssertionError("midpoint quotient first jet failed")
    if U != 2*T % prime:
        raise AssertionError("U=2T harmonic pairing failed")
    if (2*q - (2*c - 3*U)) % prime:
        raise AssertionError("paired first-jet form failed")
    return q, c, T, U


def main() -> None:
    limit = 20000
    f = franel_table((limit - 1)//2)
    forced = 0
    scalar_hasse_zeros = []
    for p in range(5, limit):
        if not is_prime(p) or p % 6 != 5 or p % 8 not in (5, 7):
            continue
        forced += 1
        midpoint_first_jet(p, f)
        k = (p + 1)//6
        n = 2*k - 1
        if f[n] % p == 0:
            scalar_hasse_zeros.append((p, n, (p-1)//2))
    print({
        "limit_exclusive": limit,
        "forced_sector_primes": forced,
        "first_jet_failures": 0,
        "scalar_hasse_zero_candidates": scalar_hasse_zeros,
        "role": "FINITE_REGRESSION_ONLY_NOT_A_PROOF",
    })


if __name__ == "__main__":
    main()
