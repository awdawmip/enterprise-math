#!/usr/bin/env python3
"""Exact finite Gauss/Clausen boundary-forcing checks for D25 (author-side).

All arithmetic is integral modulo powers of p; no floats, no Sage,
no native H0/B0 or source-native executor implied.
"""
from math import isqrt


def primes_under(limit):
    sieve = bytearray(b'\x01') * limit
    sieve[:2] = b'\x00\x00'
    for d in range(2, isqrt(limit - 1) + 1):
        if sieve[d]:
            sieve[d * d:limit:d] = b'\x00' * len(range(d * d, limit, d))
    return [p for p in range(7, limit) if sieve[p]]


def check(p):
    assert p > 5 and p % 6 in (1, 5)
    mod3 = p ** 3
    mod4 = p ** 4
    b = a = 1
    for n in range(p - 1):
        b = (b * (6 * n + 1) * (3 * n + 1)
             * pow(36 * (n + 1) ** 2, -1, mod3)) % mod3
        a = (a * (2 * n + 1) * (3 * n + 1) * (3 * n + 2)
             * pow(36 * (n + 1) ** 3, -1, mod4)) % mod4
    assert b % (p * p) == 0, (p, 'B not divisible by p^2')
    assert a % (p ** 3) == 0, (p, 'A not divisible by p^3')
    unit_b = (pow(10, -1, p) if p % 6 == 1 else 1)
    assert b // (p * p) == unit_b, (p, 'B boundary factor')
    assert a // (p ** 3) == p - 1, (p, 'A boundary factor')
    # These are the *entire* nonzero coefficients of the truncated
    # Picard-Fuchs differential operators, at degree exactly X^p.
    gauss = (-(6 * p - 5) * (3 * p - 2)
             * pow(36, -1, mod3) * b) % mod3
    clausen = (-(2 * p - 1) * (3 * p - 2) * (3 * p - 1)
               * pow(36, -1, mod4) * a) % mod4
    expected_gauss = (-pow(36, -1, p) if p % 6 == 1
                      else -5 * pow(18, -1, p)) % p
    expected_clausen = -pow(18, -1, p) % p
    assert gauss % p ** 2 == 0 and gauss // p ** 2 == expected_gauss, (p, 'Gauss forcing')
    assert clausen % p ** 3 == 0 and clausen // p ** 3 == expected_clausen, (p, 'Clausen forcing')
    if p % 6 == 1:
        assert gauss % p ** 3 != 0
    return p, b, a, gauss, clausen, unit_b, expected_gauss, expected_clausen


def main():
    all_primes = primes_under(5000)
    results = [check(p) for p in all_primes]
    frozen = [r for r in results if r[0] % 24 in (13, 19)]
    assert len(frozen) == 166, len(frozen)
    print('all_primes_p>5_under_5000', len(results))
    print('frozen_target_p_mod24_in_13_19', len(frozen))
    print('universal_Gauss_boundary_and_cubic_boundary', 'PASS')
    for p in [7, 11, 13, 19, 37, 157, 373, 997]:
        if p < 5000:
            r = next(q for q in results if q[0] == p)
            print('witness',p, 'B_last/p2=',r[1]//(p*p),
                  'A_last/p3=',r[2]//p**3,
                  'Gauss_forcing/p2=',r[3]//(p*p),
                  'Clausen_forcing/p3=',r[4]//p**3)
    print('PASS_GH170_GH171_WILSON_BOUNDARY_FORCING_EXACT')


if __name__ == '__main__':
    main()
