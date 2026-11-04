#!/usr/bin/env python3
"""Exact p-adic signed jet and 3rd Sun defect coefficient. Author-side, not native H0/B0."""
from math import comb
from fractions import Fraction
import json

def add(a,b,m):return ((a[0]+b[0])%m,(a[1]+b[1])%m)
def neg(a,m):return (-a[0]%m,-a[1]%m)
def sc(a,c,m):return (a[0]*c%m,a[1]*c%m)
def mul(a,b,m):return ((a[0]*b[0]+2*a[1]*b[1])%m,(a[0]*b[1]+a[1]*b[0])%m)
def eval_poly(cc,x,m):
    v=(0,0);d=(0,0)
    for c in cc[::-1]:
        d=add(mul(d,x,m),v,m)
        v=add(mul(v,x,m),(c,0),m)
    return v,d

def setup(p,d):
    m=p**3;c=[1]
    for k in range(1,p):
        nu=(d*(k-1)+1)*(d*(k-1)+d-1)
        c.append(c[-1]*nu*pow(d*d*k*k,-1,m)%m)
    h=[comb(2*k,k)*c[k]%m for k in range(p)]
    D=[0]*(2*p-1)
    for j,cj in enumerate(c):
        for k,ck in enumerate(c):
            D[j+k]=(D[j+k]+cj*ck)%m
    for k in range(p):
        bj=1
        for j in range(k+1):
            D[k+j]=(D[k+j]-h[k]*bj*(1 if j%2==0 else -1))%m
            if j<k:bj=bj*(k-j)//(j+1)
    assert all(z%p**2==0 for z in D),(p,d)
    assert all(D[j]==0 for j in range(p+1)),(p,d)
    E=[z//p**2 for z in D]
    z=(2,1) if d==3 else (3,2);denom=4 if d==3 else 6
    x=sc(z,pow(denom,-1,m),m)
    F,Fd=eval_poly(c,x,m)
    Ev,Ed=eval_poly(E,tuple(a%p for a in x),p)
    return {'E':E,'F':F,'Fd':Fd,'Ev':Ev,'Ed':Ed}

def rm(f,p):return f.numerator*pow(f.denominator,-1,p)%p

def original(p):
    m=p**3;A=B=MA=MB=0
    for k in range(p):
        base=comb(2*k,k)**2
        a=base*comb(3*k,k)*pow(216,-k,m)%m
        b=base*comb(4*k,2*k)*pow(2304,-k,m)%m
        A=(A+a)%m;B=(B+b)%m
        MA=(MA+k*a)%m;MB=(MB+k*b)%m
    return {'A':A,'B':B,'MA':MA,'MB':MB,'W':(A+6*MA)%m,'V':(B+8*MB)%m}

def witness(p):
    aa=setup(p,3);bb=setup(p,4);m=p**3;s=(0,1)
    assert aa['E'][p+3]==rm(Fraction(23170,177147),p)
    assert bb['E'][p+3]==rm(Fraction(106595,786432),p)
    Fa,Fb,Fda,Fdb=aa['F'],bb['F'],aa['Fd'],bb['Fd']
    assert all(v%p==0 for v in Fa+Fb)
    square=add(mul(Fa,Fa,m),neg(mul(Fb,Fb,m),m),m)
    der=add(sc(mul(s,mul(Fa,Fda,m),m),-3*pow(2,-1,m),m),
            sc(mul(s,mul(Fb,Fdb,m),m),pow(3,-1,m),m),m)
    assert all(v%p**2==0 for v in square+der)
    square=tuple(v//p**2%p for v in square)
    der=tuple(v//p**2%p for v in der)
    ev=add(neg(aa['Ev'],p),bb['Ev'],p)
    ed=add(sc(mul(s,aa['Ed'],p),3*pow(4,-1,p),p),
           sc(mul(s,bb['Ed'],p),-pow(6,-1,p),p),p)
    total=add(add(square,der,p),add(ev,ed,p),p)
    o=original(p)
    assert (o['W']-o['V'])%m==0 and total==(0,0),(p,total,o)
    return {'p':p,'origin':o,'sources':{'period_square':square,'period_derivative':der,
        'defect_evaluation':ev,'defect_derivative':ed},'total':total,
        'third_coefficients':(aa['E'][p+3],bb['E'][p+3])}

def primes(n):
    sieve=[True]*(n+1);sieve[0]=sieve[1]=False
    for i in range(2,int(n**.5)+1):
        if sieve[i]:
            for j in range(i*i,n+1,i):sieve[j]=False
    return [p for p in range(5,n+1) if sieve[p]]

if __name__=='__main__':
    n=0
    for p in primes(1000):
        for d,fr in [(3,Fraction(23170,177147)),(4,Fraction(106595,786432))]:
            assert setup(p,d)['E'][p+3]==rm(fr,p),(p,d)
            n+=1
    results=[witness(p) for p in primes(500) if p%24 in (13,19)]
    print(json.dumps({'all_prime_coefficient_checks':n,'target_jet_checks':len(results),
        'failures':0,'examples':[x for x in results if x['p'] in (13,19,139,373)]},
        ensure_ascii=False,indent=2))
