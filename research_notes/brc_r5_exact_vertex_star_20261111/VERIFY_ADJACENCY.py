#!/usr/bin/env python3
"""Exact entire 1-skeleton star of the published 14-arc R5 vertex."""
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter
from pathlib import Path
from sympy import Matrix, Rational
r=list(map(Q, ('1/10','1/2','3/4','1','5/4','3/2','19/10')))
D=[(i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j]
data=dict(s.split('=',1) for s in Path(__file__).with_name('WITNESS.txt').read_text().splitlines())
E0=Matrix([Rational(s) for s in data['ARCS'].split(',')])
C=Matrix.hstack(*(Matrix([int(i==k) for k in range(7)]
    +[int(j==k) for k in range(7)]
    +[Rational(r[i].numerator,r[i].denominator) if j==k else 0 for k in range(7)]) for i,j in D))
M={
(0,0):'219346331/10192753200',(0,1):'18669495/951323632',
(1,1):'1898238/8493961',(5,1):'3733899/475661816',
(2,2):'196521/2426846',(0,3):'8057361/237830908',
(2,3):'1544855/16987922',(3,3):'377644447/2548188300',
(4,3):'1544855/16987922',(5,3):'26530335/475661816',
(6,3):'196521/67951688',(0,5):'196521/9707384',
(6,5):'1375647/19414768',(6,6):'451274777/3397584400'}
x=Matrix([Rational(M[a]) if a in M else 0 for a in D])
P=[i for i,v in enumerate(x) if v>0];Z=[i for i,v in enumerate(x) if v==0]
assert C.rank()==15 and C[:,P].rank()==14 and len(P)==14
assert min(E0)>0 and C*x==C*E0
I=list(C[:,P].T.rref()[1]);assert len(I)==14
Ainv=C[I,P].inv()
coeff={k:Ainv*C[I,k] for k in Z}
# Row 16 gives a nonzero coordinate on the 1-dimensional column-space quotient.
lam={k:C[16,k]-(C[16,P]*coeff[k])[0] for k in Z}
assert any(v for v in lam.values())
neg={D[k]:lam[k] for k in Z if lam[k]<0}
pos={D[k]:lam[k] for k in Z if lam[k]>0}
zero={D[k]:lam[k] for k in Z if lam[k]==0}
assert neg=={(0,2):Rational(-13,20),(1,2):Rational(-1,4)}
assert pos=={(3,2):Rational(1,4),(4,2):Rational(1,2),
             (5,2):Rational(3,4),(6,2):Rational(23,20)}
assert len(zero)==10 and len(Z)==16
adj=[]
def pivot(adds,weights):
    d=Matrix.zeros(30,1)
    for k,w in zip(adds,weights): d[k]=w
    old=-sum((coeff[k]*w for k,w in zip(adds,weights)),Matrix.zeros(14,1))
    for p,v in zip(P,old): d[p]=v
    assert C*d==Matrix.zeros(21,1)
    assert all(d[k]>=0 for k in Z) and any(d[p]<0 for p in P)
    t=min(x[p]/(-d[p]) for p in P if d[p]<0)
    y=x+t*d
    assert all(v>=0 for v in y) and C*y==C*x
    U=sorted(set(P)|{k for k,v in enumerate(y) if v>0})
    assert len(U)-C[:,U].rank()==1
    S2=[k for k,v in enumerate(y) if v>0]
    assert C[:,S2].rank()==len(S2)
    adj.append((tuple(D[k] for k in adds),len(S2),sum(v!=0 for v in d),t))
for k in Z:
    if lam[k]==0: pivot((k,),(Rational(1),))
for k,l in combinations(Z,2):
    if lam[k]<0<lam[l]:pivot((k,l),(lam[l],-lam[k]))
    if lam[l]<0<lam[k]:pivot((l,k),(lam[k],-lam[l]))
assert len(adj)==18 and len({t[0] for t in adj})==18
assert Counter(v[1] for v in adj)=={14:10,15:8}
assert Counter(v[2] for v in adj)=={6:13,9:2,10:3}
print('OBS_RANK',C.rank(),'FIBER_DIMENSION',30-C.rank())
print('VERTEX_SUPPORT',len(P),'VERTEX_RANK',C[:,P].rank())
print('ZERO_ARCS',len(Z),'SINGLE_INSERTIONS',len(zero))
print('QUOTIENT_NEG',neg,'QUOTIENT_POS',pos)
print('DOUBLE_INSERTIONS',len(neg)*len(pos))
print('EXACT_ADJACENT_VERTICES',len(adj))
print('NEIGHBOR_SUPPORT_COUNT',dict(Counter(v[1] for v in adj)))
print('ADJACENCY_CIRCUIT_SUPPORT',dict(Counter(v[2] for v in adj)))
for a,s,d,t in adj:print('NEIGHBOR',a,'support',s,'direction-support',d,'exact-step',t)
print('PASS_18_NEIGHBORS_EXHAUSTIVE')
