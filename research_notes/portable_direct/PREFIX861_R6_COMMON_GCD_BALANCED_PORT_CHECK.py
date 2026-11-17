#!/usr/bin/env python3
"""Exact integer checks for named binary-source two-read gcd construction.
Scope: abstract auxiliary BRC modular observation, terminal state only.
"""
import json
from math import gcd, isqrt, ceil, log2
from collections import defaultdict

def half_order(q):
    a=2%q
    for d in range(1, 5*q+1):
        if a==1 or a==q-1:return d
        a=a*2%q
    raise AssertionError('missing period')

def g_of_p(p):
    g=3
    while half_order(g)<p:g*=3
    return g

def candidate(p):
    N=1<<p;g=g_of_p(p)
    a=1
    while g*a*(a+2)<N:a+=2
    b=a+2
    return N,g,a,b,g*a,g*b

def exact_check(p,q1,q2):
    # Different end states cannot have same two residues, even for different prior source states.
    N=1<<p
    observations={}
    n_transitions=0
    for prior in range(N):
        for curr in [prior]+[prior^(1<<i) for i in range(p)]:
            n_transitions+=1
            pair=(prior%q1,curr%q2)
            prev=observations.setdefault(pair,curr)
            if prev!=curr:
                return dict(pass_check=False,p=p,collision=[prior,curr,prev],pair=pair)
    return dict(pass_check=True,p=p,trajectories=n_transitions,distinct_output_pairs=len(observations))

def delta_check(p,g):
    e=[0]+[k*(1<<i) for i in range(p) for k in (-1,1)]
    residues=[v%g for v in e]
    return len(residues)==len(set(residues))

rows=[]
for p in range(1,19):
    N,g,a,b,q1,q2=candidate(p)
    h=half_order(g)
    assert h>=p and delta_check(p,g) and gcd(q1,q2)==g and q1*q2//g>=N
    rec={"p":p,"N":N,"g":g,"h":h,"a":a,"b":b,"q1":q1,"q2":q2,"lcm":q1*q2//g,"bits1":q1.bit_length(),"bits2":q2.bit_length(),"both_noninjective":q2<N}
    if p<=12:
        rec.update(exact_check(p,q1,q2))
        assert rec['pass_check']
    rows.append(rec)
print(json.dumps({'schema':'PREFIX861_BALANCED_GCD_V1','theory':'gcd-compatible update label plus CRT terminal reconstruction','rows':rows,'assertions':'ALL_EXACT_ASSERTIONS_PASSED'},ensure_ascii=False,indent=2))
