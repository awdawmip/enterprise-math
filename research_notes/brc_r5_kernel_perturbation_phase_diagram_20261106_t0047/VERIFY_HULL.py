#!/usr/bin/env python3
"""Complete exact four-observer hull-equivalence certificate at delta=1/4.
No numpy/SciPy required: 80 independently checked proposed halfspaces are read
from H_FACETS.txt. Every check and graph traversal uses integer/Fraction only.
Each policy visits an observation key at most once, so behavioral support
maximization has a deterministic optimum.
"""
from fractions import Fraction as F
from itertools import product,combinations
from math import gcd,lcm
from functools import reduce
from pathlib import Path
R2=(F(3,4),F(5,4)); Q2=(F(1,2),F(1,2))
R3=(F(1,2),F(1),F(3,2))
Q3=((F(13,20),F(1,5),F(3,20)),(F(1,40),F(9,20),F(21,40)))
R4=(F(1,10),F(1),F(19,10))
Q4={
(0,0):(F(509,900),F(382,900),F(9,900)),
(1,0):(F(509,900),F(382,900),F(9,900)),
(0,2):(F(9,900),F(382,900),F(509,900)),
(1,2):(F(9,900),F(382,900),F(509,900)),
(0,1):(F(1,90)+F(1,4),F(44,45)-F(1,2),F(1,90)+F(1,4)),
(1,1):(F(67,162),F(14,81),F(67,162))}

def obs(t1,t2,t3,t4):
 v=[F(0)]*4
 def add(q,r,t,d):
  v[0]+=q*r if d=='Q' else 0
  v[1]+=q if d=='P' else 0
  v[2]+=q*r*t
  v[3]+=q*t
 if t1!='C':add(F(1),F(1),1,t1)
 else:
  for i,(r2,q2) in enumerate(zip(R2,Q2)):
   if t2[i]!='C':add(q2,r2,2,t2[i]);continue
   for j,(r3,q3) in enumerate(zip(R3,Q3[i])):
    q=q2*q3
    if t3[j]!='C':add(q,r3,3,t3[j]);continue
    for k,(r4,q4) in enumerate(zip(R4,Q4[i,j])):
     add(q*q4,r4,4,t4[k])
 return tuple(v)

def full(n):
 def leaf(r,t):return max(n[0]*r+(n[2]*r+n[3])*t,n[1]+(n[2]*r+n[3])*t)
 def h3(i,j):return max(leaf(R3[j],3),sum(Q4[i,j][k]*leaf(r4,4) for k,r4 in enumerate(R4)))
 def h2(i):return max(leaf(R2[i],2),sum(Q3[i][j]*h3(i,j) for j in range(3)))
 return max(leaf(F(1),1),sum(Q2[i]*h2(i) for i in range(2)))

seen=set(); obspts=[]
for t1 in 'QPC':
 for t2 in product('QPC',repeat=2):
  for t3 in product('QPC',repeat=3):
   for t4 in product('QP',repeat=3):
    w=obs(t1,t2,t3,t4)
    if w not in seen:seen.add(w);obspts.append(w)
L=lcm(*(v.denominator for x in obspts for v in x))
assert L==720000 and len(obspts)==806
P=[tuple(int(x*L) for x in v) for v in obspts]
Pset=set(P)
H=[]
for line in Path(__file__).with_name('H_FACETS.txt').read_text(encoding='utf-8').splitlines():
 if not line.strip():continue
 parts=tuple(int(v) for v in line.split())
 assert len(parts)==5 and any(parts[:4])
 H.append((parts[:4],parts[4]))

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def det3(A):
 a,b,c=A
 return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def kernel3(A):
 v=tuple(((-1)**j)*det3([[a[k] for k in range(4) if k!=j] for a in A]) for j in range(4))
 g=reduce(gcd,v,0)
 return tuple(x//g for x in v) if g else None
def rank(rows):
 b=[list(map(F,row)) for row in rows]
 if not b:return 0
 i=0
 for col in range(4):
  pivot=next((k for k in range(i,len(b)) if b[k][col]),None)
  if pivot is None:continue
  b[i],b[pivot]=b[pivot],b[i]
  v=b[i][col]
  b[i]=[x/v for x in b[i]]
  for k in range(i+1,len(b)):
   v=b[k][col]
   if v:b[k]=[x-v*y for x,y in zip(b[k],b[i])]
  i+=1
  if i==len(b):break
 return i

def incident(v):return [j for j,(n,c) in enumerate(H) if dot(n,v)==c]

# Exact bounded H representation and an LR starting vertex.
assert len(H)==80 and len(set(H))==80
assert all(any(hi[0]==tuple((-1 if k==j else 0) for k in range(4)) and hi[1]==(-L if j>=2 else 0) for hi in H) for j in range(4))
assert all(any(hi[0]==tuple((1 if k==j else 0) for k in range(4)) and hi[1]==(4*L if j>=2 else L) for hi in H) for j in range(4))
assert rank([tuple(p[k]-P[0][k] for k in range(4)) for p in P])==4
assert all(dot(n,p)<=c for n,c in H for p in P)
v0=next(p for p in P if rank([H[i][0] for i in incident(p)])==4)
assert rank([H[i][0] for i in incident(v0)])==4
vertices={v0};queue=[v0]
edgecount=0;tested_triples=0;max_active=0
while queue:
 v=queue.pop()
 active=incident(v)
 max_active=max(max_active,len(active))
 assert rank([H[i][0] for i in active])==4
 for i1,i2,i3 in combinations(active,3):
  d=kernel3([H[i][0] for i in (i1,i2,i3)])
  if d is None:continue
  tested_triples+=1
  t=[dot(H[i][0],d) for i in active]
  if all(a<=0 for a in t):pass
  elif all(a>=0 for a in t):d=tuple(-x for x in d)
  else:continue # Not a feasible edge of the active tangent cone.
  ratios=[F(c-dot(n,v),dot(n,d)) for n,c in H if dot(n,d)>0]
  if not ratios:raise AssertionError('unbounded edge detected')
  lam=min(ratios)
  assert lam>0
  w=tuple(v[k]+lam*d[k] for k in range(4))
  assert all(dot(n,w)<=c for n,c in H)
  edgecount+=1
  if w not in vertices:
   vertices.add(w);queue.append(w)
   assert len(vertices)<3000
assert len(vertices)==82
print('H_vertices=',len(vertices),'max_active=',max_active,'edge_tests=',edgecount,'triples=',tested_triples)
absent=vertices-Pset
assert len(absent)==0
# Every H vertex is seedless LR, so H=conv(LR).
for n,c in H:
    assert full(n)*L<=c, (n,c,full(n)*L)
print('PASS_CERTIFIED_R5_DELTA_1_4_ALL_DIRECTION_HULL_EQUALITY')
print('exact_H_inequalities=',len(H),'LR_deterministic_unique=',len(P),'scale=',L)
print('all_FULL_Bellman_facets_checked=',len(H))
print('Proof: every LR point lies in bounded H, every H vertex enumerated via exact active-triple edges and lies in LR; every FULL support facet <= H.')
