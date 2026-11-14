#!/usr/bin/env python3
"""Finite exact source-bound R063 Stage2 sector vs X6 signed shells.

Current X6 Cell: six ordered signed integer displacement components;
L_E^2=sum(z_i^2), shortest word weight=t!/prod |z_i|!.
Historical Stage2 GRoot charts are nonnegative two-component Gaussian roots.
Independent of original Stage2 runner and not its native C3/C4 benchmark.
"""
from itertools import product, combinations
from math import comb, factorial, isqrt
from collections import Counter

N = (2,4)
count, total = Counter(), Counter()
shapes = {n: Counter() for n in N}
for z in product(range(-2,3), repeat=6):
    q = sum(x*x for x in z)
    if q not in N:
        continue
    t = sum(abs(x) for x in z)
    denom = 1
    for x in z:
        denom *= factorial(abs(x))
    weight = factorial(t) // denom
    assert factorial(t) % denom == 0
    count[q] += 1
    total[q] += weight
    shapes[q][tuple(sorted((abs(x) for x in z if x),reverse=True))] += 1
assert count == {2:60,4:252},count
assert total == {2:120,4:5772},total
assert shapes[2] == {(1,1):60}
assert shapes[4] == {(2,):12,(1,1,1,1):240}

# Independent orbit-size and multinomial method, not enumerating Z^6 points.
assert comb(6,2) * 4 == 60
assert comb(6,4) * 16 == 240
assert 6*2 == 12
assert 60*2 == 120
assert 12*1 + 240*factorial(4) == 5772

# Actual Stage2 two-positive-axis domain, not the signed-X6 shell.
def groot(n):
    return tuple((a,isqrt(n-a*a)) for a in range(isqrt(n)+1)
                 if isqrt(n-a*a)**2 == n-a*a)
assert groot(2) == ((1,1),)
assert set(groot(4)) == {(0,2),(2,0)}
def star(r,s):
    a,b=r; c,d=s; x=a*c-b*d; y=a*d+b*c
    return (x,y) if x >= 0 else (y,-x)
def pc(r): return comb(sum(r),r[0])
assert star((1,1),(1,1)) == (0,2)
assert pc((1,1))**2 == 4 and pc((0,2)) == 1

# Chart lift of the historical GRoot(2): choose 2 axes and 2 signs.
signed_chart_lifts = {
    tuple(signs[axes.index(i)] if i in axes else 0 for i in range(6))
    for axes in combinations(range(6),2)
    for signs in product((-1,1),repeat=2)
}
assert len(signed_chart_lifts) == count[2] == 60
assert all(sum(x*x for x in z)==2 for z in signed_chart_lifts)

# Historical positive GRoot(4) chart lifts with one nonzero coordinate
# cover 12 of 252 signed native endpoints, excluding four-axis supports.
one_axis = {tuple(sign*2 if i==axis else 0 for i in range(6))
            for axis in range(6) for sign in (-1,1)}
assert len(one_axis) == 12
assert all(sum(x*x for x in z)==4 for z in one_axis)
assert (1,1,1,1,0,0) not in one_axis
print('PASS_X6_R063_STAGE2_SIGNED_SHELL_SCOPE',
      'G2',count[2],total[2], 'G4',count[4],total[4],
      'chart_lifts',len(signed_chart_lifts),'G4_uncovered',count[4]-len(one_axis))
