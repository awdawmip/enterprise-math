#!/usr/bin/env python3
"""Exact finite checks for X6 upper V35-V36."""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from collections import Counter


def rank_q(rows):
    A=[list(map(Fraction,r)) for r in rows]
    if not A: return 0
    m=len(A); n=len(A[0]); rank=0
    for col in range(n):
        pivot=next((i for i in range(rank,m) if A[i][col]),None)
        if pivot is None: continue
        A[rank],A[pivot]=A[pivot],A[rank]
        p=A[rank][col]
        A[rank]=[x/p for x in A[rank]]
        for i in range(m):
            if i!=rank and A[i][col]:
                f=A[i][col]
                A[i]=[x-f*y for x,y in zip(A[i],A[rank])]
        rank+=1
        if rank==m: break
    return rank


def incidence(n,edges):
    B=[[0]*len(edges) for _ in range(n)]
    for k,(a,b) in enumerate(edges):
        B[a][k]-=1; B[b][k]+=1
    return B

def components(n,edges):
    adj=[set() for _ in range(n)]
    for a,b in edges: adj[a].add(b); adj[b].add(a)
    seen=set(); c=0
    for s in range(n):
        if s in seen: continue
        c+=1; stack=[s]; seen.add(s)
        while stack:
            x=stack.pop()
            for y in adj[x]:
                if y not in seen: seen.add(y); stack.append(y)
    return c

# Exhaustive simple graphs through n=5: incidence nullity = m-n+c.
graphs=0
trees=0
for n in range(1,6):
    possible=tuple(combinations(range(n),2))
    for mask in range(1<<len(possible)):
        edges=tuple(e for k,e in enumerate(possible) if mask>>k & 1)
        B=incidence(n,edges)
        r=rank_q(B)
        c=components(n,edges)
        nullity=len(edges)-r
        assert nullity==len(edges)-n+c
        if c==1 and len(edges)==n-1:
            assert nullity==0; trees+=1
        graphs+=1

# Triangle has one primitive cycle coordinate.
edges=((0,1),(1,2),(0,2))
B=incidence(3,edges)
assert len(edges)-rank_q(B)==1
# With reference orientation 0->1,1->2,0->2, cycle 0->1->2->0 is (1,1,-1).
c=(1,1,-1)
assert all(sum(B[v][e]*c[e] for e in range(3))==0 for v in range(3))
for m in range(-12,13):
    j=tuple(m*x for x in c)
    assert all(sum(B[v][e]*j[e] for e in range(3))==0 for v in range(3))

# Active-triad / V20 coupling.
N=6
TRIADS=tuple(combinations(range(N),3))
NEIGH={S:tuple(T for T in TRIADS if len(set(S)&set(T))==2) for S in TRIADS}

def perfect_matchings(items):
    items=tuple(items)
    if not items:
        yield (); return
    a=items[0]
    for k in range(1,len(items)):
        b=items[k]; rest=items[1:k]+items[k+1:]
        for mm in perfect_matchings(rest): yield tuple(sorted(((a,b),)+mm))
MATCHINGS=tuple(sorted(set(perfect_matchings(range(N)))))

def vmatch(M,S):
    S=set(S); bits=[]
    for a,b in M:
        if (a in S)+(b in S)!=1: return 0
        bits.append(1 if b in S else 0)
    return 1 if sum(bits)%2==0 else -1
V={S:tuple(vmatch(M,S) for M in MATCHINGS) for S in TRIADS}
K={(S,T):sum(a*b for a,b in zip(V[S],V[T])) for S in TRIADS for T in TRIADS}
for T in TRIADS:
    assert K[T,T]==6
    assert all(K[U,T]<6 for U in TRIADS if U!=T)


def ring_step(word):
    m=len(word); out=[]
    for i,S in enumerate(word):
        Y=word[(i+1)%m]
        assert Y in NEIGH[S]
        ranked=sorted(((K[T,Y],T) for T in NEIGH[S]),reverse=True)
        assert ranked[0]==(6,Y)
        assert ranked[0][0]>ranked[1][0]
        out.append(Y)
    return tuple(out)

def transport_slots(slotmap,S,T):
    common=set(S)&set(T); leave=next(iter(set(S)-common)); enter=next(iter(set(T)-common))
    out={a:slotmap[a] for a in common}; out[enter]=slotmap[leave]
    return out

def holonomy(word):
    slots={a:i for i,a in enumerate(word[0])}
    for i,S in enumerate(word): slots=transport_slots(slots,S,word[(i+1)%len(word)])
    return tuple(slots[a] for a in word[0])

# Exhaustive closed active walks of lengths 3 and 4: ring realization is shift.
closed=0; hols=set()
for m in (3,4):
    def dfs(path):
        global closed
        if len(path)==m:
            if path[0] in NEIGH[path[-1]]:
                W=tuple(path)
                assert ring_step(W)==W[1:]+W[:1]
                cur=W
                for _ in range(m): cur=ring_step(cur)
                assert cur==W
                hols.add(holonomy(W)); closed+=1
            return
        for T in NEIGH[path[-1]]: dfs(path+[T])
    for S in TRIADS: dfs([S])

assert hols==set(__import__('itertools').permutations((0,1,2)))
# Explicit examples of all S3 types.
assert holonomy(((0,1,2),(0,1,3),(0,1,4)))==(0,1,2)
assert holonomy(((0,1,2),(0,1,3),(0,2,3)))==(0,2,1)
assert holonomy(((0,1,2),(0,1,3),(1,2,3)))==(2,1,0)
assert holonomy(((0,1,2),(0,2,3),(1,2,3)))==(1,0,2)
assert holonomy(((0,1,2),(0,1,3),(0,2,3),(1,2,3)))==(2,0,1)
assert holonomy(((0,1,2),(0,1,3),(1,2,3),(0,2,3)))==(1,2,0)

print('PASS_X6_NETWORK_CIRCUIT_HOLONOMY_V35_V36')
print('simple_graphs_checked_n_le_5',graphs)
print('connected_trees_checked',trees)
print('triangle_cycle_rank',1)
print('closed_J633_walks_len_3_4_checked',closed)
print('S3_holonomy_elements_realized',len(hols))
print('directed_ring_realizes_every_checked_closed_walk',True)
