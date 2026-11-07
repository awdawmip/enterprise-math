#!/usr/bin/env python3
"""Exact portable D25 reflected-R/kernel/Delta check; finite regression only."""
from fractions import Fraction
from math import comb, isqrt

def primes(n):
    return (p for p in range(5,n) if all(p%d for d in range(2,isqrt(p)+1)))

def check(p):
    m=(p-1)//6; mod=p**3
    b=1; first=[]; g=h=0
    for n in range(p):
        if n<=m: first.append(b%p)
        g=(g+b)%mod; h=(h+(12*n+1)*b)%mod
        if n<p-1:
            b=b*(6*n+1)*(3*n+1)*pow(36*(n+1)**2,-1,mod)%mod
    assert g%p==0
    product=((g//p)*h)%(p*p)
    assert (product-1)%p==0
    delta=(product-1)//p%p
    c=[0]*(m+1); c[1]=pow(10,-1,p)
    for r in range(1,m):
        c[r+1]=c[r]*36*r*r*pow((6*r+5)*(3*r+2),-1,p)%p
    direct=0; ct=0; s=prefix=0
    for i in range(1,m+1):
        original=sum((1+6*(i-r))*c[r] for r in range(1,i+1))%p
        direct=(direct+2*first[i]*original)%p
        s=(s+c[i]+6*prefix)%p; prefix=(prefix+c[i])%p
        q=comb(m,i)*comb(2*m,i)*pow(2,-i,p)%p
        assert q==first[i] and s==original
        ct=(ct+2*q*s)%p
        assert ((6*i-1)*(3*i-1)*c[i]-36*(i-1)**2*c[i-1])%p==(1 if i==1 else 0)
    assert delta==direct==ct,(p,delta,direct,ct)
    return delta,direct,ct

def exact(m):
    c=[Fraction(0),Fraction(1,10)]
    for r in range(1,m):c.append(c[-1]*Fraction(36*r*r,(6*r+5)*(3*r+2)))
    for i in range(1,m+1):
        v=sum((1+6*(i-r))*c[r] for r in range(1,i+1))
        recurrence=sum(c[r] for r in range(1,i+1))+6*sum((i-r)*c[r] for r in range(1,i+1))
        assert v==recurrence
        assert (6*i-1)*(3*i-1)*c[i]-(36*(i-1)**2*c[i-1] if i>1 else 0)==(1 if i==1 else 0)

if __name__=='__main__':
    ps=[p for p in primes(5000) if p%24 in (13,19)]
    for p in ps:check(p)
    for m in range(1,9):exact(m)
    for p in (13,19,43,67,373,997):print('sample',p,check(p))
    print('PASS',len(ps),'primes:',sum(p%24==13 for p in ps),'class 13;',sum(p%24==19 for p in ps),'class 19; exact m=1..8')
