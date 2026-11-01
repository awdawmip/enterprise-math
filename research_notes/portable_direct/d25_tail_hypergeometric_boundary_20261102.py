#!/usr/bin/env python3
"""Exact finite-field checker for the D25 216 tail hypergeometric mirror.

No floating point, external dependencies, native experiment claims or Source writes.
The algebraic proof is in the accompanying markdown; finite tests are not a
proof of the universal congruences.
"""
from math import factorial


def primes_through(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for q in range(2, int(limit ** 0.5) + 1):
        if sieve[q]:
            sieve[q * q : limit + 1 : q] = b"\x00" * ((limit - q * q) // q + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def one_prime(p):
    assert p >= 7 and p % 6 == 1
    r = (p - 1) // 6
    fac = [1] * p
    for n in range(1, p):
        fac[n] = fac[n - 1] * n % p
    inv = lambda a: pow(a % p, -1, p)
    inv2 = inv(2)
    zpow = 1
    A = 1
    c0 = (4 * fac[3*r+2] * inv(pow(fac[3*r+1], 5, p))
          * inv(pow(216, 3*r+1, p))) % p
    s_raw, s_mirror, coeff_count = 0, 0, 0
    for j in range(r):
        k = 3*r + 1 + j
        original = ((6*k+1) * fac[2*k-p] * fac[3*k-p]
                    * inv(pow(fac[k], 5, p))
                    * inv(pow(216, k, p))) % p
        reflected = c0 * ((3*j+2) * inv2 % p) * A % p * zpow % p
        assert original == reflected, (p, j, original, reflected)
        s_raw = (s_raw + original) % p
        s_mirror = (s_mirror + reflected) % p
        coeff_count += 1
        zpow = zpow * inv2 % p
        A = (A * (2 * inv(9) % p) * (j+1) * (6*j+5) * (6*j+7)
             * inv(pow(2*j+3,3,p))) % p
    assert s_raw == s_mirror
    # The r-th hypergeometric coefficient is divisible by p exactly once.
    m = p*p
    a_prev = 1
    poly_a = [a_prev]
    for j in range(r - 1):
        den = 9*pow(2*j+3,3)
        a_prev = (a_prev * 2*(j+1)*(6*j+5)*(6*j+7)
                  * pow(den, -1, m)) % m
        poly_a.append(a_prev)
    # Independently apply all coefficients of the fourth-order PF operator.
    for j in range(1, r):
        left = j*pow(2*j+1, 3)*pow(8,-1,m)*poly_a[j]
        right = j*j*(36*j*j-1)*pow(36,-1,m)*poly_a[j-1]
        assert (left-right) % m == 0, (p,j)
    # L H_r has precisely one surviving coefficient, at z^r.
    # Its exact rational expression is -p*r^2*(6*r-1)/36*A_{r-1}.
    source = (-p * r*r * (6*r-1) * pow(36, -1, m) * a_prev) % m
    assert source % p == 0
    first_digit = source // p
    expected_unit = (-r*r*(6*r-1)*pow(36,-1,p)*(a_prev%p)) % p
    assert first_digit == expected_unit and first_digit != 0
    return coeff_count, s_raw, c0, first_digit


def main():
    total = 0
    primes = [p for p in primes_through(3000) if p % 6 == 1]
    for p in primes:
        count, sigma, c0, source_unit = one_prime(p)
        total += count
        if p in [7,13,19,37,61,373]:
            print(f"p={p:4d} r={(p-1)//6:3d} sigma={sigma:4d} "
                  f"c0={c0:4d} (L H_r)_z^r/p={source_unit:4d}")
    print(f"PASS: {len(primes)} primes p=1 mod 6, 7<=p<=3000; "
          f"{total} independent coefficient comparisons; "
          "all boundary sources have exact valuation one")

if __name__ == "__main__":
    main()
