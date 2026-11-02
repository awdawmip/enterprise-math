#!/usr/bin/env python3
"""Test conjectural W_full(p-1) = p * ( -3 / p ) mod p^3.
Exploration only; not an accepted universal theorem and not native H0/B0.
"""
from math import isqrt
import json

def primes_upto(n):
    a=bytearray(b'\x01')*(n+1);a[0:2]=b'\x00\x00'
    for d in range(2,isqrt(n)+1):
        if a[d]:a[d*d:n+1:d]=b'\x00'*(((n-d*d)//d)+1)
    return [p for p in range(5,n+1) if a[p]]

def weighted_W(p):
    m=p**3
    a=1; w=1
    for k in range(1,p):
        a=a*(2*k)*(2*k-1)*(3*k)*(3*k-1)*(3*k-2)*pow(216*k**5,-1,m)%m
        w=(w+(6*k+1)*a)%m
    return w

if __name__=='__main__':
    limit=10000
    primes=primes_upto(limit)
    bad=[];counts={1:0,5:0};samples={}
    for p in primes:
        chi=1 if p%3==1 else -1
        actual=weighted_W(p)
        counts[p%6]+=1
        if actual!=(p*chi)%(p**3):bad.append({'p':p,'actual':actual,'expected':(p*chi)%(p**3)})
        if p in [5,7,11,13,19,31,373,3019]:samples[str(p)]={'W_mod_p3':actual,'chi_minus3':chi}
    print(json.dumps({'schema':'AUTHOR_D25_ORIGINAL_W_CHARACTER_FINITE_TEST_V1','status':'FINITE_EXACT_EXECUTED_NOT_UNIVERSAL_PROOF',
     'range':'all primes 5<=p<=10000','count':len(primes),'pmod6_counts':counts,
     'candidate':'W_full(p-1) = p*( (-3)/p ) mod p^3',
     'failures':bad[:20],'failure_count':len(bad),'samples':samples},indent=2))
