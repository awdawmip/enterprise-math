#!/usr/bin/env python3
"""Exact frozen R5 radius-2 first-budget reconfiguration certificate.

All arithmetic integral/rational, no external dependencies. Reconstructs input
from pinned 15-atom coefficients, certifies optimality via DAG dynamic programming,
and checks the exact minimizing-pair edit distance for the unique gain-6 block.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
import json
from pathlib import Path

SCIENCE_PIN = '435e77af0d180eac32bd1f9c4c464bc4010b7551'
W = (336, 184, 18, 169, 64, 84, 299, 126, 52, 16, -420, -483, -144, -221, -80)
K0 = (-432, 0, 0, 0, 0, -108, 0, 0, 0, 0, 540, 0, 0, 0, 0)
pools = {3: set(), 12: set(), 15: set()}
mask = n = k = 0
for step in range(1, 1 << 15):
    bit = step & -step
    i = bit.bit_length() - 1
    mask ^= bit
    sign = 1 if mask & bit else -1
    n += sign * W[i]
    k += sign * K0[i]
    assert mask == (step ^ (step >> 1))
    if n >= 3 and k % 36 == 0 and k // 36 in pools:
        pools[k // 36].add(n)
assert tuple(len(pools[q]) for q in (3, 12, 15)) == (538, 298, 229)
thresholds = Counter(Fraction(p, q) for q, values in pools.items() for p in values)
assert len(thresholds) == 953
assert Counter(thresholds.values()) == {1: 869, 2: 56, 3: 28}
x = [0]
for wall in sorted(thresholds):
    x.append(x[-1] + thresholds[wall])
assert len(x) == 954 and x[-1] == 1065

blocks = []
start = 0
for i in range(1, len(x)):
    if x[i] - x[i - 1] > 2:
        blocks.append(x[start:i])
        start = i
blocks.append(x[start:])
assert len(blocks) == 29
assert sorted([x[i] - x[i-1] for i in range(1, len(x)) if x[i]-x[i-1]>2]) == [3]*28


def local_dp(xs, upto=None):
    """Exact path min-plus DP with counts of tied shortest paths."""
    N = len(xs)
    incoming = [[] for _ in xs]
    for p in range(N):
        for q in range(p+1, min(N, p+6)):
            middle = [min(xs[b]-xs[p], xs[q]-xs[b]) for b in range(p+1, q)]
            if all(d <= 2 for d in middle):
                incoming[q].append((p, sum(middle)))
    row = [None] * N
    for p in range(N):
        if xs[p]-xs[0] <= 2:
            row[p] = (sum(xs[p]-xs[b] for b in range(p)), 1)
    rows = [row]
    answers = {}
    for budget in range(1, min(N, upto or N) + 1):
        endings = [(p, entry[0] + sum(xs[b]-xs[p] for b in range(p+1, N)), entry[1])
                   for p, entry in enumerate(row) if entry and xs[-1]-xs[p] <= 2]
        if endings:
            best = min(cost for p, cost, count in endings)
            answers[budget] = (best, sum(count for p, cost, count in endings if cost==best))
        if budget == (upto or N):
            break
        new = [None]*N
        for q, edges in enumerate(incoming):
            cand = [(row[p][0]+w, row[p][1]) for p, w in edges if row[p] is not None]
            if cand:
                best = min(v for v, ct in cand)
                new[q] = (best, sum(ct for v, ct in cand if v==best))
        row = new
        rows.append(row)
    return answers, rows, incoming

component_records = []
for i, block in enumerate(blocks):
    ans, rows, edges = local_dp(block)
    kmin = min(ans)
    component_records.append({
        'block_index_0based': i, 'n': len(block), 'minimum_centers': kmin,
        'cost_at_minimum': ans[kmin][0],
        'first_extra_gain': ans[kmin][0]-ans[kmin+1][0]
    })
assert sum(item['minimum_centers'] for item in component_records) == 213
assert sum(item['cost_at_minimum'] for item in component_records) == 1070
assert sorted(item['first_extra_gain'] for item in component_records)[-2:] == [5,6]
assert [item['block_index_0based'] for item in component_records
        if item['first_extra_gain']==6] == [22]
assert sum(item['cost_at_minimum'] for item in component_records)-6 == 1064

b = blocks[22]
relative = [z-b[0] for z in b]
assert len(relative) == 38
ans, rows, incoming = local_dp(b, 10)
assert ans[9] == (42,12) and ans[10] == (36,640)

@lru_cache(None)
def prefixes(budget, q):
    if budget == 1:
        if rows[0][q] is not None:
            return ((q,),)
        return ()
    out = []
    for p, w in incoming[q]:
        if (rows[budget-2][p] is not None and
            rows[budget-2][p][0]+w == rows[budget-1][q][0]):
            for old in prefixes(budget-1, p):
                out.append((*old, q))
    return tuple(out)

def full_opt(budget):
    best, expected = ans[budget]
    result = []
    for q, entry in enumerate(rows[budget-1]):
        if entry is None or b[-1]-b[q] > 2:
            continue
        cost = entry[0]+sum(b[i]-b[q] for i in range(q+1, len(b)))
        if cost == best:
            result.extend(prefixes(budget, q))
    assert len(result) == expected and len(set(result)) == expected
    for chosen in result:
        dist = [min(abs(y-b[j]) for j in chosen) for y in b]
        assert max(dist) <= 2 and sum(dist) == best
    return result

opt9 = full_opt(9)
opt10 = full_opt(10)
edit_hist = Counter(len(set(a)-set(c)) for a in opt9 for c in opt10)
assert sum(edit_hist.values()) == 12*640
assert min(edit_hist) == 3
assert sorted(edit_hist) == [3,4,5,6,7,8]
pair = next((a,c) for a in opt9 for c in opt10 if len(set(a)-set(c))==3)
A = [relative[j] for j in pair[0]]
B = [relative[j] for j in pair[1]]
assert A == [1,5,10,15,20,25,30,35,40]
assert B == [1,5,10,13,18,23,26,30,35,40]

def brute(X):
    from itertools import combinations
    opts = {}
    for size in range(1, len(X)+1):
        for s in combinations(X, size):
            ds = [min(abs(y-z) for z in s) for y in X]
            if max(ds) > 2:
                continue
            cost = sum(ds)
            if size not in opts or cost < opts[size][0]:
                opts[size] = (cost, [s])
            elif cost == opts[size][0]:
                opts[size][1].append(s)
    return opts

small = (0,2,3,4,6)
small_results = brute(small)
assert small_results[2] == (5,[(0,4),(2,4),(2,6)])
assert small_results[3] == (2,[(0,3,6)])
assert all(not set(z).issubset(small_results[3][1][0])
           for z in small_results[2][1])

output = {
  'status':'PASS_EXACT',
  'science_pin':SCIENCE_PIN,
  'event_boundaries':len(x),
  'thresholds':len(thresholds),
  'events':x[-1],
  'separator_gaps':28,
  'blocks':len(blocks),
  'global_kmin':213,
  'global_J_kmin':1070,
  'global_J_kmin_plus_1':1064,
  'unique_gain_6_block_zero_based':22,
  'block22_relative_coordinates':relative,
  'block22_k9':{'cost':42,'optimum_count':len(opt9)},
  'block22_k10':{'cost':36,'optimum_count':len(opt10)},
  'optimum_pair_count_checked':len(opt9)*len(opt10),
  'removed_center_count_histogram':dict(sorted(edit_hist.items())),
  'minimum_removed_centers':min(edit_hist),
  'minimum_symmetric_difference':2*min(edit_hist)+1,
  'witness_k9_relative':A,
  'witness_k10_relative':B,
  'low_gain_3_counterexample':{
    'coordinates':small,
    'k2_cost':small_results[2][0],
    'k2_optima':small_results[2][1],
    'k3_cost':small_results[3][0],
    'k3_optima':small_results[3][1],
    'nested':False,
  },
  'verification':'Fraction thresholds; independent block min-plus count; exhaustive enumeration of optimal paths; direct exact cost feasibility for all 652 paths and 7680 optimal pairs; 5-point full-subset counterexample'
}
path = Path(__file__).with_name('EXACT_OUTPUT.json')
path.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(output,indent=2,ensure_ascii=False))
