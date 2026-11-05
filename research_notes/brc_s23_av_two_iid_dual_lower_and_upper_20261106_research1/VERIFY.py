#!/usr/bin/env python3
"""Exact rational verification for S23 AV two-iid reverse-deficiency bounds."""
from fractions import Fraction as F
from itertools import product

D = 10_000_000
COUNTS = (
    (0, 0, 0, 0, D, 0, 0, 0, 0),
    (0, 0, 0, 5791902, 0, 0, 4208098, 0, 0),
    (0, 5539216, 663649, 908246, 0, 1111111, 0, 1111111, 666667),
    (7533509, 375817, 1483158, 265834, 0, 0, 341682, 0, 0),
)
K = tuple(tuple(F(x, D) for x in row) for row in COUNTS)
CORNERS = list(product((F(1, 2), F(7, 8)), repeat=2))
LOWER_POINTS = ((F(1, 2), F(1, 2)), (F(11, 16), F(7, 8)), (F(47, 64), F(7, 8)))
WEIGHTS = (F(4061, 8125), F(12576, 56875), F(15872, 56875))
TESTS = (
    (-1, -1, 1, -1, 0, 1, 1, 1, 1),
    (1, 1, -1, 1, F(4, 35), -1, -1, -1, -1),
    (1, 1, -1, 1, -F(12, 119), -1, -1, -1, -1),
)
OLD_LOWER = F(423, 2468)
OLD_UPPER = F(947, 5000)
LOWER = F(1491, 8125)
UPPER = F(7573633, 40_000_000)
assertions = 0

def check(condition, name):
    global assertions
    assert condition, name
    assertions += 1

def full(a, c):
    z = (1 - a) * c
    return (a, z, 1 - a - z)

def binary(a, c):
    z = (1 - a) * c
    return (z, 1 - z)

def tensor(a, b):
    return tuple(x * y for x in a for y in b)

def error(i, j):
    a = tensor(full(*CORNERS[i]), full(*CORNERS[j]))
    b = tensor(binary(*CORNERS[i]), binary(*CORNERS[j]))
    return tuple(a[k] - sum(b[r] * K[r][k] for r in range(4)) for k in range(9))

def tv_signed(v):
    return sum(map(abs, v)) / 2

for r, row in enumerate(COUNTS):
    check(sum(row) == D and min(row) >= 0, f'row_{r}_stochastic')
checks = []
for i in range(4):
    for j in range(i, 4):
        e = error(i, j)
        f = error(j, i)
        g = tuple((u + v) / 2 for u, v in zip(e, f))
        t = tv_signed(g)
        checks.append((i, j, t))
        check(t <= UPPER, f'signed_corner_{i}_{j}')
check(max(v for i, j, v in checks) == UPPER, 'upper_certificate_max')
check(tv_signed(error(0, 0)) == UPPER, 'upper_attained_at_first_corner')

check(sum(WEIGHTS) == 1 and min(WEIGHTS) >= 0, 'dual_weights')
for k, v in enumerate(TESTS):
    check(len(v) == 9 and all(-1 <= x <= 1 for x in v), f'dual_test_{k}')
P = [tensor(full(*p), full(*p)) for p in LOWER_POINTS]
Q = [tensor(binary(*p), binary(*p)) for p in LOWER_POINTS]
constant = sum(WEIGHTS[k] * sum(TESTS[k][j] * P[k][j] for j in range(9))
               for k in range(3))
coeff = [[sum(WEIGHTS[k] * Q[k][r] * TESTS[k][j] for k in range(3))
          for j in range(9)] for r in range(4)]
maxima = tuple(max(row) for row in coeff)
check(constant / 2 == F(597, 3250), 'dual_constant')
check(maxima == (F(3, 8125), F(0), F(0), F(0)), 'dual_row_maxima')
check((constant - sum(maxima)) / 2 == LOWER, 'dual_lower_exact')
check(OLD_LOWER < LOWER < UPPER < OLD_UPPER, 'strict_both_sides_improved')

print('PASS_S23_AV_TWO_IID_DUAL_LOWER_AND_JOINT_UPPER_EXACT_20261106')
print('CHECKS', assertions)
print('FROZEN_SCIENCE', '43ec6098b1330ae86d0a7863be336c5d97f6ef34')
print('LOWER', LOWER, 'UPPER', UPPER)
print('LOWER_POINTS', LOWER_POINTS)
print('DUAL_WEIGHTS', WEIGHTS)
print('DUAL_TESTS', TESTS)
print('DUAL_HALF_CONSTANT', constant / 2)
print('DUAL_ROW_MAXIMA', maxima)
print('KERNEL_DENOMINATOR', D)
for row in COUNTS:
    print('KERNEL_ROW', ','.join(str(v) for v in row))
for i, j, tv in checks:
    print('CORNER', i, j, tv)
print('ATTAINMENT', CORNERS[0], tv_signed(error(0, 0)))
