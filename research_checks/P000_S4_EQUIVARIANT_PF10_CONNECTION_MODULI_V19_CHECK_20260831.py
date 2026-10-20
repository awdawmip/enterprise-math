from __future__ import annotations
import itertools

V=("A","B","C","D")
EDGES=(("A","B"),("A","C"),("A","D"),("B","C"),("B","D"),("C","D"))
EDGE_IDX={tuple(sorted(e)):i for i,e in enumerate(EDGES)}
ID4=tuple(range(4))
ID6=tuple(range(6))
LABELS=tuple(f"E{i+1}" for i in range(6))

def comp(p,q):
    return tuple(p[q[i]] for i in range(len(p)))
def inv(p):
    out=[0]*len(p)
    for i,j in enumerate(p): out[j]=i
    return tuple(out)
def power(p,n):
    r=tuple(range(len(p)))
    for _ in range(n): r=comp(p,r)
    return r
def conj(p,h):
    return comp(comp(p,h),inv(p))
def ctype(p):
    seen=[False]*len(p); out=[]
    for i in range(len(p)):
        if not seen[i]:
            j=i; n=0
            while not seen[j]:
                seen[j]=True; n+=1; j=p[j]
            out.append(n)
    return tuple(sorted(out, reverse=True))
def cstr(p):
    seen=[False]*len(p); out=[]
    for i in range(len(p)):
        if not seen[i]:
            j=i; cyc=[]
            while not seen[j]:
                seen[j]=True; cyc.append(LABELS[j]); j=p[j]
            if len(cyc)>1: out.append("("+" ".join(cyc)+")")
    return "".join(out) or "id"

S4=list(itertools.permutations(range(4)))
S6=list(itertools.permutations(range(6)))

def edge_action(g):
    E=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
    out=[]
    for a,b in E:
        x,y=sorted((g[a],g[b]))
        out.append(E.index((x,y)))
    return tuple(out)
EA={g:edge_action(g) for g in S4}

a=(0,2,3,1)  # (BCD)
b=(1,0,2,3)  # (AB)
s=(0,1,3,2)  # (CD), oriented-edge stabilizer of A->B
aE,bE,sE=EA[a],EA[b],EA[s]
assert power(a,3)==ID4 and power(b,2)==ID4 and power(comp(a,b),4)==ID4
assert power(aE,3)==ID6 and power(bE,2)==ID6 and power(comp(aE,bE),4)==ID6
assert len(set(EA.values()))==24

# K4/P4 structural regression.
def graph_aut_count(edge_set):
    E={tuple(sorted(e)) for e in edge_set}
    count=0
    for g in S4:
        if {tuple(sorted((g[u],g[v]))) for u,v in E}==E:
            count+=1
    return count
assert graph_aut_count({(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)})==24
assert graph_aut_count({(0,1),(1,2),(2,3)})==2

# ---------- PF10 stabilizer-orbit moduli ----------
HA=[g for g in S4 if g[0]==0]
HAE=[EA[g] for g in HA]
def point_orbits(group,n):
    unseen=set(range(n)); out=[]
    while unseen:
        x=min(unseen)
        orb={p[x] for p in group}
        out.append(tuple(sorted(orb))); unseen-=orb
    return tuple(out)
def pair_orbits(group,n):
    unseen={(i,j) for i in range(n) for j in range(n)}; out=[]
    while unseen:
        x=min(unseen)
        orb={(p[x[0]],p[x[1]]) for p in group}
        out.append(tuple(sorted(orb))); unseen-=orb
    return tuple(out)

full_point_orbits=point_orbits(tuple(EA.values()),6)
full_pair_orbits=pair_orbits(tuple(EA.values()),6)
base_point_orbits=point_orbits(HAE,6)
base_pair_orbits=pair_orbits(HAE,6)
assert tuple(sorted(map(len,full_point_orbits)))==(6,)
assert tuple(sorted(map(len,full_pair_orbits)))==(6,6,24)
assert tuple(sorted(map(len,base_point_orbits)))==(3,3)
assert tuple(sorted(map(len,base_pair_orbits)))==(3,3,3,3,6,6,6,6)
assert len(base_point_orbits)==2 and len(base_pair_orbits)==8

point_orbit_index={}
for oi,orb in enumerate(base_point_orbits):
    for x in orb: point_orbit_index[x]=oi
pair_orbit_index={}
for oi,orb in enumerate(base_pair_orbits):
    for x in orb: pair_orbit_index[x]=oi

# Distinct values make all 2+2+8 base parameters visible.
I_A=tuple((1,2)[point_orbit_index[i]] for i in range(6))
O_A=tuple((3,4)[point_orbit_index[i]] for i in range(6))
M_A=tuple(tuple(10+pair_orbit_index[(i,j)] for j in range(6)) for i in range(6))

def push_vec(p,v):
    out=[None]*6
    for i in range(6): out[p[i]]=v[i]
    return tuple(out)
def push_mat(p,m):
    out=[[None]*6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            out[p[i]][p[j]]=m[i][j]
    return tuple(tuple(row) for row in out)

assert all(push_vec(h,I_A)==I_A and push_vec(h,O_A)==O_A and push_mat(h,M_A)==M_A for h in HAE)

# Unique structural transport from base Cell A.
transport_to={}
for x in range(4):
    transport_to[x]=next(g for g in S4 if g[0]==x)
PF={}
for x,g in transport_to.items():
    p=EA[g]
    PF[x]=(push_vec(p,I_A),push_vec(p,O_A),push_mat(p,M_A))

def pf_equivariant(g):
    p=EA[g]
    for x in range(4):
        gx=g[x]
        I,O,M=PF[x]
        if PF[gx]!=(push_vec(p,I),push_vec(p,O),push_mat(p,M)):
            return False
    return True
assert all(pf_equivariant(g) for g in S4)
assert len({PF[x] for x in range(4)})==4

# ---------- Connection raw solution set ----------
# T_AB must centralize the oriented-edge stabilizer sE and obey
# bE T_AB bE^-1 = T_AB^-1 from reverse-edge consistency plus equivariance.
CAND=[
    T for T in S6
    if comp(T,sE)==comp(sE,T) and conj(bE,T)==inv(T)
]
assert len(CAND)==12
EXPECTED_RAW={
    "id",
    "(E1 E6)",
    "(E2 E3)(E4 E5)",
    "(E2 E4)(E3 E5)",
    "(E2 E5)(E3 E4)",
    "(E1 E6)(E2 E3)(E4 E5)",
    "(E1 E6)(E2 E4)(E3 E5)",
    "(E1 E6)(E2 E5)(E3 E4)",
    "(E2 E4 E3 E5)",
    "(E2 E5 E3 E4)",
    "(E1 E6)(E2 E4 E3 E5)",
    "(E1 E6)(E2 E5 E3 E4)",
}
assert {cstr(T) for T in CAND}==EXPECTED_RAW

# Representative oriented-edge transport uniquely generates the global equivariant connection.
TRANS={}
for x in range(4):
    for y in range(4):
        if x!=y:
            TRANS[(x,y)]=next(g for g in S4 if g[0]==x and g[1]==y)

def connection(T):
    return {(x,y):conj(EA[g],T) for (x,y),g in TRANS.items()}

def conn_inverse(C):
    return all(C[(y,x)]==inv(C[(x,y)]) for x in range(4) for y in range(4) if x!=y)
def conn_nat(C,g):
    p=EA[g]
    return all(C[(g[x],g[y])]==conj(p,C[(x,y)])
               for x in range(4) for y in range(4) if x!=y)
for T in CAND:
    C=connection(T)
    assert conn_inverse(C)
    assert all(conn_nat(C,g) for g in S4)

# ---------- Accepted local S6 gauge quotient ----------
# Gen10 gauge: T_xy' = g_y T_xy g_x^-1. On connected K4, a spanning-tree
# gauge kills AB, AC, AD; gauge classes are the three rooted chord-loop
# holonomies modulo simultaneous conjugation by root g_A in S6.
BASIS=((0,1,2,0),(0,1,3,0),(0,2,3,0))
FOURS=((0,1,2,3,0),(0,1,3,2,0),(0,2,1,3,0))
def path_hol(C,path):
    h=ID6
    for x,y in zip(path,path[1:]):
        h=comp(C[(x,y)],h)
    return h
def triple(T):
    C=connection(T)
    return tuple(path_hol(C,p) for p in BASIS)
def triple_conj(tr,q):
    return tuple(conj(q,h) for h in tr)

unseen=set(CAND); GAUGE_ORBITS=[]
while unseen:
    T=next(iter(unseen))
    conj_triples={triple_conj(triple(T),q) for q in S6}
    orb={U for U in unseen if triple(U) in conj_triples}
    GAUGE_ORBITS.append(orb); unseen-=orb
assert len(GAUGE_ORBITS)==8
assert sorted(len(o) for o in GAUGE_ORBITS)==[1,1,1,1,2,2,2,2]

def signature(T):
    C=connection(T)
    tri={ctype(path_hol(C,p)) for p in BASIS}
    four={ctype(path_hol(C,p)) for p in FOURS}
    assert len(tri)==1 and len(four)==1
    return (next(iter(tri)),next(iter(four)))

sig_by_orbit=[]
for orb in GAUGE_ORBITS:
    sigs={signature(T) for T in orb}
    assert len(sigs)==1
    sig_by_orbit.append(next(iter(sigs)))
EXPECTED_SIGS={
    ((1,1,1,1,1,1),(1,1,1,1,1,1)),
    ((2,2,2),(1,1,1,1,1,1)),
    ((2,2,2),(3,3)),
    ((4,1,1),(3,3)),
    ((4,2),(3,3)),
    ((2,1,1,1,1),(3,1,1,1)),
    ((2,2,1,1),(3,3)),
    ((5,1),(5,1)),
}
assert set(sig_by_orbit)==EXPECTED_SIGS
flat_raw=[T for T in CAND if all(h==ID6 for h in triple(T))]
assert len(flat_raw)==2
flat_orbits=[orb for orb in GAUGE_ORBITS if any(all(h==ID6 for h in triple(T)) for T in orb)]
assert len(flat_orbits)==1
assert ID6 in flat_orbits[0]
assert len(GAUGE_ORBITS)-len(flat_orbits)==7

# Mandatory Gen18 nonflat-equivariant witness.
WIT=next(T for T in CAND if cstr(T)=="(E1 E6)")
CW=connection(WIT)
J=next(p for p in S6 if cstr(p)=="(E1 E6)(E2 E5)(E3 E4)")
assert all(path_hol(CW,p)==J for p in BASIS)
assert all(path_hol(CW,p)!=ID6 for p in BASIS)
assert all(conn_nat(CW,g) for g in S4)

# ---------- Gen18 hidden-kernel full-lift-fiber regression ----------
# Exact finite group C2 x S4: chosen lifts generate only {0}xS4; full a,b fibers generate all 48.
def mulG(x,y): return ((x[0]+y[0])%2, comp(x[1],y[1]))
def invG(x): return (x[0], inv(x[1]))
def closureG(gens):
    e=(0,ID4); out={e}; front=[e]; gens=list(gens)
    while front:
        x=front.pop()
        for g in gens:
            for y in (mulG(g,x),mulG(x,g),mulG(invG(g),x)):
                if y not in out:
                    out.add(y); front.append(y)
    return out
chosen={(0,a),(0,b)}
fibers={(k,g) for k in (0,1) for g in (a,b)}
assert len(closureG(chosen))==24
assert len(closureG(fibers))==48

# ---------- Common non-degenerate enriched model ----------
# PF is nonconstant and fully equivariant; CW is independent, nonidentity, nonflat, fully equivariant.
assert len({PF[x] for x in range(4)})==4
assert WIT!=ID6
assert any(path_hol(CW,p)!=ID6 for p in BASIS)
assert pf_equivariant(a) and pf_equivariant(b)
assert conn_nat(CW,a) and conn_nat(CW,b)
# Since the same structural S4 action preserves both retained backgrounds,
# enriched generator relations are the frozen S4 relations.
assert power(a,3)==ID4 and power(b,2)==ID4 and power(comp(a,b),4)==ID4
assert power(aE,3)==ID6 and power(bE,2)==ID6 and power(comp(aE,bE),4)==ID6

print("PASS P000_S4_EQUIVARIANT_PF10_CONNECTION_MODULI_V19_CHECK")
print("carrier_s4_order=24")
print("pf10_base_vector_orbits=2")
print("pf10_base_ordered_pair_orbits=8")
print("pf10_raw_parameter_count=12")
print("connection_raw_equivariant_solutions=12")
print("connection_raw_identity=1")
print("connection_raw_nonidentity=11")
print("connection_gauge_classes=8")
print("connection_flat_gauge_classes=1")
print("connection_nonflat_gauge_classes=7")
print("gen18_nonflat_witness_retained=true")
print("common_nonconstant_pf10_nonflat_connection_model=true")
print("full_lift_fiber_hidden_kernel_regression=48_vs_chosen_24")
print("enriched_generator_relations=true")
print("terminal_class=NONTRIVIAL_PF10_AND_NONFLAT_CONNECTION_MODULI_COMMON_MODEL_CLASSIFIED")
