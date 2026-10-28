#!/usr/bin/env python3
"""Exact dual 3F2 kernel and first nonintegral boundary of D25 high tail.
Scalar arithmetic only; not native H0/B0 or all-prime LIFT proof.
"""
from fractions import Fraction
from math import isqrt


def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p)+1))


def rise(a,r):
    z=Fraction(1)
    for j in range(r): z*=a+j
    return z


def exact_case(r):
    R=Fraction(9*(66*r*r-25*r+3), 4*(1-3*r)**3*(3*r+2)**3)
    V=2**r*rise(Fraction(5,3),r)**3/(rise(Fraction(7,6),r)*rise(Fraction(1),r)*rise(Fraction(4,3),r))
    h=2**r*rise(Fraction(-1,3),r)**3/(rise(Fraction(7,6),r)*rise(Fraction(4,3),r)*rise(Fraction(1),r))
    assert R*V==Fraction(9,32)*(66*r*r-25*r+3)*h


def modfrac(a,b,p):
    assert b%p
    return (a%p)*pow(b,-1,p)%p


def check_prime(p):
    assert p%6==1 and p>3 and prime(p)
    m=(p-1)//6
    v,h=1,1
    s_direct=s_dual=0
    for r in range(m):
        R=modfrac(9*(66*r*r-25*r+3),4*(1-3*r)**3*(3*r+2)**3,p)
        poly=(66*r*r-25*r+3)%p
        s_direct=(s_direct+R*v)%p
        s_dual=(s_dual+modfrac(9,32,p)*poly*h)%p
        assert R*v%p==modfrac(9,32,p)*poly*h%p,(p,r)
        if r<m-1:
            v=v*modfrac(4*(3*r+5)**3,3*(6*r+7)*(r+1)*(3*r+4),p)%p
            h=h*modfrac(4*(3*r-1)**3,3*(6*r+7)*(r+1)*(3*r+4),p)%p
            assert h!=0
    assert s_direct==s_dual
    # At r=m-1 the NEXT dual hypergeometric coefficient has exact p-valuation -1.
    r=m-1
    numerator=4*(3*r-1)**3
    denominator=3*(6*r+7)*(r+1)*(3*r+4)
    assert denominator%p==0 and (denominator//p)%p != 0
    assert numerator%p!=0 and h%p!=0
    # The weight polynomial at the first excluded r=m is a p-unit (9 mod p).
    assert (66*m*m-25*m+3)%p==9%p
    return p,m,s_dual

if __name__=='__main__':
    for r in range(0,15): exact_case(r)
    ps=[p for p in range(7,1000) if p%6==1 and prime(p)]
    rows=[check_prime(p) for p in ps]
    print('PASS_D25_DUAL_3F2_NATURAL_CUTOFF',len(rows),'primes;',sum(m for _,m,_ in rows),'indexed terms; 15 exact Q cases')
    print('p373 (p,m,S_m):',next(a for a in rows if a[0]==373))
