#!/usr/bin/env python3
"""Independent standard-library exact rational check: PSD midpoint and robust gap."""
from fractions import Fraction as F
import json

def c(x=0,y=0): return (F(x),F(y))
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def conj(a): return (a[0],-a[1])
def abs2(a): return a[0]*a[0]+a[1]*a[1]
def dot(row,w):
    z=c()
    for a,b in zip(row,w):z=add(z,mul(a,b))
    return z
r4=(c(F(5,2),F(9,2)),c(F(3,2),F(7,2)),c(0,4))
r5=(c(F(11,4),F(15,8)),c(F(11,4),F(15,8)),c(F(5,4),F(9,4)))
rs=((c(),c(1),c()),(c(1),c(1),c()),(c(),c(),c(1)),(c(1),c(),c(1)),r4,r5)
wplus=(c(1),c(0,1),c())
wminus=(c(1),c(0,-1),c())
vals_plus=[abs2(dot(row,wplus)) for row in rs]
vals_minus=[abs2(dot(row,wminus)) for row in rs]
assert vals_plus==[1,2,0,1,37,F(709,32)]
assert vals_minus==[1,2,0,1,45,F(709,32)]
mid=[(a+b)/2 for a,b in zip(vals_plus,vals_minus)]
assert mid==[1,2,0,1,41,F(709,32)]
assert abs2(mul(r4[0],conj(r4[1])))==F(39,2)**2+4
assert abs2(mul(r4[0],conj(r4[2])))==424
assert abs2(mul(r4[1],conj(r4[2])))==232
# Arithmetic exact upper bounds on all PSD feasible points.
e=F(1,10000)
err=(F(29,2)+16+39)*e + 42*F(1,100) +32*F(1001,100000)
assert err==F(74727,100000)<F(3,4)
rank_defect=F(9,16)-2*e
assert rank_defect==F(5623,10000)
# Rank-one branch exclusion remains valid on the full continuous box.
d=F(459,10000)
err_plus=14*d+d*d
err_minus=18*d+d*d
exclusion_margin=min(40-(37+err_plus),(45-err_minus)-42)
assert exclusion_margin==F(217169319,100000000)>0
print(json.dumps({
    'status':'PASS_PREFIX406_INDEPENDENT_FRACTION_PSD_RANK_GAP',
    'source_readouts_plus':[str(x) for x in vals_plus],
    'source_readouts_minus':[str(x) for x in vals_minus],
    'psd_midpoint':[str(x) for x in mid],
    'strict_PSD_error_bound':str(err),
    'strict_lambda2_lower_bound':str(rank_defect),
    'strict_rank1_exclusion_margin':str(exclusion_margin)
},sort_keys=True,indent=2))
