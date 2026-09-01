from __future__ import annotations
import itertools, json, pathlib

ROOT = pathlib.Path(".")
V = ("A","B","C","D")
VIDX = {x:i for i,x in enumerate(V)}
EDGES = (("A","B"),("A","C"),("A","D"),("B","C"),("B","D"),("C","D"))
EDGE_IDX = {tuple(sorted(e)):i for i,e in enumerate(EDGES)}
LABELS = tuple("".join(e) for e in EDGES)
ID4 = tuple(range(4))
ID6 = tuple(range(6))

def comp(p,q):
    return tuple(p[q[i]] for i in range(len(q)))

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

def rho(g):
    out=[]
    for u,v in EDGES:
        a,b = V[g[VIDX[u]]], V[g[VIDX[v]]]
        out.append(EDGE_IDX[tuple(sorted((a,b)))])
    return tuple(out)

def trans4(i,j):
    p=list(ID4); p[i],p[j]=p[j],p[i]; return tuple(p)

def swap6(i,j):
    p=list(ID6); p[i],p[j]=p[j],p[i]; return tuple(p)

S4 = list(itertools.permutations(range(4)))
S6 = list(itertools.permutations(range(6)))
EA = [rho(g) for g in S4]
assert len(set(EA)) == 24
for g in S4:
    for h in S4:
        assert comp(rho(g),rho(h)) == rho(comp(g,h))

a4=(0,2,3,1)                   # (BCD)
b4=trans4(0,1)                 # (AB)
a6,b6=rho(a4),rho(b4)
assert power(a4,3)==ID4 and power(b4,2)==ID4 and power(comp(a4,b4),4)==ID4
assert power(a6,3)==ID6 and power(b6,2)==ID6 and power(comp(a6,b6),4)==ID6

def orbit_partition(points, acts, act_fn):
    unseen=set(points); out=[]
    while unseen:
        x=min(unseen)
        orb={act_fn(g,x) for g in acts}
        out.append(tuple(sorted(orb)))
        unseen-=orb
    return tuple(out)

full_vec_orbits=orbit_partition(range(6),EA,lambda g,i:g[i])
full_pair_orbits=orbit_partition([(i,j) for i in range(6) for j in range(6)],EA,lambda g,p:(g[p[0]],g[p[1]]))
stabA=[g for g in S4 if g[0]==0]
stabA6=[rho(g) for g in stabA]
cell_vec_orbits=orbit_partition(range(6),stabA6,lambda g,i:g[i])
cell_pair_orbits=orbit_partition([(i,j) for i in range(6) for j in range(6)],stabA6,lambda g,p:(g[p[0]],g[p[1]]))
assert len(full_vec_orbits)==1
assert sorted(map(len,full_pair_orbits))==[6,6,24]
assert len(cell_vec_orbits)==2 and sorted(map(len,cell_vec_orbits))==[3,3]
assert len(cell_pair_orbits)==8 and sorted(map(len,cell_pair_orbits))==[3,3,3,3,6,6,6,6]

STAR={0,1,2}; FACE={3,4,5}
def share(i,j):
    return bool(set(EDGES[i]) & set(EDGES[j]))
def mclass(i,j):
    if i in STAR and j in STAR: return "SS_eq" if i==j else "SS_neq"
    if i in FACE and j in FACE: return "FF_eq" if i==j else "FF_neq"
    if i in STAR and j in FACE: return "SF_inc" if share(i,j) else "SF_opp"
    if i in FACE and j in STAR: return "FS_inc" if share(i,j) else "FS_opp"
    raise AssertionError
MCLASSES=("SS_eq","SS_neq","FF_eq","FF_neq","SF_inc","SF_opp","FS_inc","FS_opp")
for name in MCLASSES:
    pts=[(i,j) for i in range(6) for j in range(6) if mclass(i,j)==name]
    assert len(pts) in (3,6)
    assert any(set(pts)==set(o) for o in cell_pair_orbits)

def push_vec(g,v):
    out=[None]*6
    for i in range(6): out[g[i]]=v[i]
    return tuple(out)
def push_mat(g,m):
    out=[None]*36
    for i in range(6):
        for j in range(6):
            out[6*g[i]+g[j]]=m[6*i+j]
    return tuple(out)
def profile_push(g,p):
    I,O,M=p
    return push_vec(g,I),push_vec(g,O),push_mat(g,M)

PARAM_ORDER=("I_S","I_F","O_S","O_F")+MCLASSES
def base_profile(params):
    d=dict(zip(PARAM_ORDER,params))
    I=tuple(d["I_S"] if i in STAR else d["I_F"] for i in range(6))
    O=tuple(d["O_S"] if i in STAR else d["O_F"] for i in range(6))
    M=tuple(d[mclass(i,j)] for i in range(6) for j in range(6))
    return (I,O,M)

gAto={}
for x in range(4):
    gAto[x]=next(g for g in S4 if g[0]==x)

def reconstruct(params):
    P0=base_profile(params)
    P={}
    for x in range(4):
        imgs={profile_push(rho(g),P0) for g in S4 if g[0]==x}
        assert len(imgs)==1
        P[x]=next(iter(imgs))
    return P

def pf_full(P):
    for g in S4:
        eg=rho(g)
        for x in range(4):
            if P[g[x]] != profile_push(eg,P[x]):
                return False
    return True

sym_params=tuple(PARAM_ORDER)
assert pf_full(reconstruct(sym_params))
seen=set()
for params in itertools.product((0,1), repeat=12):
    P=reconstruct(params)
    enc=tuple(P[x] for x in range(4))
    seen.add(enc)
assert len(seen)==2**12

def centralizes(p,q): return comp(p,q)==comp(q,p)
residual=[h for h in S6 if all(centralizes(h,g) for g in stabA6)]
opp_idx={}
for i,(u,v) in enumerate(EDGES):
    rem=[x for x in V if x not in (u,v)]
    opp_idx[i]=EDGE_IDX[tuple(sorted(rem))]
omega=tuple(opp_idx[i] for i in range(6))
assert set(residual)=={ID6,omega}
assert all(centralizes(omega,g) for g in EA)

def extract_params(P0):
    I,O,M=P0
    reps={"I_S": I[0],"I_F":I[3],"O_S":O[0],"O_F":O[3]}
    for name in MCLASSES:
        i,j=next((i,j) for i in range(6) for j in range(6) if mclass(i,j)==name)
        reps[name]=M[6*i+j]
    return tuple(reps[k] for k in PARAM_ORDER)
def gauge_params(params,h):
    return extract_params(profile_push(h,base_profile(params)))
pnames=gauge_params(PARAM_ORDER,omega)
name_map=dict(zip(PARAM_ORDER,pnames))
expected_param_swaps={
    "I_S":"I_F","I_F":"I_S","O_S":"O_F","O_F":"O_S",
    "SS_eq":"FF_eq","FF_eq":"SS_eq","SS_neq":"FF_neq","FF_neq":"SS_neq",
    "SF_inc":"FS_inc","FS_inc":"SF_inc","SF_opp":"FS_opp","FS_opp":"SF_opp",
}
assert name_map==expected_param_swaps
fixed_binary=sum(1 for p in itertools.product((0,1),repeat=12) if gauge_params(p,omega)==p)
assert fixed_binary==2**6
binary_pf_gauge_orbits=(2**12+2**6)//2
assert binary_pf_gauge_orbits==2080

def star_vec(x):
    return tuple(1 if V[x] in EDGES[i] else 0 for i in range(6))
PF={}
for x in range(4):
    sv=star_vec(x)
    mm=tuple(sv[i]*sv[j] for i in range(6) for j in range(6))
    PF[x]=(sv,sv,mm)
assert pf_full(PF)
assert len({PF[x] for x in range(4)})==4

s=b6
c=rho(trans4(2,3))
centralizer_c=[t for t in S6 if centralizes(t,c)]
assert len(centralizer_c)==16
valid=[]
for t in centralizer_c:
    if conj(s,t)==inv(t):
        valid.append(t)
assert len(valid)==12

e=swap6(0,5)
cmid=comp(swap6(1,2),swap6(3,4))
smid=comp(swap6(1,3),swap6(2,4))
dmid=comp(swap6(1,4),swap6(2,3))
r=(0,3,4,2,1,5)
rinv=inv(r)
U={ID6,cmid,smid,dmid,r,rinv}
assert len(U)==6
assert set(valid)==U | {comp(e,u) for u in U}

ORIENTED=[(x,y) for x in range(4) for y in range(4) if x!=y]
def conn_from_base(t):
    T={}
    for x,y in ORIENTED:
        vals={conj(rho(g),t) for g in S4 if g[0]==x and g[1]==y}
        assert len(vals)==1
        T[(x,y)]=next(iter(vals))
    return T
def inverse_consistent(T):
    return all(T[(y,x)]==inv(T[(x,y)]) for x,y in ORIENTED)
def conn_full(T):
    for g in S4:
        eg=rho(g)
        for x,y in ORIENTED:
            if T[(g[x],g[y])] != conj(eg,T[(x,y)]):
                return False
    return True

connections={t:conn_from_base(t) for t in valid}
assert all(inverse_consistent(T) and conn_full(T) for T in connections.values())

def gauge_base(t,hA):
    hB=conj(s,hA)
    return comp(comp(hB,t),inv(hA))
assert all(gauge_base(t,h) in set(valid) for t in valid for h in residual)
orbits=[]
unseen=set(valid)
while unseen:
    t=min(unseen)
    o={gauge_base(t,h) for h in residual}
    orbits.append(o); unseen-=o
assert len(orbits)==10
assert sorted(map(len,orbits))==[1]*8+[2]*2
assert sum(1 for t in valid if gauge_base(t,omega)==t)==8

def path_transport(T,path):
    z=ID6
    for x,y in zip(path,path[1:]):
        z=comp(T[(x,y)],z)
    return z
basis=((0,1,2,0),(0,1,3,0),(0,2,3,0))
def flat(T):
    return all(path_transport(T,p)==ID6 for p in basis)
def ctype(p):
    seen=[False]*6; lens=[]
    for i in range(6):
        if seen[i]: continue
        j=i; n=0
        while not seen[j]:
            seen[j]=True; n+=1; j=p[j]
        lens.append(n)
    return tuple(sorted(lens,reverse=True))

flat_raw=[t for t,T in connections.items() if flat(T)]
assert set(flat_raw)=={ID6,dmid}
assert len(flat_raw)==2
flat_orbits=[o for o in orbits if all(flat(connections[t]) for t in o)]
assert len(flat_orbits)==2
assert len(orbits)-len(flat_orbits)==8

basis_types={}
for t,T in connections.items():
    types={ctype(path_transport(T,p)) for p in basis}
    assert len(types)==1
    basis_types[t]=next(iter(types))
for o in orbits:
    assert len({basis_types[t] for t in o})==1
hist={}
for o in orbits:
    typ=basis_types[next(iter(o))]
    hist[typ]=hist.get(typ,0)+1
assert hist=={
    (1,1,1,1,1,1):2,
    (4,2):1,
    (2,2,1,1):1,
    (2,1,1,1,1):1,
    (2,2,2):3,
    (4,1,1):1,
    (5,1):1,
}

t18=e
assert t18 in valid and not flat(connections[t18])
T18=connections[t18]
for x,y in ORIENTED:
    i=EDGE_IDX[tuple(sorted((V[x],V[y])))]
    assert T18[(x,y)]==swap6(i,opp_idx[i])
hol18=[path_transport(T18,p) for p in basis]
assert all(h==omega for h in hol18)

def act_pf(P,g):
    gi=inv(g); eg=rho(g)
    return {z:profile_push(eg,P[gi[z]]) for z in range(4)}
def act_conn(T,g):
    gi=inv(g); eg=rho(g)
    return {(z,w):conj(eg,T[(gi[z],gi[w])]) for z,w in ORIENTED}
assert all(act_pf(PF,g)==PF for g in S4)
assert all(act_conn(T18,g)==T18 for g in S4)
assert PF[0]!=PF[1] and any(T18[xy]!=ID6 for xy in ORIENTED)
assert not flat(T18)

cert_path=ROOT/"research_artifacts/P000_BACKGROUND_S4_EQUIVARIANCE_GATE_V17/BACKGROUND_EQUIVARIANCE_CERTIFICATE.json"
if cert_path.exists():
    cert=json.loads(cert_path.read_text(encoding="utf-8"))
    frame_row=next(x for x in cert["background_inventory"] if x["component"]=="per-Cell frame f_x")
    assert "rho(q0(u))" in frame_row["certificate"]
    assert cert["guards"]["NO_KERNEL_QUOTIENT"] is True
    assert cert["guards"]["CARRIER_S4_IS_NOT_COMPLETE_NATIVE_P000_ROTATION_GROUP"] is True
    assert cert["guards"]["TIME_FIXED"] is True


gen18_path=ROOT/"research_result_records/RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE/RR-7FED4A83F3922D37319D.json"
if gen18_path.exists():
    gen18=json.loads(gen18_path.read_text(encoding="utf-8"))
    assert gen18["terminal_class"]=="LOCAL_GENERATOR_EQUIVARIANCE_EXACTLY_EQUIVALENT_TO_GLOBAL_BACKGROUND_TRANSPARENCY"
    assert "kernel transparency" in gen18["unresolved_residue"]

print("PASS P000_S4_EQUIVARIANT_PF10_CONNECTION_MODULI_V21_CHECK")
print("full_s4_vector_orbits=1")
print("full_s4_ordered_pair_orbits=3")
print("base_cell_vector_orbits=2")
print("base_cell_ordered_pair_orbits=8")
print("pf10_framed_parameter_count_symbolic=12")
print("pf10_binary_framed_families=4096")
print("pf10_binary_gauge_classes=2080")
print("connection_value_universe=S6_order_720")
print("connection_edge_centralizer_candidates=16")
print("connection_raw_equivariant_reverse_solutions=12")
print("connection_residual_gauge_order=2")
print("connection_gauge_classes=10")
print("connection_flat_raw=2")
print("connection_nonflat_raw=10")
print("connection_flat_gauge_classes=2")
print("connection_nonflat_gauge_classes=8")
print("gen18_opposite_edge_witness_class_nonflat=true")
print("common_nonconstant_pf10_nonflat_connection_model=true")
print("terminal_class=NONTRIVIAL_PF10_AND_NONFLAT_CONNECTION_MODULI_COMMON_MODEL_CLASSIFIED")
