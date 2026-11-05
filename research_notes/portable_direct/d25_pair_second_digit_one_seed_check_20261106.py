#!/usr/bin/env python3
"""Exact author-side check for D25 shell reciprocal mod p^2 and single seed mod p^3."""
import json,math
from pathlib import Path
LIMIT=997
def primes(n):
    s=[True]*(n+1);s[:2]=[False,False]
    for i in range(2,math.isqrt(n)+1):
        if s[i]:
            for j in range(i*i,n+1,i):s[j]=False
    return [p for p in range(5,n+1) if s[p]]
def make(p):
    mod=p**3
    u=[1]*(4*p+1);v=[0]*(4*p+1)
    for n in range(1,4*p+1):
        x=n;c=0
        while x%p==0:x//=p;c+=1
        u[n]=u[n-1]*x%mod;v[n]=v[n-1]+c
    def coeff(ns,ds,base,k):
        val=sum(v[n] for n in ns)-sum(v[n] for n in ds)
        a=pow(base,-k,mod)
        for n in ns:a=a*u[n]%mod
        for n in ds:a=a*pow(u[n],-1,mod)%mod
        return val,a
    def A(k):return coeff([2*k,3*k],[k]*5,216,k)
    def B(k):return coeff([4*k],[k]*4,2304,k)
    def aval(k):
        val,a=A(k)
        return pow(p,val,mod)*a%mod if val<3 else 0
    def bval(k):
        val,a=B(k)
        return pow(p,val,mod)*a%mod if val<3 else 0
    return A,B,aval,bval,mod
def harmonic(n,p):return sum(pow(i,-1,p) for i in range(1,n+1))%p
rows=[];pairs=0;seed_checks=0;pair_examples=[]
for p in primes(LIMIT):
    A,B,a,b,mod=make(p)
    q216=(pow(216,p-1,p*p)-1)//p
    for k in range(p//3+1,(p-1)//2+1):
        ell=p-k;v,u=A(k);w,z=A(ell)
        assert (v,w)==(1,2)
        lhs=u*z%(p*p)
        t=3*k-p
        corr=(2*harmonic(2*k-1,p)+3*harmonic(t-1,p)-5*harmonic(k-1,p)-q216)%p
        rhs=pow(36*k**3,-1,p*p)*(1+p*corr)%(p*p)
        assert lhs==rhs,(p,k,lhs,rhs)
        pairs+=1
        if p in (13,19,67,139,373) and k in (p//3+1,(p-1)//2):
            pair_examples.append([p,k,ell,lhs,corr])
    if p%6!=1:continue
    h=(p-1)//2;m=(p-1)//6
    eps=1 if pow(6,(p-1)//2,p)==1 else -1
    q2=(pow(2,p-1,p*p)-1)//p;q6=(pow(6,p-1,p*p)-1)//p
    seed=-2*eps*(1+p*(3+2*q2-3*pow(2,-1,p)*q6))%(p*p)
    assert seed==A(h)[1]%(p*p)
    seed_checks+=1
    if p%24 not in (13,19):continue
    B0=sum((6*k+1)*a(k) for k in range(2*m+1))%mod
    V=sum((8*k+1)*b(k) for k in range(h+1))%mod
    W=sum((6*k+1)*a(k) for k in range(p))%mod
    assert (B0-V)%p==0
    D=(B0-V)//p%(p*p);run=seed;middle=upper=paired=0
    for j in range(m):
        k=h-j;ell=p-k;v,u=A(k);w,z=A(ell)
        assert v==1 and w==2 and run==u%(p*p)
        partner=pow(36*k**3*(run%p),-1,p)
        assert partner==z%p
        middle+=(3*p-2-6*j)*run
        upper+=(6*j+4)*z
        paired+=(3*p-2-6*j)*run+p*(6*j+4)*partner
        if j<m-1:
            den=(2*k-1)*(3*k-1)*(3*k-2)
            assert den%p
            run=run*36*k**3*pow(den,-1,p*p)%(p*p)
    residue=(D+paired)%(p*p)
    assert residue==(W-V)//p%(p*p)
    assert residue==(D+middle+p*upper)%(p*p)
    rows.append(dict(p=p,D_mod_p2=D,M_over_p_mod_p2=middle%(p*p),
                     U_mod_p=upper%p,paired_mod_p2=paired%(p*p),
                     scalar_residue_mod_p2=residue))
print("primes",len(primes(LIMIT)),"pairs",pairs,"seed_checks",seed_checks,
      "target_primes",len(rows),"all_target_zero",all(r["scalar_residue_mod_p2"]==0 for r in rows))
print("selected",[x for x in rows if x["p"] in (13,19,67,139,373)])
Path("d25_pair_second_digit_results.json").write_text(json.dumps(dict(
    p_max=LIMIT,primes=len(primes(LIMIT)),pairs=pairs,seed_checks=seed_checks,
    target_prime_count=len(rows),target_rows=rows,pair_examples=pair_examples,
    check="EXACT_INTEGER_FINITE_AUTHOR_SIDE_NOT_NATIVE"),indent=2))
