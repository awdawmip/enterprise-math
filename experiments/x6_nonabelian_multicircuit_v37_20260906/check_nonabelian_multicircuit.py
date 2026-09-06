#!/usr/bin/env python3
"""Exact checks for X6 upper V37-V38 non-Abelian multi-circuit memory."""
from collections import Counter

A=((0,1,2),(0,1,3),(0,2,3))
Ai=((0,1,2),(0,2,3),(0,1,3))
B=((0,1,2),(0,2,3),(1,2,3))
Bi=((0,1,2),(1,2,3),(0,2,3))
BASE=(0,1,2)

def transport_slots(slotmap,S,T):
    common=set(S)&set(T)
    leave=next(iter(set(S)-common)); enter=next(iter(set(T)-common))
    out={a:slotmap[a] for a in common}; out[enter]=slotmap[leave]
    return out

def loop_transport(loop,slots=None):
    if slots is None: slots={a:i for i,a in enumerate(loop[0])}
    for i,S in enumerate(loop): slots=transport_slots(slots,S,loop[(i+1)%len(loop)])
    return slots

def hol(loop):
    s=loop_transport(loop)
    return tuple(s[a] for a in loop[0])

def seq_hol(loops):
    s={a:i for i,a in enumerate(BASE)}
    for L in loops: s=loop_transport(L,s)
    return tuple(s[a] for a in BASE)

assert hol(A)==hol(Ai)==(0,2,1)
assert hol(B)==hol(Bi)==(1,0,2)
assert seq_hol((A,B))==(2,0,1)
assert seq_hol((B,A))==(1,2,0)
assert seq_hol((A,B))!=seq_hol((B,A))

# Physical bow-tie circuits share Cell 0.
A_F=((1,0),(2,1),(0,2)); A_R=tuple((b,a) for a,b in A_F)
B_F=((3,0),(4,3),(0,4)); B_R=tuple((b,a) for a,b in B_F)
packet_edges={'A':A_F,'Ai':A_R,'B':B_F,'Bi':B_R}

def directional_counts(word):
    c=Counter()
    for name in word: c.update(packet_edges[name])
    return c

def net_skew(counts):
    pairs={tuple(sorted(e)) for e in counts}
    return {p:counts[p]-counts[(p[1],p[0])] for p in pairs}

# V37: AB and BA have identical directional event histograms, not only net current.
cAB=directional_counts(('A','B')); cBA=directional_counts(('B','A'))
assert cAB==cBA
assert seq_hol((A,B))!=seq_hol((B,A))

# V38 commutator vs grouped cancellation: same full event multiset, zero net current.
H1=('A','B','Ai','Bi')
H2=('A','Ai','B','Bi')
c1=directional_counts(H1); c2=directional_counts(H2)
assert c1==c2
assert all(v==0 for v in net_skew(c1).values())
h1=seq_hol((A,B,Ai,Bi)); h2=seq_hol((A,Ai,B,Bi))
assert h1==(1,2,0)
assert h2==(0,1,2)
assert h1!=h2

# Nonnegative counts are genuinely present even when net skew is zero.
assert sum(c1.values())==12
assert all(v==1 for v in c1.values())

print('PASS_X6_NONABELIAN_MULTICIRCUIT_V37_V38')
print('h_A',hol(A))
print('h_B',hol(B))
print('AB_holonomy',seq_hol((A,B)))
print('BA_holonomy',seq_hol((B,A)))
print('commutator_holonomy',h1)
print('grouped_cancellation_holonomy',h2)
print('same_full_directional_histogram',True)
print('commutator_net_cycle_current_zero',True)
