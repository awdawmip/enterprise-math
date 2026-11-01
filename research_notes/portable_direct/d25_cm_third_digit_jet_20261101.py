#!/usr/bin/env python3
"""Portable exact audit: D25 universal terminal source and CM third-digit jet."""
from math import isqrt

def primes(limit):
    s=[True]*(limit+1); s[0]=s[1]=False
    for i in range(2,isqrt(limit)+1):
        if s[i]:
            for k in range(i*i,limit+1,i): s[k]=False
    return [i for i in range(13,limit+1) if s[i]]

def coeffs(p,m):
    out=[1]
    for k in range(1,p):
        out.append(out[-1]*(8*k-7)*(8*k-5)*pow(64*k*k,-1,m)%m)
    return out

def horner(c,z,m):
    f=d=dd=0
    for a in reversed(c):
        dd=(dd*z+2*d)%m; d=(d*z+f)%m; f=(f*z+a)%m
    return f,d,dd

def neighbor(p,m):
    # P_(n-1)((2/3)s), s²=2, in (Z/mZ)[s]/(s²-2).
    n=(p-1)//4; x=2*pow(3,-1,m)%m
    if n==1: return 1
    prev=(1,0); cur=(0,x)
    for k in range(1,n-1):
        xcur=(2*x*cur[1]%m,x*cur[0]%m)
        inv=pow(k+1,-1,m)
        nxt=(((2*k+1)*xcur[0]-k*prev[0])*inv%m,
             ((2*k+1)*xcur[1]-k*prev[1])*inv%m)
        prev,cur=cur,nxt
    assert cur[1]%m==0
    return cur[0]

def universal(p):
    m=p**3; c=coeffs(p,m); assert c[-1]==p*p
    for z in (pow(9,-1,m),2):
        f,d,dd=horner(c,z,m)
        L=(z*(1-z)*dd+(1-3*z*pow(2,-1,m))*d-3*pow(64,-1,m)*f)%m
        rhs=-35*pow(64,-1,m)*p*p*pow(z,p-1,m)%m
        assert L==rhs,(p,z,L,rhs)

def cm(p):
    m=p**3; lam=pow(9,-1,m); c=coeffs(p,m)
    f,d,dd=horner(c,lam,m)
    assert f%p==0
    assert dd%p==(-135*pow(16,-1,p)*d)%p
    B=neighbor(p,p*p); assert d%p==(-9*pow(8,-1,p)*B)%p
    D=(d%(p*p)+9*pow(8,-1,p*p)*B)%(p*p)
    assert D%p==0; D=(D//p)%p
    q=((pow(9,p-1,m)-1)%m)//p
    f2,_,_=horner(c,pow(lam,p,m),m)
    diff=(f2-f)%m
    rhs=p*pow(8,-1,m)*q*B-p*p*(pow(9,-1,m)*q*D+
                                    17*pow(256,-1,m)*q*q*B)
    assert diff==rhs%m,(p,diff,rhs%m)
    carry=((diff-p*pow(8,-1,m)*q*B)%m)//(p*p)
    port1=(-pow(9,-1,p)*q*D)%p
    port2=(-17*pow(256,-1,p)*q*q*B)%p
    assert (port1+port2)%p==carry
    return p,B,D,carry,port1,port2

def main():
    pp=primes(3000); eligible=[p for p in pp if p%8==5]
    for p in eligible: universal(p)
    print('PASS_UNIVERSAL_P3_TERMINAL',len(eligible))
    target=[cm(p) for p in pp if p%24==13]
    print('PASS_CM_THIRD_DIGIT_FORMULA',len(target))
    for row in target:
        if row[0] in (13,37,61,109,373):print('CERT',row)

if __name__=='__main__': main()
