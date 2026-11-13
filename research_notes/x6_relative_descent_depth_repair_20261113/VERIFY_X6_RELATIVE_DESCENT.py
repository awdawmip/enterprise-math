#!/usr/bin/env python3
"""Reproduce exact quotient descent and depth repair for frozen X6 signed triads.
Frozen science: a72226e2430ffa4786321ac86e7f0c599d5f0389.
Runs with Python standard library; no external numerical libraries required.
"""
import itertools, json
IDENTITY = tuple(range(1,7))
D = (1,1,1,1,1,1)

def compose(g, h):
    """Signed images of basis vectors: (g o h)(e_i)."""
    return tuple((1 if a>0 else -1) * g[abs(a)-1] for a in h)

def group(generators):
    seen={IDENTITY}
    frontier=[IDENTITY]
    for x in frontier:
        for y in generators:
            z=compose(x,y)
            if z not in seen:
                seen.add(z)
                frontier.append(z)
    return seen

def triad(i,j,k,l=None):
    basis=list(IDENTITY)
    basis[i]=j+1
    basis[j]=k+1
    basis[k]=-(i+1)
    if l is not None:
        assert l not in (i,j,k)
        basis[l]=-(l+1)
    return tuple(basis)

def apply(g,x):
    out=[0]*6
    for i,a in enumerate(g):
        out[abs(a)-1]=(1 if a>0 else -1)*x[i]
    return tuple(out)

def canon(x):
    h=min(x)
    return tuple(v-h for v in x)

def safe(g):
    return all(a>0 for a in g) or all(a<0 for a in g)

triads=list(itertools.combinations(range(6),3))
GT=group([triad(*t) for t in triads])
GU=group([triad(*t,l) for t in triads for l in range(6) if l not in t])
assert (len(GT),len(GU))==(23040,11520)
HT={g for g in GT if safe(g)}
HU={g for g in GU if safe(g)}
assert len(HT)==len(HU)==720
assert HT==HU

# Verify that every quotient-safe action is faithful.
for g in HT:
    if all(canon(apply(g,tuple(1 if i==j else 0 for i in range(6)))) ==
           canon(tuple(1 if i==j else 0 for i in range(6))) for j in range(6)):
        assert g==IDENTITY

# Cross-check exact conjugate action on the (relative,common-depth) representation.
test_x=[(-4,2,-1,0,6,3),(0,0,0,0,0,0),D,(2,-3,0,-1,4,7)]
checked=0
for g in GT:
    eps=apply(g,D)
    assert (eps==D or eps==tuple(-1 for _ in D))==safe(g)
    for x in test_x:
        r,h=canon(x),min(x)
        gr=apply(g,r)
        repaired=tuple(a+h*b for a,b in zip(gr,eps))
        gx=apply(g,x)
        assert repaired==gx
        assert (canon(repaired),min(repaired))==(canon(gx),min(gx))
        checked+=1
assert checked==92160

# Endpoint descent at n=6, but all interior phases n=1..5 need depth.
for gen in (triad(0,1,2),triad(0,1,2,3)):
    x=IDENTITY
    for n in range(7):
        assert safe(x)==(n in (0,6)), (gen,n)
        x=compose(gen,x)
    assert x==gen

# Explicit depth-sensitive witness.
w=triad(0,1,2)
assert canon(apply(w,(0,0,0,0,0,0)))==(0,0,0,0,0,0)
assert canon(apply(w,D))==(0,2,2,2,2,2)

print(json.dumps({
    "status":"PASS_EXACT_X6_RELATIVE_QUOTIENT_AND_DEPTH",
    "frozen_source":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
    "group_orders":{"uncompensated":len(GT),"compensated":len(GU)},
    "relative_safe_subgroup_order":len(HT),
    "relative_safe_subgroups_equal":HT==HU,
    "exact_depth_repair_transitions":checked,
    "selected_6_phase_trace_pass":True,
    "depth_witness":"0 and D agree initially; signed triad sends D to a mixed-sign vector."
},indent=2))
