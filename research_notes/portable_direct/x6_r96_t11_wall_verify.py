#!/usr/bin/env python3
"""Exact finite spot-check of the analytic T=11 all-Port tie atlas (author test)."""
from fractions import Fraction
from itertools import product
import json

QMAX = 40
SAMPLES = [(1,1),(4,1),(5,1),(13,2),(7,1),(21,2),(11,1),(23,2),(100,1)]
PORTS = [11,15,16,17,20,21,26,27,40]
CANDIDATES = [
    ((10,-5,1), 11, 1),
    ((5,-4,1), 6, 5), ((9,-5,1), 10, 5),
    ((15,-9,2), 17, 7), ((19,-10,2), 21, 7),
    ((14,-9,2), 16, 11), ((24,-14,3), 27, 11),
]

def budget(a):
    return max(sum(max(t,0) for t in a),sum(max(-t,0) for t in a))

def canon(a):
    return a if next(t for t in a if t)!=0 and next(t for t in a if t)>0 else tuple(-t for t in a)

def gaps(a):
    x,y,z=a
    u=x+3*y+6*z;v=3*x+12*y+30*z;h=7*x+39*y+126*z
    return abs(u),abs(v),abs(h),abs(v-u),abs(h-u),abs(h-v)

def score(g,S):
    return max(Fraction(g[0],2),Fraction(g[1],1+S),Fraction(g[2],12),
               Fraction(g[3],1+S),Fraction(g[4],12),Fraction(g[5],S+11))

def predicted(p,S):
    if S>11 and p>=27:
        return {(24,-14,3)}
    return {a for (a,q,threshold) in CANDIDATES if q<=p and S>=threshold}

items=[]
for a in product(range(-QMAX,QMAX+1),repeat=3):
    q=budget(a)
    if q==0 or q>QMAX or canon(a)!=a:
        continue
    items.append((q,a,gaps(a)))
assert len(items)==110740, len(items)
rows=[]
comparisons=0
for sn,sd in SAMPLES:
    S=Fraction(sn,sd)
    for p in PORTS:
        eta=Fraction(6,1+S) if S>11 and p>=27 else Fraction(1,2)
        actual=set()
        for q,a,g in items:
            if q>p: continue
            val=score(g,S)
            comparisons+=1
            assert val>=eta,(S,p,a,val,eta)
            if val==eta:actual.add(a)
        expected=predicted(p,S)
        assert actual==expected,(S,p,sorted(actual),sorted(expected))
        rows.append({'S':str(S),'p':p,'eta':str(eta),'ties':len(actual)})
report={'claim':'X6 R96 T=11 exact full-S Port tie atlas',
        'status':'AUTHOR_EXACT_FRACTION_FINITE_CHECK_PASS',
        'q_max':QMAX,'unoriented_directions':len(items),
        'parameters':len(SAMPLES),'port_budgets':len(PORTS),
        'cases':len(rows),'comparisons':comparisons,
        'samples':rows,
        'scope':'finite spot-check only; unbounded-lattice theorem uses symbolic proof'}
print(json.dumps(report,indent=2))
