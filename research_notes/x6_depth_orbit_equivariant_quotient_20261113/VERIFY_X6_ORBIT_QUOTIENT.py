#!/usr/bin/env python3
"""Exact finite signed-coordinate group, common-depth and orbit-quotient checks."""
import json
from collections import deque
from itertools import combinations, product

N = 6
ID = tuple(range(1,N+1))
ONES = (1,)*N

def compose(f,g):
    return tuple((1 if x>0 else -1)*f[abs(x)-1] for x in g)

def T(i,j,k,l=None):
    out=list(ID)
    out[i]=j+1; out[j]=k+1; out[k]=-(i+1)
    if l is not None:
        assert l not in (i,j,k)
        out[l]=-(l+1)
    return tuple(out)

def group(gens):
    seen={ID}; todo=deque([ID])
    while todo:
        a=todo.popleft()
        for b in gens:
            c=compose(a,b)
            if c not in seen:
                seen.add(c);todo.append(c)
    return seen

def act(g,vec):
    out=[0]*N
    for j,v in enumerate(g):
        out[abs(v)-1] += vec[j]*(1 if v>0 else -1)
    return tuple(out)

triads=list(combinations(range(N),3))
G1=group([T(*t) for t in triads])
G2=group([T(*t,l) for t in triads for l in range(N) if l not in t])
assert len(G1)==23040 and len(G2)==11520

def in_L1(v):
    return len({x%2 for x in v})==1

def in_L2(v):
    parity={x%2 for x in v}
    if len(parity)!=1:return False
    t=next(iter(parity))
    return (sum((x-t)//2 for x in v)%2)==0

def descenders(G):
    return sum(act(g,ONES) in (ONES,tuple(-x for x in ONES)) for g in G)

def kernel(G,belongs):
    return sum(all(belongs(tuple(x-y for x,y in zip(act(g,tuple(1 if j==i else 0 for j in range(N))), tuple(1 if j==i else 0 for j in range(N))))) for i in range(N)) for g in G)

assert descenders(G1)==descenders(G2)==720
assert kernel(G1,in_L1)==64
assert kernel(G2,in_L2)==1
L2mod4={}
for t in (0,1,2,3):
    for a in product((0,1),repeat=N):
        if sum(a)%2:continue
        v=tuple((t+2*x)%4 for x in a)
        L2mod4[v]=True
assert len(L2mod4)==64
assert all((v in L2mod4)==in_L2(v) for v in product(range(4),repeat=N))
assert 4**N//len(L2mod4)==64
e0=(1,0,0,0,0,0)
assert not in_L2(e0) and not in_L2((2,0,0,0,0,0)) and in_L2((4,0,0,0,0,0))
L1mod2={tuple(0 for _ in range(N)),ONES}
assert (2**N)//len(L1mod2)==32
assert all(in_L1(v)==(tuple(x%2 for x in v) in L1mod2) for v in product(range(4),repeat=N))
def min_zero(v):return tuple(x-min(v) for x in v)
zero=(0,)*N
x=ONES
w1=act(T(0,1,2),x)
w2=act(T(0,1,2,3),x)
assert min_zero(zero)==min_zero(x)
assert min_zero(act(T(0,1,2),zero))!=min_zero(w1)
assert min_zero(act(T(0,1,2,3),zero))!=min_zero(w2)
output={
  'method':'exact signed permutation BFS, integer lattice membership, exhaustive Z4^6 residue check',
  'frozen_science_commit':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
  'uncompensated':{'group_order':len(G1),'relative_observer_descenders':descenders(G1), 'universal_orbit_lattice':'Z*ones+2*Z^6','maximal_equivariant_depth_erasing_quotient':'(Z/2)^5','quotient_order':32,'action_kernel_order':kernel(G1,in_L1)},
  'compensated':{'group_order':len(G2),'relative_observer_descenders':descenders(G2),'universal_orbit_lattice':'Z*ones+2*D6; D6=even-coordinate-sum lattice','maximal_equivariant_depth_erasing_quotient':'Z/4 x (Z/2)^4','quotient_order':64,'action_kernel_order':kernel(G2,in_L2)},
  'mod4_complete_residue_cases':4**N,
  'compensated_orbit_lattice_mod4_size':len(L2mod4),
  'exact_relative_observer_witness':{'uncompensated_image_of_ones':w1,'uncompensated_relative_image':min_zero(w1),'compensated_image_of_ones':w2,'compensated_relative_image':min_zero(w2),'image_of_zero_relative':min_zero(zero)},
  'pass':True
}
print(json.dumps(output,ensure_ascii=False,indent=2))
