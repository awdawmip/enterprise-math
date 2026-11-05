#!/usr/bin/env python3
"""Finite Clausen-square truncation high-tail source, exact Z/p^3Z checks."""
from math import isqrt


def primes_upto(n):
    s=bytearray(b'\x01')*(n+1);s[:2]=b'\x00\x00'
    for i in range(2,isqrt(n)+1):
        if s[i]:s[i*i::i]=b'\x00'*len(s[i*i::i])
    return [i for i in range(5,n+1) if s[i] and i%8==5]


def check(p):
    mod=p**3
    g=[1]
    for k in range(1,p):
        g.append(g[-1]*(8*k-7)*(8*k-5)*pow(576*k*k,-1,mod)%mod)
    F=sum(g)%mod
    D=sum(k*v for k,v in enumerate(g))%mod
    prod=F*(F+16*D)%mod
    b=1;V=0
    for k in range(p):
        V=(V+(8*k+1)*b)%mod
        if k<p-1:
            b=b*(4*k+1)*(4*k+2)*(4*k+3)*(4*k+4)*pow(2304*(k+1)**4,-1,mod)%mod
    # Evaluate the upper strip of the square after applying the weighted 1+8theta observer.
    T=0
    for i in range(p):
        a=g[i]
        for j in range(p-i,p):
            T=(T+(8*(i+j)+1)*a*g[j])%mod
    assert (V+T-prod)%mod==0,(p,'Clausen tail')
    chi=1 if p%3==1 else -1
    assert V==p*chi%mod,(p,'known quartic benchmark')
    split=(p%24==5)
    selected=(F+16*D)%mod if split else F
    assert selected%p**2==0,(p,'finite selected factor')
    assert prod%p**2==0
    assert T%p==0
    assert T//p%p==(-chi)%p
    return dict(p=p,chi=chi,F=F,D=D,selected=selected,V=V,T=T,T_over_p=T//p%p,prod=prod,prod_over_p2=prod//(p*p))

if __name__=='__main__':
    ps=primes_upto(373)
    rows=[check(p) for p in ps]
    print('PASS finite_clausen_tail primes',len(rows),'quartic modp3 and tail modp2')
    for row in rows:
        if row['p'] in (5,13,29,37,53,61,101,149,373): print('CASE',row)
