#!/usr/bin/env python3
"""PREFIX578-R6 exact 56 third cumulants; frozen science pin f42f2906d77f24085c123f3ccfe9667d41caa96d."""
import json
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations_with_replacement as combs
from PREFIX565_positive_marginal_certificate import edge,ACTIONS,ZERO_ROOT,SCIENCE_PIN
N=96; B=6
assert SCIENCE_PIN=='f42f2906d77f24085c123f3ccfe9667d41caa96d'
E=[[edge(i,a,ZERO_ROOT) for a in ACTIONS] for i in range(N)]
assert Counter(j for row in E for j,w in row)==Counter({i:6 for i in range(N)})
assert all(sum(w[:6])==1 and all(v in (0,1) for v in w) for row in E for j,w in row)
R=[[(j,(w[0],w[1],w[2],w[3],w[4],w[6])) for j,w in row] for row in E]
P=[[Q(0) for _ in range(N)] for _ in range(N)]
for i,row in enumerate(R):
 for j,w in row:P[i][j]+=Q(1,6)
assert all(sum(row)==1 for row in P)
ONE=[Q(1)]*N

def op(keys,v):
 return [sum((v[j] for j,w in row if all(w[k] for k in keys)),Q(0))/6 for row in R]
def avg(v):return sum(v)/N
def plus(*vs):return [sum(a,Q(0)) for a in zip(*vs)]
def solve(cols):
 t=len(cols)
 A=[[Q(int(i==j))-P[i][j] for j in range(1,N)]+[cols[k][i] for k in range(t)] for i in range(1,N)]
 for j in range(N-1):
  h=next(i for i in range(j,N-1) if A[i][j]);A[h],A[j]=A[j],A[h]
  d=A[j][j];A[j]=[x/d for x in A[j]]
  for i in range(N-1):
   if i!=j and A[i][j]:
    z=A[i][j];A[i]=[x-z*y for x,y in zip(A[i],A[j])]
 out=[]
 for k in range(t):
  v=[Q(0)]+[A[i][N-1+k] for i in range(N-1)];z=avg(v);v=[x-z for x in v]
  assert sum(v)==0 and all(sum((Q(int(i==j))-P[i][j])*v[j] for j in range(N))==cols[k][i] for i in range(N))
  out.append(v)
 return out

m={a:avg(op((a,),ONE)) for a in range(B)}
assert [m[a] for a in range(B)]==[Q(1,6)]*5+[Q(1,192)]
v1=dict(enumerate(solve([[x-m[a] for x in op((a,),ONE)] for a in range(B)])))
pairs=list(combs(range(B),2));l2={};rhs=[]
for a,b in pairs:
 raw=plus(op((a,b),ONE),op((a,),v1[b]),op((b,),v1[a]))
 l2[a,b]=avg(raw)
 rhs.append([raw[i]-m[a]*v1[b][i]-m[b]*v1[a][i]-l2[a,b] for i in range(N)])
v2=dict(zip(pairs,solve(rhs)))
def pair(dic,a,b):return dic[tuple(sorted((a,b)))]
cov={(a,b):l2[a,b]-m[a]*m[b] for a,b in pairs}
expected=[[Q(11,216),Q(-7,216),Q(-1,216),Q(-1,216),Q(-1,216),Q(11,6912)],
[Q(-7,216),Q(11,216),Q(-1,216),Q(-1,216),Q(-1,216),Q(-7,6912)],
[Q(-1,216),Q(-1,216),Q(11,216),Q(-7,216),Q(-1,216),Q(11,6912)],
[Q(-1,216),Q(-1,216),Q(-7,216),Q(11,216),Q(-1,216),Q(-7,6912)],
[Q(-1,216),Q(-1,216),Q(-1,216),Q(-1,216),Q(11,216),Q(-1,1728)],
[Q(11,6912),Q(-7,6912),Q(11,6912),Q(-7,6912),Q(-1,1728),Q(1127,221184)]]
assert all(pair(cov,i,j)==expected[i][j] for i in range(B) for j in range(B))
c3={}
for a,b,c in combs(range(B),3):
 raw=plus(op((a,b,c),ONE),op((a,b),v1[c]),op((a,c),v1[b]),op((b,c),v1[a]),
          op((a,),pair(v2,b,c)),op((b,),pair(v2,a,c)),op((c,),pair(v2,a,b)))
 L=avg(raw)
 c3[a,b,c]=L-pair(l2,a,b)*m[c]-pair(l2,a,c)*m[b]-pair(l2,b,c)*m[a]+2*m[a]*m[b]*m[c]
assert len(c3)==56
# Full tensor indices 0..5=R1..R6, 6=gate; replace R6 by minus sum R1..R5.
def expansion(k):return [(i,Q(-1)) for i in range(5)] if k==5 else [(k,Q(1))] if k<5 else [(5,Q(1))]
def full(a,b,c):
 return sum((x*y*z*c3[tuple(sorted((i,j,k)))] for i,x in expansion(a) for j,y in expansion(b) for k,z in expansion(c)),Q(0))
assert all(sum(full(a,b,c) for a in range(6))==0 for b in range(7) for c in range(7))
names=('R1','R2','R3','R4','R5','K')
print(json.dumps({'status':'ALL_CHECKS_PASS','science_pin':SCIENCE_PIN,
 'reduced_axis_order':names,'finite_states':N,'primitive_labeled_edges':576,
 'poisson_rhs_solved':27,'second_order_prior_covariance_check':21,
 'independent_third_entries':56,'full_seven_dimensional_entries':84,
 'independent_tensor':{','.join(names[i] for i in ijk):str(v) for ijk,v in c3.items()},
 'full_tensor':{','.join(('R1','R2','R3','R4','R5','R6','K')[i] for i in t):str(full(*t)) for t in combs(range(7),3)}},indent=2))
