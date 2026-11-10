#!/usr/bin/env python3
"""Exact local support stratification around R5's sharp physical boundary.

Run: python FACE_TRANSITION.py (from this research_notes directory).
Loads VERIFY_SHARP.py in the same directory, including its exact finite
4,845 + 1,140 support checks, and extends them to the local 7D facet.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import contextlib
import io
import runpy

with contextlib.redirect_stdout(io.StringIO()):
    model=runpy.run_path(str(Path(__file__).with_name("VERIFY_SHARP.py")))

D=model["D"]
CERT=model["CERT"]
forced=tuple(sorted(D.index(e) for e in CERT))
other=tuple(i for i in range(30) if i not in forced)
relations=model["exact_row_relations"]
b=model["br"]
B=model["bt"]
P=model["P"]
Jsl=model["jac"](model["both_slacks"])*P
sl0=model["both_slacks"](model["p"])
e0=model["EB"]
Eb=model["DeltaB"]
SB=model["SB"]
tstar=model["t"]
rstar=F(23,17050000)

mu0=F(23,4000000)
mu_gradient=(F(0),F(0),F(0),F(1,80),-F(1),F(0),F(0),F(13,4))
assert SB[7]==(1,3)
assert F(e0[7])==F(sl0[19])==mu0
assert all(F(Eb[7,k])==F(Jsl[19,k])==mu_gradient[k] for k in range(8))

bstar=[F(b[i])+sum(F(B[i][k])*tstar[k] for k in range(8))
       for i in range(15)]

def value_and_gradient(y):
    center=sum(y[i]*bstar[i] for i in range(15))
    grad=tuple(sum(y[i]*B[i][k] for i in range(15)) for k in range(8))
    return center,grad

def strongest_exclusion(vectors):
    candidates=[]
    for w in vectors:
        center,grad=value_and_gradient(w)
        if center:
            norm=sum(map(abs,grad))
            candidates.append((None if not norm else abs(center)/norm))
    # None denotes a zero-slope contradiction, thus an infinite radius.
    if not candidates:return None
    return max(candidates,key=lambda x:(x is None,x))

aligned14=0
excluded14=0
min14=None
for ext in combinations(other,4):
    rel=list(relations(forced+ext))
    radius=strongest_exclusion(rel)
    if radius is None:
        aligned14+=1
        assert len(rel)==1
        c,g=value_and_gradient(rel[0])
        assert c==0
        # Every matching 14-column span imposes precisely mu_1(t)=0.
        factor=g[3]/mu_gradient[3]
        assert factor!=0
        assert all(g[k]==factor*mu_gradient[k] for k in range(8))
    else:
        excluded14+=1
        if radius is not None and (min14 is None or radius<min14):
            min14=radius
assert (aligned14,excluded14)==(1031,3814)
assert min14 is not None and min14>0

min13=None
count13=0
for ext in combinations(other,3):
    radius=strongest_exclusion(relations(forced+ext))
    assert radius is not None
    if radius is not None and (min13 is None or radius<min13):
        min13=radius
    count13+=1
assert count13==1140 and min13 is not None and min13>0

pstar=model["pst"]
sl=model["both_slacks"](pstar)
eb=model["vst"]
assert tuple(i for i,v in enumerate(sl) if not v)==(4,15,19,23)
assert tuple(i for i,v in enumerate(eb) if not v)==(7,)

def positive_radius(values,derivatives,ignored):
    ratios=[]
    for i,v in enumerate(values):
        if i in ignored:continue
        assert v>0
        L=sum(abs(F(derivatives[i,k])) for k in range(8))
        if L:ratios.append(F(v)/L)
    return min(ratios)

min_physical=positive_radius(sl,Jsl,{4,15,19,23})
min_basis=positive_radius(eb,Eb,{7})
# Dual forced-edge positivity at tstar: prior certified global margin.
dual_margin=F(367114064296183,1957795262280000000)
dual_gradient_bound=F(585227,46800)
dual_radius=dual_margin/dual_gradient_bound
delta=min(min14,min13,min_physical,min_basis,dual_radius)/2
assert delta==F(63,151745000) and delta>0
assert model["B8"].rank()==8

print("MU1=E_(1,3)=PHYSICAL_SLACK_19")
print("MU1(t)=23/4000000 + t4/80 - t5 + 13*t8/4 (1-based indexing)")
print("FOURTEEN_EDGE_SPANS_THROUGH_TSTAR",aligned14)
print("ALL_1031_FORCE_MU1_ZERO")
print("OTHER_14_EDGE_SPANS_EXCLUDED",excluded14)
print("ALL_13_EDGE_SPANS_EXCLUDED",count13)
print("MIN_EXCLUSION_RADIUS_OTHER14",min14)
print("MIN_EXCLUSION_RADIUS_13",min13)
print("MIN_OTHER_PHYSICAL_SLACK_RADIUS",min_physical)
print("MIN_OTHER_BASIS_WEIGHT_RADIUS",min_basis)
print("DUAL_POSITIVITY_RADIUS",dual_radius)
print("EXPLICIT_LOCAL_RADIUS",delta)
print("OBSERVER_FACE_DIMENSION",7)
print("PASS_LOCAL_LAWFUL_MIN_SUPPORT_14_IFF_MU1_ZERO_ELSE_15")
