#!/usr/bin/env python3
"""Independent synthetic exact-integer check of the C306 modulus and lower bound.
Does not import or invoke C306_SUPPORT_OPTIMAL_MODULAR_NEWTON.py.
"""
from __future__ import annotations
from math import factorial,gcd
import json,random,argparse

def eval_coeff(a,t):
    y=0
    for c in reversed(a): y=y*t+c
    return y

def sup_fact(f,s):
    x=f;part=1
    while True:
        g=gcd(x,s)
        if g==1:return part
        x//=g;part*=g

def recover(s,d,a,T):
    fac=factorial(d);h=sup_fact(fac,s);M=s*h
    r=[eval_coeff(a,T+j)%M for j in range(d+1)]
    kfac=1;g=s
    for k in range(d+1):
        if k:kfac*=k
        q=gcd(kfac,h);v=kfac//q
        assert gcd(v,s)==1
        z=r[0]
        assert z%q==0
        if s>1:g=gcd(g,((z//q)*pow(v,-1,s))%s)
        if k<d:r=[(r[j+1]-r[j])%M for j in range(len(r)-1)]
    return g,M

def primes(n):
    p=2;out=[]
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:out.append(n)
    return out

def vp(n,p):
    e=0
    while n and n%p==0:e+=1;n//=p
    return e

def minimal_witness(s,d,T,p,M):
    N=M//p;ep=vp(N,p);v=vp(factorial(d),p)
    u=max(0,ep-v)
    C=(N//(p**ep))*(p**u)
    # P=C*prod_{i=0}^{d-1}(t-(T+i))
    coeff=[C]
    for i in range(d):
        r=-(T+i);new=[0]*(len(coeff)+1)
        for j,z in enumerate(coeff):new[j]+=r*z;new[j+1]+=z
        coeff=new
    assert all(eval_coeff(coeff,T+j)%N==0 for j in range(d+1))
    cont=0
    for z in coeff: cont=gcd(cont,z)
    assert vp(gcd(s,cont),p)<vp(s,p)
    return True

def main():
    rng=random.Random(30620261025)
    tested=0; witnesses=0; values=0
    # Includes d=0, zero polynomial, negative coefficients and nodes, s=1.
    for d in range(0,9):
      for s in range(1,121):
        for rep in range(2):
            a=[rng.randrange(-100000,100001) for _ in range(d+1)]
            if rep==1 and d%3==0:a=[0]*(d+1)
            T=rng.randint(-11,11)
            z,M=recover(s,d,a,T)
            c=0
            for v in a:c=gcd(c,v)
            assert z==gcd(s,c), (s,d,rep,z,gcd(s,c))
            tested+=1;values+=d+1
            if rep==0 and s>1:
                for p in primes(s):
                    minimal_witness(s,d,T,p,M);witnesses+=1
    report={"schema":"C306_INDEPENDENT_SYNTHETIC_V1","polynomials_checked":tested,
            "integer_values_checked":values,"prime_power_lower_bound_witnesses":witnesses,
            "rng_seed":30620261025,"degrees":"0..8","s_range":"1..120",
            "coefficients":"random integers [-100000,100000] with exact zero edge cases",
            "status":"PASS_EXACT_INTEGER_CHECKS"}
    with open('/mnt/data/C306_work/C306_INDEPENDENT_SYNTHETIC_AUDIT.json','w') as f:json.dump(report,f,indent=2)
    print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':main()
