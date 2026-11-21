#!/usr/bin/env python3
"""R284CZ exact d64 equality graph: all lower single flips and actual swaps."""
from R284CO_spectral_witness_checker import arcs, words, dist, FROZEN_SHA
from collections import Counter
from itertools import combinations
from bisect import bisect_left, bisect_right
from pathlib import Path
import json, hashlib

X = words()
A = arcs()
N = len(X)
F = []
for x in X:
    ds = [dist(x, a) for a in A]
    v = max(ds)
    winners = [i for i, d in enumerate(ds) if d == v]
    assert len(winners) == 1
    F.append((v, winners[0]))

links = []
edge_count = 0
for idx, (v, j) in enumerate(F):
    upper, lower = divmod(idx, 4096)
    for p in range(12):
        z = upper*4096+(lower^(1<<(11-p)))
        if z <= idx:
            continue
        edge_count += 1
        vv, l = F[z]
        if vv == v:
            links.append(("flip", str(p), idx, z, v, j, l))
    for p, q in combinations(range(12), 2):
        if ((lower>>(11-p)) & 1) == ((lower>>(11-q)) & 1):
            continue
        z = upper*4096+(lower^(1<<(11-p))^(1<<(11-q)))
        if z <= idx:
            continue
        edge_count += 1
        vv, l = F[z]
        if vv == v:
            links.append(("swap", f"{p},{q}", idx, z, v, j, l))

assert edge_count == 1474560 and len(links) == 307
counts = Counter((kind, mutation) for kind, mutation, *_ in links)
assert dict(counts) == {
    ("flip","2"):228, ("flip","6"):45, ("flip","4"):16,
    ("flip","1"):14, ("flip","0"):3, ("swap","0,1"):1
}

# Exact 63 nonconstant descending order-statistic rows with tied block endpoints.
selected = {X[i] for _,_,i,z,*_ in links} | {X[z] for _,_,i,z,*_ in links}
rows = [[] for _ in range(64)]
values = {}
for x in X:
    ds = sorted(dist(x, arc) for arc in A)
    for k in range(1,64):
        rows[k].append(-ds[k])
    if x in selected:
        values[x] = ds
for k in range(1,64):
    rows[k].sort()

tau = {}
for x in selected:
    ends = [bisect_right(rows[k], -values[x][k]) for k in range(1,64)]
    t = min(ends)
    tau[x] = (t, [k+2 for k, b in enumerate(ends) if b==t])

free = []
blocks = Counter()
for kind, mutation, idx, z, v, j, l in links:
    left = bisect_left(rows[63], -v)+1
    right = bisect_right(rows[63], -v)
    blocks[right-left+1] += 1
    if tau[X[idx]][0] > left and tau[X[z]][0] > left:
        free.append({
            "type":kind, "lower_mutation":mutation,
            "rank":left, "tie_end":right, "index_pair":[idx,z],
            "word_pair":[X[idx],X[z]], "critical_arcs":[j,l],
            "tau_pair":[tau[X[idx]][0],tau[X[z]][0]]
        })

assert len(free)==4 and sorted(e["rank"] for e in free)==[779,1263,1563,7587]
assert dict(blocks)=={2:290,3:7,4:10}
canonical_edges = [list(e) for e in links]
edge_bytes = json.dumps(canonical_edges,separators=(',',':'),ensure_ascii=False).encode('utf8')
cert = {
  "schema":"R284CZ_EXACT_NEIGHBOR_EQUALITY_GRAPH_V1",
  "status":"AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED",
  "source_module":"R284CO_spectral_witness_checker.py",
  "frozen_sha256":FROZEN_SHA,
  "population":N, "labeled_arcs":len(A), "all_farthest_arcs_unique":True,
  "graph_edges":edge_count, "equal_d64_edges":len(links),
  "equal_edges_by_mutation":{f"{a}:{b}":v for (a,b),v in sorted(counts.items())},
  "equal_edge_rank_block_lengths":{str(k):v for k,v in sorted(blocks.items())},
  "canonical_edge_tuple":"[kind,lower_mutation,source_index_small,source_index_large,d64,arc_at_small,arc_at_large]",
  "canonical_edge_list_sha256":hashlib.sha256(edge_bytes).hexdigest(),
  "both_endpoint_unforced_count":len(free),
  "both_endpoint_unforced_edges":free,
  "scope":"all 12 lower-bit flip edges and all unequal-entry lower swaps; top entries unchanged; frozen Port only",
  "global_core_classification_source":"R284CW"
}
Path(__file__).with_name("R284CZ_bit_neighbor_tie_certificate.json").write_text(
    json.dumps(cert,indent=2,ensure_ascii=False)+chr(10), encoding='utf8')
print(json.dumps({"edges":edge_count,"equal":len(links),"free":len(free),
                  "edge_sha":cert["canonical_edge_list_sha256"]}))
