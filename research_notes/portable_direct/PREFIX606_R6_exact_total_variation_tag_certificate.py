#!/usr/bin/env python3
"""PREFIX-606: exact TV distinguishability of all three native BRC slot tags.
All identities are within the original PREFIX565 phase graph and the prior
nonnegative 12-incidence weighted deformation; exact Fraction arithmetic.
"""
import io,json
from fractions import Fraction as F
from contextlib import redirect_stdout
from pathlib import Path
with redirect_stdout(io.StringIO()):
 import PREFIX605_R6_binary_tag_certificate as prev
from PREFIX565_positive_marginal_certificate import NEXT, PHASES
order=prev.order; pos=prev.pos; ei=prev.ei; pairs=prev.pairs
# The Laurent table of all 12 exact critical null generators has been checked by PREFIX605.
# Each unnormalised generator ell has 2 positive and 2 negative entries,
# each with absolute value x+1/2 where x=t_e>0; divide by that factor.
for e,f in pairs:
 w=[prev.A(prev.M(prev.NX,{0:F(prev.VW[e][i])}),prev.M(prev.H,{0:F(prev.VW[f][i])})) for i in range(24)]
 for offset in (0,24):
  types=[]
  for i,wi in enumerate(w):
   if not wi:continue
   p=order[offset+i];h=ei[(PHASES[p][0],abs(PHASES[p][2]))]
   assert h in (e,f)
   assert wi==(prev.H if h==e else prev.NX)
   types.append((i,h))
  assert sum(h==e for _,h in types)==2 and sum(h==f for _,h in types)==2
assert [len(prev.support[j]) for j in range(3)]==[48,24,24]
# Algebraic output of one normalized critical null generator h:
# tag0: four coefficients +/- (1,2*x)/(1+2*x) whose absolute sum is 2.
# tag1/tag2: two coefficients +/- (1,2*x)/(1+2*x) with abs sum 1.
# All supports (input and output, for fixed tag) are disjoint across generators.
# Thus for every null vector delta=sum c_a*h_a, exact l1 ratios are 1/2,1/4,1/4.
def check(t):
 P=[[F(0)]*48 for _ in range(48)]
 C=[[[F(0)]*48 for _ in range(48)] for _ in range(3)]
 for i,p in enumerate(order):
  e=ei[(PHASES[p][0],abs(PHASES[p][2]))]
  for j in range(3):
   q=pos[NEXT[p][j]];a=(F(1) if j==0 else t[e])/(1+2*t[e])
   P[i][q]+=a;C[j][i][q]+=a
 hlist=[]
 for e,f in pairs:
  if 4*t[e]*t[f]!=1:continue
  for off in (0,24):
   h=[F(0)]*48
   w=[prev.A(prev.M(prev.NX,{0:F(prev.VW[e][i])}),prev.M(prev.H,{0:F(prev.VW[f][i])})) for i in range(24)]
   for i,v in enumerate(w):
    if v:
     p=order[off+i];h[off+i]=F(1) if ei[(PHASES[p][0],abs(PHASES[p][2]))]==e else F(-1)
   assert sum(abs(v) for v in h)==4
   assert [sum(h[i]*P[i][q] for i in range(48)) for q in range(48)]==[0]*48
   hlist.append(h)
 for coeffs in ([1]*len(hlist), [i*(-1)**i for i in range(1,len(hlist)+1)]):
  d=[sum(c*h[i] for c,h in zip(coeffs,hlist)) for i in range(48)]
  if not hlist:continue
  norm=sum(abs(v) for v in d)
  assert norm>0
  assert [sum(d[i]*P[i][q] for i in range(48)) for q in range(48)]==[0]*48
  for j,ratio in enumerate((F(1,2),F(1,4),F(1,4))):
   out=[sum(d[i]*C[j][i][q] for i in range(48)) for q in range(48)]
   assert sum(abs(x) for x in out)==ratio*norm,(j,ratio)
   assert F(2)*sum(abs(x) for x in out)/norm==[F(1),F(1,2),F(1,2)][j]
 return len(hlist)
cases=[]
for x in (F(1,8),F(1,4),F(1,2),F(1),F(8)):
 t=[F(1)]*12
 for e,f in pairs:t[e]=x;t[f]=1/(4*x)
 cases.append({'critical_pairs':6,'x':str(x),'null_generators':check(t)})
assert len(cases)==5 and all(z['null_generators']==12 for z in cases)
result={'status':'ALL_CHECKS_PASS','frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
'exact_null_l1_tag_singleton_factors':{'slot0':'1/2','slot1':'1/4','slot2':'1/4'},
'exact_binary_tag_total_variation_retention':{'slot0':'1','slot1':'1/2','slot2':'1/2'},
'uniform_in':'all nonnegative finite 12-incidence weights, all nonzero left-null directions, any nine original roots',
'limit':'TV comparison holds on untagged P-nullspace; not a bound for all initial differences or finite-N reconstruction risk',
'validation':{'symbolic_support_and_normalization':'deduced from 36 exact Laurent identities of PREFIX605','rational_critical_cases':cases},
'status_scope':'AUTHOR_PROVED / EXACT_ALGEBRA_CHECKED / UNREVIEWED / NOT_ADMITTED'}
Path(__file__).with_name('PREFIX606_R6_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
