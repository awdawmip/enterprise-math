#!/usr/bin/env python3
"""Exact p-adic mirror fold for W216 modulo p**3, no floating point.

Author-side research checker; this is not a native H0/B0 experiment.
"""
from math import factorial

PRIMES = (5, 7, 11, 13, 19, 37, 43, 109, 139, 157, 373)

def is_prime(n):
    if n < 2: return False
    return all(n % d for d in range(2, int(n ** 0.5) + 1))

def coefficients(p):
    """a_k=(2k)!(3k)!/(216**k*(k!)**5) in Z_p/(p^3), 0<=k<p."""
    modulus = p ** 3
    terms = [1]
    for k in range(p - 1):
        ratio_num = (2*k + 1) * (3*k + 1) * (3*k + 2)
        ratio_den = 36 * (k + 1) ** 3
        terms.append(terms[-1] * ratio_num * pow(ratio_den, -1, modulus) % modulus)
    return terms

def factorial_units(p):
    """Independent factorial formula for a_k/p**valuation mod p."""
    fact = [1]
    for k in range(1, p): fact.append(fact[-1]*k % p)
    def block_unit(n):
        q, r = divmod(n, p)
        assert q <= 2
        return (-1)**q * factorial(q) * fact[r] % p
    inv216 = pow(216, -1, p)
    out = []
    for k in range(p):
        v = 2*k//p + 3*k//p
        u = block_unit(2*k) * block_unit(3*k) * pow(inv216, k, p)
        u = u * pow(fact[k], -5, p) % p
        out.append((v, u))
    return out

def verify(p):
    assert p > 3 and is_prime(p)
    mod = p**3
    a = coefficients(p)
    b = factorial_units(p)
    I0 = [k for k in range(p) if 3*k < p]
    I1 = [k for k in range(p) if p < 3*k and 2*k < p]
    I2 = [k for k in range(p) if p < 2*k and 3*k < 2*p]
    I3 = [k for k in range(p) if 2*p < 3*k]
    assert sorted(I0+I1+I2+I3) == list(range(p))
    for k in range(p):
        v, unit = b[k]
        assert a[k] % p**v == 0
        if v < 3: assert a[k] // p**v % p == unit
    for k in range(1, p):
        alpha, beta = 2*k//p, 3*k//p
        v,u = b[k]
        v2,u2 = b[p-k]
        assert v+v2 == 3
        expected = (-1)**(1+alpha+beta) * factorial(beta)*factorial(2-beta)
        expected = expected * pow(36*k**3, -1, p) % p
        assert u*u2 % p == expected, (p,k,u,u2,expected)
    full = sum((6*k+1)*a[k] for k in range(p)) % mod
    short = sum((6*k+1)*a[k] for k in I0+I1) % mod
    tail = sum((6*k+1)*(a[k]//(p*p)) for k in I2) % p
    reflected = sum((1-6*k)*pow(36*k**3*(a[k]//p % p), -1, p)
                    for k in I1) % p
    half = (short + p*p*reflected) % mod
    assert tail == reflected
    assert half == full
    return p, len(I0), len(I1), len(I2), len(I3), tail, full, short

if __name__ == '__main__':
    for p in PRIMES:
        print('p=%d layers=%d/%d/%d/%d reflected_tail=%d W_mod_p3=%d half_raw=%d' % verify(p))
    print('ALL CHECKS PASSED')
