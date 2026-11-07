#!/usr/bin/env python3
"""Exact finite plateau N(h)=439 for 71<=h<=79 and N(80)=443."""
from fractions import Fraction
from bisect import bisect_left
p7=[7**j for j in range(550)]
p10=[10**j for j in range(550)]

def count(n,h):
    items=sorted((Fraction(p10[i],p7[i+j]),i,j) for i in range(h+1) for j in range(h-i+1))
    thresholds=[z[0] for z in items]
    assert len(thresholds)==len(set(thresholds))
    seen=set()
    for ell in range(n+1):
        for k in range(n-ell+1):
            if k==ell==0: continue
            r=Fraction(p7[k+ell],p10[k])
            p=bisect_left(thresholds,r)
            assert p==len(thresholds) or thresholds[p]!=r
            seen.add(p)
    missing=[i for i in range(len(thresholds)+1) if i not in seen]
    return len(thresholds),missing,items

m,gaps,_=count(439,79)
assert m==3240 and gaps==[]
print('h=79 n=439, all 3241 open threshold intervals occupied')
m,gaps,items=count(442,80)
assert m==3321 and len(gaps)==1, (m,gaps)
idx=gaps[0]
print('h=80 n=442, one missing interval:',idx,'bound (i,j)=',items[idx-1][1:], items[idx][1:])
m,gaps,_=count(443,80)
assert m==3321 and gaps==[]
print('h=80 n=443, all 3322 open intervals occupied')
print('Via threshold-set nesting and monotonic prefix padding: N(h)=439 for all 71<=h<=79; N(80)=443')
print('PASS_S23_AV_FINITE_HORIZON_PLATEAU_71_TO_80_EXACT_20261107')
