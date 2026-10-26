#!/usr/bin/env python3
"""Exact rational check of coarse terminal observer LR-necessity witness.
Finite verification only. The universal theorem is established separately by proof.
"""
from fractions import Fraction as F
from itertools import product

H = ('a','b','c','d')
P = dict(zip(H, (F(1,4),)*4))
Q = dict(zip(H, (F(1,8),F(3,8),F(1,4),F(1,4))))
x = {'a':'A','b':'A','c':'B','d':'B'}
r = F(1)
assert sum(P.values()) == sum(Q.values()) == 1
assert all(P[h]>0 and Q[h]>0 for h in H)

# All 16 full-history deterministic depth-one decisions, exact rational.
history_points=[]
for actions in product((0,1), repeat=4):
    pa=sum((P[h]*u for h,u in zip(H,actions)),F(0))
    qa=sum((Q[h]*u for h,u in zip(H,actions)),F(0))
    history_points.append((pa,qa))
assert len(history_points)==16

# All four compressed deterministic classifiers and their convex randomized mixtures.
compressed_points=[]
for a,b in product((0,1),repeat=2):
    act = {'A':a,'B':b}
    pa=sum((P[h]*act[x[h]] for h in H),F(0))
    qa=sum((Q[h]*act[x[h]] for h in H),F(0))
    compressed_points.append((pa,qa))
assert len(compressed_points)==4
assert all(p==q for p,q in compressed_points)

history_support=max((q-r*p for p,q in history_points))
compressed_support=max((q-r*p for p,q in compressed_points))
assert history_support==F(1,8)
assert compressed_support==F(0)

# Unique 2-class compressed state masses and a quantitative fiber-straddling defect.
state_mass={key:(sum((P[h] for h in H if x[h]==key), F(0)),
                 sum((Q[h] for h in H if x[h]==key), F(0))) for key in ('A','B')}
assert state_mass=={'A':(F(1,2),F(1,2)),'B':(F(1,2),F(1,2))}
positive=lambda v:max(v,F(0))
fine=sum((positive(Q[h]-r*P[h]) for h in H),F(0))
coarse=sum((positive(q-r*p) for p,q in state_mass.values()),F(0))
assert (fine,coarse,fine-coarse)==(F(1,8),F(0),F(1,8))

# Original event D=1 precisely on symbol 'b'.
p_event=P['b'];q_event=Q['b']
assert (p_event,q_event)==(F(1,4),F(3,8))
assert (p_event,q_event) not in compressed_points
print('PASS: P/Q positive normalized; 16 full-history and 4 compressed deterministic decisions')
print('PASS: observed D=1 masses under P,Q =',str(p_event),str(q_event))
print('PASS: exact support (fine, coarse, gap) =',fine,coarse,fine-coarse)
print('Scope: horizon 1, alphabet 4, deterministic decisions exhaustive; randomized policies handled analytically by convex support.')
