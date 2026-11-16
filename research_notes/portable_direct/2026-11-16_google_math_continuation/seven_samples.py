"""Minimal consecutive window length for phase recovery invariant to cubic drift."""
from fractions import Fraction
from itertools import combinations
from math import comb

P = tuple(Fraction(x, 36) for x in (455, -295, -25, 185, -25, -295))
def phase_difference(j):
    return Fraction(-5 * (2*j-5) * (2*j*j-10*j+5), 6)

assert all(P[j]-P[(j+1)%6] == phase_difference(j) for j in range(6))
assert P[0]-P[1] != phase_difference(6)
def fourth_difference(a):
    return sum((-1)**(4-j)*comb(4,j)*P[(a+j)%6] for j in range(5))

v = [fourth_difference(a) for a in range(6)]
assert v == [20,20,20,-100,140,-100]
codes = [tuple(v[(a+j)%6] for j in range(3)) for a in range(6)]
gap = min(max(abs(x-y) for x,y in zip(u,v)) for u,v in combinations(codes,2))
assert gap == 120
for degree in range(4):
    assert sum((-1)**(4-j) * comb(4,j) * j**degree for j in range(5)) == 0
print("Seven-sample cubic-invariant codes:",codes,"minimum gap:",gap)
