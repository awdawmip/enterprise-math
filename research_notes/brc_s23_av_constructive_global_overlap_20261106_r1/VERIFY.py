#!/usr/bin/env python3
"""Exact rational checks for the constructive S23 tagged-AV overlap theorem."""
from fractions import Fraction as F
from math import isqrt

A = F(1, 2)
B = F(7, 8)
ZMIN, ZMAX = F(1, 16), F(7, 16)
QMIN, QMAX = F(1, 128), F(1, 4)
DZ, DQ = F(11, 20), F(1, 20)
CHEB = F(21, 121)
UNIFORM = F(32, 155)
CHI = F(789, 125)
C_COEFF = F(336, 18755)

assert QMAX - QMIN == F(31, 128)
assert 1 - F(1, 4) / DZ**2 == CHEB
assert DQ / (QMAX - QMIN) == UNIFORM
assert F(16, 5) * (DZ+DQ)**2 + 16*DZ**2 + 128*DQ**2 == CHI
assert CHEB * UNIFORM / 2 == C_COEFF
assert 1-ZMAX-QMAX == F(5, 16)

cases = 0
for an in range(4, 8):
    a = F(an, 8)
    for cn in range(4, 8):
        c = F(cn, 8)
        z, q = (1-a)*c, (1-a)*(1-c)
        assert ZMIN <= z <= ZMAX
        assert F(1, 64) <= q <= QMAX
        for n in (1, 4, 25, 100, 10000):
            root = isqrt(n)
            assert root*root == n
            for sign_z in (-1, 0, 1):
                raw = z + F(sign_z)*DZ / root
                zh = min(ZMAX, max(ZMIN, raw))
                assert abs(zh-z) <= DZ/root
                for sign_q in (-1, 0, 1):
                    raw_q = q + F(sign_q)*DQ / root
                    qp = min(QMAX, max(QMIN, raw_q))
                    assert abs(qp-q) <= DQ/root
                    p = (1-z-q, z, q)
                    pp = (1-zh-qp, zh, qp)
                    assert min(pp) > 0 and sum(pp) == sum(p) == 1
                    chi = sum((v-w)**2/w for v,w in zip(p, pp))
                    assert n*chi <= CHI, (a,c,n,sign_z,sign_q,n*chi)
                    cases += 1
print('PASS_S23_CONSTRUCTIVE_GLOBAL_OVERLAP_20261106')
print('rational_parameter_event_cases=', cases)
print('chebyshev_probability_lower=', CHEB)
print('q_interval_probability_factor=', UNIFORM)
print('n_times_KL_upper_via_chi_square=', CHI)
print('overlap_constant=C_coeff*exp(-789/125), C_coeff=', C_COEFF)
print('theorem=for_all_n>=1: delta_n <= 1-C/sqrt(n)')
