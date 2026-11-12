"""Exact row rank of all gated signed output probabilities, 120 supports x 3 p."""
from fractions import Fraction as F
from itertools import combinations,product
import json
SIGNS=list(product((-1,1), repeat=3))
def rank(matrix):
 a=[list(map(F,row)) for row in matrix]
 m=len(a);n=len(a[0]);r=0
 for j in range(n):
  k=next((k for k in range(r,m) if a[k][j]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r]
  pivot=a[r][j];a[r]=[x/pivot for x in a[r]]
  for k in range(m):
   if k!=r and a[k][j]:
    u=a[k][j];a[k]=[x-u*y for x,y in zip(a[k],a[r])]
  r+=1
  if r==m:break
 return r
count=0
for A in combinations(range(6),2):
 for B in combinations(range(6),2):
  A,B=set(A),set(B)
  if len(A&B)!=1:continue
  i=next(iter(A-B));j=next(iter(A&B));k=next(iter(B-A))
  assert len({i,j,k})==3
  for p in [F(0),F(1,2),F(1)]:
   theta=8*p/(1+7*p)
   out=[]
   for yi,yj,yk in SIGNS:
    gate=F(2+yi+yj,4)
    if gate==0:continue
    row=[]
    for si,sj,sk in SIGNS:
     row.append(gate*F(1+theta*si*yi,2) if (yj,yk)==(sj,sk) else F(0))
    out.append(row)
   assert len(out)==6
   # Differential of unnormalized output probabilities on 8-prior simplex.
   tangent=[[row[t]-row[7] for t in range(7)] for row in out]
   assert rank(tangent)==(3 if p==0 else 6), (A,B,p)
   # Every allowed final mass is a genuine nonconstant rational posterior query.
   row_sum=[sum(row[t] for row in out) for t in range(8)]
   assert all(x>0 for x in out[0]) is False
   for row in out:
    assert any(row[t]*row_sum[u]!=row[u]*row_sum[t] for t in range(8) for u in range(8))
   # Uniform full-support prior defines a strictly positive gate normalization.
   Z=sum(row_sum)/8
   assert Z>0
   assert sum((sum(row)/8)/Z for row in out)==1
   count+=1
assert count==360
print(json.dumps({"status":"PASS","directed_supports":120,"parameters":["0","1/2","1"],"rank_checks":count,"nonzero_gated_final_states":6,"minimum_affine_initial_coordinates":{"p=0":3,"p>0":6},"native_event_permission":False},sort_keys=True))
