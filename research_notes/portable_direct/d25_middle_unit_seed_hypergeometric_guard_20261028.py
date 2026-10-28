#!/usr/bin/env python3
"""D25 author-side exact certificate: one-seed middle/high transport for 216.
Runs scalar integer/modular arithmetic, not the native H0/B0 benchmark.
"""
from math import comb, factorial, isqrt


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def divide(a, b, p):
    assert b % p != 0
    return (a % p) * pow(b, -1, p) % p


def check(p):
    assert p > 3 and p % 6 == 1 and is_prime(p)
    m, modulus = (p - 1) // 6, p**3
    j0 = 2*m + 1
    seed = divide(-2 * factorial(4*m + 2),
                  factorial(2*m + 1)**5 * 216**(2*m + 1), p)
    assert seed != 0
    v, S, observed_high = 1, 0, 0
    for r in range(m):
        j, k = j0 + r, 4*m - r
        # Independent original factorial sources for each middle/high pair.
        tj = comb(2*j, j)**2 * comb(3*j, j) * pow(216, -j, p**2) % p**2
        tk = comb(2*k, k)**2 * comb(3*k, k) * pow(216, -k, modulus) % modulus
        assert tj % p == 0 and tk % p**2 == 0
        u = tj // p
        assert u * v % p == seed, (p, r, 'unit transport')
        R = divide(9*(66*r*r - 25*r + 3),
                   4*(1 - 3*r)**3*(3*r + 2)**3, p)
        ak = (66*k*k + 113*k + 49) * tk * pow(9*(k+1)**3, -1, modulus) % modulus
        observed = ak // p**2
        predicted = R * v * pow(seed, -1, p) % p
        assert observed == predicted, (p, r, observed, predicted)
        S = (S + R*v) % p
        observed_high = (observed_high + observed) % p
        if r < m-1:
            v = v * divide(4*(3*r+5)**3,
                           3*(6*r+7)*(r+1)*(3*r+4), p) % p
    assert observed_high == S * pow(seed, -1, p) % p

    # Independent original hypergeometric step recurrence and endpoint readout.
    t, W, J, lowmiddle = 1, 0, 0, 0
    for n in range(p):
        W = (W + (6*n + 1)*t) % modulus
        if n < p-1:
            a = ((66*n*n + 113*n + 49)*t
                 * pow(9*(n+1)**3, -1, modulus)) % modulus
            J = (J+a) % modulus
            if n <= 3*m:
                lowmiddle = (lowmiddle+a) % modulus
            t = (t * (2*n+1)*(3*n+1)*(3*n+2)
                 * pow(36*(n+1)**3, -1, modulus)) % modulus
    assert (W-J+4) % modulus == 0
    assert (J-lowmiddle-p**2*observed_high) % modulus == 0
    if p % 24 in (13, 19):
        assert W == p  # Instance regression only; not a universal proof.
    return (p, m, seed, S, observed_high, W)


if __name__ == '__main__':
    ps = [p for p in range(7, 1000) if p % 6 == 1 and is_prime(p)]
    results = [check(p) for p in ps]
    print('PASS_D25_ONE_SEED_HYPERGEOMETRIC_TRANSPORT',
          len(results), 'primes;', sum(a[1] for a in results), 'indexed pairs')
    for row in results:
        if row[0] in (13, 19, 37, 43, 61, 67, 211, 373):
            print('p,m,u0,S_m,H,W=', row)
