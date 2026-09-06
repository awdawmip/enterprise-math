#!/usr/bin/env python3
"""Exact finite checks for X6 upper V28 passage continuity and conservative bias."""
from __future__ import annotations

from itertools import combinations

N=6
TRIADS=tuple(combinations(range(N),3))
NEIGH={S:tuple(T for T in TRIADS if len(set(S)&set(T))==2) for S in TRIADS}
MATCHINGS=(
    ((0,1),(2,3),(4,5)),
    ((0,2),(1,4),(3,5)),
    ((0,3),(1,5),(2,4)),
    ((0,4),(1,3),(2,5)),
)

def vmatch(M,S):
    S=set(S); bits=[]
    for a,b in M:
        if (a in S)+(b in S)!=1: return 0
        bits.append(1 if b in S else 0)
    return 1 if sum(bits)%2==0 else -1

CODES={S:tuple(vmatch(M,S) for M in MATCHINGS) for S in TRIADS}
assert len(set(CODES.values()))==20

M=(
    (0,0,2,2),
    (0,0,1,1),
    (0,0,0,1),
    (0,0,0,0),
)
assert all(x>=0 for row in M for x in row)
row=tuple(sum(r) for r in M)
col=tuple(sum(M[i][j] for i in range(4)) for j in range(4))
assert row==(4,2,1,0)
assert col==(0,0,3,4)

OMEGA=tuple(tuple(M[i][j]-M[j][i] for j in range(4)) for i in range(4))
assert OMEGA==(
    (0,0,2,2),
    (0,0,1,1),
    (-2,-1,0,1),
    (-2,-1,-1,0),
)
div=tuple(sum(r) for r in OMEGA)
assert div==(4,2,-2,-4)
assert sum(div)==0

RIN=(0,0,6,3)
ROUT=(7,2,0,0)
assert sum(RIN)==sum(ROUT)==9
I=tuple(row[i]+RIN[i] for i in range(4))
O=tuple(col[i]+ROUT[i] for i in range(4))
U=tuple(I[i]-O[i] for i in range(4))
assert I==(4,2,7,3)
assert O==(7,2,3,4)
assert U==(-3,0,4,-1)
assert sum(I)==sum(O)==16
assert sum(U)==0
assert U==tuple(div[i]+RIN[i]-ROUT[i] for i in range(4))

# rank two: Pfaffian zero and nonzero 2x2 minor.
pf=OMEGA[0][1]*OMEGA[2][3]-OMEGA[0][2]*OMEGA[1][3]+OMEGA[0][3]*OMEGA[1][2]
assert pf==0
assert OMEGA[0][2]*OMEGA[2][0]!=0


def dot(a,b): return sum(x*y for x,y in zip(a,b))
def matvec(A,v): return tuple(sum(A[i][j]*v[j] for j in range(4)) for i in range(4))
def edge_a(S,T): return dot(CODES[S],matvec(OMEGA,CODES[T]))
def score(S,T): return dot(U,CODES[T])+edge_a(S,T)

def successor(S):
    ranked=sorted(((score(S,T),T) for T in NEIGH[S]),reverse=True)
    assert ranked[0][0]>ranked[1][0]
    return ranked[0][1],ranked[0][0]-ranked[1][0]

UPDATE={S:successor(S)[0] for S in TRIADS}
GAPS={S:successor(S)[1] for S in TRIADS}
assert min(GAPS.values())==1


def cycles_of_map(f):
    visited=set(); cycles=[]
    for start in TRIADS:
        if start in visited: continue
        path=[]; pos={}; cur=start
        while cur not in pos and cur not in visited:
            pos[cur]=len(path); path.append(cur); cur=f[cur]
        if cur in pos: cycles.append(tuple(path[pos[cur]:]))
        visited.update(path)
    return cycles

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

ODD=((0,3,4),(0,2,3),(2,3,5),(1,3,5),(0,1,5),(0,4,5))
CYCLES=cycles_of_map(UPDATE)
assert CYCLES==[ODD]
assert holonomy(ODD)==((1,0,2),1)
EDGE=[edge_a(ODD[i],ODD[(i+1)%6]) for i in range(6)]
assert EDGE==[3,1,2,2,1,3]
assert sum(EDGE)==12

# Closed unit triadic passage has zero completed-passage divergence.
M3=(
    (0,1,0,0),
    (0,0,1,0),
    (1,0,0,0),
    (0,0,0,0),
)
row3=tuple(sum(r) for r in M3)
col3=tuple(sum(M3[i][j] for i in range(4)) for j in range(4))
assert row3==col3==(1,1,1,0)

print('PASS_X6_PASSAGE_CONTINUITY_NETWORK_V28')
print('completed_passage_row_sums',row)
print('completed_passage_col_sums',col)
print('boundary_residual_totals',(sum(RIN),sum(ROUT)))
print('total_ingress_egress',(sum(I),sum(O)))
print('net_bias_sum',sum(U))
print('skew_rank',2)
print('minimum_score_gap',min(GAPS.values()))
print('odd_cycle',ODD)
print('odd_holonomy',holonomy(ODD))
print('cycle_circulation',sum(EDGE))
