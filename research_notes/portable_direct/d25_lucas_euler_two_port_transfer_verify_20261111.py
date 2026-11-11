#!/usr/bin/env python3
"""Exact regression for Lucas/Euler two-port transport, not native Source execution."""
from math import comb,isqrt
from pathlib import Path
import json

def primes(n):
    a=[True]*(n+1);a[0]=a[1]=False
    for x in range(2,isqrt(n)+1):
        if a[x]:
            for t in range(x*x,n+1,x):a[t]=False
    return [q for q in range(5,n+1) if a[q]]

def poly_port(a,b,q):
    x=pow(2,-1,q);f=d=0
    for k in range(min(a,b)+1):
        c=comb(a,k)*comb(b,k)%q
        f=(f+c*pow(x,k,q))%q
        if k:d=(d+k*c*pow(x,k-1,q))%q
    return f,d

def base(q):
    e=0 if q%6==1 else 1
    a=(q-1-4*e)//6
    return e,a,2*a+e

def factorization(n):
    t=n;p=2;out=[]
    while p*p<=t:
        if t%p==0:
            out.append(p)
            while t%p==0:t//=p
        p+=1 if p==2 else 2
    if t>1:out.append(t)
    return out

def verify():
    ps=primes(997);coeffs=0;polys=0
    for q in ps:
        eq,a,b=base(q);d=q-1-a-b
        if q<=251:
            left=[comb(q-1-a,k)*comb(q-1-b,k)%q for k in range(q-max(a,b))]
            right=[0]*len(left)
            for i in range(d+1):
                for j in range(min(a,b)+1):
                    right[i+j]=(right[i+j]+(-1)**i*comb(d,i)*comb(a,j)*comb(b,j))%q
            assert left==right,(q,"polynomial")
            coeffs+=len(left);polys+=1
        fv,dv=poly_port(a,b,q)
        fc,dc=poly_port(q-1-a,q-1-b,q)
        s=pow(2,-d,q)
        assert fc==s*fv%q
        assert ((1-6*(1-eq))*fc+6*dc)%q==s*((1-6*eq)*fv+6*dv)%q
    cases=mismatch=doublezero=0
    for m in range(401):
        for e in (0,1):
            n=6*m+1+4*e
            if n<5:continue
            for q in factorization(n):
                eq,a,b=base(q);d=q-1-a-b
                F,D=poly_port(m,2*m+e,q)
                raw=(F,((1-6*e)*F+6*D)%q)
                M,R=m//q,(2*m+e)//q
                h,_=poly_port(M,R,q)
                f0,d0=poly_port(a,b,q)
                sc=1 if e==eq else pow(2,-d,q)
                guess=((sc*h*f0)%q,(sc*h*((1-6*eq)*f0+6*d0))%q)
                assert raw==guess,(m,e,q,raw,guess)
                cases+=1;mismatch+=e!=eq;doublezero+=raw==(0,0)
    assert (polys,coeffs,len(ps),cases,mismatch,doublezero)==(52,4077,166,1273,480,122)
    return {"polynomial_primes":polys,"checked_polynomial_coefficients":coeffs,
            "pointwise_prime_count":len(ps),"mixed_factor_cases":cases,
            "mismatched_branches":mismatch,"both_zero_cases":doublezero,
            "range_m":[0,400],"all_exact_checks_passed":True}

if __name__=="__main__":
    x=verify()
    Path(__file__).with_name("d25_lucas_euler_transfer_gh_check.json").write_text(json.dumps(x,indent=2)+"\n")
    print(json.dumps(x,indent=2))
