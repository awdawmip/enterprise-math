#!/usr/bin/env python3
"""PREFIX-578-R2 exact X6-BRC axis/gate third cumulants.

Rebuilds PREFIX565 native edges and PREFIX566 future-exact 37-state quotient.
Requires SymPy for rational matrix inversion. Observer weights are exact.
Scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import Counter
from itertools import product
from math import factorial
import json
import sympy as sp

STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(star,c):
    return tuple((-1 if c>0 else 1)*k for k in STARS[star] if k!=abs(c))
PHASES=tuple((a,p,sgn*k) for a in range(4) for k in STARS[a]
             for sgn in (-1,1) for p in near(a,sgn*k))
PHASE_INDEX={x:i for i,x in enumerate(PHASES)}
def successors(phase):
    a,p,c=PHASES[phase]
    b=next(b for b in range(4) if b!=a and abs(c) in STARS[b])
    return tuple(PHASE_INDEX[t] for t in
      [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
NEXT=tuple(successors(i) for i in range(48))
TARGET=PHASE_INDEX[(0,1,-3)]
ACTIONS=tuple(product(range(3),(0,1)))
ROOT=(0,)*6

def sg(phase,k):
    c=PHASES[phase][2]
    return (1 if c>0 else -1) if abs(c)==k else 0

def edge(port,action,root=ROOT):
    phase,bit=divmod(port,2)
    slot,newbit=action
    nxt=NEXT[phase][slot]
    weights=[]
    for k in range(1,7):
        left=sg(phase,k); right=sg(nxt,k); z=root[k-1]
        v=abs(left)+abs(right)-abs(right-z)+abs(left-z)
        assert v in (0,2)
        weights.append(v//2)
    gate=int(bit==newbit==1 and nxt==TARGET)
    return 2*nxt+newbit,tuple(weights)+(gate,)

def weighted_quotient(rows):
    ids=[0]*len(rows)
    growth=[1]
    for _ in range(len(rows)):
        keys=[]
        for row in rows:
            out=Counter()
            for (j,a,b,g),m in row.items():
                out[(ids[j],a,b,g)]+=m
            keys.append(tuple(sorted(out.items())))
        lookup={}
        nxt=[lookup.setdefault(k,len(lookup)) for k in keys]
        if nxt==ids: break
        ids=nxt
        growth.append(len(lookup))
    else:
        raise AssertionError('nonconvergent partition')
    quotient={}
    for i,row in enumerate(rows):
        q=Counter()
        for (j,a,b,g),m in row.items():
            q[ids[j],a,b,g]+=m
        if ids[i] in quotient:
            assert quotient[ids[i]]==q
        else:
            quotient[ids[i]]=q
    return tuple(ids),tuple(quotient[i] for i in range(len(quotient))),growth

rows=[Counter((j,w[4],w[5],w[6]) for action in ACTIONS
        for j,w in [edge(i,action)]) for i in range(96)]
gate_edges=sorted((i,j) for i,row in enumerate(rows)
     for (j,a,b,g),m in row.items() if g for _ in range(m))
assert gate_edges==[(7,9),(29,9),(31,9)]
ids,Q,growth=weighted_quotient(rows)
assert len(Q)==37 and growth==[1,4,13,21,33,37]
sizes=[Counter(ids)[i] for i in range(37)]
assert sizes==[8,4,2,1,1,2,2,8,4,2,4,4,2,4,1,1,1,1,2,2,4,
    2,4,4,2,2,2,2,2,2,2,2,2,2,2,2,2]
n=len(Q)
pi=sp.Matrix(1,n,lambda i,j:sp.Rational(sizes[j],96))
ones=sp.ones(n,1)
P=sp.zeros(n,n)
for i,row in enumerate(Q):
    for (j,a,b,g),m in row.items():
        P[i,j]+=sp.Rational(m,6)
assert P*ones==ones and pi*P==pi
Z=sp.eye(n)-P+ones*pi
Zinv=Z.inv()
assert Z*Zinv==sp.eye(n)

