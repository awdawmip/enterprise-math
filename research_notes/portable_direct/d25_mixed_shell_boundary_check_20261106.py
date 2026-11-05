#!/usr/bin/env python3
"""Original-factorial integer and independent exact-rational verification of D25 (A)(B)."""
from math import factorial, isqrt
from fractions import Fraction

def primes(n):
    z=[True]*(n+1);z[0]=z[1]=False
    for k in range(2,isqrt(n)+1):
        if z[k]:
            for a in range(k*k,n+1,k):z[a]=False
    return [i for i in range(5,n+1) if z[i]]

def afactor(k,p,M):
    def fu(n):
        v,u=0,1
        for i in range(1,n+1):
            x=i
            while x%p==0:x//=p;v+=1
            u=u*x%M
        return v,u
    v2,u2=fu(2*k);v3,u3=fu(3*k);vk,uk=fu(k)
    return v2+v3-5*vk,(u2*u3*pow(uk,-5,M)*pow(216,-k,M))%M

def G(h,j):return (2*h-2*j+1)*(3*h-3*j+2)*(3*h-3*j+1)
def P(h,j):return 36*(h-j)**3-G(h,j)

count=0
for p in primes(997):
    if p%6!=1:continue
    m=(p-1)//6;h=3*m;M=p*p
    us=[]
    for j in range(m):
        v,u=afactor(h-j,p,M)
        assert v==1
        us.append(u)
    vb,b=afactor(2*m,p,M);vs,s=afactor(h,p,M)
    assert (vb,vs)==(0,1)
    lhs=sum(P(h,j)*us[j] for j in range(m))%M
    bot=(4*m+1)*(p+1)*b%M
    top=(9*m+1)*(9*m+2)*p*s%M
    assert lhs==(bot-top)%M
    assert lhs%p==b*pow(3,-1,p)%p
    count+=1

for p in (13,19):
    m=(p-1)//6;h=3*m
    def a(k):
        return Fraction(factorial(2*k)*factorial(3*k),216**k*factorial(k)**5)
    u=[a(h-j)/p for j in range(m+1)]
    assert all(G(h,j+1)*u[j+1]-G(h,j)*u[j]==P(h,j)*u[j] for j in range(m))
    assert sum(P(h,j)*u[j] for j in range(m)) == (4*m+1)*(p+1)*a(2*m)-(9*m+1)*(9*m+2)*a(h)
assert count==80
print("PASS:",count,"prime modular checks, two independent rational examples")
