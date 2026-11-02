#!/usr/bin/env python3
"""Independent exact arithmetic for the W216 truncated all-precision tower.

Original coefficients: binom(2k,k)^2 binom(3k,k)/216^k.
Second computation: 3-band tagged p-adic factorization and symmetric ports.
No external packages or floating arithmetic; no native benchmark claim.
"""
from math import comb, isqrt
from collections import defaultdict
import json


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def original(p, q):
    r = (p-1)//6
    modulus = p**q
    b = 1
    total = 0
    for k in range(4*r+1):
        total = (total+(6*k+1)*b) % modulus
        if k < 4*r:
            b = (b*(2*k+1)*(3*k+1)*(3*k+2)
                 * pow(36*(k+1)**3, -1, modulus)) % modulus
    return total


def independent_binomial_boundary_check(p, q=4):
    r = (p-1)//6
    modulus = p**q
    cutoffs = sorted({0, 2*r, 2*r+1, 3*r, 3*r+1, 4*r})
    b = 1
    checked = []
    for k in range(4*r+1):
        if k in cutoffs:
            from_binom = (comb(2*k,k)**2 * comb(3*k,k)
                          * pow(216,-k,modulus)) % modulus
            assert b == from_binom, (p,k,b,from_binom)
            checked.append(k)
        if k < 4*r:
            b = (b*(2*k+1)*(3*k+1)*(3*k+2)
                 * pow(36*(k+1)**3,-1,modulus)) % modulus
    return checked


def tagged_ports(p, q):
    assert p >= 7 and p%6 == 1 and is_prime(p) and q>=3
    r = (p-1)//6
    modulus = p**q
    # Each tagged a satisfies a = -n + p*a exactly.
    # Cross j=n only once, contributes p*a; retain other 1+p*a/(j-n).
    n_a = [(3*r,1,2), (2*r,1,3), (4*r,2,3)]
    star = 1
    valuation = 0
    es = [1] + [0]*(q-1)
    ports = defaultdict(int)
    for k in range(4*r+1):
        assert valuation == ((k>2*r)+(k>3*r))
        for t in range(q-valuation):
            ports[(valuation,t)] = (
                ports[(valuation,t)]+(6*k+1)*star*es[t]) % modulus
        if k == 4*r:
            break
        for n,num,den in n_a:
            if k == n:
                valuation += 1
                star = star*num*pow(den,-1,modulus) % modulus
            else:
                u = num*pow((k-n)*den % modulus,-1,modulus) % modulus
                for t in range(q-1,0,-1):
                    es[t] = (es[t]+u*es[t-1]) % modulus
                star = star*(k-n) % modulus
        star = star*pow(2*(k+1)**3,-1,modulus) % modulus
    total = sum(pow(p,v+t,modulus)*c
                for (v,t),c in ports.items()) % modulus
    return total, ports


def run():
    cases = [(7,3),(7,4),(7,5),(7,7),(13,4),(13,5),(13,14),
             (19,4),(19,5),(31,4),(37,4),(43,4),(61,4),
             (373,4),(373,5),(1171,4)]
    report = {
        "schema":"D25_W216_ALL_ORDER_PORTS_EXACT_CHECK_V1",
        "target":"W(4r) modulo p^q",
        "tests":[],
        "independent_boundary_binomial_checks":{},
        "full_range":{"limit":3000,"q":4,"count":0,"failures":[]}
    }
    for p,q in cases:
        w0 = original(p,q)
        w1,ports = tagged_ports(p,q)
        assert w0==w1,(p,q,w0,w1)
        entry = {"p":p,"q":q,"modulus":p**q,
                 "W_original":w0,"W_ports":w1,
                 "port_count":len(ports),
                 "target_p3_verified":w0%(p**3)==p}
        if q>=4 and w0%(p**3)==p:
            entry["fourth_digit"]=((w0-p)//(p**3))%p
        if p==373 and q==4:
            entry["port_table"]={
                f"v{v}_e{t}":{
                    "raw":c,
                    "contribution":(p**(v+t)*c)%(p**q),
                    "raw_mod_p":c%p
                }
                for (v,t),c in sorted(ports.items())
            }
        report["tests"].append(entry)
    for p in [7,13,19,31,37,43,373,1171]:
        report["independent_boundary_binomial_checks"][str(p)] = (
            independent_binomial_boundary_check(p,4))
    for p in range(7,3001,6):
        if not is_prime(p):
            continue
        w0 = original(p,4)
        w1,_ = tagged_ports(p,4)
        report["full_range"]["count"] += 1
        if w0 != w1:
            report["full_range"]["failures"].append(
                {"p":p,"original":w0,"ports":w1})
    assert not report["full_range"]["failures"]
    print(json.dumps(report,indent=2,ensure_ascii=False,sort_keys=True))
    return report


if __name__=="__main__":
    run()
