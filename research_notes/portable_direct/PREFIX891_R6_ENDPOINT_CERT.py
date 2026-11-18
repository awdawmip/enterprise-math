#!/usr/bin/env python3
"""PREFIX-891: exact endpoint-witness criterion and 16 disjoint-axis rows.
Frozen science pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Python 3 standard library only; integers are exact.
"""
from math import gcd
from collections import defaultdict
import json

P, N, LO, HI = 32, 1 << 32, 262145, 524287
PANEL = [262147, 280001, 300001, 320003, 340007, 360007, 380003,
         400009, 420001, 440003, 460001, 480007, 500383, 510007,
         520001, 524285]

def axis(q, p=P):
    return any(pow(2, h, q) in (1, q-1) for h in range(1, p))

def endpoint(p, q1, q2):
    """Return (x,u,i,k,kind), an explicit zero-flip collision, or None."""
    n = 1 << p
    if gcd(q1, q2) != 1:
        return None
    K = (n-1)//q1
    if not K:
        return None
    inv = pow(q1, -1, q2)
    for i in range(p):
        b = 1 << i
        r = (b * inv) % q2
        if r <= K:
            u, k, kind = n-1, r, 'DOWN_END'
        elif (q2-r)*q1+b < n:
            u, k, kind = n-1-b, q2-r, 'UP_END'
        else:
            continue
        x = u-k*q1
        assert 0 <= x < n and x%q1 == u%q1
        assert x%q2 == (u ^ b)%q2
        return (x,u,i,k,kind)
    return None

def direct(p,q1,q2):
    n = 1 << p
    fiber = defaultdict(int)
    for u in range(n):
        for i in range(p):
            fiber[u%q1,(u^(1 << i))%q2] += 1
    return any(fiber[x%q1,x%q2] for x in range(n))

def main():
    brute = 0
    for p in range(1, 9):
        for q1 in range(3,20,2):
            for q2 in range(3,20,2):
                assert (endpoint(p,q1,q2) is not None) == direct(p,q1,q2)
                brute += 1
    assert all(not axis(q) for q in PANEL)
    special = {262147, 300001, 400009, 500383, 524285}
    independently_confirmed = {
      262147:(103640,103623), 300001:(89859,89846),
      400009:(84913,84898), 500383:(66613,66603),
      524285:(49010,49001)}
    a = {q:axis(q) for q in range(LO,HI+1,2)}
    rows=[]
    for q1 in PANEL:
        hits=free=overlap=noncoprime=0
        first=None
        for q2 in range(LO,HI+1,2):
            if gcd(q1,q2)>1: noncoprime += 1
            witness = endpoint(P,q1,q2)
            if witness is not None:
                hits += 1
                if a[q2]: overlap += 1
                else:
                    free += 1
                    if first is None: first={'q2':q2, 'x':witness[0],
                        'u':witness[1], 'i':witness[2], 'k':witness[3],
                        'kind':witness[4]}
        assert hits == free+overlap
        if q1 in special:
            assert (hits,free)==independently_confirmed[q1]
        rows.append(dict(q1=q1,pairs=131072,noncoprime=noncoprime,
                         zero_flip_positive=hits,axis_overlap=overlap,
                         axis_free=free,first_axis_free_witness=first))
    totals={k:sum(r[k] for r in rows) for k in
            ('pairs','noncoprime','zero_flip_positive','axis_overlap','axis_free')}
    out={'schema':'PREFIX891_R6_ENDPOINT_CERT_V1',
         'frozen_scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
         'domain':{'p':P,'odd_q2_min':LO,'odd_q2_max':HI,
                   'q2_count':131072,'axis_q2_count':sum(a.values()),
                   'axis_free_q1_panel':PANEL},
         'proof_basis':'r_i = (2^i)*(q1^-1 mod q2) mod q2; k=r_i or q2-r_i',
         'small_full_bruteforce_triples':brute,
         'independent_full_row_crosschecks':list(sorted(special)),
         'rows':rows,'totals':totals,
         'classification':'AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED'}
    print(json.dumps(out,indent=2,ensure_ascii=False,sort_keys=True))

if __name__=='__main__': main()
