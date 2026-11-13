#!/usr/bin/env python3
"""R5 exact collision residual locus: integer polyhedral and rational support audit.
Proof uses the published 24 exact facets; no numerical LP, SciPy or sampling.
"""
from itertools import combinations
from fractions import Fraction as F
import json
from pathlib import Path
S=[('A',1,120,240,-1),('B',1,240,120,-1),('A0',2,60,180,0),
('A1',2,60,60,0),('B0',2,180,60,1),('B1',2,60,60,1),
('A00',3,30,108,2),('A01',3,30,72,2),('A10',3,30,45,3),
('A11',3,30,15,3),('B00',3,90,36,4),('B01',3,90,24,4),
('B10',3,20,40,5),('B11',3,40,20,5)]
keys=[];ki=[]
for n,t,p,q,pa in S:
 k=(t,F(p,q))
 if k not in keys:keys.append(k)
 ki.append(keys.index(k))
assert len(S)==14 and len(keys)==12 and ki[3]==ki[5] and ki[9]==ki[13]
assert sum(S[i][2] for i in (0,1))==sum(S[i][3] for i in (0,1))==360
for i,(n,t,p,q,pa) in enumerate(S):
 assert p>0 and q>0
 kids=[s for s in S if s[4]==i]
 if kids:
  assert len(kids)==2 and sum(s[2] for s in kids)==p and sum(s[3] for s in kids)==q

def vectors(lr,a=1,b=1):
 out={}
 for mask in range(1<<(12 if lr else 14)):
  cont=[False]*14;R=DP=DQ=0
  for i,(n,t,p,q,pa) in enumerate(S):
   reach=pa<0 or cont[pa]
   stop=reach and bool(mask & (1<<(ki[i] if lr else i)))
   cont[i]=reach and not stop
   if stop:
    R+=q*(a if i==9 else b if i==13 else 0)
    DP+=(4-t)*p; DQ+=(4-t)*q
  out.setdefault((R,DP,DQ),mask)
 return out
L=vectors(True);G=vectors(False)
assert len(L)==272 and len(G)==647
C=json.loads(Path(__file__).with_name('FACET_CERT.json').read_text())
assert C['schema']=='R5_EQUAL_COLLISION_EXACT_3D_FACETS_V1'
facets=[tuple(x) for x in C['facets']]
assert len(facets)==len(set(facets))==24

def dot(n,p):return sum(n[i]*p[i] for i in range(3))
for plane in facets:
 assert all(dot(plane,p)<=plane[3] for p in L)
 assert all(dot(plane,p)<=plane[3] for p in G)
 assert sum(dot(plane,p)==plane[3] for p in L)>=3
box=[(0,-1,0,0),(0,1,0,1080),(0,0,-1,0),(0,0,1,1080)]
assert all(all(dot(n,p)<=n[3] for p in L) for n in box)
assert all(all(dot(n,p)<=n[3] for p in G) for n in box)
planes=facets+box

def det(a,b,c):
 return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
V=set();nonsing=0
for a,b,c in combinations(planes,3):
 den=det(a[:3],b[:3],c[:3])
 if den==0:continue
 nonsing+=1
 x=(F(det((a[3],a[1],a[2]),(b[3],b[1],b[2]),(c[3],c[1],c[2])),den),
 F(det((a[0],a[3],a[2]),(b[0],b[3],b[2]),(c[0],c[3],c[2])),den),
 F(det((a[0],a[1],a[3]),(b[0],b[1],b[3]),(c[0],c[1],c[3])),den))
 if all(dot(n,x)<=n[3] for n in planes):V.add(x)
assert len(V)==31 and V.issubset(L)
assert len(list(combinations(planes,3)))==3276 and nonsing==3075
assert any(det(tuple(a[i]-d[i] for i in range(3)),
               tuple(b[i]-d[i] for i in range(3)),
               tuple(c[i]-d[i] for i in range(3)))!=0
           for d,a,b,c in combinations(sorted(V),4))
Lu=vectors(True,1,0);Gu=vectors(False,1,0)
W=lambda p:F(p[0])-F(p[2],2)
assert max(map(W,Lu))==0 and max(map(W,Gu))==F(15,2)
assert F(15,2*360*1000)==F(1,48000)
TP=F(47,12);TQ=F(95,24)
eP=F(21,100)+TP/20+TQ/100
eQ=F(41,100)+TP/200-TQ/30+F(1,24000)
assert (eP,eQ)==(F(1069,2400),F(21433,72000))
assert 48000*eQ-240*TP+1624*TQ==19777
assert all(48000*(F(41,100)+(4-F(p[1],360))/200-(4-F(p[2],360))/30+F(p[0],360000))
              -240*(4-F(p[1],360))+1624*(4-F(p[2],360))<=19776 for p in Lu)
for a,b in ((1,1),(1,0),(1,-1)):
 for n,t,p,q,pa in S:
  Lratio=F(p,q)
  pe=F(1,5)+F(t,20)+F(t+1,100)/Lratio
  qe=F(2,5)-F(t,30)+F(t+2,200)*Lratio+F(a if n=='A11' else b if n=='B11' else 0,1000)
  assert 0<pe<1 and 0<qe<1
  if t==3:
   p4=F(1,5)+F(4,20)+F(5,100)/Lratio
   q4=F(2,5)-F(4,30)+F(6,200)*Lratio
   assert 0<p4<1 and 0<q4<1
assert (360,720) in {(p[1],p[2]) for p in L}
assert (720,360) in {(p[1],p[2]) for p in L}
print('EXACT_TREE nodes=14 lr_keys=12 collisions=2 strictly_positive=True')
print('EQUAL_COEFF all_FULL_masks=16384 all_LR_masks=4096 FULL_unique=647 LR_unique=272')
print('EXACT_FACET_CERT planes=24 bounded_intersection_triples=3276 nonsingular=3075 vertices=31')
print('EQUAL_COEFF_HULL_EQUAL rank=3 from invertible 3-coordinate projection')
print('UNEQUAL_COEFF_WITNESS full=(1069/2400,21433/72000,47/12,95/24)')
print('UNEQUAL_COEFF_SEPARATION 48000eQ-240TP+1624TQ<=19776; FULL=19777; gap=1/48000')
print('PASS_EXACT_R5_COLLISION_RESIDUAL_EQUALITY_LOCUS')
