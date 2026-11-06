#!/usr/bin/env python3
"""Exact p-adic source-coefficient vs mixed-jet carry certificate, author-side."""
from math import comb

def primes(n):
    a=bytearray(b'\x01')*(n+1);a[:2]=b'\x00\x00'
    for k in range(2,int(n**0.5)+1):
        if a[k]: a[k*k::k]=b'\x00'*((n-k*k)//k+1)
    return [p for p in range(7,n+1) if a[p] and p%6==1]

def test(p):
    m=(p-1)//6
    s=(2*m,3*m,4*m); v=(-pow(3,-1,p),-pow(2,-1,p),-2*pow(3,-1,p))
    fac=[1]*p;invfac=[1]*p
    for j in range(1,p):fac[j]=fac[j-1]*j%p
    invfac[-1]=pow(fac[-1],-1,p)
    for j in range(p-1,0,-1):invfac[j-1]=invfac[j]*j%p
    N=p**4
    h=1
    counts=[0,0,0,0]
    leading_sums=[0,0,0,0]
    for j in range(p):
        carry=sum(j>x for x in s)
        assert h%(p**carry)==0,(p,j,carry)
        expected=pow(-2,-j,p)
        for index,x in enumerate(s):
            if j<=x:
                c=comb(x,j)%p
            else:
                c=fac[x]*fac[j-x-1]*invfac[j]%p
                if (j-x-1)%2:c=(-c)%p
                c=c*v[index]%p
            expected=expected*c%p
        observed=(h//p**carry)%p
        assert observed==expected,(p,j,carry,observed,expected)
        assert observed!=0,(p,j,'leading coefficient vanished')
        counts[carry]+=1
        leading_sums[carry]=(leading_sums[carry]+(6*j+1)*observed)%p
        if j+1<p:
            h=h*(2*j+1)*(3*j+1)*(3*j+2)*pow(36*(j+1)**3,-1,N)%N
    return counts,leading_sums

if __name__=='__main__':
    ps=primes(3000)
    for p in ps:
        counts,sums=test(p)
        if p in (7,13,19,31,373,1009):print('p=%d shells=%s leading_weighted_modp=%s'%(p,counts,sums))
    print('PASS: %d primes p=1(mod6), p<=3000; all j<p, four source carry layers and leading coefficients.'%len(ps))
