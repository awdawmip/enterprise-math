#!/usr/bin/env python3
"""Exact finite positive two-measure BRC tree certificate, EC48J.

No floating-point, external packages, or guessed tolerance. This program checks
ALL 3^7 full-history and 3^6 compressed nonterminal deterministic policies and
each affine objective at ALL four parameter-box corners. At terminal nodes,
the Bayes label is optimal for the specified signed normal independently of
predecessor and source kernel, so both terminal decision spaces are covered
for linear support minima (not for nonconvex raw-image membership).
"""
from fractions import Fraction as F
from itertools import product

NORMAL = (304, 212, -20, 33)
SA, SB = F(1, 5), F(1, 4)
SA_RANGE = (F(19, 100), F(21, 100))
SB_RANGE = (F(6, 25), F(13, 50))
BOX_CORNERS = tuple(product(SA_RANGE, SB_RANGE))
GUARANTEED_GAP = F(1, 10)
NODES = ('', 'a', 'b', 'ax', 'ay', 'bu', 'bv')
Q = {'': F(1), 'a': F(1, 2), 'b': F(1, 2),
     'ax': F(1, 4), 'ay': F(1, 4),
     'bu': F(1, 8), 'bv': F(3, 8)}
LR = {'': F(1), 'a': F(3, 2), 'b': F(1, 2),
      'ax': F(1), 'ay': F(2), 'bu': F(1), 'bv': F(1, 3)}
CHILDREN = {'': ('a', 'b'), 'a': ('ax', 'ay'), 'b': ('bu', 'bv'),
            'ax': ('axl', 'axm', 'axh'), 'bu': ('bul', 'bum', 'buh'),
            'ay': ('aym',), 'bv': ('bvm',)}

def affine(c=0, da=0, db=0):
    return (F(c), F(da), F(db))

def add(*vectors):
    return tuple(sum((v[j] for v in vectors), F(0)) for j in range(3))

def scale(k, v):
    return tuple(F(k)*x for x in v)

def evaluate(v, sa, sb):
    return v[0] + v[1]*sa + v[2]*sb

LEAF_Q = {
    'axl': affine(da=F(1, 4)),
    'axm': affine(F(1, 4), da=-F(1, 2)),
    'axh': affine(da=F(1, 4)),
    'aym': affine(F(1, 4)),
    'bul': affine(db=F(1, 8)),
    'bum': affine(F(1, 8), db=-F(1, 4)),
    'buh': affine(db=F(1, 8)),
    'bvm': affine(F(3, 8)),
}
LEAF_LR = {
    'axl': F(1, 2), 'axm': F(1), 'axh': F(3, 2),
    'aym': F(2), 'bul': F(1, 2), 'bum': F(1),
    'buh': F(3, 2), 'bvm': F(1, 3),
}
assert set(LEAF_Q) == set(LEAF_LR)
for history, children in CHILDREN.items():
    q_child = add(*(affine(Q[c]) if c in Q else LEAF_Q[c] for c in children))
    p_child = add(*(affine(Q[c]*LR[c]) if c in Q else scale(LEAF_LR[c], LEAF_Q[c])
                    for c in children))
    assert q_child == affine(Q[history]), (history, 'Q mass')
    assert p_child == affine(Q[history]*LR[history]), (history, 'P mass')
assert add(*LEAF_Q.values()) == affine(1)
assert add(*(scale(LEAF_LR[k], v) for k, v in LEAF_Q.items())) == affine(1)
assert all(evaluate(v, sa, sb)>0 for v in LEAF_Q.values() for sa, sb in BOX_CORNERS)

A, B, C, D = NORMAL
# At a fixed leaf LR, time cost cancels in the Q/P decision comparison.
TERMINAL_LABEL = {h: ('Q' if A*LEAF_LR[h] <= B else 'P') for h in LEAF_Q}
assert TERMINAL_LABEL == {'axl':'Q','axm':'P','axh':'P','aym':'P',
                          'bul':'Q','bum':'P','buh':'P','bvm':'Q'}

def signed_stop_cost(q_aff, ratio, t, decision):
    return scale(C*t*ratio + D*t + (A*ratio if decision=='Q' else B), q_aff)

STOP_COST = {h: {d:signed_stop_cost(affine(Q[h]),LR[h],len(h),d) for d in ('P','Q')}
             for h in NODES}
LEAF_COST = {h:signed_stop_cost(LEAF_Q[h],LEAF_LR[h],3,TERMINAL_LABEL[h])
             for h in LEAF_Q}

def policy_cost(actions):
    policy = dict(zip(NODES, actions))
    def descend(history):
        if history in LEAF_COST:
            return LEAF_COST[history]
        if policy[history] == 'C':
            return add(*(descend(k) for k in CHILDREN[history]))
        return STOP_COST[history][policy[history]]
    return descend('')

FULL_POLICY = ('C','C','C','P','C','C','Q')
SEEDLESS_POLICY = ('C','P','C','C','P','C','Q')
assert SEEDLESS_POLICY[3] == SEEDLESS_POLICY[5]
FULL_AFFINE = affine(F(1571, 8), db=-F(15, 2))
COARSE_WITNESS_AFFINE = affine(F(1573, 8), db=-F(15, 2))
assert policy_cost(FULL_POLICY) == FULL_AFFINE
assert policy_cost(SEEDLESS_POLICY) == COARSE_WITNESS_AFFINE

full_count = seedless_count = full_comparisons = seedless_comparisons = 0
smallest_full_advantage = smallest_compressed_margin = None
best_full_at_point = best_seedless_at_point = None
for policy in product(('P','Q','C'), repeat=7):
    v = policy_cost(policy)
    full_count += 1
    z = evaluate(v, SA, SB)
    best_full_at_point = z if best_full_at_point is None else min(best_full_at_point, z)
    for sa,sb in BOX_CORNERS:
        difference = evaluate(v,sa,sb) - evaluate(FULL_AFFINE,sa,sb)
        assert difference >= 0, ('FULL BOX FAILURE', policy, sa, sb, difference)
        smallest_full_advantage = (difference if smallest_full_advantage is None else
                                   min(smallest_full_advantage,difference))
        full_comparisons += 1
    if policy[3] == policy[5]:
        seedless_count += 1
        best_seedless_at_point = z if best_seedless_at_point is None else min(best_seedless_at_point,z)
        for sa,sb in BOX_CORNERS:
            margin = evaluate(v,sa,sb)-evaluate(FULL_AFFINE,sa,sb)
            assert margin >= GUARANTEED_GAP, ('GAP BOX FAILURE',policy,sa,sb,margin)
            smallest_compressed_margin = (margin if smallest_compressed_margin is None else
                                          min(smallest_compressed_margin,margin))
            seedless_comparisons += 1

assert full_count == 2187 and seedless_count == 729
assert full_comparisons == 8748 and seedless_comparisons == 2916
assert smallest_full_advantage == 0
assert smallest_compressed_margin == GUARANTEED_GAP
assert best_full_at_point == F(389,2)
assert best_seedless_at_point == F(779,4)
assert best_seedless_at_point-best_full_at_point == F(1,4)

# Independently sum the four original observable coordinates at (sa,sb).
def observer_vector(actions):
    policy = dict(zip(NODES,actions))
    endpoints = []
    def descend(h):
        if h in LEAF_Q:
            endpoints.append((h,3,TERMINAL_LABEL[h],evaluate(LEAF_Q[h],SA,SB),LEAF_LR[h]))
        elif policy[h]=='C':
            for k in CHILDREN[h]:descend(k)
        else:
            endpoints.append((h,len(h),policy[h],Q[h],LR[h]))
    descend('')
    assert sum((q for _,_,_,q,_ in endpoints),F(0)) == 1
    assert sum((q*r for _,_,_,q,r in endpoints),F(0)) == 1
    pe = sum((q*r for _,_,d,q,r in endpoints if d=='Q'),F(0))
    qe = sum((q for _,_,d,q,r in endpoints if d=='P'),F(0))
    tp = sum((t*q*r for _,t,_,q,r in endpoints),F(0))
    tq = sum((t*q for _,t,_,q,r in endpoints),F(0))
    return (pe,qe,tp,tq),endpoints

of, full_stops = observer_vector(FULL_POLICY)
oc, seedless_stops = observer_vector(SEEDLESS_POLICY)
linear = lambda vec:sum((F(k)*v for k,v in zip(NORMAL,vec)),F(0))
assert linear(of) == best_full_at_point
assert linear(oc) == best_seedless_at_point

# A separate exact recursion, conditioning the seedless collision action,
# verifies the point minimization independently of the 2187/729 loop.
def bellman_fixed_collision(collision_action=None):
    def value(h):
        if h in LEAF_Q:
            return evaluate(LEAF_COST[h],SA,SB)
        choices = {d:evaluate(STOP_COST[h][d],SA,SB) for d in ('P','Q')}
        choices['C'] = sum((value(k) for k in CHILDREN[h]),F(0))
        return (choices[collision_action] if collision_action is not None and
                h in ('ax','bu') else min(choices.values()))
    return value('')
assert bellman_fixed_collision() == F(389,2)
assert min(bellman_fixed_collision(x) for x in ('P','Q','C')) == F(779,4)

print('R5 EC48J THIRD-NORMAL EXACT CERTIFICATE PASS')
print('INPUT sa=1/5 sb=1/4; NORMAL=(304,212,-20,33)')
print('BRC P/Q source mass symbolic conservation: PASS')
print('Terminal decision: independent Bayes label at each LR, exact')
print('Policy enumeration: full=',full_count,'seedless=',seedless_count)
print('Parameter rectangle [19/100,21/100] x [6/25,13/50]')
print('Exact affine vertex checks: full=',full_comparisons, 'seedless=',seedless_comparisons,
      'total=',full_comparisons+seedless_comparisons)
print('Full optimum throughout rectangle: 1571/8 - (15/2)*sb')
print('Seedless minus full >= 1/10 throughout rectangle (ALL real parameters)')
print('Tight rectangle margin:',smallest_compressed_margin)
print('At 1/5,1/4: full=',best_full_at_point,'seedless=',best_seedless_at_point,
      'exact gap=',best_seedless_at_point-best_full_at_point)
print('Full optimal nonterminal policy:',dict(zip(NODES,FULL_POLICY)))
print('Seedless optimal nonterminal policy:',dict(zip(NODES,SEEDLESS_POLICY)))
print('Full four-observer witness:',tuple(map(str,of)))
print('Seedless four-observer witness:',tuple(map(str,oc)))
print('Full terminal/stops:',[(k,t,d,str(q),str(r)) for k,t,d,q,r in full_stops])
print('Seedless terminal/stops:',[(k,t,d,str(q),str(r)) for k,t,d,q,r in seedless_stops])
print('Independent exact Bellman check: PASS')
print('SCOPE: external positive two-measure BRC; author-side UNREVIEWED/NOT_ADMITTED')
