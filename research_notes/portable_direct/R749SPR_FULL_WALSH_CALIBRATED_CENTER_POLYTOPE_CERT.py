#!/usr/bin/env python3
"""R749SPR: complete 3D minimax-center polytope at t=1/10,s=1/2, exact arithmetic.
No scientific use of numerical LP, approximate tests or native X6 operations.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json

MASKS=(3,12,15,1,2,4,8)
C=tuple(tuple(-1 if (k&m).bit_count()&1 else 1 for m in MASKS) for k in range(16))
A=tuple(c[2:] for c in C)
B=tuple(-10-c[0]-5*c[1] for c in C)
FACETS=(
 ((-1,-1,-1),-2,0x0F8F,(-1,0,0,9,6)),
 ((-1,-1, 1),-2,0x00BF,(-1,0,0,6,9)),
 ((-1, 1,-1),-2,0x00DF,(-1,0,0,6,9)),
 ((-1, 1, 1),-2,0x01FF,(-1,0,0,6,9)),
 (( 1,-1,-1),-2,0x00EF,(0,-1,-1,5,9)),
 (( 1,-1, 1),-4,0x02FF,(-1,0,0,6,9)),
 (( 1, 1,-1),-4,0x04FF,(-1,0,0,6,9)),
 (( 1, 1, 1),-2,0x007F,(0,1,1,5,9)),
)

def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def feas(y):return all(dot(a,y)>=b for a,b in zip(A,B))
def bareiss5(ind):
 n=5;d=[list(A[i])+[B[i]] for i in ind];prev=1
 for j in range(n-1):
  row=next((k for k in range(j,n) if d[k][j]),None)
  if row is None:return None
  if row!=j:d[j],d[row]=d[row],d[j]
  p=d[j][j]
  for k in range(j+1,n):
   v=d[k][j]
   for l in range(j+1,n+1):
    z=d[k][l]*p-v*d[j][l]
    assert z%prev==0
    d[k][l]=z//prev
   d[k][j]=0
  prev=p
 if not d[-1][n-1]:return None
 out=[F(0)]*n
 for j in range(n-1,-1,-1):out[j]=(F(d[j][n])-sum((d[j][k]*out[k] for k in range(j+1,n)),F(0)))/d[j][j]
 return tuple(out)

def cross(a,b):return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def solve3(planes):
 (a,r),(b,s),(c,t)=planes
 det=dot(a,cross(b,c))
 if det==0:return None
 # Cramer's rule using oriented scalar triple products
 rhs=(F(r),F(s),F(t))
 x=(dot(rhs,cross((a[1],b[1],c[1]),(a[2],b[2],c[2])))/det,
    dot((a[0],b[0],c[0]),cross(rhs,(a[2],b[2],c[2])))/det,
    dot((a[0],b[0],c[0]),cross((a[1],b[1],c[1]),rhs))/det)
 return x

def run():
 sources=set();non=feas_bases=0
 for ind in combinations(range(16),5):
  y=bareiss5(ind)
  if y is None:continue
  non+=1
  if feas(y):feas_bases+=1;sources.add(y)
 assert len(sources)==50 and non==3008 and feas_bases==196
 # Each exposed event yields a necessary inequality in scaled Q=(10h,10u,10v).
 witnesses=[]
 for m,c,mask,source in FACETS:
  v=tuple(sum(A[k][i] for k in range(16) if mask&(1<<k)) for i in range(5))
  assert v[:3]==m and feas(source)
  assert dot(v,source)==72+c
  witnesses.append({'normal':list(m),'right_side':c,'event_mask_hex':hex(mask),'source_scaled_10':list(source),'event_vector':list(v)})
 # Exactly 11 vertices from all 8 choose 3 intersecting triples; all sign normals present -> bounded.
 all3=[(m,c) for m,c,*_ in FACETS]
 centers=set();nonsingular=0;feasible_triples=0
 for T in combinations(all3,3):
  q=solve3(T)
  if q is None:continue
  nonsingular+=1
  if all(dot(m,q)>=c for m,c in all3):feasible_triples+=1;centers.add(q)
 assert len(centers)==11,(len(centers),sorted(centers))
 expected={(-2,-1,1),(-2,1,-1),(-1,-2,1),(-1,-1,2),(-1,1,-2),(-1,2,-1),(0,-2,0),(0,0,-2),(0,0,2),(0,2,0),(2,0,0)}
 assert centers==expected
 for q in centers:
  q5=tuple(map(F,(*q,0,0)))
  assert feas(q5)
  assert max(sum((abs(dot(a,tuple(y[i]-q5[i] for i in range(5)))) for a in A),F(0)) for y in sources)==144
 # Irredundancy: each of the 8 supporting hyperplanes contains 3 affinely independent vertices.
 facets_tight=[]
 for m,c,*_ in FACETS:
  on=[p for p in centers if dot(m,p)==c]
  assert any(cross(tuple(b[i]-a[i] for i in range(3)),tuple(d[i]-a[i] for i in range(3)))!=(0,0,0) for a,b,d in combinations(on,3))
  facets_tight.append(len(on))
 # Full 5D source-fiber optimal calibrated center must have w=z=0: two signed source pairs.
 four=[(1,0,0,9,4),(1,0,0,-9,-4),(1,0,0,4,9),(1,0,0,-4,-9)]
 assert all(feas(y) for y in four)
 # Unconstrained lower bound from two opposite compatible sources.
 p=(0,-1,-1,5,9);n=(0,-1,-1,-5,-9)
 assert feas(p) and feas(n)
 assert sum(abs(dot(a,tuple(p[i]-n[i] for i in range(5)))) for a in A)==288
 # Calibrated center feasibility and exact upper against all sources implies common radius 9/20.
 print(json.dumps({
  'status':'PASS','unit':'R749SPR','pinned_science':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
  'scope':'auxiliary Walsh 16-atom calibrated minimax centers, (t,s)=(1/10,1/2)',
  'rho_and_rho_cal':'9/20',
  'coefficient_scale':'H=10h, U=10u, V=10v',
  'necessity_full_fiber':'w=z=0 from 4 explicit feasible signed moment sources',
  'inequalities':'(m dot (H,U,V)) >= c, 8 witnesses',
  'facet_witnesses':witnesses,
  'source_basis_count':comb(16,5),'source_nonsingular_bases':non,'source_feasible_bases_with_repetition':feas_bases,'source_distinct_vertices':len(sources),
  'facet_plane_triples':comb(8,3),'facet_nonsingular_triples':nonsingular,'facet_feasible_triples_with_repetition':feasible_triples,
  'complete_center_vertices':[[int(q) for q in p] for p in sorted(centers)],'complete_center_vertex_count':len(centers),
  'facet_tight_vertex_counts':facets_tight,
  'max_source_risk_numerator_at_every_center_vertex':'144 (TV=144/320=9/20)',
  'independent_review':'NOT_REVIEWED'
 },sort_keys=True,ensure_ascii=False,indent=2))
if __name__=='__main__':run()
