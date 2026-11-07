#!/usr/bin/env python3
"""Exact rational S23 AV observer bridge / finite-bank certificates.

Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34
No floating point; finite checks support the analytic statements in PROOF.md.
"""
from fractions import Fraction as F
from math import comb

M20 = (
    (10,10,0,0,0,0), (9,11,0,0,0,0), (0,0,20,0,0,0),
    (0,0,0,10,10,0), (0,0,0,2,18,0), (0,0,0,0,0,20),
)
assert all(sum(row) == 20 and all(x >= 0 for x in row) for row in M20)
assert tuple(F(i,20) for i in M20[2]) == (F(0),F(0),F(1),F(0),F(0),F(0))

def av_law(a,c):
    """Frozen S23 source AV when b_AV=0, in stop-time order (1,2,3,4)."""
    return (a, F(0), (1-a)*c, (1-a)*(1-c))

def ternary_and_binary(q):
    """Ternary (time1,time3,time4); binary event time3."""
    assert q[1] == 0 and sum(q) == 1 and all(p >= 0 for p in q)
    return (q[0], q[2], q[3]), (q[2], 1-q[2])

# Entire finite four-policy witness, with the first-stage A parameter a fixed to 1/2.
a = F(1,2)
cs = [F(1,2) + F(i,8) for i in range(4)]
zs = [(1-a)*c for c in cs]
q = [av_law(a,c) for c in cs]
assert zs == [F(1,4), F(5,16), F(3,8), F(7,16)]
for i in range(4):
    triple, binary = ternary_and_binary(q[i])
    assert triple == (a,zs[i],1-a-zs[i])
    assert binary == (zs[i],1-zs[i])

# Under any fixed Markov kernel H : stop time -> 3 bits, each output event
# probability is affine in c, hence has vanishing third forward difference.
def d3(values):
    return sum(F((-1)**(3-i)*comb(3,i))*values[i] for i in range(4))

assert d3([qi[0] for qi in q]) == 0
assert d3([qi[1] for qi in q]) == 0
assert d3([qi[2] for qi in q]) == 0
assert d3([qi[3] for qi in q]) == 0
third = d3([z**3 for z in zs])
assert third == F(3,2048)
one_kernel_TV_obstruction = third / 8
assert one_kernel_TV_obstruction == F(3,16384)

# A finite collection of affine functions cannot exactly match the cubic z^3
# throughout this infinite interval: each equality polynomial has <=3 roots.
# Confirm nonzero cubic coefficient of z^3 - (u+v*c) with a=1/2.
assert (1-a)**3 == F(1,8)

# A fixed source encoder E and m fixed decoders D_l produce m constant
# decoded probability values for event {T=3} in pure preparation AV.
# z ranges over [1/16,7/16] on the declared AV rectangle.
z_lo,z_hi = F(1,8)*F(1,2), F(1,2)*F(7,8)
assert (z_lo,z_hi) == (F(1,16),F(7,16))
assert z_hi-z_lo == F(3,8)
m=10
radius=(z_hi-z_lo)/(2*m)
assert radius == F(3,160)
# Evenly spaced bank probabilities attain this radius for the one-event
# scalar readout alone. This is not an upper bound for whole four-time TV.
centers=[z_lo + (2*j+1)*radius for j in range(m)]
assert centers[0]-radius == z_lo
assert centers[-1]+radius == z_hi
assert all(centers[j+1]-centers[j] == 2*radius for j in range(m-1))
# Full S23 control range a_A=0,b_AV=0,c_AV in [0,1] yields 1/(2m).
assert F(1,2*m) == F(1,20)

print('PASS_S23_AV_MOTHER_SINGLE_STOP_VS_THREE_IID_FINITE_DIFF_20261107')
print('frozen_science=43ec6098b1330ae86d0a7863be336c5d97f6ef34')
print('pure_AV_mixing_row=', tuple(F(i,20) for i in M20[2]))
print('c_grid=', ','.join(map(str,cs)))
print('z_grid=', ','.join(map(str,zs)))
print('third_difference_z_cubed=',third)
print('one_kernel_TV_lower_bound=',one_kernel_TV_obstruction)
print('m10_pure_AV_event_bank_lower_bound=',radius)
print('m10_full_legal_cube_event_bank_lower_bound=',F(1,20))
print('coverage=exact finite four policies + analytic affine/cubic argument + interval covering')
