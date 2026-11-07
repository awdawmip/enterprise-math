#!/usr/bin/env python3
"""Exact F_p/F_(p^2) p=8k+3 CM/Hasse checks. Pure standard library."""
from math import comb

def primes(limit):
    s=bytearray(b"\x01")*limit;s[:2]=b"\x00\x00"
    for n in range(2,int((limit-1)**.5)+1):
        if s[n]:s[n*n:limit:n]=b"\x00"*(((limit-1-n*n)//n)+1)
    return [p for p in range(5,limit) if s[p] and p%8==3]

def tbl(p):
    f=[1]*p
    for i in range(1,p):f[i]=f[i-1]*i%p
    inv=[1]*p;inv[-1]=pow(f[-1],-1,p)
    for i in range(p-1,0,-1):inv[i-1]=inv[i]*i%p
    return f,inv

def choose(n,j,p,f,v):
    return 0 if j<0 or j>n else f[n]*v[j]*v[n-j]%p

def horner(c,x,p):
    z=0
    for a in c[::-1]:z=(z*x+a)%p
    return z

def mul(x,y,p):return ((x[0]*y[0]+2*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
def horner2(c,u,p):
    z=(0,0)
    for a in c[::-1]:
        v=mul(z,u,p);z=((v[0]+a)%p,v[1])
    return z

def check(limit=5000):
    count={11:0,19:0};examples={}
    for p in primes(limit):
        k=(p-3)//8;d=2*k;N=(p-1)//2;f,v=tbl(p)
        H=[choose(3*k+1,j,p,f,v)*choose(k,j,p,f,v)%p for j in range(k+1)]
        L=[choose(3*d+2,j,p,f,v)*choose(d,j,p,f,v)%p for j in range(d+1)]
        T=[0]*(d+1)
        for j,hj in enumerate(H):
            for t in range(j+1):
                T[j+t]=(T[j+t]+hj*pow(4,j,p)*choose(j,t,p,f,v)*(-1 if t%2 else 1))%p
        assert T==L,(p,"quadratic transform")
        A=[(-1)**j*choose(N,j,p,f,v)*choose(2*N-2*j,N,p,f,v)%p for j in range(d+1)]
        assert all((x+y)%p==0 for x,y in zip(A,L)),(p,"Hasse")
        w=pow(9,-1,p);value=horner(H,w,p)
        derivative=sum(j*H[j]*pow(w,j-1,p) for j in range(1,len(H)))%p
        assert (value==0)==(p%24==19),(p,"CM",value)
        if p%24==19:assert derivative!=0,(p,"double root")
        u=(pow(2,-1,p),pow(3,-1,p));u2=(u[0],-u[1]%p)
        assert horner2(L,u,p)==(value,0) and horner2(L,u2,p)==(value,0)
        assert mul(u,u2,p)==(pow(36,-1,p),0)
        count[p%24]+=1
        if p in (11,19,43,67,139,163):examples[p]=(value,derivative)
    print("PASS",limit,count,examples)

if __name__=="__main__":check()
