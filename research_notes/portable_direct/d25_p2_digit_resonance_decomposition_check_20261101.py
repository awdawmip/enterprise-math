#!/usr/bin/env python3
"""Exactly test a new first-digit decomposition of Y_p(1/2)/p.

Research role: portable numerical-meaning check; no native H0/B0 execution.
"""
from math import comb, factorial
from collections import Counter


def primes_upto(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i,n+1,i): sieve[j] = False
    return [p for p in range(7, n+1) if sieve[p] and p%6 == 1]


def run(p):
    r=(p-1)//6; pp=p*p
    # Projective Legendre value through original finite binomial sum.
    A=[comb(r,k)*comb(2*r,k)*pow(2,-k,pp)%pp for k in range(r+1)]
    S=sum(A)%pp
    if p%24 not in (13,19): return None
    assert S%p==0,(p,'CM selector failed')
    carry=(S//p)%p
    low=0
    for k in range(0,r+1):
        H1=sum(pow(j-r,-1,p) for j in range(k))%p
        H2=sum(pow(j-2*r,-1,p) for j in range(k))%p
        low += (A[k]%p) * (H1*pow(6,-1,p) + H2*pow(3,-1,p))
    low%=p
    mid=0
    # The first resonance happens only in the (1/6) Pochhammer factor.
    for k in range(r+1,2*r+1):
        ratio=((-1)**(r+k)*factorial(r)*factorial(k-r-1)*factorial(2*r)
               *pow(6*factorial(2*r-k)*factorial(k)**2*2**k,-1,p))%p
        mid=(mid+ratio)%p
    # Independent source is original 2F1 product recurrence mod p^2.
    term=1; ys=1
    for k in range(p-1):
        term=term*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,pp)%pp
        ys=(ys+term)%pp
    assert ys%p==0
    a0=ys//p
    assert (carry+low+mid)%p==a0,(p,carry,low,mid,a0)
    return (p,carry,low,mid,a0)


def main():
    targets=[run(p) for p in primes_upto(3000)]
    targets=[a for a in targets if a]
    assert len(targets)==107
    print('PASS: 107 target primes p<=3000: CM carry + low harmonic + middle resonance = Y_p(1/2)/p mod p')
    for x in targets:
        if x[0] in (13,19,37,61,109,373,997):
            print('witness [p,carry,low-harmonic,middle-resonance,a0]:',x)
    print('scope: finite exact check; algebraic formula holds for all p=6r+1 with selector zero, by coefficient expansion.')


if __name__=='__main__': main()
