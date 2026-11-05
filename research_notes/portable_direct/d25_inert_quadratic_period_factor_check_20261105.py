#!/usr/bin/env python3
"""D25 exact F_(p^2) test of a conditional analytic period multiplier.
Does NOT compute native H0/B0 or establish a p-adic finite-sum identity.
"""
from sympy import primerange
import json

def mul(a, b, p):
    return ((a[0]*b[0] + 2*a[1]*b[1]) % p,
            (a[0]*b[1] + a[1]*b[0]) % p)

def power(a, n, p):
    y = (1, 0)
    while n:
        if n & 1:
            y = mul(y, a, p)
        a = mul(a, a, p)
        n >>= 1
    return y

def check(p):
    assert p % 24 in (13, 19)
    assert pow(2, (p-1)//2, p) == p-1
    s = (0, 3*pow(4, -1, p) % p)
    eta = (0, 2*pow(3, -1, p) % p)
    sigma_s = power(s, p, p)
    sigma_eta = power(eta, p, p)
    ns = mul(s, sigma_s, p)
    ne = mul(eta, sigma_eta, p)
    assert power(s, 2, p) == (9*pow(8, -1, p) % p, 0)
    assert sigma_s == (0, -s[1] % p)
    assert ns == (-9*pow(8, -1, p) % p, 0)
    assert sigma_eta == (0, -eta[1] % p)
    assert ne == (-8*pow(9, -1, p) % p, 0)
    assert mul(s, eta, p) == (1, 0)
    assert mul(ns, ne, p) == (1, 0)
    for a, b in ((0, 0), (0, 1), (1, 0), (1, 1), (p-1, 7)):
        t = (a, b)
        assert (mul(t, s, p)[1] == 0) == (a == 0)
    return dict(p=p, s_T=s[1], s2=power(s, 2, p)[0], norm_s=ns[0])

if __name__ == "__main__":
    rows = [check(p) for p in primerange(5, 10000)
            if p % 24 in (13, 19)]
    print(json.dumps({"tested_primes":len(rows), "failures":0,
        "examples":[r for r in rows if r["p"] in (13, 19, 139, 373)],
        "claim":"finite-field lemma algebraically proved; finite check only",
        "native_H0B0_executed":False}, indent=2))
