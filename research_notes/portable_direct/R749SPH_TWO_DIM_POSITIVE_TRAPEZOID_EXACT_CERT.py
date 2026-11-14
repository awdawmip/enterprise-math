#!/usr/bin/env python3
"""Exact 2D positive Walsh gap trapezoid: no sampling/no floats.
Scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389
T = {1/2<=s<=11/15; 0<=t-s<=1/30}.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from collections import Counter
import json
M=(3,12,15,1,2,4,8)
W=tuple(tuple(1 if ((k&m).bit_count()&1)==0 else -1 for m in M) for k in range(16))
def law(x): return tuple((1+sum((a*b for a,b in zip(x,row)),F(0)))/16 for row in W)
def tv(p,q): return sum((abs(x-y) for x,y in zip(p,q)),F(0))/2
def solve(rows,rhs,inds):
    n=7;a=[list(rows[i])+[rhs[i]] for i in inds];prev=1
    for j in range(n-1):
        pi=next((i for i in range(j,n) if a[i][j]),None)
        if pi is None:return None
        if pi!=j:a[pi],a[j]=a[j],a[pi]
        pivot=a[j][j]
        for i in range(j+1,n):
            m=a[i][j]
            for k in range(j+1,n+1):
                num=a[i][k]*pivot-m*a[j][k]
                if num%prev:raise ValueError('Nonexact Bareiss division')
                a[i][k]=num//prev
            a[i][j]=0
        prev=pivot
    if a[-1][n-1]==0:return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(a[j][n])-sum((a[j][i]*x[i] for i in range(j+1,n)),F(0)))/a[j][j]
    return tuple(x)
def qfree(t,s):
    A=(8*s-3)/5
    return law((F(1),A,A,0,0,0,0))
def qcal(t,s):
    return law((t,s,(t+17*s-7)/11,0,0,0,0))
def rf(t,s):return (8-5*t-3*s)/10
def rc(t,s):return (9-6*t-3*s)/11
def Pminus(t,s):return law((t,s,t+s-1,s-1,s-1,t-1,t-1))
def Pa(t,s):return law((t,s,1+s-t,s-t,s-t,0,0))
def events_check(t,s):
    EA=(7,11,13,14,15);EB=(0,3,5,6,9,10,12,15)
    Pm=Pminus(t,s); P_a=Pa(t,s)
    for p in (Pm,P_a):assert min(p)>=0 and sum(p)==1
    assert sum(Pm[k] for k in EA)==F(5,4)-(t+s)/2
    assert sum(P_a[k] for k in EB)==1+(s-t)/2
    h=(t+17*s-7)/11
    qc=qcal(t,s)
    assert sum(Pm[k]-qc[k] for k in EA)==(15-9*t-9*s+3*h)/16
    assert sum(P_a[k]-qc[k] for k in EB)==(1+s-t-h)/2
    assert (15-9*t-9*s+3*h)/16 == rc(t,s)
    assert (1+s-t-h)/2 == rc(t,s)
    assert rf(t,s)<=rc(t,s)
    return {'t':str(t),'s':str(s),'rho':str(rf(t,s)),'rho_cal':str(rc(t,s)), 'gap':str(rc(t,s)-rf(t,s))}
def check_pair_swap():
    perm=lambda k: ((k & 3)<<2)|((k & 12)>>2)
    for k in range(16):
        a=W[k];b=W[perm(k)]
        assert b==(a[1],a[0],a[2],a[5],a[6],a[3],a[4])
    return "PASS"
def run():
    assert check_pair_swap()=="PASS"
    # x=(t,s,h,u,v,w,z), constraints rows_i*x>=rhs_i.
    # 16 Walsh nonnegativity inequalities plus 4 trapezoid facets.
    # s >= 1/2, s <= 11/15, t-s >= 0, t-s <= 1/30.
    # Clear denominators 2,15,30 to keep integer Bareiss.
    rows=list(W)+[(0,2,0,0,0,0,0),(0,-15,0,0,0,0,0),
                  (1,-1,0,0,0,0,0),(-30,30,0,0,0,0,0)]
    rhs=[-1]*16+[1,-11,0,-1]
    verts=set();nonsingular=feasible=0
    for inds in combinations(range(20),7):
        x=solve(rows,rhs,inds)
        if x is None:continue
        nonsingular+=1
        if any(sum((a*b for a,b in zip(row,x)),F(0)) < b for row,b in zip(rows,rhs)):
            continue
        feasible+=1;verts.add(x)
    assert verts
    hist=Counter();tight_f=tight_c=0;maxef=maxec=None
    errors=[];min_gap=None
    for x in verts:
        t,s=x[:2]
        p=law(x);qf=qfree(t,s);qc=qcal(t,s)
        assert min(p)>=0 and sum(p)==1
        assert min(qf)>=0 and sum(qf)==1
        assert min(qc)>=0 and sum(qc)==1
        ef=tv(p,qf)-rf(t,s)
        ec=tv(p,qc)-rc(t,s)
        maxef=ef if maxef is None else max(maxef,ef)
        maxec=ec if maxec is None else max(maxec,ec)
        tight_f+=int(ef==0);tight_c+=int(ec==0)
        if ef>0 or ec>0:errors.append({'x':list(map(str,x)),'free_excess':str(ef),'cal_excess':str(ec)})
        hist[str((str(t),str(s)))]+=1
        min_gap=rc(t,s)-rf(t,s) if min_gap is None else min(min_gap,rc(t,s)-rf(t,s))
    corners=[(F(1,2),F(1,2)),(F(8,15),F(1,2)),(F(11,15),F(11,15)),(F(23,30),F(11,15))]
    lower=[events_check(t,s) for t,s in corners]
    assert min_gap>0 and maxef<=0 and maxec<=0 and not errors
    return {'schema':'R749SPH_WALSH_POSITIVE_GAP_TRAPEZOID_V1','status':'PASS',
     'frozen_science':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
     'region':'1/2<=s<=11/15 and 0<=t-s<=1/30, all real parameters',
     'region_area':'7/900', 'reflection_union_area':'7/450', 'bit_pair_swap_automorphism':check_pair_swap(),
     'free_radius':'(8-5*t-3*s)/10',
     'cal_radius':'(9-6*t-3*s)/11',
     'gap':'(2-5*t+3*s)/110 > 0',
     'exact_method':'integer Bareiss enumeration of all 7-facet active bases, rational feasible-vertex risk checks, convexity; explicit source/event lower certificates',
     'candidate_bases':comb(20,7),'nonsingular_bases':nonsingular,'feasible_bases_with_repeats':feasible,
     'distinct_vertices':len(verts),'tight_free_vertices':tight_f,'tight_cal_vertices':tight_c,
     'max_free_excess':str(maxef),'max_cal_excess':str(maxec),
     'min_gap_at_polytope_vertices':str(min_gap),
     'parameter_vertex_histogram':dict(sorted(hist.items())),
     'explicit_lower_certificates_at_four_corners':lower,
     'errors':errors[:5], 'review':'AUTHOR_EXACT_NOT_REVIEWED', 'native_mapping':'OPEN'}
if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
