#!/usr/bin/env python3
"""Independent finite-ring and exact-rational checks of the D25 Cartier boundary identity.

No symbolic hypotheses, float arithmetic, remote service, or native experiments are used.
"""
from fractions import Fraction
from math import comb, isqrt


def primes(limit):
    for p in range(7, limit):
        if p % 6 == 1 and all(p % d for d in range(2, isqrt(p) + 1)):
            yield p


def check_p(p):
    assert p > 3 and p % 6 == 1
    m = (p - 1) // 6
    mod = p * p
    c = [0] * (4 * m + 1)
    c[1] = pow(10, -1, mod)
    for r in range(1, 4 * m):
        den = (6 * r + 5) * (3 * r + 2)
        assert den % p != 0
        c[r + 1] = (c[r] * 36 * r * r * pow(den, -1, mod)) % mod
    w = [comb(m, i) * comb(2 * m, i) * pow(2, -i, mod) % mod
         for i in range(m + 1)]
    sigma = [comb(3 * m, j) * pow(-2, j, mod) % mod
             for j in range(3 * m + 1)]
    kappa = 36 * (4 * m) ** 2 * c[4 * m] % mod
    numerator = (kappa * w[m] - pow(-2, 3 * m, mod)) % mod
    assert numerator % p == 0, ('boundary-unit', p, numerator)
    correction = volume = 0
    for i in range(m + 1):
        for r in range(1, 4 * m + 1):
            j = 3 * m + 1 + i - r
            if 0 <= j <= 3 * m:
                u = w[i] * c[r] * sigma[j] % mod
                correction = (correction + (18 * i + 9 * r + 2) * u) % mod
                volume = (volume + u) % mod
    # Exact rational identity implies two p-adic checks.
    assert (numerator + p * correction - p * p * volume) % mod == 0
    digit = (numerator // p) % p
    assert digit == (-correction) % p, ('divided-boundary', p)
    return p, m, digit, volume % p


def check_exact(m):
    p = 6 * m + 1
    c = [Fraction(0)] * (4 * m + 1)
    c[1] = Fraction(1, 10)
    for r in range(1, 4 * m):
        c[r + 1] = c[r] * Fraction(36 * r * r, (6 * r + 5) * (3 * r + 2))
    w = [Fraction(comb(m, i) * comb(2 * m, i), 2**i) for i in range(m + 1)]
    kappa = 36 * (4 * m)**2 * c[4 * m]
    v = a = Fraction(0)
    for i in range(m + 1):
        for r in range(1, 4 * m + 1):
            j = 3 * m + 1 + i - r
            if 0 <= j <= 3 * m:
                term = w[i] * c[r] * comb(3 * m, j) * (-2)**j
                v += term
                a += (18 * i + 9 * r + 2) * term
    assert kappa * w[m] - (-2)**(3 * m) == -p * a + p*p*v
    return m


def check_adjoint(p):
    m = (p - 1) // 6
    sigma = {3*m+j: comb(3*m, j) * (-2)**j % p for j in range(3*m+1)}
    # L^*t^k = (6k+1)(3k+1)t^k - 36(k+1)^2 t^(k+1).
    for n in (-3, -1, 0, 1, 4):
        lhs = {}
        rhs = {}
        for k, v in sigma.items():
            h = k + n
            lhs[h] = (lhs.get(h, 0) + v * (6*h+1)*(3*h+1)) % p
            lhs[h+1] = (lhs.get(h+1, 0) - 36 * (h+1)**2 * v) % p
            rhs[h] = (rhs.get(h, 0) + v * (6*n-1)*(3*n-1)) % p
            rhs[h+1] = (rhs.get(h+1, 0) - 36 * n*n * v) % p
        assert all(lhs.get(k, 0) == rhs.get(k, 0) for k in set(lhs)|set(rhs)), (p, n)
    return p


if __name__ == '__main__':
    for m in (1, 2, 3, 4, 7):
        assert check_exact(m) == m
    checked = list(primes(1000))
    for p in checked:
        check_p(p)
        check_adjoint(p)
    for p in (13, 19, 43, 67, 373, 997):
        print('sample p,m,divided_boundary,volume:', check_p(p))
    print('PASS', len(checked), 'primes p<1000, universal rational m={1,2,3,4,7}, and adjoint monomial tests')
