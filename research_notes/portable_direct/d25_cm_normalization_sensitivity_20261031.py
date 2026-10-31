#!/usr/bin/env python3
"""Exact finite-field observer sensitivity for original D25 normalization.

Standalone author evidence: no native control grant or P000 bridge is implied.
"""
from math import comb

def primes_up_to(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[0:2]=b'\x00\x00'
    for j in range(2,int(n**0.5)+1):
        if sieve[j]:
            sieve[j*j::j]=b'\x00'*((n-j*j)//j+1)
    return [j for j in range(2,n+1) if sieve[j]]

def derivative_and_value(p):
    ell=(p-1)//6
    v=0
    d=0
    z=pow(2,-1,p)
    for k in range(ell+1):
        c=comb(ell,k)*comb(2*ell,k)%p
        v=(v+c*pow(z,k,p))%p
        if k:
            d=(d+k*c*pow(z,k-1,p))%p
    return v,d

def original_coefficients(p):
    q=p*p
    a=[1]
    for n in range(p-1):
        num=(2*n+1)*(3*n+1)*(3*n+2)
        den=36*(n+1)**3
        a.append(a[-1]*num*pow(den,-1,q)%q)
    return a

def weighted_sum(a,p,t):
    q=p*p
    x=pow(1+p*t,-1,q)
    pw=1
    total=0
    for n,c in enumerate(a):
        total=(total+(6*n+1)*c*pw)%q
        pw=pw*x%q
    return total

def main():
    target=[p for p in primes_up_to(5000) if p%24 in (13,19)]
    checks=0
    print('CASE p Gprime (A0 mod p2)  finite_diff_per_p at t=1')
    for p in target:
        v,d=derivative_and_value(p)
        assert v==0, ('cm-root-input-failed',p,v)
        assert d!=0, ('derivative-nonzero',p)
        a=original_coefficients(p)
        a0=weighted_sum(a,p,0)
        # Check a direct finite difference of the original 216 coefficient sum.
        assert a0%p==0
        for t in [-2,-1,0,1,2]:
            at=weighted_sum(a,p,t)
            assert (at-a0)%p==0
            obs=((at-a0)//p)%p
            expected=(-3*t*d*d)%p
            assert obs==expected, ('sensitivity',p,t,obs,expected)
            checks+=1
        if p in (13,19,37,157,373,1327):
            print(p,d,a0,((weighted_sum(a,p,1)-a0)//p)%p)
    print('TARGET_PRIMES',len(target),'NORMALIZATION_CHECKS',checks)
    print('PASS_D25_CM_FIXED_NORMALIZATION_FIRST_DIGIT_SENSITIVITY_EXACT')
if __name__=='__main__':
    main()
