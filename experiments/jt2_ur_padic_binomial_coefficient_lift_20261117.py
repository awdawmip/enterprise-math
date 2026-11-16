#!/usr/bin/env python3
"""Exact modular checks for JT2 hypergeometric-to-binomial p-adic lifting.

Checks the general coefficientwise mod-p^2 theorem for all p<=2000,
p=6m+1 prime, and the special CM-port quotient for p mod 24 in {13,19}.
All arithmetic is exact integer arithmetic; no third-party packages.
Finite tests are crosschecks, not an all-prime UR proof.
"""
from math import comb, isqrt


def primes_up_to(limit):
    flags = [True] * (limit + 1)
    flags[:2] = [False, False]
    for n in range(2, isqrt(limit) + 1):
        if flags[n]:
            for multiple in range(n * n, limit + 1, n):
                flags[multiple] = False
    return [n for n, good in enumerate(flags) if good]


def check_prime(p):
    m, modulus = (p - 1) // 6, p * p
    f = b = half = 1
    correction = 0
    F = B = 1
    L = 0
    half_inverse = pow(2, -1, modulus)

    for j in range(m + 1):
        assert (f - b * (1 + p * L)) % modulus == 0, (p, j)
        correction = (correction + (b % p) * L * half) % p

        if j == m:
            break

        f = (f * (6 * j + 1) * (3 * j + 1)
             * pow(9 * (2 * j + 1) * (j + 1), -1, modulus)) % modulus
        b = (b * (j - m) * (j - 2 * m)
             * pow((j - 3 * m) * (j + 1), -1, modulus)) % modulus
        L = (L + pow(6 * (j - m), -1, p)
             + pow(3 * (j - 2 * m), -1, p)
             - pow(2 * (j - 3 * m), -1, p)) % p
        half = half * half_inverse % modulus
        F = (F + f * half) % modulus
        B = (B + b * half) % modulus

    # Independent binomial coefficient extraction for B_m(1/2).
    A = sum(comb(2 * m, m - r) * comb(m, r) * 2**r
            for r in range(m + 1))
    denominator = 2**m * comb(3 * m, m)
    assert B == A * pow(denominator, -1, modulus) % modulus, p

    if p % 24 not in (13, 19):
        return None

    # CM0 is the previously established exact hypothesis for these classes.
    assert A % p == F % p == B % p == 0, p
    v_from_truncation = F // p
    v_from_binomial = ((A // p) * pow(denominator, -1, p)
                       + correction) % p
    assert v_from_binomial == v_from_truncation, p
    return p, m, v_from_truncation, (A // p) % p


def main():
    all_cases = 0
    cm_cases = []
    for p in primes_up_to(2000):
        if p % 6 != 1:
            continue
        all_cases += 1
        cm = check_prime(p)
        if cm is not None:
            cm_cases.append(cm)

    assert all_cases == 148
    assert len(cm_cases) == 77
    print(f"PASS: coefficientwise={all_cases}; CM-quotients={len(cm_cases)}")
    print("p, m, F_m(1/2)/p mod p, A_m/p mod p")
    for case in cm_cases[:8]:
        print(*case, sep=", ")


if __name__ == "__main__":
    main()
