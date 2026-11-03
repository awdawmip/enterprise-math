#!/usr/bin/env python3
"""Exact D25 three-edge gluing and Fermat boundary checks; Python stdlib only."""
import json
from math import comb

def inv(a,m): return pow(a%m,-1,m)
def primes(n):
    sieve=bytearray(b"\x01")*(n+1);sieve[0:2]=b"\x00\x00"
    for k in range(2,int(n**0.5)+1):
        if sieve[k]:sieve[k*k:n+1:k]=b"\x00"*((n-k*k)//k+1)
    return [p for p in range(7,n+1) if sieve[p] and p%6==1]

def check(p):
    r=(p-1)//6;m=p*p;M=m*m
    chi=1 if pow(6,(p-1)//2,p)==1 else -1
    q=lambda a:(pow(a,p-1,p*p)-1)//p
    eps=(3+(q(2)-3*q(3))*inv(2,p))%p
    u=1;E=0
    for t in range(1,r):
        u=u*9*(2*t-1)**3*inv(t*(36*t*t-1),m)%m
        E=(E+inv(2*t,p)+3*inv(6*t-1,p)+3*inv(6*t+1,p)-3*inv(2*t-1,p))%p
    h=0
    for i in range(2*r):
        h=(h+inv(2*(i-3*r),p)+inv(3*(i-2*r),p)+2*inv(3*(i-4*r),p))%p
    T=comb(3*r,2*r)*comb(4*r,2*r)*inv(2**(2*r),m)%m
    b=[1]
    for k in range(4*r+1):
        b.append(b[-1]*(2*k+1)*(3*k+1)*(3*k+2)*inv(36*(k+1)**3,M)%M)
    assert b[2*r]%p and b[3*r]%p==0 and (b[3*r]//p)%p
    assert b[3*r+1]%(p*p)==0 and (b[3*r+1]//(p*p))%p
    assert b[4*r+1]%(p**3)==0 and (b[4*r+1]//p**3)%p
    alpha=(2*p+1)*(p+1)*inv(4*(p+2)**3,m)%m
    beta=(9*p*p-1)*inv(18*(p+1)**3,m)%m
    gamma=(4*p-1)*(2*p-1)*inv(2*(2*p+1)**3,m)%m
    assert alpha==inv(32,m)*(1+3*p*inv(2,m))%m
    assert beta==(-inv(18,m)*(1-3*p))%m
    assert gamma==inv(2,m)*(1-12*p)%m
    if p in [7,13,19,37,43,373]:
        for k in (2*r,3*r,3*r+1,4*r,4*r+1):
            assert b[k]==comb(2*k,k)**2*comb(3*k,k)*inv(216**k,M)%M
    bn=b[3*r]//p%m
    assert bn==(-2*chi*(1+p*eps))%m
    jump=b[2*r]*inv(bn,m)%m
    assert jump==32*u*(1+p*((E-3*inv(2,p))%p))%m
    low=T*(1+p*h)%m
    middle=-64*chi*u*(1+p*((eps+E-3*inv(2,p))%p))%m
    assert low==middle==b[2*r]%m
    assert (T+64*chi*u)%p==0
    ratio=T*inv(-64*chi*u,m)%m
    assert ratio%p==1
    delta=((ratio-1)//p)%p
    assert eps==(h-E+3*inv(2,p)+delta)%p
    high=b[3*r+1]//(p*p)%m
    assert high==(chi*inv(9,m)*(1+p*((eps-3)%p)))%m
    f=1
    for t in range(r-1):
        f=f*(t+1)*(6*t+5)*(6*t+7)*inv(9*(2*t+3)**3,p)%p
    third=b[4*r+1]//p**3%p
    assert third==chi*f*inv(18,p)%p
    return {"p":p,"chi":chi,"epsilon":eps,"E":E,"delta":delta,
            "h":h,"pU_r":jump,"b_2r":low,"high_entry":high,"third_entry":third}

if __name__=="__main__":
    rows=[check(p) for p in primes(2000)]
    highlights=[v for v in rows if v["p"] in (7,13,19,37,43,373)]
    print(json.dumps({"primes":len(rows),"all_assertions_passed":True,"highlights":highlights}))
