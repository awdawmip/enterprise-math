#!/usr/bin/env python3
"""Independent exact direct-arc test of the near-half-integer slope risk law."""
from fractions import Fraction as F
from bisect import bisect_right
from math import isqrt
M=128
K=isqrt(2*10**60)
LO=F(1,2)+F(K,10**42)
HI=F(1,2)+F(K+1,10**42)

def direct_risk(x,n):
    history=sorted((i*x)%1 for i in range(M))
    cuts=sorted((i*x)%1 for i in range(n))
    assert len(set(cuts))==n
    best=[F(0)]*M
    for j,p in enumerate(cuts):
        q=cuts[(j+1)%n]
        gap=(q-p)%1
        if j==n-1:gap=1-p+cuts[0]
        owner=bisect_right(history,p)-1
        assert owner>=0
        best[owner]=max(best[owner],gap)
    return F(1)-sum(best)

for n in (128,129,130,131,200,256,400,513,1000,2000):
    for x in (LO,HI):
        assert 0<x-F(1,2)<F(1,2*(n+1))
        actual=direct_risk(x,n)
        expected=2*(x-F(1,2))*(n-M)
        assert actual==expected,(n,actual,expected)
    print('PASS_INDEPENDENT_EXACT_DIRECT_ARC_RISK',n,'R=(2theta-1)*(n-128)')
print('PASS_NEAR_RATIONAL_AFFINE_RISK_LAW')
