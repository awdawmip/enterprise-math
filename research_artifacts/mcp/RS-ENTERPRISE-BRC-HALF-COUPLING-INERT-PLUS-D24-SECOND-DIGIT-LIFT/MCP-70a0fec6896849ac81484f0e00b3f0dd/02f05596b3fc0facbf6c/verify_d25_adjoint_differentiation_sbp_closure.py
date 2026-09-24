#!/usr/bin/env python3
"""Exact modular regression for the D25 adjoint-differentiation SBP closure.
Finite checking is falsification only; the companion note contains the proof.
"""
from math import isqrt

def primes_below(n):
    sieve=[True]*n
    if n>0: sieve[0]=False
    if n>1: sieve[1]=False
    for q in range(2,isqrt(n-1)+1):
        if sieve[q]:
            for k in range(q*q,n,q): sieve[k]=False
    return [q for q,ok in enumerate(sieve) if ok]

def check(p):
    m=(p-1)//6
    N=p-1
    inv=lambda x: pow(x%p,-1,p)
    c=[0]*(N+1); d=[0]*(N+1); e=[0]*(N+1)
    c[0]=1
    for k in range(N):
        b0=(k-m)*(k-2*m)
        b1=3*k-4*m
        den=inv((k+1)*(k+1))
        c[k+1]=c[k]*b0*den%p
        d[k+1]=(d[k]*b0+c[k]*b1)*den%p
        e[k+1]=(e[k]*b0+2*d[k]*b1+4*c[k])*den%p

    half=inv(2)
    lam=[0]*(p+1); l1=[0]*(p+1); l2=[0]*(p+1)
    lam[p]=pow(half,p,p)
    for k in range(N,0,-1):
        b0=(k-m)*(k-2*m)%p
        b1=(3*k-4*m)%p
        den=inv(k*k)
        lam[k]=(pow(half,k,p)+b0*lam[k+1])*den%p
        l1[k]=(b0*l1[k+1]+b1*lam[k+1])*den%p
        l2[k]=(b0*l2[k+1]+2*b1*l1[k+1]+4*lam[k+1])*den%p

    A=sum((3*j-4*m)*lam[j+1]*d[j] for j in range(0,2*m+1))%p
    A_sbp=sum((3*j-4*m)*l1[j+1]*c[j] for j in range(0,m+1))%p
    if A!=A_sbp:
        return ("FIRST_SBP",A,A_sbp)

    S=sum(lam[j+1]*(2*(3*j-4*m)*d[j]+4*c[j]) for j in range(0,2*m+1))%p
    S0=sum(c[j]*(2*(3*j-4*m)*l1[j+1]+4*lam[j+1]) for j in range(0,m+1))%p
    if S!=S0:
        return ("SOURCE_REDUCTION",S,S0)

    b00=(-m)*(-2*m)%p
    b10=(-4*m)%p
    endpoint=(b00*l2[1]+2*b10*l1[1]+4*lam[1])%p
    if S!=endpoint:
        return ("ENDPOINT_TELESCOPE",S,endpoint)

    F2=sum(e[k]*pow(half,k,p) for k in range(N+1))%p
    if F2!=(S-2)%p:
        return ("TERMINAL_RELATION",F2,(S-2)%p)
    return None

def main():
    targets=[p for p in primes_below(5000) if p%24 in (13,19)]
    failures=[]
    for p in targets:
        err=check(p)
        if err is not None: failures.append((p,err))
    print({"target_primes":len(targets),"class13":sum(p%24==13 for p in targets),"class19":sum(p%24==19 for p in targets),"failures":failures})
    if failures: raise SystemExit(1)

if __name__=="__main__": main()
