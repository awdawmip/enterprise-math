#!/usr/bin/env python3
"""R5: exact all-prefix batch and monotone-event sweep on pinned original corpus.

Run from the stacked PR checkout:
python3 research_notes/brc_r5_batch_from_seed_20261112/VERIFY_R5_BATCH_FROM_PINNED.py

Imports the predecessor which performs full original-frozen-corpus checks first.
All research comparisons are rational/integer; benchmark timers are separate.
"""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter
from time import perf_counter
import json
import sys

base = Path(__file__).resolve().parents[1] / 'brc_r5_bp_derived_index_20261112'
sys.path.insert(0, str(base))
import VERIFY_R5_REBUILD_FROM_BP_LABELS as pinned

N = len(pinned.paths)
term = list(pinned.term2)
paths = list(pinned.paths)
pairs = list(pinned.pairs)
samples = list(pinned.prev.samples)
U = F(1, 23)
assert (N, sum(term), len(pairs), len(samples)) == (2880, 1065, 1065, 20)
assert Counter(q for q, n in pairs) == {3:538, 12:298, 15:229}

ids = {path:i for i, path in enumerate(paths)}
parent = [ids[path[:-1]] if path else -1 for path in paths]
terminal_ids = [i for i in range(N) if term[i]]
assert len(terminal_ids) == len(pairs)
assert sum(len(paths[i]) for i in terminal_ids) == 6379

def active(q, n, r):
    if r == U:
        return True
    d = 1 - 23*r
    assert d > 0
    return n*d.numerator <= 36*q*d.denominator

def batch(r):
    counts = [0]*N
    for i, (q,n) in zip(terminal_ids,pairs):
        counts[i] = int(active(q,n,r))
    for i in range(N-1,0,-1):
        counts[parent[i]] += counts[i]
    return counts

events = sorted(((1-F(36*q,n))/23,i)
                for i,(q,n) in zip(terminal_ids,pairs))
assert len(events) == 1065
assert len(set(t for t,i in events)) == 953

def sweep(sorted_parameters):
    counts=[0]*N
    next_event=0
    increments=0
    snapshots=[]
    for r in sorted_parameters:
        while next_event < len(events) and events[next_event][0] <= r:
            node=events[next_event][1]
            while node >= 0:
                counts[node]+=1
                increments+=1
                node=parent[node]
            next_event+=1
        snapshots.append(counts.copy())
    return snapshots,increments

total=0
for r in samples:
    values=batch(r)
    for i in range(N):
        assert values[i] == pinned.count(i,r)
        total+=1
assert total == 57600
assert batch(F(0))[0] == 605 and batch(U)[0] == 1065
for threshold in sorted(set(t for t,i in events)):
    assert pinned.count(0,threshold)==sum(active(q,n,threshold) for q,n in pairs)

ordered=sorted(samples)
snapshots,updates=sweep(ordered)
assert updates == 7444
assert all(v == batch(r) for r,v in zip(ordered,snapshots))
checksum=sum(sum(v) for v in snapshots)

def timing(f):
    elapsed=[]
    for _ in range(3):
        start=perf_counter()
        result=f()
        elapsed.append(perf_counter()-start)
        assert result == checksum
    return sorted(elapsed)[1]

wave_s=timing(lambda:sum(pinned.count(i,r) for r in samples for i in range(N)))
batch_s=timing(lambda:sum(sum(batch(r)) for r in samples))
sweep_s=timing(lambda:sum(sum(v) for v in sweep(ordered)[0]))

result={
  'status':'PASS_R5_BATCH_SWEEP_PINNED_REAL_1065',
  'original_certificates':len(pairs),
  'nodes':N,
  'activation_walls':953,
  'exact_prefix_comparisons':total,
  'sweep_ancestor_increments':updates,
  'root_zero':605,
  'root_endpoint':1065,
  'checksum':checksum,
  'wavelet_20_snapshots_sec_median3':round(wave_s,6),
  'batch_20_snapshots_sec_median3':round(batch_s,6),
  'sorted_sweep_20_snapshots_sec_median3':round(sweep_s,6),
  'timing_scope':'post-import, identical 20-parameter full snapshots; exact integer comparisons'
}
print(json.dumps(result,indent=2))
