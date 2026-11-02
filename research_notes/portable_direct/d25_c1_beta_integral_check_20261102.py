#!/usr/bin/env python3
"""Exact Fraction and independent polynomial-division check of C1-BETA."""
from fractions import Fraction
from math import comb
import json

def divide_by_one_plus_t(a):
    q=[0]*(len(a)-1)
    q[-1]=a[-1]
    for i in range(len(q)-2,-1,-1):q[i]=a[i+1]-q[i+1]
    assert a[0]==q[0]
    return q

def integrate_pair(n,m):
    a=[(-1)**k*comb(n,k) for k in range(n+1)]
    for k in range(n-m+1): a[m+k]-=(-2)**m*(-1)**k*comb(n-m,k)
    while a and a[-1]==0:a.pop()
    if not a: return Fraction(0)
    return Fraction(1,2)*sum(Fraction(c,i+1) for i,c in enumerate(divide_by_one_plus_t(a)))

def check(r):
    n=3*r
    v=lambda s:Fraction((-1)**(s+1)*2**s,4*s*comb(n,s))
    T=lambda m:Fraction((-1)**m*comb(3*r,m)*comb(2*r,m)*comb(4*r,m),2**m)
    V=Fraction(0); total=Fraction(0); via_integral=Fraction(0)
    for m in range(2*r+1):
        if m:V+=v(m)
        observed=integrate_pair(n,m)
        assert observed==V,(r,m)
        total+=(6*m+1)*T(m)*V
        via_integral+=(6*m+1)*T(m)*observed
    assert total==via_integral
    return {'r':r,'m_checked':2*r+1,'Hbin':str(total)}

if __name__=='__main__':
    print(json.dumps({'schema':'D25_C1_BETA_RATIONAL_CHECK_V1',
        'status':'EXACT_FINITE_CHECK_NOT_UNIVERSAL_CHARACTER_PROOF',
        'checks':[check(r) for r in (1,2,3,4,6,8)]},indent=2))
