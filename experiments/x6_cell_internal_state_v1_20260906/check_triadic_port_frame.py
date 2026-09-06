#!/usr/bin/env python3
from collections import Counter
from itertools import permutations, product

# Signed direction is +/- (axis+1), axis in 0..5.
frames=[]
for axes in permutations(range(6),3):
    for signs in product((-1,1), repeat=3):
        frames.append(tuple(s*(a+1) for a,s in zip(axes,signs)))
assert len(frames)==960 and len(set(frames))==960


def sign(x): return 1 if x>0 else -1

def axis(x): return abs(x)-1

# Correct action of one fixed canonical Q_S=J_S rho_S on the three token
# provenance slots: each token moves to the next underlying axis and flips its
# OWN sign. Do not reorder the signed token values themselves.
def R(t):
    a=[axis(x) for x in t]; s=[sign(x) for x in t]
    return tuple((-s[r])*(a[(r+1)%3]+1) for r in range(3))


def F(state):
    t,mode=state
    return (t,1) if mode==0 else (R(t),0)

def io_support(t): return frozenset(abs(x) for x in t)
def passage(t):
    a,b,c=[abs(x) for x in t]
    return frozenset(((a,b),(b,c),(c,a)))

# Concrete mixed-sign regression against the superseded tuple-reordering rule.
def old_R(t): return (-t[1],-t[2],-t[0])
w=(1,-2,3)
assert R(w)==(-2,3,-1)
assert old_R(w)==(2,-3,-1)
assert R(w)!=old_R(w)

# Exact C6 orbits on the 960 ordered signed triad frames.
seen=set(); orbit_count=0
for t in frames:
    if t in seen: continue
    orb=[]; x=t
    for _ in range(6):
        orb.append(x); seen.add(x); x=R(x)
    assert x==t and len(set(orb))==6
    assert len({passage(y) for y in orb})==1
    orbit_count+=1
assert len(seen)==960 and orbit_count==160

# Shell/closure lift is exact C12 on every one of 1920 states.
for t in frames:
    for mode in (0,1):
        start=(t,mode); x=start; seq=[]
        for _ in range(12):
            seq.append(x); x=F(x)
        assert x==start and len(set(seq))==12

# Instantaneous PF-10-style quotient sizes under a chosen identity channel frame.
io_counts=Counter(io_support(t) for t in frames)
p_counts=Counter(passage(t) for t in frames)
assert len(io_counts)==20 and set(io_counts.values())=={48}
assert len(p_counts)==40 and set(p_counts.values())=={24}

# 6! axis-channel frame choices.
bridges=tuple(permutations(range(6)))
assert len(bridges)==720
identity=tuple(range(6))
transposition=(1,0,2,3,4,5)
assert tuple(transposition[i] for i in identity)!=identity

# Canonical Q family is covariant under unsigned axis relabelings.
def axis_swap(t,i):
    out=[]
    for x in t:
        s=sign(x); a=axis(x)
        if a==i: a=i+1
        elif a==i+1: a=i
        out.append(s*(a+1))
    return tuple(out)
for t in frames:
    for i in range(5): assert R(axis_swap(t,i))==axis_swap(R(t),i)

# Naive independent-sign equivariance of the canonical representative is false;
# full signed covariance is handled by the V5 four-twist bundle.
def sign_flip(t,i):
    return tuple(-x if axis(x)==i else x for x in t)
assert R(sign_flip(w,0))!=sign_flip(R(w),0)

# Cumulative PF-10 counts lose the active last-passage state.
A=(1,2,3)   # cycle 1->2->3->1
B=(1,3,2)   # opposite cycle on same support
assert io_support(A)==io_support(B)
assert passage(A)!=passage(B)

def aggregate(history):
    I=Counter(); O=Counter(); M=Counter()
    for t in history:
        for ch in io_support(t): I[ch]+=1; O[ch]+=1
        for e in passage(t): M[e]+=1
    return (tuple(sorted(I.items())),tuple(sorted(O.items())),tuple(sorted(M.items())))
assert aggregate((A,B))==aggregate((B,A))
assert passage(R(B))!=passage(R(A))

print('PASS_X6_CELL_INTERNAL_STATE_V1_CORRECTED')
print('ordered_signed_triad_frames',960)
print('triadic_C6_orbits',160)
print('decorated_shell_closure_states',1920)
print('axis_channel_bijections',720)
print('PF10_IO_support_states',20)
print('PF10_IO_fiber_size',48)
print('PF10_directed_passage_states',40)
print('PF10_passage_fiber_size',24)
print('canonical_independent_sign_equivariance',False)
print('cumulative_counts_markov_complete',False)
