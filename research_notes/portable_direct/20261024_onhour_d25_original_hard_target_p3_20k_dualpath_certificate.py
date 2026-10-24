#!/usr/bin/env python3
"""D25 direct original hard-target finite certificate, author-side exact arithmetic.

Verifies the p^3 statement for every prime p<=BOUND with p mod 24 in {13,19}
by two algebraically identical, computationally independent source-faithful
representations: original term recurrence vs closed factorial summand.

The certificate does NOT substitute native benchmark, Source admission,
independent replication or an infinite-prime proof.
"""
from hashlib import sha256
from math import isqrt
from pathlib import Path
import csv
import sys
import time

def prime_list(bound):
    sieve=bytearray(b'\x01')*(bound+1)
    sieve[:2]=b'\x00\x00'
    for d in range(2,isqrt(bound)+1):
        if sieve[d]: sieve[d*d:bound+1:d]=b'\x00'*((bound-d*d)//d+1)
    return [x for x in range(7,bound+1) if sieve[x] and x%24 in (13,19)]


def strip(x,p):
    e=0
    while x%p==0:
        x//=p;e+=1
    return x,e


def exact_residue(p,return_detail=False):
    m=(p-1)//6; M=p**3
    # Original A_m factorial ratio (all factors are p-units).
    f2=f6=1
    for j in range(1,6*m+1):
        f6=(f6*j)%M
        if j==2*m: f2=f6
    A=f6*pow((pow(3,6*m,M)*pow(f2,3,M))%M,-1,M)%M
    Runit=1; v=0; total=0
    hist={}; nfirst=None; nlast=None
    for n in range(4*m+1):
        t=(A*(6*n+12*m+1)*Runit)%M
        if v<0: raise ValueError(('negative valuation',p,n,v))
        t=t*(p**min(v,3))%M
        total=(total+t)%M
        hist[v]=hist.get(v,0)+1
        if n<4*m:
            num=(4*m+2*n+1,3*n+1,3*n+2)
            den=(36,n+1,2*m+n+1,4*m+n+1)
            en=ed=0; un=ud=1
            for x in num:
                z,e=strip(x,p);un=(un*z)%M;en+=e
            for x in den:
                z,e=strip(x,p);ud=(ud*z)%M;ed+=e
            v+=en-ed
            Runit=(Runit*un*pow(ud,-1,M))%M
    target=p*pow(4*pow(3,-1,M)%M,p-1,M)%M
    diff=(total-target)%M
    if return_detail: return {'p':p,'m':m,'S':total,'target':target,'diff':diff,'valuation_hist':hist}
    return diff


def factorial_residue(p):
    """Independent closed factorial R formula; no term-to-term hypergeometric recursion.

    R_{m,n} = (4m+2n)! (2m)!^2 (3n)! /
       (216^n (2m+n)!^2 (4m+n)! (n!)^2).
    For n<=4m every factorial index <=2p-2, so factorial valuation is
    exactly 0 or 1 and the unique p-factor can be stripped explicitly.
    """
    m=(p-1)//6;M=p**3
    N=12*m
    F=[1]*(N+1)
    for k in range(1,N+1):
        F[k]=F[k-1]*(k//p if k==p else k)%M
    FI=[1]*(N+1);FI[N]=pow(F[N],-1,M)
    for k in range(N,0,-1):
        FI[k-1]=FI[k]*(k//p if k==p else k)%M
    A=F[6*m]*pow(FI[2*m],3,M)*pow(3,-6*m,M)%M
    f2square=F[2*m]*F[2*m]%M
    inv216=pow(216,-1,M)
    z=1;s=0
    for n in range(4*m+1):
        unit=F[4*m+2*n]*f2square*F[3*n]%M
        unit=unit*FI[2*m+n]**2*FI[4*m+n]*FI[n]**2%M
        unit=unit*z%M
        if n>m:unit=unit*p%M
        s=(s+A*(6*n+12*m+1)*unit)%M
        z=z*inv216%M
    return s


def certify(bound, out=None):
    start = time.monotonic()
    primes = prime_list(bound)
    rows = []
    for p in primes:
        obj = exact_residue(p, return_detail=True)
        other = factorial_residue(p)
        assert obj["S"] == other, ("independent mismatch", p)
        m = (p-1)//6
        assert obj["valuation_hist"] == {0:m+1, 1:3*m}, ("support mismatch", p)
        assert obj["diff"] == 0, ("hard target fails", p, obj)
        rows.append((p, m, obj["S"], other, obj["target"], obj["diff"]))
    assert rows == sorted(rows) and len(rows) == len(primes)
    data = ''.join(f'{p},{m},{r},{t},{d}\n' for p,m,r,_other,t,d in rows)
    digest = sha256(data.encode('ascii')).hexdigest()
    if out is not None:
        path = Path(out)
        with path.open('w', newline='', encoding='utf-8') as f:
            w = csv.writer(f, lineterminator='\n')
            w.writerow(("p", "m", "S_recurrence", "S_factorial", "target", "difference_mod_p3"))
            w.writerows(rows)
    print("BOUND",bound,"PRIMES",len(rows),"p13",sum(p%24==13 for p in primes),
          "p19",sum(p%24==19 for p in primes),"ALL_EXACT_PASS",True)
    print("ROW_DIGEST_SHA256",digest,"SECONDS",round(time.monotonic()-start,2))
    if 211 in primes:
        x=rows[primes.index(211)]
        print("p211",x)
    print("FIRST_LAST", rows[0],rows[-1])
    return rows, digest

if __name__ == "__main__":
    bound=int(sys.argv[1]) if len(sys.argv)>1 else 20000
    outfile=sys.argv[2] if len(sys.argv)>2 else None
    certify(bound,outfile)
