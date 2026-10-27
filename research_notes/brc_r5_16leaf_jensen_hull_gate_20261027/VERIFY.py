"""Exact rational check of a 16-leaf BRC likelihood-ratio auxiliary observer.

Every probability is a Fraction.  This is a finite external two-measure
stopping model carried on declared X6 cell paths, NOT a native X6 evolution.
"""
from fractions import Fraction as F
from itertools import product

ZERO, ONE = F(0), F(1)
Y = (F(1, 10), F(99, 100), F(101, 100), F(19, 10))
PARS = ((F(2, 5), F(3, 8)), (F(1, 100), F(1, 50)))
STOP_P, STOP_Q, CONTINUE = 0, 1, 2


def kernel(p):
    return (p, F(1, 2) - p, F(1, 2) - p, p)


def unit(axis, sign=1):
    return tuple(sign * int(i == axis) for i in range(6))


def plus(*vectors):
    return tuple(sum(z) for z in zip(*vectors))


LAST = (unit(4), unit(4, -1), unit(5), unit(5, -1))
LEAVES = []
for g, j, k in product(range(2), range(2), range(4)):
    cell = plus(unit(g), unit(2 + j), LAST[k])
    q = F(1, 4) * kernel(PARS[g][j])[k]
    p = Y[k] * q
    LEAVES.append((g, j, k, cell, p, q))

assert len(LEAVES) == 16
assert len({row[3] for row in LEAVES}) == 16
assert all(row[4] > 0 and row[5] > 0 for row in LEAVES)
assert sum(row[4] for row in LEAVES) == ONE
assert sum(row[5] for row in LEAVES) == ONE
for g, j in product(range(2), range(2)):
    rows = [row for row in LEAVES if row[:2] == (g, j)]
    assert sum(row[4] for row in rows) == F(1, 4)
    assert sum(row[5] for row in rows) == F(1, 4)
for g in range(2):
    rows = [row for row in LEAVES if row[0] == g]
    assert sum(row[4] for row in rows) == F(1, 2)
    assert sum(row[5] for row in rows) == F(1, 2)


def obs(decision):
    ep = eq = tp = tq = ZERO
    for g, j, k, cell, p, q in LEAVES:
        t, d = decision(g, j, k)
        assert t in (1, 2, 3) and d in (STOP_P, STOP_Q)
        if d == STOP_Q:
            ep += p
        else:
            eq += q
        tp += t * p
        tq += t * q
    return (ep, eq, tp, tq)


def val(ob, s):
    return ob[0] + ob[1] + s * ob[3]


def terminal(k):
    return STOP_Q if Y[k] < ONE else STOP_P


def full_policy(t1, t2):
    def fn(g, j, k):
        if not t1[g]:
            return (1, STOP_P)
        if not t2[2 * g + j]:
            return (2, STOP_P)
        return (3, terminal(k))
    return fn


def lr_policy(m1, m2, bits):
    def fn(g, j, k):
        if m1 != CONTINUE:
            return (1, m1)
        if m2 != CONTINUE:
            return (2, m2)
        return (3, bits[k])
    return fn


GAINS = tuple(tuple(ONE - sum(ki * min(y, ONE) for ki, y in zip(kernel(p), Y))
                   for p in row) for row in PARS)
GA = sum(GAINS[0]) / 2
GB = sum(GAINS[1]) / 2
GAVG = (GA + GB) / 2
assert GAINS == ((F(361, 1000), F(271, 800)), (F(139, 10000), F(57, 2500)))
assert GA == F(2799, 8000) and GB == F(367, 20000)
assert GAVG == F(14729, 80000)
assert GA / 2 < min(GAINS[0]) and GB / 2 < min(GAINS[1])


def positive(x):
    return max(ZERO, x)


def full_formula(s):
    return ONE + s - (positive(GA - 2 * s) + positive(GB - 2 * s)) / 2


def lr_formula(s):
    return ONE + s - positive(GAVG - 2 * s)


def full_exhaustive(s):
    return min(val(obs(full_policy(t1, t2)), s)
               for t1 in product((0, 1), repeat=2)
               for t2 in product((0, 1), repeat=4))


def lr_exhaustive(s):
    return min(val(obs(lr_policy(m1, m2, bits)), s)
               for m1 in (STOP_P, STOP_Q, CONTINUE)
               for m2 in (STOP_P, STOP_Q, CONTINUE)
               for bits in product((STOP_P, STOP_Q), repeat=4))


R_B, R_L, R_A = GB / 2, GAVG / 2, GA / 2

def gap_phase(s):
    if s <= R_B or s >= R_A:
        return ZERO
    if s <= R_L:
        return s - R_B
    return R_A - s


checks = sorted(set((ZERO, R_B, (R_B + R_L) / 2, F(2, 25), R_L,
                     (R_L + R_A) / 2, R_A, F(1, 4), F(1, 2))))
for s in checks:
    full_min = full_exhaustive(s)
    lr_min = lr_exhaustive(s)
    assert full_min == full_formula(s), (s, full_min, full_formula(s))
    assert lr_min == lr_formula(s), (s, lr_min, lr_formula(s))
    assert lr_min - full_min == gap_phase(s), s

s = R_L
witness = obs(full_policy((1, 0), (1, 1, 0, 0)))
assert witness == (F(1201, 16000), F(3, 4), F(2), F(2))
assert val(witness, s) == full_formula(s) == F(40367, 40000)
assert lr_formula(s) == F(174729, 160000)
assert lr_formula(s) - full_formula(s) == F(13261, 160000)
assert gap_phase(s) == (GA - GB) / 4
# All 144 LR deterministic vertex descriptions satisfy the rational separating halfspace.
LR_VERTEX_VALUES = [val(obs(lr_policy(m1, m2, bits)), s)
                    for m1 in (STOP_P, STOP_Q, CONTINUE)
                    for m2 in (STOP_P, STOP_Q, CONTINUE)
                    for bits in product((STOP_P, STOP_Q), repeat=4)]
assert len(LR_VERTEX_VALUES) == 144 and min(LR_VERTEX_VALUES) == lr_formula(s)

print('GLOBAL_X6_LEAF_CERT:', len(LEAVES), 'strict positive P/Q; distinct native cells; sums P=Q=1')
print('TERMINAL_RATIOS:', Y)
print('TERMINAL_GAINS:', GAINS)
print('MEAN_GAINS: A=', GA, 'B=', GB, 'pooled=', GAVG)
print('TRIANGLE_BREAKS:', R_B, R_L, R_A)
print('EXACT_GAP_MAX:', F(13261, 160000), 'at s=', s)
print('WITNESS_O_FULL:', witness)
print('WITNESS_VALUE_FULL:', full_formula(s))
print('LR_SUPPORT_MIN:', lr_formula(s))
print('RATIONAL_SEPARATING_GAP:', lr_formula(s) - val(witness, s))
print('FULL_STOP_CONTINUE_POLICIES:', 64, 'terminal decisions Bayes optimal for (a,b)=(1,1)')
print('LR_DETERMINISTIC_DESCRIPTIONS:', len(LR_VERTEX_VALUES), 'including every terminal P/Q declaration')
for a in checks:
    print('PHASE_SAMPLE:', a, full_formula(a), lr_formula(a), gap_phase(a))
print('ALL EXACT CHECKS PASSED')
