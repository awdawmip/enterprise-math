#!/usr/bin/env python3
"""Exact integer tests of diagonal binomial action and two boundary fluxes.
Author checks only; not native CM or independent verification.
"""
from math import comb
from random import Random

def fibre(m,n):
    M=2*m
    return max(1,1-n),min(M,M-n)

def choose(j,s):
    return comb(j,s) if 0<=s<=j else 0

def B(m,w,n,s):
    lo,hi=fibre(m,n)
    return sum(choose(j-1,s)*w.get((j,j+n),0) for j in range(lo,hi+1))

def Bq(m,w,n,s):
    Q=lambda j:(j-1-m)*(j-1-2*m)
    lo,hi=fibre(m,n)
    return sum(choose(j-1,s)*Q(j)*w.get((j,j+n),0) for j in range(lo,hi+1))

def closed_q(m,w,n,s):
    return ((s-m)*(s-2*m)*B(m,w,n,s)
            +(s+1)*(2*s+1-3*m)*B(m,w,n,s+1)
            +(s+1)*(s+2)*B(m,w,n,s+2))

def shift_j(m,w):
    M=2*m
    return {(j+1,ell):v for (j,ell),v in w.items() if j<M}

def shift_ell(m,w):
    M=2*m
    return {(j,ell+1):v for (j,ell),v in w.items() if ell<M}

def predict_shift_j(m,w,n,s):
    M=2*m
    edge=choose(M,s)*w[(M,M+n)] if 1-M<=n<=0 else 0
    return B(m,w,n,s)+B(m,w,n,s-1)-edge

def predict_shift_ell(m,w,n,s):
    M=2*m
    edge=choose(M-n-1,s)*w[(M-n,M)] if 0<=n<=M-1 else 0
    return B(m,w,n,s)-edge

def check():
    checks=0
    for m in range(1,13):
        M=2*m
        for trial in range(3):
            rng=Random(47_317*m+trial)
            w={(j,ell):rng.randrange(-1000,1001)
               for j in range(1,M+1) for ell in range(1,M+1)}
            left=shift_j(m,w)
            right=shift_ell(m,w)
            for n in range(1-M,M):
                for s in range(M+2):
                    assert Bq(m,w,n,s)==closed_q(m,w,n,s), (m,n,s,'Q')
                    assert B(m,left,n-1,s)==predict_shift_j(m,w,n,s),(m,n,s,'left')
                    assert B(m,right,n+1,s)==predict_shift_ell(m,w,n,s),(m,n,s,'right')
                    checks+=3
    print(f"PASS: {checks} exact integer checks for Q rank action and two boundary-preserving shifts")

if __name__=='__main__':
    check()
