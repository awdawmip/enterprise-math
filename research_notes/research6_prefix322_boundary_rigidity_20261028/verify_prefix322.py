#!/usr/bin/env python3
"""Exact BRC verification for PREFIX-322 boundary-rigidity witnesses.
No third-party dependencies. Proves finite rational premises; global
phase-minimizer classification is inherited from PREFIX-321's proof.
"""
from fractions import Fraction as F
import json

Z = (F(0), F(0))
ONE = (F(1), F(0))
I = (F(0), F(1))

def g(a=0,b=0): return (F(a),F(b))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def conj(a): return (a[0],-a[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(t,a): return (t*a[0],t*a[1])
def norm2(a): return mul(a,conj(a))[0]
def normv2(a): return sum((norm2(z) for z in a),F(0))
def fs(x): return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def gs(a): return [fs(a[0]),fs(a[1])]

A = [[g(4),g(4),Z], [Z,g(-4),g(4)], [g(-5,3),Z,g(-3,1)], [g(-2,-2),g(4,4),g(2,2)], [g(-2),Z,g(5,2)]]
b0 = [g(-2),g(0,-2),g(1)]
b2 = [g(0,2),g(2),g(0,-1)]
t0 = g(F(-7,14),F(3,14))
t2 = g(F(-7,14),F(-3,14))
assert norm2(t0)==norm2(t2)==F(29,98)
assert normv2(b0)==normv2(b2)==9

# BRC is performed at labeled-path pair level, including reference path.
count = 0
pairs = 0
def brc(state,port,ref=Z):
    global count,pairs
    paths = [(f"source:{k}",scale(F(1,8),mul(A[port][k],state[k]))) for k in range(3)]
    if ref!=Z: paths.append(("reference",ref))
    total=Z
    for la,a in paths:
        for lb,b in paths:
            total=add(total,mul(a,conj(b)))
            pairs+=1
    assert total[1]==0 and total[0]>=0
    count+=1
    return total[0]

def obs(state): return [[brc(state,j,rho) for rho in (Z,ONE,I)] for j in range(5)]

# Verify the exact Port amplitudes and their shared accurate base masses.
def amplitude(state,j):
    value=Z
    for k in range(3): value=add(value,scale(F(1,8),mul(A[j][k],state[k])))
    return value

c=[amplitude(b0,j) for j in range(5)]
d=[amplitude(b2,j) for j in range(5)]
port_m=[F(2),F(5,4),F(37,32),F(25,8),F(85,64)]
assert [norm2(x) for x in c]==port_m
assert [norm2(x) for x in d]==port_m
assert max(port_m)==F(25,8)

witnesses=[]
all_pairs=[]
for k in range(4):
    rotation=(ONE,I,g(-1),g(0,-1))[k]
    a0=[mul(mul(rotation,t0),v) for v in b0]
    a2=[mul(mul(rotation,t2),v) for v in b2]
    all_pairs.append((a0,a2))
    o0,o2=obs(a0),obs(a2)
    assert all(o0[j][0]==o2[j][0] for j in range(5))
    assert all(abs(o0[j][r]-o2[j][r])<=2 for j in range(5) for r in (1,2))
    mid=[[ (o0[j][r]+o2[j][r])/2 for r in (1,2)] for j in range(5)]
    assert all(abs(mid[j][r-1]-obs_[j][r])<=1 for j in range(5) for r in (1,2) for obs_ in (o0,o2))
    d2=normv2([sub(a,b) for a,b in zip(a0,a2)])
    assert d2==F(240,49)
    assert d2/4==F(60,49)
    witnesses.append({"rotation":k,"a0":list(map(gs,a0)),"a2":list(map(gs,a2)),"Q0":[fs(o0[j][0]) for j in range(5)],"common_Y":[list(map(fs,row)) for row in mid],"distance_squared":fs(d2),"two_state_meb_squared":fs(d2/4)})
assert count==120 and pairs==1640
# Finite C4 cross-pair exclusion; global exclusion of all other phases
# comes ONLY from the prior PREFIX-321 continuous minimizer theorem.
cross_grid=[]
for j,(a,_) in enumerate(all_pairs):
    row=[]
    for k,(_,b) in enumerate(all_pairs):
        diffs=[sub(amplitude(a,t),amplitude(b,t)) for t in range(5)]
        feasible=all(abs(v[0])<=1 and abs(v[1])<=1 for v in diffs)
        assert feasible==(j==k)
        row.append(feasible)
    cross_grid.append(row)

# A separate exact rational r=1/4 witness for the small-scale full-circle lemma.
r=F(1,4)
assert 25*r*r <= 2   # r <= sqrt(2)/5
# For both shapes and every phase the maximal per-coordinate BRC error is
# 2 r max_j |(U b)_j| = 2r sqrt(25/8) <= 1.
assert 4*r*r*F(25,8)<=1
assert F(9)*r*r == F(9,16)

# At rcrit, four cross pairs are the complete minimizer list by PREFIX-321.
# Cross-pair uniqueness then excludes a third phase in any mixed shared-Y fiber.
assert len({tuple(gs(mul(rot,t0))) for rot in (ONE,I,g(-1),g(0,-1))})==4
assert len({tuple(gs(mul(rot,t2))) for rot in (ONE,I,g(-1),g(0,-1))})==4
result={
  "schema":"EM_PREFIX322_BOUNDARY_RIGIDITY_EXACT_V1",
  "source":"PREFIX-321 global minimizer theorem reused (not independently re-proved here)",
  "BRC_observation_count":count,
  "ordered_labeled_path_pairs":pairs,
  "critical_scale_squared":fs(F(29,98)),
  "phase_minimum_squared":fs(F(98,29)),
  "critical_mixed_fiber_max_cardinality":2,
  "critical_exact_meb_squared":fs(F(60,49)),
  "small_scale_full_circle_threshold_squared":fs(F(2,25)),
  "small_scale_exact_meb_formula":"9*r^2, 0 < r^2 <= 2/25 (continuous phases)",
  "witnesses":witnesses,
  "cross_C4_pair_feasibility":cross_grid,
  "port_base_masses_unscaled":[fs(m) for m in port_m],
  "status":"PASS",
  "unverified_by_this_checker":"Continuous global sharpness, leaf margin delta_e, X6/Detector bridge, independent admission"
}
print(json.dumps(result,ensure_ascii=False,indent=2))
