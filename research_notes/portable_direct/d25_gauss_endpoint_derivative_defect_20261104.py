#!/usr/bin/env python3
"""Exact integer p-adic check of the finite 1/8,3/8 Gauss endpoint defect.
No external dependencies. The general theorem uses the ODE proof, not this finite check.
"""
from math import isqrt


def primes_through(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for j in range(2, isqrt(n) + 1):
        if sieve[j]:
            sieve[j*j:n+1:j] = b'\x00' * ((n-j*j)//j+1)
    return [p for p in range(5, n+1) if sieve[p] and p % 8 in (5, 7)]


def gauss_observer(p):
    mod = p**3
    term = 1
    f = g = z_times_g_prime = 0
    for k in range(p):
        f = (f + term) % mod
        g = (g + (1 + 16*k)*term) % mod
        z_times_g_prime = (z_times_g_prime + k * (1 + 16*k)*term) % mod
        if k < p - 1:
            term = term * (8*k+1) * (8*k+3) * pow(576*(k+1)**2, -1, mod) % mod
    # z = 1/9; derivative converts theta into 9*theta.
    g_prime = 9*z_times_g_prime % mod
    defect = (g_prime - 9*pow(8, -1, mod)*g + 9*pow(32, -1, mod)*f) % mod
    expected = (-315 * pow(32, -1, mod) * p*p) % mod
    assert defect == expected, (p, defect, expected)
    assert defect % (p*p) == 0
    if p >= 11:
        assert defect % (p*p*p) != 0
    else:
        assert defect == 0
    # Consequences on the previously observed factor branches, including slopes.
    mod2 = p*p
    if p % 24 in (13, 23):
        assert f % mod2 == 0, (p, 'F-branch', f % mod2)
        assert g % p != 0
        assert (g_prime - 9*pow(8, -1, mod2)*g) % mod2 == 0
    elif p % 24 in (5, 7):
        assert g % mod2 == 0, (p, 'G-branch', g % mod2)
        assert f % p != 0
        assert (g_prime + 9*pow(32, -1, mod2)*f) % mod2 == 0
    else:
        raise AssertionError((p, p % 24))
    return f % p, g % p, (defect // (p*p)) % p


def main():
    primes = primes_through(2000)
    outcomes = {}
    for p in primes:
        f, g, d = gauss_observer(p)
        assert f != 0 or g != 0, (p, f, g)
        outcomes[p] = (f, g, d)
    print(f'PASS: {len(primes)} primes p <=2000 with p %8 in {{5,7}}; full original p-1 truncation; universal endpoint defect mod p^3; conditional p^2 slope locks')
    for p in [5, 7, 13, 23, 29, 37, 47, 373]:
        if p in outcomes:
            print(f'p={p}  (F mod p, G mod p, defect/p^2 mod p)={outcomes[p]}')

if __name__ == '__main__':
    main()
