#!/usr/bin/env python3
"""Exact signed 216/2304 upper half-endpoint p^4 Wilson/harmonic test.
Author-side auxiliary arithmetic; native original-class H0/B0 NOT RUN.
"""
from math import comb
import argparse
import json


def primes_below(n):
    sieve = bytearray([1]) * (n+1)
    sieve[:2] = bytes([0,0])
    for d in range(2, int(n**0.5)+1):
        if sieve[d]:
            sieve[d*d:n+1:d] = bytes([0])*((n-d*d)//d+1)
    return [p for p in range(5,n+1) if sieve[p]]


def check(p, independent=False):
    m=p**4
    mp=p*p
    H=(p-1)//2
    ca2=(2*p-1)//3
    cb2=(3*p-1)//4
    f=[1]*p
    h=[0]*p
    for j in range(1,p):
        f[j]=f[j-1]*j%mp
        h[j]=(h[j-1]+pow(j,-1,p))%p
    q=((f[p-1]+1)//p)%p
    assert (f[p-1]+1)%p==0
    fi=[pow(t,-1,mp) for t in f]
    d216=pow(216,-1,mp)
    a=b=1
    ua=ja=da=ub=jb=db=0
    A=B=0
    counts=[0,0,0,0]
    for k in range(p):
        if k>H:
            A=(A+(6*k+1)*a)%m
            B=(B+(8*k+1)*b)%m
            if k<=ca2:
                r2=2*k-p
                r3=3*k-p
                u=f[r2]*f[r3]*pow(d216,k,mp)*pow(fi[k],5,mp)%mp
                ell=(h[r2]+h[r3]-2*q)%p
                ua=(ua+(6*k+1)*u)%mp
                ja=(ja+(6*k+1)*(u%p)*ell)%p
                assert a//p**2%mp==u*(1+p*ell)%mp,(p,k,"A2")
                counts[0]+=1
            else:
                u=(-2*f[2*k-p]*f[3*k-2*p]
                   *pow(216,-k,p)*pow(fi[k]%p,5,p))%p
                da=(da+(6*k+1)*u)%p
                assert a//p**3%p==u,(p,k,"A3")
                counts[1]+=1
            if k<=cb2:
                r4=4*k-2*p
                u=2*f[r4]*pow(2304,-k,mp)*pow(fi[k],4,mp)%mp
                ell=(2*h[r4]-2*q)%p
                ub=(ub+(8*k+1)*u)%mp
                jb=(jb+(8*k+1)*(u%p)*ell)%p
                assert b//p**2%mp==u*(1+p*ell)%mp,(p,k,"B2")
                counts[2]+=1
            else:
                u=(-6*f[4*k-3*p]*pow(2304,-k,p)*pow(fi[k]%p,4,p))%p
                db=(db+(8*k+1)*u)%p
                assert b//p**3%p==u,(p,k,"B3")
                counts[3]+=1
        if k+1<p:
            a=a*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,m)%m
            b=b*(4*k+1)*(4*k+2)*(4*k+3)*pow(576*(k+1)**3,-1,m)%m
    predA=p*p*(ua+p*(ja+da))%m
    predB=p*p*(ub+p*(jb+db))%m
    assert A==predA and B==predB,(p,"shell sums")
    assert (A-B-(predA-predB))%m==0,(p,"joint")
    assert ub%p==0,(p,"preexisting signed B cancellation")
    if independent:
        tA=sum((6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,m)
               for k in range(H+1,p))%m
        tB=sum((8*k+1)*comb(2*k,k)**2*comb(4*k,2*k)*pow(2304,-k,m)
               for k in range(H+1,p))%m
        assert (tA,tB)==(A,B),(p,"original binomial cross-check")
    return dict(p=p,UA=ua,JA=ja,DA=da,UB=ub,JB=jb,DB=db,
                Aupper=A,Bupper=B,counts=counts,independent=independent)


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--bound",type=int,default=1200)
    args=ap.parse_args()
    pp=primes_below(args.bound)
    samples={7,13,19,139,373}
    rows=[check(p,p in samples) for p in pp]
    print(json.dumps(dict(total=len(rows),max_prime=pp[-1],failures=0,
                          sample=[row for row in rows if row["p"] in samples],
                          native_H0B0="NOT_RUN",admission="UNREVIEWED_NOT_ADMITTED"),indent=2))
