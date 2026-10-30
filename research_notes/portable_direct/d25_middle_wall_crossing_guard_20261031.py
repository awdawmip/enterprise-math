#!/usr/bin/env python3
"""D25 author-side exact integer modular check.

Checks a new middle-strip wall-crossing of the Clausen prime-index mirror
and the resulting E.2-to-216 signed bridge decomposition. Does not execute
native H0/B0 benchmark, create Source claim or establish all-prime lift.
"""
from math import isqrt


def primes(limit):
    s = bytearray(b'\x01') * (limit + 1)
    s[0:2] = b'\x00\x00'
    for d in range(2, isqrt(limit) + 1):
        if s[d]:
            s[d*d:limit+1:d] = b'\x00' * ((limit-d*d)//d+1)
    return [p for p in range(7, limit + 1) if s[p] and p % 6 == 1]


def coefficients(p, power):
    modulus = p**power
    a = [1]
    for n in range(p - 1):
        num = (2*n + 1)*(3*n + 1)*(3*n + 2)
        den = 36*(n + 1)**3
        a.append(a[-1]*num*pow(den, -1, modulus) % modulus)
    return a


def e2_coefficients(p, power):
    modulus = p**power
    b = [1]
    m = (p-1)//3
    for n in range(m):
        b.append(-b[-1]*(3*n + 1)**3 * pow(27*(n+1)**3, -1, modulus) % modulus)
    return b


def check(p):
    modulus = p**3
    m = (p-1)//3
    h = (p-1)//2
    a = coefficients(p, 4)
    b = e2_coefficients(p, 3)
    # Literal prime-index products in the original coefficient ring.
    M = [None]
    for k in range(1, h+1):
        v = (-18*k**3*a[k]*a[p-k]) % p**4
        assert v % p**3 == 0, ('mirror valuation', p,k)
        mv = v//p**3
        M.append(mv)
        if k <= m:
            assert mv == 1, ('low mirror',p,k,mv)
        else:
            assert (2*mv+1) % p == 0, ('wall mirror',p,k,mv)
    # The only discontinuity of the prime-index ratio occurs at k=m+1.
    assert M[1] == 1
    assert M[m] == 1
    assert M[m+1]*pow(M[m], -1, p) % p == (-pow(2,-1,p)) % p
    for k in range(2,m+1):
        assert M[k] == M[k-1]
    for k in range(m+2,h+1):
        assert M[k] == M[k-1]
    # Original weighted, source-separated strips of A-B.
    c0 = sum((6*n+1)*(a[n] - b[n]) for n in range(m+1)) % modulus
    c1 = sum((6*n+1)*a[n] for n in range(m+1,h+1)) % modulus
    c2 = sum((6*n+1)*a[n] for n in range(h+1,2*m+1)) % modulus
    assert c1 % p == 0
    assert c2 % p**2 == 0
    # NEW inverse-moment formula uses only middle first-valuation a[k]/p.
    inv_moment = 0
    for k in range(m+1,h+1):
        assert a[k] % p == 0
        t = (a[k] // p) % p
        assert t != 0
        inv_moment += (1-6*k)*pow(36*k**3*t,-1,p)
    inv_moment %= p
    assert c2//p**2 == inv_moment, ('inverse-moment',p,c2//p**2,inv_moment)
    full_a = sum((6*n+1)*a[n] for n in range(p)) % modulus
    full_b = sum((6*n+1)*b[n] for n in range(m+1)) % modulus
    assert (c0+c1+c2) % modulus == (full_a-full_b) % modulus
    assert c0 % p == 0
    assert (c0+c1) % p**2 == 0, ('first-digit bridge',p)
    e = ((c0+c1) % modulus)//p**2
    assert (e+inv_moment) % p == 0, ('second-digit bridge',p,e,inv_moment)
    assert full_a == p and full_b == p, ('original external target',p,full_a,full_b)
    return {'p':p, 'm':m,'h':h,'carry':e,'inverse_moment':inv_moment,
            'low':c0,'mid':c1,'second_strip':c2,
            'low_mod_p2':(c0//p)%p,'mid_mod_p2':(c1//p)%p}


def main():
    pp = primes(5000)
    target = 0
    nonzero_inverse = 0
    nonzero_carry = 0
    for p in pp:
        r = check(p)
        if p % 24 in (13, 19):
            target += 1
            nonzero_inverse += int(r['inverse_moment'] != 0)
            nonzero_carry += int(r['carry'] != 0)
        if p in (7,13,19,37,67,157,373):
            print('ANCHOR',r)
    print('PASS_D25_CLAUSEN_WALL_E2_BRIDGE',
          'p_mod6_1',len(pp),'frozen',target,
          'frozen_nonzero_inverse',nonzero_inverse,
          'frozen_nonzero_carry',nonzero_carry)


if __name__ == '__main__':
    main()
