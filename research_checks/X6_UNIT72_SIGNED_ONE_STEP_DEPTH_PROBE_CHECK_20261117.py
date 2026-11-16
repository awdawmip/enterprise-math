#!/usr/bin/env python3
"""Author-side exact integer check for Unit72; does not import the frozen native benchmark.
Frozen math: Enterprise Math P000 V5 signed X6, selected axes (0,1,2), remaining zeros.
"""
from collections import defaultdict
from itertools import product
from math import isqrt, factorial
import json

BOUND = 12

def data(z):
    h = min(z)
    r = tuple(x-h for x in z)
    return (r, sum(x*x for x in z), sum(abs(x) for x in z))

def roots(r, g, t):
    # min(r)=0, so g >= h*h for every possible native depth.
    return [h for h in range(-isqrt(g), isqrt(g)+1)
            if sum((x+h)**2 for x in r)==g
            and sum(abs(x+h) for x in r)==t]

def n_brc(z):
    ans = factorial(sum(abs(v) for v in z))
    for v in z: ans //= factorial(abs(v))
    return ans

def run():
    seen = defaultdict(int)
    for z in product(range(-BOUND, BOUND+1), repeat=3):
        seen[data(z)] += 1
    two = 0
    tests = 0
    same_mass = 0
    different_mass = 0
    for (r, g, t), count in seen.items():
        H = roots(r, g, t)
        if len(H) > 2: raise AssertionError(('too_many_roots',r,g,t,H))
        if len(H) != 2: continue
        two += 1
        R=sum(r)
        d=R*R+3*(g-sum(x*x for x in r))
        if d<=0 or isqrt(d)**2!=d or H!=[(-R-isqrt(d))//3,(-R+isqrt(d))//3]:
            raise AssertionError(('bad_quadratic',r,g,t,H,d))
        zlo, zhi = [tuple(x+h for x in r) for h in H]
        if n_brc(zlo)==n_brc(zhi): same_mass+=1
        else: different_mass+=1
        for i in range(3):
            delta = [2*(r[i]+h)+1 for h in H]   # G(z+e_i)-G(z), exact native components
            threshold_3 = 3+6*r[i]-2*R    # 3 times threshold; entirely integral
            margins = [3*x-threshold_3 for x in delta]
            if margins != [-2*isqrt(d), 2*isqrt(d)]:
                raise AssertionError(('probe_failure',r,g,t,i,H,delta,margins))
            tests += 1
    def example(r,g,t,i):
        H=roots(r,g,t)
        R=sum(r)
        return {'r':r,'G':g,'T':t,'depths':H,
                'native_z':[tuple(x+h for x in r) for h in H],
                'N_BRC':[n_brc(tuple(x+h for x in r)) for h in H],
                'probe_axis':i,
                'delta_G':[2*(r[i]+h)+1 for h in H],
                'threshold_times_three':3+6*r[i]-2*R}
    return {'schema':'EM_X6_UNIT72_ONE_STEP_PROBE_AUTHOR_EXACT_V1',
            'date':'2026-11-17', 'frozen_source':'59538f585d037d09ef687b28715c4bc1a3f9fe03',
            'method':'independent exact integer enumeration; no original-source benchmark import',
            'input_cube':[-BOUND,BOUND], 'input_count':(2*BOUND+1)**3,
            'distinct_observer_signatures':len(seen),
            'signatures_with_two_global_candidates':two,
            'axis_probe_comparisons':tests,
            'equal_unweighted_BRC_double_signatures':same_mass,
            'unequal_unweighted_BRC_double_signatures':different_mass,
            'failures':0,
            'different_BRC_example':example((3,0,0),18,6,1),
            'same_BRC_example':example((0,2,4),11,5,0)}

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,sort_keys=True,indent=2))
