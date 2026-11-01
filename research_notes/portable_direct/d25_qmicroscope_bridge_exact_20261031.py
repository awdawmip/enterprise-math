#!/usr/bin/env python3
"""Exact finite p³ comparator: weighted-216 D25 vs Guo–Zudilin weighted-2304.
Run: python d25_qmicroscope_bridge_exact_20261031.py 15000
Only finite mathematical evidence; NOT an all-prime bridge theorem.
"""
from math import comb, isqrt
from hashlib import sha256

def primes_up_to(n):
    sieve=bytearray(b"\x01")*(n+1)
    sieve[:2]=b"\x00\x00"
    for q in range(2,isqrt(n)+1):
        if sieve[q]:
            sieve[q*q::q]=b"\x00"*((n-q*q)//q+1)
    return [q for q in range(5,n+1) if sieve[q]]

def evaluate(p):
    m=p**3
    inv=[0]*p
    inv[1]=1
    for k in range(2,p):
        inv[k]=(-(m//k)*inv[m%k])%m
        assert k*inv[k]%m==1
    a=b=1
    A=B=1
    Ah=Bh=None
    half=(p-1)//2
    for k in range(1,p):
        j=k-1
        v=pow(inv[k],3,m)
        a=a*(2*j+1)*(3*j+1)*(3*j+2)*pow(36,-1,m)*v%m
        b=b*(4*j+1)*(2*j+1)*(4*j+3)*pow(288,-1,m)*v%m
        A=(A+(6*k+1)*a)%m
        B=(B+(8*k+1)*b)%m
        if k==half:
            Ah,Bh=A,B
    return A,B,Ah,Bh

def direct_original(p):
    m=p**3
    u=pow(216,-1,m)
    power=1
    total=0
    for k in range(p):
        total=(total+(6*k+1)*comb(2*k,k)**2*comb(3*k,k)*power)%m
        power=power*u%m
    return total

def direct_comparator(p):
    m=p**3
    u=pow(2304,-1,m)
    power=1
    total=0
    for k in range(p):
        total=(total+(8*k+1)*comb(4*k,2*k)*comb(2*k,k)**2*power)%m
        power=power*u%m
    return total

def main(limit=15000):
    ps=primes_up_to(limit)
    targets=0
    digest=sha256()
    rows={}
    for p in ps:
        A,B,Ah,Bh=evaluate(p)
        char=1 if p%3==1 else -1
        assert A==B==Bh==(p*char)%(p**3), (p,A,B,Ah,Bh)
        targets+=p%24 in (13,19)
        digest.update(f"{p},{A},{B},{Ah},{Bh};".encode())
        if p in (5,7,13,19,31,37,67,373,997,14983):
            rows[p]=(A,B,Ah,Bh,(A-Ah)%(p**3))
    for p in (5,7,13,19,31,37,67):
        a,b,_,_=evaluate(p)
        assert a==direct_original(p)
        assert b==direct_comparator(p)
    print("primes",len(ps),"frozen-target",targets)
    print("SHA256 witness:",digest.hexdigest())
    for p,row in rows.items():
        print(p,row)
    print("FINITE_EXACT_CHECK_ONLY / BRIDGE_UNPROVED / NATIVE_NOT_EXECUTED")

if __name__=="__main__":
    import sys
    main(int(sys.argv[1]) if len(sys.argv)>1 else 15000)
