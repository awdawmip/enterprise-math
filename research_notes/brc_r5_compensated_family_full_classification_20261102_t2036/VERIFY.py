#!/usr/bin/env python3
"""Exact author-side regression for a compensated two-law I->J->K stopping model.

All arithmetic uses fractions.Fraction. This tests rational instances of the
analytic support-gap theorem; the proof for all real parameters is in RESEARCH.md.
This is auxiliary dual-law BRC source flow, not native X6 computation.
"""
from fractions import Fraction as F
from itertools import product

check_count = 0
flow_count = 0

def check(p, label):
    global check_count
    check_count += 1
    if not p:
        raise AssertionError(label)

def model(p, kappa, lam, j):
    assert len(p) == 4 and len(j) == 4
    q = tuple((8 * t - 1) / 9 for t in p)
    alpha = tuple(1 + t for t in p)
    U = tuple(kappa * t for t in alpha)
    V = tuple(lam * t for t in alpha)
    for v in p + q + U + V + j:
        check(0 < v < 1, 'nature probability strictly positive')
    return p, q, alpha, kappa, lam, j

def reduced(m, x, jb, ji, ks):
    global flow_count
    flow_count += 1
    p, q, alpha, kap, lam, (ab, ai, bb, bi) = m
    db = (1 - jb) / 8
    di = (1 - x) * (1 - ji) / 8
    d = db + di
    w = (F(1, 4), (1 - x) / 4, db, di)
    r = sum(alpha[s] * w[s] * (1 - ks[s]) for s in range(4))
    base = F(5, 2) - F(3, 4) * x + 2 * d
    return x, db, di, d, r, base

def obs(m, x, jb, ji, ks):
    p, q, alpha, kap, lam, (ab, ai, bb, bi) = m
    x, db, di, d, r, base = reduced(m, x, jb, ji, ks)
    return (1 - ab * db - ai * di - kap * r,
            bb * db + bi * di + lam * r,
            base + r, base + F(8, 9) * r)

def score(n, o):
    return sum(n[i] * o[i] for i in range(4))

def corners(m):
    full = [obs(m, *map(F, bits[:3]), tuple(map(F, bits[3:])))
            for bits in product((0, 1), repeat=7)]
    lr = [obs(m, F(x), F(y), F(y), (F(z),) * 4)
          for x, y, z in product((0, 1), repeat=3)]
    check(len(full) == 128 and len(lr) == 8, 'all deterministic corners')
    return full, lr

def exact_gap(n, full, lr, target, label):
    lhs = max(score(n, x) for x in full)
    rhs = max(score(n, x) for x in lr)
    check(lhs - rhs == target, label)
    return lhs, rhs

def check_case(name, p, kappa, lam, j, expect_equal=False):
    m = model(p, kappa, lam, j)
    full, lr = corners(m)
    ab, ai, bb, bi = j
    sa, sb = ab + ai, bb + bi
    np = (F(1), F(0), -2 * sa + 9 * kappa, F(9, 4) * sa - 9 * kappa)
    nq = (F(0), F(-1), -2 * sb + 9 * lam, F(9, 4) * sb - 9 * lam)
    gp = abs(ab - ai) / 16
    gq = abs(bb - bi) / 16
    exact_gap(np, full, lr, gp, name + ' P-J support identity')
    exact_gap(nq, full, lr, gq, name + ' Q-J support identity')
    for o in full + lr:
        r = 9 * (o[2] - o[3])
        b = -8 * o[2] + 9 * o[3]
        a = 1 - o[0] - kappa * r
        c = o[1] - lam * r
        check(b <= 3 and r >= 0, name + ' source time face bounds')
        check(a >= 0 and c >= 0, name + ' corrected source answer masses')
    gk = None
    if ab == ai and bb == bi:
        c = (m[2][2] + m[2][3]) / 2
        nk = (c / ab, F(0), 9 * (1 + c * kappa / ab),
              -9 * (1 + c * kappa / ab))
        gk = abs(p[2] - p[3]) / 16
        exact_gap(nk, full, lr, gk, name + ' K-J source time support identity')
    if expect_equal:
        check(ab == ai and bb == bi and p[2] == p[3], 'sufficient parameter conditions')
        for bits in product((0, 1), repeat=7):
            x, jb, ji = map(F, bits[:3])
            ks = tuple(map(F, bits[3:]))
            _, db, di, d, r, _ = reduced(m, x, jb, ji, ks)
            y = 1 - 8 * d / (2 - x)
            maximum = m[2][0] / 4 + m[2][1] * (1 - x) / 4 + m[2][2] * d
            z = 1 - r / maximum
            check(0 <= y <= 1 and 0 <= z <= 1, name + ' valid LR witness')
            check(obs(m, x, y, y, (z,) * 4) == obs(m, x, jb, ji, ks),
                  name + ' exact real LR realization')
        for k in range(32):
            x = F(k + 1, 40)
            jb = F((3 * k + 1) % 37, 37)
            ji = F((5 * k + 2) % 39, 39)
            ks = tuple(F((t * (k + 1) + 3) % 41, 41) for t in (1, 3, 7, 11))
            _, db, di, d, r, _ = reduced(m, x, jb, ji, ks)
            y = 1 - 8 * d / (2 - x)
            maximum = m[2][0] / 4 + m[2][1] * (1 - x) / 4 + m[2][2] * d
            z = 1 - r / maximum
            check(0 <= y <= 1 and 0 <= z <= 1, name + ' interior LR witness')
            check(obs(m, x, y, y, (z,) * 4) == obs(m, x, jb, ji, ks),
                  name + ' interior observer equality')
    print(name, 'Delta_P=', gp, 'Delta_Q=', gq,
          'Delta_K=', gk if gk is not None else 'requires_J_equal',
          'equal_image_regression=', expect_equal)

base = (F(1, 4), F(1, 3), F(1, 2), F(2, 3))
check_case('independent_J_and_K', base, F(2, 5), F(1, 3),
           (F(3, 5), F(1, 2), F(2, 5), F(1, 2)))
check_case('equal_J_unequal_K', base, F(2, 5), F(1, 3),
           (F(3, 5), F(3, 5), F(2, 5), F(2, 5)))
check_case('equal_J_equal_K', (F(1,4), F(1,3), F(1,2), F(1,2)),
           F(2, 5), F(1, 3), (F(3, 5), F(3, 5), F(2, 5), F(2, 5)), True)
check_case('P_only_J', base, F(2, 5), F(1, 3),
           (F(7, 10), F(2, 5), F(3, 5), F(3, 5)))
check_case('Q_only_J', base, F(2, 5), F(1, 3),
           (F(3, 5), F(3, 5), F(4, 5), F(2, 5)))
check_case('second_equal', (F(1, 6), F(3, 8), F(7, 10), F(7, 10)),
           F(1, 3), F(1, 4), (F(1, 5), F(1, 5), F(3, 4), F(3, 4)), True)
check_case('second_non_equal', (F(1, 6), F(3, 8), F(7, 10), F(1, 5)),
           F(1, 3), F(1, 4), (F(1, 5), F(1, 5), F(3, 4), F(3, 4)))
print('PASS_EXACT_R5_FULL_COMPENSATED_FAMILY_CLASSIFICATION')
print('exact_assertions=', check_count)
print('source_flow_evaluations=', flow_count)
print('FULL_vertices_per_case=128 LR_vertices_per_case=8 cases=7')
