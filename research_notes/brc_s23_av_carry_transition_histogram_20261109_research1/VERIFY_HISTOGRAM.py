#!/usr/bin/env python3
"""Exact rational certificate for S23/AV carry symbol histogram, 2026-11-09.
No floating point. Source pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
"""
from fractions import Fraction
from collections import Counter

B=79

def log_interval(p,q,n):
    x=Fraction(p-q,p+q)
    term=x
    lo=Fraction(0)
    for j in range(n):
        lo+=2*term/(2*j+1)
        term*=x*x
    return lo,lo+2*term/((2*n+1)*(1-x*x))

def alpha_interval(n):
    l7,u7=log_interval(7,1,n)
    l107,u107=log_interval(10,7,n)
    dl=79*l7-431*u107
    du=79*u7-431*l107
    nl=2074774*l107-380295*u7
    nu=2074774*u107-380295*l7
    assert 0<dl<du and 0<nl<nu
    l,u=nl/du,nu/dl
    assert Fraction(1,2)<l<u<Fraction(2,3)
    return l,u

def floor_sum(n,m,a,b):
    """Sum floor((a*i+b)/m), i=0..n-1, a,b>=0."""
    ans=0
    while True:
        if a>=m:
            ans+=(n-1)*n*(a//m)//2
            a%=m
        if b>=m:
            ans+=n*(b//m)
            b%=m
        y=a*n+b
        if y<m:return ans
        n=y//m
        b=y%m
        m,a=a,m

def rational_floor_sum(K, x, shift_num=0,shift_den=1):
    # sum k=1..K floor(k*x + shift_num/shift_den)
    p,q=x.numerator,x.denominator
    return floor_sum(K,q*shift_den,p*shift_den,p*shift_den+q*shift_num)

def certified_hist(K, terms=160):
    lo,hi=alpha_interval(terms)
    base_l=rational_floor_sum(K,lo)
    base_u=rational_floor_sum(K,hi)
    if base_l!=base_u: raise AssertionError(('base_not_certified',K,base_u-base_l))
    threshold={0:K,79:0}
    for m in range(1,79):
        tlo=rational_floor_sum(K,lo,79-m,79)
        thi=rational_floor_sum(K,hi,79-m,79)
        if tlo!=thi:
            raise AssertionError(('shift_not_certified',K,m,thi-tlo))
        threshold[m]=tlo-base_l
    hist={c:threshold[c]-threshold[c+1] for c in range(79)}
    assert all(v>=0 for v in hist.values())
    assert sum(hist.values())==K
    S=sum(c*hist[c] for c in range(79))
    sb=rational_floor_sum(K,lo*79)-79*base_l
    assert S==sb
    return lo,hi,hist,S

def certified_transition_check(K=100000, terms=160):
    lo,hi=alpha_interval(terms)
    # prove q=floor(79*alpha)=46 with exact rational interval
    q0=(79*lo).__floor__()
    assert q0==(79*hi).__floor__()==46
    # Each C_k separately certified, also for k=K+1.
    symbols=[]
    for k in range(1,K+2):
        c_lo=(79*k*lo).__floor__()-79*(k*lo).__floor__()
        c_hi=(79*k*hi).__floor__()-79*(k*hi).__floor__()
        assert c_lo==c_hi
        symbols.append(c_lo)
    edges=Counter()
    low_count=high_count=0
    for k in range(K):
        a,b=symbols[k],symbols[k+1]
        if b == (a+q0)%79:
            low_count+=1
            edges[(a,b)]+=1
        elif b == (a+q0+1)%79:
            high_count+=1
            edges[(a,b)]+=1
        else:
            raise AssertionError(('invalid_edge',k+1,a,b))
    assert len(edges)==158 and low_count+high_count==K
    return q0,low_count,high_count,len(edges),min(edges.values()),max(edges.values())

if __name__=='__main__':
    import sys,time
    Ks=[int(x) for x in sys.argv[1:]] or [10_000,1_000_000,1_000_000_000_000]
    for K in Ks:
        t=time.perf_counter()
        lo,hi,hist,S=certified_hist(K,160)
        if K<=10000:
            direct=Counter((79*k*lo).__floor__()-79*(k*lo).__floor__() for k in range(1,K+1))
            assert all(hist[c]==direct[c] for c in hist)
        print('PASS_EXACT_79_SYMBOL_CARRY_HISTOGRAM', 'K=',K,'terms=',160)
        print('  alpha_bounds_width_lt_1e-20=',hi-lo<Fraction(1,10**20))
        print('  horizons_second_candidate=',S)
        print('  freq0,1,39,77,78=',[hist[c] for c in (0,1,39,77,78)])
        print('  min/max_symbol_frequencies=',min(hist.values()),max(hist.values()))
        print('  sum_frequencies=',sum(hist.values()),'weighted_sum=',sum(c*hist[c] for c in hist))
        print('  runtime_seconds=',round(time.perf_counter()-t,3))
    print('PASS_EXACT_79_STATE_TRANSITIONS', 'K=',100000,'q,low,high,edges,min,max=',certified_transition_check(100000))
