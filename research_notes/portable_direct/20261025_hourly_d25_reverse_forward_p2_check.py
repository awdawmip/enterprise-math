#!/usr/bin/env python3
"""Exact mod-p² author check of D25 original source-band reciprocal lift.

No native CM/Frobenius experiment is performed.
"""
from math import isqrt


def primes_1mod6(limit):
    for p in range(7, limit):
        if p % 6 == 1 and all(p % d for d in range(2, isqrt(p) + 1)):
            yield p


def certify(p):
    assert p >= 7 and p % 6 == 1
    m, mod = (p - 1) // 6, p*p
    fac = [1]*p
    for i in range(1, p):
        fac[i] = fac[i-1]*i % mod
    invfac = [1]*p
    invfac[-1] = pow(fac[-1], -1, mod)
    for i in range(p-1, 0, -1):
        invfac[i-1] = invfac[i]*i % mod

    prefactor = fac[2*m]*fac[3*m]*fac[4*m] % mod
    prefactor = prefactor * (-1 if m%2 else 1) * pow(9, -1, mod) % mod

    def d(n):
        assert 4*m < n <= 6*m
        return (prefactor*(6*n+1)*fac[n-1-2*m]*fac[n-1-3*m]*fac[n-1-4*m]
                *invfac[n]**3 * pow(2, -n, mod)) % mod

    def inv(x):
        return pow(x % mod, -1, mod)

    d0 = d(p-1)
    assert d0 % p == 5
    A = 1
    H = 0
    exceptional = None
    for k in range(2*m):
        actual = d(p-1-k)*A % mod
        phi = 2*(6*k+5)*inv((2*k+1)*(3*k+1)*(3*k+2)) % mod
        prediction = phi*d0*inv(5)*(1+p*H) % mod
        assert actual == prediction, (p,k,actual,prediction)
        if k == m:
            exceptional = actual
            special = 16*d0*inv(5)*(1+p*(H-19*inv(12))) % mod
            assert actual == special, (p,"exceptional p²")
            assert actual%p == 16%p
        if k+1 < 2*m:
            j = k
            E = (6*inv(6*j+5)-6*inv(6*j+11)-3*inv(j+1)
                 +2*inv(3*j+5)+inv(2*j+3)+inv(3*j+4)) % mod
            H = (H+E) % mod
            A = A*(2*k+1)*(3*k+1)*(3*k+2)*inv(36*(k+1)**3) % mod
    return d0, exceptional


def main():
    cases = list(primes_1mod6(1000)) + [1327,19963]
    for p in cases:
        endpoint, exceptional = certify(p)
        if p in (7,13,19,373,1327,19963):
            print(f"p={p}: d_(p-1)={endpoint}, d_(5m)*A_m={exceptional} mod {p*p}")
    print(f"PASS: {len(cases)} primes, each complete 2m coefficient interval at precision p²")


if __name__ == '__main__':
    main()
