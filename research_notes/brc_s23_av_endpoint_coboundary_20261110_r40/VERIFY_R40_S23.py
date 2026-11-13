#!/usr/bin/env python3
"""Reproduce R40 exact last-source ages in frozen S23/AV at trillion horizon.

Requires the co-located published VERIFY_R40.py; uses only rational integer
arithmetic for the frozen S23 theta enclosure.
"""
from fractions import Fraction as Q
import hashlib, json
from VERIFY_R40 import Observer, CoboundarySelector, independent_last

D=10**24
TLO=262204504569236716045286
THI=262204504569236716045287
M=128
J=10**12+128
N=10**9
lo,hi=Q(TLO,D),Q(THI,D)
obs=Observer(lo,hi,M)
selector=CoboundarySelector(obs,J,N)
last,stats=selector.solve(range(M))
ref,oracle_calls=independent_last(obs.arcs,J-N,J,(lo+hi)/2)
assert [last[i] for i in range(M)]==ref
assert all(last[i] is not None for i in range(M))
ages={J-last[i] for i in range(M)}
assert ages==set(range(1,107)) | set(range(143,165))
assert all(c>0 for c in selector.all_counts(J-164))
assert sum(c>0 for c in selector.all_counts(J-163))==127
for i,t in last.items():
    assert selector.all_counts(t)[i]>0
    assert selector.all_counts(t+1)[i]==0
    assert obs.owner(t,lo)==i and obs.owner(t,hi)==i
raw=json.dumps([last[i] for i in range(M)],separators=(',',':'))
digest=hashlib.sha256(raw.encode()).hexdigest()
print('S23 exact J',J,'N',N,'owners',M,'max_age',max(ages))
print('age intervals [1,106] and [143,164]; missing [107,142]')
print('distinct thresholds',selector.unique_thresholds,'certified scalar floor endpoints',selector.boundary_scalar_calls,'independent Euclidean sums',2*oracle_calls)
print('last-source-owner-vector SHA256',digest)
print('PASS_R40_FROZEN_S23_TRILLION_LAST_SOURCE_128_128')
