#!/usr/bin/env python3
"""EC49FQH phase certificate audit.

python EC49FQH_VERIFY_ALL_PRICE_FIRST_QUERIES.py <unpacked-EC49FQG-root> <new-certificates-directory>
All comparisons are exact rational/integer. The inherited verifier reconstructs
the native 228 response vectors, audits 25 endpoint certificates and replays 54
prior trees. This script replays 28 new trees and verifies the interval closure.
"""
from fractions import Fraction
from pathlib import Path
import runpy
import sys
import json
import hashlib

base, directory = map(Path, sys.argv[1:3])
prior = base / "code" / "EC49FQG_PALETTE_VERIFY.py"
saved_args = sys.argv
try:
    sys.argv = [str(prior), str(base / "EC49FQF_EVIDENCE")]
    verified = runpy.run_path(str(prior), run_name="__main__")
finally:
    sys.argv = saved_args

replay = verified["replay"]
info = verified["info"]
aliases = verified["alias_by_q"]
weights = verified["weights"]
sha = verified["sha"]
assert len(verified["V"]) == 228 and len(weights) == 141 and sum(weights) == 310
source_pin = verified["PIN"]
ratios = [(1,2),(16,31),(15,26),(13,22),(11,18),(5,8),(7,10),
          (5,7),(10,13),(18,23),(9,11),(8,9),(17,18),(2,1)]
samples = []
for r, t in ratios:
    name = f"EC49FQH_{r}_{t}.json"
    file = directory / name
    obj = json.loads(file.read_text())
    assert obj["prices"] == {"root": r, "terminal": t}
    assert obj["frozen_scientific_commit"] == source_pin
    assert obj["reps"] == verified["reps"] and obj["weights"] == weights
    assert obj["profile_count"] == 141 and obj["config_count"] == 310
    assert obj["observation_scope"] == "all_228"
    assert obj["source_master_sha256"] == verified["MASTER"]
    assert obj["native_root_costs_sha256"] == verified["CSV"]
    record = {"x": Fraction(r,t), "r":r, "t":t}
    for name, prefix, cost_field, opt_field, total_field in (
        ("uniform","U","first_query_costs_uniform","optimal_first_uniform","optimal_total_uniform"),
        ("config_weighted","M","first_query_costs_weighted",
         "optimal_first_config_weighted","optimal_total_config_weighted")):
        costs = obj[cost_field]
        assert len(costs) == 228
        best = min(costs)
        assert best == obj[total_field]
        first = [q for q in range(228) if costs[q] == best]
        assert first == obj[opt_field] and all(len(aliases[q]) == 1 for q in first)
        R,T,cost = replay(obj["trees"][name], name, r, t)
        assert cost == best
        record[prefix] = {"first":first,"R":R,"T":T,"cost":cost}
    record["sha256"] = sha(file)
    samples.append(record)

count = {}
for key, label, field in (
    ("uniform_endpoints","U","optimal_total_uniform"),
    ("multiplicity_endpoints","M","optimal_total_config_weighted")
):
    endpoints = []
    for ep in info[key]:
        file = base / "EC49FQF_EVIDENCE" / "certificates" / ep["full_certificate_file"]
        assert sha(file) == ep["full_certificate_sha256"]
        obj = json.loads(file.read_text())
        endpoints.append((Fraction(ep["r"],ep["t"]),
                          Fraction(obj[field],ep["t"]),ep["argmin_indices"]))
    intervals = 0
    for (a,va,A),(b,vb,B) in zip(endpoints,endpoints[1:]):
        witnesses = [s for s in samples if a < s["x"] < b]
        assert witnesses, (label,a,b)
        common = sorted(set(A) & set(B))
        assert len(common) == 2
        slope = (vb-va)/(b-a)
        intercept = va-slope*a
        assert slope.denominator == intercept.denominator == 1
        for s in witnesses:
            x = s["x"]
            assert Fraction(s[label]["cost"],s["t"]) == va+slope*(x-a)
            assert s[label]["first"] == common
            assert (s[label]["R"],s[label]["T"]) == (int(slope),int(intercept))
        intervals += 1
    count[label] = intervals
assert count == {"U":9,"M":14}
print("EC49FQH_ALL_14_INTERIOR_BELLMAN_AND_23_OPEN_PHASES_PASS")
print("Verified native class 16943, 228 physical queries, 14 exact interiors, 28 new replay trees.")
