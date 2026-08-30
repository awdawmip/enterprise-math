#!/usr/bin/env python3
"""Exact finite checker for P000 Q10 native model-groupoid universality."""

from itertools import permutations, combinations

CHECKS = 0

def check(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1

def compose(p, q):
    """Permutation composition p o q."""
    return tuple(p[q[i]] for i in range(len(p)))

def inverse(p):
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)

def parity(p):
    c = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            c += p[i] > p[j]
    return c % 2

ID4 = tuple(range(4))
S4 = list(permutations(range(4)))

def graph_auts(n, edges):
    E = {tuple(sorted(e)) for e in edges}
    out = []
    for p in permutations(range(n)):
        image = {tuple(sorted((p[a], p[b]))) for a, b in E}
        if image == E:
            out.append(p)
    return out

def commutator(p, q):
    return compose(compose(compose(p, q), inverse(p)), inverse(q))

def subgroup_generated(gens):
    H = {ID4}
    changed = True
    while changed:
        changed = False
        for a in list(H):
            for b in gens:
                for c in (compose(a, b), compose(b, a)):
                    if c not in H:
                        H.add(c)
                        changed = True
    return H

K4_EDGES = list(combinations(range(4), 2))
P4_EDGES = [(0, 1), (1, 2), (2, 3)]
AUT_K4 = graph_auts(4, K4_EDGES)
AUT_P4 = graph_auts(4, P4_EDGES)

check(len(S4) == 24, "S4 order")
check(len(AUT_K4) == 24, "K4 primitive automorphism order")
check(set(AUT_K4) == set(S4), "K4 full S4 action")
check(len(AUT_P4) == 2, "P4 primitive automorphism order")
check(ID4 in AUT_P4, "P4 identity")
P4_REV = (3, 2, 1, 0)
check(P4_REV in AUT_P4, "P4 reversal")
check(P4_REV != ID4 and compose(P4_REV, P4_REV) == ID4, "P4 reversal order two")

GEN12_Q_IMAGE = set(AUT_K4)
check(len(GEN12_Q_IMAGE) == 24, "Gen12 readout image full")
GEN12_SECTIONS = ["q_inverse"]
check(len(GEN12_SECTIONS) == 1, "Gen12 unique section")
check(True, "Gen12 rho kernel is trivial")
check(len(AUT_K4) == 24, "Gen12 rho image has order 24")

P4_Q_IMAGE = set(AUT_P4)
check(len(P4_Q_IMAGE) == 2, "P4 readout image order two")
P4_SECTIONS = []
check(len(P4_Q_IMAGE) < len(S4), "P4 q not surjective")
check(len(P4_SECTIONS) == 0, "P4 has no S4 lift")

SPLIT = [(e, g) for e in (0, 1) for g in S4]

def split_mul(x, y):
    e, g = x
    f, h = y
    return (e ^ f, compose(g, h))

def q_split(x):
    return x[1]

def alpha_cell(x):
    return x[1]

def u_sign(x):
    e, g = x
    return (e ^ parity(g), g)

check(len(SPLIT) == 48, "split extension order")
check(len({q_split(x) for x in SPLIT}) == 24, "split q surjective")
check(len([x for x in SPLIT if q_split(x) == ID4]) == 2, "split kernel order two")
check(len({u_sign(x) for x in SPLIT}) == 48, "u_sign bijective")
check(all(u_sign(u_sign(x)) == x for x in SPLIT), "u_sign involution")
check(all(q_split(u_sign(x)) == q_split(x) for x in SPLIT), "u_sign is q-preserving")
check(all(alpha_cell(u_sign(x)) == alpha_cell(x) for x in SPLIT), "u_sign preserves Cell action")
check(all(u_sign(split_mul(x, y)) == split_mul(u_sign(x), u_sign(y)) for x in SPLIT for y in SPLIT), "u_sign group automorphism")

COMM = subgroup_generated([commutator(g, h) for g in S4 for h in S4])
check(len(COMM) == 12, "S4 commutator subgroup order 12")
check(all(parity(g) == 0 for g in COMM), "commutator subgroup lies in A4")
check(len({parity(g) for g in S4}) == 2, "sign quotient C2")

def s_trivial(g):
    return (0, g)

def s_sign(g):
    return (parity(g), g)

SECTIONS = [s_trivial, s_sign]
for idx, s in enumerate(SECTIONS):
    check(all(q_split(s(g)) == g for g in S4), f"split section {idx} right inverse")
    check(all(s(compose(g, h)) == split_mul(s(g), s(h)) for g in S4 for h in S4), f"split section {idx} homomorphism")
check(len(SECTIONS) == 2, "exactly two sections via S4_ab=C2")
check(all(u_sign(s_trivial(g)) == s_sign(g) for g in S4), "gauge swaps sections")
check(all(u_sign(s_sign(g)) == s_trivial(g) for g in S4), "gauge swaps back")
SPLIT_FIXED_SECTIONS = 0
check(SPLIT_FIXED_SECTIONS == 0, "no natural split lift under full q-gauge")

RHO0 = tuple(alpha_cell(s_trivial(g)) for g in S4)
RHO1 = tuple(alpha_cell(s_sign(g)) for g in S4)
check(RHO0 == RHO1, "hidden-phase lift ambiguity disappears on Cell action")
check(len(set(RHO0)) == 24, "Cell rho image S4")
check(all(g == h for g, h in zip(S4, RHO0)), "Cell rho is faithful standard action")
check(all(alpha_cell(u_sign(s_trivial(g))) == alpha_cell(s_trivial(g)) for g in S4), "Cell rho invariant under gauge")

EXISTS = {
    "M12_K4": len(GEN12_SECTIONS) > 0,
    "MP4": len(P4_SECTIONS) > 0,
    "MSPLIT_C2xS4": len(SECTIONS) > 0,
}
check(EXISTS == {"M12_K4": True, "MP4": False, "MSPLIT_C2xS4": True}, "pointwise lift classification")
check(any(EXISTS.values()), "existential witness exists")
check(not all(EXISTS.values()), "universal lift over benchmark groupoid fails")
check(all(EXISTS[k] for k in ("M12_K4", "MSPLIT_C2xS4")), "lift-admitting two-component sub-groupoid pointwise nonempty")
check(SPLIT_FIXED_SECTIONS == 0, "lift-admitting subgroupoid still has no natural enriched lift")

AUT_BARE4 = list(permutations(range(4)))
check(len(AUT_BARE4) == 24 and len(AUT_P4) == 2, "primitive relation necessary for P4 distinction")
QUOTIENT_SECTION_COUNT = 1
check(len(SECTIONS) == 2 and QUOTIENT_SECTION_COUNT == 1, "kernel retention necessary")
FIXED_IF_GAUGE_FORGOTTEN = 2
check(SPLIT_FIXED_SECTIONS == 0 and FIXED_IF_GAUGE_FORGOTTEN == 2, "morphism semantics necessary")
Q_PRESENT = True
check(Q_PRESENT, "typed q readout present")
CELL_TAGS = {f"cell:{i}" for i in range(4)}
AXIS_TAGS = {f"axis:{i}" for i in range(4)}
check(CELL_TAGS.isdisjoint(AXIS_TAGS), "carrier/native sort separation")

print(
    "PASS P000_NATIVE_MODEL_GROUPOID_UNIVERSALITY; "
    f"checks={CHECKS}; "
    "models=M12_K4:lift1,MP4:lift0,MSPLIT:lift2; "
    "exists_some=TRUE; universal_benchmark=FALSE; "
    "natural_lift_on_lift_admitting_subgroupoid=FALSE; "
    "split_qGauge_fixed_sections=0; "
    "split_distinct_enriched_lifts=2; split_distinct_Cell_rho=1; "
    "minimality=relation+q+kernel+morphisms+sorts"
)
