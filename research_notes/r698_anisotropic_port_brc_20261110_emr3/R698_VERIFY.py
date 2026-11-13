#!/usr/bin/env python3
"""R698 exact positive-rational BRC port test; standard-library only."""
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict
from math import factorial, prod
import json

MASKS = tuple(range(16))
def ids(a):
    return tuple(i for i in range(4) if a & (1 << i))
def sumw(a, w):
    return sum((w[i] for i in ids(a)), F(0))
def trans(a, w):
    d = {a: F(1)-sumw(a,w)}
    for i in ids(a):
        d[a & ~(1 << i)] = w[i]
    assert all(x >= 0 for x in d.values())
    assert sum(d.values(), F(0)) == 1
    return d
def dp(a, n, w):
    v = {a:F(1)}
    for step in range(n):
        z = defaultdict(F)
        for state, mass in v.items():
            for dest, p in trans(state,w).items():
                z[dest] += mass*p
        v = dict(z)
        assert sum(v.values(), F(0)) == 1
    return v
def ie(a, b, n, w):
    if b & ~a:
        return F(0)
    remaining = a & ~b
    return sum(((-1)**len(ids(c))*(1-sumw(b|c,w))**n
                for c in MASKS if not(c & ~remaining)),F(0))
def ej(a,j,w):
    return sum((prod((w[i] for i in c),start=F(1))
                for c in combinations(ids(a),j)), F(0))
def signature(a,w):
    return tuple(sorted(w[i] for i in ids(a)))
def frac(p):
    return [p.numerator,p.denominator]

w=tuple(F(i,10) for i in (1,2,3,4))
checks=0
for a in MASKS:
    for n in range(13):
        masses=dp(a,n,w)
        for b in MASKS:
            assert masses.get(b,F(0)) == ie(a,b,n,w)
            checks += 1
    for j in range(len(ids(a))+1):
        masses=dp(a,j,w)
        observed=sum((p for b,p in masses.items()
                      if len(ids(b))==len(ids(a))-j),F(0))
        assert observed==factorial(j)*ej(a,j,w)
assert checks==3328

multiplicities=[((1,1,1,1),5),((1,1,1,2),8),
                ((1,1,2,2),9),((1,1,2,3),12),
                ((1,2,3,4),16)]
for nums,count in multiplicities:
    rates=tuple(F(i,12) for i in nums)
    assert len({signature(a,rates) for a in MASKS})==count
    laws={}
    for a in MASKS:
        laws[a]=tuple(
            tuple(sum((p for b,p in dp(a,n,rates).items()
                       if len(ids(b))==k),F(0)) for k in range(5))
            for n in range(5))
    for a in MASKS:
        for b in MASKS:
            assert (signature(a,rates)==signature(b,rates)) == (laws[a]==laws[b])

a=(1<<0)|(1<<3)
b=(1<<1)|(1<<2)
assert len(ids(a))==len(ids(b))==2
assert sumw(a,w)==sumw(b,w)==F(1,2)
p_a=dp(a,2,w).get(0,F(0))
p_b=dp(b,2,w).get(0,F(0))
assert (p_a,p_b)==(F(2,25),F(3,25))
tau=lambda n: ie(15,0,n,w)
E=sum(((-1)**(len(ids(s))+1)/sumw(s,w)
       for s in MASKS if s),F(0))
assert (E,tau(4),tau(8))==(F(445,36),F(36,625),F(319977,781250))
assert all(dp(15,n,w).get(0,F(0))==tau(n) for n in range(21))
spectral=defaultdict(int)
for s in MASKS:
    spectral[sumw(s,w)]+=(-1)**len(ids(s))
assert {k:v for k,v in spectral.items() if v}=={
    F(0):1,F(1,10):-1,F(1,5):-1,F(1,2):2,
    F(4,5):-1,F(9,10):-1,F(1):1}
out={
    "marker":"R698_ANISOTROPIC_BRC_EXACT_PASS",
    "source_pin":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
    "weights":[frac(x) for x in w],
    "dp_vs_inclusion_exclusion_exact_cases":checks,
    "horizon_inclusive":[0,12],
    "quotient_counts":[{"weight_numerators_over_12":list(x),
                        "states":n} for x,n in multiplicities],
    "two_tick_counterexample":{"A":[0,3],"B":[1,2],
         "both_active_rate":frac(F(1,2)),
         "P_A_HALT":frac(p_a),"P_B_HALT":frac(p_b)},
    "hitting_time":{"expectation":frac(E),"CDF_4":frac(tau(4)),
                    "CDF_8":frac(tau(8))},
    "spectral":[{"sum_rate":frac(k),"coefficient":v}
                 for k,v in sorted(spectral.items()) if v],
    "classical_background":"May 2008 DOI:10.37236/906; Berthet 2017 arXiv:1703.01886"
}
with open("R698_EVIDENCE.json","w",encoding="utf-8") as f:
    json.dump(out,f,ensure_ascii=False,indent=2)
print(out["marker"],"cases",checks,"E_tau",E,"CDF8",tau(8))
