#!/usr/bin/env python3
"""Exact Fraction algebra/polyhedral audit of EC49FSY; not a Bellman solver.
For original-source recomputation, use the self-contained evidence archive.
"""
import itertools,json
from fractions import Fraction as Q
from pathlib import Path
C=json.loads(Path(__file__).with_name("EC49FSY_CERT.json").read_text())
L=[(Q(323),-Q(89),-Q(12),-Q(141)),(Q(325),-Q(94),-Q(9),-Q(141)),(Q(324),-Q(141),-Q(8),-Q(93))]
bounds=[(Q(1,2),Q(2,3)),(Q(7,16),Q(57,128)),(Q(21,32),Q(1531,2304))]
def cost(l,p):return l[0]+sum(l[i+1]*p[i] for i in range(3))
def swapped(p):return min(cost(l,p) for l in L)
def direct(p):a,b,z=p;return 319-18*a-75*b-141*z
def lin_solve(eq):
 m=[[Q(x) for x in row]+[Q(rhs)] for row,rhs in eq]
 for j in range(3):
  k=next((i for i in range(j,3) if m[i][j]),None)
  if k is None:return None
  m[j],m[k]=m[k],m[j]
  d=m[j][j];m[j]=[x/d for x in m[j]]
  for i in range(3):
   if i==j:continue
   d=m[i][j];m[i]=[m[i][t]-d*m[j][t] for t in range(4)]
 return tuple(m[i][-1] for i in range(3))
planes=[]
for i,(lo,hi) in enumerate(bounds):
 v=[Q(0)]*3;v[i]=Q(1)
 planes.extend([(tuple(v),lo),(tuple(v),hi)])
for i,j in itertools.combinations(range(3),2):
 planes.append((tuple(L[i][k]-L[j][k] for k in range(1,4)),L[j][0]-L[i][0]))
pts=set()
for sub in itertools.combinations(planes,3):
 p=lin_solve(sub)
 if p is not None and all(lo<=x<=hi for x,(lo,hi) in zip(p,bounds)):pts.add(p)
assert len(pts)==22
obs=C["lower_slab_swapped_22_exact_bellman_vertices"]
assert len(obs)==22 and set(tuple(map(Q,r[:3])) for r in obs)==pts
for r in obs:assert swapped(tuple(map(Q,r[:3])))==Q(r[3])
for r in C["lower_face_direct_4_exact_bellman_vertices"]:
 assert direct(tuple(map(Q,r[:3])))==Q(r[3])
g=[(direct(p)-swapped(p),p) for p in pts]
assert min(v for v,p in g)==Q(441,128) and max(v for v,p in g)==Q(259,16)
for r in C["new_independent_raw_94family"]:assert swapped(tuple(map(Q,r[:3])))==Q(r[3])
print("PASS 22 exact polyhedral vertices, 4 direct corner values, 2 independent reported identities, sharp gaps")
print("ORIGINAL_NATIVE_BELLMAN_RECOMPUTATION: requires the separate frozen-source evidence archive")
