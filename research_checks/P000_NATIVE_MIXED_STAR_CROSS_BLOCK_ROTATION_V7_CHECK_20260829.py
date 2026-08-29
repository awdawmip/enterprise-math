#!/usr/bin/env python3
"""Deterministic obstruction checker for P000 native mixed-star / cross-block rotation V7.

This checker intentionally separates:
(1) frozen native/clone-product transformation grammar, and
(2) FCC/K4 observation readout.
It proves that J_B is a valid carrier observation but is not generated as a
native Cell by the current pure-block grammar, and that the desired b-axis
permutation is outside even the generous block/whole-factor automorphism
envelope W=(S3 x S3) semidirect C2.
"""
from itertools import combinations, permutations, product

IA = frozenset((1,2,3))
IB = frozenset((4,5,6))
JB = frozenset((1,4,5))
JC = frozenset((2,4,6))
JD = frozenset((3,5,6))

# ---- Native constructor inventory frozen by prior P000 returns ----
# A native Cell constructor is available only blockwise. Addresses are arbitrary
# boundary-base triples r=(a,b,c), min(r)=0; address changes do not alter block type.
def is_base(r):
    return len(r)==3 and min(r)==0 and all(isinstance(x,int) and x>=0 for x in r)

def native_cell(block, r):
    assert block in ("A","B") and is_base(r)
    return IA if block=="A" else IB

# Positive controls at multiple addresses: every currently constructible Cell is pure.
for r in ((0,0,0),(0,2,7),(5,0,1),(3,4,0)):
    assert native_cell("A",r)==IA
    assert native_cell("B",r)==IB

# No current constructor has codomain "mixed native Cell".
NATIVE_CELL_AXIS_SETS = {IA,IB}
assert JB not in NATIVE_CELL_AXIS_SETS
assert JC not in NATIVE_CELL_AXIS_SETS
assert JD not in NATIVE_CELL_AXIS_SETS

# ---- FCC/K4 observation readout: mixed stars are real observations ----
V=("A","B","C","D")
E=tuple("".join(x) for x in combinations(V,2))
B={1:"AB",2:"AC",3:"AD",4:"BC",5:"BD",6:"CD"}
ST={v:frozenset(e for e in E if v in e) for v in V}
J={"A":IA,"B":JB,"C":JC,"D":JD}
assert {v:frozenset(B[i] for i in J[v]) for v in V}==ST
assert all(len(ST[x]&ST[y])==1 for x,y in combinations(V,2))
# Critical no-quotient regression: carrier validity does not change native typing.
assert frozenset(B[i] for i in JB)==ST["B"] and JB not in NATIVE_CELL_AXIS_SETS

# ---- Current native/clone-product transform envelope ----
# Allow more than the known G0: arbitrary S3 inside each block plus optional whole
# factor swap. If desired b is absent from this 72-element envelope, it cannot be
# synthesized by the extant blockwise / whole-factor grammar.
S3=list(permutations(range(3)))
W=set()
for p in S3:
    for q in S3:
        W.add(tuple(list(p)+[3+x for x in q]))
        W.add(tuple([3+x for x in p]+list(q)))
assert len(W)==72

# Desired b: axis action (E2 E4)(E3 E5), E1,E6 fixed.
B_NATIVE_TARGET=(0,3,4,1,2,5)
assert B_NATIVE_TARGET not in W
assert tuple(B_NATIVE_TARGET[i] for i in B_NATIVE_TARGET)==tuple(range(6))  # b^2=1
assert frozenset(B_NATIVE_TARGET[i-1]+1 for i in IA)==JB

# Positive controls: within-block and whole-factor maps are in W.
A_CYCLE=(1,2,0,3,4,5)
WHOLE_SWAP=(3,4,5,0,1,2)
assert A_CYCLE in W and WHOLE_SWAP in W

# Overlap/gluing consequence: readout says JA and JB share E1, but a native
# overlap law cannot be formed because JB lacks native Cell type.
assert IA & JB == frozenset((1,))
def native_overlap(x,y):
    if x not in NATIVE_CELL_AXIS_SETS or y not in NATIVE_CELL_AXIS_SETS:
        raise TypeError("mixed observation is not a native Cell")
    return x & y
try:
    native_overlap(IA,JB)
    raise AssertionError("JB incorrectly accepted as native Cell")
except TypeError:
    pass

# A cross-block full-state b lift cannot be type-checked in the frozen grammar:
# its axis action is outside W before payload/support/inverse checks can even begin.
def typecheck_native_transform(axis_perm):
    if axis_perm not in W:
        raise TypeError("axis action outside blockwise/whole-factor native envelope")
    return True
try:
    typecheck_native_transform(B_NATIVE_TARGET)
    raise AssertionError("cross-block b incorrectly accepted")
except TypeError:
    pass

# ---- Frozen carrier regressions; not used to define native motion ----
# Physical S4 edge actions on the six K4 edges.
def ce(a,b): return "".join(sorted((a,b)))
def edge_action(p):
    m=dict(zip(V,p))
    return tuple(E.index(ce(m[e[0]],m[e[1]])) for e in E)
CA={edge_action(p) for p in permutations(V)}
assert len(CA)==24
RHO=WHOLE_SWAP
assert RHO not in CA  # old whole-factor C2 is not a physical carrier S4 action.

# The carrier b edge action is exactly the desired six-axis permutation and is
# outside W: readout automorphism exists, native lift does not.
p_b=("B","A","C","D")
EB=edge_action(p_b)
assert EB==B_NATIVE_TARGET and EB not in W and EB in CA

# Split S4xC2 regression in the symmetric all-negative gauge: all S4 actions fix
# the edge-sign representative, while independent deck flip commutes.
Q0={e:-1 for e in E}
for p in permutations(V):
    m=dict(zip(V,p))
    acted={ce(m[e[0]],m[e[1]]):s for e,s in Q0.items()}
    assert acted==Q0
def deck(v,s): return (v,-s)
def lift(p,x):
    m=dict(zip(V,p)); v,s=x
    return (m[v],s)
for p in permutations(V):
    for x in product(V,(-1,1)):
        assert lift(p,deck(*x))==deck(*lift(p,x))

# Exact minimal repair interface: it is new native structure, not a conclusion.
MISSING_PRIMITIVES={
    "mixed_cell_constructor":"mu_r: Axis_A x Axis_B x Axis_B -> Cell_mixed",
    "cross_block_transform":"R_b_tilde: FullState -> FullState with axis action (2 4)(3 5)",
}
assert len(MISSING_PRIMITIVES)==2

print("PASS")
print("carrier_JB_valid=True; native_JB_constructible=False")
print("native_transform_envelope_order=72; desired_b_in_envelope=False")
print("desired_b_squared=identity; carrier_b_exists=True; native_b_lift_typechecks=False")
print("overlap_JA_JB_readout={1}; native_overlap=UNDEFINED")
print("minimal_obstruction=MIXED_SLICE_RELATION_MISSING + NO_AXIS_REFINED_CROSS_BLOCK_STATE_TRANSFORM")
print("carrier_split_S4xC2_regression=True; no_quotient_regression=True")
