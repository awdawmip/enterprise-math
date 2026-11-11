#!/usr/bin/env python3
"""Exact rational implication checker for PREFIX-702. Requires trusted PREFIX-700/701 input certificates."""
from fractions import Fraction as F

S = 10**6
M0, M1 = 17931816, 17766
# Each row is (lower bound of W(e)-W(c), upper bound of mu(e)-mu(c)), in 1e-6 ticks.
corner = {
    '00': (557257209, 48811612),
    '01': (386820427, -111509700),
    '11': (439711044, -119288767),
}
a, b = F(386820427, S), F(111509700, S)

def lower_gap(key, q):
    w, mu = corner[key]
    return F(w, S) - F(mu, S)/q

def lipschitz(q):
    return F(M0) + F(M1)/q

def certified_radius(q):
    return (a+b/q)/lipschitz(q)

# At all real q>=2, the second corner class has the smallest certified gap.
assert F(557257209-386820427, S) - F(48811612+111509700,S)/2 > 0
assert 439711044-386820427 > 0
assert 119288767-111509700 > 0

assert 386820427*M1 - 111509700*M0 == -1992699170909118
rinf = a/F(M0)
assert rinf == F(55260061,2561688000000)
r0 = F(1,46357)
assert r0 < rinf
margin_uniform = a-F(M0)*r0
assert margin_uniform == F(18534439,46357000000) and margin_uniform > 0
assert b - F(M1)*r0 > 0

r1224 = F(1,45809)
margin_24 = a+b/F(24) - lipschitz(F(24))*r1224
assert margin_24 == F(14756219,4822000000) and margin_24 > 0
assert certified_radius(F(24)) >= r1224
old_r = F(1,65536)
assert r0 > old_r and r1224 > r0
assert (r0/old_r)**2 == F(4294967296,2148971449)
assert (r0/old_r)**2 > F(1998,1000)

print('ALL_CHECKS_PASS PREFIX702-R6')
print('universal_radius',r0,'universal_margin',margin_uniform)
print('uniform_q_ge_2_area_ratio', (r0/old_r)**2)
print('parameter_12_to_24_radius',r1224,'margin_lower',margin_24)
print('envelope_radius_supremum',rinf)
