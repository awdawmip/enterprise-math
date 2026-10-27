#!/usr/bin/env python3
"""Exact rational phase diagram for signed BRC two-law support functional.
External finite probability tree, not native Heartbeat or X6 computation.
"""
from fractions import Fraction as F
from itertools import product

A, B, U, V = F(298), F(375), F(37), F(-17)
R0 = {'':F(1), 'a':F(3,2), 'b':F(1,2),
      'ax':F(1), 'ay':F(2), 'bu':F(1), 'bv':F(1,3)}
Q0 = {'':F(1), 'a':F(1,2), 'b':F(1,2),
      'ax':F(1,4), 'ay':F(1,4), 'bu':F(1,8), 'bv':F(3,8)}
CH = {'':('a','b'), 'a':('ax','ay'), 'b':('bu','bv'),
      'ax':('axl','axm','axh'), 'bu':('bul','bum','buh'),
      'ay':('aym',), 'bv':('bvm',)}

def model(sa, sb):
    assert 0 < sa < F(1,2) and 0 < sb < F(1,2)
    r, q = dict(R0), dict(Q0)
    for h, s in (('ax',sa),('bu',sb)):
        for suffix, ratio, w in [('l',F(1,2),s), ('m',F(1),1-2*s),
                                 ('h',F(3,2),s)]:
            r[h+suffix], q[h+suffix] = ratio, q[h]*w
    for h in ('ay','bv'):
        r[h+'m'], q[h+'m'] = r[h], q[h]
    assert len(q) == 15 and len([h for h in q if h not in CH]) == 8
    assert all(x > 0 for x in q.values())
    for h, cs in CH.items():
        assert sum((q[c] for c in cs), F(0)) == q[h]
        assert sum((q[c]*r[c] for c in cs), F(0)) == q[h]*r[h]
    return r, q

def independent_bellman(sa, sb, collision_action=None):
    r, q = model(sa,sb)
    def solve(h):
        ratio = r[h]
        costs = [(B,0), (A*ratio,1)]
        if h in CH:
            next_value = U*ratio + V + sum(
                (q[c]/q[h]*solve(c) for c in CH[h]), F(0))
            costs.append((next_value,2))
        if collision_action is not None and h in ('ax','bu'):
            return next(value for value, action in costs if action == collision_action)
        return min(value for value, _ in costs)
    return solve('')

def plus(x):
    return max(F(0),x)

def closed_full(sa, sb):
    return F(281) - plus(18*sa-5) - plus(9*sb-F(5,2))

def closed_coarse(sa, sb):
    return min(F(281), F(282)-plus(18*sa-5)-plus(9*sb-F(3,2)))

def closed_gap(sa,sb):
    return min(plus(18*sa-5), plus(1-plus(9*sb-F(3,2))))

samples = (F(1,100),F(1,10),F(1,6),F(1,4),F(5,18),
           F(1,3),F(2,5),F(49,100))
for sa,sb in product(samples,repeat=2):
    full = independent_bellman(sa,sb)
    coarse = min(independent_bellman(sa,sb,action) for action in (0,1,2))
    assert full == closed_full(sa,sb), (sa,sb,full,closed_full(sa,sb))
    assert coarse == closed_coarse(sa,sb), (sa,sb,coarse,closed_coarse(sa,sb))
    assert coarse-full == closed_gap(sa,sb), (sa,sb)
    assert (coarse>full) == (sa>F(5,18) and sb<F(5,18))
assert (closed_full(F(1,3),F(1,6)),
        closed_coarse(F(1,3),F(1,6)),
        closed_gap(F(1,3),F(1,6))) == (F(280),F(281),F(1))
assert (closed_full(F(49,100),F(1,100)),
        closed_coarse(F(49,100),F(1,100)),
        closed_gap(F(49,100),F(1,100))) == (F(13859,50),F(13909,50),F(1))
assert closed_gap(F(49,100),F(49,100)) == 0
print('EXACT_FRACTION_BELLMAN_PASS')
print('NODES 15 POSITIVE_LEAVES 8 GRID_CHECKS',len(samples)**2)
print('PHASE_BOUNDARY sa=5/18 sb=5/18')
print('BASE full=280 coarse=281 gap=1')
print('DISTANT full=13859/50 coarse=13909/50 gap=1')
print('GLOBAL_GAP_MAX 1 attained when sa>=1/3 and sb<=1/6')
print('STRICT_REGION sa>5/18 AND sb<5/18; outside only this normal does not separate')
