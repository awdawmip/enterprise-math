#!/usr/bin/env python3
"""R110: exact finite checks of the all-weight residue certificate examples."""
from fractions import Fraction as Q
from math import lcm
import json
S=(10,-5,1)
T=(24,-14,3)
WEIGHTS={
    "original_sharp":(9,1,58,41),
    "extended_large_D":(5,1,100,100),
    "outside_order_B_gt_A":(2,5,100,100),
    "equal_weights":(1,1,1,1)
}
def port(a):
    return max(sum(max(0,t) for t in a),sum(max(0,-t) for t in a))
def moments(a):
    x,y,z=a
    return x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z
def six(a):
    u,v,h=moments(a)
    return abs(u),abs(v),abs(h),abs(v-u),abs(h-u),abs(h-v)
def orbit(a):
    return min(tuple(t%3 for t in a),tuple((-t)%3 for t in a))
assert (port(S),moments(S))==(11,(1,0,1))
assert (port(T),moments(T))==(27,(0,-6,0))
directions=[]
for x in range(-38,39):
    for y in range(-38,39):
        for z in range(-38,39):
            if not (x>0 or x==0 and y>0 or x==0 and y==0 and z>0):
                continue
            a=(x,y,z)
            q=port(a)
            if q<=38:
                directions.append((a,q,six(a)))
assert len(directions)==95133
result={
 "id":"X6-R110-ALL-WEIGHT-EXCLUSION-CERT",
 "status":"PASS",
 "finite_domain":"all unoriented nonzero integer triples q<=38",
 "scanned_directions":len(directions),
 "examples":{}
}
for name,(A,B,C,D) in WEIGHTS.items():
    den=(A+B,A+C,A+D,B+C,B+D,C+D)
    L=lcm(*den)
    k=tuple(L//d for d in den)
    def score(c):
        return max(n*t for n,t in zip(c,k))
    U=min(Q(1,min(A,C)+min(B,D)),Q(6,C+min(A,B,D)))
    thresholds=(Q(2,A+B),Q(6,C+min(A,B)),Q(8,D+min(A,B,C)))
    assert U<=min(thresholds)
    assert Q(score(six(S)),L)==Q(1,min(A,C)+min(B,D))
    assert Q(score(six(T)),L)==Q(6,C+min(A,B,D))
    eta27=min(score(c) for a,q,c in directions if q<=27)
    eta38=min(score(c) for a,q,c in directions)
    near=[(a,q) for a,q,c in directions if 2*score(c)<3*eta38]
    assert len(near)<=12
    assert len({orbit(a) for a,q in near})==len(near)
    assert (0,1,2) not in {orbit(a) for a,q in near}
    if name=="original_sharp":
        assert eta38*10==L and len(near)==12 and max(q for a,q in near)==38
    if name in ("extended_large_D","outside_order_B_gt_A"):
        assert len(near)==3
    if name=="equal_weights":
        assert len(near)==1
    result["examples"][name]={
       "weights":[A,B,C,D],
       "U":str(U),
       "certificate_thresholds":[str(t) for t in thresholds],
       "eta_p27":str(Q(eta27,L)),
       "eta_p38":str(Q(eta38,L)),
       "near_count_p38":len(near),
       "near_vectors":[list(a) for a,q in near]
    }
print(json.dumps(result,ensure_ascii=False,indent=2))
