#!/usr/bin/env python3
"""Exact finite regression of D25 full-band p-adic reflection product, p>3."""
from math import factorial
def primes_upto(n):
    s=bytearray([1])*(n+1)
    s[:2]=b"\x00\x00"
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=b"\x00"*(((n-i*i)//i)+1)
    return [p for p in range(5,n+1) if s[p]]
def check(p):
    mod=p**4
    a=[1]
    for k in range(p-1):
        a.append(a[-1]*(2*k+1)*(3*k+1)*(3*k+2)
                 *pow(36*(k+1)**3,-1,mod)%mod)
    for k in range(1,p):
        q2=2*k//p
        q3=3*k//p
        right= (-(-1)**(q2+q3)*factorial(q3)*factorial(2-q3)
                *pow(36*k**3,-1,p))%p
        product=a[k]*a[p-k]%mod
        assert product%p**3==0, (p,k,'valuation')
        assert product//p**3==right, (p,k,product//p**3,right)
    return p-1
if __name__=="__main__":
    eligible=[p for p in primes_upto(10000) if p%24 in (13,19)]
    assert len(eligible)==312
    a=sum(check(p) for p in eligible)
    other=[5,7,11,17,23,29,31,41,47,53,59]
    b=sum(check(p) for p in other)
    assert (a,b)==(1475586,312)
    print('eligible_primes=',len(eligible),'eligible_pairs=',a,
          'outside_pairs=',b,'total_exact_checked=',a+b)
