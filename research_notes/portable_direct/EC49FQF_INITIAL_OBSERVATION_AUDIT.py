#!/usr/bin/env python3
"""EC49FQF: independent exact endpoint/first-observation evidence audit.

Usage:
 python EC49FQF_INITIAL_OBSERVATION_AUDIT.py EXTRACTED_EVIDENCE_ROOT MACHINE_SUMMARY_JSON

Evidence root contains source/frozen_original_master.txt,
source/EC49FPG_PROFILE.csv, certificates/EC49FQD_*.json and
certificates/EC49FQE_*.json, unpacked from the 2026-11-16 evidence bundle.

This audit checks original input hashes and every saved 228-query Bellman
first-branch array, but it does not independently rerun all Bellman recursions.
"""
import sys, json, hashlib
from pathlib import Path
from fractions import Fraction

root = Path(sys.argv[1])
summary = json.loads(Path(sys.argv[2]).read_text())
assert summary["schema"] == "EC49FQF_SHARP_INITIAL_OBSERVATION_PHASE_V1"
assert summary["source_pin"] == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert hashlib.sha256((root/"source/frozen_original_master.txt").read_bytes()).hexdigest() == summary["source_master_sha256"]
assert hashlib.sha256((root/"source/EC49FPG_PROFILE.csv").read_bytes()).hexdigest() == summary["source_root_csv_sha256"]
assert summary["counts"] == {"originals":310,"profiles":141,"terminal_queries":144,"root_queries":84}
for prior, prefix, switch in (("uniform", "EC49FQD", Fraction(153,184)),
                              ("multiplicity", "EC49FQE", Fraction(17,24))):
    rows = summary[prior+"_endpoints"]
    lines = summary["prior_phase_lines"][prior]
    assert len(rows)+1 == len(lines)
    earlier = Fraction(0)
    for ix, (a,b,optimal,best_root,best_terminal,first) in enumerate(rows):
        x = Fraction(a,b)
        assert earlier < x
        earlier = x
        p = root/"certificates"/(prefix+"_"+str(a)+"_"+str(b)+".json")
        d = json.loads(p.read_text())
        assert d["prices"] == {"root":a,"terminal":b}
        values = d["first_query_costs_uniform" if prior=="uniform" else "first_query_costs_weighted"]
        assert len(values) == 228
        target = d["optimal_total_uniform" if prior=="uniform" else "optimal_total_config_weighted"]
        assert target == optimal == min(values)
        assert best_root == min(values[144:]) and best_terminal == min(values[:144])
        q = [i for i, value in enumerate(values) if value==target]
        assert q == first == d["optimal_first_uniform" if prior=="uniform" else "optimal_first_config_weighted"]
        assert sum(v*c for v,c in zip(lines[ix],(a,b))) == target
        assert sum(v*c for v,c in zip(lines[ix+1],(a,b))) == target
        has_root = any(i>=144 for i in first)
        has_terminal = any(i<144 for i in first)
        if x < switch:
            assert has_root and not has_terminal
        elif x > switch:
            assert has_terminal and not has_root
        else:
            assert has_root and has_terminal
        print("ENDPOINT_PASS",prior,f"{a}/{b}",target,first)
for tail in summary["tail_checks"]:
    a,b=tail["root"],tail["terminal"]
    name = "EC49FQE_TAIL_LOW_1_4.json" if (a,b)==(1,4) else "EC49FQE_TAIL_HIGH_4_1.json"
    p = root/"certificates"/name
    raw = p.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == tail["full_certificate_sha256"]
    cert = json.loads(raw)
    assert cert["prices"] == {"root":a,"terminal":b}
    for prior in ("uniform","multiplicity"):
        key = "optimal_total_uniform" if prior=="uniform" else "optimal_total_config_weighted"
        init = "optimal_first_uniform" if prior=="uniform" else "optimal_first_config_weighted"
        assert cert[key] == tail[prior]
        assert cert[init] == tail[prior+"_initial"]
        if a < b:
            assert all(q>=144 for q in cert[init])
        else:
            assert all(q<144 for q in cert[init])
    print("TAIL_PASS",str(a)+"/"+str(b))
assert Fraction(153,184)-Fraction(4,7)==Fraction(335,1288)
assert Fraction(17,24)-Fraction(26,71)==Fraction(583,1704)
assert Fraction(153,184)-Fraction(17,24)==Fraction(17,138)
print("EC49FQF_ALL_25_ENDPOINTS_AND_TWO_TAILS_VERIFIED")
