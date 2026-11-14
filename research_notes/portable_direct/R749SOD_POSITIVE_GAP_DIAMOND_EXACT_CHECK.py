#!/usr/bin/env python3
"""R749SOD: 7D joint-polytope exact certificate of a larger Walsh calibration gap.
Frozen scientific input: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Source and proof not independently reviewed. Pure Python stdlib Fraction/integer Bareiss.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from math import comb
import json

MASKS=(3,12,15,1,2,4,8)
D=F(1,100)
ROWS=[tuple(1 if (m & x).bit_count()%2==0 else -1 for m in MASKS) for x in range(16)]
ROWS += [(1,1,0,0,0,0,0),(-1,-1,0,0,0,0,0),
         (1,-1,0,0,0,0,0),(-1,1,0,0,0,0,0)]
# Integers after scaling all seven unknowns by 100: y=(100t,100s,100h,...)
RHS=[-100]*16+[100*(1-D),-100*(1+D),-100*D,-100*D]
RHS=[int(x) for x in RHS]
assert len(ROWS)==20

def bareiss_solve(row_ids):
    n=7
    a=[list(ROWS[i])+[RHS[i]] for i in row_ids]
    prev=1
    for j in range(n-1):
        k=next((k for k in range(j,n) if a[k][j]!=0),None)
        if k is None: return None
        if k!=j:
            a[j],a[k]=a[k],a[j]
        p=a[j][j]
        for i in range(j+1,n):
            q=a[i][j]
            for l in range(j+1,n+1):
                z=a[i][l]*p-q*a[j][l]
                assert z%prev==0
                a[i][l]=z//prev
            a[i][j]=0
        prev=p
    if a[n-1][n-1]==0: return None
    v=[F(0)]*n
    for j in range(n-1,-1,-1):
        v[j]=(F(a[j][n])-sum((a[j][k]*v[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(v)

def witness_laws(t,s):
    d=abs(t-F(1,2))+abs(s-F(1,2))
    e=abs(t-s)
    had=1-e
    neg=(d,)+tuple((-F(1,2)+d for _ in range(4)))
    return (had,F(0),F(0),F(0),F(0)),neg

def law(t,s,h,u,v,w,z):
    coeff=(t,s,h,u,v,w,z)
    return tuple((1+sum((a*b for a,b in zip(row,coeff)),F(0)))/16 for row in ROWS[:16])

def verify_witnesses():
    # All is piecewise-affine on orthants of the (t,s) diamond.
    # In every orthant, checking the boundary corners and the center suffices.
    t0=s0=F(1,2)
    candidates=[(t0,s0),(t0+D,s0),(t0-D,s0),(t0,s0+D),(t0,s0-D)]
    Etad=(1,2,4,7,8,11,13,14)
    Eneg=(0,1,2,3,4,5,6,8,9,10,12)
    for t,s in candidates:
        ad,neg=witness_laws(t,s)
        muad=law(t,s,*ad); muneg=law(t,s,*neg)
        assert min(muad)>=0 and min(muneg)>=0
        assert sum(muad)==sum(muneg)==1
        q=law(t,s,F(2,11),0,0,0,0)
        l_ad=sum((q[i]-muad[i] for i in Etad),F(0))
        l_neg=sum((q[i]-muneg[i] for i in Eneg),F(0))
        d=abs(t-t0)+abs(s-s0); e=abs(t-s)
        assert l_ad==(1-e-F(2,11))/2
        assert l_neg==(3*F(2,11)+6-15*d)/16
        assert (3*l_ad+8*l_neg)/11==F(9,22)-(3*e+15*d)/22
    return {'witness_endpoints_checked':len(candidates),
            'calibrated_lower_formula':'9/22-(3*abs(t-s)+15*d)/22',
            'uniform_calibrated_lower':str(F(9,22)-F(9,11)*D),
            'witness_A_h':'1-abs(t-s)',
            'witness_B_free_coefficients':'(d,-1/2+d,-1/2+d,-1/2+d,-1/2+d)',
            'event_A':list(Etad),'event_B':list(Eneg)}

def risk_at_vertex(y):
    t,s,h,u,v,w,z=(v/100 for v in y)
    diff=(t-F(3,5),s-F(3,5),h-F(1,5),u,v,w,z)
    return sum((abs(sum((a*b for a,b in zip(row,diff)),F(0))) for row in ROWS[:16]),F(0))/32

def exact_orthant_certificates():
    """On each signed quadrant d is affine, so risk-d/12 is convex."""
    global ROWS, RHS
    saved_rows=ROWS[:]; saved_rhs=RHS[:]
    reports=[]
    for sx,sy in ((1,1),(1,-1),(-1,1),(-1,-1)):
        ROWS=saved_rows[:16]+[(sx,0,0,0,0,0,0),
                              (0,sy,0,0,0,0,0),
                              (-sx,-sy,0,0,0,0,0)]
        RHS=saved_rhs[:16]+[50*sx,50*sy,-1-50*(sx+sy)]
        vset=set(); counts=Counter()
        for ids in combinations(range(19),7):
            counts['active_sets']+=1
            y=bareiss_solve(ids)
            if y is None:continue
            counts['nonsingular_bases']+=1
            if all(sum((a*b for a,b in zip(row,y)),F(0))>=bound
                   for row,bound in zip(ROWS,RHS)):
                counts['feasible_bases']+=1
                vset.add(y)
        assert counts['active_sets']==comb(19,7)==50388
        assert vset
        max_adjusted=F(-100)
        for y in vset:
            t,s=(z/100 for z in y[:2])
            d=sx*(t-F(1,2))+sy*(s-F(1,2))
            assert 0<=d<=D
            max_adjusted=max(max_adjusted,risk_at_vertex(y)-d/12)
        assert max_adjusted<=F(2,5),(sx,sy,max_adjusted)
        reports.append({'signs':[sx,sy],**counts,
                        'distinct_vertices':len(vset),
                        'max_risk_minus_d_over_12':str(max_adjusted),
                        'violations':0})
    ROWS=saved_rows; RHS=saved_rhs
    return reports

def main():
    wit=verify_witnesses()
    orthants=exact_orthant_certificates()
    counts=Counter()
    vertices=set()
    for ids in combinations(range(20),7):
        counts['active_sets']+=1
        ys=bareiss_solve(ids)
        if ys is None: continue
        counts['nonsingular_bases']+=1
        if all(sum((a*b for a,b in zip(row,ys)),F(0))>=bound for row,bound in zip(ROWS,RHS)):
            counts['feasible_bases']+=1
            vertices.add(ys)
    assert counts['active_sets']==comb(20,7)==77520
    assert len(vertices)>0
    worst=max((risk_at_vertex(v) for v in vertices))
    upper=F(2,5)+D/12
    assert worst<=upper,(worst,upper)
    gap=F(9,22)-F(9,11)*D-upper
    assert gap==F(1,13200)>0
    return {'result':'PASS','unit':'R749SOD',
      'scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'scope':'auxiliary 16-state Walsh source fiber, all real L1 diamond points, author-side / NOT_REVIEWED',
      'diamond_L1_radius':str(D),'diamond_area':str(2*D**2),
      'global_free_center':'q0=[1+(3/5)(chi_3+chi_12)+(1/5)chi_15]/16',
      'free_center_worst_joint_vertex_risk':str(worst),
      'free_center_uniform_certified_upper':str(upper),
      'pointwise_free_upper':'2/5+d/12',
      'orthant_exact_polytope_certificates':orthants,
      'pointwise_strict_gap_bound':'1/110-(3*abs(t-s)+15*d)/22-d/12 >= 1/110-119*d/132',
      'calibrated_lower_witness':wit,
      'strict_gap_uniform_lower':str(gap),
      'joint_source_polytope':dict(counts,distinct_vertices=len(vertices)),
      'method':'Exact joint 7D polytope convexity, full seven-active-constraint enumeration, plus analytic two-event lower bound.'}
if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,sort_keys=True,indent=2))
