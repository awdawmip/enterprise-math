#!/usr/bin/env python3
"""Exact finite checks for the channel-frame gauge theorem."""
from itertools import permutations

N=6
PERMS=tuple(permutations(range(N)))
assert len(PERMS)==720


def inv(p):
    q=[0]*N
    for i,j in enumerate(p): q[j]=i
    return tuple(q)


def compose(p,q):
    return tuple(p[q[i]] for i in range(N))


def relabel_vector(v,h):
    hi=inv(h)
    return tuple(v[hi[c]] for c in range(N))


def relabel_matrix(M,h):
    hi=inv(h)
    return tuple(tuple(M[hi[c]][hi[d]] for d in range(N)) for c in range(N))


def relabel_frame(phi,h):
    # new channel c names old physical channel h^-1(c)
    return compose(phi,inv(h))


def push_vector(phi,v):
    out=[0]*N
    for c,a in enumerate(phi): out[a]=v[c]
    return tuple(out)


def push_matrix(phi,M):
    out=[[0]*N for _ in range(N)]
    for c,a in enumerate(phi):
        for d,b in enumerate(phi): out[a][b]=M[c][d]
    return tuple(tuple(row) for row in out)

# One nontrivial exact channel package with unequal entries makes label mistakes visible.
I=(1,2,3,5,7,11)
O=(13,17,19,23,29,31)
M=tuple(tuple((c+1)*10+(d+1) for d in range(N)) for c in range(N))

# Exhaustively verify gauge invariance for all 720 frame choices against all
# six adjacent transposition generators of channel relabeling.
gens=[]
for i in range(N-1):
    h=list(range(N)); h[i],h[i+1]=h[i+1],h[i]; gens.append(tuple(h))

checks=0
for phi in PERMS:
    pI=push_vector(phi,I); pO=push_vector(phi,O); pM=push_matrix(phi,M)
    for h in gens:
        ph=relabel_frame(phi,h)
        Ih=relabel_vector(I,h); Oh=relabel_vector(O,h); Mh=relabel_matrix(M,h)
        assert push_vector(ph,Ih)==pI
        assert push_vector(ph,Oh)==pO
        assert push_matrix(ph,Mh)==pM
        checks+=1

# The frame set is a free transitive right S6 torsor.
phi0=PERMS[0]
images={relabel_frame(phi0,h) for h in PERMS}
assert len(images)==720

# Fixed-name observer is not gauge invariant: reading raw channel 0 changes
# under a relabeling that swaps channels 0 and 1.
swap01=(1,0,2,3,4,5)
Ih=relabel_vector(I,swap01)
assert I[0]!=Ih[0]

print('PASS_X6_CHANNEL_FRAME_GAUGE_V1')
print('axis_channel_frames',len(PERMS))
print('generator_gauge_checks',checks)
print('frame_torsor_transitive',True)
print('raw_named_channel_observer_gauge_invariant',False)
