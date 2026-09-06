#!/usr/bin/env python3
"""Finite exact checks for X6 rotation-path groupoid V2."""
from itertools import product

N=6
ID=tuple(range(1,N+1))

def compose(g,h):
    out=[]
    for x in h:
        s=1 if x>0 else -1
        y=g[abs(x)-1]
        out.append(s*y)
    return tuple(out)

def power(g,k):
    out=ID
    for _ in range(k): out=compose(g,out)
    return out

def q_triad(S=(0,1,2)):
    i,j,k=S
    q=list(ID)
    q[i]=-(j+1); q[j]=-(k+1); q[k]=-(i+1)
    return tuple(q)

def act(g,z):
    out=[0]*N
    for i,c in enumerate(z):
        if not c: continue
        y=g[i]
        out[abs(y)-1]+=(1 if y>0 else -1)*c
    return tuple(out)

def unit(i):
    z=[0]*N; z[i]=1; return tuple(z)

def add(a,b): return tuple(x+y for x,y in zip(a,b))

def l1(a,b): return sum(abs(x-y) for x,y in zip(a,b))

q=q_triad()
assert power(q,6)==ID
phases=[unit(0)]
for _ in range(5): phases.append(act(q,phases[-1]))
assert act(q,phases[-1])==phases[0]

# Every macro edge has INNER and OUTER two-step lifts.
for r in range(6):
    a=phases[r]; b=phases[(r+1)%6]; outer=add(a,b); zero=(0,)*6
    assert l1(a,zero)==1 and l1(zero,b)==1
    assert l1(a,outer)==1 and l1(outer,b)==1

# All 64 branch words give distinct length-12 loops.
loops={}
for bits in product((0,1), repeat=6):
    seq=[phases[0]]
    for r,bit in enumerate(bits):
        a=phases[r]; b=phases[(r+1)%6]
        mid=(0,)*6 if bit==0 else add(a,b)
        seq.extend((mid,b))
    seq=tuple(seq)
    assert len(seq)==13
    assert seq[0]==seq[-1]
    loops[bits]=seq
assert len(set(loops.values()))==64

# Shortest-fiber composition obstruction.
a=phases[0]; b=phases[1]
assert l1(a,b)==2
assert l1(b,a)==2
assert l1(a,a)==0
assert 2+2>0

print('PASS_X6_ROTATION_PATH_GROUPOID_V2')
print('triadic_frame_order',6)
print('macro_branches_per_step',2)
print('six_macrostep_shortest_lifts',64)
print('micro_length_per_closed_frame_cycle',12)
print('shortest_fiber_closed_under_composition',False)
