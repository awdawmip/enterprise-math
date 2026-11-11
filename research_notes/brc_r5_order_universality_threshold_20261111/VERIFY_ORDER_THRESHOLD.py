#!/usr/bin/env python3
"""Exact R5 universal atom-order radius and first two order-count phases.

Uses immutable parent PR #2102's scientific witness on the stacked branch.
Python stdlib Fraction and integer Boolean-lattice DP; no numerical tolerance.
"""
from fractions import Fraction as F
from math import factorial, lcm
from pathlib import Path
import runpy, io, contextlib

prior_path=(Path(__file__).resolve().parents[1] /
    "brc_r5_sharp_nonlocal_fifteen_ray_20261111" / "VERIFY_R5_SHARP_RAY.py")
with contextlib.redirect_stdout(io.StringIO()):
    p=runpy.run_path(str(prior_path))
X=p["X"]
steps=p["steps"]
eps_max=p["eps_max"]
V=p["V"]
obs=p["obs"]
assert len(steps)==15 and len(X)==28 and min(X)>0
assert eps_max==F(9,115400000)
M=[tuple(a*w for w in v) for j,i,a,v in steps]
assert all(not any(obs(m)) for m in M)

# Every atom subset can be the prefix of some permutation.
negative_budget=[sum((-m[k] for m in M if m[k]<0),F(0)) for k in range(28)]
eps_all,kcrit=min((X[k]/negative_budget[k],k)
                  for k in range(28) if negative_budget[k]>0)
assert all(X[k]-eps_all*negative_budget[k]>=0 for k in range(28))
assert (eps_all,kcrit,negative_budget[kcrit])==(
    F(1401139989,8472895976720000000),14,F(337,9))
assert V[kcrit]==(0,3)
critical_atoms=tuple((steps[i][0],steps[i][1])
                     for i,m in enumerate(M) if m[kcrit]<0)
assert critical_atoms==tuple((5,i) for i in range(1,6))

# Integerized subset vectors at eps_max; each nonpositive change gives an
# exact first-zero breakpoint in eps/eps_max.
common=1
for z in X: common=lcm(common,z.denominator)
for m in M:
    for z in m:
        if z: common=lcm(common,(eps_max*z).denominator)
base=tuple(int(z*common) for z in X)
moves=[tuple(int(eps_max*z*common) for z in m) for m in M]
T=1<<15
states=[None]*T
states[0]=base
thresholds={}
for mask in range(1,T):
    bit=mask&(-mask)
    i=bit.bit_length()-1
    states[mask]=tuple(a+b for a,b in zip(states[mask^bit],moves[i]))
    ratios=[(F(base[k],base[k]-states[mask][k]),k)
            for k in range(28) if states[mask][k]<base[k]]
    if ratios:
        ratio,coord=min(ratios)
        if ratio<=1: thresholds.setdefault(ratio,[]).append((mask,coord))
phase=sorted(thresholds)
assert len(phase)>=3 and eps_max*phase[0]==eps_all
assert all(len(thresholds[phase[i]])==1 for i in range(3))
assert [eps_max*q for q in phase[:3]]==[
    F(1401139989,8472895976720000000),
    F(155682221,930258608720000000),
    F(1401139989,8359756416200000000)]
assert [thresholds[q][0][0] for q in phase[:3]]==[31744,32256,31748]

def census(eps):
    """Count all legal labeled permutations via exact subset recurrence."""
    assert 0<=eps<=eps_max
    scale=1
    for z in X: scale=lcm(scale,z.denominator)
    for m in M:
        for z in m:
            if z: scale=lcm(scale,(eps*z).denominator)
    base0=tuple(int(z*scale) for z in X)
    mm=[tuple(int(eps*z*scale) for z in m) for m in M]
    state=[None]*T
    state[0]=base0
    valid=bytearray(T)
    valid[0]=1
    ways=[0]*T
    ways[0]=1
    for mask in range(1,T):
        bit=mask&(-mask)
        i=bit.bit_length()-1
        state[mask]=tuple(a+b for a,b in zip(state[mask^bit],mm[i]))
        valid[mask]=int(min(state[mask])>=0)
        if valid[mask]:
            z=mask
            while z:
                bit=z&(-z)
                ways[mask]+=ways[mask^bit]
                z^=bit
    return ways[-1],sum(valid)

full=factorial(15)
assert census(eps_all)==(full,T)
mid1=eps_max*(phase[0]+phase[1])/2
mid2=eps_max*(phase[1]+phase[2])/2
assert census(mid1)==(full-factorial(5)*factorial(10),T-1)
assert census(mid2)==(
    full-factorial(5)*factorial(10)-
    (factorial(6)-factorial(5))*factorial(9),T-2)
assert census(eps_max)==(3514190816,7109)

print("FROZEN_PRIOR_R5_COMMIT 435e77af0d180eac32bd1f9c4c464bc4010b7551")
print("ATOM_COUNT",len(M),"DYNAMIC_COORDINATES",len(X))
print("MAXIMAL_NONNEGATIVE_RAY_EPS",eps_max)
print("ALL_PERMUTATIONS_FEASIBLE_THROUGH_INCLUSIVE",eps_all)
print("BOTTLENECK_COORDINATE",V[kcrit],"MAX_NEGATIVE_MOVE",negative_budget[kcrit])
print("BOTTLENECK_SUBSET",critical_atoms)
print("ALL_15_FACTORIAL_PERMUTATIONS",full)
for n in range(3):
    q=phase[n]
    mask,coord=thresholds[q][0]
    print("CRITICAL_EPSILON",n+1,eps_max*q,
          "SUBSET_MASK",mask,"COORDINATE",V[coord])
print("FIRST_OPEN_PHASE_ORDERS",census(mid1)[0],
      "ADMISSIBLE_SUBSETS",census(mid1)[1])
print("SECOND_OPEN_PHASE_ORDERS",census(mid2)[0],
      "ADMISSIBLE_SUBSETS",census(mid2)[1])
print("MID_RAY_ORDERS",census(eps_max/2))
print("THREE_QUARTERS_RAY_ORDERS",census(3*eps_max/4))
print("ENDPOINT_ORDERS",census(eps_max))
print("PASS_R5_EXACT_ALL_ORDER_THRESHOLD_FIRST_TWO_PHASES")
