#!/usr/bin/env python3
"""Exact author-side original-216 high-tail moment checker (not native H0/B0)."""
from math import isqrt

def primes(n):
    for p in range(7,n+1):
        if all(p%q for q in range(2,isqrt(p)+1)):
            yield p

def check(p):
    m=(p-1)//6
    P=p**3
    b=[1]
    for k in range(p-1):
        b.append(b[-1]*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,P)%P)
    d=pow(10,-1,p)
    assert (b[p-1]//p**2)%p==d
    M=[0,0,0]
    q=[0,0,0]
    for i in range(1,m+1):
        assert (b[p-i]//p**2)%p==d,(p,i)
        for j in range(3):
            M[j]=(M[j]+pow(i,j,p)*d)%p
        readouts=(M[0],i*M[0]-M[1],i*i*M[0]-2*i*M[1]+M[2])
        for j,x in enumerate(readouts):
            q[j]=(q[j]+2*(b[i]%p)*x)%p
        if i<m:
            d=d*36*i*i*pow((6*i+5)*(3*i+2),-1,p)%p
    direct=[0,0,0]
    for i in range(p):
        for j in range(max(0,p-i),p):
            z=b[i]*b[j]%P
            for k in range(3):
                direct[k]=(direct[k]+(i+j)**k*z)%P
    assert all(x%p**2==0 for x in direct)
    assert q==[(x//p**2)%p for x in direct],(p,q,direct)
    if p==19:
        inv10=pow(10,-1,p)
        wrong=inv10*2*pow((5*pow(6,-1,p))*(2*pow(3,-1,p)),-1,p)%p
        assert wrong==11
        assert (b[p-2]//p**2)%p==2
    return q

rows=[(p,check(p)) for p in primes(373) if p%6==1]
assert len(rows)==35
for p,q in rows:
    if p in (7,13,19,37,61,373):
        print("p",p,"T0,T1,T2",q,"T0+6T1",(q[0]+6*q[1])%p)
print("PASS 35/35, including corrected r=2, p=19 witness")
