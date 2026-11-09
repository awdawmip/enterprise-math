#!/usr/bin/env python3
"""Exact original-2304 grade-2/3 check; independent binomial and recurrence methods.
External all-prime proof: Guo--Zudilin, Advances in Mathematics 346 (2019),
Theorem 1.1 (arXiv:1803.01830), full and half truncations modulo p^3.
This script verifies finite examples, not the published all-prime theorem.
"""
import json
from math import comb

PRIMES = (5, 7, 11, 13, 17, 19, 37, 43, 73, 373)

def make_terms(p, method):
    mod = p**4
    if method == "binomial":
        return [((8*n+1)*comb(4*n, 2*n)*comb(2*n, n)**2 * pow(2304, -n, mod)) % mod for n in range(p)]
    assert method == "recurrence"
    coeff = 1
    out = []
    for n in range(p):
        out.append((8*n+1)*coeff % mod)
        if n+1 < p:
            num = (4*n+1)*(4*n+3)*(2*n+1)
            den = 288*(n+1)**3  # unit mod p^4 because n+1<p
            coeff = coeff*num*pow(den, -1, mod) % mod
    return out

def report(p, terms):
    mod = p**4
    n0=(p+1)//2
    n1=(3*p-1)//4
    grade2=sum(terms[n0:n1+1]) % mod
    grade3=sum(terms[n1+1:]) % mod
    full=sum(terms) % mod
    half=sum(terms[:n0]) % mod
    tail=(full-half) % mod
    assert tail == (grade2+grade3) % mod
    assert grade2 % p**3 == 0 and grade3 % p**3 == 0 and tail % p**3 == 0
    return {"p":p, "n0":n0, "n1":n1,
            "grade2_over_p3_modp":grade2//p**3,
            "grade3_over_p3_modp":grade3//p**3,
            "tail_over_p3_modp":tail//p**3,
            "grade2_over_p2_modp":(grade2//p**2)%p}

if __name__=="__main__":
    results=[]
    for p in PRIMES:
        a=make_terms(p, "binomial")
        b=make_terms(p, "recurrence")
        assert a==b, ("coefficient mismatch", p)
        results.append(report(p, a))
    print(json.dumps({"arithmetic":"exact integers in Z/p^4", "primes":list(PRIMES),
                      "independent_methods":["direct binomial","unit-denominator recurrence"],
                      "results":results}, indent=2, ensure_ascii=False))
