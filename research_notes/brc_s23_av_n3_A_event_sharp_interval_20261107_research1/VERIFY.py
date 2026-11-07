#!/usr/bin/env python3
"""Exact Fraction verification of S23 n=3 A-event sharp-face interval.

Four-point equality of degree <=3 polynomials is an identity certificate.
Nonnegative factor signs on the intervals are proved in PROOF.md.
"""
from fractions import Fraction as F
from math import comb

D = F(5211, 21952)
T0 = F(919, 37044)
T1 = F(345827, 1407672)
Z0 = F(1, 4)
ZSTAR = F(7, 64)
assert T1 - T0 == F(235, 1064)


def masses(t):
    return (F(0), 3*t-F(919, 12348), F(30839, 37044)-2*t, t)


def q(z, t):
    return sum((F(comb(3, k)) * z**(3-k) * (1-z)**k * p
                for k, p in enumerate(masses(t))), F(0))


def q0(z):
    return (1-z)**2 * (86084*z+919)/37044


def h_left(z):
    return 1-(1-z)**3


def h_right(z):
    return 1-(F(1, 2)+z)**3


def l_left(z):
    return 1-(F(7, 8)+z)**3


def l_right(z):
    return 1-(1-z/7)**3


# All polynomials below are cubic or lower. Their equality at 4 distinct
# rational values proves symbolic equality for all real z.
NODES = [F(0), F(1, 6), F(1, 4), F(1, 2)]
for z in NODES:
    assert q(z, T0) == q0(z)
    assert q(z, T1) - q(z, T0) == F(235, 1064)*(1-z)*(4*z-1)**2
    assert D-h_left(z)+q(z, T0) == (4*z-1)*(196160*z*z-191428*z-155401)/592704
    assert D-h_right(z)+q(z, T0) == (4*z-1)*(492512*z*z-339604*z+363215)/592704
    assert D-q(z, T1)+l_left(z) == (64*z-7)*(295616*z*z-4617064*z-4141441)/90091008
    assert D-q(z, T1)+l_right(z) == 13339*(4*z-1)**2*(64*z-7)/11261376

assert T0 < T1 < F(13267, 37044)
assert masses(T0) == (F(0), F(0), F(1381, 1764), T0)
assert masses(T1) == (F(0), F(705, 1064), F(5717, 16758), T1)
for t in [T0, (T0+T1)/2, T1]:
    assert all(0 <= p <= 1 for p in masses(t))
    assert q(Z0, t) == F(935, 2744)
    assert q(Z0, t)-l_right(Z0) == D
    assert h_left(Z0)-q(Z0, t) == D

# This corner is legal: (a,c)=(7/8,7/8), z=7/64.
assert D-q(ZSTAR, T1)+l_right(ZSTAR) == 0
assert q(ZSTAR, T1) - l_right(ZSTAR) == D
for t in (T0, (T0+T1)/2, T1):
    # These grid checks are regression only, not the all-real proof.
    for i in range(17):
        for j in range(17):
            a = F(1, 2)+F(3*i, 128)
            c = F(1, 2)+F(3*j, 128)
            z = (1-a)*c
            truth = 1-(a+z)**3
            assert abs(q(z, t)-truth) <= D
print('PASS_S23_N3_A_EVENT_SHARP_FACE_EXACT_INTERVAL_20261107')
print('t_exact_interval', T0, T1)
print('t_interval_width', T1-T0)
print('upper_endpoint_A_masses', masses(T1))
print('saturated_z', Z0, ZSTAR)
print('symbolic_identities', 6, 'nodes_each', len(NODES))
print('rational_regression_cases', 3*17*17)
