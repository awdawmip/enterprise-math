#!/usr/bin/env python3
"""Exact portable CM(-24) branch checker. This is a concise reproducible checker."""
from fractions import Fraction as F
from math import comb
def qm(a,b):
    return (a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def qinv(a):
    d=a[0]*a[0]-2*a[1]*a[1]
    return (a[0]/d,-a[1]/d)
B=(F(1,8),F(1,12))
c=(F(1)-3*B[0],-3*B[1])
d=qm(qm(B,B),(F(1)-4*B[0],-4*B[1]))
j=qm(qm((F(256),F(0)),qm(qm(c,c),c)),qinv(d))
assert j==(F(2417472),F(-1707264))
assert 2*j[0]==4834944 and j[0]*j[0]-2*j[1]*j[1]==14670139392
def mul(x,y,p):
    return ((x[0]*y[0]+2*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
def pw(x,n,p):
    z=(1,0)
    while n:
        if n&1:z=mul(z,x,p)
        x=mul(x,x,p);n//=2
    return z
def Hdata(p):
    n=(p-1)//2; b=(pow(8,-1,p),pow(12,-1,p))
    H=(0,0);Hp=(0,0);power=(1,0);prev=(1,0)
    for k in range(n//2+1):
        coeff=comb(n,k)*comb(n-k,k)%p
        v=mul((coeff,0),power,p)
        H=((H[0]+v[0])%p,(H[1]+v[1])%p)
        if k:
            v=mul((k*coeff,0),prev,p)
            Hp=((Hp[0]+v[0])%p,(Hp[1]+v[1])%p)
        prev=power;power=mul(power,b,p)
    return H,Hp
def rprime(p):
    m=(p-3)//8; h=1; result=0
    for k in range(2*m+1):
        result=(result+(8*k+5)*h*pow(9,2*m+k,p))%p
        if k<2*m:h=h*(4*k+3)**3*pow((4*k+4)*(4*k+5)*(4*k+6),-1,p)%p
    return result
def isprime(p):
    if p<2:return False
    for d in range(2,int(p**.5)+1):
        if p%d==0:return False
    return True
seen={11:0,19:0}
for p in range(11,4000,8):
    if not isprime(p):continue
    H,Hp=Hdata(p)
    K=(4*pow(3,-1,p)*Hp[1]-8*H[0])%p
    assert H[1]==0 and Hp[0]==0 and rprime(p)==0
    if p%24==19:assert H==(0,0) and Hp[1]!=0 and K!=0
    else:assert p%24==11 and H[0]!=0 and K==0
    seen[p%24]+=1
def trace_q(p):
    q=p*p; B=(pow(8,-1,p),pow(12,-1,p)); s=0
    for a in range(p):
        for b in range(p):
            x=(a,b);xx=mul(x,x,p)
            t=mul(x,((xx[0]+a+B[0])%p,(xx[1]+b+B[1])%p),p)
            if t==(0,0):continue
            v=pw(t,(q-1)//2,p)
            assert v in ((1,0),(p-1,0))
            s+=1 if v==(1,0) else -1
    return -s
counts={}
for p in (11,19,43,59,67,83,107,139,163,283):
    t=trace_q(p);H,_=Hdata(p)
    assert t%p==H[0]**2%p
    if p%24==19:assert t==2*p
    counts[p]=t
assert Hdata(3347)==((783,0),(0,1351))
print("PASS_CM24_PORTABLE_EXACT",seen,counts,"p3347_H=783,Hprime=1351rho")
