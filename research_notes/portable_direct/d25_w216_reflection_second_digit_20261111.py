#!/usr/bin/env python3
"""Exact integer verifier: all-band second digit and p5 weighted fourth-band reflection.
Author-side portable evidence; NOT an original H0/B0 native experiment.
"""
from math import comb, factorial, isqrt

def primes_up_to(n):
    s=bytearray(b"\x01")*(n+1)
    s[:2]=b"\x00\x00"
    for d in range(2,isqrt(n)+1):
        if s[d]:
            s[d*d::d]=b"\x00"*(((n-d*d)//d)+1)
    return [p for p in range(5,n+1) if s[p]]

def check(p,compare_factorials=False):
    assert p>3
    modulus=p**5
    a=[1]*p
    inv36=pow(36,-1,modulus)
    for k in range(1,p):
        n=k-1
        a[k]=(a[n]*(2*n+1)*(3*n+1)*(3*n+2)*
              inv36*pow(k,-3,modulus))%modulus
    if compare_factorials:
        for k in range(p):
            direct=comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,modulus)%modulus
            assert direct==a[k],(p,k,'factorial versus recurrence')
    H=[0]*p
    for k in range(1,p):
        H[k]=(H[k-1]+pow(k,-1,p))%p
    Q=(pow(216,p-1,p*p)-1)//p
    pairs=0
    for k in range(1,p):
        s2,r2=divmod(2*k,p)
        s3,r3=divmod(3*k,p)
        lam=(2*H[r2-1]+3*H[r3-1]-5*H[k-1]-Q)%p
        leading=-(-1)**(s2+s3)*factorial(s3)*factorial(2-s3)*pow(36*k**3,-1,p*p)
        right=leading*(1+p*lam)%(p*p)
        left=(a[k]*a[p-k]%modulus)//p**3
        assert left==right,(p,k,left,right)
        pairs+=1
    if p%6!=1:
        return pairs,None
    m=(p-1)//6
    high=(sum((6*j+1)*a[j] for j in range(4*m+1,p))%modulus)//p**3
    low=0
    for k in range(1,2*m+1):
        lam=(2*H[2*k-1]+3*H[3*k-1]-5*H[k-1]-Q)%p
        low+=((6*k-1)+p*((6*k-1)*lam-6))*pow(18*k**3*a[k],-1,p*p)
    low%=p*p
    assert high==low,(p,high,low)
    return pairs,high

def main():
    target=[p for p in primes_up_to(10000) if p%24 in(13,19)]
    assert len(target)==312
    cases={13:70,19:156,109:3677,139:6591,157:22547,
           373:109567,997:655376,2131:756}
    pairs=0
    for p in target:
        count,high=check(p,compare_factorials=p in{13,19,37,109})
        pairs+=count
        if p in cases:
            assert high==cases[p],(p,high)
    assert pairs==1475586
    others=[5,7,11,17,23,29,31,41,47,53,59]
    extra=sum(check(p,compare_factorials=p<=29)[0] for p in others)
    assert extra==312
    print('target_primes',len(target),'target_pairs',pairs,
          'outside_pairs',extra,'total',pairs+extra)
    print('top_band_regressions',cases)
    print('EXACT_INTEGER_PASS AUTHOR_SIDE UNREVIEWED NOT_ADMITTED')

if __name__=='__main__':
    main()
