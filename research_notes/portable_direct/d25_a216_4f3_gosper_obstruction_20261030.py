#!/usr/bin/env python3
"""Exact rational certificate for D25 A216 universal 4F3 kernel.

Author-side independent check only. It does not run the native H0/B0
benchmark, prove the full D25 LIFT congruence, or claim Source admission.
"""
from fractions import Fraction as F
from functools import reduce


def mul(a, b):
    result = [F(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            result[i + j] += ai * bj
    return tuple(result)


def product(*factors):
    return reduce(mul, factors, (F(1),))


def lin(a):
    return (F(a), F(1))  # polynomial s+a, ascending coefficients


def scale(p, c):
    return tuple(F(c) * x for x in p)


A = scale(product(lin(F(2, 3)), lin(F(2, 3)), lin(F(2, 3))), 2)
B = product(lin(1), lin(F(4, 3)), lin(F(7, 6)))
C = lin(F(1, 2))
B_previous = product(lin(0), lin(F(1, 3)), lin(F(1, 6)))
C_next = lin(F(3, 2))
raw_num = scale(product(lin(F(3, 2)), *([lin(F(2, 3))] * 3)), 2)
raw_den = product(lin(F(1, 2)), lin(F(7, 6)), lin(F(4, 3)), lin(1))

# Exact polynomial, not sample or floating-point, identities:
assert product(A, C_next) == raw_num
assert product(B, C) == raw_den
assert A[-1] == 2 and B_previous[-1] == 1
assert len(A) - 1 == 3 and len(B_previous) - 1 == 3
assert len(C) - 1 == 1

# Gosper normal form is shift-free: roots -2/3 and
# -1,-4/3,-7/6 have no integral shift collisions.
A_offset = F(2, 3)
B_offsets = (F(1), F(4, 3), F(7, 6))
assert all((b - A_offset).denominator != 1 for b in B_offsets)
assert all((F(3, 2) != b) for b in B_offsets)
assert F(1, 2) != A_offset

# For x(s) polynomial of any degree d>=0, the Gosper equation
# A(s)*x(s+1)-B(s-1)*x(s)=C(s) has degree d+3 on the left,
# because the leading coefficient is (2-1)*LC(x) != 0.
# The right has degree 1. Thus no solution exists over Q[s].
# By the rational Gosper normal-form theorem, no q in Q(s) solves
# R(s)*q(s+1)-q(s)=1 for R=h(s+1)/h(s).

# Independently verify the original h(s) recurrence exactly.
h = F(1)
for s in range(24):
    ratio = F(4 * (2*s+3) * (3*s+2)**3,
              3 * (2*s+1) * (6*s+7) * (3*s+4) * (s+1))
    ratio_ABC = F(2, 1) * F(3*s+2, 3)**3 * F(2*s+3, 2) / (
        F(s+1, 1) * F(3*s+4, 3) * F(6*s+7, 6) * F(2*s+1, 2)
    )
    assert ratio == ratio_ABC
    h *= ratio
print('PASS_D25_A216_EXACT_GOSPER_NORMAL_FORM')
print('A=', A, 'B_previous=', B_previous, 'C=', C)
print('NO_RATIONAL_SINGLE_TERM_ANTIDIFFERENCE_OVER_Q_S')
print('PROOF_DEGREE_OBSTRUCTION: left_degree=d+3>=3, right_degree=1')
print('P_ADIC_TRUNCATION_AND_NATIVE_H0_B0_NOT_INFERRED')
