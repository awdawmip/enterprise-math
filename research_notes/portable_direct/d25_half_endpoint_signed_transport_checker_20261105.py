#!/usr/bin/env python3
"""D25 exact signed half-endpoint factorial-unit observer; no native H0/B0 execution."""
from math import factorial, comb
from argparse import ArgumentParser
import json

def prime(n):
    if n < 2: return False
    d = 2
    while d*d <= n:
        if n%d == 0: return False
        d += 1
    return True

def check(p):
    mod=p**4
    a=b=1
    W=V=WH=VH=0
    CA=M0=M1=0
    for k in range(p):
        va=2*k//p+3*k//p
        vb=4*k//p
        ta=(6*k+1)*a%mod
        tb=(8*k+1)*b%mod
        W=(W+ta)%mod
        V=(V+tb)%mod
        if k <= (p-1)//2:
            WH=(WH+ta)%mod
            VH=(VH+tb)%mod
        if va == 2:
            unit=factorial(2*k-p)*factorial(3*k-p)*pow(216,-k,p)*pow(factorial(k),-5,p)%p
            assert (a//p**2)%p == unit,(p,k,"A_unit")
            CA=(CA+(6*k+1)*unit)%p
        if vb == 2:
            unit=2*factorial(4*k-2*p)*pow(2304,-k,p)*pow(factorial(k),-4,p)%p
            assert (b//p**2)%p == unit,(p,k,"B_unit")
            M0=(M0+unit)%p
            M1=(M1+k*unit)%p
        if k+1 < p:
            a=a*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,mod)%mod
            b=b*(4*k+1)*(4*k+2)*(4*k+3)*pow(576*(k+1)**3,-1,mod)%mod
    assert (M0+8*M1)%p == 0,p
    assert (W-V-WH+VH-p**2*CA)%p**3 == 0,p
    character=1 if pow(p-3,(p-1)//2,p)==1 else -1
    assert V%p**3 == (p*character)%p**3
    assert VH%p**3 == (p*character)%p**3
    target=p%24 in (13,19)
    E=None
    if target:
        assert (WH-VH)%p**2 == 0,p
        E=((WH-VH)%p**3)//p**2
        assert (E+CA)%p == 0,p # finite tested conjecture, not theorem
    return dict(p=p,target=target,M0=M0,M1=M1,CA=CA,E=E,W=W,V=V,WH=WH,VH=VH)

def original_binomial(p):
    mod=p**4
    W=V=WH=VH=0
    for k in range(p):
        a=comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,mod)%mod
        b=comb(2*k,k)**2*comb(4*k,2*k)*pow(2304,-k,mod)%mod
        W=(W+(6*k+1)*a)%mod
        V=(V+(8*k+1)*b)%mod
        if k <= (p-1)//2:
            WH=(WH+(6*k+1)*a)%mod
            VH=(VH+(8*k+1)*b)%mod
    return (W,V,WH,VH)

if __name__ == "__main__":
    ap=ArgumentParser()
    ap.add_argument("--bound",type=int,default=997)
    args=ap.parse_args()
    rows=[check(p) for p in range(5,args.bound+1) if prime(p)]
    for p in [7,13,19,139,373]:
        if p<=args.bound:
            row=check(p)
            assert tuple(row[k] for k in ("W","V","WH","VH"))==original_binomial(p)
    summary=dict(bound=args.bound,primes=len(rows),target=sum(r["target"] for r in rows),failures=0,independent_original_binomial=[p for p in (7,13,19,139,373) if p<=args.bound],native="NOT_EXECUTED")
    print(json.dumps(summary,indent=2))
