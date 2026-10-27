#!/usr/bin/env python3
"""Exact author checks for D25 R47/R48; no native execution claim."""
from fractions import Fraction as Q
from math import factorial

def primes(n):
    a=[True]*(n+1);a[0:2]=[False,False]
    for i in range(2,int(n**.5)+1):
        if a[i]:
            for j in range(i*i,n+1,i):a[j]=False
    return [p for p in range(7,n+1) if a[p] and p%6==1]

def w(k):
    return Q((6*k+1)*factorial(2*k)*factorial(3*k),factorial(k)**5*216**k)

def s(k):
    return Q((8*k+1)*factorial(4*k),factorial(k)**4*2304**k)

def A(k):
    return Q((6*k+7)*(2*k+1)*(3*k+1)*(3*k+2),36*(6*k+1)*(k+1)**3)

def B(k):
    return Q((8*k+9)*(2*k+1)*(4*k+1)*(4*k+3),288*(8*k+1)*(k+1)**3)

def P(k):
    return 2688*k**4+6160*k**3+4456*k**2+1166*k+85

def vp(n,p):
    e=0
    while n and n%p==0:n//=p;e+=1
    return e

def endpoint(p):
    nmax=4*(p-1);u=[1]*(nmax+1);e=[0]*(nmax+1)
    for n in range(1,nmax+1):
        t=n
        while t%p==0:t//=p;e[n]+=1
        e[n]+=e[n-1]
        u[n]=(u[n-1]*t)%p
    k=p-1
    vw=e[2*k]+e[3*k]-5*e[k]+vp(6*k+1,p)
    vs=e[4*k]-4*e[k]+vp(8*k+1,p)
    uw=(6*k+1)*u[2*k]*u[3*k]*pow(u[k],-5,p)*pow(216,-k,p)%p
    us=(8*k+1)*u[4*k]*pow(u[k],-4,p)*pow(2304,-k,p)%p
    return vw,vs,uw,us

def check():
    for k in range(35):
        a,b=A(k),B(k)
        det=Q((2*k+1)*P(k),288*(k+1)**3*(6*k+1)*(8*k+1))
        assert a-b==det and det>0
        assert w(k+1)==a*w(k) and s(k+1)==b*s(k)
        d=w(k)-s(k);dn=w(k+1)-s(k+1)
        assert (dn-b*d)/det==w(k) and (dn-a*d)/det==s(k)
        dnn=w(k+2)-s(k+2)
        assert det*dnn-(a*A(k+1)-b*B(k+1))*dn+a*b*(A(k+1)-B(k+1))*d==0
    assert w(1)-s(1)==Q(85,288)
    ps=primes(997);positions=0;excluded=0
    for p in ps:
        assert 85%p and 288%p
        H=(3*p-1)//4
        for k in range(H+1,p):
            assert 2*k//p+3*k//p+vp(6*k+1,p)==3
            assert 4*k//p+vp(8*k+1,p)>=3
            positions+=1
        vw,vs,uw,us=endpoint(p)
        assert vw==3 and vs==(5 if p==7 else 3)
        assert (uw,us)==(5%p,7%p) and (uw-us)%p==(-2)%p
        c=85*pow(288,-1,p)*pow(2,-1,p)%p
        assert c!=0 and (85*pow(288,-1,p)-2*c)%p==0
        for k in range(min(23,p//4)+1):
            a,b=A(k),B(k)
            if any(t.denominator%p==0 for t in (a,b,a-b)) or P(k)%p==0:
                excluded+=1;continue
            def mq(t):return t.numerator*pow(t.denominator,-1,p)%p
            d=w(k)-s(k);dn=w(k+1)-s(k+1)
            assert mq((dn-b*d)/(a-b))==mq(w(k))
            assert mq((dn-a*d)/(a-b))==mq(s(k))
    print("PASS 35 exact rank checks; %d primes; %d high-high positions; endpoint 5/7/-2; %d modular exclusions" %(len(ps),positions,excluded))

if __name__=="__main__":check()
