#!/usr/bin/env python3
"""Exact two-shift farthest-arc collision and forced-rank census (R284CY).

Run beside the unchanged, pinned R284CO_spectral_witness_checker.py.
The imported generator asserts the 65,536-site frozen SHA-256.
"""
import bisect
import json
from pathlib import Path
from R284CO_spectral_witness_checker import P, arcs, words, dist, FROZEN_SHA

SHIFTS = (("A", 6669045998, (19, 18)), ("B", 4503221351, (37, 21)))
X = words()
A = arcs()
assert len(X) == len(set(X)) == 65536
assert len(A) == 64 and all(0 < w < P//2 for _, w in A)
sites = set(X)
indices = {x: i for i, x in enumerate(X)}
farthest = {}
for x in X:
    values = [dist(x, a) for a in A]
    m = max(values)
    wins = [j for j, v in enumerate(values) if v == m]
    assert len(wins) == 1
    farthest[x] = (m, wins[0])

records = []
counts = {}
for label, delta, required_arcs in SHIFTS:
    links = sorted((x, (x+delta) % P) for x in X if (x+delta) % P in sites)
    collisions = []
    for x, y in links:
        vx, j = farthest[x]
        vy, l = farthest[y]
        if vx != vy:
            continue
        assert (j, l) == required_arcs
        ix, iy = indices[x], indices[y]
        assert ix//4096 == iy//4096
        changed = [p for p in range(12)
                   if ((ix%4096 >> (11-p)) & 1) != ((iy%4096 >> (11-p)) & 1)]
        assert changed == ([6] if label == "A" else [0, 1])
        collisions.append({"shift": label, "x": x, "y": y, "d64": vx,
                           "arcs": [j, l], "indices": [ix, iy],
                           "lower_changed": changed})
    counts[label] = {"delta": delta, "population_links": len(links),
                     "equal_farthest_pairs": len(collisions)}
    records.extend(collisions)
assert counts["A"]["population_links"] == 79
assert counts["B"]["population_links"] == 8
assert counts["A"]["equal_farthest_pairs"] == 6
assert counts["B"]["equal_farthest_pairs"] == 1
assert P-sum(A[19])+sum(A[18]) == SHIFTS[0][1]
assert A[21][0]-A[37][0] == SHIFTS[1][1]
assert len(records) == 7

# Sort exact integer order statistics. For a site's k-value, the final
# descending equal-value rank is the count of sites with value >= it.
chosen = {x for rec in records for x in (rec["x"], rec["y"])}
rows = [[] for _ in range(64)]
candidate_values = {}
for x in X:
    ds = sorted(dist(x, a) for a in A)
    for k in range(1, 64):
        rows[k].append(-ds[k])
    if x in chosen:
        candidate_values[x] = ds
for k in range(1, 64):
    rows[k].sort()

for rec in records:
    x, y, v = rec["x"], rec["y"], rec["d64"]
    left = bisect.bisect_left(rows[63], -v)+1
    right = bisect.bisect_right(rows[63], -v)
    assert right == left+1
    rec["rank_block"] = [left, right]
    rec["tau"] = {}
    rec["forcing_levels"] = {}
    for side, z in (("x", x), ("y", y)):
        ends = [bisect.bisect_right(rows[k], -candidate_values[z][k])
                for k in range(1, 64)]
        t = min(ends)
        rec["tau"][side] = t
        rec["forcing_levels"][side] = [k+2 for k, b in enumerate(ends) if b == t]
    rec["both_unforced_at_cutoff"] = all(t > left for t in rec["tau"].values())

exceptional = sorted(r["rank_block"][0] for r in records
                     if r["both_unforced_at_cutoff"])
absorbed = sorted(r["rank_block"][0] for r in records
                  if not r["both_unforced_at_cutoff"])
assert exceptional == [779, 1263, 1563, 7587]
assert absorbed == [3061, 3607, 6515]
result = {
    "schema": "R284CY_SEVEN_TRANSLATION_COLLISIONS_V1",
    "status": "AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED",
    "scope": "exactly shifts A and B, frozen Port population; not native X6",
    "source_module": "R284CO_spectral_witness_checker.py",
    "frozen_population_sha256": FROZEN_SHA,
    "modulus": P, "population": 65536, "labeled_arcs": 64,
    "all_farthest_arcs_unique": True, "shift_counts": counts,
    "records": records, "absorbed_tie_ranks": absorbed,
    "both_unforced_tie_ranks": exceptional,
    "global_minimum_core_classification_source": "R284CW"
}
out = Path(__file__).with_name("R284CY_seven_translation_collisions_certificate.json")
out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + chr(10), encoding="utf-8")
print(json.dumps({"counts": counts, "absorbed": absorbed, "unforced": exceptional}))
