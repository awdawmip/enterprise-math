#!/usr/bin/env python3
"""Universal first Frobenius-defect (mod p**2) for the D25 integer carrier.

Author-side exact arithmetic. Not a native H0/B0 benchmark or a canonical
Source CLAIM, accepted result, independent check, or proof of N | U_l.
"""
from functools import lru_cache
from math import comb


def choose(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


@lru_cache(maxsize=None)
def defect_coefficients(p, a):
    """Coeffs of (1+x)^a * ((1+x)^p-1-x^p)/p, exactly in Z."""
    assert 0 <= a < p and p >= 5
    return tuple(sum((choose(p, s) // p) * choose(a, t-s)
                     for s in range(1, p)) for t in range(p+a))


def digit_ports(p, n, k):
    """(L, E): binom(n,k) == L + p E (mod p**2)."""
    a, b = n % p, n // p
    c, d = k % p, k // p
    L = choose(a, c) * choose(b, d)
    if b == 0:
        return L, 0
    T = defect_coefficients(p, a)
    # Two distinct output locations: in-digit and carry-to-next-digit.
    E = b * (T[c] * choose(b-1, d) +
             (T[c+p] if c+p < len(T) else 0) * choose(b-1, d-1))
    return L, E


def integer_carrier_split(l, p):
    """Exact U_l plus source-separated order-zero and first-defect ports."""
    u0 = 0
    u1 = [0, 0, 0]  # original source order 3*l, 2*l, 4*l
    direct = 0
    for k in range(2*l+1):
        le = [digit_ports(p, s*l, k) for s in (3, 2, 4)]
        L = [v[0] for v in le]
        E = [v[1] for v in le]
        weight = (6*k+1)*(-1)**k*2**(2*l-k)
        u0 += weight*L[0]*L[1]*L[2]
        for a in range(3):
            other = 1
            for b in range(3):
                if a != b:
                    other *= L[b]
            u1[a] += weight*E[a]*other
        direct += weight*choose(3*l, k)*choose(2*l, k)*choose(4*l, k)
    assert (u0+p*sum(u1)-direct)%(p*p) == 0, (l,p)
    return u0%(p*p), [v%p for v in u1], direct%(p*p)


def run():
    coefficient_checks = 0
    for p in (5,7,11,13,17,19):
        for n in range(4*p+4):
            for k in range(n+1):
                L,E = digit_ports(p,n,k)
                assert (L+p*E-choose(n,k))%(p*p) == 0, (p,n,k)
                coefficient_checks += 1
    # All square-divisor probes use the exact solution 6*l+1=0 mod p**2.
    square_primes = (5,7,11,13,17,19,23,29,31,37)
    for p in square_primes:
        l = (-pow(6, -1, p*p)) % (p*p)
        u0, u1, direct = integer_carrier_split(l,p)
        assert direct == 0, (p,l,direct)
        assert (u0+p*sum(u1))%(p*p) == 0
        print('SQUARE_DIVISOR p l N U0_mod_p2 E3_Em_E4_mod_p U_mod_p2',
              p, l, 6*l+1, u0, *u1, direct)
    # Unlike square divisors, a single prime divisor does NOT imply p^2 | U.
    for l,p,nonzero in ((2,13,143),(3,19,171)):
        u0,u1,direct=integer_carrier_split(l,p)
        assert direct == nonzero and sum(u1)%p == 0
        print('SINGLE_DIVISOR p l U_mod_p2',p,l,direct)
    # Same p^2 divisor, different higher digits; not an isolated low-digit test.
    for l in (29,54):
        u0,u1,direct=integer_carrier_split(l,5)
        assert direct==0
        print('HIGHER_DIGITS p l U0_mod_p2 E_sum_mod_p U_mod_p2',5,l,u0,sum(u1)%5,direct)
    # Genuine missing carry: p=5,l=4 has U0=20, E4=1, and 20+5=0 (mod25).
    a,b,c=integer_carrier_split(4,5)
    assert a==20 and b==[0,0,1] and c==0
    print('PASS_D25_LUCAS_P2_FROBENIUS_CARRY_IDENTITY')
    print('COEFFICIENT_CHECKS',coefficient_checks,
          'SQUARE_DIVISOR_PRIMES',len(square_primes))


if __name__=='__main__':
    run()
