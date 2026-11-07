#!/usr/bin/env python3
"""Exact rational certificate for equal-TV / distinct-likelihood-profile R5 experiment."""
from fractions import Fraction as F
from itertools import product

w = (F(1, 2), F(1, 2))
Q = ((F(1, 2), F(1, 2)), (F(1, 3), F(1, 3), F(1, 3)))
P = ((F(1, 4), F(3, 4)), (F(1, 12), F(1, 3), F(7, 12)))
ratio = tuple(tuple(p / q for p, q in zip(pp, qq)) for pp, qq in zip(P, Q))
assert ratio == ((F(1, 2), F(3, 2)), (F(1, 4), F(1), F(7, 4)))
assert len(set(sum((list(x) for x in ratio), []))) == 5
assert all(sum(row) == 1 for row in Q + P)
assert all(x > 0 for row in Q + P for x in row)

k, tau = F(3, 8), F(1, 48)
delta = tuple(min(F(1), k) - sum(min(pp, k * qq) for pp, qq in zip(P[i], Q[i])) for i in range(2))
tv = tuple(sum(abs(pp - qq) for pp, qq in zip(P[i], Q[i])) / 2 for i in range(2))
assert tv == (F(1, 4), F(1, 4))
assert delta == (F(0), F(1, 24))
assert sum(w[i] * delta[i] for i in range(2)) == tau

def obs(actions, labels):
    """actions[h]: 0 STOP_P, 1 STOP_Q, 2 CONTINUE; labels[h][s]: 0 P, 1 Q."""
    ep = eq = F(0)
    tp = tq = F(0)
    for h in range(2):
        a = actions[h]
        tp += w[h] * (1 + (a == 2))
        tq += w[h] * (1 + (a == 2))
        if a == 0:
            eq += w[h]
        elif a == 1:
            ep += w[h]
        else:
            for j, label in enumerate(labels[h]):
                if label == 1:
                    ep += w[h] * P[h][j]
                else:
                    eq += w[h] * Q[h][j]
    return ep, eq, tp, tq

def score(o):
    return -o[0] - k * o[1] - tau * o[2]

label_choices = list(product((0, 1), repeat=5))
full = []
lr = []
for flat in label_choices:
    lab = (flat[:2], flat[2:])
    for actions in product(range(3), repeat=2):
        full.append(obs(actions, lab))
    for action in range(3):
        lr.append(obs((action, action), lab))
assert len(full) == 288 and len(lr) == 96
hfull = max(map(score, full))
hlr = max(map(score, lr))
W = obs((0, 2), ((0, 0), (1, 0, 0)))
# A stops with P; B continues, low LR declares Q, other terminals P.
assert W == (F(1, 24), F(5, 6), F(3, 2), F(3, 2))
assert hfull == score(W) == -F(37, 96)
assert hlr == -F(19, 48)
assert hfull - hlr == F(1, 96)
assert hfull - hlr == sum(w[i] * max(F(0), delta[i] - tau) for i in range(2)) - max(F(0), sum(w[i] * delta[i] for i in range(2)) - tau)
assert (hfull - hlr) / (1 + k + tau) == F(1, 134)
print('SOURCE_RATIO_A', ','.join(map(str, ratio[0])))
print('SOURCE_RATIO_B', ','.join(map(str, ratio[1])))
print('TV_A_B', ','.join(map(str, tv)))
print('BAYES_ADVANTAGES_AT_K', ','.join(map(str, delta)))
print('POLICIES_FULL_LR', len(full), len(lr))
print('WITNESS', ','.join(map(str, W)))
print('SUPPORT_FULL', hfull)
print('SUPPORT_LR', hlr)
print('SUPPORT_GAP', hfull - hlr)
print('DIST_INFINITY_LOWER_BOUND', F(1, 134))
print('PASS_EXACT_R5_EQUAL_TV_DIFFERENT_ROC_SEPARATION')
