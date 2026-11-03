#!/usr/bin/env python3
"""Author-side finite exact p^3 check, not a universal theorem or native benchmark."""
from math import comb, isqrt
import json

LIMIT = 2000
CROSS = {5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 43, 73, 373}


def primes_to(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for k in range(2, isqrt(n) + 1):
        if sieve[k]:
            sieve[k*k:n+1:k] = b'\x00' * (1 + (n-k*k)//k)
    return [i for i in range(5, n+1) if sieve[i]]


def recurrence(p, n):
    modulus = p**3
    val = 1
    acc = 0
    for k in range(n+1):
        acc = (acc + (6*k+1)*val) % modulus
        if k < n:
            val = (val * (2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3, -1, modulus))%modulus
    return acc


def binomial_direct(p, n):
    modulus = p**3
    inv216 = pow(216, -1, modulus)
    denominator = 1
    acc = 0
    for k in range(n+1):
        numer = comb(2*k,k)**2 * comb(3*k,k)
        acc = (acc + (6*k+1)*numer*denominator) % modulus
        denominator = denominator*inv216 % modulus
    return acc


def factorial_v(n,p):
    s=0
    while n:
        n//=p
        s+=n
    return s


def expected_v(p,k):
    return (int(k>p//3) + int(k>p//2) + int(k>(2*p)//3))


def main():
    ps=primes_to(LIMIT)
    assert len(ps)==301
    allpass=0; split=0; inert=0; profile_checks=0; direct_checks=0
    examples=[]
    for p in ps:
        m=p**3
        full=recurrence(p,p-1)
        trunc=recurrence(p,2*p//3)
        sign=1 if p%3==1 else -1
        expect=(sign*p)%m
        assert full==expect, ('character mismatch', p,full,expect)
        assert trunc==full, ('tail mismatch',p)
        for k in range(p):
            observed=(factorial_v(2*k,p)+factorial_v(3*k,p)-5*factorial_v(k,p))
            assert observed==expected_v(p,k),(p,k,observed,expected_v(p,k))
            profile_checks+=1
        if p in CROSS:
            assert binomial_direct(p,p-1)==full, ('independent binomial mismatch',p)
            direct_checks+=1
        split+=sign==1
        inert+=sign==-1
        allpass+=1
        if p in {5,7,11,13,19,31,37,73,373,1999}:
            half=recurrence(p,(p-1)//2)
            examples.append({'p':p,'p_mod_6':p%6,'W_mod_p3':full,
               'signed_p_mod_p3':expect,'half_truncation_mod_p3':half,
               'valuation_cutoff':2*p//3})
    assert (split,inert)==(148,153)
    report={"scope":"all primes 5<=p<=2000", "total_primes":allpass,
       "p_1_mod_3":split,"p_2_mod_3":inert,
       "character_congruence_failures":0,"exact_tail_failures":0,
       "valuation_indices_verified":profile_checks,
       "independent_binomial_crosschecks":direct_checks,
       "proof_strength":"universal valuation theorem; finite exact character experiment only",
       "examples":examples}
    print(json.dumps(report,indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
