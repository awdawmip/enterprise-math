#!/usr/bin/env python3
"""Exact integer-mod-p certificate for the p=13 (mod 24) Gauss complement
and the original V Clausen Gauss derivative observer. No native H0/B0 claim.
"""
from math import comb


def primes_below(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for d in range(2, int(limit ** 0.5) + 1):
        if sieve[d]:
            sieve[d * d:limit + 1:d] = b'\x00' * ((limit - d * d) // d + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def binomial_poly(n, m, p, inv):
    assert 0 <= n <= m < p
    c = [1]
    for k in range(1, n + 1):
        c.append(c[-1] * (n - k + 1) * (m - k + 1) * inv[k] ** 2 % p)
    return c


def evaluate_and_derivative(coeff, z, p):
    y = dy = 0
    for c in reversed(coeff):
        dy = (dy * z + y) % p
        y = (y * z + c) % p
    return y, dy


def original_MN(p, z, inv):
    # (1/8)_k (3/8)_k (1/9)^k / (k!)^2.
    term = 1
    M = 1
    N = 0
    i576 = pow(576, -1, p)
    for k in range(1, p):
        term = term * (8*k-7) * (8*k-5) * i576 * inv[k] ** 2 % p
        M = (M + term) % p
        N = (N + k * term) % p
    return M, N


def check_prime(p, coefficientwise=False):
    assert p > 5 and p % 24 == 13
    a = (5*p-1)//8
    b = (7*p-3)//8
    h = (p+1)//2
    u = (p-5)//8
    v = 3*u + 1
    assert b == p - 1 - u and a == p - 1 - v
    assert h == a+b-p+1
    inv = [0] * p
    inv[1] = 1
    for j in range(2, p):
        inv[j] = -(p//j) * inv[p%j] % p
    z = pow(9, -1, p)
    P = binomial_poly(a,b,p,inv)
    Q = binomial_poly(u,v,p,inv)
    Pval,Pder = evaluate_and_derivative(P,z,p)
    Qval,Qder = evaluate_and_derivative(Q,z,p)
    factor = pow((1-z)%p,h,p)
    assert factor == -8*z%p
    assert Pval == factor*Qval%p
    assert Pder == (-h * pow((1-z)%p,h-1,p)*Qval + factor * Qder)%p
    M,N = original_MN(p,z,inv)
    assert M == Pval and N == z*Pder%p
    H = (M+16*N)%p
    short_H = (-128 * pow(81,-1,p)*Qder)%p
    assert H == short_H, (p,H,short_H)
    if coefficientwise:
        # Test polynomial equality P=(1-z)^h Q in the entire F_p[z].
        fac = [(-1)**j * comb(h,j)%p for j in range(h+1)]
        result = [0]*(a+1)
        for i,c in enumerate(Q):
            for j,f in enumerate(fac):
                result[i+j] = (result[i+j]+c*f)%p
        assert result == P
    return dict(p=p,u=u,v=v,h=h,Q_mod_p=Qval,Qprime_mod_p=Qder,
                M_mod_p=M, H_mod_p=H, Pprime_mod_p=Pder,
                coeff_checked=coefficientwise)


if __name__ == '__main__':
    rows=[check_prime(p,coefficientwise=(p<=181)) for p in primes_below(10000) if p%24==13]
    assert len(rows)==157
    print('ALL_PASS',len(rows),'coefficient checks',sum(x['coeff_checked'] for x in rows),
          'Q_zero_checks',sum(x['Q_mod_p']==0 for x in rows),
          'Qprime_nonzero_checks',sum(x['Qprime_mod_p']!=0 for x in rows))
    for p in [13,37,61,109,157,181,373,9973]:
        print(next(x for x in rows if x['p']==p))
