#!/usr/bin/env python3
"""Exact fixed simplicial 96-port cone common invariant for all nonnegative X6 axis/gate weights."""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
import runpy,json
src=runpy.run_path(str(Path(__file__).with_name('PREFIX587_R2_combinatorial_inverse_simplicial_cone.py')))
P,N,G=src['P'],src['NEXT'],src['G']
TARGET=P.index((0,1,-3))
BLOCKS=[[2*i+u for i in I] for c,I in G.items() for u in (0,1)]
assert len(BLOCKS)==24 and len({i for b in BLOCKS for i in b})==96
BID={i:bid for bid,grp in enumerate(BLOCKS) for i in grp}
def AW(x,z):
 q=[[0]*96 for _ in range(96)]
 for i,nxt in enumerate(N):
  axis=abs(P[i][2])-1
  for j in nxt:
   for u in (0,1):
    for v in (0,1):
     a=x[axis]*(z if j==TARGET and u==v==1 else 1)
     if not a:continue
     row=q[2*i+u]
     jv=2*j+v
     for k in BLOCKS[BID[jv]]:
      if k!=jv:row[k]+=a
 return q
def conjugated(x,z):
 q=AW(x,z)
 t=[[F(0)]*96 for _ in range(96)]
 for group in BLOCKS:
  sums=[sum(q[k][j] for k in group) for j in range(96)]
  for i in group:
   t[i]=[F(s,3)-q[i][j] for j,s in enumerate(sums)]
 return t
coef=[]
for a in range(6):
 x=[0]*6;x[a]=1
 coef.append(conjugated(x,0))
x=[1,0,0,0,0,0]
g0=conjugated(x,0);g1=conjugated(x,1)
coef.append([[g1[i][j]-g0[i][j] for j in range(96)] for i in range(96)])
summary=[]
for k,m in enumerate(coef):
 vals=Counter(v for row in m for v in row)
 assert min(vals)>=0,(k,min(vals))
 summary.append({'coefficient':('axis_'+str(k+1) if k<6 else 'axis_1_x_gate_z'),
                  'nonzero':sum(v!=0 for row in m for v in row),
                  'value_histogram':{str(v):c for v,c in vals.items() if c},
                  'all_nonnegative':True,'all_integer':all(v.denominator==1 for row in m for v in row)})
assert all(t['all_integer'] for t in summary)
unweighted=[[sum(coef[a][i][j] for a in range(7)) for j in range(96)] for i in range(96)]
assert all(v in (0,1) for row in unweighted for v in row)
assert sum(v for row in unweighted for v in row)==576
assert all(sum(row)==6 for row in unweighted)
assert all(sum(unweighted[i][j] for i in range(96))==6 for j in range(96))
for x,z in [((1,)*6,0),((1,)*6,1),((1,)*6,7),((2,3,5,7,11,13),17),((0,0,0,0,0,0),999),((0,1,0,0,0,0),2)]:
 actual=conjugated(x,z)
 expected=[[sum(x[a]*coef[a][i][j] for a in range(6))+x[0]*z*coef[6][i][j] for j in range(96)] for i in range(96)]
 assert actual==expected
 assert all(v>=0 for row in actual for v in row)
results={'schema':'PREFIX588_R2_COMMON_NATIVE_BRC_INVARIANT_96_RAY_CONE_V1',
         'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
         'fixed_cone':'W=direct sum over 12 signed axes and 2 branch bits of (J4-I4)',
         'inverse':'W^-1=direct sum of (J4/3-I4)',
         'all_weights':'x_a>=0, z>=0',
         'exact_identity':'W^-1 A(x,z) W = sum_{a=1}^6 x_a C_a + x_1*z C_gate, all 7 C have nonnegative integer entries',
         'all_96_square_entries_each_coefficient_checked':7*96*96,
         'coefficients':summary,
         'unweighted_conjugate_adjacency':'96 x 96 zero-one 6-in/6-out with exactly 576 ones; seven supports disjoint',
         'positive_weight_regression_cases':6,
         'conclusion':'The identical 96-ray simplicial cone is invariant under all nonnegative native 96-port BRC transition matrices and their arbitrary products',
         'status':'ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED'}
Path(__file__).with_name('PREFIX588_R2_common_invariant_cone_results.json').write_text(json.dumps(results,indent=2)+'\n')
print(results['status'])
for row in summary: print(row)
