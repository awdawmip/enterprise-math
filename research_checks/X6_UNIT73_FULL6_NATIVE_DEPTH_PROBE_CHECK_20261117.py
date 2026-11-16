#!/usr/bin/env python3
"""Exact full signed X6 common-depth probe test, author-side independent oracle.
P000 V5; frozen mathematical source 59538f585d037d09ef687b28715c4bc1a3f9fe03.
No import/re-execution of prior R063 benchmark.
"""
from collections import Counter
from itertools import product
from math import isqrt, factorial
import json

BOUND=3
N=6

def observation(z):
    h=min(z)
    r=tuple(x-h for x in z)
    return (r,sum(x*x for x in z),sum(abs(x) for x in z))

def global_depths(r,g,t):
    R=sum(r);Q=sum(x*x for x in r)
    D=R*R+N*(g-Q)
    if D<0 or isqrt(D)**2!=D: return []
    d=isqrt(D)
    values=set()
    for u in [-d,d]:
        numerator=-R+u
        if numerator%N==0:
            h=numerator//N
            if sum(abs(x+h) for x in r)==t and sum((x+h)**2 for x in r)==g:
                values.add(h)
    return sorted(values)

def brc(z):
    t=sum(abs(x) for x in z)
    ans=factorial(t)
    for x in z: ans//=factorial(abs(x))
    return ans

def run():
    signatures=Counter(observation(z) for z in product(range(-BOUND,BOUND+1),repeat=N))
    double=0
    double_both_in_cube=0
    equal=0
    unequal=0
    checks=0
    examples={}
    for (r,g,t),occur in signatures.items():
        roots=global_depths(r,g,t)
        if not 1 <= len(roots) <= 2:
            raise ValueError(('observed_signature_bad_candidate_count',r,g,t,roots))
        if len(roots)!=2:continue
        double+=1
        double_both_in_cube+=int(occur==2)
        R=sum(r);Q=sum(x*x for x in r)
        D=R*R+N*(g-Q)
        d=isqrt(D)
        if d==0 or roots!=[(-R-d)//N,(-R+d)//N]:
            raise ValueError(('quadratic_bad',r,g,t,roots,D))
        pair=[tuple(x+h for x in r) for h in roots]
        masses=[brc(z) for z in pair]
        equal_mass=masses[0]==masses[1]
        equal+=int(equal_mass)
        unequal+=int(not equal_mass)
        for i in range(N):
            diffs=[2*(r[i]+h)+1 for h in roots]
            K=N+2*N*r[i]-2*R
            margins=[N*delta-K for delta in diffs]
            if margins!=[-2*d,2*d]:
                raise ValueError(('probe_bad',r,g,t,roots,i,diffs,margins))
            checks+=1
        typ='equal' if equal_mass else 'unequal'
        if typ not in examples:
            i=0
            examples[typ]={'r':r,'G':g,'T':t,'depths':roots,'native_z':pair,
                           'N_BRC':masses,'probe_axis':i,'delta_G':[2*(r[i]+h)+1 for h in roots],
                           'threshold_times_six':N+2*N*r[i]-2*R,
                           'comparator_margins':[-2*d,2*d]}
    return {'schema':'EM_X6_UNIT73_FULL6_NATIVE_PROBE_AUTHOR_EXACT_V1',
            'date':'2026-11-17',
            'frozen_source':'59538f585d037d09ef687b28715c4bc1a3f9fe03',
            'method':'full six-axis independent exact integer oracle, no original benchmark import',
            'input_cube':[-BOUND,BOUND],'input_count':(2*BOUND+1)**N,
            'observed_passive_signatures':len(signatures),
            'global_two_depth_signatures':double,
            'both_depths_seen_inside_input_cube':double_both_in_cube,
            'equal_N_BRC_signatures':equal,'unequal_N_BRC_signatures':unequal,
            'six_axis_probe_comparisons':checks,'failures':0,
            'examples':examples}
if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True,ensure_ascii=False))
