#!/usr/bin/env python3
"""Exact p-adic coefficients for the original 216 Ramanujan series.

Self-contained executable: python3 d25_all_prime_reciprocal_tail_check.py
No floating-point arithmetic and no external dependencies.
This is finite regression evidence, not an infinite-prime proof.
"""
from math import comb


def primes_below(limit: int):
    sieve = bytearray(b'\x01') * limit
    sieve[:2] = b'\x00\x00'
    for d in range(2, int(limit**0.5) + 1):
        if sieve[d]:
            sieve[d*d:limit:d] = b'\x00' * len(sieve[d*d:limit:d])
    return [p for p in range(5, limit) if sieve[p]]


def coefficients(p: int):
    mod = p**4
    a = [1]
    for n in range(1, p):
        num = (2*n-1)*(3*n-2)*(3*n-1)
        den = 36*n*n*n
        a.append((a[-1] * num * pow(den, -1, mod)) % mod)
    return a


def check_prime(p: int, *, anchors=False):
    mod = p**4
    a = coefficients(p)
    h = (p-1)//3
    q = (2*p)//3
    N = q + 1
    assert N == p-h
    assert all(a[n] % p**3 == 0 for n in range(N,p)), (p,'valuation')
    tau = [0]*p
    for n in range(N,p):
        tau[n] = a[n]//(p**3)
    assert tau[-1] % p == p-1, (p,'terminal',tau[-1])
    inv18 = pow(18,-1,p)
    signed_tail_mirror = 0
    actual_signed_tail = 0
    for k in range(1,h+1):
        ak = a[k] % p
        assert ak and k % p, (p,'low units',k)
        want = (-inv18 * pow(k,-3,p) * pow(ak,-1,p)) % p
        actual = tau[p-k] % p
        assert actual == want, (p,'mirror',k,actual,want)
        signed_tail_mirror = (signed_tail_mirror + (6*k-1)*pow(k,-3,p)*pow(ak,-1,p)*inv18) % p
        actual_signed_tail = (actual_signed_tail + (6*(p-k)+1)*actual) % p
    assert actual_signed_tail == signed_tail_mirror, (p,'signed tail',actual_signed_tail,signed_tail_mirror)

    # L=theta^3-X/2(theta+1/2)(theta+1/3)(theta+2/3), modulo p.
    # Truncated tail gives one start boundary plus a terminal X^p boundary.
    u = tau[N] % p
    for n in range(0,p+1):
        a_n = tau[n] if n<p else 0
        a_prev = tau[n-1] if 1<=n<=p else 0
        coef = (n**3*a_n - (2*n-1)*(3*n-2)*(3*n-1)*pow(36,-1,p)*a_prev) % p
        expected = (N**3*u) % p if n==N else (-inv18)%p if n==p else 0
        assert coef == expected, (p,'differential',n,coef,expected)

    # Weighted terminal coefficient is always 5 mod p, including the exceptional p=5 (zero).
    assert ((6*(p-1)+1)*tau[p-1])%p == 5%p
    # Coefficientwise full weighted-prefix congruence mod p^4, and its scalar at X=1.
    full = sum((6*n+1)*a[n] for n in range(p)) % mod
    prefix = sum((6*n+1)*a[n] for n in range(q+1)) % mod
    assert (full-prefix) % mod == p**3*signed_tail_mirror % mod
    if anchors:
        for n in range(p):
            # Independent factorial/binomial origin, with modular denominator.
            original = comb(2*n,n)**2 * comb(3*n,n)*pow(216,-n,mod) % mod
            assert a[n] == original, (p,'binomial',n)
    return h, signed_tail_mirror, u


def main():
    primes = primes_below(4000)
    anchors = {5,7,11,13,17,19,23,31,37,73,157,373}
    total_indices = 0
    p5_count = 0
    for p in primes:
        h, tail, u = check_prime(p, anchors=p in anchors)
        total_indices += h
        if p%6==5:
            p5_count += 1
        if p in {5,7,11,13,19,373}:
            print('anchor',p,'k_count',h,'signed_tail_mod_p',tail,'start_boundary',u)
    print('primes_checked',len(primes),'p_mod_6_eq_5',p5_count,'mirror_indices',total_indices,'independent_binomial_anchors',len(anchors))
    print('PASS_D25_ALL_PRIME_RECIPROCAL_P3_TAIL_TWO_BOUNDARY_EXACT')


if __name__ == '__main__':
    main()
