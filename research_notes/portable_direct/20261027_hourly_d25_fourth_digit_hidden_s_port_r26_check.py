#!/usr/bin/env python3
"""D25 R26 exact integral fourth-digit original S-source/weight-jet checks.

Author-side integer arithmetic only, not native CM/Frobenius execution.
"""
from math import comb, isqrt


def primes(bound=1999):
    return [p for p in range(13,bound+1) if p%24==13 and all(p%d for d in range(2,isqrt(p)+1))]


def beta(p,j,m):
    f=[1]*p
    for a in range(1,p): f[a]=f[a-1]*a%p
    b=4*j-6*m+2
    assert 0<=b<p
    return 2*pow(2304,j,p)*pow(f[j],4,p)*pow(f[b],-1,p)%p


def observed(p):
    m=(p-1)//6
    r=(p-13)//24
    j=(3*p-7)//8
    k=(5*p-1)//8
    assert j==2*m+r and k==p-1-j and 8*k+1==5*p and 8*j+7==3*p
    Be=beta(p,j,m)
    assert Be!=0
    mod=p**4
    unweighted=comb(4*k,2*k)*comb(2*k,k)**2*pow(2304,-k,mod)%mod
    weighted=(8*k+1)*unweighted%mod
    assert unweighted%(p*p)==0 and unweighted%(p**3)!=0
    assert weighted%(p**3)==0 and weighted%(p**4)!=0
    u=unweighted//(p*p)%p
    value=weighted//(p**3)%p
    assert u==(-Be)%p,(p,u,Be)
    assert value==(-5*Be)%p,(p,value,Be)
    return p,m,r,j,k,Be,value


def run():
    ps=primes()
    rows=[observed(p) for p in ps]
    for row in rows:
        if row[0] in [13,37,61,181,373,733,997]:
            print('p=%d m=%d r0=%d j0=%d k0=%d beta=%d s_k/p^3=%d' % row)
    print('PASS: %d primes p<2000, p=13(mod24): exact integer S source v_p=3, fourth-digit residue -5 beta_j !=0' % len(ps))

if __name__=='__main__':
    run()
