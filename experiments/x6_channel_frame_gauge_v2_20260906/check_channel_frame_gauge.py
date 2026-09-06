#!/usr/bin/env python3
from itertools import permutations

S6=tuple(permutations(range(6)))
ID=tuple(range(6))

def compose(p,q): return tuple(p[q[i]] for i in range(6))
def inv(p): return tuple(p.index(i) for i in range(6))
def conj(g,u): return compose(compose(g,u),inv(g))

# Stabilizer of axis 0 is S5 on labels 1..5.
stab0=tuple(p for p in S6 if p[0]==0)
assert len(stab0)==120
centralizer=tuple(u for u in S6 if all(compose(u,h)==compose(h,u) for h in stab0))
assert centralizer==(ID,)

# Any fully equivariant direction-local transport assignment is determined by
# U_0 and U_0 must be in the trivial centralizer, hence all U_i are identity.
U0=centralizer[0]
Us=[]
for i in range(6):
    g=next(p for p in S6 if p[0]==i)
    Us.append(conj(g,U0))
assert all(u==ID for u in Us)

# Translation-invariant square holonomy is commutator; demonstrate commuting
# flat and noncommuting twisted examples.
swap01=(1,0,2,3,4,5)
swap12=(0,2,1,3,4,5)

def comm(u,v): return compose(compose(compose(inv(u),inv(v)),u),v)
assert comm(ID,swap01)==ID
assert comm(swap01,swap12)!=ID

# 6! global gauge frames.
assert len(S6)==720

print('PASS_X6_CHANNEL_FRAME_GAUGE_V2')
print('axis_channel_global_gauge_frames',len(S6))
print('axis_stabilizer_order',len(stab0))
print('stabilizer_centralizer_order',len(centralizer))
print('fully_S6_equivariant_pure_translation_transport','IDENTITY')
print('noncommuting_transport_has_square_holonomy',True)
