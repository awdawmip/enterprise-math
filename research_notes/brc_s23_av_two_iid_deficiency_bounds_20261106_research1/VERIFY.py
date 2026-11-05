#!/usr/bin/env python3
"""Exact rational check for the S23/AV two-iid-trial reverse deficiency bounds."""
from fractions import Fraction as F
from itertools import product

V = F(88, 105)
LOWER = F(423, 2468)
UPPER = F(18549, 78400)
ONE = F(1)
checks = 0

def check(claim, label):
    global checks
    assert claim, label
    checks += 1

def av(a, c):
    z = (1 - a) * c
    return (a, z, 1 - a - z)

def compressed(a, c):
    z = (1 - a) * c
    return (z, 1 - z)

def recovered(a, c):
    z = (1 - a) * c
    return (V * (1 - z), z, (1 - V) * (1 - z))

def tensor(p, q):
    return tuple(x*y for x in p for y in q)

def tv(p, q):
    check(len(p) == len(q), 'matched outcome spaces')
    return sum(abs(x - y) for x, y in zip(p, q)) / 2

def bayes(p, q, prior_high):
    return sum(min((1 - prior_high)*x, prior_high*y) for x, y in zip(p, q))

corners = tuple(product((F(1, 2), F(7, 8)), repeat=2))

for a, c in corners:
    check(sum(av(a, c)) == ONE, 'full AV probability mass')
    check(sum(compressed(a, c)) == ONE, 'binary AV probability mass')
    check(sum(recovered(a, c)) == ONE, 'kernel recovery probability mass')
    check(tv(av(a, c), recovered(a, c)) <= F(9, 70), 'one-trial endpoint bound')

# The signed vector of (A(theta_1) tensor A(theta_2)) -
# (B(theta_1) K tensor B(theta_2) K) is separately affine in
# a_1,c_1,a_2,c_2. TV is a convex function of that signed vector.
# Its maximum over the four-dimensional rectangle occurs at corners.
corner_grid = []
for t1 in corners:
    row = []
    for t2 in corners:
        d = tv(tensor(av(*t1), av(*t2)),
               tensor(recovered(*t1), recovered(*t2)))
        check(d <= UPPER, '4D vertex upper certificate')
        row.append(d)
    corner_grid.append(row)
check(max(max(row) for row in corner_grid) == UPPER, 'sharp product-kernel upper')
check(corner_grid[3][3] == UPPER, 'same-parameter endpoint upper witness')

lo = (F(1, 2), F(1, 2))
hi = (F(7, 8), F(7, 8))
prior = F(256, 617)
alo, ahi = (tensor(av(*t), av(*t)) for t in (lo, hi))
blo, bhi = (tensor(compressed(*t), compressed(*t)) for t in (lo, hi))
risk_a = bayes(alo, ahi, prior)
risk_b = bayes(blo, bhi, prior)
check(risk_a == F(601, 2468), 'two-trial full Bayes risk')
check(risk_b == F(256, 617), 'two-trial compressed Bayes risk')
check(risk_b - risk_a == LOWER, 'two-trial deficiency lower')

# For this pair, the Bayes-gap function is continuous and piecewise linear
# in the prior. Its breakpoints occur at p/(p+q) for output events.
knots = {F(0), F(1)}
knots.update(x/(x+y) for p, q in ((alo, ahi), (blo, bhi)) for x, y in zip(p,q))
maxima = [(bayes(blo, bhi, t) - bayes(alo, ahi, t), t) for t in sorted(knots)]
check(max(maxima) == (LOWER, prior), 'exact pair-optimal Bayes prior')
check(LOWER <= UPPER, 'compatible upper and lower')

print('PASS_S23_AV_TWO_IID_TRIAL_DEFICIENCY_BOUNDS_EXACT_20261106')
print('CHECKS', checks)
print('LOWER', str(LOWER), 'PRIOR_HIGH', str(prior), 'RA', str(risk_a), 'RB', str(risk_b))
print('UPPER', str(UPPER), 'K_NO_FIRST', str(V), 'CORNER_WITNESS', '(7/8,7/8)')
print('CORNER_GRID')
for row in corner_grid:
    print(' '.join(str(d) for d in row))
