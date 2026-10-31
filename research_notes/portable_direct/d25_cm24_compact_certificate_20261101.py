#!/usr/bin/env python3
"""Exact CM(-24) beta selector checks; finite checks are not a CM proof."""
from math import isqrt

def primes(n):
    a=bytearray(b'\1')*(n+1);a[:2]=b'\0\0'
    for d in range(2,isqrt(n)+1):
        if a[d]:a[d*d:n+1:d]=b'\0'*((n-d*d)//d+1)
    return [p for p in range(5,n+1) if a[p]]

def beta(p,mod):
    v=1;g=h=0;bs=[]
    for k in range(p):
        bs.append(v);g=(g+v)%mod;h=(h+(16*k+1)*v)%mod
        if k<p-1:
            v=v*(8*k+1)*(8*k+3)*pow(576*(k+1)**2,-1,mod)%mod
    return g,h,bs

def mul(a,b,p):return ((a[0]*b[0]+2*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def add(a,b,p):return ((a[0]+b[0])%p,(a[1]+b[1])%p)
def scale(a,b,p):return (a[0]*b%p,a[1]*b%p)
def qpow(a,n,p):
    v=(1,0)
    while n:
        if n&1:v=mul(v,a,p)
        a=mul(a,a,p);n>>=1
    return v

def hasse_check(p,g):
    m=(p-1)//2;n=m//2;f=[1]
    for j in range(1,m+1):f.append(f[-1]*j%p)
    v=[pow(x,-1,p) for x in f]
    hs=[f[m]*v[j]**2*v[m-2*j]*pow(2,m-2*j,p)%p for j in range(n+1)]
    pn=[1]
    for j in range(n):pn.append(pn[-1]*(-n+j)*(n+1+j)*pow((j+1)**2,-1,p)%p)
    assert hs==[pow(2,m,p)*x%p for x in pn],('Hasse coefficients',p)
    u=(pow(2,-1,p),-pow(3,-1,p)%p);t=(0,2*pow(3,-1,p)%p)
    val=(0,0)
    for c in reversed(hs):val=add(mul(val,u,p),(c,0),p)
    expected=scale(val,pow(pow(2,m,p),-1,p),p)
    if n&1:expected=mul(qpow(t,p,p),expected,p)
    assert expected==(g,0),('Hasse / beta observer',p,expected,g)
    return val==(0,0)

def tail(bs,p):
    m=p*p;s=[0]*(p+1);t=[0]*(p+1)
    for i in range(p-1,-1,-1):
        s[i]=(s[i+1]+bs[i])%m;t[i]=(t[i+1]+i*bs[i])%m
    return sum(bs[i]*((8*i+1)*s[p-i]+8*t[p-i]) for i in range(p))%m

ps=primes(5000);inert=0;tested=0;lift=0
for p in ps:
    g,h,_=beta(p,p)
    is_inert=pow((-6)%p,(p-1)//2,p)==p-1
    assert (g==0)==is_inert and (not is_inert or h!=0),('CM selector',p)
    inert+=is_inert
    if p<=997:
        assert hasse_check(p,g)==is_inert
        tested+=1
    if p<=1500 and p%24==19:
        gg,hh,bs=beta(p,p*p)
        assert tail(bs,p)==0 and gg%p==0 and hh%p!=0
        assert (gg//p)*(hh%p)%p==1,('p-linear lift',p)
        lift+=1
print('PASS CM selector',len(ps),'primes <=5000; inert',inert,'split',len(ps)-inert)
print('PASS exact Hasse coefficients and beta observer',tested,'primes <=997')
print('PASS p=19 mod24 unit inverse first lift and signed tail',lift,'primes <=1500')
