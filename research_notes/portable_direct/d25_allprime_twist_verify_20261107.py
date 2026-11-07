#!/usr/bin/env python3
"""Exact finite p-adic tests for original216 across BOTH mod-3 prime classes.
No external packages, floating point, or mathematical acceptance implied.
"""
from math import comb, isqrt

def primes_below(limit):
    sieve = bytearray(b'\x01') * limit
    sieve[:2] = b'\x00\x00'
    for d in range(2, isqrt(limit - 1) + 1):
        if sieve[d]:
            sieve[d*d:limit:d] = bytes(len(range(d*d, limit, d)))
    return [p for p in range(5,limit) if sieve[p]]

def original216(p, exponent=3):
    modulus = p**exponent
    inv36 = pow(36, -1, modulus)
    fac_inv = [1] * p
    for k in range(1,p):
        fac_inv[k] = (fac_inv[k-1] * pow(k,-1,modulus)) % modulus
    term, acc = 1,0
    for k in range(p):
        acc = (acc + (6*k+1)*term) % modulus
        if k+1 < p:
            term = (term*(2*k+1)*(3*k+1)*(3*k+2)*inv36 * fac_inv[k+1]**3)%modulus
    return acc

def original216_fast(p, exponent=3):
    modulus = p**exponent
    a, acc = 1,0
    for k in range(p):
        acc = (acc+(6*k+1)*a)%modulus
        if k+1 < p:
            a = a*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,modulus)%modulus
    return acc

def binomial_independent(p, exponent=3):
    modulus = p**exponent
    inverse216 = pow(216,-1,modulus)
    a_power,acc=1,0
    for k in range(p):
        numerator=(comb(2*k,k)**2)*comb(3*k,k)
        acc=(acc+(6*k+1)*numerator*a_power)%modulus
        a_power=a_power*inverse216%modulus
    return acc

def verify():
    ps=primes_below(10000)
    by_class={1:0,2:0}; errors=[]
    examples={5,7,11,13,19,31,37,43,61,67,73,199,373,1009,5003,9967}
    rows=[]
    for p in ps:
        residue=1 if p%3==1 else 2
        sign=1 if residue==1 else -1
        value=original216_fast(p)
        by_class[residue]+=1
        if value!=(sign*p)%(p**3):
            errors.append((p,value,sign*p))
        if p<=401:
            assert binomial_independent(p)==value, (p, value,binomial_independent(p))
        if p in examples:
            high=original216_fast(p,4)
            fourth=((high-sign*p)%(p**4))//p**3
            rows.append((p,residue,value,fourth))
    print('range p<10000, p>3, total',len(ps), 'classes',by_class, 'failures',len(errors))
    print('independent exact binomial checks',sum(p<=401 for p in ps))
    print('examples (p,p mod3,W mod p^3, (W-chi*p)/p^3 modp):')
    for row in rows:print(row)
    if errors: print('first errors',errors[:12]); raise AssertionError('conjecture falsified')
    # Sharp modulus test witness p=7: (W_7-7)/7^3=1 mod7.
    assert ((original216_fast(7,4)-7)%(7**4))//(7**3)==1
if __name__ == '__main__': verify()
