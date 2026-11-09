#!/usr/bin/env python3
"""Exact author-side falsification checks for the W216 finite p^4 terminal boundary.

Independent coefficient tracks: modular Pochhammer-ratio recurrence and integer
binomial expression. This is not the original-class H0/B0 native benchmark.
"""
from math import comb

PRIMES = (5, 7, 11, 13, 17, 19, 23, 37, 43, 73, 373)


def check(p):
    mod = p**4
    half, third, two_thirds = pow(2, -1, mod), pow(3, -1, mod), 2*pow(3, -1, mod)
    shifts = (half, third, two_thirds)

    # This sequence is c_k=(1/2)_k (1/3)_k (2/3)_k/(k!)^3.
    c = [1]
    for k in range(p - 1):
        num = (2*k + 1)*(3*k + 1)*(3*k + 2)
        den = 18*(k + 1)**3
        c.append(c[-1]*num*pow(den, -1, mod) % mod)

    assert c[-1] % mod == (-p**3) % mod
    independent = comb(2*p - 2, p - 1)**2*comb(3*p - 3, p - 1)
    independent = independent*pow(108, -(p - 1), mod) % mod
    assert independent == c[-1]

    # Full coefficientwise Picard-Fuchs finite operator through z^p.
    residual = []
    for n in range(p+1):
        term = (n**3*c[n] if n < p else 0)
        if 1 <= n <= p:
            prod = 1
            for shift in shifts:
                prod = prod*(n-1+shift) % mod
            term -= c[n-1]*prod
        residual.append(term % mod)
    assert all(x == 0 for x in residual[:p])
    force = (-p**3*pow(9, -1, mod)) % mod
    assert residual[p] == force
    ev = force*pow(2, -p, mod) % mod
    assert ev == (-p**3*pow(18, -1, mod)) % mod
    return p, c[-1]//p**3, residual[p]//p**3, ev//p**3


if __name__ == "__main__":
    for row in map(check, PRIMES):
        print(*row)
    print(f"PASS ({len(PRIMES)} primes; exact mod p^4; all coefficients 0..p)")
