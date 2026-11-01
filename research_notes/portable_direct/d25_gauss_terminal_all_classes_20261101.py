#!/usr/bin/env python3
"""Verify D25 all-residue terminal forcing by exact integer modular arithmetic."""
from math import isqrt

def primes(n):
    sieve=[True]*(n+1); sieve[0]=sieve[1]=False
    for p in range(2,isqrt(n)+1):
        if sieve[p]:
            for j in range(p*p,n+1,p): sieve[j]=False
    return [p for p in range(11,n+1) if sieve[p]]

def original_coefficients(p):
    m=p**3; c=[1]
    for k in range(1,p):
        c.append(c[-1]*(8*k-7)*(8*k-5)*pow(64*k*k,-1,m)%m)
    return c

def operator_at(coeff,z,mod):
    f=d=dd=0
    for a in reversed(coeff):
        dd=(dd*z+2*d)%mod
        d=(d*z+f)%mod
        f=(f*z+a)%mod
    return (z*(1-z)*dd+(1-3*z*pow(2,-1,mod))*d-3*pow(64,-1,mod)*f)%mod

def check(p):
    m=p**3; c=original_coefficients(p)
    alpha=next(a for a in (1,3,5,7) if a*p%8==1)
    beta=next(a for a in (1,3,5,7) if a*p%8==3)
    assert c[-1]%(p*p)==0
    unit=(c[-1]//(p*p))%p
    assert unit==(alpha*beta*pow(35,-1,p))%p
    for z in (2,pow(9,-1,m)):
        assert operator_at(c,z,m)==(-alpha*beta*pow(64,-1,m)*p*p*pow(z,p-1,m))%m
    return p,alpha,beta,unit,(-alpha*beta*pow(64,-1,p))%p

def main():
    rows=[check(p) for p in primes(3000)]
    assert len(rows)==426
    print("PASS_ALL_CLASS_P3_TERMINAL",len(rows))
    for r in (1,3,5,7):
        group=[v for v in rows if v[0]%8==r]
        print("CLASS",r,"count",len(group),"alpha_beta",(group[0][1],group[0][2]))
    for row in rows:
        if row[0] in (11,13,17,19,23,37,61,109,373):
            print("CERT",row)

if __name__=="__main__":main()
