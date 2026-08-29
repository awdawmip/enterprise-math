#!/usr/bin/env python3
from itertools import combinations, permutations, product

V=("A","B","C","D")
E=tuple("".join(x) for x in combinations(V,2))
I={e:i for i,e in enumerate(E)}
Q=(1,1,0,1,0,0); Q0=(1,1,1,1,1,1); T=(0,0,0,1)
ID=V; P=list(permutations(V))

def ce(a,b): return "".join(sorted((a,b)))
def xx(a,b): return tuple(x^y for x,y in zip(a,b))
def delta(t): return tuple(t[V.index(e[0])]^t[V.index(e[1])] for e in E)
def sw(q,t): return xx(q,delta(t))
def inv(p):
    r=[None]*4
    for i,x in enumerate(p): r[V.index(x)]=V[i]
    return tuple(r)
def comp(p,s): return tuple(p[V.index(s[i])] for i in range(4))
def a0(p,t):
    z=inv(p)
    return tuple(t[V.index(z[i])] for i in range(4))
def a1(p,q):
    z=inv(p); m={V[i]:z[i] for i in range(4)}
    return tuple(q[I[ce(m[e[0]],m[e[1]])]] for e in E)
def edgeact(p):
    m={V[i]:p[i] for i in range(4)}
    return tuple(I[ce(m[e[0]],m[e[1]])] for e in E)

assert sw(Q0,T)==Q
tri={}
for a,b,c in combinations(V,3):
    tri[a+b+c]=-1 if Q[I[ce(a,b)]]^Q[I[ce(b,c)]]^Q[I[ce(c,a)]] else 1
assert set(tri.values())=={-1}
for c in (("A","B","C","D"),("A","B","D","C"),("A","C","B","D")):
    x=0
    for i in range(4): x^=Q[I[ce(c[i],c[(i+1)%4])]]
    assert x==0
assert len(E)-len(V)+1==3

O={sw(Q,t) for t in product((0,1),repeat=4)}
assert len(O)==8 and Q0 in O
M=[q for q in O if sum(q)==2]
assert len(M)==3
assert {frozenset(E[i] for i,b in enumerate(q) if b) for q in M}=={
    frozenset(("AB","CD")),frozenset(("AC","BD")),frozenset(("AD","BC"))
}
assert len([p for p in P if a1(p,Q)==Q])==6
assert len([p for p in P if a1(p,Q0)==Q0])==24

H={}
for p in P:
    H[p]=xx(T,a0(p,T))
    assert sw(a1(p,Q),H[p])==Q
for p,s in product(P,repeat=2):
    assert H[comp(p,s)]==xx(H[p],a0(p,H[s]))

a=("A","C","D","B"); b=("B","A","C","D")
assert H[a]==(0,1,0,1) and H[b]==(0,0,0,0)

def mul(x,y):
    p,g=x; s,h=y
    return comp(p,s),xx(g,a0(p,h))
def pw(x,n):
    r=(ID,(0,0,0,0))
    for _ in range(n): r=mul(r,x)
    return r
A=(a,H[a]); B=(b,H[b])
assert pw(A,3)==(ID,(0,0,0,0))
assert pw(B,2)==(ID,(0,0,0,0))
assert pw(mul(A,B),4)==(ID,(0,0,0,0))
for n in range(9):
    for w in product((0,1),repeat=n):
        r=(ID,(0,0,0,0))
        for x in w: r=mul(r,A if x==0 else B)
        assert r[1]==H[r[0]]
        if r[0]==ID: assert r[1]==(0,0,0,0)

EQ=[]
for p in P:
    S=[t for t in product((0,1),repeat=4) if sw(a1(p,Q),t)==Q]
    assert len(S)==2 and set(S)=={H[p],xx(H[p],(1,1,1,1))}
    EQ += [(p,t) for t in S]
assert len(EQ)==48
assert {t for p,t in EQ if p==ID}=={(0,0,0,0),(1,1,1,1)}

ST={v:frozenset(e for e in E if v in e) for v in V}
J={"A":(0,1,2),"B":(0,3,4),"C":(1,3,5),"D":(2,4,5)}
assert {v:frozenset(E[i] for i in J[v]) for v in V}==ST
assert all(len(ST[x]&ST[y])==1 for x,y in combinations(V,2))

R={"AB":(1,1,0),"AC":(1,0,1),"AD":(0,1,-1),"BC":(0,1,1),"BD":(1,0,-1),"CD":(1,-1,0)}
def add(vs): return tuple(sum(v[i] for v in vs) for i in range(3))
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def sc(s,x): return tuple(s*a for a in x)
for star in ST.values():
    es=tuple(sorted(star)); good=0
    for ss in product((-1,1),repeat=3):
        vv=[sc(ss[i],R[e]) for i,e in enumerate(es)]
        good+=int(add(vv)==(0,0,0) and all(dot(vv[i],vv[j])==-1 for i,j in combinations(range(3),2)))
    assert good==2
GLOB=0
for ss in product((-1,1),repeat=6):
    g=dict(zip(E,ss)); ok=True
    for star in ST.values():
        es=tuple(sorted(star)); vv=[sc(g[e],R[e]) for e in es]
        if add(vv)!=(0,0,0) or not all(dot(vv[i],vv[j])==-1 for i,j in combinations(range(3),2)):
            ok=False; break
    GLOB+=int(ok)
assert GLOB==0

CA={edgeact(p) for p in P}; assert len(CA)==24
EA=edgeact(a); EB=edgeact(b); RHO=(3,4,5,0,1,2)
assert RHO not in CA
assert EA not in {tuple(range(6)),RHO} and EB not in {tuple(range(6)),RHO}
SA=frozenset((0,1,2)); CO=frozenset((3,4,5))
assert all(frozenset(x[i] for i in SA)!=CO for x in CA)

S3=list(permutations(range(3))); W=set()
for p in S3:
    for q in S3:
        W.add(tuple(list(p)+[3+x for x in q]))
        W.add(tuple([3+x for x in p]+list(q)))
assert len(W)==72 and EA in W and EB not in W

Q6=list(product((0,1),repeat=6))
def cp(x,p):
    r=[None]*6
    for i,j in enumerate(p): r[j]=x[i]
    return tuple(r)
def hd(x,y): return sum(a!=b for a,b in zip(x,y))
for p in (EA,EB):
    assert len({cp(x,p) for x in Q6})==64
    for x in Q6:
        for i in range(6):
            y=list(x); y[i]^=1
            assert hd(cp(x,p),cp(tuple(y),p))==1

U=range(4); VX=tuple(product(U,U))
def adj(x,y): return x!=y and ((x[0]==y[0])^(x[1]==y[1]))
C={frozenset(s) for s in combinations(VX,4) if all(adj(x,y) for x,y in combinations(s,2))}
ROWS={frozenset((i,j) for j in U) for i in U}
COLS={frozenset((i,j) for i in U) for j in U}
assert C==ROWS|COLS and len(C)==8

n1=("u","v",0); n2=("x","y",0)
assert n1!=n2 and E[0]=="AB"

R0=[(2,0,0),(1,3,0),(-1,3,0),(-2,0,0),(-1,-3,0),(1,-3,0)]
U3=[(1,1,1),(-1,1,1),(0,-2,1)]
FCC=R0+U3+[(0,2,-1),(-1,-1,-1),(1,-1,-1)]
HCP=R0+U3+[(1,1,-1),(-1,1,-1),(0,-2,-1)]
def ap(X):
    S=set(X)
    return {tuple(sorted((x,tuple(-a for a in x)))) for x in X if tuple(-a for a in x) in S}
assert len(ap(FCC))==6 and len(ap(HCP))==3

print("PASS")
print("signed_K4=ANTIBALANCED; H1_dim=3; switching_orbit=8; symmetric_normal_form=all_negative")
print("strict_stabilizer_q=6; strict_stabilizer_all_negative=24")
print("g_a=",H[a],"g_b=",H[b],"; cocycle_pairs=576")
print("lift_group=E_q_order_48_is_S4xC2; lift_relations: a^3=1 b^2=1 (ab)^4=1; central_residue=(0,0,0)")
print("local_chart_orientations=2_each; global_signed_sections=0")
print("native_current_G0=2; carrier_actions=24; rho_not_carrier_action=True")
print("block_axis_group=72; a_in_block_group=True; b_in_block_group=False")
print("Q6_full_coordinate_permutation_witness=True")
print("FCC_antipodal_pairs=6; HCP_antipodal_pairs=3")
