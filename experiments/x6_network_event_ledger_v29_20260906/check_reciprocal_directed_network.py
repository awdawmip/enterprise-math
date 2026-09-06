#!/usr/bin/env python3
"""Exact finite regressions for X6 upper V31-V32."""
from __future__ import annotations

from itertools import combinations, product
from collections import Counter

N=6
TRIADS=tuple(combinations(range(N),3))
NEIGH={S:tuple(T for T in TRIADS if len(set(S)&set(T))==2) for S in TRIADS}


def perfect_matchings(items):
    items=tuple(items)
    if not items:
        yield (); return
    a=items[0]
    for k in range(1,len(items)):
        b=items[k]
        rest=items[1:k]+items[k+1:]
        for m in perfect_matchings(rest):
            yield tuple(sorted(((a,b),)+m))

MATCHINGS=tuple(sorted(set(perfect_matchings(range(N)))))
assert len(MATCHINGS)==15

def vmatch(M,S):
    S=set(S); bits=[]
    for a,b in M:
        if (a in S)+(b in S)!=1: return 0
        bits.append(1 if b in S else 0)
    return 1 if sum(bits)%2==0 else -1

V={S:tuple(vmatch(M,S) for M in MATCHINGS) for S in TRIADS}
K={(S,T):sum(a*b for a,b in zip(V[S],V[T])) for S in TRIADS for T in TRIADS}
assert set(K.values())=={-6,-2,2,6}
for S in TRIADS:
    assert K[S,S]==6
    comp=tuple(i for i in range(N) if i not in S)
    assert K[S,comp]==-6
    assert all(K[T,S]<6 for T in TRIADS if T!=S)

# Three-cell complete reciprocal equal-coupling regression.
def reciprocal_update(state):
    out=[]
    for i,S in enumerate(state):
        ranked=sorted((sum(K[T,state[j]] for j in range(3) if j!=i),T) for T in NEIGH[S], reverse=True)
        if ranked[0][0]==ranked[1][0]: return None
        out.append(ranked[0][1])
    return tuple(out)

states=tuple(product(TRIADS,repeat=3))
mapping={s:reciprocal_update(s) for s in states if reciprocal_update(s) is not None}
assert len(mapping)==2700
visited=set(); cycles=[]
for start in mapping:
    if start in visited: continue
    path=[]; pos={}; cur=start
    while cur in mapping and cur not in pos and cur not in visited:
        pos[cur]=len(path); path.append(cur); cur=mapping[cur]
    if cur in pos: cycles.append(tuple(path[pos[cur]:]))
    visited.update(path)
assert Counter(map(len,cycles))==Counter({2:1350})


def transport_slots(slotmap,S,T):
    common=set(S)&set(T)
    leave=next(iter(set(S)-common)); enter=next(iter(set(T)-common))
    out={a:slotmap[a] for a in common}; out[enter]=slotmap[leave]
    return out

def holonomy(cycle):
    base=cycle[0]; slots={a:i for i,a in enumerate(base)}
    for i,S in enumerate(cycle):
        slots=transport_slots(slots,S,cycle[(i+1)%len(cycle)])
    perm=tuple(slots[a] for a in base)
    parity=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))%2
    return perm,parity

# All unordered J(6,3) triangles.
triangles=[]
for A,B,C in combinations(TRIADS,3):
    if B in NEIGH[A] and C in NEIGH[A] and C in NEIGH[B]:
        triangles.append((A,B,C))
assert len(triangles)==120
assert Counter(holonomy(t)[1] for t in triangles)==Counter({0:60,1:60})

# Directed 3-ring: each site observes only the next site.  On any triangle,
# the next site's exact state is admissible and has unique K-score 6.
def directed_ring_update(state):
    out=[]
    for i,S in enumerate(state):
        Y=state[(i+1)%3]
        assert Y in NEIGH[S]
        ranked=sorted((K[T,Y],T) for T in NEIGH[S], reverse=True)
        assert ranked[0][0]==6 and ranked[0][1]==Y
        assert ranked[0][0]>ranked[1][0]
        out.append(Y)
    return tuple(out)

for tri in triangles:
    s0=tri
    s1=directed_ring_update(s0)
    s2=directed_ring_update(s1)
    s3=directed_ring_update(s2)
    assert s1==(tri[1],tri[2],tri[0])
    assert s2==(tri[2],tri[0],tri[1])
    assert s3=s0

CURVED=((0,1,2),(0,1,3),(0,2,3))
FLAT=((0,1,2),(0,1,3),(0,1,4))
assert holonomy(CURVED)==((0,2,1),1)
assert holonomy(FLAT)==((0,1,2),0)

print('PASS_X6_RECIPROCAL_DIRECTED_NETWORK_V31_V32')
print('reciprocal_three_cell_states',len(states))
print('unique_reciprocal_successor_states',len(mapping))
print('reciprocal_period2_cycles',len(cycles))
print('J633_triangles',len(triangles))
print('flat_triangles',60)
print('odd_triangles',60)
print('directed_ring_period',3)
print('curved_example_holonomy',holonomy(CURVED))
