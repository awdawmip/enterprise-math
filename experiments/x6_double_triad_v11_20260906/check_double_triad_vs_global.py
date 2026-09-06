#!/usr/bin/env python3
"""Exact checks for complementary-triad double-C6 frames versus global odd C12."""
from collections import deque, Counter
from itertools import combinations, permutations, product

N=6
ID=tuple(range(1,N+1)); NEG=tuple(-(i+1) for i in range(N))

def compose(g,h):
    out=[]
    for x in h:
        s=1 if x>0 else -1
        y=g[abs(x)-1]
        out.append(s*y)
    return tuple(out)
def inv(g):
    out=[None]*N
    for i,y in enumerate(g): out[abs(y)-1]=(1 if y>0 else -1)*(i+1)
    return tuple(out)
def conj(h,g): return compose(compose(h,g),inv(h))
def power(g,n):
    out=ID
    for _ in range(n): out=compose(g,out)
    return out
def qtri(S):
    i,j,k=S;q=list(ID);q[i]=-(j+1);q[j]=-(k+1);q[k]=-(i+1);return tuple(q)
def perm(g): return tuple(abs(x)-1 for x in g)
def parity(g):
    p=perm(g);return sum(p[i]>p[j] for i in range(N) for j in range(i+1,N))%2
def cycles(p):
    seen=set();out=[]
    for i in range(N):
        if i in seen: continue
        C=[];j=i
        while j not in seen: seen.add(j);C.append(j);j=p[j]
        out.append(tuple(C))
    return tuple(out)
def sign_hols(g):
    eps=[1 if x>0 else -1 for x in g]
    return tuple(__import__('math').prod(eps[i] for i in C) for C in cycles(perm(g)))
def act(g,z):
    out=[0]*N
    for i,c in enumerate(z):
        if c:
            y=g[i];out[abs(y)-1]+=(1 if y>0 else -1)*c
    return tuple(out)
def unit(i,s=1):
    z=[0]*N;z[i]=s;return tuple(z)
def add(a,b): return tuple(x+y for x,y in zip(a,b))

def signed_direction_orbits(g):
    states={unit(i,s) for i in range(N) for s in (-1,1)};orbs=[]
    while states:
        x=next(iter(states));orb=[];y=x
        while y not in orb:
            orb.append(y);states.discard(y);y=act(g,y)
        orbs.append(tuple(orb))
    return tuple(sorted(orbs,key=lambda o:(len(o),o)))

# 10 unordered complementary 3+3 decompositions.
parts=[];seen=set()
for S in combinations(range(N),3):
    T=tuple(i for i in range(N) if i not in S)
    key=frozenset((frozenset(S),frozenset(T)))
    if key not in seen: seen.add(key);parts.append((S,T))
assert len(parts)==10

# Four chirality choices per partition produce 40 distinct canonical frames.
CANON=set()
for S,T in parts:
    for es,et in product((1,-1),repeat=2):
        qs=qtri(S) if es==1 else inv(qtri(S))
        qt=qtri(T) if et==1 else inv(qtri(T))
        assert compose(qs,qt)==compose(qt,qs)
        h=compose(qs,qt)
        assert power(h,3)==NEG and power(h,6)==ID
        assert parity(h)==0
        assert tuple(sorted(map(len,cycles(perm(h)))))==(3,3)
        assert sign_hols(h)==(-1,-1)
        assert tuple(sorted(map(len,signed_direction_orbits(h))))==(6,6)
        CANON.add(h)
assert len(CANON)==40

# Full signed double-C6 class: positive cycle type (3,3), negative holonomy on both cycles.
B6=tuple(tuple(signs[i]*(p[i]+1) for i in range(N))
         for p in permutations(range(N)) for signs in product((-1,1),repeat=N))
DOUBLE=[]
for g in B6:
    C=cycles(perm(g))
    crit=(tuple(sorted(map(len,C)))==(3,3) and all(h==-1 for h in sign_hols(g)))
    if crit:
        assert power(g,3)==NEG and power(g,6)==ID and parity(g)==0
        assert tuple(sorted(map(len,signed_direction_orbits(g))))==(6,6)
        DOUBLE.append(g)
assert len(DOUBLE)==40*16==640

# Current R_triad is transitive by conjugation on the whole 640 class.
def closure(gens):
    G={ID};Q=deque([ID])
    while Q:
        h=Q.popleft()
        for g in gens:
            x=compose(g,h)
            if x not in G:G.add(x);Q.append(x)
    return G
R=closure(tuple(qtri(S) for S in combinations(range(N),3)))
REP=next(iter(CANON))
orb={conj(r,REP) for r in R}
assert orb==set(DOUBLE)
assert len(R)//len(orb)==36

# All-OUTER lift of the two signed C6 direction orbits gives two disjoint C12 Cell cycles.
orbs=signed_direction_orbits(REP)
outer_cycles=[]
for O in orbs:
    assert len(O)==6
    seq=[]
    for r,a in enumerate(O):
        b=O[(r+1)%6];m=add(a,b);seq.extend((a,m))
    assert len(seq)==12 and len(set(seq))==12
    outer_cycles.append(tuple(seq))
assert not (set(outer_cycles[0]) & set(outer_cycles[1]))
assert len(set(outer_cycles[0]+outer_cycles[1]))==24

# Canonical global odd C12 representative has one signed-direction orbit and one C24 outer cycle.
G=(2,3,4,5,6,-1)
Gorbs=signed_direction_orbits(G)
assert tuple(map(len,Gorbs))==(12,) and parity(G)==1
O=Gorbs[0]; gseq=[]
for r,a in enumerate(O): gseq.extend((a,add(a,O[(r+1)%12])))
assert len(gseq)==24 and len(set(gseq))==24

print('PASS_X6_DOUBLE_TRIAD_VS_GLOBAL_C12_V11')
print('complementary_triad_decompositions',len(parts))
print('canonical_chiral_double_triad_frames',len(CANON))
print('full_signed_double_C6_class',len(DOUBLE))
print('R_triad_conjugacy_stabilizer',len(R)//len(orb))
print('double_triad_signed_direction_orbits',(6,6))
print('double_triad_outer_Cell_topology','C12 + C12')
print('global_odd_outer_Cell_topology','C24')
