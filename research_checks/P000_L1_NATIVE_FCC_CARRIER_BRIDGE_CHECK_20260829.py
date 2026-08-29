#!/usr/bin/env python3
from itertools import combinations, permutations, product

V=("A","B","C","D")
E=tuple("".join(x) for x in combinations(V,2))
ST={v:frozenset(e for e in E if v in e) for v in V}
B={1:"AB",2:"AC",3:"AD",4:"BC",5:"BD",6:"CD"}
IA=frozenset((1,2,3)); IB=frozenset((4,5,6))
J={"A":frozenset((1,2,3)),"B":frozenset((1,4,5)),"C":frozenset((2,4,6)),"D":frozenset((3,5,6))}
R={"AB":(1,1,0),"AC":(1,0,1),"AD":(0,1,-1),"BC":(0,1,1),"BD":(1,0,-1),"CD":(1,-1,0)}
S={"A":{"AB":-1,"AC":1,"AD":1},"B":{"AB":1,"BC":-1,"BD":-1},"C":{"AC":-1,"BC":1,"CD":1},"D":{"AD":1,"BD":-1,"CD":1}}

def add(vs): return tuple(sum(v[i] for v in vs) for i in range(3))
def sc(a,v): return tuple(a*x for x in v)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def ce(a,b): return "".join(sorted((a,b)))

assert all(len(ST[a]&ST[b])==1 for a,b in combinations(V,2))
assert all(sum(e in ST[v] for v in V)==2 for e in E)
assert {k:frozenset(B[i] for i in t) for k,t in J.items()}==ST
COMP=frozenset(B[i] for i in IB)
assert frozenset(B[i] for i in IA)==ST["A"]
assert COMP==frozenset(E)-ST["A"] and COMP not in set(ST.values())

U=set(range(1,7)); T=list(combinations(range(1,7),3)); D=set()
for four in combinations(T,4):
    Q=[frozenset(t) for t in four]
    if set().union(*Q)==U and all(sum(i in q for q in Q)==2 for i in U) and all(len(a&b)==1 for a,b in combinations(Q,2)):
        D.add(tuple(sorted(tuple(sorted(q)) for q in Q)))
assert len(D)==30
assert sum(tuple(sorted(IA)) in d for d in D)==6

acts=set()
for p in permutations(V):
    m=dict(zip(V,p)); ep={e:ce(m[e[0]],m[e[1]]) for e in E}
    image=frozenset(ep[e] for e in ST["A"])
    assert image in set(ST.values()) and image!=COMP
    acts.add(tuple(ep[e] for e in E))
assert len(acts)==24

for c,star in ST.items():
    es=tuple(sorted(star)); good=[]
    for signs in product((-1,1),repeat=3):
        vs=[sc(signs[k],R[e]) for k,e in enumerate(es)]
        if add(vs)==(0,0,0) and all(dot(vs[i],vs[j])==-1 for i,j in combinations(range(3),2)):
            good.append(dict(zip(es,signs)))
    assert len(good)==2 and any(all(g[e]==S[c][e] for e in star) for g in good)

global_good=0
for signs in product((-1,1),repeat=6):
    g=dict(zip(E,signs))
    ok=True
    for star in ST.values():
        es=tuple(sorted(star)); vs=[sc(g[e],R[e]) for e in es]
        if add(vs)!=(0,0,0) or not all(dot(vs[i],vs[j])==-1 for i,j in combinations(range(3),2)):
            ok=False; break
    global_good+=int(ok)
assert global_good==0

q={}
for a,b in combinations(V,2):
    e=next(iter(ST[a]&ST[b])); q[a,b]=q[b,a]=S[b][e]*S[a][e]
hol={a+b+c:q[a,b]*q[b,c]*q[c,a] for a,b,c in combinations(V,3)}
assert set(hol.values())=={-1}
for flips in product((-1,1),repeat=4):
    t=dict(zip(V,flips))
    for a,b,c in combinations(V,3):
        assert (t[b]*q[a,b]*t[a])*(t[c]*q[b,c]*t[b])*(t[a]*q[c,a]*t[c])==-1

R0=[(2,0,0),(1,3,0),(-1,3,0),(-2,0,0),(-1,-3,0),(1,-3,0)]
U3=[(1,1,1),(-1,1,1),(0,-2,1)]
FCC=R0+U3+[(0,2,-1),(-1,-1,-1),(1,-1,-1)]
HCP=R0+U3+[(1,1,-1),(-1,1,-1),(0,-2,-1)]
def ap(P):
    X=set(P)
    return {tuple(sorted((p,tuple(-x for x in p)))) for p in P if tuple(-x for x in p) in X}
assert len(ap(FCC))==6 and len(ap(HCP))==3

print("PASS")
print("k4_star_designs=30; containing_I_A=6; carrier_S4=24")
print("global_120_orientation_sections=0; triangle_Z2_holonomy=",hol)
print("FCC_antipodal_pairs=6; HCP_antipodal_pairs=3")
