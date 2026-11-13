#!/usr/bin/env python3
"""Exact R749SNT single-triangle zero calibration-gap certificate.

Scientific input pinned to awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389
Pure standard-library integer Bareiss + Fraction; not native X6 correspondence.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json

PIN = 'a72226e2430ffa4786321ac86e7f0c599d5f0389'
MASKS = (3, 12, 15, 1, 2, 4, 8)
ROWS = tuple(tuple(1 if (x&m).bit_count()%2 == 0 else -1 for m in MASKS)
             for x in range(16))
EVENT = (3, 5, 7, 9, 11, 13, 14, 15)
A=(F(7,10), F(1,10))
C=(F(3,5), F(7,40))
X=(F(3,5), F(3,20))
SCALE=40

def law(t,s,h,u,v,w,z):
    return tuple((1+sum((r*c for r,c in zip(row,(t,s,h,u,v,w,z))),F(0)))/16
                 for row in ROWS)

def eta(t,s):
    return F(31,40)-F(3,4)*t-F(5,2)*s

def radius(t,s):
    return (3+t-s)/8

def solve_bareiss(normals,bounds,selected,n=7):
    m=[list(normals[i])+[bounds[i]] for i in selected]
    prev=1
    for col in range(n-1):
        r=next((i for i in range(col,n) if m[i][col]),None)
        if r is None: return None
        if r != col: m[r],m[col]=m[col],m[r]
        pivot=m[col][col]
        for i in range(col+1,n):
            entry=m[i][col]
            for j in range(col+1,n+1):
                num=m[i][j]*pivot-entry*m[col][j]
                assert num%prev == 0
                m[i][j]=num//prev
            m[i][col]=0
        prev=pivot
    if not m[n-1][n-1]: return None
    sol=[F(0)]*n
    for i in range(n-1,-1,-1):
        sol[i]=(F(m[i][n])-sum((m[i][j]*sol[j] for j in range(i+1,n)),F(0)))/m[i][i]
    return tuple(sol)

def main():
    # Triangle parameters: t >= 3/5, 3t+4s <= 5/2, t+2s >= 9/10.
    normals=list(ROWS)+[(1,0,0,0,0,0,0),(-3,-4,0,0,0,0,0),(1,2,0,0,0,0,0)]
    bounds=[-SCALE]*16+[24,-100,36]
    stats={'all_active_bases':0,'nonsingular_bases':0,'feasible_bases':0}
    vertices=set()
    for selected in combinations(range(19),7):
        stats['all_active_bases']+=1
        sol=solve_bareiss(normals,bounds,selected)
        if sol is None: continue
        stats['nonsingular_bases']+=1
        if any(sum((a*b for a,b in zip(row,sol)),F(0))<limit
               for row,limit in zip(normals,bounds)):
            continue
        stats['feasible_bases']+=1
        vertices.add(tuple(v/SCALE for v in sol))
    assert stats['all_active_bases']==comb(19,7)==50388
    assert vertices
    excess=F(-1)
    tight=violations=0
    for t,s,h,u,v,w,z in vertices:
        source=law(t,s,h,u,v,w,z)
        center=law(t,s,eta(t,s),0,0,0,0)
        assert min(source)>=0 and min(center)>=0
        assert sum(source)==sum(center)==1
        gap=sum((abs(a-b) for a,b in zip(source,center)),F(0))/2-radius(t,s)
        if gap>excess: excess=gap
        tight+=int(gap==0)
        violations+=int(gap>0)
    assert violations==0 and excess==0
    for t,s in (A,C,X):
        center=law(t,s,eta(t,s),0,0,0,0)
        witness=law(t,s,0,s-1,-t,-s,-s)
        assert min(center)>=0 and min(witness)>=0
        assert sum(center)==sum(witness)==1
        # Any invariant predictor has mass 1/2 on EVENT.
        assert sum((witness[i] for i in EVENT),F(0))-F(1,2)==radius(t,s)
    assert all(sum((ROWS[i][j] for i in EVENT))==0 for j in (0,1,2))
    # A sharp failure for extrapolating the *old* P1 center to X.
    # Both measures are rational probability laws; the excess is exactly 1/640.
    t,s=X
    old_eta=F(3,20)-F(3,2)*s
    old_center=law(t,s,old_eta,0,0,0,0)
    bad_source=law(t,s,0,F(17,20),F(3,5),-F(3,20),-F(3,20))
    assert min(old_center)>=0 and min(bad_source)>=0
    old_risk=sum((abs(a-b) for a,b in zip(old_center,bad_source)),F(0))/2
    assert (old_eta,old_risk,radius(t,s),old_risk-radius(t,s)) == (
       -F(3,40),F(277,640),F(69,160),F(1,640))
    # Edge AC shares the SNS-P1 center eta=3/20-3s/2.
    for t,s in (A,C):
        assert eta(t,s)==F(3,20)-F(3,2)*s
    # All parameter triangle vertices are distinct, noncollinear; area 1/800.
    twice_area=abs((C[0]-A[0])*(X[1]-A[1])-(C[1]-A[1])*(X[0]-A[0]))
    assert twice_area==F(1,400)
    stats.update(distinct_vertices=len(vertices),tight_vertices=tight,
                 violating_vertices=violations,max_excess=str(excess))
    return dict(unit='R749SNT',status='PASS',review='NOT_REVIEWED',
        source_pin=PIN,
        model='16-state auxiliary Walsh source observer; no native X6/V29/V39 event identification',
        triangle_vertices=[list(map(str,p)) for p in (A,C,X)],
        triangle_halfspaces=['t >= 3/5','3*t+4*s <= 5/2','t+2*s >= 9/10'],
        triangle_area=str(twice_area/2),
        minimax_identity='rho(t,s)=rho_cal(t,s)=(3+t-s)/8',
        calibrated_center_eta='31/40-3*t/4-5*s/2',
        lower_source='(h,u,v,w,z)=(0,s-1,-t,-s,-s)',
        lower_event=list(EVENT),
        old_center_extrapolation_counterexample={
          'parameter':['3/5','3/20'], 'old_eta':'-3/40',
          'source_coefficients':['0','17/20','3/5','-3/20','-3/20'],
          'source_loss':'277/640','target_radius':'69/160','excess':'1/640',
          'scope':'failure of old P1 decoder extension, not a positive calibration gap'},
        exact_joint_vertex_certificate=stats,
        next_question='Continue along outer boundary t+2s=9/10 and test center-piece validity; seek full positive calibration gap outside certified polygons')

if __name__ == '__main__':
    print(json.dumps(main(),sort_keys=True,indent=2,ensure_ascii=False))
