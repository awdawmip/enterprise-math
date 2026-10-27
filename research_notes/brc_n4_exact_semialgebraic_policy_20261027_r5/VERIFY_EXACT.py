#!/usr/bin/env python3
"""Exact rational regression for finite-tree sequential-policy semantics.
No quantifier-elimination implementation and no native P000 experiment.
"""
from fractions import Fraction as F
from itertools import product

Q = {'': F(1), 'a': F(1,2), 'b': F(1,2),
     'ax': F(1,4), 'ay': F(1,4), 'bx': F(1,4), 'by': F(1,4)}
P = {'': F(1), 'a': F(1,2), 'b': F(1,2),
     'ax': F(3,8), 'ay': F(1,8), 'bx': F(1,4), 'by': F(1,4)}
NODES = ('','a','b','ax','ay','bx','by')
INTERNAL = ('','a','b')
STOP_P, STOP_Q, CONTINUE = 'P','Q','C'

for h in NODES:
    assert P[h] > 0 and Q[h] > 0
for h in INTERNAL:
    children = [g for g in NODES if len(g) == len(h)+1 and g.startswith(h)]
    assert sum((P[g] for g in children), F(0)) == P[h]
    assert sum((Q[g] for g in children), F(0)) == Q[h]


def vector(actions):
    """Direct nonanticipative probability accumulation, including root stopping."""
    ep = eq = tp = tq = F(0)
    for h in NODES:
        ancestors = ('',) if len(h) == 1 else (('', h[:1]) if len(h)==2 else ())
        if any(actions[a] != CONTINUE for a in ancestors):
            continue
        action = actions[h]
        if action == CONTINUE:
            tp += P[h]
            tq += Q[h]
        elif action == STOP_Q:
            ep += P[h]
        elif action == STOP_P:
            eq += Q[h]
        else:
            raise AssertionError(action)
    return (ep, eq, tp, tq)


def objective(obs):
    ep, eq, tp, tq = obs
    return ep + eq + (tp + tq)/32


def enumeration(groups):
    domains = [('P','Q','C') if len(group[0]) < 2 else ('P','Q') for group in groups]
    minimum = None
    witness = None
    count = 0
    for choices in product(*domains):
        a = {h: decision for group, decision in zip(groups, choices) for h in group}
        value = objective(vector(a))
        count += 1
        if minimum is None or value < minimum:
            minimum, witness = value, a
    return minimum, count, witness


full_groups = (('',), ('a',), ('b',), ('ax',), ('ay',), ('bx',), ('by',))
lr_groups = (('',), ('a','b'), ('ax',), ('ay',), ('bx','by'))
fv, fc, fw = enumeration(full_groups)
cv, cc, cw = enumeration(lr_groups)
assert fc == 432 and cc == 72
assert fv == F(31,32) and cv == F(1)
assert cv - fv == F(1,32)
assert vector(fw) == (F(1,8),F(3,4),F(3,2),F(3,2))

# Independent rational Bellman calculation: H(l)=min(l,1), c(l)=(l+1)/32.
H = lambda l: min(l,F(1))
c = lambda l: (l+1)/32
la = [P[h]/Q[h] for h in ('ax','ay')]
fa = (H(la[0])+H(la[1]))/2
fb = H(F(1))
Va = min(H(F(1)), c(F(1))+fa)
Vb = min(H(F(1)), c(F(1))+fb)
full_bellman = min(H(F(1)),c(F(1))+(Va+Vb)/2)
compressed_at_t1 = min(H(F(1)), c(F(1))+(fa+fb)/2)
coarse_bellman = min(H(F(1)),c(F(1))+compressed_at_t1)
assert full_bellman == fv and coarse_bellman == cv

print('TREE_POSITIVITY_NORMALIZATION=PASS')
print(f'FULL_DETERMINISTIC_POLICIES={fc}')
print(f'COARSE_DETERMINISTIC_POLICIES={cc}')
print(f'FULL_MIN_J={fv}')
print(f'COARSE_MIN_J={cv}')
print(f'EXACT_SEPARATION={cv-fv}')
print('FULL_POLICY_O=' + ','.join(map(str, vector(fw))))
print('BELLMAN_AND_EXHAUSTIVE_ENUMERATION_MATCH=PASS')
print('QUANTIFIER_ELIMINATION_NOT_EXECUTED')
