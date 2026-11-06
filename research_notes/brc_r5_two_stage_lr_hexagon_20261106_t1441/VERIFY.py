"""Exact rational check for the frozen four-stage R5 P/Q tree's two-stage LR subfamily."""
from fractions import Fraction as F
from itertools import product

H = F(7, 128)
G = F(7, 8)
RATIOS = (F(3, 4), F(1), F(5, 4))
MASS = {F(3, 4): F(7, 16), F(1): F(1, 8), F(5, 4): F(7, 16)}
assert sum(MASS.values()) == 1
assert sum(r * m for r, m in MASS.items()) == 1
assert 1 + G == F(15, 8)


def policy(c, d):
    assert abs(c) <= H and abs(d) <= H
    t = {
        F(3, 4): F(1, 2) + F(32, 7) * (c + d),
        F(1): F(1, 2) + 8 * d,
        F(5, 4): F(1, 2) - F(32, 7) * (c + d),
    }
    assert all(F(0) <= x <= F(1) for x in t.values())
    ep = 1 - sum(r * MASS[r] * t[r] for r in RATIOS)
    eq = sum(MASS[r] * t[r] for r in RATIOS)
    assert (ep, eq) == (F(1, 2) + c, F(1, 2) + d)
    return ep, eq, t

for c, d in product((-H, H), repeat=2):
    policy(c, d)
for i, j in product(range(-16, 17), repeat=2):
    policy(H * i / 16, H * j / 16)


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

observations = []
for bits in product((0, 1), repeat=3):
    t = dict(zip(RATIOS, bits))
    ep = 1 - sum(r * MASS[r] * t[r] for r in RATIOS)
    eq = sum(MASS[r] * t[r] for r in RATIOS)
    assert F(3) <= 4 * ep + 3 * eq <= F(4)
    assert F(4) <= 4 * ep + 5 * eq <= F(5)
    assert F(57, 64) <= ep + eq <= F(71, 64)
    observations.append((ep, eq))
points = sorted(set(observations))
lo = []
for pt in points:
    while len(lo) >= 2 and cross(lo[-2], lo[-1], pt) <= 0:
        lo.pop()
    lo.append(pt)
hi = []
for pt in points[::-1]:
    while len(hi) >= 2 and cross(hi[-2], hi[-1], pt) <= 0:
        hi.pop()
    hi.append(pt)
hull = lo[:-1] + hi[:-1]
expected = [(F(0), F(1)), (F(21, 64), F(9, 16)),
            (F(29, 64), F(7, 16)), (F(1), F(0)),
            (F(43, 64), F(7, 16)), (F(35, 64), F(9, 16))]
assert hull == expected
assert H == F(1, 2) * (F(7, 64))  # support bound on ep+eq at (+H,+H)
prior = F(287903, 10672000)
factor = H / prior
assert factor > 2
print('PASS_EXACT_R5_TWO_STAGE_LR_HEXAGON_AND_MAX_INSCRIBED_SQUARE')
print('strategy: time1 continuation g=', G, '; all stop at time2')
print('Q stop-masses=', ', '.join(f'{r}:{MASS[r]}' for r in RATIOS))
print('time P=Q=', F(15, 8))
print('polytope inequalities: 3<=4eP+3eQ<=4; 4<=4eP+5eQ<=5; 57/64<=eP+eQ<=71/64')
print('hexagon CCW vertices=', '; '.join(f'({a},{b})' for a, b in hull))
print('largest centered square halfside=', H, 'decimal=', float(H))
print('prior two-key optimal restricted-family halfside=', prior)
print('improvement exact factor=', factor, 'decimal=', float(factor))
print('universal real-square proof: affine inverse with corner bounds')
print('exhaustive deterministic declaration vectors=', len(observations))
print('exact rational grid checks=', 33 * 33)
