#!/usr/bin/env python3
"""R749SPH: exact complementary upper-wedge Walsh center-risk certificate.

Frozen scientific setup: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Checks continuous real-parameter triangle W0 via complete 7D rational-polytope
vertex enumeration. The companion R749SPG certificate covers the complementary
triangle W1. Python 3 standard library only.
"""
import json
from fractions import Fraction as F
from itertools import combinations
from math import comb
M=(3,12,15,1,2,4,8)
W=tuple(tuple(1 if ((k&m).bit_count()%2)==0 else -1 for m in M) for k in range(16))

def law(t,s,h=0,u=0,v=0,w=0,z=0):
    return tuple((1+sum((a*b for a,b in zip((t,s,h,u,v,w,z),row)),F(0)))/16 for row in W)

def tv(p,q):
    return sum((abs(x-y) for x,y in zip(p,q)),F(0))/2

def solve(rows,rhs,inds):
    """Integer fraction-free Bareiss elimination with exact rational backsolve."""
    n=7
    a=[list(rows[i])+[rhs[i]] for i in inds]
    prev=1
    for j in range(n-1):
        pivot_idx=next((i for i in range(j,n) if a[i][j]),None)
        if pivot_idx is None:return None
        if pivot_idx!=j:a[pivot_idx],a[j]=a[j],a[pivot_idx]
        pivot=a[j][j]
        for i in range(j+1,n):
            mul=a[i][j]
            for k in range(j+1,n+1):
                numerator=a[i][k]*pivot-mul*a[j][k]
                if numerator%prev:raise ArithmeticError("nonexact Bareiss division")
                a[i][k]=numerator//prev
            a[i][j]=0
        prev=pivot
    if not a[-1][-2]:return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(a[j][n])-sum((a[j][i]*x[i] for i in range(j+1,n)),F(0)))/a[j][j]
    return tuple(x)

def run():
    # Seven-dimensional joint source polytope P:
    # t>=s; t+s>=1; 3t-2s<=1; and 16 Walsh atom inequalities.
    # These three parameter inequalities exactly form the triangle
    # conv{(1/2,1/2),(3/5,2/5),(1,1)}.
    rows=list(W);rhs=[-1]*16
    rows += [(1,-1,0,0,0,0,0),(1,1,0,0,0,0,0),(-3,2,0,0,0,0,0)]
    rhs += [0,1,-1]
    V=set();nonsingular=feasible=0
    for ids in combinations(range(len(rows)),7):
        sol=solve(rows,rhs,ids)
        if sol is None:continue
        nonsingular+=1
        if any(sum((a*b for a,b in zip(row,sol)),F(0))<b for row,b in zip(rows,rhs)):continue
        feasible+=1;V.add(sol)
    assert V
    hist={};maximum_excess=None;tight=0;violations=[]
    for t,s,h,u,v,w,z in sorted(V):
        p=law(t,s,h,u,v,w,z)
        q=law(t,s,t+s-1)
        H=law(t,s,1-t+s)
        R=1-t
        assert F(0)<=s<=t<=1 and t+s>=1 and 3*t-2*s<=1
        assert min(p)>=0 and sum(p)==1
        assert min(q)>=0 and sum(q)==1
        assert min(H)>=0 and sum(H)==1
        assert tv(H,q)==R  # explicit matching witness on EVERY parameter point
        excess=tv(p,q)-R
        if excess>0:violations.append({'coordinates':[str(x) for x in (t,s,h,u,v,w,z)],'excess':str(excess)})
        maximum_excess=excess if maximum_excess is None else max(excess,maximum_excess)
        tight+=int(excess==0)
        key=f'({t},{s})';hist[key]=hist.get(key,0)+1
    # symbolic target endpoints and 2D geometry: area W0=1/20
    for t,s in [(F(1,2),F(1,2)),(F(3,5),F(2,5)),(F(1),F(1)),(F(4,5),F(7,10))]:
        if 3*t-2*s<=1 and t+s>=1 and t>=s:
            assert tv(law(t,s,1-t+s),law(t,s,t+s-1))==1-t
    assert maximum_excess==0 and not violations
    return {
        'schema':'R749SPH_WALSH_COMPLEMENTARY_CENTER_RISK_V1',
        'status':'PASS','review':'AUTHOR_EXACT_NOT_REVIEWED',
        'frozen_science':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'scope':'auxiliary 16-atom Walsh fiber; continuous all-real complementary triangle',
        'parameter_region':'conv{(1/2,1/2),(3/5,2/5),(1,1)}',
        'exact_center':'p(t,s,t+s-1,0,0,0,0)',
        'exact_worst_tv':'1-t',
        'lower_witness':'H=p(t,s,1-t+s,0,0,0,0), TV(H,q)=1-t',
        'symmetric_region':'by swap of (t,s) and bit pairs',
        'full_upper_wedge_formula':'for t>=s, t+s>=1: max((3-t-2*s)/4,1-t); swap t,s otherwise',
        'complementary_parameter_area':'1/20',
        'candidate_active_sets':comb(19,7),
        'nonsingular_bases':nonsingular,
        'feasible_bases_with_repeats':feasible,
        'distinct_vertices':len(V),
        'risk_tight_vertices':tight,
        'max_risk_excess':str(maximum_excess),
        'parameter_vertex_histogram':dict(sorted(hist.items())),
        'violations':violations,
        'meaning':'proof of worst-case risk for the specified calibrated center, not a global minimax assertion on complementary triangle',
        'native_transfer':'OPEN'
    }

if __name__=='__main__':
    print(json.dumps(run(),indent=2,ensure_ascii=False,sort_keys=True))
