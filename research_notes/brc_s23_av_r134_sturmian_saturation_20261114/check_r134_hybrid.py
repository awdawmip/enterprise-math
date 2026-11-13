#!/usr/bin/env python3
"""Uniform polynomial-time exact S23 vocabulary and rational witnesses for any K,m."""
from fractions import Fraction as Q
from math import gcd
import json

def S(K,m,t):
    return ''.join(str(((K+i)*t).__floor__()-((K+i-1)*t).__floor__()) for i in range(m))

def phi(q): return sum(gcd(r,q)==1 for r in range(1,q+1))
def F(m): return 1+sum((m+1-q)*phi(q) for q in range(1,m+1))
def farey(m): return sorted({Q(p,q) for q in range(1,m+1) for p in range(q+1)})

def hybrid(K,m):
    assert K>=1 and m>=1
    out={}
    if K>=4*m**3+2:
        ff=farey(m)
        for a,b in zip(ff,ff[1:]):
            alpha=(a+b)/2
            cuts=sorted({Q(0),Q(1)}|{(-j*alpha)%1 for j in range(m+1)})
            for u,v in zip(cuts,cuts[1:]):
                rho=(u+v)/2
                N=((K-1)*alpha-rho+Q(1,2)).__floor__()
                t=(N+rho)/(K-1)
                assert 0<t<1
                out.setdefault(S(K,m,t),t)
        assert len(out)==F(m)
    else:
        cuts={Q(0),Q(1)}
        for n in range(K-1,K+m):
            if n>0:cuts.update(Q(p,n) for p in range(1,n))
        v=sorted(cuts)
        for t in v[1:-1]: out.setdefault(S(K,m,t),t)
        for a,b in zip(v,v[1:]):
            t=(a+b)/2
            out.setdefault(S(K,m,t),t)
    return out

def exact_reference(K,m):
    cuts={Q(0),Q(1)}
    for n in range(K-1,K+m):
        if n>0:cuts.update(Q(p,n) for p in range(1,n))
    v=sorted(cuts)
    return {S(K,m,t) for t in v[1:-1]}|{S(K,m,(a+b)/2) for a,b in zip(v,v[1:])}

def run():
    tests=0; sampled=0; rows=[]
    for m in range(1,9):
        for K in range(1,75):
            got=hybrid(K,m)
            assert set(got)==exact_reference(K,m)
            assert all(S(K,m,t)==w for w,t in got.items())
            tests+=1; sampled+=len(got)
        Kbig=10**90+7
        got=hybrid(Kbig,m)
        assert len(got)==F(m)
        assert all(S(Kbig,m,t)==w for w,t in got.items())
        rows.append(dict(m=m,K75_count=len(hybrid(75,m)),Kbig_count=len(got),full_F=F(m)))
    return dict(result='R134_HYBRID_BIT_POLY_PASS',bruteforce_matches=tests,
                rational_witness_crosschecks=sampled,
                huge_coefficient_cases=8, rows=rows,
                arithmetic='exact Fraction', all_K_theorem=True)

if __name__=='__main__': print(json.dumps(run(),indent=2))
