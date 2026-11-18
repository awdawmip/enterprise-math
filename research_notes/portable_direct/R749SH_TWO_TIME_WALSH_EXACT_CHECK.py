#!/usr/bin/env python3
"""Exact two-time Walsh identity, source-memory repair witness for R749SH."""
from fractions import Fraction as F
from itertools import product
import json

bits=list(product((-1,1),repeat=3))
# Initial axes are 0,1,2; nonforced C={2,3}: old 0 erased,
# 1 and 2 copied, new 3 fresh fair. x=(x0,x1,x2), y=(x1,x2,x3).
def kernel(x): return {(x[1],x[2],fresh):F(1,2) for fresh in (-1,1)}

plus={x:(F(1,4) if x[0]==x[1] else F(0)) for x in bits}
minus={x:(F(1,4) if x[0]==-x[1] else F(0)) for x in bits}
assert sum(plus.values())==sum(minus.values())==1

def current(mu):
 out={y:F(0) for y in bits}
 for x,w in mu.items():
  for y,p in kernel(x).items():out[y]+=w*p
 return out

U={y:F(1,8) for y in bits}
assert current(plus)==current(minus)==U

def cross(mu):
 return sum(w*x[0]*sum(p*y[0] for y,p in kernel(x).items()) for x,w in mu.items())
assert cross(plus)==1 and cross(minus)==-1

checks=0
for x in bits:
 for maskT in range(8):
  valT=__import__('math').prod(x[i] for i in range(3) if (maskT>>i)&1)
  for maskS in range(8):
   lhs=sum(p*valT*__import__('math').prod(y[i] for i in range(3) if (maskS>>i)&1) for y,p in kernel(x).items())
   if maskS & 4:rhs=0
   else:
    rhs=valT*__import__('math').prod(x[i+1] for i in range(2) if (maskS>>i)&1)
   assert lhs==rhs,(x,maskT,maskS,lhs,rhs)
   checks+=1
print(json.dumps({'status':'PASS','conditional_source_rows':8,'joint_Walsh_row_identities':checks,
 'p_range':'0<=p<1: nonforced conditional reset is uniform',
 'identical_current_final_distributions':True,
 'final_current_probability_each_of_eight':'1/8',
 'historic_current_cross_moment_plus':'+1',
 'historic_current_cross_moment_minus':'-1',
 'repair_coordinate':'E[sigma_0(initial)*sigma_1(current)]',
 'native_event_permission':False},indent=2,sort_keys=True))
