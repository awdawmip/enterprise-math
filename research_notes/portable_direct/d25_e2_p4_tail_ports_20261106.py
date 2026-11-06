#!/usr/bin/env python3
"""Independent exact p^4 source-separated tail-port checker, 2026-11-06.
Author-side portable research only; no native p373 H0/B0 experiment.
"""
from math import isqrt

def primes_upto(x):
    sieve=bytearray(b'\x01')*(x+1)
    sieve[:2]=b'\x00\x00'
    for k in range(2,isqrt(x)+1):
        if sieve[k]:
            sieve[k*k::k]=b'\x00'*(((x-k*k)//k)+1)
    return [n for n in range(7,x+1) if sieve[n] and n%6==1]

def check(p):
    m=(p-1)//6
    mod=p**4
    fac=[1]*p
    for n in range(1,p):
        fac[n]=fac[n-1]*n%p
    # Independent hypergeometric recurrence path.
    a=b=1
    W=V=0
    upper216=upperE2=0
    for n in range(p):
        wa=(6*n+1)*a%mod
        vb=(6*n+1)*b%mod
        W=(W+wa)%mod
        V=(V+vb)%mod
        if n>4*m:
            assert wa % p**3 == 0
            upper216=(upper216+wa//p**3)%p
        if n>2*m:
            assert vb % p**3 == 0
            upperE2=(upperE2+vb//p**3)%p
        if n<p-1:
            a=(a*(2*n+1)*(3*n+1)*(3*n+2)*pow(36*(n+1)**3,-1,mod))%mod
            b=(-b*(3*n+1)**3*pow(27*(n+1)**3,-1,mod))%mod
    # Independent factorial reflection path modulo p.
    c216=0
    for n in range(4*m+1,p):
        num=(fac[3*m]*fac[2*m]*fac[4*m]*fac[n-3*m-1]*fac[n-2*m-1]*fac[n-4*m-1])%p
        den=(9*pow(2,n,p)*pow(fac[n],3,p))%p
        c216=(c216+(6*n+1)*(-1)**m*num*pow(den,-1,p))%p
    cE2=0
    for n in range(2*m+1,p):
        num=fac[2*m]*fac[n-2*m-1]%p
        den=27*pow(fac[n],3,p)%p
        bn3=(-1)**n*pow(num,3,p)*pow(den,-1,p)%p
        cE2=(cE2+(6*n+1)*bn3)%p
    assert c216==upper216,(p,c216,upper216)
    assert cE2==upperE2==0,(p,cE2,upperE2)
    assert (W-V)%p**3==0,(p,W,V)
    return p,upper216,upperE2,((W-V)//p**3)%p,W,V

if __name__=="__main__":
    data=[check(p) for p in primes_upto(1999)]
    assert len(data)==148
    print("all primes:",len(data))
    print("target primes:",sum(p%24 in (13,19) for p,*_ in data))
    print("p^4 exact matches:",[p for p,_,_,delta,_,_ in data if delta==0])
    for row in data:
        if row[0] in (13,19,67,373):
            print("witness p, original-tail, E2-tail, delta, W, V:",row)
    print("PASS: full recurrence vs factorial reflection at 148 primes")
