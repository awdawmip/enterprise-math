#!/usr/bin/env python3
"""Exact finite external non-IID two-measure LR-minimal obstruction certificate."""
from fractions import Fraction as F
import json

ONE=F(1)
initial={'a':{'P':F(1,2),'Q':F(1,2)},'b':{'P':F(1,2),'Q':F(1,2)}}
cond={
'a':{'P':{'x':F(3,4),'y':F(1,4)},'Q':{'x':F(1,4),'y':F(3,4)}},
'b':{'P':{'x':F(1,2),'y':F(1,2)},'Q':{'x':F(1,2),'y':F(1,2)}},
}
assert all(sum(initial[h][z] for h in initial)==1 for z in ('P','Q'))
assert all(sum(cond[h][z].values())==1 for h in cond for z in ('P','Q'))
assert all(v>0 for h in cond for z in ('P','Q') for v in cond[h][z].values())
leaf={(h,y):{z:initial[h][z]*cond[h][z][y] for z in ('P','Q')}
      for h in cond for y in ('x','y')}
lr1={h:initial[h]['P']/initial[h]['Q'] for h in initial}
lr2={(h,y):v['P']/v['Q'] for (h,y),v in leaf.items()}
assert lr1=={'a':ONE,'b':ONE}
assert lr2=={('a','x'):F(3),('a','y'):F(1,3),('b','x'):ONE,('b','y'):ONE}
assert cond['a']['P']['x']==F(3,4)
assert sum(cond['b']['P'][y] for y in ('x','y') if lr2[('b',y)]==F(3))==0
eP=initial['b']['P']+leaf[('a','y')]['P']
eQ=leaf[('a','x')]['Q']
EP=ONE+initial['a']['P']
EQ=ONE+initial['a']['Q']
assert (eP,eQ,EP,EQ)==(F(5,8),F(1,8),F(3,2),F(3,2))
overlap={h:sum(min(cond[h]['P'][y],cond[h]['Q'][y]) for y in ('x','y')) for h in cond}
assert overlap=={'a':F(1,2),'b':ONE}
mean_overlap=sum(initial[h]['Q']*overlap[h] for h in initial)
assert mean_overlap==F(3,4)
# Root stopping allowed: s(1+p)=3/2, 0<=s,p<=1 => c=sp<=3/4.
cmax=F(3,4)
lower=ONE-cmax*(ONE-mean_overlap)
assert lower==F(13,16) and eP+eQ==F(3,4)
assert lower-(eP+eQ)==F(1,16)
gamma=F(1,4)
assert eP+eQ+gamma*EQ==F(9,8)
assert F(5,4)-(eP+eQ+gamma*EQ)==F(1,8)
print(json.dumps({
'model':'external strictly positive non-IID N=2 tree',
'T1_LR':{'a':'1','b':'1'},
'T2_LR':{'ax':'3','ay':'1/3','bx':'1','by':'1'},
'four_observables':['5/8','1/8','3/2','3/2'],
'max_continued_mass_c':'3/4',
'T_only_error_sum_lower_bound':'13/16',
'history_error_sum':'3/4',
'exact_gap':'1/16',
'forced_root_J_gap':'1/8',
'status':'ALL_EXACT_ASSERTIONS_PASS'
},indent=2))
