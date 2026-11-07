#!/usr/bin/env python3
"""EC49BH independent exact Blackwell kernel identity checker; standard-library Fraction."""
from fractions import Fraction as Q
from itertools import product
def P(e,u,w):
    return Q(1,2)+(2*u-1)*(1-w)*e
def K(r,v,u):
    return (1+r)/2 if v==u else (1-r)/2
tested=0
for numerator,denominator in [(0,1),(1,8),(1,4),(1,3),(2,5),(1,2)]:
  for numerator2,denominator2 in [(1,8),(1,4),(1,3),(2,5),(1,2)]:
    lo,hi=Q(numerator,denominator),Q(numerator2,denominator2)
    if lo>hi: continue
    for w,v in product(range(3),range(2)):
      assert P(lo,v,w)==sum((P(hi,u,w)*K(lo/hi,v,u) for u in range(2)),Q(0))
      tested+=1
assert tested>24
print({"result":"PASS","rational_pair_wv_equalities":tested,"scope":"finite test of universally proved coefficient identity"})
