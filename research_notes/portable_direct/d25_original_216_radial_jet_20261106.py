#!/usr/bin/env python3
"""Exact original-216 p-adic coefficients versus radial-jet leading terms."""
from math import comb
def primes(n):
    a=bytearray(b'\x01')*(n+1);a[:2]=b'\x00\x00'
    for k in range(2,int(n**0.5)+1):
        if a[k]: a[k*k::k]=b'\x00'*((n-k*k)//k+1)
    return [p for p in range(7,n+1) if a[p] and p%6==1]
def check(p):
    m=(p-1)//6;s=(2*m,3*m,4*m)
    fac=[1]*p;invfac=[1]*p
    for j in range(1,p):fac[j]=fac[j-1]*j%p
    invfac[-1]=pow(fac[-1],-1,p)
    for j in range(p-1,0,-1):invfac[j-1]=invfac[j]*j%p
    modulus=p**4;h=1;counts=[0]*4;totals=[0]*4
    for j in range(p):
        r=sum(j>x for x in s)
        assert h%p**r==0
        e=pow(-2,-j,p)
        for x in s:
            if j<=x: c=comb(x,j)%p
            else:
                c=fac[x]*fac[j-x-1]*invfac[j]%p
                if (j-x-1)%2:c=(-c)%p
                c=c*x%p  # derivative along x_i=s_i*t
            e=e*c%p
        actual=h//p**r%p
        assert e==actual and e!=0,(p,j,r,e,actual)
        counts[r]+=1
        totals[r]=(totals[r]+(6*j+1)*e)%p
        if j+1<p:
            h=h*(2*j+1)*(3*j+1)*(3*j+2)*pow(36*(j+1)**3,-1,modulus)%modulus
    return counts,totals
if __name__=='__main__':
    ps=primes(3000)
    for p in ps:
        c,t=check(p)
        if p in (7,13,19,373,1009):print(p,c,t)
    print('PASS',len(ps),'primes: all j<p, exact original-216/radial leading jets')
