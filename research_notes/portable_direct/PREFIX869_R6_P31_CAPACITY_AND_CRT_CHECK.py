#!/usr/bin/env python3
"""Exact arithmetic check of PREFIX-869 p=31 construction and capacity bound."""
from math import gcd

def half_order(g):
    x = 1
    for d in range(1, g + 1):
        x = 2*x % g
        if x in (1, g - 1):
            return d
    raise AssertionError('no half order found')

def min_bit_width_by_capacity(T):
    B = 0
    while ((1 << B) - 1)**2 < T:
        B += 1
    return B

p, g, a, b = 31, 67, 5661, 5663
N = 1 << p
T = N*(p + 1)
q1, q2 = g*a, g*b
assert half_order(g) == 33 >= p
assert gcd(a,b) == 1
assert g*a*b >= N
assert q1 % 2 == 1 and q2 % 2 == 1
assert min_bit_width_by_capacity(T) == 19
assert max(q1.bit_length(), q2.bit_length()) == 19
assert ((1 << 18)-1)**2 < T
for k in (1,3,5,7,9):
    pp = (1 << k)-1
    TT = (1 << pp)*(pp+1)
    assert min_bit_width_by_capacity(TT) == (pp+k)//2+1
print('ALL_EXACT_ASSERTIONS_PASSED')
print(dict(p=p, q1=q1, q2=q2, half_order=half_order(g), lcm=g*a*b,
           transcript_count=T, max_18bit_pairs=((1<<18)-1)**2,
           capacity_gap=T-((1<<18)-1)**2, optimum_width=19))
