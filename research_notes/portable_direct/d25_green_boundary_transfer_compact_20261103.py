#!/usr/bin/env python3
"""Finite exact D25 Gauss-Green entry/interior/exit checker; author-side only."""
from math import factorial

def primes(n):
    a=[True]*(n+1);a[:2]=[False,False]
    for d in range(2,int(n**.5)+1):
        if a[d]:
            for k in range(d*d,n+1,d):a[k]=False
    return [p for p in range(n+1) if a[p]]

def check(p):
    r=(p-1)//6; m=3*(4*r+1)
    F=[1]*(m+1);V=[0]*(m+1)
    for j in range(1,m+1):
        t=j; v=0
        while t%p==0:t//=p;v+=1
        F[j]=F[j-1]*t%p;V[j]=V[j-1]+v
    def bu(k):
        v=V[2*k]+V[3*k]-5*V[k]
        u=F[2*k]*F[3*k]*pow(F[k],-5,p)*pow(216,-k,p)%p
        return v,u
    assert bu(3*r)[0]==1
    E=bu(3*r)[1]; U=-E*pow(18,-1,p)%p
    assert bu(3*r+1)==(2,U)
    assert (6*(3*r+1)+1)*U%p==(6*(3*r)+1)*E*pow(9,-1,p)%p
    H=0
    for k in range(3*r+1,4*r+1):
        assert bu(k)==(2,U)
        H=(H+(6*k+1)*U)%p
        if k<4*r:
            rho=(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,p)%p
            assert rho!=0
            U=U*rho%p
            a=bu(k+1)[1]*pow(2,k+1,p)%p
            b=bu(k)[1]*pow(2,k,p)%p
            Q=(2*k+1)*(3*k+1)*(3*k+2)*pow(18,-1,p)%p
            assert (k+1)**3*a%p==Q*b%p
    assert bu(4*r+1)==(3,U*pow(2,-1,p)%p)
    after=(6*(4*r+1)+1)*bu(4*r+1)[1]%p
    before=(6*(4*r)+1)*U%p
    assert after==(-before*pow(2,-1,p))%p
    fact=[1]*p
    for k in range(1,p):fact[k]=fact[k-1]*k%p
    H2=0
    for j in range(2*r+1,3*r+1):
        z=(6*j-1)*pow(216,j-1,p)*pow(fact[j-1],5,p)
        z=z*pow(fact[2*j-1]*fact[3*j-p-1],-1,p)%p
        H2=(H2+z)%p
    assert H==H2
    return H
if __name__=='__main__':
    ps=[p for p in primes(2000) if p%6==1]
    result={p:check(p) for p in ps}
    assert {p:result[p] for p in (7,13,19,37,373)}=={7:5,13:10,19:9,37:20,373:266}
    print('PASS',len(ps),'p=6r+1 primes, entry/interior/exit/Green/independent H2')
