#!/usr/bin/env python3
"""Exact author check of adaptive unimodular diagonal source tomography.
Not native CM, formal verification or independent review.
"""
from math import comb
from random import Random

def nbinom(a,k):
    if k==0: return 1
    if a==0: return 0
    return (-1)**k*comb(a+k-1,k)

def fibre(m,n):
    M=2*m
    low=max(1,1-n)
    high=min(M,M-n)
    assert high-low+1==M-abs(n)
    return low,high

def polar_signature(m,cells):
    M=2*m; N=2*M-1
    return [[(-1)**k*sum(comb(j-1,s)*comb(2*M+ell-j,k)*w
                          for (j,ell),w in cells.items())
              for k in range(N)] for s in range(M)]

def invert_high_poles(m,beta):
    M=2*m; N=2*M-1
    B={n:{} for n in range(1-M,M)}
    for s in range(M):
        d=[sum(comb(M+h,h)*beta[s][k-h] for h in range(k+1))
           for k in range(N)]
        x=[(-1)**r*sum(comb(k,r)*d[k] for k in range(r,N))
           for r in range(N)]
        for r,n in enumerate(range(1-M,M)): B[n][s]=x[r]
    return B

def restore_cells(m,beta):
    B=invert_high_poles(m,beta); restored={}
    for n in range(1-2*m,2*m):
        jmin,jmax=fibre(m,n); a=jmin-1; d=jmax-jmin+1
        C=[sum(nbinom(a,h)*B[n][s-h] for h in range(s+1))
           for s in range(d)]
        for r in range(d):
            restored[(jmin+r,jmin+r+n)]=sum(
                (-1)**(s-r)*comb(s,r)*C[s] for s in range(r,d))
    return restored,B

def validate():
    checks=0
    for m in range(1,12):
        M=2*m
        for trial in range(3):
            rng=Random(104729*m+trial)
            cells={(j,ell):rng.randint(-10000,10000)
                   for j in range(1,M+1) for ell in range(1,M+1)}
            restored,B=restore_cells(m,polar_signature(m,cells))
            assert restored==cells,(m,trial)
            for n in range(1-M,M):
                jlo,jhi=fibre(m,n)
                for s in range(jhi-jlo+1):
                    assert B[n][s]==sum(comb(j-1,s)*cells[(j,j+n)]
                                        for j in range(jlo,jhi+1))
                    checks+=1
    for m in range(2,30):
        delta=[1,-3,3,-1]
        assert [sum(delta[i]*i**s for i in range(4))
                for s in (0,1,2)]==[0]*3
        assert all(sum(delta[i]*comb(i,s) for i in range(4))==0
                   for s in (0,1,2))
        Q=lambda j:(j-1-m)*(j-1-2*m)
        assert sum(delta[j-1]*Q(j)**2 for j in range(1,5))==36*(m-1)
        checks+=1
    primes=[p for p in range(13,300,6)
            if all(p%d for d in range(2,int(p**.5)+1))]
    for p in primes:
        assert 36*((p-1)//6-1)%p!=0
        checks+=1
    print(f"PASS: {checks} exact counted checks; 33 integer signed arrays;"
          f" 28 quadratic witness cases; {len(primes)} target primes")
    print("m=2 / p=13: Q^2 observer discrepancy 36 mod 13 =",36%13)

if __name__=="__main__": validate()
