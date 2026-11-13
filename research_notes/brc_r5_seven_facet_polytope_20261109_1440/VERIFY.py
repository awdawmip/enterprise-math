#!/usr/bin/env python3
"""Exact enumeration of every vertex of the fixed R5 4D Blackwell polytope.
Uses Fraction only; 7-facet and 17-edge enumeration are checked independently.
Source of fixed P and V: previous exact author-side PR #1859, f63a025...
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter

P = {
 (0,0): F('33553/432000'), (0,1): F('3997/368000'),
 (4,1): F('3997/690000'), (0,2): F('13091471/3762128400'),
 (2,2): F('8901809/21809440'), (4,2): F('170189123/37621284000'),
 (0,3): F('8294919533/677183112000'),
 (3,3): F('4095218743/29442744000'),
 (4,3): F('8294919533/188106420000'),
 (4,5): F('172449787/1363090000'),
 (5,5): F('219439/545236000'),
 (6,5): F('172449787/2180944000'),
 (6,6): F('38053/432000')
}
NEW = ((2,1),(3,1),(3,2),(2,3))
BASIS = (
 {(0,1):-F(10,23),(4,1):-F(13,23),(0,2):F(10,23),(2,2):-F(1),(4,2):F(13,23)},
 {(0,1):-F(5,23),(4,1):-F(18,23),(0,3):F(5,23),(3,3):-F(1),(4,3):F(18,23)},
 {(0,2):-F(5,23),(4,2):-F(18,23),(0,3):F(5,23),(3,3):-F(1),(4,3):F(18,23)},
 {(0,2):F(10,23),(2,2):-F(1),(4,2):F(13,23),(0,3):-F(10,23),(4,3):-F(13,23)}
)
ALL = tuple(P) + NEW
FAC = ((2,1),(3,1),(4,1),(3,2),(2,3),(4,2),(0,3))
C = {e:[F(int(e==x)) for x in NEW] for e in ALL}
for i,b in enumerate(BASIS):
 for e,v in b.items(): C[e][i] += v

def solve(a,b):
 m=[list(row)+[v] for row,v in zip(a,b)]
 for k in range(4):
  p=next((j for j in range(k,4) if m[j][k]),None)
  if p is None: return None
  m[k],m[p] = m[p],m[k]
  v=m[k][k]; m[k]=[x/v for x in m[k]]
  for j in range(4):
   if j!=k and m[j][k]:
    v=m[j][k]
    m[j]=[x-v*y for x,y in zip(m[j],m[k])]
 return tuple(row[-1] for row in m)

def weights(q):
 return {e:P.get(e,F(0))+sum((a*b for a,b in zip(C[e],q)),F(0)) for e in ALL}

def enumerate_vertices(ineq):
 vs=set(); full_rank=0
 for subset in combinations(ineq,4):
  q=solve([C[e] for e in subset],[-P.get(e,F(0)) for e in subset])
  if q is None: continue
  full_rank += 1
  w=weights(q)
  if all(w[e]>=0 for e in ineq):vs.add(q)
 return sorted(vs),full_rank

full,nfull=enumerate_vertices(ALL)
seven,nseven=enumerate_vertices(FAC)
assert full == seven and len(full)==12
assert nfull==324
assert all(sum(v>0 for v in weights(q).values())==13 for q in full)
assert all(sum(weights(q)[e]==0 for e in FAC)==4 for q in full)
assert all(min(weights(q)[e] for q in full)>0 for e in ALL if e not in FAC)

facets={e:{i for i,q in enumerate(full,1) if weights(q)[e]==0} for e in FAC}
assert sorted(map(len,facets.values())) == [6,6,6,6,8,8,8]
for e in FAC:
 assert len(facets[e])>=4
# The three 8-vertex facets are the triangle factor; the four 6-vertex
# facets have square incidence (cycle), with opposite intersections empty.
A=[e for e in FAC if len(facets[e])==8]
B=[e for e in FAC if len(facets[e])==6]
assert len(A)==3 and len(B)==4
assert all(len(facets[a]&facets[b])==4 for a,b in combinations(A,2))
assert sorted(len(facets[a]&facets[b]) for a,b in combinations(B,2))==[0,0,3,3,3,3]
# Product vertices have two active A facets and two active B facets.
assert all(sum(i in facets[e] for e in A)==2 and
           sum(i in facets[e] for e in B)==2 for i in range(1,13))

adj=[]
for i,j in combinations(range(1,13),2):
 zi={e for e in FAC if i in facets[e]}
 zj={e for e in FAC if j in facets[e]}
 if len(zi&zj)==3:adj.append((i,j))
faces2={frozenset(facets[e]&facets[f]) for e,f in combinations(FAC,2)
        if len(facets[e]&facets[f])>=3}
assert len(adj)==24 and len(faces2)==19
assert all(sum(i in pair for pair in adj)==4 for i in range(1,13))

c=F('225713944957/3385915560000')
def gap(q):return c+F(28,23)*q[1]+F(5,23)*q[2]+F(13,23)*q[3]
low=min(gap(q) for q in full); high=max(gap(q) for q in full)
assert low==c and high==F('8555233477/73606860000')
assert sum(gap(q)==high for q in full)==1
assert sum(gap(q)==low for q in full)==2

print('FULL17_NONSINGULAR_FOURSETS',nfull,'SEVEN_NONSINGULAR_FOURSETS',nseven)
print('PASS_EXACT_7_FACETS_12_VERTICES 12')
print('PASS_ALL_VERTICES_EXACT_13_EDGES')
print('PASS_COMBINATORIAL_TRIANGLE_TIMES_SQUARE_FVECTOR 12 24 19 7')
print('PASS_ATLAS_ESCAPE_RANGE',low,high)
for i,q in enumerate(full,1):
 print('V%02d'%i,'q='+','.join(map(str,q)),'support=13',
       'gap='+str(gap(q)),
       'zero='+str(tuple(e for e in ALL if weights(q)[e]==0)))
print('PASS_NONFACET_EDGE_STRICT_POSITIVITY',
      [(e,str(min(weights(q)[e] for q in full))) for e in ALL if e not in FAC])
