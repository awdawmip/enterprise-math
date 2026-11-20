#!/usr/bin/env python3
"""Exact finite regression for scoped two-prime X6 actual short-ball baseline.
Auxiliary independent full projective dual lines, not geometrically conditioned
good seed sets. No network. Theorem for pairwise modular rank supports large case.
"""
from fractions import Fraction
from math import gcd, isqrt
from functools import reduce
from itertools import combinations, product
import json

CASES = ((100019, 100049), (500029, 500041), (1000037, 1000039))

def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))

def qmax_exact(p, q):
    n = p*q
    k = n.bit_length()-1
    # B^12 42^12 k^9 <= N^4 exactly iff B <= R^2 for gamma=3/8.
    b = 0
    while (b+1)**12 * 42**12 * k**9 <= n**4:
        b += 1
    return b,k

def witnesses(b):
    size=isqrt(b)
    out=[]
    for v in product(range(-size,size+1), repeat=6):
        Q=sum(x*x for x in v)
        if not 0 < Q <= b: continue
        if reduce(gcd, (abs(x) for x in v), 0) != 1: continue
        if next(x for x in v if x) < 0: continue
        out.append(v)
    return out

def independent(v,w,p):
    return any((v[i]*w[j]-v[j]*w[i]) % p
               for i in range(6) for j in range(i+1,6))

def compute(p,q):
    assert prime(p) and prime(q) and p != q
    assert p%7 in (3,5) and q%7 in (3,5)
    b,k=qmax_exact(p,q)
    assert 2*b < min(p,q)
    W=witnesses(b)
    t=len(W)
    a=lambda r:Fraction(r**5-1,r**6-1)
    d=lambda r:Fraction(r**4-1,r**6-1)
    mu=t*a(p)*a(q)
    S2=t*(t-1)//2*d(p)*d(q)
    checked=0
    if t<=2100:
        for v,w in combinations(W,2):
            assert independent(v,w,p) and independent(v,w,q)
            checked += 1
        assert checked==t*(t-1)//2
    ratio=S2/mu if mu else Fraction(0)
    return dict(p=p,q=q,k=k,B=b,t=t,pair_checks=checked,
                mu=[mu.numerator,mu.denominator],
                S2=[S2.numerator,S2.denominator],
                S2_over_mu=[ratio.numerator,ratio.denominator],
                decimal_correction=float(ratio))

if __name__ == '__main__':
    print(json.dumps({'model':'FULL_PROJECTIVE_UNCONDITIONED_FIRST_LEVEL',
                      'cases':[compute(p,q) for p,q in CASES]},indent=2))
