#!/usr/bin/env python3
"""Exact 7D (t,s,h,u,v,w,z) Walsh 16-atom joint-polytope certificate.
Region T=conv{(1,0),(3/5,2/5),(1,1)} and its parameter-swapped image.
No external packages, floats, or sampling.
"""
import json
from fractions import Fraction as F
from itertools import combinations
from math import comb
M=(3,12,15,1,2,4,8)
W=tuple(tuple(1 if not ((k&m).bit_count()&1) else -1 for m in M) for k in range(16))
def law(t,s,h=0,u=0,v=0,w=0,z=0):
    return tuple((1+sum((a*b for a,b in zip((t,s,h,u,v,w,z),row)),F(0)))/16 for row in W)
def tv(p,q):return sum((abs(x-y) for x,y in zip(p,q)),F(0))/2
def solve(rows,rhs,inds):
    n=7;a=[list(rows[i])+[rhs[i]] for i in inds];prev=1
    for j in range(n-1):
        pivot_idx=next((i for i in range(j,n) if a[i][j]),None)
        if pivot_idx is None:return None
        if pivot_idx!=j:a[pivot_idx],a[j]=a[j],a[pivot_idx]
        pivot=a[j][j]
        for i in range(j+1,n):
            mul=a[i][j]
            for k in range(j+1,n+1):
                num=a[i][k]*pivot-mul*a[j][k]
                if num%prev:raise ValueError('Bareiss exact division failed')
                a[i][k]=num//prev
            a[i][j]=0
        prev=pivot
    if not a[-1][-2]:return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(a[j][n])-sum((a[j][i]*x[i] for i in range(j+1,n)),F(0)))/a[j][j]
    return tuple(x)
def pplus(t,s,sign=1):
    return law(t,s,t+s-1,sign*(1-s),sign*(1-s),sign*(1-t),sign*(1-t))
def exact_lower(t,s):
    assert F(0)<=s<=t<=1 and t+s>=1
    q=law(t,s,t+s-1)
    P=pplus(t,s,1);N=pplus(t,s,-1)
    for a in (q,P,N): assert sum(a)==1 and min(a)>=0
    R=(3-t-2*s)/4
    assert all((x+y)/2==z for x,y,z in zip(P,N,q))
    assert tv(P,N)==2*R
    return dict(t=str(t),s=str(s),radius=str(R),pair_tv=str(tv(P,N)))
def check_swap_automorphism():
    # Swap the two bit-pairs of K=F_2^4: (k0,k1) <-> (k2,k3).
    perm=lambda k: ((k & 3)<<2) | ((k & 12)>>2)
    for k in range(16):
        kp=perm(k)
        a=W[k];b=W[kp]
        assert b == (a[1],a[0],a[2],a[5],a[6],a[3],a[4])
    # Thus p_{t,s,h,u,v,w,z} maps to p_{s,t,h,w,z,u,v}.
    # This exchange preserves positivity, normalization, TV,
    # minimax radii and center calibration for EVERY (t,s).
    for t,s in [(F(3,5),F(2,5)),(F(1),F(0)),(F(1),F(1))]:
        src=law(t,s,t+s-1,1-s,1-s,1-t,1-t)
        flipped=law(s,t,t+s-1,1-t,1-t,1-s,1-s)
        assert all(src[k]==flipped[perm(k)] for k in range(16))
    return 'PASS'
def run():
    assert check_swap_automorphism()=='PASS'
    # A x >= b; x=(t,s,h,u,v,w,z)
    rows=list(W);rhs=[-1]*16
    rows += [(-1,0,0,0,0,0,0),(1,1,0,0,0,0,0),(3,-2,0,0,0,0,0)]
    rhs += [-1,1,1]
    vertices=set();feasible=nonsingular=0
    for inds in combinations(range(len(rows)),7):
        x=solve(rows,rhs,inds)
        if x is None:continue
        nonsingular+=1
        if any(sum((a*b for a,b in zip(r,x)),F(0))<b for r,b in zip(rows,rhs)):
            continue
        feasible+=1;vertices.add(x)
    assert vertices
    paramhist={};maxexcess=None;bad=[];tight=0
    for t,s,h,u,v,w,z in vertices:
        p=law(t,s,h,u,v,w,z);q=law(t,s,t+s-1)
        R=(3-t-2*s)/4
        assert min(p)>=0 and sum(p)==1 and min(q)>=0 and sum(q)==1
        ex=tv(p,q)-R
        if ex>0:bad.append((tuple(str(v) for v in (t,s,h,u,v,w,z)),str(ex)))
        maxexcess=max(maxexcess,ex) if maxexcess is not None else ex
        tight+=int(ex==0)
        key=(str(t),str(s));paramhist[key]=paramhist.get(key,0)+1
    res={'schema':'R749SPG_WALSH_REENTRANT_TRIANGLE_V1','status':'PASS' if not bad else 'FAIL',
    'frozen_science':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
    'region':'conv{(1,0),(3/5,2/5),(1,1)}; all real t,s',
    'exact_radius':'(3-t-2s)/4','gap':'0',
    'symmetric_region':'conv{(0,1),(2/5,3/5),(1,1)}; parameter swap',
    'combined_zero_gap_area':'2/5',
    'symmetry_automorphism':'PASS',
    'method':'seven-dimensional joint polytope exact Bareiss vertex audit plus explicit antipodal feasible sources',
    'candidate_active_sets':comb(19,7),'nonsingular_bases':nonsingular,'feasible_bases_with_repeats':feasible,
    'distinct_vertices':len(vertices),'tight_vertices':tight,'max_upper_excess':str(maxexcess),
    'parameter_vertex_histogram':{str(k):v for k,v in sorted(paramhist.items())},
    'lower_certificates':[exact_lower(*p) for p in [(F(1),F(0)),(F(3,5),F(2,5)),(F(1),F(1))]],
    'counterexamples':bad[:5],'review':'AUTHOR_EXACT_NOT_REVIEWED','native_transfer':'OPEN'}
    return res
if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
