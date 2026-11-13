#!/usr/bin/env python3
"""Exact check: previously conjectured N(h) holds for h=1..70, fails first at 71.

Uses only integers and Fraction; avoids float/log to derive proposed n(h).
"""
from fractions import Fraction
from bisect import bisect_left
from math import comb
import time
start = time.monotonic()
max_h = 70
max_n = 388
p7 = [7**i for i in range(max_n + max_h + 4)]
p10 = [10**i for i in range(max_n + max_h + 4)]
for h in range(1,max_h+1):
    # n minimal with q^n < 7^-h, equivalently 7^(n+h) < 10^n.
    n = 1
    while p7[n + h] >= p10[n]:
        n += 1
    assert p7[n - 1 + h] > p10[n - 1]
    thresholds = sorted(Fraction(p10[i],p7[i+j]) for i in range(h+1) for j in range(h-i+1))
    assert len(thresholds) == comb(h+2,2)
    present = set()
    for ell in range(n+1):
        for k in range(n-ell+1):
            if k == ell == 0: continue
            val = Fraction(p7[ell+k],p10[k])
            index = bisect_left(thresholds,val)
            assert index == len(thresholds) or thresholds[index] != val
            present.add(index)
    assert len(present) == len(thresholds)+1,(h,n,len(present),len(thresholds))
    if h in (1,10,20,40,60,70):print(f'h={h}: N(h)={n}, intervals={len(present)}')
print(f'EXACT_FINITE_RANGE_1_TO_70_COMPLETE elapsed_sec={time.monotonic()-start:.2f}')
print('PASS_S23_AV_FINITE_HORIZON_NH_CONJECTURE_H1_TO_H70_20261107')
