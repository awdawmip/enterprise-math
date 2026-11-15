#!/usr/bin/env python3
"""Finite exact audit of the fixed JT2 UR ordinary-Legendre norm-jet scalar.

Checks the stated finite prime range, not a uniform congruence.
All arithmetic uses integers modulo p or p**2; no floating point.
"""
from math import isqrt


def primes_upto(limit):
    for p in range(2, limit + 1):
        if all(p % d for d in range(2, isqrt(p) + 1)):
            yield p


def mod_inverse(a, p):
    return pow(a % p, -1, p)


def legendre_coeffs(n, modulus):
    if n == 0:
        return [1]
    previous, current = [1], [0, 1]
    for m in range(1, n):
        next_poly = [0] * (m + 2)
        a = (2 * m + 1) * mod_inverse(m + 1, modulus) % modulus
        b = m * mod_inverse(m + 1, modulus) % modulus
        for i, c in enumerate(current):
            next_poly[i + 1] = (next_poly[i + 1] + a * c) % modulus
        for i, c in enumerate(previous):
            next_poly[i] = (next_poly[i] - b * c) % modulus
        previous, current = current, next_poly
    return current


def norm_jet_scalar(p):
    assert p > 3 and p % 24 in (13, 19)
    n = (p - 1) // 3
    assert n % 2 == 0 and 2 * n + 1 < p
    q = p * p
    f = legendre_coeffs(n, q)
    half_q = mod_inverse(2, q)
    half_p = mod_inverse(2, p)
    f_at_t = sum(c * pow(half_q, i // 2, q) for i, c in enumerate(f) if i % 2 == 0) % q
    assert f_at_t % p == 0, f"CM0 violation p={p}"
    u = f_at_t // p
    jet_over_t = sum(i * c * pow(half_p, (i - 2) // 2, p)
                     for i, c in enumerate(f) if i % 2 == 0 and i >= 2) % p
    f_mod_p = [c % p for c in f]
    sq = [0] * (2 * n + 1)
    for i, a in enumerate(f_mod_p):
        if a:
            for j, b in enumerate(f_mod_p):
                if b:
                    sq[i + j] = (sq[i + j] + a * b) % p
    integral_over_t = sum(
        c * mod_inverse(j + 1, p) * pow(half_p, j // 2, p)
        for j, c in enumerate(sq) if j % 2 == 0
    ) % p
    epsilon = (9 * u * jet_over_t - 2 * integral_over_t - 3) % p
    return (p, n, u, jet_over_t, integral_over_t, epsilon)


def main():
    cases = [norm_jet_scalar(p) for p in primes_upto(997) if p % 24 in (13, 19)]
    assert len(cases) == 45
    assert cases[0] == (13, 4, 2, 11, 0, 0)
    assert cases[-1] == (997, 332, 473, 920, 609, 0)
    failures = [row for row in cases if row[-1]]
    print("p,n,Pn_over_p,jet_over_t,integral_over_t,epsilon")
    for p, n, u, jet, integral, epsilon in cases:
        print(f"{p},{n},{u},{jet},{integral},{epsilon}")
    print(f"TESTED={len(cases)} FAILURE_COUNT={len(failures)}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
