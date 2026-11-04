#!/usr/bin/env python3
"""Exact two-origin, three-stage serial-hazard BRC observer checks."""
from fractions import Fraction as F
from itertools import product

w = (F(1,3), F(2,3))

def weighted(a,b):
    return tuple(w[0]*x+w[1]*y for x,y in zip(a,b))

def dot(n,v):
    return sum((a*b for a,b in zip(n,v)), F(0))

def check_family(V, name, normals):
    full = [weighted(V[0][j],V[1][k]) for j,k in product(range(3), repeat=2)]
    lr = [weighted(V[0][j],V[1][j]) for j in range(3)]
    assert len(full)==9 and len(lr)==3
    for n in normals:
        hfull=max(dot(n,z) for z in full)
        hlr=max(dot(n,z) for z in lr)
        d=hfull-hlr
        assert d>=0
        print(name, 'n=', tuple(map(str,n)), 'FULL=',hfull,'LR=',hlr,'GAP=',d)
    return full,lr

strict = (
    ((F(0),F(1),F(1),F(1)),(F(1,2),F(1,2),F(2),F(2)),(F(1),F(0),F(3),F(3))),
    ((F(1),F(0),F(1),F(1)),(F(1,2),F(1,2),F(2),F(2)),(F(0),F(1),F(3),F(3)))
)
unit=(F(1),F(0),F(0),F(0))
full,lr=check_family(strict,'STRICT', (unit,(F(0),F(1),F(0),F(0)),(F(0),F(0),F(1),F(0)),(F(1),F(1),F(0),F(0))))
assert max(dot(unit,v) for v in full)==F(1)
assert max(dot(unit,v) for v in lr)==F(2,3)
assert weighted(strict[0][2],strict[1][0]) == (F(1),F(0),F(5,3),F(5,3))

d=((F(1,10),F(1,5),F(1),F(1)),
   (F(1,5),F(1,10),F(2),F(2)),
   (F(3,10),F(1,5),F(3),F(3)))
b=((F(1,20),F(0),F(0),F(0)),(F(0),F(1,30),F(0),F(0)))
lam=(F(1,2),F(3,2))
V=tuple(tuple(tuple(b[i][k]+lam[i]*d[j][k] for k in range(4)) for j in range(3)) for i in range(2))
full2,lr2=check_family(V,'HOMOTHETIC', (unit,(F(0),F(1),F(0),F(0)),(F(0),F(0),F(1),F(0)),(F(2),-F(3),F(1,7),-F(2,7))))
L=sum(w[i]*lam[i] for i in range(2))
assert L==F(7,6)
for j,k in product(range(3),repeat=2):
    pi=[F(0)]*3
    pi[j]+=w[0]*lam[0]/L
    pi[k]+=w[1]*lam[1]/L
    assert sum(pi)==1 and all(t>=0 for t in pi)
    assert weighted(V[0][j],V[1][k])==tuple(sum((pi[t]*lr2[t][c] for t in range(3)),F(0)) for c in range(4))

pia=(F(1,5),F(3,10),F(1,2))
pib=(F(1,3),F(1,6),F(1,2))
pit=tuple(sum((w[i]*lam[i]*pp for i,pp in enumerate((pia[j],pib[j]))),F(0))/L for j in range(3))
assert sum(pit)==1
full_int=tuple(sum((w[i]*pi[j]*V[i][j][c] for i,pi in enumerate((pia,pib)) for j in range(3)), F(0)) for c in range(4))
lr_int=tuple(sum((pit[j]*lr2[j][c] for j in range(3)),F(0)) for c in range(4))
assert full_int==lr_int
alpha=pit[0]
beta=pit[1]/(1-alpha) if alpha<1 else F(0)
assert 0<=alpha<=1 and 0<=beta<=1
print('HOMOTHETIC_INTERIOR','pi=',tuple(map(str,pit)),'alpha=',alpha,'beta=',beta)
print('PASS_EXACT_R5_TWO_SERIAL_MERGERS_HAZARD_FILTER')
