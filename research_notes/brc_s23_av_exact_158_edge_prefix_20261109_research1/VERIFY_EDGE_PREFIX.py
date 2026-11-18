#!/usr/bin/env python3
"""S23/AV 79-state exact directed edge counts, with certified rational arithmetic.
Frozen science: 43ec6098b1330ae86d0a7863be336c5d97f6ef34
All results depend only on the earlier established S23/AV carry definition,
and the exact irrational alpha.  This is an auxiliary-model result.
"""
from fractions import Fraction
from collections import Counter
import sys
B = 79

def log_interval(p,q,n):
    x=Fraction(p-q,p+q)
    term=x; low=Fraction(0)
    for j in range(n):
        low += 2*term/(2*j+1)
        term *= x*x
    return low, low+2*term/((2*n+1)*(1-x*x))

def alpha_interval(n=160):
    l7,u7=log_interval(7,1,n)
    l107,u107=log_interval(10,7,n)
    dl=79*l7-431*u107; du=79*u7-431*l107
    nl=2074774*l107-380295*u7
    nu=2074774*u107-380295*l7
    assert 0<dl<du and 0<nl<nu
    lo,hi=nl/du,nu/dl
    assert Fraction(1,2)<lo<hi<Fraction(2,3)
    assert (79*lo).__floor__()==(79*hi).__floor__()==46
    return lo,hi

def floor_sum(n,m,a,b):
    """Sum floor((a*j+b)/m), j=0..n-1, a>=0, m>0, b any integer."""
    assert n>=0 and m>0 and a>=0
    base,b=divmod(b,m)
    ans=n*base
    while True:
        if a>=m:
            ans+=(n-1)*n*(a//m)//2
            a%=m
        if b>=m:
            ans+=n*(b//m)
            b%=m
        y=a*n+b
        if y<m:
            return ans
        n=y//m
        b=y%m
        m,a=a,m

def sum_floor_shifted(K,x,shift_num,shift_den=79,start=1):
    """sum_(k=1)^K floor((k+start-1)*x + shift_num/shift_den)."""
    p,q=x.numerator,x.denominator
    return floor_sum(K, q*shift_den, p*shift_den, start*p*shift_den+shift_num*q)

def pair_sums(K,lo,hi,offset,start):
    a=sum_floor_shifted(K,lo,offset,start=start)
    b=sum_floor_shifted(K,hi,offset,start=start)
    assert a==b,('uncertified',K,offset,start,a,b)
    return a

def edge_histogram(K,n=160):
    lo,hi=alpha_interval(n)
    hist={}
    for c in range(B):
        # E_(c,high)=sum [floor((k+1)*alpha+(32-c)/79)
        #                      - floor(k*alpha+(78-c)/79)]
        first=pair_sums(K,lo,hi,32-c,2)
        second=pair_sums(K,lo,hi,78-c,1)
        high=first-second
        # F_c via exact tail indicator thresholds (c=0,78 included)
        def tail(m):
            if m==0:return K
            if m==79:return 0
            a=pair_sums(K,lo,hi,79-m,1)
            b=pair_sums(K,lo,hi,0,1)
            return a-b
        freq=tail(c)-tail(c+1)
        low=freq-high
        assert 0<=high<=freq and 0<=low<=freq,(c,freq,high)
        hist[c]=(low,high)
    high=sum(h for l,h in hist.values())
    low=sum(l for l,h in hist.values())
    assert low+high==K
    # Sum_(k=1)^K floor((k+1)*theta)-floor(k*theta) = floor((K+1)*theta).
    theta_lo=79*lo-46; theta_hi=79*hi-46
    h0=((K+1)*theta_lo).__floor__()
    h1=((K+1)*theta_hi).__floor__()
    assert h0==h1==high,(h0,h1,high)
    return hist,low,high,lo,hi

def direct_edges(K,lo,hi):
    counts=Counter()
    for k in range(1,K+1):
        c0=(79*k*lo).__floor__()-79*(k*lo).__floor__()
        c1=(79*k*hi).__floor__()-79*(k*hi).__floor__()
        nxt0=(79*(k+1)*lo).__floor__()-79*((k+1)*lo).__floor__()
        nxt1=(79*(k+1)*hi).__floor__()-79*((k+1)*hi).__floor__()
        assert c0==c1 and nxt0==nxt1
        high=(nxt0-(c0+46))%79
        assert high in (0,1)
        counts[(c0,high)]+=1
    return counts

if __name__=='__main__':
    ks=list(map(int,sys.argv[1:])) or [10000,1000000,10**12]
    for K in ks:
        hist,low,high,lo,hi=edge_histogram(K)
        if K<=10000:
            direct=direct_edges(K,lo,hi)
            assert all(direct[c,0]==hist[c][0] and direct[c,1]==hist[c][1] for c in range(79))
        print('PASS_EXACT_158_EDGE_PREFIX', 'K=',K,'terms=160')
        print('  low/high=',low,high,'sum=',low+high)
        print('  selected (low,high)=',[(c,hist[c]) for c in (0,1,39,77,78)])
        print('  per_edge_minmax=',min(v for pair in hist.values() for v in pair),max(v for pair in hist.values() for v in pair))
        print('  nonzero_edges=',sum(v>0 for pair in hist.values() for v in pair))
        print('  alpha_bounds_width_lt_1e-20=',hi-lo<Fraction(1,10**20))
    print('PASS_CERTIFIED_ALL_158_EDGE_COUNTS')
