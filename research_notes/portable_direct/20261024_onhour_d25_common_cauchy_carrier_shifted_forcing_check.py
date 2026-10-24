#!/usr/bin/env python3
"""Exact D25 author-side verification of the rational LOW/HIGH Cauchy carrier.
This is NOT a native benchmark, formal Result or independent review.
"""
from fractions import Fraction as F
from math import comb, factorial

def Q(m, z):
    q = F(factorial(m))
    for j in range(m + 1):
        q /= z + j
    return q

def H(m, order=1):
    return sum((F(1, j**order) for j in range(1, m + 1)), F(0))

def b(m,n):
    return F((-1)**n * comb(m,n),2**n)

def a(m,t):
    return F(2**max(m-t,0)*factorial(2*m)*factorial(t-1),
             2**max(t-m,0)*factorial(m+t)*factorial(m-1))

def k(z):
    return -2 + F(2,3)/(z+F(1,3)) + 1/(z+F(2,3))

def kappa(t):
    return -2 + F(4,6*t+1) + F(2,2*t+1)

def cauchy(m,z,q):
    return sum((F((-1)**n*comb(m,n))*q**n/(z+n)
                for n in range(m+1)), F(0))

def main():
    ranks = list(range(1,11)) + [35]
    for m in ranks:
        D = F(2**m*factorial(2*m), factorial(m)*factorial(m-1))
        for n in range(m+1):
            rho = F((-1)**n*comb(m,n))
            assert b(m,n)==rho/F(2**n)
            ell=H(n)-H(m-n)
            # Expand independent rational factors of epsilon*Q(-n+epsilon).
            coeff=[F(1), F(0), F(0)]
            for j in range(m+1):
                if j==n: continue
                delta=F(j-n)
                out=[F(0),F(0),F(0)]
                for i in range(3):
                    for h in range(3-i):
                        out[i+h]+=coeff[i]*((-1)**h)/delta**h
                coeff=out
            assert coeff[1]==ell
            assert coeff[2]==(ell**2+H(n,2)+H(m-n,2))/2
        for t in range(1,3*m+1):
            assert a(m,t)==D*Q(m,F(t))/2**t
            assert kappa(t)==k(F(t)-F(1,6))
            assert Q(m,F(t))==sum((F((-1)**n*comb(m,n),t+n)
                                  for n in range(m+1)),F(0))
            if t<3*m:
                assert Q(m,F(t+1))/Q(m,F(t))==F(t,t+m+1)
        for alpha in (1,2):
            z=F(alpha,3)
            ia=sum((b(m,n)/F(3*n+alpha) for n in range(m+1)), F(0))
            mix=sum((F(comb(m,j),2**m)*Q(j,z) for j in range(m+1)),F(0))/3
            assert ia==mix==cauchy(m,z,F(1,2))/3
        low=sum((b(m,n)*k(F(n)) for n in range(m+1)),F(0))
        high=sum((a(m,t)*kappa(t) for t in range(1,m)),F(0))
        high+=sum((a(m,t)*kappa(t)/3 for t in range(m+1,3*m)),F(0))
        dualhigh=D*sum((Q(m,F(t))*k(F(t)-F(1,6))/2**t
                        for t in range(1,m)),F(0))
        dualhigh+=D*sum((Q(m,F(t))*k(F(t)-F(1,6))/(3*2**t)
                         for t in range(m+1,3*m)),F(0))
        assert high==dualhigh
        assert low==sum((b(m,n)*k(F(n)) for n in range(m+1)),F(0))
    print("PASS: exact D25 common carrier and forcing for m="+str(ranks))

if __name__ == "__main__":
    main()
