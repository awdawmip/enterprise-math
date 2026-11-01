#!/usr/bin/env python3
"""Exact modular p-adic Hadamard bridge checks; no floats or simulated native H0/B0."""
from fractions import Fraction
from math import isqrt


def primes(limit):
    t = bytearray(b"\x01") * (limit+1)
    t[:2] = b"\x00\x00"
    for d in range(2, isqrt(limit)+1):
        if t[d]:
            t[d*d::d] = b"\x00" * len(t[d*d::d])
    return [i for i in range(2,limit+1) if t[i]]


def term(x,p):
    v=0
    while x%p==0:
        x//=p
        v+=1
    return v,x%p


def step(value, factors_num, factors_den, p):
    v,u=value
    for x in factors_num:
        a,b=term(x,p)
        v+=a
        u=u*b%p
    for x in factors_den:
        a,b=term(x,p)
        v-=a
        u=u*pow(b,-1,p)%p
    return (v,u)


def predicted(p,n):
    r,s=(p-1)//6,(p-1)//3
    if p%24==13:
        a,b=(5*p-1)//8,(7*p-3)//8
        assert r<s<a<b<p
        return int(n>a)+int(n>b)-int(n>r)-int(n>s)
    a,b=(p-3)//8,(3*p-1)//8
    assert a<r<s<b<p
    return int(n>a)+int(n>b)-int(n>r)-int(n>s)


def check(p):
    # Maintain valuation and p-adic unit separately even across denominator p-factors.
    y=b=h=(0,1)
    hmin=0
    for n in range(p+1):
        assert y[0]+h[0]==b[0] and y[1]*h[1]%p==b[1],(p,n,y,b,h)
        if n<p:
            assert h[0]==predicted(p,n),(p,n,h)
            hmin=min(hmin,h[0])
        if n==p-1:
            assert y[0]==b[0]==2
            assert y[1]==pow(10,-1,p)
        if n==p:
            alpha=next(i for i in (1,3,5,7) if (i*p-1)%8==0)
            beta=next(i for i in (1,3,5,7) if (i*p-3)%8==0)
            assert h[0]==0
            assert h[1]==9*alpha*beta*pow(32,-1,p)%p
            ea=-pow(18,-1,p)%p
            eb=-alpha*beta*pow(64,-1,p)%p
            assert ea*h[1]%p==eb
            assert hmin==(-2 if p%24==13 else -1)
            return p,h[1],ea,eb,hmin
        y=step(y,[6*n+1,3*n+1],[18,n+1,n+1],p)
        b=step(b,[8*n+1,8*n+3],[64,n+1,n+1],p)
        h=step(h,[9,8*n+1,8*n+3],[32,6*n+1,3*n+1],p)


def check_fraction(p):
    y=b=h=Fraction(1)
    for n in range(p):
        assert y*h==b
        hnext=h*Fraction(9*(8*n+1)*(8*n+3),32*(6*n+1)*(3*n+1))
        assert (n+Fraction(1,6))*(n+Fraction(1,3))*hnext == h*(n+Fraction(1,8))*(n+Fraction(3,8))
        y*=Fraction((6*n+1)*(3*n+1),18*(n+1)**2)
        b*=Fraction((8*n+1)*(8*n+3),64*(n+1)**2)
        h=hnext
    assert y*h==b
    ya=y/Fraction((6*(p-1)+1)*(3*(p-1)+1),18*p*p)
    bb=b/Fraction((8*(p-1)+1)*(8*(p-1)+3),64*p*p)
    ea=-(p-Fraction(5,6))*(p-Fraction(2,3))*ya
    eb=-(p-Fraction(7,8))*(p-Fraction(5,8))*bb
    assert eb==ea*h


if __name__=="__main__":
    rows=[check(p) for p in primes(3000) if p%24 in (13,19)]
    assert len(rows)==107
    assert sum(p%24==13 for p,*_ in rows)==53
    assert sum(p%24==19 for p,*_ in rows)==54
    for p in (13,19,37,61): check_fraction(p)
    print("PASS: 107/107 primes through 3000; 53 class13 and 54 class19")
    print("PASS: exact five-band valuations; independent u,b,h valuations and units")
    print("PASS: p-terminal source bridge and all four Fraction spot checks")
    for row in rows:
        if row[0] in (13,19,37,61,109,373): print("WITNESS",row)
