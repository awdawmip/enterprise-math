#!/usr/bin/env python3
"""Exact auxiliary CM(-24) second-digit inversion certificate; no external dependencies."""
from math import isqrt

def primes(n):
    s=bytearray(b'\x01')*(n+1);s[:2]=b'\x00\x00'
    for j in range(2,isqrt(n)+1):
        if s[j]:s[j*j:n+1:j]=b'\x00'*((n-j*j)//j+1)
    return [i for i in range(5,n+1) if s[i] and i%8==5]

def red(a,p):
    x=[v%p for v in a];x += [0]*max(0,4-len(x))
    for j in range(len(x)-1,3,-1):
        v=x[j];x[j]=0
        x[j-1]=(x[j-1]+140*v)%p;x[j-2]=(x[j-2]-294*v)%p
        x[j-3]=(x[j-3]+140*v)%p;x[j-4]=(x[j-4]-v)%p
    return tuple(x[:4])

def mul(a,b,p):
    c=[0]*7
    for i in range(4):
        for j in range(4):c[i+j]+=a[i]*b[j]
    return red(c,p)

def pw(a,n,p):
    r=(1,0,0,0)
    while n:
        if n&1:r=mul(r,a,p)
        a=mul(a,a,p);n//=2
    return r

def ev(a,z,p):
    r=(0,0,0,0)
    for c in reversed(a):
        b=list(mul(r,z,p));b[0]=(b[0]+c)%p;r=tuple(b)
    return r

def check(p):
    m=(p-1)//2;mod=p*p;h=[0]*(m+3);b=1
    for j in range(m+1):
        if j:b=b*(m-j+1)*pow(j,-1,mod)%mod
        h[j]=b*b%mod
    c=[0]*(m+3)
    for j in range(m+3):
        c[j]=((16*j+1)*h[j]+(2*h[j-1] if j>=1 else 0)
             -((16*j-25)*h[j-2] if j>=2 else 0))%mod
    for j in range(m+3):
        assert (c[m+2-j]-c[j]-8*p*((h[j-2] if j>=2 else 0)-h[j]))%mod==0
        assert (c[m+2-j]-8*p*h[m+2-j]-c[j]+8*p*h[j])%mod==0
    if p%24!=5:return None
    r=red(c,mod)
    assert all(v%p==0 for v in r)
    T=tuple(v//p%p for v in r);H=red(h,p)
    t=(0,1,0,0);inv=tuple(v%p for v in (140,-294,140,-1))
    assert mul(t,inv,p)==(1,0,0,0)
    wt=pw(t,m+2,p)
    L=mul(wt,ev(T,inv,p),p)
    S=mul(((-8)%p,0,8%p,0),H,p)
    assert tuple((L[j]-T[j])%p for j in range(4))==S
    fixed=tuple((T[j]-8*H[j])%p for j in range(4))
    assert mul(wt,ev(fixed,inv,p),p)==fixed
    assert T!=(0,0,0,0)
    return (T,H,fixed)

if __name__=='__main__':
    xs=primes(5000);sn=0
    for p in xs:
        a=check(p)
        if a:sn+=1
        if p in [5,29,53]:print('PORT',p,a)
    assert len(xs)==168 and sn==85
    print('PASS',len(xs),'primes',sn,'split',len(xs)-sn,'inert')
