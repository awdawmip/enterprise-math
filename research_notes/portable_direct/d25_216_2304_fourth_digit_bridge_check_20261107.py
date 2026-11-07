#!/usr/bin/env python3
"""Exact finite tests; the fourth-digit relation is a conjecture, not a theorem."""
from math import comb, isqrt
def primes(bound):
    s=bytearray(b'\x01')*bound;s[0:2]=b'\x00\x00'
    for k in range(2,isqrt(bound-1)+1):
        if s[k]:s[k*k::k]=b'\x00'*len(s[k*k::k])
    return (p for p in range(5,bound) if s[p])
def recur(p,mod):
    a=b=1;W=V=0
    u=pow(216,-1,mod);v=pow(2304,-1,mod)
    for k in range(p):
        W=(W+(6*k+1)*a)%mod;V=(V+(8*k+1)*b)%mod
        if k==p-1:break
        t=k+1;inv=pow(t,-1,mod)
        a=a*(2*k+1)*(2*k+2)*(3*k+1)*(3*k+2)*(3*k+3)*u*pow(inv,5,mod)%mod
        b=b*(4*k+1)*(4*k+2)*(4*k+3)*(4*k+4)*v*pow(inv,4,mod)%mod
    return W,V
def direct(p,mod):
    x=y=0;a=b=1;u=pow(216,-1,mod);v=pow(2304,-1,mod)
    for k in range(p):
        c=comb(2*k,k)**2
        x=(x+(6*k+1)*c*comb(3*k,k)*a)%mod
        y=(y+(8*k+1)*c*comb(4*k,2*k)*b)%mod
        a=a*u%mod;b=b*v%mod
    return x,y
def run():
    n=small=plus=minus=0
    for p in primes(10000):
        mod=p**4;W,V=recur(p,mod);chi=1 if p%3==1 else -1
        assert (2*V-W-p*chi)%mod==0,p
        assert (V-p*chi)%(p**3)==0,p
        assert (W-p*chi)%(p**3)==0,p
        if p<=401:assert direct(p,mod)==(W,V),p;small+=1
        if chi==1:plus+=1
        else:minus+=1
        n+=1
    assert (n,plus,minus,small)==(1227,611,616,77)
    p=11;W,V=direct(p,p**5)
    assert (W,V)==(119779,103807)
    assert (2*V-W+p)%(p**5)==6*p**4
    print('p<5000',n,'chi=+',plus,'chi=-',minus,'independent',small,'failures',0)
    print('p11 p5 correction = 6*11^4 (nonzero)')
if __name__=='__main__':run()
