#!/usr/bin/env python3
"""Exact finite proof certificate of a 3D optimal-center octahedron in the frozen auxiliary Walsh fiber."""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json

MASKS=(3,12,15,1,2,4,8)
C=tuple(tuple((-1 if (k&m).bit_count()%2 else 1) for m in MASKS) for k in range(16))
# Fixed t=1/10 and s=1/2; Y=10*(h_source,u,v,w,z).
A=tuple(c[2:] for c in C)
B=tuple(-10-c[0]-5*c[1] for c in C)

def bareiss(ind):
    n=5
    a=[list(A[i])+[B[i]] for i in ind]
    prev=1
    for j in range(n-1):
        i=next((k for k in range(j,n) if a[k][j]),None)
        if i is None:return None
        if i!=j:a[i],a[j]=a[j],a[i]
        p=a[j][j]
        for k in range(j+1,n):
            v=a[k][j]
            for l in range(j+1,n+1):
                z=a[k][l]*p-v*a[j][l]
                if z%prev:raise ArithmeticError('inexact Bareiss')
                a[k][l]=z//prev
            a[k][j]=0
        prev=p
    if not a[-1][n-1]:return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(a[j][n])-sum((a[j][k]*x[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(x)

def dot(x,y):return sum((a*b for a,b in zip(x,y)),F(0))
def risk_numerator(y,q):return sum((abs(dot(a,tuple(z-v for z,v in zip(y,q)))) for a in A),F(0))

def run():
    vv=set();non=feas=0
    for ind in combinations(range(16),5):
        y=bareiss(ind)
        if y is None: continue
        non+=1
        if all(dot(a,y)>=b for a,b in zip(A,B)):
            feas+=1;vv.add(y)
    assert len(vv)>0
    qs=[tuple(F((2 if i==j else 0)*sign) for i in range(5)) for j in range(3) for sign in (-1,1)]
    out=[]
    for q in qs:
        assert all(10+c[0]+5*c[1]+dot(a,q)>=0 for c,a in zip(C,A))
        excess=[risk_numerator(y,q)-144 for y in vv]
        assert max(excess)==0,(q,max(excess))
        out.append({'center_scaled_10':list(map(str,q)), 'max_excess_times_320':str(max(excess)), 'tight_vertices':sum(e==0 for e in excess)})
    lo=(F(0),F(-1),F(-1),F(5),F(9))
    hi=(F(0),F(-1),F(-1),F(-5),F(-9))
    assert all(dot(a,z)>=b for z in (lo,hi) for a,b in zip(A,B))
    assert risk_numerator(lo,hi)==288   # TV between source pair = 288/320 = 9/10
    print(json.dumps({
        'status':'PASS','unit':'R749SPP','pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'scope':'auxiliary 16-atom Walsh fiber at t=1/10,s=1/2',
        'theorem':'all q=p(t,s,h,u,v,0,0) with |h|+|u|+|v|<=1/5 are calibrated minimax centers',
        'exact_rho_and_calibrated_rho':'9/20',
        'dimension_of_proved_optimal_face_carrier':3,'octahedron_volume_in_huv_coordinates':'4/375',
        'source_pair_tv':'9/10','candidate_bases':comb(16,5),'nonsingular_bases':non,
        'feasible_bases_with_repetitions':feas,'distinct_source_vertices':len(vv),
        'six_center_exact_upper_certificates':out,'review':'AUTHOR_EXACT_NOT_REVIEWED'
    },sort_keys=True,indent=2))

if __name__=='__main__':run()
