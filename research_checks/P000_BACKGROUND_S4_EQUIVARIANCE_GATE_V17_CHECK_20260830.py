from __future__ import annotations
import hashlib, itertools, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1] if "__file__" in globals() else pathlib.Path(".")
EXPECTED_G15_SHA256 = "50ef864f0713d1f19ddf918dae2486a05a7e1d52bf538f1603b2d1c6c655281e"

V = ("A","B","C","D")
E = ("E1","E2","E3","E4","E5","E6")
EDGE = {
    "E1": ("A","B"),
    "E2": ("A","C"),
    "E3": ("A","D"),
    "E4": ("B","C"),
    "E5": ("B","D"),
    "E6": ("C","D"),
}
EDGE_OF = {tuple(sorted(v)): k for k,v in EDGE.items()}

def vperm(images):
    return dict(zip(V, images))

def eaction(p):
    out={}
    for e,(u,v) in EDGE.items():
        out[e] = EDGE_OF[tuple(sorted((p[u],p[v])))]
    return out

S4 = [vperm(t) for t in itertools.permutations(V)]
EA = [eaction(p) for p in S4]
ID_E = {e:e for e in E}

def sig(p, elems):
    return tuple(p[x] for x in elems)

def comp(p,q, elems):
    return {x:p[q[x]] for x in elems}

def inv(p, elems):
    return {p[x]:x for x in elems}

def conj(p,h, elems=E):
    return comp(comp(p,h,elems), inv(p,elems), elems)

def is_group_index(indices):
    S={sig(EA[i],E) for i in indices}
    if sig(ID_E,E) not in S: return False
    for i in indices:
        for j in indices:
            if sig(comp(EA[i],EA[j],E),E) not in S:
                return False
    return True

def point_orbits(actions, elems):
    unseen=set(elems); out=[]
    for x in elems:
        if x not in unseen: continue
        o={a[x] for a in actions}
        unseen -= o
        out.append(frozenset(o))
    return tuple(out)

def pair_orbits(actions):
    pairs=[(x,y) for x in E for y in E]
    unseen=set(pairs); out=[]
    for p in pairs:
        if p not in unseen: continue
        o={(a[p[0]],a[p[1]]) for a in actions}
        unseen -= o
        out.append(frozenset(o))
    return tuple(out)

# carrier action regression
assert len({sig(a,E) for a in EA}) == 24
stab_e1 = [i for i,a in enumerate(EA) if a["E1"]=="E1"]
assert len(stab_e1) == 4 and is_group_index(stab_e1)

# exact generators a=(BCD), b=(AB)
aV={"A":"A","B":"C","C":"D","D":"B"}
bV={"A":"B","B":"A","C":"C","D":"D"}
aE=eaction(aV); bE=eaction(bV)
assert sig(aE,E)==("E2","E3","E1","E6","E4","E5")
assert sig(bE,E)==("E1","E4","E5","E2","E3","E6")

generated={sig(ID_E,E):ID_E}
front=[ID_E]
while front:
    x=front.pop()
    for g in (aE,bE):
        y=comp(g,x,E); s=sig(y,E)
        if s not in generated:
            generated[s]=y; front.append(y)
assert len(generated)==24

# PF10 compatibility: I/O vectors and conjugation action on M.
def vec_preserved(vec, act):
    return all(vec[E.index(act[e])] == vec[E.index(e)] for e in E)

def mat_preserved(M, act):
    idx={e:i for i,e in enumerate(E)}
    return all(M[idx[act[x]]][idx[act[y]]] == M[idx[x]][idx[y]] for x in E for y in E)

ones=(1,1,1,1,1,1)
e1=(1,0,0,0,0,0)
I6=tuple(tuple(1 if i==j else 0 for j in range(6)) for i in range(6))
pf10_e1=[i for i,a in enumerate(EA) if vec_preserved(e1,a) and mat_preserved(I6,a)]
pf10_sym=[i for i,a in enumerate(EA) if vec_preserved(ones,a) and mat_preserved(I6,a)]
assert len(pf10_e1)==4
assert set(pf10_e1)==set(stab_e1)
assert len(pf10_sym)==24

# Full local S4 invariants vs orbitwise equivariance under Cell stabilizer S3.
H_A=[i for i,p in enumerate(S4) if p["A"]=="A"]
Hacts=[EA[i] for i in H_A]
assert len(H_A)==6
assert sorted(len(o) for o in point_orbits(EA,E)) == [6]
assert sorted(len(o) for o in point_orbits(Hacts,E)) == [3,3]
assert len(pair_orbits(EA)) == 3
assert len(pair_orbits(Hacts)) == 8

# generator-only conditions: both generators suffice; each alone is strictly weaker.
v_a=(1,1,1,0,0,0)
v_b=(1,0,0,0,0,0)
assert vec_preserved(v_a,aE) and not vec_preserved(v_a,bE)
assert vec_preserved(v_b,bE) and not vec_preserved(v_b,aE)

# Independent connection countermodel on K4: nonidentity h=(E1 E6) on Cell edge AB=E1.
h=dict(ID_E); h["E1"]="E6"; h["E6"]="E1"
T={e:(h if e=="E1" else ID_E) for e in E}
def conn_ok(act):
    for cell_edge in E:
        mapped=act[cell_edge]
        if sig(T[mapped],E)!=sig(conj(act,T[cell_edge],E),E):
            return False
    return True
conn_compat=[i for i,a in enumerate(EA) if conn_ok(a)]
assert len(conn_compat)==4
assert set(conn_compat)==set(stab_e1)
assert is_group_index(conn_compat)
assert len(pf10_sym)==24 and len(conn_compat)==4

# Frame-induced connection automatic naturality with arbitrary local frames.
C=tuple(range(6))
frames={
    "A": {E[i]: C[i] for i in range(6)},
    "B": {E[i]: C[(i+1)%6] for i in range(6)},
    "D": {E[i]: C[(5-i)] for i in range(6)},
}
cperm=(0,2,4,1,3,5)
frames["C"]={E[i]:cperm[i] for i in range(6)}
def cinv(f): return {v:k for k,v in f.items()}
def channel_map_from_axis(f_to, axis_perm, f_from):
    fi=cinv(f_from)
    return {c: f_to[axis_perm[fi[c]]] for c in C}
def T_frame(x,y):
    fi=cinv(frames[x])
    return {c: frames[y][fi[c]] for c in C}
def composeC(p,q): return {c:p[q[c]] for c in C}
for idx,p in enumerate(S4):
    act=EA[idx]
    for x in V:
        pix=channel_map_from_axis(frames[p[x]], act, frames[x])
        for y in V:
            if x==y: continue
            piy=channel_map_from_axis(frames[p[y]], act, frames[y])
            left=composeC(T_frame(p[x],p[y]), pix)
            right=composeC(piy, T_frame(x,y))
            assert left==right

# Native adjacency structural regressions.
K4_edges={frozenset((u,v)) for u in V for v in V if u<v}
P4_edges={frozenset(x) for x in (("A","B"),("B","C"),("C","D"))}
def graph_auts(edges):
    out=[]
    for p in S4:
        ok=True
        for u in V:
            for v in V:
                if u>=v: continue
                before=frozenset((u,v)) in edges
                after=frozenset((p[u],p[v])) in edges
                if before!=after: ok=False; break
            if not ok: break
        if ok: out.append(p)
    return out
assert len(graph_auts(K4_edges))==24
assert len(graph_auts(P4_edges))==2

# Tetra Cell-Axis incidence automorphisms: vertex permutation uniquely determines edge action.
tetra_inc={(v,e) for e,(u,w) in EDGE.items() for v in (u,w)}
for idx,p in enumerate(S4):
    act=EA[idx]
    assert {(p[v],act[e]) for v,e in tetra_inc} == tetra_inc

# Global compatibility projection theorem can be strict.
def parity(p):
    t=[V.index(p[v]) for v in V]
    invs=sum(t[i]>t[j] for i in range(4) for j in range(i+1,4))
    return invs%2
G1={(0,sig(p,V)) for p in S4}
G2={(parity(p),sig(p,V)) for p in S4}
inter=G1&G2
assert len(G1)==24 and len(G2)==24 and len(inter)==12
assert {g for k,g in G1} == {sig(p,V) for p in S4}
assert {g for k,g in G2} == {sig(p,V) for p in S4}
assert len({g for k,g in inter})==12

# Fiber compatibility can be a coset/partial-domain set, not a subgroup.
A_to_B=[i for i,p in enumerate(S4) if p["A"]=="B"]
A_to_A=[i for i,p in enumerate(S4) if p["A"]=="A"]
assert len(A_to_B)==6 and len(A_to_A)==6
assert is_group_index(A_to_A)
assert sig(ID_E,E) not in {sig(EA[i],E) for i in A_to_B}

# Charged transparency gates and deletion tests.
G0=set(range(24))
assert set(pf10_sym)==G0
assert set(conn_compat)!=G0
assert len(set(pf10_e1)&G0)==4
assert len(set(conn_compat)&set(pf10_sym))==4

# Extended cost vectors.
k4_pf10=(0,0,0,0,0,0,2,0)
k4_pf10_conn=(0,0,0,0,0,0,3,0)
tetra_pf10=(0,1,0,1,0,0,2,0)
tetra_pf10_conn=(0,1,0,1,0,0,3,0)
def dominates(a,b):
    return all(x<=y for x,y in zip(a,b)) and a!=b
assert dominates(k4_pf10,tetra_pf10)
assert dominates(k4_pf10_conn,tetra_pf10_conn)

# Frozen source regressions when run from repository checkout.
g15 = ROOT / "research_artifacts/P000_S4_RELATIONAL_MINIMALITY_GRAMMAR_V15/GRAMMAR_CERTIFICATE.json"
if g15.exists():
    assert hashlib.sha256(g15.read_bytes()).hexdigest() == EXPECTED_G15_SHA256

expected_results = {
    "RR-8E63B078AE7DB4C7EFFD": "SUCCESS",
    "RR-E1438E73B8EDBA797602": "SUCCESS",
    "RR-6A14E9C27B53D8F104F2": "NEEDS_REVISION",
    "RR-9EBCAF7C1C66D8643C35": "SUCCESS",
    "RR-14CD1A7DE8CF7A30D49E": "SUCCESS",
}
for rr,status in expected_results.items():
    p=ROOT / f"research_result_records/RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE/{rr}.json"
    if p.exists():
        obj=json.loads(p.read_text())
        assert obj["result_id"]==rr
        assert obj["terminal_verdict"]==status

gen16_review = ROOT / "driver_reviews/P000_G15_PARETO_MINIMAL_S4_PACKAGES_V16_DRIVER_REVIEW_20260830.md"
if gen16_review.exists():
    review_text=gen16_review.read_text()
    assert "REVISION_REQUIRED" in review_text
    assert "G15_CURRENT_UNIVERSAL_POSITIVE_FRONTIERS = EMPTY_AT_DRIVER_AUDIT_STRENGTH" in review_text

inventory = ROOT / "research_artifacts/P000_BACKGROUND_S4_EQUIVARIANCE_GATE_V17/BACKGROUND_EQUIVARIANCE_CERTIFICATE.json"
if inventory.exists():
    cert=json.loads(inventory.read_text())
    assert cert["terminal_class"]=="MULTIPLE_INDEPENDENT_BACKGROUND_LEAK_SOURCES_AND_PARETO_GATES_CLASSIFIED"
    assert len(cert["background_inventory"])>=6
    assert cert["pf10_classification"]["gen16_countermodel"]["compatibility_order"]==4
    assert cert["connection_classification"]["independent_leak_witness"]["compatibility_order"]==4
    assert cert["minimality_and_frontier"]["frame_induced_connection_subclass"]["cost"] == [0,0,0,0,0,0,2,0]
    assert cert["minimality_and_frontier"]["independent_connection_subclass"]["cost"] == [0,0,0,0,0,0,3,0]

print("PASS P000_BACKGROUND_S4_EQUIVARIANCE_GATE_V17_CHECK")
print("carrier_s4_order=24")
print("pf10_e1_compat_order=4")
print("pf10_symmetric_compat_order=24")
print("local_full_s4_vector_orbits=1")
print("local_full_s4_matrix_pair_orbits=3")
print("tetra_cell_stabilizer_vector_orbits=2")
print("tetra_cell_stabilizer_matrix_pair_orbits=8")
print("connection_marked_edge_compat_order=4")
print("frame_induced_connection_naturality=automatic")
print("compat_projection_strict_witness_individual=24,24_joint=12")
print("partial_fiber_A_to_B_size=6_not_subgroup=true")
print("k4_pf10_gate_cost=(0,0,0,0,0,0,2,0)")
print("k4_pf10_connection_gate_cost=(0,0,0,0,0,0,3,0)")
print("terminal_class=MULTIPLE_INDEPENDENT_BACKGROUND_LEAK_SOURCES_AND_PARETO_GATES_CLASSIFIED")
