#!/usr/bin/env python3
"""Exact certified-endpoint experiments for the rational-cluster risk law."""
import math
from fractions import Fraction as F
from bisect import bisect_right
from pathlib import Path

Q=10**24
s=math.isqrt(2*Q*Q)
assert s*s<2*Q*Q<(s+1)**2


def exact_risk_by_sort(t,m,n):
    seq=sorted(((i*t)%1 for i in range(n)))
    history=sorted(((i*t)%1 for i in range(m)))
    maxima=[F(0)]*m
    for i,v in enumerate(seq):
        nxt=seq[i+1] if i+1<n else seq[0]+1
        length=nxt-v
        j=bisect_right(history,v)-1
        if length>maxima[j]:maxima[j]=length
    return 1-sum(maxima)


def exact_theta_interval(p,q,eps_denom):
    return (F(p,q)+F(s,Q*eps_denom),F(p,q)+F(s+1,Q*eps_denom))


if __name__=='__main__':
    total=0
    for p,q,m,N in [(1,2,128,380),(1,3,33,322),(2,3,30,333),(2,5,40,240),(3,7,28,210),(0,1,17,200)]:
        eps_denom=10**8
        lo,hi=exact_theta_interval(p,q,eps_denom)
        assert (N+q)*(hi-F(p,q))<F(1,q)
        for n in range(m,N+1):
            for theta in (lo,hi):
                got=exact_risk_by_sort(theta,m,n)
                predicted=(n-m)*(q*theta-p)
                assert got==predicted,(p,q,m,n,theta,got,predicted)
                total+=1
        print('PASS_CLUSTER',p,q,'m',m,'last_n',N,'runs',1,'slope',(-p,q),'checked_endpoints',2*(N-m+1))
    p,q,m,n=1,3,6,12
    lo,hi=exact_theta_interval(p,q,25)
    for theta in (lo,hi):
        observed=exact_risk_by_sort(theta,m,n)
        extrap=(n-m)*(q*theta-p)
        assert observed!=extrap and extrap>1 and 0<=observed<=1
    print('PASS_OUTSIDE_SCOPE_WITNESS','p=1 q=3 m=6 n=12 eps=sqrt2/25; extrapolated risk > 1')
    print('PASS_RATIONAL_CLUSTER_ALL',total,'exact rational endpoint comparisons')
