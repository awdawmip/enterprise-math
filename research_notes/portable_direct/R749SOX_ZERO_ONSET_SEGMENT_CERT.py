#!/usr/bin/env python3
"""R749SOX exact 6D Walsh onset zero-gap segment certificate.
Frozen: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389
No floating point acceptance. Python 3 standard library.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json

MASKS=(3,12,15,1,2,4,8)
W=[tuple(1 if (k&m).bit_count()%2==0 else -1 for m in MASKS) for k in range(16)]
SEGMENTS=(
    (F(1,2),F(11,20),'(4-10*s)/11'),
    (F(11,20),F(7,12),'45*(s-7/12)/11'),
    (F(7,12),F(5,7),'0'),
)

def t_of(s): return (1+3*s)/11

def h_of(s,mode):
    if mode==0:return (4-10*s)/11
    if mode==1:return 45*(s-F(7,12))/11
    return F(0)

def law(t,s,h=0,u=0,v=0,w=0,z=0):
    return tuple((1+sum((a*b for a,b in zip((t,s,h,u,v,w,z),row)),F(0)))/16 for row in W)

def tv(p,q):return sum((abs(a-b) for a,b in zip(p,q)),F(0))/2

def solve(rows,rhs,idx):
    n=6; a=[list(rows[i])+[rhs[i]] for i in idx]
    den=1
    for j in range(n-1):
        piv=next((i for i in range(j,n) if a[i][j]),None)
        if piv is None:return None
        if piv!=j:a[j],a[piv]=a[piv],a[j]
        pivot=a[j][j]
        for i in range(j+1,n):
            factor=a[i][j]
            for k in range(j+1,n+1):
                z=a[i][k]*pivot-factor*a[j][k]
                assert z%den==0
                a[i][k]=z//den
            a[i][j]=0
        den=pivot
    if a[-1][-2]==0:return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(a[j][n])-sum((a[j][k]*x[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(x)

def source_rows(lo,hi):
    rows=[];rhs=[]
    for a,b,c,d,e,f,g in W:
        rows.append((3*a+11*b,11*c,11*d,11*e,11*f,11*g))
        rhs.append(-(11+a))
    rows.extend([(lo.denominator,0,0,0,0,0),(-hi.denominator,0,0,0,0,0)])
    rhs.extend([lo.numerator,-hi.numerator])
    return rows,rhs

def lower_pair():
    signs=[]
    for s in (F(1,2),F(5,7)):
        t=t_of(s)
        a=law(t,s,0,t,t,1-t,s)
        b=law(t,s,0,-t,-t,t-1,-s)
        assert min(a)>=0 and min(b)>=0 and sum(a)==sum(b)==1
        assert tv(a,b)==(3-t+s)/4==2*(4+s)/11
        signs.append(tuple((x>y)-(x<y) for x,y in zip(a,b)))
    assert all(x*y>=0 for x,y in zip(*signs))
    return {'endpoint_signs_consistent':True,
      'lower_TV':'(3-t+s)/4 = 2*(4+s)/11',
      'source_pair':'p(t,s,0,+/-t,+/-t,+/-(1-t),+/-s)'}

def certificate(lo,hi,mode):
    rows,rhs=source_rows(lo,hi)
    seen=set();nonsing=feasible=0
    for idx in combinations(range(18),6):
        y=solve(rows,rhs,idx)
        if y is None:continue
        nonsing+=1
        if any(sum((a*b for a,b in zip(row,y)),F(0))<bound for row,bound in zip(rows,rhs)):
            continue
        feasible+=1;seen.add(y)
    assert seen
    max_excess=F(-1);tight=0;endpoints={}
    for s,h,u,v,w,z in seen:
        t=t_of(s);p=law(t,s,h,u,v,w,z);q=law(t,s,h_of(s,mode))
        assert min(p)>=0 and sum(p)==1
        assert min(q)>=0 and sum(q)==1
        excess=tv(p,q)-(4+s)/11
        assert excess<=0,(str(s),str(h),str(excess))
        if excess==0:tight+=1
        max_excess=max(max_excess,excess)
        endpoints[str(s)]=endpoints.get(str(s),0)+1
    assert max_excess==0
    return {'s_interval':[str(lo),str(hi)],'h':SEGMENTS[mode][2],
      'active_six_facet_combinations':comb(18,6),
      'nonsingular_bases':nonsing,'feasible_bases_including_duplicates':feasible,
      'distinct_exact_vertices':len(seen),'parameter_endpoints':endpoints,
      'tight_vertices':tight,'max_upper_excess':str(max_excess)}

def main():
    low=lower_pair()
    segments=[certificate(lo,hi,i) for i,(lo,hi,_) in enumerate(SEGMENTS)]
    return {'status':'PASS','id':'R749SOX',
      'frozen_science':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'model':'auxiliary_16_atom_Walsh_fiber',
      'domain':'s in [1/2,5/7], t=(1+3*s)/11',
      'exact_minimax':'rho=rho_cal=(4+s)/11; calibration_gap=0',
      'proof':'lower source diameter + complete 6D exact vertex upper + convexity',
      'calibrated_center_segments':segments,'lower':low,
      'all_real_s':'from affine source/center/radius, polytope vertex convexity',
      'review':'AUTHOR_EXACT_NOT_REVIEWED','native_correspondence':'OPEN'}
if __name__=='__main__':print(json.dumps(main(),sort_keys=True,indent=2))
