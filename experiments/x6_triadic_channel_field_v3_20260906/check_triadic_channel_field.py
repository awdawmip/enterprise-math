#!/usr/bin/env python3
from itertools import permutations, product

S6=tuple(permutations(range(6)))
ID=tuple(range(6))

def compose(p,q): return tuple(p[q[i]] for i in range(6))
def inv(p): return tuple(p.index(i) for i in range(6))
def conj(g,u): return compose(compose(g,u),inv(g))

# Reference ordered active triad 0,1,2. Stabilizer fixes these pointwise and
# permutes complement 3,4,5.
H=tuple(p for p in S6 if p[0]==0 and p[1]==1 and p[2]==2)
assert len(H)==6
C=tuple(u for u in S6 if all(compose(u,h)==compose(h,u) for h in H))
assert len(C)==6
# Every centralizer element fixes complement pointwise and permutes active block.
assert all(u[3:]==(3,4,5) and set(u[:3])=={0,1,2} for u in C)

# Cyclic-origin invariance: commute with c=(012), leaving complement fixed.
c=(1,2,0,3,4,5)
Ccyc=tuple(u for u in C if compose(u,c)==compose(c,u))
assert len(Ccyc)==3
assert ID in Ccyc
nontrivial=[u for u in Ccyc if u!=ID]
assert len(nontrivial)==2
assert compose(nontrivial[0],nontrivial[1])==ID

# Equivariant rule transported to every ordered distinct-axis triad is
# well-defined independent of chosen g: test for one chosen reference u.
u0=nontrivial[0]
ordered=tuple(t for t in permutations(range(6),3))
# all g mapping reference tuple to t
for t in ordered:
    gs=[g for g in S6 if (g[0],g[1],g[2])==t]
    vals={conj(g,u0) for g in gs}
    assert len(vals)==1

# PF10 directed passage is invariant under internal R=(cyclic shift + sign flip).
def passage(t):
    a=[abs(x)-1 for x in t]
    return ((a[0],a[1]),(a[1],a[2]),(a[2],a[0]))
def R(t): return (-t[1],-t[2],-t[0])
frames=[]
for axes in permutations(range(6),3):
    for signs in product((-1,1),repeat=3):
        frames.append(tuple(s*(a+1) for a,s in zip(axes,signs)))
assert len(frames)==960
for t in frames:
    assert set(passage(R(t)))==set(passage(t))

# 40 directed unsigned passages, each fiber 24.
from collections import Counter
pc=Counter(frozenset(passage(t)) for t in frames)
assert len(pc)==40 and set(pc.values())=={24}

# Same active triad/chirality repeated gives C3 channel period.
assert compose(compose(u0,u0),u0)==ID

print('PASS_X6_TRIADIC_CHANNEL_FIELD_V3')
print('ordered_triad_stabilizer_order',len(H))
print('allowed_equivariant_active_channel_permutations',len(C))
print('cyclic_origin_invariant_rules',len(Ccyc))
print('nontrivial_channel_circulations',len(nontrivial))
print('full_signed_triad_frames',len(frames))
print('PF10_directed_passage_states',len(pc))
print('PF10_passage_fiber_size',next(iter(pc.values())))
print('passage_invariant_along_internal_R',True)
