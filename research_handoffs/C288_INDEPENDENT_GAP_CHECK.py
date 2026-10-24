#!/usr/bin/env python3
"""Independent exact interval-order kernel for C288; shares frozen input and box construction."""
from fractions import Fraction
from itertools import combinations
from C288_ISOLATING_BOXES_EXACT import build_paths

paths,_=build_paths()
margin=Fraction(1,8388608)
count=0
for i,j in combinations(range(len(paths)),2):
    b1,b2=paths[i]['box'],paths[j]['box']
    separable=any(a[1]+margin < b[0] or b[1]+margin < a[0]
                  for a,b in zip(b1,b2))
    assert separable,(i,j)
    count+=1
assert count==7750
print('C288_INDEPENDENT_RATIONAL_INTERVAL_ORDER_PASS',count,'pairs')
