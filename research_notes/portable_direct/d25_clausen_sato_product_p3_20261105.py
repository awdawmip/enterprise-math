#!/usr/bin/env python3
"""Exact author-side verification: supersingular Ramanujan-Sato product.
This is NOT a native H0/B0 divided-power experiment.
"""
import json
from math import comb

def primes_upto(bound):
    primes = []
    for x in range(2, bound+1):
        if all(x % q for q in primes if q*q <= x):
            primes.append(x)
    return primes

def bounded_valuation(x, p, limit=4):
    v = 0
    if x == 0:
        return limit
    while v < limit and x % p == 0:
        x //= p
        v += 1
    return v

def check(p):
    assert p >= 13 and p % 24 in (13, 19)
    mod = p**4
    a = [1]
    for k in range(p-1):
        a.append(a[-1] * (2*k+1) * (3*k+1) * (3*k+2)
                 * pow(36*(k+1)**3, -1, mod) % mod)
    H = sum(a) % mod
    W = sum((6*k+1)*a[k] for k in range(p)) % mod
    # Cauchy product truncated at degree p-1, not HW itself.
    # Symmetry changes weight (6*j+1) to (3*k+1).
    P = sum((3*k+1)*sum(a[j]*a[k-j] for j in range(k+1))
            for k in range(p)) % mod
    E = (H*W-P) % mod
    assert H % p**2 == 0
    assert W % p**2 == p
    assert E % p**3 == 0
    assert P % p**3 == 0
    # Independent original integer-binomial check at representative anchors.
    if p in (13,19,139,373):
        h2 = sum(comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,mod)
                 for k in range(p)) % mod
        w2 = sum((6*k+1)*comb(2*k,k)**2*comb(3*k,k)
                 * pow(216,-k,mod) for k in range(p)) % mod
        assert (h2,w2) == (H,W)
    return {
        "p":p, "H_over_p2_mod_p": H//p**2%p,
        "v_p_H_bounded4":bounded_valuation(H,p),
        "W_mod_p3":W%p**3, "P_over_p3_mod_p":P//p**3%p,
        "v_p_P_bounded4":bounded_valuation(P,p),
        "endpoint_E_over_p3_mod_p":E//p**3%p
    }

def run():
    data = [check(p) for p in primes_upto(997) if p%24 in (13,19)]
    assert len(data) == 45
    print("45 target primes pass; 0 failures")
    print("all v_p(H)=2?", all(x["v_p_H_bounded4"]==2 for x in data))
    print("all v_p(P)=3?", all(x["v_p_P_bounded4"]==3 for x in data))
    print("anchors:", [x for x in data if x["p"] in (13,19,139,373)])
    return data

if __name__=="__main__":
    run()
