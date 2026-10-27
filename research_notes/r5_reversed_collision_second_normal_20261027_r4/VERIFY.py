#!/usr/bin/env python3
"""Exact R5 reversed-collision separating-support certificate.

All probabilities and costs use fractions.Fraction. The finite tree is an
EXTERNAL positive BRC-weighted two-measure decision model, not native X6.
No floating-point arithmetic or external solver is used.
"""
from fractions import Fraction as F
from itertools import product

NORMAL = (298, 376, 37, -17)
SA0, SA1 = F(0), F(19, 71)
SB0, SB1 = F(22, 71), F(1, 2)
CORNERS = list(product((SA0, SA1), (SB0, SB1)))

# A(s_a,s_b) = A0 + A1*s_a + A2*s_b.
def aff(v=0, a=0, b=0):
    return (F(v), F(a), F(b))

def plus(*args):
    return tuple(sum((v[i] for v in args), F(0)) for i in range(3))

def scale(c, v):
    return tuple(F(c) * x for x in v)

def at(v, sa, sb):
    return v[0] + v[1]*sa + v[2]*sb

# Nonterminal masses, LR, times; historical physical labels must be preserved.
Q = {'': F(1), 'a': F(1, 2), 'b': F(1, 2),
     'ax': F(1, 4), 'ay': F(1, 4),
     'bu': F(1, 8), 'bv': F(3, 8)}
R = {'': F(1), 'a': F(3, 2), 'b': F(1, 2),
     'ax': F(1), 'ay': F(2), 'bu': F(1), 'bv': F(1, 3)}
TIME = {h: len(h) for h in Q}
CHILDREN = {'': ('a', 'b'), 'a': ('ax', 'ay'), 'b': ('bu', 'bv'),
            'ax': ('axl', 'axm', 'axh'),
            'bu': ('bul', 'bum', 'buh'),
            'ay': ('aym',), 'bv': ('bvm',)}

# Terminal leaf Q masses as symbolic affine fractions.
QL = {'axl': aff(a=F(1,4)), 'axm': aff(F(1,4), a=-F(1,2)),
      'axh': aff(a=F(1,4)),
      'bul': aff(b=F(1,8)), 'bum': aff(F(1,8), b=-F(1,4)),
      'buh': aff(b=F(1,8)),
      'aym': aff(F(1,4)), 'bvm': aff(F(3,8))}
RL = {'axl': F(1,2), 'axm': F(1), 'axh': F(3,2),
      'bul': F(1,2), 'bum': F(1), 'buh': F(3,2),
      'aym': F(2), 'bvm': F(1,3)}
assert set(QL) == set(RL)

# Symbolic conservation in BOTH source measures, every branch.
for h, children in CHILDREN.items():
    q_sum = plus(*(aff(Q[c]) if c in Q else QL[c] for c in children))
    p_sum = plus(*(aff(Q[c]*R[c]) if c in Q else scale(RL[c], QL[c]) for c in children))
    assert q_sum == aff(Q[h]), (h, 'Q', q_sum)
    assert p_sum == aff(Q[h]*R[h]), (h, 'P', p_sum)
assert plus(*QL.values()) == aff(1)
assert plus(*(scale(RL[h],v) for h,v in QL.items())) == aff(1)

A, B, C, D = NORMAL

def decision_cost(q, r, t, action):
    """Affine signed cost of stopping at one physical node."""
    base = C*t*r + D*t
    return scale(base + (A*r if action == 'Q' else B), q)

# The Bayes-optimal terminal label is independent of its predecessor.
TERMINAL = {h: ('Q' if A*RL[h] <= B else 'P') for h in QL}
assert {r: {TERMINAL[h] for h in QL if RL[h] == r} for r in set(RL.values())} == {
    F(1,3): {'Q'}, F(1,2): {'Q'}, F(1): {'Q'},
    F(3,2): {'P'}, F(2): {'P'} }

STOP = {h: {d: decision_cost(aff(Q[h]), R[h], TIME[h], d)
            for d in ('Q','P')} for h in Q}
LEAF = {h: decision_cost(QL[h], RL[h], 3, TERMINAL[h]) for h in QL}
NODES = ('', 'a', 'b', 'ax', 'ay', 'bu', 'bv')

def symbolic_policy(actions):
    action = dict(zip(NODES, actions))
    def go(h):
        if h in QL:
            return LEAF[h]
        if action[h] == 'C':
            return plus(*(go(k) for k in CHILDREN[h]))
        return STOP[h][action[h]]
    return go('')

full_rows = []
coarse_rows = []
for table in product(('P', 'Q', 'C'), repeat=len(NODES)):
    value = symbolic_policy(table)
    full_rows.append(value)
    if table[NODES.index('ax')] == table[NODES.index('bu')]:
        coarse_rows.append(value)
assert len(full_rows) == 3**7 == 2187
assert len(coarse_rows) == 3**6 == 729

# Derived analytic Bellman branches, genuine policy values, not fitted constants.
FULL_CERT = aff(F(1135,4), b=-F(71,8))
COARSE_CERT = aff(F(284), b=-F(71,8))
full_policy = ('C','C','C','Q','P','C','C')
coarse_policy = ('C','P','C','C','P','C','C')
assert symbolic_policy(full_policy) == FULL_CERT
assert symbolic_policy(coarse_policy) == COARSE_CERT

# Every competitor minus the proposed optimum is affine. A rectangular box
# is the convex hull of its four rational corners: 4 inequalities per policy
# are a complete all-real-parameter certificate, not sampling evidence.
for rows, cert in ((full_rows, FULL_CERT),(coarse_rows,COARSE_CERT)):
    for v in rows:
        for sa,sb in CORNERS:
            assert at(v,sa,sb) >= at(cert,sa,sb), (v,sa,sb)
assert plus(COARSE_CERT,scale(-1,FULL_CERT)) == aff(F(1,4))

# Independently sum the four original observer coordinates of the witnesses.
SA, SB = F(1,10),F(2,5)
assert SA0 < SA < SA1 and SB0 < SB < SB1

def witness_vector(policy):
    acts = dict(zip(NODES,policy))
    visited = []
    def walk(h):
        if h in QL:
            visited.append((h,3,TERMINAL[h],at(QL[h],SA,SB),RL[h]))
            return
        if acts[h]=='C':
            for k in CHILDREN[h]: walk(k)
        else:
            visited.append((h,TIME[h],acts[h],Q[h],R[h]))
    walk('')
    ep=eq=tp=tq=F(0)
    for h,t,d,q,r in visited:
        p=q*r
        if d=='Q': ep+=p
        if d=='P': eq+=q
        tp+=p*t
        tq+=q*t
    assert sum(q for h,t,d,q,r in visited)==1
    assert sum(q*r for h,t,d,q,r in visited)==1
    return (ep,eq,tp,tq),visited

OF, full_stops = witness_vector(full_policy)
OC, coarse_stops = witness_vector(coarse_policy)
assert OF == (F(17,40),F(3,10),F(9,4),F(5,2)), OF
assert OC == (F(7,40),F(11,20),F(3,2),F(2)), OC

def signed(vec):
    return sum((F(k)*v for k,v in zip(NORMAL,vec)),F(0))
assert signed(OF)==at(FULL_CERT,SA,SB)==F(1401,5)
assert signed(OC)==at(COARSE_CERT,SA,SB)==F(5609,20)
assert signed(OC)-signed(OF)==F(1,4)

# Check previous published normal's zero-gap observation at the same point
# by a separate exact direct Bellman recursion, not by modifying the new proof.
def prev_normal_gap():
    a,b,c,d=(298,375,37,-17)
    def decision(h,t,q,r,choice):
        return q*(c*t*r+d*t + (a*r if choice=='Q' else b))
    def opt(force=None):
        def go(h):
            if h in QL:
                q=at(QL[h],SA,SB)
                return min(decision(h,3,q,RL[h],x) for x in ('Q','P'))
            stop = {x:decision(h,TIME[h],Q[h],R[h],x) for x in ('Q','P')}
            stop['C']=sum((go(x) for x in CHILDREN[h]),F(0))
            return stop[force] if force is not None and h in ('ax','bu') else min(stop.values())
        return go('')
    return opt(), min(opt(x) for x in ('P','Q','C'))
assert prev_normal_gap()==(F(2799,10),F(2799,10))

print('R5 REVERSED-COLLISION SECOND-NORMAL CERTIFICATE PASS')
print('INPUT: sa=1/10, sb=2/5; NORMAL=(298,376,37,-17)')
print('SOURCE MASS CONSERVATION: P=Q=1, EXACT SYMBOLIC PASS')
print('DETERMINISTIC POLICY ENUMERATION: full=2187, seedless=729')
print('BOX CORNERS:', [(str(a),str(b)) for a,b in CORNERS])
print('ALL CORNER COMPARISONS:',4*(len(full_rows)+len(coarse_rows)),'PASS')
print('OPTIMUM FOR ALL REAL 0<sa<19/71, 22/71<sb<1/2:')
print('  full     = 1135/4 - (71/8)*sb')
print('  seedless = 284 - (71/8)*sb')
print('  gap      = 1/4')
print('FULL_POLICY:',dict(zip(NODES,full_policy)))
print('COARSE_POLICY:',dict(zip(NODES,coarse_policy)))
print('FULL_OBSERVER:',tuple(map(str,OF)),'J=',signed(OF))
print('COARSE_OBSERVER:',tuple(map(str,OC)),'J=',signed(OC))
print('PREVIOUS NORMAL (298,375,37,-17) OPTIMA:',prev_normal_gap(), 'GAP=0')
print('NEW EXACT RATIONAL SUPPORT GAP:',F(1,4))
print('SCOPE: external two-measure positive BRC tree; UNREVIEWED / NOT_ADMITTED')
