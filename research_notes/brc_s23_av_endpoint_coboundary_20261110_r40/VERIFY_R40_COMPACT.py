#!/usr/bin/env python3
"""R40: exact batch coboundary counts versus independent Euclidean floor sums."""
from fractions import Fraction as Q
from math import isqrt

def floor(x): return x.numerator // x.denominator

def theta(p,q,s,scale):
    D=10**70; u=isqrt(s*D*D)
    return Q(p,q)+Q(u,D*scale),Q(p,q)+Q(u+1,D*scale)

def sum_floor(n,M,a,b):
    v=0
    while True:
        if a>=M:
            v+=n*(n-1)*(a//M)//2; a%=M
        if b>=M:
            v+=n*(b//M); b%=M
        y=a*n+b
        if y<M: return v
        n,b,M,a=y//M,y%M,a,M

def shifted(L,J,z,t):
    q,r=divmod((L-z)*t.numerator,t.denominator)
    return (J-L)*q+sum_floor(J-L,t.denominator,t.numerator,r)

def run(case,p,q,s,scale,m,J,N):
    lo,hi=theta(p,q,s,scale)
    t=(lo+hi)/2
    order=sorted(range(m),key=lambda z: (z*t.numerator)%t.denominator)
    assert order[0]==0
    assert all(floor(d*lo)==floor(d*hi) for d in range(1,m))
    arcs=[(a,order[(k+1)%m],int(k==m-1)) for k,a in enumerate(order)]
    def certified(s):
        a=floor(s*lo); b=floor(s*hi);assert a==b,(case,s,a,b);return a
    a_hist=[certified(z) for z in range(m)]
    a_end=[certified(J-1-z) for z in range(m-1)]
    count_calls=0
    def counts(L):
        nonlocal count_calls
        count_calls+=1
        n=J-L
        prefix=[0]
        for z in range(m-1):
            prefix.append(prefix[-1]+a_end[z]-certified(L-1-z))
        cs=[prefix[b]-prefix[a]+n*(a_hist[a]-a_hist[b]+w) for a,b,w in arcs]
        assert min(cs)>=0 and sum(cs)==n
        return cs
    # One-pass exact reference: two independent Euclidean floor sums per arc.
    for L in [J-N,J-N//2,J-1,J]:
        got=counts(L)
        for k,(a,b,w) in enumerate(arcs):
            oracle=(shifted(L,J,a,t)-shifted(L,J,b,t)
                    +(J-L)*(floor(a*t)-floor(b*t)+w))
            assert got[k]==oracle,(case,k,L,got[k],oracle)
    # Last source via independent arithmetic and with the batch endpoint counts.
    for k,(a,b,w) in enumerate(arcs):
        base=counts(J-N)[k]
        if base==0:continue
        left,right=J-N,J
        while right-left>1:
            mid=(left+right)//2
            if counts(mid)[k]>0:left=mid
            else:right=mid
        assert counts(left)[k]>=1 and counts(left+1)[k]==0
        # Last actual owner membership at both strict rational endpoints.
        for t0 in (lo,hi):
            x=(left*t0)%1; u=(a*t0)%1; v=(b*t0)%1
            assert u<=x<v or (w and (u<=x or x<v)),(case,k,left)
    print(case,'m',m,'query_calls',count_calls,'owners',m)

for c in [('NEAR_THIRD_21',1,3,2,10**7,21,10**9,10**8),
          ('MIXED_128',1,3,2,1000,128,10**9,10**8),
          ('SQRT2_129',-1,1,2,1,129,10**9,10**8),
          ('NEGATIVE_WINDOW',-1,1,2,1,16,9,50)]:run(*c)
print('PASS_R40_COMPACT_FOUR_EXACT_FAMILIES')
