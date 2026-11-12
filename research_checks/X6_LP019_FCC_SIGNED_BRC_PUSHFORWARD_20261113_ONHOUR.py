#!/usr/bin/env python3
"""Author-side exact certificate: signed X6 N-BRC pushed to FCC carrier.

Source observation: experiments/x6_nonfcc_observer_switch_v42_20260906/
check_nonfcc_observer_switch.py, Git blob 2a8c8c804c6d4b0a4e0919f62235e58ccb583e4e.
This is a finite checker, not canonical admission or an original benchmark.
"""
from collections import Counter
from functools import lru_cache
from math import comb, factorial

V = ((1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1))
STEPS = V + tuple(tuple(-c for c in v) for v in V)
TARGET = (0,1,1)

@lru_cache(None)
def sgn_binomial(k, exponent):
    if abs(exponent) > k or (k-exponent) % 2:
        return 0
    return comb(k, (k+exponent)//2)

def pair_formula(n, y):
    x,y0,z = y
    ans = 0
    for a in range(n+1):
        for b in range(n-a+1):
            c = n-a-b
            coeff = (sgn_binomial(a+b, x)*
                     sgn_binomial(a+c, y0)*
                     sgn_binomial(b+c, z))
            if coeff:
                ans += (factorial(n)//factorial(a)//factorial(b)//factorial(c))*coeff
    return ans

def projected(z):
    return tuple(sum(z[i]*V[i][j] for i in range(6)) for j in range(3))

def advance_carrier(dist):
    new = Counter()
    for y, count in dist.items():
        for step in STEPS:
            new[tuple(u+v for u,v in zip(y,step))] += count
    return new

def advance_native(dist):
    new = Counter()
    for z, count in dist.items():
        for axis in range(6):
            for sign in (-1,1):
                nxt=list(z); nxt[axis]+=sign
                new[tuple(nxt)]+=count
    return new

def main():
    native = Counter({(0,)*6: 1})
    carrier = Counter({(0,0,0): 1})
    exact_formula_states = 0
    exact_native_states = 0
    results = []
    for n in range(9):
        pushed=Counter()
        for z,count in native.items():
            pushed[projected(z)] += count
        assert pushed==carrier, ('pushforward',n)
        assert sum(native.values())==12**n, ('mass',n)
        exact_native_states += len(native)
        for y,count in carrier.items():
            assert pair_formula(n,y)==count, ('formula',n,y,count)
            exact_formula_states += 1
        results.append((n, len(native), len(carrier), carrier[TARGET], carrier[(0,0,0)]))
        if n<8:
            native=advance_native(native)
            carrier=advance_carrier(carrier)
    # Source-level witness: one carrier point, two length-2 signed native endpoints.
    one=(0,0,0,0,1,0)
    two_a=(0,-1,1,0,0,0)
    two_b=(1,0,0,-1,0,0)
    assert projected(one)==projected(two_a)==projected(two_b)==TARGET
    assert sum(abs(c) for c in one)==1
    assert sum(abs(c) for c in two_a)==sum(abs(c) for c in two_b)==2
    assert results[1][3]==1 and results[2][3]==4
    print('PASS FCC_SIGNED_X6_N_BRC_EXACT')
    print('native_endpoints_checked', exact_native_states)
    print('carrier_formula_states_checked', exact_formula_states)
    print('n,native_states,carrier_states,target_011_brc,zero_brc')
    for row in results: print(*row,sep=',')

if __name__=='__main__':
    main()
