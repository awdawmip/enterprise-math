#!/usr/bin/env python3
"""Exact checks for X6 non-FCC observer switching V42-V43."""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations

# Fixed FCC carrier atlas order: AB, CD, AC, BD, BC, AD.
V=(
    (1,1,0),
    (1,-1,0),
    (1,0,1),
    (1,0,-1),
    (0,1,1),
    (0,1,-1),
)
CHARTS=tuple(combinations(range(6),3))


def matS(S):
    return tuple(tuple(V[idx][r] for idx in S) for r in range(3))

def det3(M):
    a,b,c=M[0]; d,e,f=M[1]; g,h,i=M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def inv3(M):
    A=[
        [Fraction(M[i][j]) for j in range(3)]
        + [Fraction(i==j) for j in range(3)]
        for i in range(3)
    ]
    for col in range(3):
        pivot=next(r for r in range(col,3) if A[r][col])
        A[col],A[pivot]=A[pivot],A[col]
        q=A[col][col]
        A[col]=[x/q for x in A[col]]
        for r in range(3):
            if r!=col and A[r][col]:
                q=A[r][col]
                A[r]=[x-q*y for x,y in zip(A[r],A[col])]
    return tuple(tuple(A[i][3+j] for j in range(3)) for i in range(3))

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)) for i in range(3))

def mv(A,x):
    return tuple(sum(A[i][j]*x[j] for j in range(3)) for i in range(3))

# V4/V5 rank split and flat direct rank-3 carrier atlas.
DETS={S:det3(matS(S)) for S in CHARTS}
STAR=tuple(S for S,d in DETS.items() if d==0)
RANK3=tuple(S for S,d in DETS.items() if d)
assert STAR==((0,2,5),(0,3,4),(1,2,4),(1,3,5))
assert len(STAR)==4 and len(RANK3)==16
assert all(abs(DETS[S])==2 for S in RANK3)

transition_checks=0
composition_checks=0
for S in RANK3:
    for T in RANK3:
        ATS=mm(inv3(matS(T)),matS(S))
        assert all(x.denominator==1 for row in ATS for x in row)
        assert abs(det3(ATS))==1
        transition_checks+=1
        for U in RANK3:
            AUT=mm(inv3(matS(U)),matS(T))
            AUS=mm(inv3(matS(U)),matS(S))
            assert mm(AUT,ATS)==AUS
            composition_checks+=1

# Same FCC point, different native X6 slice lift.
S_FACE=(0,2,4)  # AB,AC,BC
T_PATH=(0,1,2)  # AB,CD,AC
nS=(0,0,1)
y=mv(matS(S_FACE),nS)
nT=mv(inv3(matS(T_PATH)),y)
assert y==(0,1,1)
assert nT==(0,-1,1)
# Full X6 lifts: +BC versus -CD+AC.
xS=(0,0,0,0,1,0)
xT=(0,-1,1,0,0,0)
assert xS!=xT
assert sum(a*a for a in xS)==1
assert sum(a*a for a in xT)==2

# A6 stabilizer hierarchy of visible chart 012.
def parity(p):
    return sum(p[i]>p[j] for i in range(6) for j in range(i+1,6))%2
A6=tuple(p for p in permutations(range(6)) if parity(p)==0)
assert len(A6)==360
S0={0,1,2}
set_stab=tuple(p for p in A6 if {p[i] for i in S0}==S0)
assert len(set_stab)==18

def visible_parity(p):
    arr=(p[0],p[1],p[2])
    rank={x:i for i,x in enumerate(sorted(S0))}
    a=tuple(rank[x] for x in arr)
    return sum(a[i]>a[j] for i in range(3) for j in range(i+1,3))%2
cyclic_stab=tuple(p for p in set_stab if visible_parity(p)==0)
pointwise_stab=tuple(p for p in set_stab if all(p[i]==i for i in range(3)))
assert len(cyclic_stab)==9
assert len(pointwise_stab)==3
assert set(pointwise_stab)=={
    (0,1,2,3,4,5),
    (0,1,2,4,5,3),
    (0,1,2,5,3,4),
}

# Explicit hidden-C3 chart loop from V42.
ID=tuple(range(6))
def compose(p,q): return tuple(p[q[i]] for i in range(6))
def swap(a,b):
    p=list(ID); p[a],p[b]=p[b],p[a]; return tuple(p)
def edge_lift(S,T):
    S=set(S); T=set(T)
    assert len(S&T)==2
    a=next(iter(S-T)); b=next(iter(T-S))
    c,d=sorted(set(range(6))-(S|T))
    return compose(swap(a,b),swap(c,d))

loop=((0,1,2),(0,1,3),(0,3,4),(0,2,4),(0,1,2))
hol=ID
for S,T in zip(loop,loop[1:]):
    r=edge_lift(S,T)
    assert parity(r)==0
    hol=compose(r,hol)
assert hol==(0,1,2,4,5,3)
assert hol in pointwise_stab

# Reverse loop writes inverse hidden C3.
hol_rev=ID
rev=tuple(reversed(loop))
for S,T in zip(rev,rev[1:]): hol_rev=compose(edge_lift(S,T),hol_rev)
assert hol_rev==(0,1,2,5,3,4)
assert compose(hol,hol_rev)==ID

# Common-depth loss is independent of hidden frame.
def can3(n):
    m=min(n); return tuple(x-m for x in n),m
r0,h0=can3((0,0,0)); r1,h1=can3((1,1,1))
assert r0==r1==(0,0,0)
assert h0==0 and h1==1
assert sum(x*x for x in (0,0,0))==0
assert sum(x*x for x in (1,1,1))==3

print('PASS_X6_NONFCC_OBSERVER_SWITCH_V42_V43')
print('STAR_rank2_charts',len(STAR))
print('FACE_PATH_rank3_charts',len(RANK3))
print('GL3Z_transitions_checked',transition_checks)
print('flat_compositions_checked',composition_checks)
print('A6_setwise_stabilizer',len(set_stab))
print('A6_cyclic_visible_stabilizer',len(cyclic_stab))
print('A6_pointwise_visible_hidden_C3',len(pointwise_stab))
print('hidden_C3_loop',loop)
print('hidden_C3_holonomy',hol)
print('same_FCC_point_native_norm2_pair',(1,2))
print('normalized_STAR_repair_types','Z_common_depth x C3_hidden_frame')
