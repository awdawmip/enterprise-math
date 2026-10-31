#!/usr/bin/env python3
"""R423 finite exact checks: original signed coefficients vs symmetric kernel."""
from fractions import Fraction as F
from math import comb
from functools import lru_cache
import json

def choose(n,k):
    return comb(n,k) if 0<=k<=n else 0

@lru_cache(maxsize=None)
def rho(q,d):
    v=F(1)
    for j in range(abs(d)):
        v*=F(q-j,q+j+1)
    return v

def delta(q,n):
    return sum(comb(n,k)*(choose(2*q,q+n-2*k)-
                    choose(2*q,q+n-2*k-1)) for k in range(n+1))

def avg(q,n):
    assert q>=n
    return sum((F(comb(n,k),2**n)*rho(q,n-2*k)*
                F(q+1-2*(n-2*k)**2,(q+1)**2-(n-2*k)**2))
               for k in range(n+1))

def norm_D(m,s):
    b={h:s*avg(s+h,m-h) for h in (-1,0,1)}
    lam=F(m*s*s*(2*s+m+1),(m+1)*(s+1)**2*(2*s+m))
    return F(4**m,s*s)*(b[0]**2-lam*b[-1]*b[1]),b,lam

def main():
    A=B=C=E=0
    for q in range(2,26):
        for n in range(min(q,8)+1):
            assert F(delta(q,n),comb(2*q,q)*2**n)==avg(q,n)
            A+=1
    for n in range(29):
        for q in set((max(2,2*n*n),max(3,2*n*n+1),max(4,2*n*n+23))):
            if q<n+1:continue
            x=q*avg(q,n)
            assert 0<=1-x<=F(3*n+2,q)
            B+=1
    for m in list(range(1,17))+[20,24,32,48,64]:
        S=96*(m+2)**2
        for s in (S,S+1,2*S):
            D,b,lam=norm_D(m,s)
            for h in (-1,0,1):
                q,n=s+h,m-h
                x=q*avg(q,n)
                assert q>=2*n*n
                assert 0<=1-x<=F(3*n+2,q)
                assert abs(b[h]-1)<=F(12*(m+2),s)<=F(1,8*(m+2))
            assert 0<lam<F(m,m+1)
            assert D>=F(4**m,2*(m+1)*s*s)
            C+=1
    for m in range(1,9):
        for s in range(max(3,m+2),19):
            r=s+m
            def H(q): return choose(r+q,2*q)*delta(q,r-q)
            W=comb(2*s+m,2*s)*comb(2*s,s)
            D,_,_=norm_D(m,s)
            assert F(H(s)**2-H(s-1)*H(s+1),W*W)==D
            E+=1
    print(json.dumps(dict(status="R423_EXACT_PASS",raw_delta_identity_cases=A,
        moment_bound_cases=B,uniform_threshold_cases=C,
        independent_raw_turan_cases=E,
        arithmetic="exact Python integers and Fraction")))
if __name__=="__main__":main()
