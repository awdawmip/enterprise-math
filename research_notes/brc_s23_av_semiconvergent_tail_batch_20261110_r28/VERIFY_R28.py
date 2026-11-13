#!/usr/bin/env python3
"""Exact rational interval certificate for S23 Farey semiconvergent batch, R28.
Uses only Python stdlib. Optional positional argument: R27 EVENTS_R27.tsv.
Every strict sign test is at both endpoints of the frozen theta interval.
"""
from fractions import Fraction
from bisect import bisect_right
from hashlib import sha256
from pathlib import Path
import sys

D = 10**24
ENDPOINTS = (Fraction(262204504569236716045286, D),
             Fraction(262204504569236716045287, D))
M, Q, A, J, C, H, K = 128, 14298, 3749, 25339, 6644, 164, 9
CANDIDATES = set(range(J-164, J-97)) | set(range(J-61, J))
assert Q*C-J*A == 1
assert len(CANDIDATES) == M

predicted = {}
slacks = []
for side, theta in enumerate(ENDPOINTS):
    u = Q*theta-A
    v0 = C-J*theta
    assert 0 < u < 1 and 0 < v0
    assert v0-8*u > u > v0-9*u > 0
    cuts = sorted(((s*theta) % 1, s) for s in range(M))
    cut_positions = [x for x, _ in cuts]
    if side == 0:
        cut_ids_lo = [s for _,s in cuts]
        cut_floors_lo = [(s*theta)//1 for s in range(M)]
    else:
        assert cut_ids_lo == [s for _,s in cuts]
        assert cut_floors_lo == [(s*theta)//1 for s in range(M)]

    def owner(t):
        p = (t*theta) % 1
        idx = bisect_right(cut_positions, p)-1
        assert idx >= 0
        return idx

    # Source interval for new bracket at n=J+1: [J+1-Q, J),
    # and its H=164 terminal sources cover all M=128 old arcs.
    assert J+1-Q <= J-H
    base_owner = {t:owner(t) for t in range(J-H, J)}
    assert len(set(base_owner.values())) == M
    if side == 0:
        base_owner_lo = base_owner.copy()
    else:
        assert base_owner == base_owner_lo
    leaders = {}
    for t in range(J-H, J):
        leaders[base_owner[t]] = t
    assert set(leaders.values()) == CANDIDATES

    # The full interval is also certified: every floor(t*theta) is
    # unchanged across endpoints for the required finite t-range;
    # each signed cut-distance and the translation slack is affine.
    if side == 0:
        floors_lo = {t: (t*theta)//1 for t in range(J-H, J)}
        floors_hi = None
    else:
        for t in range(J-H, J):
            assert floors_lo[t] == (t*theta)//1
    for t, arc in base_owner.items():
        p = (t*theta) % 1
        successor = cut_positions[(arc+1) % M]
        if arc == M-1:
            successor += 1
        clearance = successor-p
        slack = clearance-K*u
        assert slack > 0
        slacks.append(slack)
        assert owner(t+K*Q) == arc
        if side == 0:
            assert (t+K*Q)*theta//1 == ((t+K*Q)*ENDPOINTS[1])//1
    for k in range(K+1):
        jk = J+k*Q
        ck = C+k*A
        vk = ck-jk*theta
        assert Q*ck-jk*A == 1 and vk > 0
        if k <= 8:
            assert vk > u
        else:
            assert vk < u
        # Necessary for a Farey bracket (left denominator q fixed).
        assert jk >= Q and jk+Q <= 10**12+128
        for t, arc in base_owner.items():
            assert owner(t+k*Q) == arc
        pairs = [(Q+t+k*Q+1, -A, Q) for t in leaders.values()]
        if k == K:
            pairs = [(n, ck, -jk) for n, _, _ in pairs]
        this = {n:(aa,bb) for n,aa,bb in pairs}
        assert len(this) == M
        assert all(jk+1 < n <= jk+Q for n in this)
        blocks=[]
        seq=sorted(this)
        start=prev=seq[0]
        for n in seq[1:]:
            if n > prev+1:
                blocks.append((start,prev,prev-start+1))
                start=n
            prev=n
        blocks.append((start,prev,prev-start+1))
        assert blocks == [(39474+k*Q, 39540+k*Q, 67),
                          (39577+k*Q, 39637+k*Q, 61)]
        if side == 0:
            predicted.update(this)
        else:
            assert {n:predicted[n] for n in this} == this

# Compact certificate: min slack is strictly positive over theta enclosure.
assert min(slacks) == 40342-153857*ENDPOINTS[1] > 0
assert len(predicted) == (K+1)*M
assert len({n for n in predicted if predicted[n]==(-A,Q)}) == 9*M
assert len({n for n in predicted if predicted[n]==(C+K*A,-(J+K*Q))}) == M

# Optional independent predecessor archive comparison (same frozen theta/observer).
if len(sys.argv)>1:
    predecessor={}
    for line in Path(sys.argv[1]).read_text().splitlines()[1:]:
        n,aa,bb=map(int,line.split('\t'))
        if J+1<=n<=J+(K+1)*Q:
            predecessor[n]=(aa,bb)
    assert predecessor == predicted, (len(predecessor),len(predicted),
                                     len(set(predecessor)^set(predicted)))

encoded=''.join(f'{n}\t{a}\t{b}\n' for n,(a,b) in sorted(predicted.items()))
print('PASS_R28_SEMICONVERGENT_TRANSLATION_CERTIFICATE')
print('q',Q,'j0',J,'K',K,'history',M,'tail',H)
print('theta_interval',ENDPOINTS)
print('leader_intervals',[(J-164,J-98,67),(J-61,J-1,61)])
print('min_clearance_minus_9u',min(slacks),float(min(slacks)))
print('positive_events',len(predicted),'regimes',K+1,'events_per_regime',M)
print('u_events',9*M,'v9_events',M)
print('event_SHA256',sha256(encoded.encode()).hexdigest())
print('predecessor_crosscheck', 'PASSED' if len(sys.argv)>1 else 'NOT_REQUESTED')
