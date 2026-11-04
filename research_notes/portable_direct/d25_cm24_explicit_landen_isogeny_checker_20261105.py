#!/usr/bin/env python3
"""Exact CM−24 Landen/Vélu identities, no external libraries."""
from fractions import Fraction
from math import isqrt
O=(1,0,0,0)
def n(i):return (i,0,0,0)
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def sub(x,y):return tuple(a-b for a,b in zip(x,y))
def mul(x,y):
    z=[0]*4
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            c=i&j
            z[i^j]+=a*b*(2 if c&1 else 1)*(3 if c&2 else 1)
    return tuple(z)
def sq(x):return mul(x,x)
def red(x,p):return tuple(a%p for a in x)
def pw(x,k,p):
    y=O
    while k:
        if k&1:y=red(mul(y,x),p)
        x=red(sq(x),p);k//=2
    return y
def prime(p):return p>=2 and all(p%k for k in range(2,isqrt(p)+1))
def s(e,d):return (3,2*e,2*d,e*d)
def main():
    for e in (-1,1):
        for d in (-1,1):
            v=s(e,d);w=s(-e,-d);t=sq(v)
            assert mul(add(O,v),w)==sub(O,v)
            alpha=tuple(-a for a in sq(add(O,v)))
            beta=tuple(-a for a in sq(sub(O,v)))
            assert mul(alpha,sq(w))==beta
            assert add(alpha,beta)==tuple(-2*a for a in add(O,t))
            assert mul(alpha,beta)==sq(sub(O,t))
    cnt=0
    for t in (Fraction(2),Fraction(5),Fraction(11),Fraction(17,3)):
        for x in (Fraction(3),Fraction(7),Fraction(13,2),Fraction(19)):
            A=-(1+t);B=t;X=x+A+B/x
            y2=x**3+A*x*x+B*x
            assert y2*(1-B/x**2)**2==X**3-2*A*X**2+(A*A-4*B)*X
            cnt+=1
    classes={5:0,13:0}
    for p in range(5,20001):
        if p%24 not in classes or not prime(p):continue
        assert pow(-1,(p-1)//2,p)==1
        for e in (-1,1):
            for d in (-1,1):
                v=s(e,d);t=sq(v);partner=sq(s(-e,-d))
                alpha=tuple(-a for a in sq(add(O,v)))
                beta=tuple(-a for a in sq(sub(O,v)))
                assert red(mul(alpha,partner),p)==red(beta,p)
                t_frob=pw(t,p,p)
                if p%24==5:assert red(partner,p)==t_frob
                else:assert red(mul(partner,t_frob),p)==red(O,p)
        classes[p%24]+=1
    print('PASS Landen/Vélu rational checks',cnt,'primes',sum(classes.values()),
          'branch comparisons',4*sum(classes.values()),'classes',classes)
if __name__=='__main__':main()
