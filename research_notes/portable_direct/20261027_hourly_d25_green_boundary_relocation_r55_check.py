#!/usr/bin/env python3
"""Exact rational R55 Green-coefficient relocation checks (author verification)."""
from fractions import Fraction
from math import prod

def a(k):
    return Fraction((6*k+7)*(2*k+1)*(3*k+1)*(3*k+2),36*(6*k+1)*(k+1)**3)

def b(k):
    return Fraction((8*k+9)*(2*k+1)*(4*k+1)*(4*k+3),288*(8*k+1)*(k+1)**3)

def vp(x,p):
    n,d=x.numerator,x.denominator
    if n==0: return 10**9
    z=0
    while n%p==0: n//=p;z+=1
    while d%p==0: d//=p;z-=1
    return z

def check(p):
    N=(3*p-1)//4+1
    A=prod(a(k) for k in range(1,N))
    B=prod(b(k) for k in range(1,N))
    aa,bb=a(N),b(N)
    a1,b1=a(N+1),b(N+1)
    D=aa-bb
    D1=a1-b1
    beta=aa*a1-bb*b1
    gamma=aa*bb*D1
    assert vp(gamma,p)==0
    QN=(aa/B-bb/A)/D
    QN1=(1/A-1/B)/D
    assert QN+aa*QN1==1/A
    assert QN+bb*QN1==1/B
    shifted1=QN1+beta*QN/gamma
    shifted2=-D*QN/gamma
    Ap,Bp=A*aa,B*bb
    direct1=(a1/Bp-b1/Ap)/D1
    direct2=(1/Ap-1/Bp)/D1
    assert shifted1==direct1 and shifted2==direct2
    assert min(vp(shifted1,p),vp(shifted2,p))==-3
    if p in (139,199,277):
        assert (vp(QN,p),vp(QN1,p))==(-4,-4)
        assert vp(D,p)==1 and vp(D1,p)==0
    else:
        assert vp(D,p)==0 and vp(D1,p)==0
    return p,N,vp(QN,p),vp(QN1,p),vp(shifted1,p),vp(shifted2,p)

if __name__=='__main__':
    rows=[check(p) for p in (13,19,37,139,181,199,277,373)]
    for r in rows:
        print(r)
    print('PASS')
