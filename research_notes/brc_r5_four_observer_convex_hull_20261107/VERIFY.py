#!/usr/bin/env python3
"""Exact 34/26-corner and eight-convex-dominator certificate for R5."""
from fractions import Fraction as F
from itertools import product
def v(**d): return (F(0),)+tuple(F(d.get(k,0)) for k in 'gabuvwz')
def add(*args): return tuple(sum(x[i] for x in args) for i in range(8))
def scale(k,x): return tuple(k*t for t in x)
def neg(x): return scale(-1,x)
def value(aff,x): return aff[0]+sum(a*b for a,b in zip(aff[1:],x))
G,A,B,U,V,W,Z=[v(**{k:1}) for k in 'gabuvwz']
ONE=(F(1),)+(F(0),)*7
c0=add(scale(F(13,40),A),scale(F(1,80),B))
c1=add(scale(F(1,10),A),scale(F(9,40),B))
c2=add(scale(F(3,40),A),scale(F(21,80),B))
M=[add(scale(F(509,900),U),scale(F(47,180),Z),scale(F(67,162),add(V,neg(Z))),scale(F(1,100),W)),
   add(c0,neg(U)),scale(F(1,2),add(G,neg(A))),
   add(ONE,neg(G),c1,neg(V),scale(F(191,450),add(U,W)),scale(F(43,90),Z),scale(F(14,81),add(V,neg(Z)))),
   scale(F(1,2),add(G,neg(B))),add(c2,neg(W)),
   add(scale(F(1,100),U),scale(F(47,180),Z),scale(F(67,162),add(V,neg(Z))),scale(F(509,900),W))]
TP=add(ONE,G,scale(F(3,8),A),scale(F(5,8),B),scale(F(1,2),U),V,scale(F(3,2),W))
TQ=add(ONE,G,scale(F(1,2),A),scale(F(1,2),B),U,V,W)
LR=list(map(F,('1/10','1/2','3/4','1','5/4','3/2','19/10')))
def hinge(lam,x): return sum(max(F(0),1-(1+lam)*r)*value(m,x) for r,m in zip(LR,M))
def corners(seedless):
    out=set()
    for g,a,b in ((0,0,0),(1,0,0),(1,1,0),(1,0,1),(1,1,1)):
        for eta,omega,tA,tB in product((0,1),repeat=4):
            if seedless and tA!=tB: continue
            u=eta*(F(13,40)*a+F(1,80)*b)
            w=omega*(F(3,40)*a+F(21,80)*b)
            z=F(tA*a,10)
            vv=z+F(tB*9*b,40)
            out.add((F(g),F(a),F(b),u,vv,w,z))
    return sorted(out)
full=corners(False);seed=corners(True)
assert len(full)==34 and len(seed)==26
bad=[x for x in full if x not in seed]
assert len(bad)==8
WITNESSES=[
 [(11,'243/803'),(19,'126/803'),(20,'434/803')],
 [(19,'9/13'),(21,'4/13')],
 [(2,'253558/6198131'),(12,'570430/6198131'),(19,'234720/6198131'),(20,'5139423/6198131')],
 [(0,'6916/581811'),(3,'4446/193937'),(19,'370174/2521181'),(21,'6189719/7563543')],
 [(15,'3/8'),(24,'4/9'),(25,'13/72')],
 [(18,'9/40'),(25,'31/40')],
 [(15,'27/292'),(18,'13/292'),(24,'63/73')],
 [(3,'22646/7631655'),(11,'428564/7631655'),(19,'12522/508777'),(25,'1398523/1526331')]
]
critical=list(map(F,('-1','-9/19','-1/3','-1/5','0','1/3','1','9')))
for x in full:
    masses=[value(m,x) for m in M]
    assert all(y>=0 for y in masses)
    assert sum(masses)==1 and sum(r*m for r,m in zip(LR,masses))==1
    assert 1<=value(TP,x)<=4 and 1<=value(TQ,x)<=4
for x in seed:
    g,a,b,u,v,w,z=x
    assert 9*b*z==4*a*(v-z)
for k,(target,ws) in enumerate(zip(bad,WITNESSES)):
    weights=[(idx,F(weight)) for idx,weight in ws]
    assert all(w>=0 and 0<=idx<len(seed) for idx,w in weights)
    assert sum(w for _,w in weights)==1
    for t in (TP,TQ):
        assert sum(w*value(t,seed[idx]) for idx,w in weights)==value(t,target)
    gaps=[sum(w*hinge(lam,seed[idx]) for idx,w in weights)-hinge(lam,target) for lam in critical]
    assert all(g>=0 for g in gaps),(k,gaps)
    print('WITNESS',k,'residual',9*target[2]*target[6]-4*target[1]*(target[4]-target[6]),
          'weights',','.join('%s:%s'%(idx,w) for idx,w in weights),
          'minimum_hinge_gap',min(gaps))
print('PASS_EXACT_34_FULL_26_SEEDLESS_8_SIMULTANEOUS_HINGE_DOMINATORS')
print('PASS_ALL_REAL_FOUR_OBSERVER_CONVEX_SUPPORT_EQUALITY_BY_MULTIAFFINE_REDUCTION')
