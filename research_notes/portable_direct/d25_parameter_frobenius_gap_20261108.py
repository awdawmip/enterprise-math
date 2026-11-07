#!/usr/bin/env python3
"""Exact D25 parameter Frobenius-boundary gap checks (integers only)."""
from fractions import Fraction
from math import factorial

def primes_below(n):
    s=bytearray(b'\x01')*n
    s[:2]=b'\x00\x00'
    for j in range(2,int(n**.5)+1):
        if s[j]: s[j*j:n:j]=b'\x00'*len(s[j*j:n:j])
    return [j for j in range(2,n) if s[j]]

def residue(q,mod):
    return q.numerator*pow(q.denominator,-1,mod)%mod

def models(p):
    m=(p-1)//6
    k=(p-3)//8 if p%8==3 else (p-5)//8
    return {'A':(m,2*m,Fraction(1,6),Fraction(1,3)),
            'B':(k,3*k+1,Fraction(1,8),Fraction(3,8))}

def poch_product(p,u,c,mod):
    x=residue(c,mod)*p-u
    ans=1
    for j in range(p): ans=ans*(x+j)%mod
    return ans

def polynomial_factor(p,u,c):
    arr=[1]
    t=residue(c,p)
    for j in range(p):
        out=[0]*(len(arr)+1)
        for i,x in enumerate(arr):
            out[i]=(out[i]+(j-u)*x)%p
            out[i+1]=(out[i+1]+t*x)%p
        arr=out
    expected=[0]*(p+1)
    expected[1]=-t%p
    expected[p]=t
    assert arr==expected

def verify(p,u,v,c1,c2,formal=False):
    assert 0<=u<v<=p-2
    mod=p**4
    N=poch_product(p,u,c1,mod)*poch_product(p,v,c2,mod)%mod
    N=N*pow(factorial(p-1),-2,mod)%mod
    H=lambda n:sum(pow(j,-1,p*p) for j in range(1,n+1))%(p*p)
    predicted=p*p*residue(c1*c2,mod)*(1+p*(H(u)+H(v)))%mod
    assert N==predicted,(p,u,v,N,predicted)
    for q in (u,v):
        H0=sum(pow(j,-1,p) for j in range(1,q+1))%p
        H1=sum(pow(j,-1,p) for j in range(1,p-q))%p
        assert H0==H1 # exact coefficient-of-h^3 vanishing mod p
    if formal:
        polynomial_factor(p,u,c1)
        polynomial_factor(p,v,c2)
        # Hence the complete product equals c1*c2*(h^p-h)^2.
    return N//(p*p)

if __name__=='__main__':
    pp=[p for p in primes_below(2500) if p%24 in (13,19)]
    probes={13,19,43,67,373}
    n=0
    for p in pp:
        a={}
        for name,args in models(p).items():
            a[name]=verify(p,*args,formal=p in probes)
            n+=1
        if p in probes:
            print('p=',p,'A=',a['A'],'B=',a['B'],'mod=',p*p)
    print('PASS',len(pp),'primes;',n,'complete mod p^4 tests;',
          len(probes)*2,'formal polynomial factorizations (each p-fold product)')
