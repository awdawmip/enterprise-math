#!/usr/bin/env python3
"""Exact 8-leaf BRC-labeled external two-measure support-facet certificate.
Python standard library only; all mass and observation calculations use Fraction.
"""
from fractions import Fraction as F
from itertools import product

LR = {'': F(1), 'a': F(3, 2), 'b': F(1, 2),
      'ax': F(1), 'ay': F(2), 'bu': F(1), 'bv': F(1, 3)}
Q = {'': F(1), 'a': F(1, 2), 'b': F(1, 2),
     'ax': F(1, 4), 'ay': F(1, 4), 'bu': F(1, 8), 'bv': F(3, 8)}
for prefix, s in (('ax', F(1, 3)), ('bu', F(1, 6))):
    for label, ratio, conditional in (
            ('l', F(1, 2), s), ('m', F(1), 1 - 2*s),
            ('h', F(3, 2), s)):
        key = prefix + label
        LR[key] = ratio
        Q[key] = Q[prefix] * conditional
for prefix in ('ay', 'bv'):
    LR[prefix + 'm'] = LR[prefix]
    Q[prefix + 'm'] = Q[prefix]
CHILDREN = {'': ('a', 'b'), 'a': ('ax', 'ay'), 'b': ('bu', 'bv'),
            'ax': ('axl', 'axm', 'axh'), 'bu': ('bul', 'bum', 'buh'),
            'ay': ('aym',), 'bv': ('bvm',)}
TERMINALS = tuple(k for k in Q if k not in CHILDREN)
LEVEL = {k: 0 if k == '' else 1 if k in ('a', 'b') else
         2 if k in ('ax', 'ay', 'bu', 'bv') else 3 for k in Q}
ZERO = (F(0),) * 4
LAMBDA = (298, 375, 37, -17)

def add(*vs):
    return tuple(sum((v[i] for v in vs), F(0)) for i in range(4))

def stop(h, decision):
    p, q, t = Q[h] * LR[h], Q[h], LEVEL[h]
    return (F(0), q, t*p, t*q) if decision == 0 else (p, F(0), t*p, t*q)

def dot(x):
    return sum((LAMBDA[i] * x[i] for i in range(4)), F(0))

def rank(rows):
    matrix = [list(row) for row in rows]
    if not matrix:
        return 0
    nr, nc, j, rk = len(matrix), len(matrix[0]), 0, 0
    while j < nc and rk < nr:
        lead = next((i for i in range(rk, nr) if matrix[i][j]), None)
        if lead is None:
            j += 1
            continue
        matrix[rk], matrix[lead] = matrix[lead], matrix[rk]
        pivot = matrix[rk][j]
        matrix[rk] = [v / pivot for v in matrix[rk]]
        for i in range(nr):
            if i != rk and matrix[i][j]:
                coeff = matrix[i][j]
                matrix[i] = [u - coeff*v for u, v in zip(matrix[i], matrix[rk])]
        rk += 1
        j += 1
    return rk

# Exact probability conservation at every node, including hidden-history identity.
assert len(TERMINALS) == 8 and len(Q) == 15
assert all(x > 0 for x in Q.values())
for h, cs in CHILDREN.items():
    assert sum((Q[c] for c in cs), F(0)) == Q[h]
    assert sum((Q[c]*LR[c] for c in cs), F(0)) == Q[h]*LR[h]
assert sum((Q[c] for c in TERMINALS), F(0)) == F(1)
assert sum((Q[c]*LR[c] for c in TERMINALS), F(0)) == F(1)
assert LR['ax'] == LR['bu'] == F(1)
assert (Q['axl']/Q['ax'], Q['axm']/Q['ax'], Q['axh']/Q['ax']) == (F(1,3), F(1,3), F(1,3))
assert (Q['bul']/Q['bu'], Q['bum']/Q['bu'], Q['buh']/Q['bu']) == (F(1,6), F(2,3), F(1,6))

# Enumerate every deterministic seedless time/LR table: 3^6 nonterminal
# action tables and 2^5 terminal decision tables. Stop policy actions:
# 0=decide P, 1=decide Q, 2=continue.
terminal_ratios = tuple(sorted({LR[h] for h in TERMINALS}))
assert len(terminal_ratios) == 5
vectors = set()
descriptions = 0
for td in product((0, 1), repeat=5):
    terminal_decision = dict(zip(terminal_ratios, td))
    for actions_2 in product((0, 1, 2), repeat=3):
        action_2 = dict(zip((F(1), F(2), F(1,3)), actions_2))
        vec2 = {}
        for h in ('ax', 'ay', 'bu', 'bv'):
            a = action_2[LR[h]]
            vec2[h] = stop(h, a) if a != 2 else add(*(
                stop(c, terminal_decision[LR[c]]) for c in CHILDREN[h]))
        for act_a, act_b in product((0, 1, 2), repeat=2):
            va = stop('a', act_a) if act_a != 2 else add(vec2['ax'], vec2['ay'])
            vb = stop('b', act_b) if act_b != 2 else add(vec2['bu'], vec2['bv'])
            vroot_continue = add(va, vb)
            for root_action in (0, 1, 2):
                descriptions += 1
                vectors.add(stop('', root_action) if root_action != 2 else vroot_continue)
assert descriptions == 23328
assert len(vectors) == 326
minimum_coarse = min(dot(v) for v in vectors)
assert minimum_coarse == F(281)
tight = sorted((v for v in vectors if dot(v) == 281))
assert len(tight) == 4
assert rank([[v[i]-tight[0][i] for i in range(4)] for v in tight[1:]]) == 3
# The compressed hull is 4-dimensional, so the four tight points span a facet.
expected_tight = {
    (F(3,8),F(1,3),F(2),F(7,4)),
    (F(1,4),F(1,2),F(11,8),F(15,8)),
    (F(1,2),F(1,4),F(17,8),F(19,8)),
    (F(11,32),F(17,48),F(5,2),F(11,4)),
}
assert set(tight) == expected_tight
basis = [next(iter(vectors))]
for v in vectors:
    if rank([[p[i]-basis[0][i] for i in range(4)] for p in basis[1:]+[v]]) == len(basis):
        basis.append(v)
    if len(basis) == 5:
        break
assert len(basis) == 5

# Independent full-history Bellman oracle, optimized for this exact signed
# objective. Each physical history has its own action, including ax vs bu.
best_action = {}
def full_bellman(h):
    choices = [(dot(stop(h, 0)), 0), (dot(stop(h, 1)), 1)]
    if h in CHILDREN:
        choices.append((sum((full_bellman(c) for c in CHILDREN[h]), F(0)), 2))
    value, action = min(choices)
    best_action[h] = action
    return value
minimum_full = full_bellman('')
assert minimum_full == F(280)

def full_policy_vector(h):
    if best_action[h] != 2:
        return stop(h, best_action[h])
    return add(*(full_policy_vector(c) for c in CHILDREN[h]))
full_witness = full_policy_vector('')
assert full_witness == (F(3,8), F(1,3), F(19,8), F(21,8))
assert dot(full_witness) == minimum_full
assert best_action['ax'] == 2 and best_action['bu'] == 1
# The outcome is not only outside the behavioral seedless set but also its
# convex hull, and the separating normal is an exact facet normal.
assert minimum_coarse - minimum_full == 1
print('MODEL 8 positive Q/P leaves; single nonterminal LR collision ax~bu at t=2')
print('SEEDLESS_DESCRIPTIONS', descriptions, 'UNIQUE_OBSERVATIONS', len(vectors))
print('FACET_NORMAL', LAMBDA, 'COARSE_FACET_LEVEL', minimum_coarse)
print('FACET_TIGHT_VERTICES', len(tight), 'AFFINE_RANK', 3, 'COARSE_DIMENSION', 4)
print('FULL_OPTIMUM', minimum_full, 'COARSE_OPTIMUM', minimum_coarse, 'STRICT_GAP', minimum_coarse-minimum_full)
print('FULL_WITNESS', full_witness)
print('FULL_ACTIONS', tuple((k,best_action[k]) for k in ('','a','b','ax','ay','bu','bv')))
print('ALL EXACT CHECKS PASSED')
