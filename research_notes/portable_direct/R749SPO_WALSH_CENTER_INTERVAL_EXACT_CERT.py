#!/usr/bin/env python3
"""Exact finite certificate for an entire 1D slice of auxiliary Walsh minimax centers.
Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Rational arithmetic only, no floating tolerance or external dependencies.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import json

MASKS=(3,12,15,1,2,4,8)
W=tuple(tuple((-1 if (k & m).bit_count() % 2 else 1) for m in MASKS) for k in range(16))
# Scaled variables X=(6t,6h,6u,6v,6w,6z); s=1/2.
ROWS=tuple((w[0],w[2],w[3],w[4],w[5],w[6]) for w in W)+((1,0,0,0,0,0),(-1,0,0,0,0,0))
RHS=tuple(-6-3*w[1] for w in W)+(0,-1)
assert len(ROWS)==18 and len(RHS)==18

def solve_bareiss(ind):
    n=6
    A=[list(ROWS[i])+[RHS[i]] for i in ind]
    prev=1
    for j in range(n-1):
        p=next((i for i in range(j,n) if A[i][j]),None)
        if p is None: return None
        if p!=j: A[j],A[p]=A[p],A[j]
        pivot=A[j][j]
        for i in range(j+1,n):
            mult=A[i][j]
            for k in range(j+1,n+1):
                numerator=A[i][k]*pivot-mult*A[j][k]
                if numerator%prev: raise ArithmeticError('nonexact Bareiss')
                A[i][k]=numerator//prev
            A[i][j]=0
        prev=pivot
    if A[-1][n-1]==0: return None
    out=[Q(0)]*n
    for j in range(n-1,-1,-1):
        out[j]=(Q(A[j][n])-sum((A[j][k]*out[k] for k in range(j+1,n)),Q(0)))/A[j][j]
    return tuple(out)

def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q(0))
def risk_num(X,sign):
    # TV <= (1-t)/2 iff sum of 16 absolute (scaled Walsh differences) <= 16*(6-X_t)
    H=sign*(3-3*X[0])
    return sum((abs((X[1]-H)*w[2] + X[2]*w[3] + X[3]*w[4]+X[4]*w[5]+X[5]*w[6]) for w in W),Q(0))

def verify():
    vertices=set(); non=ok=0
    for ind in combinations(range(18),6):
        X=solve_bareiss(ind)
        if X is None: continue
        non+=1
        if all(dot(a,X)>=b for a,b in zip(ROWS,RHS)):
            ok+=1;vertices.add(X)
    assert len(vertices)>0
    maxex={s: max(risk_num(v,s)-16*(6-v[0]) for v in vertices) for s in (1,-1)}
    assert maxex[1]==maxex[-1]==0,maxex
    tight={str(s):sum(risk_num(v,s)==16*(6-v[0]) for v in vertices) for s in (1,-1)}
    # Endpoints and mid-slice source-pair/risk checks.
    for t in (Q(0),Q(1,100),Q(1,10),Q(1,6)):
        a=Q(1,2)-3*t
        assert a>=0
        for h in (a,-a):
            # feasibility of every atom at the selected center
            assert all(1+t*w[0]+Q(1,2)*w[1]+h*w[2]>=0 for w in W)
        # one explicit source: h_src=0,u=v=t,w=1-t,z=1/2
        source=(Q(0),t,t,1-t,Q(1,2))
        assert all(1+t*w[0]+Q(1,2)*w[1]+sum((c*d for c,d in zip(source,(w[2],w[3],w[4],w[5],w[6]))),Q(0))>=0 for w in W)
        def tv_h(h):
            return sum((abs(source[0]*w[2]+source[1]*w[3]+source[2]*w[4]+source[3]*w[5]+source[4]*w[6]-h*w[2]) for w in W),Q(0))/32
        assert tv_h(a)==tv_h(-a)==(1-t)/2
        eps=Q(1,100)
        assert tv_h(a+eps)>(1-t)/2 and tv_h(-a-eps)>(1-t)/2
    out={
        'status':'PASS','research_unit':'R749SPO','model':'frozen auxiliary 16-atom Walsh',
        'scientific_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'parameter_slice':'s=1/2, 0<=t<=1/6',
        'all_calibrated_optimal_h_in_one_Walsh_center_family':'-(1/2-3t) <= h <= 1/2-3t',
        'center':'p(t,1/2,h,0,0,0,0)',
        'radius':'(1-t)/2',
        'active_six_facet_candidates':comb(18,6),
        'nonsingular_bases':non,'feasible_bases_with_repetitions':ok,
        'unique_exact_vertices':len(vertices),'tight_vertices_by_center':tight,
        'maximum_exact_upper_bound_excess_scaled_by_192':{str(k):str(v) for k,v in maxex.items()},
        'lower_bound':'explicit compatible antipodal source pair with TV=1-t',
        'necessity':'explicit compatible source (h_src=0,u=v=t,w=1-t,z=1/2) gives risk>(1-t)/2 whenever |h|>1/2-3t',
        'review_status':'AUTHOR_EXACT_NOT_REVIEWED'
    }
    print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':verify()
