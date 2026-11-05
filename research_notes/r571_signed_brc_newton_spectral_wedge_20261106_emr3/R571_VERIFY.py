#!/usr/bin/env python3
"""R571 independent exact rational crosscheck of universal Newton spectral wedge.
Science source: frozen R462 signed BRC auxiliary Toeplitz-Hessenberg scalar.
All tests use Python integer arithmetic / Fraction; no numerical roots are used.
"""
from fractions import Fraction as F
from math import comb, isqrt


def cat(n):
    return comb(2*n, n)//(n+1)


def h(k,t):
    r=2*k+1
    if not 2<=t<=r:
        return 0
    return comb(r+t, 2*t)*sum(
        comb(t-1, 2*q)*4**q*cat(k-q)
        for q in range(min(k,(t-1)//2)+1)
    )


def calc(k):
    assert k>=2
    a1=F(h(k,3),h(k,2))
    a2=F(h(k,4),h(k,2))
    a1_formula=F((k+2)*(4*k+1),15)
    a2_formula=F((k+2)*(k-1)*(2*k+5)*(8*k+5),420)
    p2=a1*a1-2*a2
    p2_formula=-F((k+2)*(16*k**3-50*k**2-613*k-403),3150)
    assert (a1,a2,p2)==(a1_formula,a2_formula,p2_formula)
    return a1,a2,p2


def main():
    assert calc(8)[-1]==1
    assert calc(9)[-1]==-F(1331,225)
    for k in range(2,1001):
        _, _, p2=calc(k)
        assert (p2<0)==(k>=9)
    # independent integer finite-difference sign certificate f(9+t)>0 for t>=0
    # f(k)=16k^3-50k^2-613k-403.
    assert (16,382,2375,1694)==(16,16*27-50,16*243-50*18-613,16*729-50*81-613*9-403)
    for k in [9,10,29,30,100,1000]:
        p2=calc(k)[-1]
        bound_square=-p2/F(2*k-1)
        assert bound_square>0
        print('K',k,'P2',str(p2),'RHO_LOWER_SQUARED',str(bound_square))
    print('R571_NEWTON_SPECTRAL_WEDGE_EXACT_PASS','k=2..1000',999,'cases')

if __name__=='__main__':
    main()
