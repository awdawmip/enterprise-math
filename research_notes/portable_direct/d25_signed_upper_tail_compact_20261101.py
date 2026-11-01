#!/usr/bin/env python3
"""Exact signed D25 upper-tail exceptions; author-side, not native H0/B0."""
from math import isqrt

def primes(limit):
    s=bytearray(b'\1')*(limit+1);s[:2]=b'\0\0'
    for d in range(2,isqrt(limit)+1):
        if s[d]: s[d*d:limit+1:d]=b'\0'*((limit-d*d)//d+1)
    return [p for p in range(5,limit+1) if s[p]]

def upper_digit(p):
    m=p//4;P=Q=1;u=0
    for j in range(m):
        u=(u+(5+6*j)*P-2*(7+8*j)*Q)%p
        if j+1<m:
            h=j+1
            P=P*36*h**3*pow((2*j+3)*(3*j+4)*(3*j+5),-1,p)%p
            Q=Q*288*h**3*pow((2*j+3)*(4*j+5)*(4*j+7),-1,p)%p
    return u

def forward(p):
    m=p**4;a=b=1;A=B=0
    for k in range(p):
        if 4*k>=3*p:
            A=(A+(6*k+1)*a)%m;B=(B+(8*k+1)*b)%m
        if k+1<p:
            h=k+1
            a=a*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*h**3,-1,m)%m
            b=b*(2*k+1)*(4*k+1)*(4*k+3)*pow(288*h**3,-1,m)%m
    return A,B

def original_integer_binomials(p, lower=None):
    m=p**4;n=4*(p-1);v=[0]*(n+1);f=[1]*(n+1)
    for i in range(1,n+1):
        q=i;e=0
        while q%p==0: q//=p;e+=1
        v[i]=v[i-1]+e;f[i]=f[i-1]*q%m
    inv=[1]*(n+1);inv[n]=pow(f[n],-1,m)
    for i in range(n,0,-1):
        q=i
        while q%p==0:q//=p
        inv[i-1]=inv[i]*q%m
    def c(n,k):
        return (p**(v[n]-v[k]-v[n-k])*f[n]*inv[k]*inv[n-k])%m
    lo=(3*p+3)//4 if lower is None else lower;x=pow(pow(216,-1,m),lo,m);y=pow(pow(2304,-1,m),lo,m)
    inv216=pow(216,-1,m);inv2304=pow(2304,-1,m);A=B=0
    for k in range(lo,p):
        h=c(2*k,k)**2
        A=(A+(6*k+1)*h*c(3*k,k)*x)%m
        B=(B+(8*k+1)*h*c(4*k,2*k)*y)%m
        x=x*inv216%m;y=y*inv2304%m
    return A,B

def verify():
    pp=primes(20000);assert len(pp)==2260
    zeros=[p for p in pp if upper_digit(p)==0]
    assert zeros==[1019,17231],zeros
    print('EXHAUSTIVE',len(pp),'primes <= 20000:',zeros)
    for p in (13,19,373,1019,17231):
        A,B=forward(p);assert (A,B)==original_integer_binomials(p)
        assert A%p**3==0 and B%p**3==0
        u=upper_digit(p);assert (A-2*B)%p**4==p**3*u
        if p in zeros:assert A and B and u==0
        print(p, 'U=',u, 'A5/p^3=',A//p**3, 'B5/p^3=',B//p**3)
    print('PASS exact integer two-route crosschecks; not an all-prime theorem')

if __name__=='__main__':
    verify()
    for p in (1019,17231):
        A,B=original_integer_binomials(p,lower=0)
        assert (A-2*B-p)%p**4==0
        assert (A+p)%p**3==0 and (B+p)%p**3==0
        print('EXCEPTIONAL_FULL_AFFINE',p,'A=',A,'B=',B,'A-2B-p mod p^4=',(A-2*B-p)%p**4)

