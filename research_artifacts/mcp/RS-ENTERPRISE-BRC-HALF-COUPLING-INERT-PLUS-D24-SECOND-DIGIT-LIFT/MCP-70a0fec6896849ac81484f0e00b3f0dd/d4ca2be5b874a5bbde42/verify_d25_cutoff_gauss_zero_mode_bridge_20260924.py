#!/usr/bin/env python3
"""Regression for the D25 cutoff finite-Gauss zero-mode bridge.
Finite checking is falsification only; the companion note contains the proof.
"""
from math import isqrt

def primes_below(n):
    s=[True]*n
    if n: s[0]=False
    if n>1: s[1]=False
    for q in range(2,isqrt(n-1)+1):
        if s[q]:
            for k in range(q*q,n,q): s[k]=False
    return [q for q,ok in enumerate(s) if ok]

def check(p):
    m=(p-1)//6
    M=p**3
    p2=p*p
    inv=lambda x,mod: pow(x%mod,-1,mod)

    c0=[0]*p; c1=[0]*p; c2=[0]*p
    c0[0]=1
    for k in range(p-1):
        den=inv((k+1)*(k+1),M)
        r0=(k-m)*(k-2*m)
        r1=3*k-4*m
        c0[k+1]=c0[k]*r0*den%M
        c1[k+1]=(c1[k]*r0+c0[k]*r1)*den%M
        c2[k+1]=(c2[k]*r0+2*c1[k]*r1+4*c0[k])*den%M

    F0=F1=F2=F2T=Psi=H1=H1T=0
    z=1
    half=inv(2,M)
    for k in range(p):
        if k: z=z*half%M
        F0=(F0+c0[k]*z)%M
        F1=(F1+c1[k]*z)%M
        F2=(F2+c2[k]*z)%M
        if k<=2*m: F2T=(F2T+c2[k]*z)%M
        w=12*k+1
        Psi=(Psi+w*c0[k]*z)%M
        H1=(H1+w*c1[k]*z)%M
        if k<=m: H1T=(H1T+w*c1[k]*z)%M

    assert F0%p==0
    aparent=(F0//p + (F1%p2)*inv(6,p2))%p2
    prod=(aparent*(Psi%p2)-1)%p2
    assert prod%p==0
    product_digit=(prod//p)%p
    zjet=(product_digit
          +(aparent%p)*(H1T%p)*inv(6,p)
          +(Psi%p)*(F2T%p)*inv(72,p))%p

    B=[1]; cur=1
    for k in range(p-1):
        cur=cur*((6*k+1)*(3*k+1)%M)*inv(36*(k+1)*(k+1),M)%M
        B.append(cur)
    g=sum(B)%M
    S=sum(B[:2*m+1])%M
    assert g%p==0 and S%p==0
    GT=(S//p)%p2
    HU=sum((12*k+1)*B[k] for k in range(m+1))%p2
    zn=(GT*HU-1)%p2
    assert zn%p==0
    ZT=(zn//p)%p

    A=0
    for r in range(1,m+1):
        k=m+r
        assert B[k]%p==0
        A=(A+(12*r-1)*((B[k]//p)%p))%p
    Y=0
    for k in range(2*m+1,p):
        assert B[k]%p2==0
        Y=(Y+B[k]//p2)%p

    Ajet=((H1-H1T)%p)*inv(6,p)%p
    Yjet=((F2-F2T)%p)*inv(72,p)%p

    h=sum((12*k+1)*B[k] for k in range(p))%p2
    G=(g//p)%p2
    dn=(G*h-1)%p2
    assert dn%p==0
    Delta=(dn//p)%p
    globaljet=(product_digit
               +(aparent%p)*(H1%p)*inv(6,p)
               +(Psi%p)*(F2%p)*inv(72,p))%p

    assert ZT==zjet
    assert A==Ajet
    assert Y==Yjet
    assert Delta==globaljet
    assert Delta==(ZT+(aparent%p)*A+(Psi%p)*Y)%p

def main():
    T=[p for p in primes_below(5000) if p%24 in (13,19)]
    failures=[]
    for p in T:
        try: check(p)
        except Exception as e: failures.append((p,repr(e)))
    print({"targets":len(T),
           "class13":sum(p%24==13 for p in T),
           "class19":sum(p%24==19 for p in T),
           "failures":failures})
    if failures: raise SystemExit(1)

if __name__=="__main__": main()
