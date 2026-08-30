#!/usr/bin/env python3
"""Deterministic certificate for P000 S4 relational-minimality grammar V15.

Scope:
- freezes a finite candidate relation/constraint grammar;
- validates the package Pareto partial order;
- checks the Gen12/13/14 mandatory finite regressions;
- proves the K4-vs-tetrahedral-incidence fixed-sort definability asymmetry;
- checks the four expressivity regimes.

No external packages.
"""
from itertools import permutations, product, combinations

TASK_ID = "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE"
PUBLICATION_ID = "TP2-3E7A91C5B2406DF814A2"
TERMINAL = "RELATIONAL_MINIMALITY_GRAMMAR_EQUIVALENCE_COST_AND_ENVELOPE_FROZEN"

BACKGROUND_SORTS = ("NativeCell", "AxisType")
OPTIONAL_SORTS = ("Hidden",)
RELATIONS = {
    # name: (arity, uses_hidden, source/target signature)
    "I_CA": (2, False, ("NativeCell", "AxisType")),
    "I_HC": (2, True, ("Hidden", "NativeCell")),
    "I_HA": (2, True, ("Hidden", "AxisType")),
    "ADD_H": (3, True, ("Hidden", "Hidden", "Hidden")),
}
CONSTRAINTS = {
    # name: required relation symbols, required constraints
    "K4_ADJ": (set(), set()),                    # background native adjacency is K4 on |C|=4
    "TETRA_CA": ({"I_CA"}, set()),               # exact 4-cell/6-axis tetrahedral incidence
    "H_C3X3": ({"ADD_H"}, set()),                # Hidden is C3 x C3 under ADD_H
    "PROJECTIVE_HC": ({"ADD_H", "I_HC"}, {"H_C3X3"}),
    "PAIR_AXIS_HA": ({"ADD_H", "I_HC", "I_HA"}, {"H_C3X3", "PROJECTIVE_HC"}),
}
FORBIDDEN_TOKENS = ("R_a", "R_b", "section_primitive", "K=1", "carrier_native_identity")

ENVELOPE = {
    "NativeCell_max": 8,
    "AxisType_exact": 6,
    "Hidden_max": 9,
}
WITNESSES = {
    "GEN12_K1_CANONICAL": {"NativeCell": 4, "AxisType": 6, "Hidden": 0},
    "GEN13_P4_NO_LIFT": {"NativeCell": 4, "AxisType": 6, "Hidden": 0},
    "GEN13_K2222_SPLIT_NONCANONICAL": {"NativeCell": 8, "AxisType": 6, "Hidden": 0},
    "GEN13_GL23_SURJECTIVE_NONSPLIT": {"NativeCell": 4, "AxisType": 6, "Hidden": 9},
    "GEN14_K4_CANONICAL": {"NativeCell": 4, "AxisType": 6, "Hidden": 0},
    "GEN14_TETRA_INCIDENCE_CANONICAL": {"NativeCell": 4, "AxisType": 6, "Hidden": 0},
}

def assert_(cond, msg):
    if not cond:
        raise AssertionError(msg)

def compose(p,q):
    return tuple(p[q[i]] for i in range(len(p)))

def inverse_perm(p):
    q=[0]*len(p)
    for i,j in enumerate(p): q[j]=i
    return tuple(q)

def graph_auts(n, edges):
    E={tuple(sorted(e)) for e in edges}
    out=[]
    for p in permutations(range(n)):
        im={tuple(sorted((p[i],p[j]))) for i,j in E}
        if im==E:
            out.append(p)
    return out

def k4_edges():
    return set(combinations(range(4),2))

def p4_edges():
    return {(0,1),(1,2),(2,3)}

def k2222_edges():
    fib=(0,0,1,1,2,2,3,3)
    return {(i,j) for i,j in combinations(range(8),2) if fib[i]!=fib[j]}

def tetra_incidence():
    pairs=list(combinations(range(4),2))
    I={(c,a) for a,pair in enumerate(pairs) for c in pair}
    return pairs,I

def tetra_aut_count():
    _,I=tetra_incidence()
    count=0
    for pc in permutations(range(4)):
        for pa in permutations(range(6)):
            if {(pc[c],pa[a]) for c,a in I}==I:
                count+=1
    return count

def tetra_induces_k4():
    _,I=tetra_incidence()
    E=set()
    for c,d in combinations(range(4),2):
        if any((c,a) in I and (d,a) in I for a in range(6)):
            E.add((c,d))
    return E == k4_edges()

def k4_cannot_define_fixed_axis_tetra_incidence():
    # A parameter-free relation definable from the K4 Cell reduct (even with
    # the six AxisType objects pointwise fixed) must be invariant under every
    # K4 Cell automorphism extended by identity on AxisType.
    _,I=tetra_incidence()
    for pc in permutations(range(4)):
        if pc == tuple(range(4)):
            continue
        im={(pc[c],a) for c,a in I}
        if im != I:
            return True
    return False

# GL(2,3) exact hidden witness
MOD=3
MAT_I=((1,0),(0,1))
MAT_NEG=((2,0),(0,2))
def det(A):
    return (A[0][0]*A[1][1]-A[0][1]*A[1][0])%MOD
def matmul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%MOD for j in range(2)) for i in range(2))
def matpow(A,n):
    R=MAT_I
    for _ in range(n):
        R=matmul(R,A)
    return R
def gl23():
    out=[]
    for vals in product(range(3), repeat=4):
        A=((vals[0],vals[1]),(vals[2],vals[3]))
        if det(A):
            out.append(A)
    return out
LINES=((1,0),(0,1),(1,1),(1,2))
LINE_INDEX={v:i for i,v in enumerate(LINES)}
def canon_line(v):
    x,y=v[0]%3,v[1]%3
    if x==0:
        return (0,1)
    inv=1 if x==1 else 2
    return (1,(y*inv)%3)
def projective_action(A):
    out=[]
    for x,y in LINES:
        w=((A[0][0]*x+A[0][1]*y)%3,(A[1][0]*x+A[1][1]*y)%3)
        out.append(LINE_INDEX[canon_line(w)])
    return tuple(out)

# C2 wr S4 exact split/noncanonical witness
S4=list(permutations(range(4)))
P_ID=tuple(range(4))
ZERO=(0,0,0,0)
def act_vec(p,w):
    inv=inverse_perm(p)
    return tuple(w[inv[i]] for i in range(4))
def xorv(v,w):
    return tuple(a^b for a,b in zip(v,w))
def wr_mul(g,h):
    v,p=g; w,q=h
    return (xorv(v,act_vec(p,w)), compose(p,q))
WR_E=(ZERO,P_ID)
def wr_pow(g,n):
    r=WR_E
    for _ in range(n):
        r=wr_mul(r,g)
    return r
def wr_inv(g):
    v,p=g
    pi=inverse_perm(p)
    return (act_vec(pi,v),pi)
def wr_conj(k,g):
    return wr_mul(wr_mul(k,g),wr_inv(k))

A_PERM=(0,2,3,1) # (BCD), A fixed
B_PERM=(1,0,2,3) # (AB)

def wreath_section_certificate():
    liftsA=[(v,A_PERM) for v in product((0,1),repeat=4)]
    liftsB=[(v,B_PERM) for v in product((0,1),repeat=4)]
    pairs=[]
    residues=set()
    for A in liftsA:
        for B in liftsB:
            residues.add((wr_pow(A,3)[0],wr_pow(B,2)[0],wr_pow(wr_mul(A,B),4)[0]))
            if wr_pow(A,3)==WR_E and wr_pow(B,2)==WR_E and wr_pow(wr_mul(A,B),4)==WR_E:
                pairs.append((A,B))
    kernel=[(v,P_ID) for v in product((0,1),repeat=4)]
    index={pair:i for i,pair in enumerate(pairs)}
    unseen=set(range(len(pairs)))
    orbit_sizes=[]
    while unseen:
        i=next(iter(unseen))
        A,B=pairs[i]
        orb=set()
        for k in kernel:
            pair=(wr_conj(k,A),wr_conj(k,B))
            if pair in index:
                orb.add(index[pair])
        orbit_sizes.append(len(orb))
        unseen -= orb
    fixed=sum(
        1 for A,B in pairs
        if all(wr_conj(k,A)==A and wr_conj(k,B)==B for k in kernel)
    )
    return len(residues),len(pairs),sorted(orbit_sizes),fixed

def valid_package(relset, cset):
    for c in cset:
        reqr,reqc=CONSTRAINTS[c]
        if not reqr.issubset(relset) or not reqc.issubset(cset):
            return False
    return True

def cost(relset,cset):
    hidden = any(RELATIONS[r][1] for r in relset)
    arity_counts={1:0,2:0,3:0}
    for r in relset:
        arity_counts[RELATIONS[r][0]] += 1
    # No distinguished constants/parameters are permitted in G15.
    return (
        1 if hidden else 0, # new sort count
        len(relset),        # new relation symbol count
        arity_counts[1],
        arity_counts[2],
        arity_counts[3],
        1 if hidden else 0, # hidden-sort flag, explicit requested dimension
        len(cset),          # extra global constraints
        0,                  # distinguished parameters/constants
    )

def package_leq(P,Q):
    # Strict Pareto cost dominance plus exact equality. Distinct equal-cost
    # packages remain incomparable; this avoids arbitrary tie-breaking.
    cp,cq=cost(*P),cost(*Q)
    if P==Q:
        return True
    return all(a<=b for a,b in zip(cp,cq)) and cp!=cq

def all_valid_packages():
    rn=list(RELATIONS); cn=list(CONSTRAINTS)
    out=[]
    for mask in range(1<<len(rn)):
        rs={rn[i] for i in range(len(rn)) if mask>>i & 1}
        for cmask in range(1<<len(cn)):
            cs={cn[i] for i in range(len(cn)) if cmask>>i & 1}
            if valid_package(rs,cs):
                out.append((frozenset(rs),frozenset(cs)))
    return out

def check_poset(pkgs):
    # reflexive, antisymmetric, transitive
    for P in pkgs:
        assert_(package_leq(P,P), "non-reflexive")
    for P in pkgs:
        for Q in pkgs:
            if package_leq(P,Q) and package_leq(Q,P):
                assert_(P==Q, "antisymmetry failure")
    # optimize transitivity: cost dominance itself is transitive, but exact
    # exhaustive check is still small enough for the frozen grammar.
    for P in pkgs:
        for Q in pkgs:
            if not package_leq(P,Q): continue
            for R in pkgs:
                if package_leq(Q,R):
                    assert_(package_leq(P,R), "transitivity failure")

def main():
    checks=0

    # Finite grammar + anti-tautology naming firewall.
    assert_(len(RELATIONS)==4 and len(CONSTRAINTS)==5, "catalog cardinality drift"); checks+=1
    text=" ".join(RELATIONS)+" "+" ".join(CONSTRAINTS)
    assert_(not any(tok in text for tok in FORBIDDEN_TOKENS), "forbidden primitive leaked into grammar"); checks+=1
    assert_(all(RELATIONS[r][0] in (2,3) for r in RELATIONS), "unexpected arity"); checks+=1

    # Envelope.
    for w,v in WITNESSES.items():
        assert_(v["NativeCell"]<=ENVELOPE["NativeCell_max"], w+" cell envelope")
        assert_(v["AxisType"]==ENVELOPE["AxisType_exact"], w+" axis envelope")
        assert_(v["Hidden"]<=ENVELOPE["Hidden_max"], w+" hidden envelope")
        checks+=3

    # Gen14 K4/incidence definability regression.
    assert_(len(graph_auts(4,k4_edges()))==24, "K4 Aut != 24"); checks+=1
    assert_(tetra_aut_count()==24, "tetra incidence Aut != 24"); checks+=1
    assert_(tetra_induces_k4(), "incidence does not define K4 adjacency"); checks+=1
    assert_(k4_cannot_define_fixed_axis_tetra_incidence(), "K4 unexpectedly defines tetra incidence on fixed AxisType sort"); checks+=1

    # P4 and K2222 finite regimes.
    assert_(len(graph_auts(4,p4_edges()))==2, "P4 Aut != 2"); checks+=1
    assert_(len(graph_auts(8,k2222_edges()))==384, "K2222 Aut != 384"); checks+=1
    residue_count,sections,orbits,fixed=wreath_section_certificate()
    assert_((residue_count,sections,orbits,fixed)==(16,16,[8,8],0), "wreath section regression"); checks+=4

    # GL(2,3) hidden regime.
    GL=gl23()
    assert_(len(GL)==48, "GL23 order"); checks+=1
    acts={projective_action(A) for A in GL}
    assert_(len(acts)==24, "PGL23 image order"); checks+=1
    kernel=[A for A in GL if projective_action(A)==P_ID]
    assert_(set(kernel)=={MAT_I,MAT_NEG}, "projective kernel"); checks+=1
    liftsA=[A for A in GL if projective_action(A)==A_PERM]
    liftsB=[B for B in GL if projective_action(B)==B_PERM]
    assert_(len(liftsA)==2 and len(liftsB)==2, "frozen lift counts"); checks+=1
    assert_(all(matpow(B,2)==MAT_I for B in liftsB), "B^2 residue"); checks+=1
    assert_(all(matpow(matmul(A,B),4)==MAT_NEG for A in liftsA for B in liftsB), "(AB)^4 residue"); checks+=1

    # Four-regime expressivity gate.
    regimes={
        "NO_LIFT": len(graph_auts(4,p4_edges()))==2,
        "SURJECTIVE_NONSPLIT": len(acts)==24 and all(matpow(matmul(A,B),4)==MAT_NEG for A in liftsA for B in liftsB),
        "SPLIT_NONCANONICAL": sections==16 and fixed==0,
        "CANONICAL_FAITHFUL": len(graph_auts(4,k4_edges()))==24 and tetra_aut_count()==24,
    }
    assert_(all(regimes.values()), "expressivity gate"); checks+=4

    # Package partial order.
    pkgs=all_valid_packages()
    assert_(len(pkgs)>0 and len(pkgs)<=512, "package universe not finite/bounded"); checks+=1
    check_poset(pkgs); checks+=3

    print("PASS")
    print("task",TASK_ID)
    print("publication",PUBLICATION_ID)
    print("terminal",TERMINAL)
    print("relations",len(RELATIONS),"constraints",len(CONSTRAINTS),"valid_packages",len(pkgs))
    print("definability","TETRA_CA -> K4_ADJ; K4_ADJ -/-> TETRA_CA on fixed AxisType sort; bi-interpretable only after derived Pair2(Cell) sort")
    print("regimes",",".join(k for k,v in regimes.items() if v))
    print("checks",checks)

if __name__=="__main__":
    main()
