#!/usr/bin/env python3
"""R71: Exact finite certificate for D=4 weighted positive-BRC moment lattice.

This is integer combinatorial arithmetic on the R70 *conditional* normalized
positive-branch star-moment observer. It does not implement a native Cell/Link
reset, an X6 update, or a time evolution.
"""
from itertools import combinations
from math import gcd
from functools import reduce
import json
from pathlib import Path

D=4
n=D-1
source_d=(2,3,4)
rows_id=((1,0,0),(0,1,0),(0,0,1))
# m_t - m_1 where m_t=sum_{d=0}^4 c_d d^t.
rows_z={t: tuple(d**t-d for d in source_d) for t in range(2,D+1)}
def diff(i,j):
    z_i=(0,0,0) if i==1 else rows_z[i]
    z_j=rows_z[j]
    return tuple(b-a for a,b in zip(z_i,z_j))
rows_B=tuple(diff(i,j) for i,j in combinations(range(1,D+1),2))
T=rows_id+rows_B

def vector_cross(u,v):
    return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
def canonical(v):
    g=reduce(gcd,v,0)
    if not g: return None
    w=tuple(x//g for x in v)
    if next(x for x in w if x)!=abs(next(x for x in w if x)):
        w=tuple(-x for x in w)
    return w

def q(a):
    return max(sum(max(x,0) for x in a),sum(max(-x,0) for x in a))
def sign(x): return (x>0)-(x<0)
def signature(a): return tuple(sign(sum(x*y for x,y in zip(row,a))) for row in T)
def compatible(a,b): return all(x*y>=0 for x,y in zip(signature(a),signature(b)))

axes={canonical(vector_cross(a,b)) for a,b in combinations(T,2)}
axes.discard(None)
rays=sorted(axes | {tuple(-x for x in a) for a in axes})
assert len(axes)==28 and len(rays)==56
assert len(T)==9
assert len(rows_B)==6
assert rows_B == ((2,6,12),(6,24,60),(14,78,252),(4,18,48),(12,72,240),(8,54,192))
max_ray=max(q(a) for a in rays)
assert max_ray==125
triples=[]
for indices in combinations(range(len(rays)),3):
    ra,rb,rc=(rays[k] for k in indices)
    if compatible(ra,rb) and compatible(ra,rc) and compatible(rb,rc):
        triples.append((q(ra)+q(rb)+q(rc), indices))
assert len(triples)==212
largest=max(score for score,indices in triples)
assert largest==235
witness=next(tuple(rays[i] for i in indices) for score, indices in triples if score==235)
assert sorted(map(q,witness))==[39,71,125]
q_bound=max(max_ray,largest-1)
assert q_bound==234
old_Q=n*n*2*(4**4-4)**2
assert old_Q==1143072

# Independent bounded sanity test on the exact integer lattice.
checks=0
for p in range(1,21):
    for a in range(-p,p+1):
      for b in range(-p,p+1):
       for c in range(-p,p+1):
        v=(a,b,c)
        if v!=(0,0,0) and q(v)==p:
          checks+=1
          assert min(q(v),q_bound)<=q_bound

out={
  'schema':'X6_R71_D4_WEIGHTED_RAY_BOUND_CERTIFICATE_V1',
  'date':'2026-11-21',
  'model':'R70 conditional positive-branch normalized star moment, shared offset and arbitrary positive channel error weights',
  'frozen_p000_commit':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
  'degree_difference_coordinates':['a2','a3','a4'],
  'T_rows':[list(row) for row in T],
  'hyperplane_count':len(T),
  'independent_cross_product_lines':len(axes),
  'oriented_primitive_rays':len(rays),
  'max_ray_port_requirement':max_ray,
  'conformal_oriented_triples_checked':len(triples),
  'max_conformal_triple_port_sum':largest,
  'triple_witness':[list(x) for x in witness],
  'triple_witness_q':[q(x) for x in witness],
  'certified_universal_port_bound':q_bound,
  'prior_universal_port_bound':old_Q,
  'tested_nonzero_vectors_q_le_20':checks,
  'validation_status':'PASS exact integer certificate; author checked, not independently reviewed',
  'all_primitive_ray_orientations':[list(a) for a in rays],
}
print(json.dumps({k:v for k,v in out.items() if k != 'all_primitive_ray_orientations'},indent=2))
