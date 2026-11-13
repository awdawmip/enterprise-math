#!/usr/bin/env python3
"""Independent exact checker for the Stage306-B dyadic full-square certificate."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

root=Path(__file__).parent
obj=json.loads((root/'CERT_STAGE306B_DYADIC.json').read_text(encoding='utf-8'))
assert obj['schema']=='STAGE306B_EXACT_DYADIC_COVER_V1'
assert obj['low_risk_per_outer_public_prefix']=='604661379/50000000000'
paths=obj['leaf_paths']
assert len(set(paths))==len(paths)
assert all(set(p)<={'0','1'} for p in paths)
ordered=sorted(paths)
assert all(not b.startswith(a) for a,b in zip(ordered,ordered[1:])), 'overlap'
assert sum((F(1,2)**len(p) for p in paths),F(0))==1, 'coverage gap'

low=F(604661379,50000000000)
a=F(1,4);b=F(3,4)
P=[F(9,10)*a**k*(1-a)**(3-k)+F(1,10)*b**k*(1-b)**(3-k) for k in range(4)]

def bracket(t0,t1,k):
    f=lambda t:t**k*(1-t)**(3-k)
    values=[f(t0),f(t1)]
    peak=F(k,3)
    if t0<=peak<=t1:values.append(f(peak))
    return min(values),max(values)

maxdepth=0
for p in paths:
    xx=[F(0),F(1)];yy=[F(0),F(1)]
    for d,digit in enumerate(p):
        pair=xx if d%2==0 else yy
        center=sum(pair)/2
        if digit=='0':pair[1]=center
        else: pair[0]=center
    infimum=F(0)
    for k in range(4):
        la,ha=bracket(*xx,k);lb,hb=bracket(*yy,k)
        lo=F(4,5)*la+F(1,5)*lb-P[k]
        hi=F(4,5)*ha+F(1,5)*hb-P[k]
        infimum+=comb(3,k)*max(F(0),lo,-hi)/2
    assert infimum>=low,(p,infimum)
    maxdepth=max(maxdepth,len(p))

print('INDEPENDENT_STAGE306B_DYADIC_CERT_VERIFY_PASS')
print('prefix_free_and_kraft_complete=1')
print('all_leaf_interval_bounds_at_least='+str(low))
print('verified_leaves='+str(len(paths)))
print('max_depth='+str(maxdepth))
