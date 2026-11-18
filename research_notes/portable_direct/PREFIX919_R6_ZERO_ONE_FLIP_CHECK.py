#!/usr/bin/env python3
"""PREFIX-919: exact zero-or-one named XOR trajectory collision masses.
Run: python3 PREFIX919_R6_ZERO_ONE_FLIP_CHECK.py
"""
from collections import defaultdict
from math import gcd, lcm
import json

def mixed_scan(p, a, b):
    n = 1 << p
    mass, eligible = 0, []
    for k in range(1, (n-1)//a+1):
        A = k*a
        L = n-A
        for i in range(p):
            h = 1 << i
            r = A % (2*h)
            tau = min(r, 2*h-r)
            if (A+h) % b == 0:
                w = L-tau
                assert w >= 0
                mass += w
                if w: eligible.append((k, i, +1, w))
            if (A-h) % b == 0:
                w = L+tau
                assert w >= 0
                mass += w
                if w: eligible.append((k, i, -1, w))
    return mass, eligible

def mixed_inverse(p, a, b):
    n = 1 << p
    if gcd(a,b)>1: return 0, []
    inv = pow(a, -1, b)
    K = (n-1)//a
    total, eligible = 0, []
    for i in range(p):
        h = 1 << i
        for s in (+1,-1):
            k0 = (-s*h*inv) % b
            for k in range(k0 if k0 else b, K+1, b):
                A = k*a
                L = n-A
                r = A % (2*h)
                tau = min(r, 2*h-r)
                w = L-s*tau
                assert w >= 0
                total += w
                if w: eligible.append((k, i, s, w))
    return total, eligible

def zero_zero(p, a, b):
    n = 1 << p
    d = lcm(a,b)
    q = (n-1)//d
    return q*n - d*q*(q+1)//2

def brute(p, a, b):
    n = 1 << p
    obs = defaultdict(lambda: [0,0])
    for x in range(n):
        obs[(x%a,x%b)][0] += 1
        for i in range(p):
            obs[(x%a,(x ^ (1<<i))%b)][1] += 1
    z0 = sum(u*(u-1)//2 for u,v in obs.values())
    z1 = sum(u*v for u,v in obs.values())
    z2 = sum(v*(v-1)//2 for u,v in obs.values())
    return z0,z1,z2

def main():
    checked, coprime, noncoprime = 0,0,0
    for p in range(2,9):
        n=1<<p
        for a in range(3,min(15,n-1)+1,2):
            for b in range(3,min(15,n-1)+1,2):
                e00,e01,_=brute(p,a,b)
                scan01,_=mixed_scan(p,a,b)
                inv01,_=mixed_inverse(p,a,b)
                assert zero_zero(p,a,b)==e00, (p,a,b,"00")
                assert scan01==e01==inv01, (p,a,b,"01")
                assert e01==mixed_scan(p,b,a)[0], (p,a,b,"reversal")
                checked += 1
                if gcd(a,b)==1: coprime+=1
                else: noncoprime+=1
    p,a,b=32,321651,440665
    m0=zero_zero(p,a,b)
    m1,rows=mixed_scan(p,a,b)
    m1_inv,invrows=mixed_inverse(p,a,b)
    assert (m0,m1,len(rows))==(0,59007025662,17)
    assert m1==m1_inv and sorted(rows)==sorted(invrows)
    assert m1==mixed_scan(p,b,a)[0]
    m2=422370153289 # PREFIX-918 separately checked theorem, reused.
    output={
        "schema":"PREFIX919_ZERO_ONE_FLIP_MASS_V1",
        "model":{"p":p,"a":a,"b":b,"trajectory_types":"Z_x and F_x^i, named"},
        "small_observer_exhaustive_cases":checked,
        "small_coprime_cases":coprime,
        "small_noncoprime_cases":noncoprime,
        "zero_zero_mass":m0,
        "zero_flip_mass":m1,
        "zero_flip_positive_parameter_families":len(rows),
        "zero_flip_nonzero_fibers":[
            {"k":k,"i":i,"sign":s,"mass":w} for k,i,s,w in rows
        ],
        "independent_congruence_recount":m1_inv,
        "time_reversal_recount":mixed_scan(p,b,a)[0],
        "two_flip_mass_prefix918_reused":m2,
        "all_zero_or_one_flip_mass":m0+m1+m2
    }
    print(json.dumps(output,indent=2,ensure_ascii=False))

if __name__=="__main__":
    main()
