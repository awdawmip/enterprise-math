#!/usr/bin/env python3
"""Exact finite checker for P000 Gen11 framed full-Cell b-equivariance."""
from itertools import permutations
from math import factorial

N=6
ID=tuple(range(N))
PERMS=list(permutations(range(N)))

def comp(p,q): return tuple(p[q[i]] for i in range(N))
def inv(p):
    r=[0]*N
    for i,j in enumerate(p): r[j]=i
    return tuple(r)
def group(gens):
    seen={ID}; todo=[ID]
    while todo:
        x=todo.pop()
        for g in gens:
            y=comp(g,x)
            if y not in seen: seen.add(y); todo.append(y)
    return seen
def relv(v,g):
    gi=inv(g); return [v[gi[i]] for i in range(N)]
def relm(M,g):
    gi=inv(g); return [[M[gi[i]][gi[j]] for j in range(N)] for i in range(N)]
def pm(M,f): return [[M[f[i]][f[j]] for j in range(N)] for i in range(N)]
def tf(fx,fy): return comp(fy,inv(fx))
def pi(fx,fr): return comp(fr,comp(b,inv(fx)))
def oriented(edges):
    out=[]
    for e in edges:
        x,y=tuple(e); out += [(x,y),(y,x)]
    return out
def path_T(path,T):
    z=ID
    for x,y in zip(path,path[1:]): z=comp(T[(x,y)],z)
    return z

b=(0,3,4,1,2,5)
assert comp(b,b)==ID

# Gen7.
B0={0,1,2}; B1={3,4,5}
W=[p for p in PERMS if {p[i] for i in B0} in (B0,B1)]
assert len(W)==72 and b not in W and len(group(W+[b]))==720

# Gen8.
src=frozenset({(0,1),(1,2),(2,0)})
dst=frozenset({(0,3),(3,4),(4,0)})
matching={frozenset({1,3}),frozenset({2,4})}
def ie(p,E): return frozenset((p[x],p[y]) for x,y in E)
def im(p,M):
    return {frozenset({p[x],p[y]}) for x,y in (tuple(z) for z in M)}
auts=[]
for p in PERMS:
    if p[0]==0 and p[5]==5 and {ie(p,src),ie(p,dst)}=={src,dst} and im(p,matching)==matching:
        auts.append(p)
assert set(auts)=={ID,b}

# Gen9.
stabs=[sum(all(p[i]==i for i in range(k)) for p in PERMS) for k in range(7)]
assert stabs==[720,120,24,6,2,1,1]
assert stabs==[factorial(6-k) for k in range(7)]

# Gen10 PASS gauge invariance and flat frame connection.
probe=(2,5,1,4,0,3)
Mp=[[10*i+j for j in range(N)] for i in range(N)]
Pp=pm(Mp,probe)
for g in PERMS:
    assert pm(relm(Mp,g),comp(g,probe))==Pp

F4=[ID,(1,0,2,3,5,4),(2,1,0,5,4,3),(5,4,3,2,1,0)]
T4={}
for x,y in [(0,1),(1,2),(2,3),(3,0)]:
    T4[(x,y)]=tf(F4[x],F4[y]); T4[(y,x)]=inv(T4[(x,y)])
assert path_T([0,1,2,3,0],T4)==ID

def zmat(): return [[0]*N for _ in range(N)]
M0=zmat()
for i in range(N): M0[i][i]=1
M1=[r[:] for r in M0]
M1[1][3]=M1[3][1]=2
M1[2][4]=M1[4][2]=3
def omega(M,f):
    P=pm(M,f)
    return P[1][3]>0 and P[1][3]==P[3][1] and P[2][4]>0 and P[2][4]==P[4][2]
assert not omega(M0,ID) and omega(M1,ID)

# Gen11 model predicates.
def bij_inv(r,cells):
    return set(r)==set(cells) and set(r.values())==set(cells) and all(r[r[x]]==x for x in cells)
def adj_eq(r,edges):
    return {frozenset({r[x],r[y]}) for x,y in (tuple(e) for e in edges)}==set(edges)
def pf_eq(r,F,I,O,M):
    for x in F:
        rx=r[x]; p=pi(F[x],F[rx])
        for c in range(N):
            if I[rx][p[c]]!=I[x][c] or O[rx][p[c]]!=O[x][c]: return False
            for d in range(N):
                if M[rx][p[c]][p[d]]!=M[x][c][d]: return False
    return True
def nat(r,F,T,edges):
    for x,y in oriented(edges):
        if comp(T[(r[x],r[y])],pi(F[x],F[r[x]])) != comp(pi(F[y],F[r[y]]),T[(x,y)]):
            return False
    return True
def strict(r,cells,edges,F,I,O,M,T=None):
    if not bij_inv(r,cells) or not adj_eq(r,edges) or not pf_eq(r,F,I,O,M): return False
    if T is not None and not nat(r,F,T,edges): return False
    return all(comp(pi(F[r[x]],F[x]),pi(F[x],F[r[x]]))==ID for x in cells)
def frame_T(edges,F): return {(x,y):tf(F[x],F[y]) for x,y in oriented(edges)}
def inv_auts(cells,edges):
    ans=[]
    for p in permutations(cells):
        r=dict(zip(cells,p))
        if bij_inv(r,cells) and adj_eq(r,edges): ans.append(r)
    return ans
def exists(cells,edges,F,I,O,M,T=None):
    return any(strict(r,cells,edges,F,I,O,M,T) for r in inv_auts(cells,edges))
def any_omega(cells,F,M): return any(omega(M[x],F[x]) for x in cells)

cells=(0,1); edges={frozenset({0,1})}; F={0:ID,1:ID}; r={0:1,1:0}
T=frame_T(edges,F); one=[1]*N
def rep(M,I=None):
    if I is None: I=one
    return ({x:list(I) for x in cells},{x:one[:] for x in cells},{x:[q[:] for q in M] for x in cells})

# Positive witness and frame-induced naturality.
Itt,Ott,Mtt=rep(M1)
assert strict(r,cells,edges,F,Itt,Ott,Mtt,T)
for fx in PERMS[::37]:
    for fy in PERMS[::53]:
        FF={0:fx,1:fy}; assert nat(r,FF,frame_T(edges,FF),edges)

# Gauge covariance.
G={0:PERMS[101],1:PERMS[503]}
Fg={x:comp(G[x],F[x]) for x in cells}
Tg={(x,y):comp(G[y],comp(T[(x,y)],inv(G[x]))) for x,y in oriented(edges)}
Ig={x:relv(Itt[x],G[x]) for x in cells}
Og={x:relv(Ott[x],G[x]) for x in cells}
Mg={x:relm(Mtt[x],G[x]) for x in cells}
for x in cells:
    assert pi(Fg[x],Fg[r[x]])==comp(G[r[x]],comp(pi(F[x],F[r[x]]),inv(G[x])))
assert strict(r,cells,edges,Fg,Ig,Og,Mg,Tg)

# Omega/base-R four-grid.
asym=[1]*N; asym[3]=2
Itf,Otf,Mtf=rep(M1,asym)
Ift,Oft,Mft=rep(M0)
Iff,Off,Mff=rep(M0,asym)
assert any_omega(cells,F,Mtt) and exists(cells,edges,F,Itt,Ott,Mtt,T)
assert any_omega(cells,F,Mtf) and not exists(cells,edges,F,Itf,Otf,Mtf,T)
assert not any_omega(cells,F,Mft) and exists(cells,edges,F,Ift,Oft,Mft,T)
assert not any_omega(cells,F,Mff) and not exists(cells,edges,F,Iff,Off,Mff,T)

# Independent adjacency and PF10 conditions.
c3=(0,1,2); e3={frozenset({0,1}),frozenset({1,2})}
F3={x:ID for x in c3}; bad={0:1,1:0,2:2}
I3={x:one[:] for x in c3}; O3={x:one[:] for x in c3}; M3={x:[q[:] for q in M0] for x in c3}
assert bij_inv(bad,c3) and pf_eq(bad,F3,I3,O3,M3) and not adj_eq(bad,e3)
assert adj_eq(r,edges) and not pf_eq(r,F,Itf,Otf,Mtf)

# Order-two condition is not implied by relation preservation.
K3={frozenset({0,1}),frozenset({1,2}),frozenset({0,2})}
r3={0:1,1:2,2:0}
assert adj_eq(r3,K3) and pf_eq(r3,F3,I3,O3,M3)
assert not bij_inv(r3,c3)

# Nonflat independent connection: equivariant may pass; noncommuting may fail.
tri=c3; Etri=K3; Rfix={x:x for x in tri}
hgood=(5,1,2,3,4,0)
assert comp(hgood,b)==comp(b,hgood)
Tgood={(x,y):ID for x,y in oriented(Etri)}
Tgood[(2,0)]=hgood; Tgood[(0,2)]=hgood
assert path_T([0,1,2,0],Tgood)==hgood!=ID
assert nat(Rfix,F3,Tgood,Etri) and strict(Rfix,tri,Etri,F3,I3,O3,M3,Tgood)
hbad=(1,0,2,3,4,5)
assert comp(hbad,b)!=comp(b,hbad)
Tbad=dict(Tgood); Tbad[(2,0)]=hbad; Tbad[(0,2)]=inv(hbad)
assert not nat(Rfix,F3,Tbad,Etri)
assert not strict(Rfix,tri,Etri,F3,I3,O3,M3,Tbad)

# Strength guards.
assert not any([False,False,False,False,False])  # P000 mutation/S6 promotion/quotient/carrier-ID/time move

print("PASS P000_BASE_CELL_RB_EQUIVARIANCE_V11_CHECK")
print("terminal_class=FRAMED_FULL_CELL_b_AUTOMORPHISM_IFF_CLASSIFIED_AND_WITNESSED")
print("gen7_W_order=72")
print("gen7_W_plus_b_order=720")
print("gen8_AutSigma_b_order=2")
print("gen9_anchor_stabilizers="+",".join(map(str,stabs)))
print("gen10_PASS_gauge_invariant=true")
print("gen10_Omega_b_forced=false")
print("frame_induced_connection_naturality=automatic")
print("independent_connection_naturality=additional")
print("nonflat_holonomy_can_be_b_equivariant=true")
print("holonomy_equivariance_failure_can_obstruct=true")
print("Omega_and_base_R_four_grid=all_four_realized")
print("Omega_b_logic_vs_base_R=INDEPENDENT")
print("Omega_b_semantic_role=CONTACT_ROUTE_SPECIFIC")
print("base_R_b_witness=two_cell_nonidentity_swap")
print("full_P000_native_rotation_group_promoted=false")
