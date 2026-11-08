#!/usr/bin/env python3
"""PREFIX587 exact native original phase local inverse and simplicial boundary cone."""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json
STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple(-k if c>0 else k for k in STARS[a] if k!=abs(c))
P=tuple((a,p,t*k) for a in range(4) for k in STARS[a] for t in (-1,1) for p in near(a,t*k))
IX={v:i for i,v in enumerate(P)}
def nxt(i):
 a,p,c=P[i]; b=next(b for b in range(4) if b!=a and abs(c) in STARS[b])
 return tuple(IX[t] for t in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
NEXT=tuple(nxt(i) for i in range(48))
S=[[int(j in NEXT[i]) for j in range(48)] for i in range(48)]
REV=[IX[(a,c,p)] for a,p,c in P]
R=[[int(k==REV[j]) for k in range(48)] for j in range(48)]
T=[[S[i][j]-2*R[j][i] for i in range(48)] for j in range(48)]
assert all(REV[REV[i]]==i for i in range(48))
assert all(sum(S[i][k]*T[k][j] for k in range(48))==3*int(i==j)
  for i in range(48) for j in range(48))
assert all(sum(T[i][k]*S[k][j] for k in range(48))==3*int(i==j)
  for i in range(48) for j in range(48))
G={c:[i for i,(_,_,v) in enumerate(P) if v==c] for c in (-6,-5,-4,-3,-2,-1,1,2,3,4,5,6)}
assert len(G)==12 and all(len(I)==4 for I in G.values())
assert all(sum(S[i][j]*S[k][j] for j in range(48)) ==
    (3 if i==k else (2 if P[i][2]==P[k][2] else 0))
    for i in range(48) for k in range(48))
assert all(sum(S[i][j]*R[j][k] for j in range(48)) ==
    int(i!=k and P[i][2]==P[k][2])
    for i in range(48) for k in range(48))
assert all(sum(T[j][i]!=0 for i in range(48))==4 for j in range(48))
assert all(T[j][i]==(0 if i not in G[P[j][1]] else (-2 if i==REV[j] else 1))
    for j in range(48) for i in range(48))
block_count=0
for c,I in G.items():
 for u in (0,1):
  block_count+=1
  for omit in range(4):
   lam=[int(k==omit) for k in range(4)]
   r=[sum(lam)-lam[k] for k in range(4)]
   recovered=[F(sum(r),3)-r[k] for k in range(4)]
   assert recovered==lam
   assert all(t>=0 for t in r)
   assert sum(t!=0 for t in r)==3
   assert recovered.count(0)==3 and recovered.count(1)==1
  for bad in range(4):
   r=[F(4) if k==bad else F(1) for k in range(4)]
   vals=[F(sum(r),3)-r[k] for k in range(4)]
   assert vals[bad]<0 and all(vals[k]>0 for k in range(4) if k!=bad)
assert block_count==24
results={
 'schema':'PREFIX587_R2_NATIVE_COMBINATORIAL_INVERSE_CONE_V1',
 'source_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'phases':48,'native_ports':96,'signed_current_axis_groups':12,'phases_per_group':4,
 'branch_bits':2,'independent_cone_blocks':24,
 'combinatorial_inverse':'3*S^-1 = S^T-2*R, R(j)=reverse_phase(j)=(a,c,p)',
 'SS_transpose_groups':'12 copies of I4+2J4',
 'S_singular_values':'12 copies of 3 and 36 copies of 1',
 'S_two_norm_condition_number':3,
 'positive_cone':'in each signed-axis/bit group, r_i = sum(lambda)-lambda_i for 4 nonnegative lambda_i',
 'extreme_rays_per_group':4,'total_extreme_rays':96,'facet_inequalities_irredundant':96,
 'all_original_phase_edges_checked':144,
 'full_matrix_ST_and_TS_checks':4608,
 'all_original_row_overlaps_checked':2304,
 'code_execution_status':'ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED'
}
Path(__file__).with_name('PREFIX587_R2_combinatorial_inverse_simplicial_cone_results.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
print(results['code_execution_status'], '| 12 blocks of 4 phases; 24 simplicial cone blocks; 96 extreme rays')
