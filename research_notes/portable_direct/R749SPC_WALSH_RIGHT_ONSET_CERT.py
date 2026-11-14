#!/usr/bin/env python3
"""R749SPC: exact 16-atom Walsh s=3/5 first post-zero-gap interval.
Frozen scientific input: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Pure Python 3 standard library, exact integer Bareiss + Fraction.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json

MASKS=(3,12,15,1,2,4,8)
W=tuple(tuple(1 if ((k&m).bit_count() & 1)==0 else -1 for m in MASKS) for k in range(16))
S=F(3,5); L=F(2,5); U=F(1,2)
E1=(7,11,12,13,14,15)
E2=(0,3,5,6,9,10,12,15)

def law(t,s,h=F(0),u=F(0),v=F(0),w=F(0),z=F(0)):
    c=(t,s,h,u,v,w,z)
    return tuple((1+sum((a*b for a,b in zip(c,row)),F(0)))/16 for row in W)

def tv(p,q):
    return sum((abs(x-y) for x,y in zip(p,q)),F(0))/2

def source_pair(t):
    h=t-L
    return (law(t,S,h,F(2,5),F(2,5),1-t,1-t),
            law(t,S,h,-F(2,5),-F(2,5),t-1,t-1))

def source_two(t):
    return law(t,S,t+L,F(0),F(0),t-S,t-S)

def free_center(t):
    d=2*t-2*L
    return law(d,1,d)

def calibrated_center(t):
    return law(t,S,F(9,5)*(t-L))

def free_radius(t):return S-t/2
def calibrated_radius(t):return F(14,25)-F(2,5)*t

def solve_bareiss(rows,rhs,idx):
    n=6
    a=[list(rows[i])+[rhs[i]] for i in idx]
    prev=1
    for j in range(n-1):
        piv=next((i for i in range(j,n) if a[i][j]!=0),None)
        if piv is None:return None
        if piv!=j:a[j],a[piv]=a[piv],a[j]
        pivot=a[j][j]
        for i in range(j+1,n):
            factor=a[i][j]
            for k in range(j+1,n+1):
                numerator=a[i][k]*pivot-factor*a[j][k]
                assert numerator%prev==0
                a[i][k]=numerator//prev
            a[i][j]=0
        prev=pivot
    if a[n-1][n-1]==0:return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(a[j][n])-sum((a[j][i]*x[i] for i in range(j+1,n)),F(0)))/a[j][j]
    return tuple(x)

def lower_witness():
    endpoint=[]
    signs=[]
    for t in (L,U):
        p,q=source_pair(t)
        v=source_two(t)
        for x in (p,q,v,free_center(t),calibrated_center(t)):
            assert min(x)>=0 and sum(x)==1
        assert tv(p,q)==2*free_radius(t)
        signs.append(tuple((a>b)-(a<b) for a,b in zip(p,q)))
        hc=F(9,5)*(t-L)
        assert sum((q[k]-calibrated_center(t)[k] for k in E1),F(0))==F(13,20)-F(5,8)*t+hc/8
        assert sum((v[k]-calibrated_center(t)[k] for k in E2),F(0))==F(1,5)+t/2-hc/2
        assert tv(q,calibrated_center(t))==calibrated_radius(t)
        assert tv(v,calibrated_center(t))==calibrated_radius(t)
        endpoint.append({'t':str(t),'source_pair_TV':str(tv(p,q)),
                         'free_radius':str(free_radius(t)),
                         'cal_radius':str(calibrated_radius(t)),
                         'free_q_min_atom':str(min(free_center(t))),
                         'cal_q_min_atom':str(min(calibrated_center(t)))})
    assert all(a*b>=0 for a,b in zip(signs[0],signs[1]))
    # Check affine event identities at four (t,h) corners.
    for t in (L,U):
        negative_source=source_pair(t)[1]
        other_source=source_two(t)
        for h in (F(-1),F(1)):
            qh=law(t,S,h)  # purely algebraic Walsh array, may not be positive here
            lhs1=sum((negative_source[k]-qh[k] for k in E1),F(0))
            lhs2=sum((other_source[k]-qh[k] for k in E2),F(0))
            assert lhs1==F(13,20)-F(5,8)*t+h/8
            assert lhs2==F(1,5)+t/2-h/2
    # Two event bounds have opposite slopes in h and meet at h*=9/5(t-2/5).
    for t in (L,U):
        h=F(9,5)*(t-L)
        c1=F(13,20)-F(5,8)*t+h/8
        c2=F(1,5)+t/2-h/2
        assert c1==c2==calibrated_radius(t)
    return {'endpoint_checks':endpoint,'pair_sign_consistency':True,
            'free_pair_TV_all_t':'6/5-t',
            'cal_event_1':{'source':'p(t,3/5,t-2/5,-2/5,-2/5,t-1,t-1)',
                           'positive_event_indices':list(E1),
                           'bound':'13/20-5*t/8+h/8'},
            'cal_event_2':{'source':'p(t,3/5,t+2/5,0,0,t-3/5,t-3/5)',
                           'positive_event_indices':list(E2),
                           'bound':'1/5+t/2-h/2'},
            'cal_lower_intersection_h':'9/5*(t-2/5)',
            'cal_lower_radius':'14/25-2*t/5'}

def exact_upper():
    # six variables (t,h,u,v,w,z). Inequalities A*x>=b.
    rows=[];rhs=[]
    for r in W:
        rows.append(tuple(5*r[i] for i in (0,2,3,4,5,6)))
        rhs.append(-5-3*r[1])
    rows.append((5,0,0,0,0,0));rhs.append(2)
    rows.append((-2,0,0,0,0,0));rhs.append(-1)
    assert len(rows)==18
    distinct=set();nonsingular=feasible=0
    for idx in combinations(range(18),6):
        x=solve_bareiss(rows,rhs,idx)
        if x is None:continue
        nonsingular+=1
        if any(sum((a*b for a,b in zip(row,x)),F(0))<v for row,v in zip(rows,rhs)):
            continue
        feasible+=1;distinct.add(x)
    assert distinct
    worst_free=None;worst_cal=None;tight_free=tight_cal=0
    t_hist={}
    for x in distinct:
        t,h,u,v,w,z=x
        p=law(t,S,h,u,v,w,z)
        qf=free_center(t);qc=calibrated_center(t)
        assert min(p)>=0 and sum(p)==1
        assert min(qf)>=0 and sum(qf)==1
        assert min(qc)>=0 and sum(qc)==1
        ef=tv(p,qf)-free_radius(t)
        ec=tv(p,qc)-calibrated_radius(t)
        worst_free=ef if worst_free is None or ef>worst_free else worst_free
        worst_cal=ec if worst_cal is None or ec>worst_cal else worst_cal
        if ef==0:tight_free+=1
        if ec==0:tight_cal+=1
        assert ef<=0,('FREE_RISK_VIOLATION',tuple(map(str,x)),str(ef))
        assert ec<=0,('CAL_RISK_VIOLATION',tuple(map(str,x)),str(ec))
        t_hist[str(t)]=t_hist.get(str(t),0)+1
    assert worst_free==worst_cal==0
    return {'dimension':6,'facet_count':18,'active_basis_combinations':comb(18,6),
            'nonsingular_bases':nonsingular,'feasible_bases_with_multiplicity':feasible,
            'distinct_exact_vertices':len(distinct),
            'vertex_t_values':dict(sorted(t_hist.items())),
            'free_tight_vertices':tight_free,'cal_tight_vertices':tight_cal,
            'max_free_risk_excess':str(worst_free),'max_cal_risk_excess':str(worst_cal)}

def main():
    return {'status':'PASS','research_id':'R749SPC',
            'frozen_science':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
            'model':'Complete compatible 16-atom Walsh source; s=3/5, real t in [2/5,1/2]',
            'free_radius':'3/5-t/2', 'calibrated_radius':'14/25-2*t/5',
            'gap':'(t-2/5)/10',
            'free_center':'p(2*t-4/5,1,2*t-4/5,0,0,0,0)',
            'cal_center':'p(t,3/5,9/5*(t-2/5),0,0,0,0)',
            'lower':lower_witness(),'upper':exact_upper(),
            'coverage':'exact full joint polytope vertex enumeration plus convexity for all real t',
            'review':'AUTHOR_EXACT_NOT_REVIEWED',
            'native_X6_transfer':'OPEN'}
if __name__=='__main__':print(json.dumps(main(),ensure_ascii=False,sort_keys=True,indent=2))
