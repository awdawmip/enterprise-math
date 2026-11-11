#!/usr/bin/env python3
"""Exact p-adic original W216 signed-observer coordinate-shift check.
Frozen mathematical series; no native H0/B0 data or Source Result.
"""
from math import isqrt

def isprime(n):
    if n < 2: return False
    return all(n % d for d in range(2, isqrt(n) + 1))

def original_signed(p, c=0):
    """S_p(1/2 + p^2*c) modulo p^3, and S'_p(1/2) modulo p.

    a_k = (2k)!(3k)! / (216^k (k!)^5).
    For k<p-1 use a_{k+1}/a_k =
    (2k+1)(3k+1)(3k+2)/(36(k+1)^3), whose denominator is a p-unit.
    Since 2*x = 1+2*p^2*c, evaluating S_p(x) uses a_k*(2x)^k.
    """
    assert isprime(p) and p >= 5 and p % 24 in (13, 19)
    modulus = p**3
    a = 1
    total = 0
    derivative = 0
    z = (1 + 2*p*p*c) % modulus
    zpow = 1
    for k in range(p):
        total = (total + (6*k+1)*a*zpow) % modulus
        derivative = (derivative + 2*k*(6*k+1)*a) % p
        zpow = zpow*z % modulus
        if k < p-1:
            num = (2*k+1)*(3*k+1)*(3*k+2)
            den = 36*(k+1)**3
            a = (a*num*pow(den,-1,modulus)) % modulus
    return total,derivative

def check():
    cases = [13,19,37,43,109,139,157,373]
    for p in cases:
        x0,s = original_signed(p)
        assert x0 % p**2 == p and s != 0
        r0 = ((x0-p)//p**2) % p
        assert r0 == 0
        for c in (1,2,p-1,pow(s,-1,p)):
            shifted,ds = original_signed(p,c)
            assert ds == s
            assert (shifted-x0-p*p*c*s) % p**3 == 0
            assert ((shifted-p)//p**2) % p == (r0+c*s)%p
        print("p=%d slope=%d r0=%d r1=%d c_for_residue_1=%d" %
              (p,s,r0,s,pow(s,-1,p)))
    p=373
    assert original_signed(p,0)[0] == 373
    assert original_signed(p,1)[0] == 29356592
    assert original_signed(p,99)[0] == 139502
    assert original_signed(p,372)[0] == 22539271
    print("PASS: all direct original-series checks, p373 exact witnesses")

if __name__ == "__main__":
    check()
