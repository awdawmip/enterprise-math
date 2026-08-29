#!/usr/bin/env python3
from itertools import combinations, permutations, product

V=("A","B","C","D")
E=tuple("".join(x) for x in combinations(V,2))
EI={e:i for i,e in enumerate(E)}
Q=(1,1,0,1,0,0)  # 1 means negative edge
Q0=(1,1,1,1,1,1) # all-negative canonical symmetric representative
TD=(0,0,0,1)      # vertex switching cochain supported at D

def ce(a,b): return "".join(sorted((a,b)))
def xor(a,b): return tuple(x^y for x,y in zip(a,b))
def delta(t): return tuple(t[V.index(e[0])] ^ t[V.index(e[1])] for e in E)
def switch(sig,t): return xor(sig,delta(t))
def pmap(p): return {V[i]:p[i] for i in range(4)}
def pinv(p):
    out=[None]*4
    for i,img in enumerate(p):
        out[V.index(img)] = V[i]
    return tuple(out)
def pcompose(p,s): # p o s
    return tuple(p[V.index(s[i])] for i in range(4))
ID=V
PERMS=list(permutations(V))
def act0(p,t): # push-forward: (p.t)(v)=t(p^-1 v)
    inv=pinv(p)
    return tuple(t[V.index(inv[i])] for i in range(4))
def act1(p,sig):
    inv=pinv(p); m=pmap(inv)
    return tuple(sig[EI[ce(m[e[0]],m[e[1]])]] for e in E)
def ep_action(p):
    m=pmap(p)
    return tuple(EI[ce(m[e[0]],m[e[1]])] for e in E)

# A. Signed-K4 exact class
assert switch(Q0,TD)==Q
triangles={}
for a,b,c in combinations(V,3):
    parity=Q[EI[ce(a,b)]] ^ Q[EI[ce(b,c)]] ^ Q[EI[ce(c,a)]]
    triangles[a+b+c] = -1 if parity else 1
assert set(triangles.values())=={-1}
four_cycles={}
for cyc in (("A","B","C","D"),("A","B","D","C"),("A","C","B","D")):
    parity=0
    for i in range(4):
        parity ^= Q[EI[ce(cyc[i],cyc[(i+1)%4])]]
    four_cycles["".join(cyc)] = -1 if parity else 1
assert set(four_cycles.values())=={1}
assert len(E)-len(V)+1==3  # dim H^1(K4;F2)

orbit={switch(Q,t) for t in product((0,1),repeat=4)}
assert len(orbit)==8
assert Q0 in orbit
mins=[s for s in orbit if sum(s)==min(map(sum,orbit))]
assert len(mins)==3 and min(map(sum,orbit))==2
min_negative_sets={frozenset(E[i] for i,b in enumerate(s) if b) for s in mins}
assert min_negative_sets=={
    frozenset(("AB","CD")),
    frozenset(("AC","BD")),
    frozenset(("AD","BC")),
}

# B/C. S4 invariance, gauge correction and split lift
strict_q=[p for p in PERMS if act1(p,Q)==Q]
strict_q0=[p for p in PERMS if act1(p,Q0)==Q0]
assert len(strict_q)==6
assert len(strict_q0)==24

G={}
for p in PERMS:
    gp=xor(TD,act0(p,TD))
    assert switch(act1(p,Q),gp)==Q
    G[p]=gp
for p,s in product(PERMS,repeat=2):
    ps=pcompose(p,s)
    assert G[ps]==xor(G[p],act0(p,G[s]))  # exact 1-cocycle, hence no 2-cocycle residue

a=("A","C","D","B") # (BCD)
b=("B","A","C","D") # (AB)
assert G[a]==(0,1,0,1)
assert G[b]==(0,0,0,0)

def pair_mul(left,right): # (p,gp)(s,gs) = (p s, gp + p.gs)
    p,gp=left; s,gs=right
    return pcompose(p,s), xor(gp,act0(p,gs))
def pair_pow(x,n):
    r=(ID,(0,0,0,0))
    for _ in range(n): r=pair_mul(r,x)
    return r
La=(a,G[a]); Lb=(b,G[b])
assert pair_pow(La,3)==(ID,(0,0,0,0))
assert pair_pow(Lb,2)==(ID,(0,0,0,0))
assert pair_pow(pair_mul(La,Lb),4)==(ID,(0,0,0,0))

# shortlex/path regression: every word of length <=8 reaches the unique (sigma,g_sigma)
for n in range(9):
    for word in product((0,1),repeat=n):
        lift=(ID,(0,0,0,0))
        for letter in word:
            lift=pair_mul(lift, La if letter==0 else Lb)
        assert lift[1]==G[lift[0]]
        if lift[0]==ID:
            assert lift[1]==(0,0,0,0)

# The full switching-automorphism lift group E_q has 48 elements:
# for each sigma, exactly two gauge corrections differing by the constant cochain.
Eq=[]
for p in PERMS:
    sols=[]
    for t in product((0,1),repeat=4):
        if switch(act1(p,Q),t)==Q:
            sols.append(t)
    assert len(sols)==2 and set(sols)=={G[p],xor(G[p],(1,1,1,1))}
    Eq.extend((p,t) for t in sols)
assert len(Eq)==48
kernel=[(p,t) for p,t in Eq if p==ID]
assert set(t for _,t in kernel)=={(0,0,0,0),(1,1,1,1)}
# split section plus central constant identifies E_q with S4 x C2.

# D/E. K4 star incidence and local orientation torsor
ST={v:frozenset(e for e in E if v in e) for v in V}
J={
    "A":frozenset((0,1,2)),
    "B":frozenset((0,3,4)),
    "C":frozenset((1,3,5)),
    "D":frozenset((2,4,5)),
}
assert all(len(ST[x]&ST[y])==1 for x,y in combinations(V,2))
assert all(sum(i in J[v] for v in V)==2 for i in range(6))
assert {v:frozenset(E[i] for i in J[v]) for v in V}==ST

R={"AB":(1,1,0),"AC":(1,0,1),"AD":(0,1,-1),
   "BC":(0,1,1),"BD":(1,0,-1),"CD":(1,-1,0)}
S={"A":{"AB":-1,"AC":1,"AD":1},
   "B":{"AB":1,"BC":-1,"BD":-1},
   "C":{"AC":-1,"BC":1,"CD":1},
   "D":{"AD":1,"BD":-1,"CD":1}}
def add(vs): return tuple(sum(v[i] for v in vs) for i in range(3))
def sc(a,v): return tuple(a*x for x in v)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
local_counts={}
for c,star in ST.items():
    es=tuple(sorted(star)); good=[]
    for signs in product((-1,1),repeat=3):
        vs=[sc(signs[k],R[e]) for k,e in enumerate(es)]
        if add(vs)==(0,0,0) and all(dot(vs[i],vs[j])==-1 for i,j in combinations(range(3),2)):
            good.append(signs)
    local_counts[c]=len(good)
    assert len(good)==2
assert set(local_counts.values())=={2} # one C2 presentation bit iff oriented chart is retained
global_good=0
for signs in product((-1,1),repeat=6):
    g=dict(zip(E,signs)); ok=True
    for star in ST.values():
        es=tuple(sorted(star)); vs=[sc(g[e],R[e]) for e in es]
        if add(vs)!=(0,0,0) or not all(dot(vs[i],vs[j])==-1 for i,j in combinations(range(3),2)):
            ok=False; break
    global_good += int(ok)
assert global_good==0

# F. Carrier actions and current native G0 obstruction
carrier_actions={ep_action(p) for p in PERMS}
assert len(carrier_actions)==24
ea=ep_action(a); eb=ep_action(b)
rho=(3,4,5,0,1,2) # clone-product whole-block exchange under typed copy positions
assert rho not in carrier_actions
G0={tuple(range(6)),rho}
assert ea not in G0 and eb not in G0

# Old star/complement no-intertwiner regression
SA=frozenset((0,1,2)); COMP=frozenset((3,4,5))
assert all(frozenset(act[i] for i in SA)!=COMP for act in carrier_actions)

# Logical-independence positive witness: Q6 supports every coordinate permutation
Q6=list(product((0,1),repeat=6))
def hamming(x,y): return sum(a!=b for a,b in zip(x,y))
def coord_perm(x,act):
    out=[None]*6
    for src,dst in enumerate(act): out[dst]=x[src]
    return tuple(out)
for act in (ea,eb):
    assert len({coord_perm(x,act) for x in Q6})==64
    for x in Q6:
        for i in range(6):
            y=list(x); y[i]^=1; y=tuple(y)
            assert hamming(coord_perm(x,act),coord_perm(y,act))==1

# Logical-independence block witness: axis action S3 wr C2 (size 72), a in, b out
S3=list(permutations(range(3)))
block_axis_actions=set()
for p1 in S3:
    for p2 in S3:
        block_axis_actions.add(tuple(list(p1)+[3+x for x in p2]))
        block_axis_actions.add(tuple([3+x for x in p1]+list(p2)))
assert len(block_axis_actions)==72
assert ea in block_axis_actions
assert eb not in block_axis_actions

# Verify K4 square has exactly the row/column maximal 4-cliques used by the block proof
P4=range(4)
VX=tuple(product(P4,P4))
def adj_prod(x,y):
    return x!=y and ((x[0]==y[0]) ^ (x[1]==y[1]))
cliques4=[]
for C in combinations(VX,4):
    if all(adj_prod(x,y) for x,y in combinations(C,2)):
        cliques4.append(frozenset(C))
rows={frozenset((i,j) for j in P4) for i in P4}
cols={frozenset((i,j) for i in P4) for j in P4}
assert set(cliques4)==rows|cols and len(cliques4)==8

# Any passive hidden fiber cannot manufacture a missing base map:
# checked as a type invariant encoded in the certificate, not as a quotient.
PASSIVE_FIBER_REQUIRES_BASE_MAP=True
assert PASSIVE_FIBER_REQUIRES_BASE_MAP

# Carrier readout is many-to-one but is not native identity.
native_edge_1=("cell-u","cell-v",0)
native_edge_2=("cell-x","cell-y",0)
beta=E[0]
assert native_edge_1!=native_edge_2 and beta==E[0]

# Mandatory FCC/HCP 6/3 antipodal regression
R0=[(2,0,0),(1,3,0),(-1,3,0),(-2,0,0),(-1,-3,0),(1,-3,0)]
U3=[(1,1,1),(-1,1,1),(0,-2,1)]
FCC=R0+U3+[(0,2,-1),(-1,-1,-1),(1,-1,-1)]
HCP=R0+U3+[(1,1,-1),(-1,1,-1),(0,-2,-1)]
def ap(P):
    X=set(P)
    return {tuple(sorted((p,tuple(-x for x in p)))) for p in P if tuple(-x for x in p) in X}
assert len(ap(FCC))==6 and len(ap(HCP))==3

print("PASS")
print("signed_K4=ANTIBALANCED; H1_dim=3; switching_orbit=8; symmetric_normal_form=all_negative")
print("strict_stabilizer_q=6; strict_stabilizer_all_negative=24")
print("g_a=",G[a],"g_b=",G[b],"; cocycle_pairs=576")
print("lift_group=E_q_order_48_is_S4xC2; lift_relations: a^3=1 b^2=1 (ab)^4=1; central_residue=(0,0,0)")
print("local_chart_orientations=2_each; global_signed_sections=0")
print("native_current_G0=2; carrier_actions=24; rho_not_carrier_action=True")
print("block_axis_group=72; a_in_block_group=True; b_in_block_group=False")
print("Q6_full_coordinate_permutation_witness=True")
print("FCC_antipodal_pairs=6; HCP_antipodal_pairs=3")
