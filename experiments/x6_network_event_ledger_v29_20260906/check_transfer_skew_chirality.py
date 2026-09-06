#!/usr/bin/env python3
"""Exact checks for X6 upper V33 transfer-skew chirality memory."""
from itertools import permutations

CELLS=(0,1,2)

def cycle_matrix(direction,m=1):
    # direction + implements context 0<-1<-2<-0: transfers 1->0,2->1,0->2.
    edges=((1,0),(2,1),(0,2)) if direction==1 else ((0,1),(1,2),(2,0))
    N=[[0]*3 for _ in range(3)]
    for a,b in edges: N[a][b]=m
    return tuple(tuple(r) for r in N)

def skew(N): return tuple(tuple(N[i][j]-N[j][i] for j in CELLS) for i in CELLS)

def incoming_context(N,x):
    A=skew(N)
    vals=sorted((A[y][x],y) for y in CELLS if y!=x, reverse=True)
    assert vals[0][0]>vals[1][0]
    return vals[0][1],vals[0][0]

def reinforce(N):
    N=[list(r) for r in N]
    chosen=[]
    for x in CELLS:
        y,_=incoming_context(tuple(tuple(r) for r in N),x)
        chosen.append((y,x))
    # Read contexts from the pre-layer state, then apply transfers as one layer.
    for y,x in chosen: N[y][x]+=1
    return tuple(tuple(r) for r in N),tuple(chosen)

for direction in (1,-1):
    for m in range(1,10):
        N=cycle_matrix(direction,m)
        A=skew(N)
        assert all(sum(r)==0 for r in A)
        contexts=tuple(incoming_context(N,x)[0] for x in CELLS)
        expected=(1,2,0) if direction==1 else (2,0,1)
        assert contexts==expected
        N2,chosen=reinforce(N)
        assert N2==cycle_matrix(direction,m+1)
        assert sum(map(sum,N2))==3*(m+1)

# The two orientations form the sign torsor under S3: even permutations preserve,
# odd permutations reverse.  Compare transported edge sets.
def perm_parity(p):
    return sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2

def permute_matrix(N,p):
    out=[[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3): out[p[i]][p[j]]=N[i][j]
    return tuple(tuple(r) for r in out)

plus=cycle_matrix(1)
minus=cycle_matrix(-1)
for p in permutations(CELLS):
    image=permute_matrix(plus,p)
    assert image==(minus if perm_parity(p) else plus)

# Zero transfer skew has no unique incoming positive-skew neighbor.
zero=((0,0,0),(0,0,0),(0,0,0))
for x in CELLS:
    vals=[skew(zero)[y][x] for y in CELLS if y!=x]
    assert vals==[0,0]

print('PASS_X6_TRANSFER_SKEW_CHIRALITY_V33')
print('ring_orientations',2)
print('orientation_torsor','S3/A3=C2')
print('reinforcement_levels_checked',18)
print('zero_skew_unique_orientation',False)
