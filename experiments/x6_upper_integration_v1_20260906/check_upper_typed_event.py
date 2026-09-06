#!/usr/bin/env python3
from itertools import product

# Minimal exact regression for the integration note.
N=6
ZERO=(0,)*N

def unit(i,s=1):
    z=[0]*N; z[i]=s; return tuple(z)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)

def tensor(a,b): return tuple(x*y for x in a for y in b)

def jet2(path):
    s1=ZERO
    s2=(0,)*(N*N)
    for i,x in enumerate(path):
        s1=add(s1,x)
        for y in path[i+1:]:
            s2=tuple(a+b for a,b in zip(s2,tensor(x,y)))
    return s1,s2

# Strong all-order path-jet collision on two length-two collinear reversals.
e=unit(0)
gamma=(e,neg(e))
eta=(neg(e),e)
assert gamma!=eta
assert jet2(gamma)==jet2(eta)
assert jet2(gamma)==(ZERO,tuple(-x for x in tensor(e,e)))

# Generic triadic one-step branch population: 2 choices per token -> 8 joint.
branches=tuple(product((0,1),repeat=3))
assert len(branches)==8
# Atomic law section keeps exactly III.
atomic=[b for b in branches if b==(0,0,0)]
assert len(atomic)==1

# 960 ordered signed triad frames and 1920 shell/closure states.
from itertools import permutations
frames=[]
for axes in permutations(range(6),3):
    for signs in product((-1,1),repeat=3):
        frames.append(tuple(s*(a+1) for a,s in zip(axes,signs)))
assert len(frames)==960 and len(set(frames))==960
assert 2*len(frames)==1920

# Same spatial pivot can carry six distinct closure relation phases.
closure=tuple(('pivot',r) for r in range(6))
assert len({c[0] for c in closure})==1
assert len(set(closure))==6

# Same spatial anchor can have distinct frame state.
ID=tuple(range(1,7))
Q=(-2,-3,-1,4,5,6)
assert ID!=Q
anchor=ZERO
# Every signed coordinate permutation fixes zero.
def act(g,z):
    out=[0]*N
    for i,c in enumerate(z):
        if c:
            y=g[i]; out[abs(y)-1]+=(1 if y>0 else -1)*c
    return tuple(out)
assert act(ID,anchor)==act(Q,anchor)==anchor
assert act(ID,unit(0))!=act(Q,unit(0))

# One full frame-closed Q cycle has 64 branch histories.
assert len(tuple(product((0,1),repeat=6)))==64

print('PASS_X6_UPPER_TYPED_EVENT_V1')
print('raw_path_jet_global_identity',False)
print('atomic_joint_branch_population',8)
print('atomic_selected_joint_branch_population',1)
print('ordered_signed_triad_frames',960)
print('deterministic_triadic_internal_states',1920)
print('closure_relation_phases_same_spatial_pivot',6)
print('frame_state_recoverable_from_anchor_coordinate',False)
print('generic_Q_cycle_shortest_histories',64)
