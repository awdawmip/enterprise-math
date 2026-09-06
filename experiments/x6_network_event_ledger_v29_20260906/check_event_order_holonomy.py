#!/usr/bin/env python3
"""Exact two-event order/relative-holonomy obstruction for X6 upper V30."""
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

C={S:tuple(vmatch(M,S) for M in MATCHINGS) for S in TRIADS}

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def matvec(A,v): return tuple(sum(A[i][j]*v[j] for j in range(4)) for i in range(4))
def addv(a,b): return tuple(x+y for x,y in zip(a,b))
def addm(A,B): return tuple(tuple(A[i][j]+B[i][j] for j in range(4)) for i in range(4))
def e(a,s=1): return tuple(s if i==a else 0 for i in range(4))
ZM=tuple(tuple(0 for _ in range(4)) for _ in range(4))
def K(a,b):
    A=[list(r) for r in ZM]; A[a][b]=1; A[b][a]=-1
    return tuple(tuple(r) for r in A)

def score(u,Om,S,T): return dot(u,C[T])+dot(C[S],matvec(Om,C[T]))
def successor(u,Om,S):
    ranked=sorted(((score(u,Om,S,T),T) for T in NEIGH[S]), reverse=True)
    assert ranked[0][0]>ranked[1][0]
    return ranked[0][1],ranked[0][0]-ranked[1][0]

def transport_slots(slotmap,S,T):
    common=set(S)&set(T)
    leave=next(iter(set(S)-common)); enter=next(iter(set(T)-common))
    out={a:slotmap[a] for a in common}; out[enter]=slotmap[leave]
    return out

def path_transport(path):
    slots={a:i for i,a in enumerate(path[0])}
    for S,T in zip(path,path[1:]): slots=transport_slots(slots,S,T)
    return tuple(slots[a] for a in path[-1])

u0=(-3,0,4,-1)
Om0=(
    (0,0,2,2),
    (0,0,1,1),
    (-2,-1,0,1),
    (-2,-1,-1,0),
)
A=('P01',addv(e(0),e(1,-1)),K(0,1))
B=('P10',addv(e(1),e(0,-1)),K(1,0))
S0=(3,4,5)

# Full nonnegative cumulative M increment is identical in either order.
M_AB=[[0]*4 for _ in range(4)]
M_AB[0][1]+=1; M_AB[1][0]+=1
M_BA=[[0]*4 for _ in range(4)]
M_BA[1][0]+=1; M_BA[0][1]+=1
assert M_AB==M_BA
assert all(v>=0 for r in M_AB for v in r)

def run(order):
    u,Om,S=u0,Om0,S0
    path=[S]; gaps=[]
    for _,du,dOm in order:
        u=addv(u,du); Om=addm(Om,dOm)
        S,gap=successor(u,Om,S)
        path.append(S); gaps.append(gap)
    return u,Om,S,tuple(path),tuple(gaps),path_transport(path)

ab=run((A,B)); ba=run((B,A))

assert ab[0]==ba[0]==u0
assert ab[1]==ba[1]==Om0
assert ab[2]==ba[2]==(0,3,4)
assert ab[3]==((3,4,5),(1,3,4),(0,3,4))
assert ba[3]==((3,4,5),(0,4,5),(0,3,4))
assert ab[4]==(1,1)
assert ba[4]==(3,5)
assert ab[5]==(2,0,1)
assert ba[5]==(0,2,1)
assert ab[5]!=ba[5]

# Relative slot transport is a transposition: compare which source slots land
# on each final axis.  Slot 1 agrees; slots 0 and 2 are exchanged.
assert ab[5][2]==ba[5][2]==1
assert {ab[5][0],ab[5][1]}=={ba[5][0],ba[5][1]}=={0,2}
assert ab[5][0]==ba[5][1] and ab[5][1]==ba[5][0]

print('PASS_X6_EVENT_ORDER_RELATIVE_HOLONOMY_V30')
print('event_multiset',('PASS_0_1','PASS_1_0'))
print('AB_active_path',ab[3])
print('BA_active_path',ba[3])
print('same_final_count_ledger',True)
print('same_final_contrast',True)
print('same_final_active_triad',ab[2])
print('AB_frame_transport',ab[5])
print('BA_frame_transport',ba[5])
print('relative_frame_difference','transposition')
