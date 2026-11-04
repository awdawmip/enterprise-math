#!/usr/bin/env python3
"""Exact Clausen factorization and p-adic cancellation checker; author-side only."""
from math import isqrt, comb

def primes(limit):
    flag=bytearray(b'\x01')*(limit+1)
    flag[:2]=b'\x00\x00'
    for d in range(2,isqrt(limit)+1):
        if flag[d]: flag[d*d:limit+1:d]=b'\x00'*((limit-d*d)//d+1)
    return [p for p in range(5,limit+1) if flag[p]]

def valuation_mod3(x,p):
    return 0 if x%p else (1 if x%(p*p) else (2 if x%(p*p*p) else 3))

def check(p):
    m=p**3
    u=[1]*p; v=[1]*p; a=[1]*p; b=[1]*p
    j36=pow(36,-1,m);j576=pow(576,-1,m)
    for k in range(p-1):
        j2=pow((k+1)**2,-1,m); j3=pow((k+1)**3,-1,m)
        u[k+1]=u[k]*(6*k+1)*(3*k+1)*j36*j2%m
        v[k+1]=v[k]*(8*k+1)*(8*k+3)*j576*j2%m
        a[k+1]=a[k]*(2*k+1)*(3*k+1)*(3*k+2)*j36*j3%m
        b[k+1]=b[k]*(4*k+1)*(4*k+2)*(4*k+3)*j576*j3%m
    for n in range(p):
        assert sum(u[i]*u[n-i] for i in range(n+1))%m==a[n],('a',p,n)
        assert sum(v[i]*v[n-i] for i in range(n+1))%m==b[n],('b',p,n)
    if p in (11,13,17,19,23,29,37):
        for n in range(p):
            assert a[n]==comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,m)%m
            assert b[n]==comb(2*n,n)**2*comb(4*n,2*n)*pow(2304,-n,m)%m
    def upper(C,raw,w):
        s=sum(C)%m;d=sum(k*C[k] for k in range(p))%m
        return (s*s+2*w*s*d-raw)%m
    ta=upper(u,sum((6*k+1)*a[k] for k in range(p))%m,6)
    tb=upper(v,sum((8*k+1)*b[k] for k in range(p))%m,8)
    if p>=7 and p%6==1:
        r=(p-1)//6
        assert all(valuation_mod3(u[k],p)==int(k>r)+int(k>2*r) for k in range(p))
        assert ta%p**2==0
        assert ta==2*sum((6*(i+j)+1)*u[i]*u[j] for i in range(1,r+1) for j in range(p-i,p))%m
    if p>=11 and p%8==3:
        q=(p-3)//8
        assert all(valuation_mod3(v[k],p)==int(k>q)+int(k>3*q+1) for k in range(p))
        assert tb%p**2==0
        assert tb==2*sum((8*(i+j)+1)*v[i]*v[j] for i in range(1,q+1) for j in range(p-i,p))%m
    ca=cb=0
    if p>=11 and p%6==5:
        r=(p-5)//6
        assert all(u[k]%p for k in range(4*r+4))
        for n in range(2*r+2,4*r+4):
            assert valuation_mod3(a[n],p)==(1 if n<=3*r+2 else 2)
            assert all(u[j]%p and u[n-j]%p for j in range(n+1))
            ca+=1
    if p>=13 and p%8==5:
        q=(p-5)//8
        assert all(v[k]%p for k in range(5*q+4))
        for n in range(2*q+2,5*q+4):
            assert valuation_mod3(b[n],p)==(1 if n<=4*q+2 else 2)
            assert all(v[j]%p and v[n-j]%p for j in range(n+1))
            cb+=1
    return ca,cb

if __name__=="__main__":
    rows=[(p,*check(p)) for p in primes(503)]
    print("PASS primes=%d Clausen_coefficient_checks=%d A_unit_cancellation_positions=%d B_unit_cancellation_positions=%d; triangle checks passed"%(len(rows),2*sum(x[0] for x in rows),sum(x[1] for x in rows),sum(x[2] for x in rows)))
    for p in (11,13,19,29,37,97,373):
        print("sample",p,check(p))
