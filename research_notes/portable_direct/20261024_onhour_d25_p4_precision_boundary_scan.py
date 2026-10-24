#!/usr/bin/env python3
"""D25 original-endpoint p^4 precision-boundary study.

Author-side, finite exact arithmetic; not native benchmark, Source result, or
proof of an infinite-prime supercongruence.  Prime classes 13,19 (mod 24).
All factorial products are p-free units modulo p^4. Distinct labeled n-terms
are accumulated into their unit/valuation branches before totalization.
"""
from __future__ import annotations
import argparse
import csv
from math import isqrt


def target_primes(bound: int):
    composite=bytearray(bound+1)
    for d in range(2,isqrt(bound)+1):
        if not composite[d]:
            composite[d*d:bound+1:d]=b'\x01'*(((bound-d*d)//d)+1)
    return [p for p in range(13,bound+1) if not composite[p] and p%24 in (13,19)]


def original_endpoint_mod_p4(p: int):
    """No p-denominator inversions. Every term is original T_(m,n)."""
    if p % 6 != 1 or p<13:
        raise ValueError('expected p=6m+1 >=13 prime')
    m=(p-1)//6
    mod=p**4
    maxidx=12*m
    fac=[1]*(maxidx+1)
    for i in range(1,maxidx+1):
        fac[i]=fac[i-1]*(i if i%p else 1)%mod
    ifac=[1]*(maxidx+1)
    ifac[maxidx]=pow(fac[maxidx],-1,mod)
    for i in range(maxidx,0,-1):
        ifac[i-1]=ifac[i]*(i if i%p else 1)%mod
    a=fac[6*m]*pow(pow(3,6*m,mod)*pow(fac[2*m],3,mod)%mod,-1,mod)%mod
    const=fac[2*m]*fac[2*m]%mod
    q=pow(216,-1,mod)
    qn=1
    total=0
    low=0
    high=0
    for n in range(4*m+1):
        r=(fac[4*m+2*n]*const*fac[3*n]*ifac[2*m+n]*ifac[2*m+n]
           *ifac[4*m+n]*ifac[n]*ifac[n]*qn)%mod
        if n>m:
            r=r*p%mod
        t=(a*(6*n+12*m+1)*r)%mod
        total=(total+t)%mod
        if n<=m: low=(low+t)%mod
        else: high=(high+t)%mod
        qn=qn*q%mod
    target=p*pow(4*pow(3,-1,mod)%mod,p-1,mod)%mod
    difference=(total-target)%mod
    return {"p":p,"m":m,"S_mod_p4":total,"target_mod_p4":target,
            "S_mod_p3":total%(p**3),"low_mod_p4":low,"high_mod_p4":high,
            "difference_mod_p4":difference,
            "delta_mod_p":difference//(p**3) if difference%(p**3)==0 else None}


def original_endpoint_by_independent_recurrence(p: int):
    """Independent p-stripped ratio stream (no factorial quotient formula)."""
    m=(p-1)//6
    mod=p**4
    f6=1
    f2=1
    for t in range(1,p):
        f6=f6*t%mod
        if t<=2*m:
            f2=f2*t%mod
    a=f6*pow((pow(3,p-1,mod)*pow(f2,3,mod))%mod,-1,mod)%mod
    unit=1
    val=0
    total=0
    for n in range(4*m+1):
        assert val==(n>m), (p,n,val)
        total=(total+a*(6*n+12*m+1)*unit*(p if val else 1))%mod
        if n==4*m:
            break
        numer=(4*m+2*n+1)*(3*n+1)*(3*n+2)
        denom=36*(n+1)*(2*m+n+1)*(4*m+n+1)
        while numer%p==0:
            numer//=p
            val+=1
        while denom%p==0:
            denom//=p
            val-=1
        unit=unit*numer*pow(denom,-1,mod)%mod
    return total


def verify_divided_factorial_jet(p: int):
    """Symbolic elementary-symmetric three-jet, independently of p-free product."""
    mod=p**4
    inv=[0]*p
    inv[1]=1
    for t in range(2,p):
        inv[t]=-(mod//t)*inv[mod%t]%mod
    H1=H2=H3=0
    small_fact=1
    little=[1]*p
    h1=[0]*p;h2=[0]*p;h3=[0]*p
    for s in range(1,p):
        small_fact=small_fact*s%mod
        little[s]=small_fact
        iv=inv[s]
        H1=(H1+iv)%mod
        H2=(H2+iv*iv)%mod
        H3=(H3+iv*iv*iv)%mod
        h1[s]=H1;h2[s]=H2;h3[s]=H3
    pf=little[-1]
    for s in range(p):
        a=h1[s];b=h2[s];c=h3[s]
        jet=(1+p*a + p*p* ((a*a-b)*pow(2,-1,mod)%mod)
              +p**3*((a*a*a-3*a*b+2*c)*pow(6,-1,mod)%mod))%mod
        predicted=little[-1]*little[s]*jet%mod
        if s:
            pf=pf*(p+s)%mod
        assert predicted==pf,(p,s,predicted,pf)
    return True


def run(bound):
    cases=target_primes(bound)
    records=[]
    for p in cases:
        v=original_endpoint_mod_p4(p)
        records.append(v)
        independently=original_endpoint_by_independent_recurrence(p)
        if independently!=v['S_mod_p4']:
            raise AssertionError(f'independent recurrence mismatch p={p}: {independently} != {v["S_mod_p4"]}')
        if v['delta_mod_p'] is None:
            raise AssertionError(f'p^3 hard target failed at {p}')
    return records


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--limit',type=int,default=1000)
    parser.add_argument('--out',default='')
    args=parser.parse_args()
    data=run(args.limit)
    exc=[v['p'] for v in data if v['delta_mod_p']==0]
    print('prime_count',len(data),'p4_lifts',len(exc),'exceptional_primes',exc)
    print('initial',[(v['p'],v['delta_mod_p']) for v in data[:30]])
    v211=next((v for v in data if v['p']==211),None)
    if v211: print('p211',v211)
    if args.out:
        with open(args.out,'w',newline='',encoding='utf-8') as f:
            w=csv.DictWriter(f,fieldnames=list(data[0])); w.writeheader();w.writerows(data)
        print('wrote',args.out)
