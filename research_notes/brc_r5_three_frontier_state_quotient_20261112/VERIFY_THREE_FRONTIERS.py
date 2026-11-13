#!/usr/bin/env python3
"""Exact R5 two-port activation-state quotient; standard-library-only verification.
Frozen W,K: R5 PR #2152. Inherited 28-coordinate word legality is NOT recomputed.
"""
from bisect import bisect_right
from collections import Counter, defaultdict
from fractions import Fraction as F

W = (336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K = (-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
QS = (3,12,15)
L = -F(427508577031693280,628800490619)
U = F(1,23)
M = 1 << 15
w, k = [0]*M, [0]*M
for mask in range(1,M):
    bit = mask & -mask
    j = bit.bit_length()-1
    w[mask] = w[mask ^ bit] + W[j]
    k[mask] = k[mask ^ bit] + K[j]

fixed_n = {-v for v in w if v <= -3}
candidates = defaultdict(list)
for mask in range(1,M):
    n, negk = -w[mask], -k[mask]
    if n in fixed_n and negk in (108,432,540):
        candidates[negk//36,n].append(mask)
assert (len(fixed_n),len(candidates),sum(map(len,candidates.values()))) == (1144,1065,2935)
by_q = {q:sorted(n for qq,n in candidates if qq==q) for q in QS}
assert tuple(len(by_q[q]) for q in QS) == (538,298,229)
tau = {(q,n):(1-F(36*q,n))/23 for q,n in candidates}
assert all(L<t<U for t in tau.values())
by_wall=defaultdict(list)
for pair,t in tau.items():
    by_wall[t].append(pair)
events=sorted(by_wall.items())
assert len(events)==953
assert Counter(len(v) for _,v in events)=={1:869,2:56,3:28}
assert events[0][0] == -F(179,23) and events[-1][0] == F(8,211)

def frontiers(r):
    assert L<=r<U
    h=1-23*r
    return tuple(bisect_right(by_q[q], F(36*q)/h) for q in QS)
def decode(counts):
    return {(q,n) for q,c in zip(QS,counts) for n in by_q[q][:c]}
def direct(r):
    return {p for p,t in tau.items() if t<=r}

states=[(0,0,0)]
for i,(r,pairs) in enumerate(events,1):
    inc=Counter(q for q,_ in pairs)
    states.append(tuple(states[-1][j]+inc[QS[j]] for j in range(3)))
    assert frontiers(r)==states[-1]
    assert decode(states[-1])==direct(r)
    before=events[i-2][0] if i>1 else L
    mid=(before+r)/2
    assert frontiers(mid)==states[-2]
    assert decode(states[-2])==direct(mid)
assert len(set(states))==len(states)==954
assert states[-1]==(538,298,229)
assert frontiers((events[-1][0]+U)/2)==states[-1]
assert frontiers(F(0))==(100,276,229)
assert sum(frontiers(F(0)))==605
keys=[r for r,_ in events]
for i,(r,_) in enumerate(events,1):
    ordinal=bisect_right(keys,r)
    assert ordinal==i and decode(states[ordinal])==direct(r)
assert (len(states)-1).bit_length()==10
assert tuple(len(by_q[q]).bit_length() for q in QS)==(10,9,8)

print("FROZEN_SUBSETS", M)
print("FIXED_FIRST_ZERO_N", len(fixed_n))
print("SELECTED_PAIR_KEYS", len(candidates))
print("CANDIDATE_MASKS", sum(map(len,candidates.values())))
print("FAMILY_COUNTS_Q3_Q12_Q15", *(len(by_q[q]) for q in QS))
print("DISTINCT_ACTIVATION_WALLS", len(events))
print("EVENT_MULTIPLICITY_COUNTS", dict(sorted(Counter(len(v) for _,v in events).items())))
print("ALL_REACHABLE_ACTIVE_SETS", len(states))
print("MINIMAL_FIXED_STATE_BITS", (len(states)-1).bit_length())
print("THREE_FRONTIER_COUNTER_BITS", sum(len(by_q[q]).bit_length() for q in QS))
print("ACTIVE_FRONTIERS_AT_R_ZERO", frontiers(F(0)))
print("ACTIVE_CERTIFICATES_AT_R_ZERO", sum(frontiers(F(0))))
print("FIRST_LAST_WALL", events[0][0], events[-1][0])
print("PASS_R5_THREE_FRONTIER_QUOTIENT_954_STATES")
