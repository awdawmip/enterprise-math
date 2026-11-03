#!/usr/bin/env python3
"""Exact integer checks, not a native H0/B0 experiment."""
from math import comb
import json

def primes(n):
    s=bytearray(b'\x01')*(n+1)
    s[0:2]=b'\x00\x00'
    for d in range(2,int(n**0.5)+1):
        if s[d]:
            s[d*d:n+1:d]=b'\x00'*((n-d*d)//d+1)
    return [p for p in range(13,n+1) if s[p] and p%24 in (13,19)]

def check(p):
    mod=p**4
    bs=[1]; inv36=pow(36,-1,mod)
    for k in range(1,p):
        bs.append(bs[-1]*(2*k-1)*(3*k-2)*(3*k-1)*inv36*pow(k,-3,mod)%mod)
    w=[(6*k+1)*b%mod for k,b in enumerate(bs)]
    W1=sum(w)%mod
    r=(p-1)//6
    j=sum(k*comb(r,k)*comb(2*r,k)*pow(2,-k,p) for k in range(r+1))%p
    assert j!=0
    d3=sum(k*(k-1)*(k-2)*w[k] for k in range(p))%p
    d4=sum(k*(k-1)*(k-2)*(k-3)*w[k] for k in range(p))%p
    assert d3==116*pow(3,-1,p)*j*j%p
    assert d4==760*pow(9,-1,p)*j*j%p
    C1=sum(bs[k]*bs[p-1-k] for k in range(p))%mod
    assert C1%p**2==0 and C1//p**2%p==10%p
    d1=sum(k*w[k] for k in range(p))%mod
    d2=sum(k*(k-1)*w[k] for k in range(p))%mod
    d3_mod=sum(k*(k-1)*(k-2)*w[k] for k in range(p))%mod
    sample=[]
    for lam in (1,2,3):
        t=1+p*lam
        term=1; Wt=0
        for wk in w:
            Wt=(Wt+wk*term)%mod
            term=term*t%mod
        Ct=C1*pow(t,p-1,mod)%mod
        assert Ct==sum(bs[k]*bs[p-1-k]*pow(t,p-1,mod) for k in range(p))%mod
        dc=(Ct-C1)%mod;dw=(Wt-W1)%mod
        assert dc%p**3==0 and dc//p**3%p==(-10*lam)%p
        assert dw%p**2==12*p*lam*j*j%p**2
        assert dw%p**2==(-6*pow(5,-1,mod)*j*j*(dc//p**2))%p**2
        taylor=(W1+p*lam*d1+p*p*lam*lam*d2*pow(2,-1,mod)
                +p**3*lam**3*d3_mod*pow(6,-1,mod))%mod
        assert Wt==taylor
        sample.append({"lambda":lam,"reflection_digit":dc//p**3%p,
                       "weighted_digit":dw//p%p,"W_t_mod_p4":Wt})
    return {"p":p,"j":j,"D3_modp":d3,"D4_modp":d4,
            "C1_modp4":C1,"W1_modp4":W1,"samples":sample}

if __name__=="__main__":
    results=[check(p) for p in primes(2000)]
    print(json.dumps({"status":"PASS","count":len(results),
      "selection":"all target-class primes <=2000",
      "lambdas":[1,2,3],"examples":[x for x in results
      if x["p"] in (13,19,373)]},indent=2))
