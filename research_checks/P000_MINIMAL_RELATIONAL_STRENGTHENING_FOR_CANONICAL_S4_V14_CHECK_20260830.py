#!/usr/bin/env python3
"""Exact checker for P000 minimal relational strengthening V14 recovery."""

from collections import deque
from itertools import permutations, product

def comp(p,q): return tuple(p[q[i]] for i in range(len(p)))
def ppow(p,n):
    r=tuple(range(len(p)))
    for _ in range(n): r=comp(p,r)
    return r
def cycle(n,xs):
    p=list(range(n))
    for i,x in enumerate(xs): p[x]=xs[(i+1)%len(xs)]
    return tuple(p)
def gen(gens):
    e=tuple(range(len(gens[0]))); seen={e}; q=deque([e])
    while q:
        x=q.popleft()
        for g in gens:
            y=comp(g,x)
            if y not in seen: seen.add(y); q.append(y)
    return seen
def aut_graph(n, edges, partition=None):
    E={frozenset(e) for e in edges}
    if partition is None:
        cand=permutations(range(n))
    else:
        blocks=[list(permutations(b)) for b in partition]
        def build():
            for choices in product(*blocks):
                p=list(range(n))
                for block,ch in zip(partition,choices):
                    for old,new in zip(block,ch): p[old]=new
                yield tuple(p)
        cand=build()
    out=[]
    for p in cand:
        image={frozenset((p[i],p[j])) for i,j in (tuple(e) for e in E)}
        if image==E: out.append(p)
    return out

ID4=tuple(range(4))
A4=cycle(4,(1,2,3))
B4=cycle(4,(0,1))
S4=gen([A4,B4])
assert len(S4)==24
assert ppow(A4,3)==ID4 and ppow(B4,2)==ID4 and ppow(comp(A4,B4),4)==ID4

# Canonical one-relation package 1: K4 Cell adjacency.
K4_edges=[(i,j) for i in range(4) for j in range(i+1,4)]
K4aut=aut_graph(4,K4_edges)
assert len(K4aut)==24
pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
pindex={frozenset(x):i for i,x in enumerate(pairs)}
def edge_action(p):
    return tuple(pindex[frozenset((p[i],p[j]))] for i,j in pairs)
assert len({edge_action(p) for p in K4aut})==24
assert sum(edge_action(p)==tuple(range(6)) for p in K4aut)==1

# Canonical one-relation package 2: tetrahedral Cell-axis incidence.
inc=[]
for k,(i,j) in enumerate(pairs):
    e=4+k; inc.extend([(i,e),(j,e)])
IncAut=aut_graph(10,inc,partition=[list(range(4)),list(range(4,10))])
assert len(IncAut)==24
assert len({tuple(p[4+i]-4 for i in range(6)) for p in IncAut})==24

# Faithful-but-noncanonical one-relation package: K_{2,2,2,2}.
parts=[(0,1),(2,3),(4,5),(6,7)]
Wedges=[]
for a in range(4):
    for b in range(a+1,4):
        for i in parts[a]:
            for j in parts[b]:
                Wedges.append((i,j))
Waut=aut_graph(8,Wedges)
assert len(Waut)==384
def part(v): return v//2
qimgs=set(); kernel=[]
for p in Waut:
    q=tuple(part(p[2*i]) for i in range(4))
    assert all(part(p[2*i])==part(p[2*i+1]) for i in range(4))
    qimgs.add(q)
    if q==ID4: kernel.append(p)
assert len(qimgs)==24 and len(kernel)==16

# Gen13 no-lift adjacency regression.
P4aut=aut_graph(4,[(0,1),(1,2),(2,3)])
assert len(P4aut)==2

# Gen13 nonsplit GL(2,3) regression.
MI=(1,0,0,1); MMINUS=(2,0,0,2)
def mmul(A,B):
    return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2))%3
                 for i in range(2) for j in range(2))
def mpow(A,n):
    r=MI
    for _ in range(n): r=mmul(A,r)
    return r
def det(A): return (A[0]*A[3]-A[1]*A[2])%3
def mvec(A,v):
    return ((A[0]*v[0]+A[1]*v[1])%3,
            (A[2]*v[0]+A[3]*v[1])%3)
GL=[A for A in product(range(3),repeat=4) if det(A)]
P1=((1,0),(0,1),(1,1),(1,2)); pind={v:i for i,v in enumerate(P1)}
def canon(v):
    if v[0]:
        s=1 if v[0]==1 else 2
        return (1,v[1]*s%3)
    return (0,1)
def read(A): return tuple(pind[canon(mvec(A,v))] for v in P1)
assert len(GL)==48 and len({read(A) for A in GL})==24
assert {A for A in GL if read(A)==ID4}=={MI,MMINUS}
LA=[A for A in GL if read(A)==A4]
LB=[B for B in GL if read(B)==B4]
assert len(LA)==len(LB)==2
assert all(mpow(mmul(A,B),4)==MMINUS for A in LA for B in LB)

print("PASS P000_MINIMAL_RELATIONAL_STRENGTHENING_FOR_CANONICAL_S4_V14_CHECK")
print("S4_presentation_finite_image_order=24")
print("K4_adjacency_aut_order=24")
print("K4_edge_readout_kernel_order=1")
print("tetrahedral_incidence_aut_order=24")
print("K2222_aut_order=384")
print("K2222_readout_order=24")
print("K2222_kernel_order=16")
print("P4_aut_order=2")
print("GL23_order=48")
print("GL23_projective_image_order=24")
print("GL23_all_AB4_residue=-I")
print("native_relational_minimality_requires_frozen_grammar=true")
