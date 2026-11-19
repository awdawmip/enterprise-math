#!/usr/bin/env python3
"""Exact bounded regression for a typed A2 quotient/G6 minimization bridge.

Research evidence for X6 Unit151.  No P000 axioms are altered; no R063 native
benchmark is executed.  All invariant checks are active under python -O/-OO.
"""
from itertools import product
from math import factorial
import json

R = 8
D = (1, 1, 1)


def need(cond, reason):
    if not cond:
        raise ValueError(reason)


def q(x):
    a, b, c = x
    return a*a+b*b+c*c-a*b-b*c-c*a


def g(x):
    return sum(t*t for t in x)


def s(x):
    return sum(x)


def shift(x,k):
    return tuple(t+k for t in x)


def canonical(x):
    # The unique translate whose sum is in {-1,0,+1}.
    S=s(x)
    k= -((S+1)//3)
    z=shift(x,k)
    need(s(z) in (-1,0,1), 'canonical sum')
    return z


def steps_count(x):
    n=sum(abs(t) for t in x)
    d=1
    for t in x:
        d*=factorial(abs(t))
    return factorial(n)//d


def verify():
    seen_q_mod=set()
    q0_nonzero=0
    metric_mismatch=0
    nonadditive_carry=0
    vectors=0
    transitions=0
    shift_cases=0
    for x in product(range(-R,R+1), repeat=3):
        vectors+=1
        Q=q(x)
        S=s(x)
        need(2*Q == 3*g(x)-S*S,'quadratic bridge')
        need(Q>=0,'A2 positivity')
        need(Q == ((x[0]-x[1])**2+(x[1]-x[2])**2+(x[2]-x[0])**2)//2,'A2 pairwise differences')
        need((x[0]-x[1])**2+(x[1]-x[2])**2+(x[2]-x[0])**2 == 2*Q,'A2 identity exact')
        need(Q%3 == S*S%3,'mod3 congruence')
        seen_q_mod.add(Q%3)
        need(Q%3 in (0,1),'no residue 2')
        z=canonical(x)
        m=(2*Q+Q%3)//3
        need(g(z)==m,'least G exact')
        need(g(z)==(2*Q+min((S+3*k)**2 for k in range(-R-2,R+3)))/3,'bounded min comparison')
        need(g(z)<g(shift(z,-1)) and g(z)<g(shift(z,1)),'unique nearest integer')
        if Q==0 and x!=(0,0,0): q0_nonzero+=1
        if Q!=g(x):metric_mismatch+=1
        for t in range(-2,3):
            shift_cases+=1
            y=shift(x,t)
            need(q(y)==Q,'quotient metric invariance')
            need(canonical(y)==z,'quotient section invariance')
        for i in range(3):
            for sign in (-1,1):
                transitions+=1
                e=tuple(sign if j==i else 0 for j in range(3))
                actual=tuple(z[j]+e[j] for j in range(3))
                # Finite-state common-depth carry: +/- one axis from canonical representative.
                carry = -1 if sign==1 and s(z)==1 else (1 if sign==-1 and s(z)==-1 else 0)
                target=tuple(actual[j]+carry for j in range(3))
                need(canonical(actual)==target,'operational section carry')
                if carry: nonadditive_carry+=1
    x=(1,1,0)
    z=canonical(x)
    need(z==(0,0,-1),'minimal two-step witness')
    need(q(x)==1 and g(x)==2 and g(z)==1,'native/carrier metric witness')
    need(steps_count(x)==2 and steps_count(z)==1,'native BRC witness')
    need(q((1,1,1))==0 and g((1,1,1))==3 and steps_count((1,1,1))==6,'diagonal return witness')
    need(seen_q_mod=={0,1},'observed residue classes')
    return {
      'schema':'X6_UNIT151_A2_TO_SIGNED_MIN_G_CARRY_EXACT_CERT_V1',
      'scope':'Signed Z^3 selected slice embedded in signed Z^6, derived diagonal quotient, no native time dynamics',
      'source_historical_commit':'fd2bcff10ca6e147348b6c1236027fc0d2877df3',
      'science_pin':'59538f585d037d09ef687b28715c4bc1a3f9fe03',
      'cube_radius':R, 'states_checked':vectors,'gauge_shift_checks':shift_cases,
      'primitive_transition_checks':transitions,'carry_events':nonadditive_carry,
      'q_mod3_values':sorted(seen_q_mod),'nonzero_q0_states':q0_nonzero,
      'raw_g_neq_carrier_q_states':metric_mismatch,
      'witness':{'raw':[1,1,0],'canonical':[0,0,-1], 'A2_q':1,'native_g_raw':2,'native_g_canonical':1,'BRC_raw':2,'BRC_canonical':1},
      'theorems_checked': ['Q=(3G-S²)/2','min_k G(z+kD)=ceil(2Q/3)','unique minG representative sum∈{-1,0,1}', 'section +/- axis carry','Q mod3 ∈ {0,1}'],
      'original_R063_native_benchmark_executed':False,
      'acceptance':'AUTHOR_EXACT_PROVED_FINITE_CHECKED_UNREVIEWED_NOT_ADMITTED'
    }

if __name__=='__main__':
    print(json.dumps(verify(),sort_keys=True,ensure_ascii=False,separators=(',',':')))
