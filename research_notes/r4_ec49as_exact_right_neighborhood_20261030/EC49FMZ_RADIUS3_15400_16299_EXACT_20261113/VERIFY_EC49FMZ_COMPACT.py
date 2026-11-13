#!/usr/bin/env python3
"""Check lossless finite-cost vector and ordered signed native-prefix witness.

This verifier checks certificate integrity, 900-row extrema, and the 24-word
prefix construction. For independent lower-bound DP and legal-word catalogue
membership checks, run VERIFY_EC49FMZ.py --deep from the full evidence bundle.
"""
import base64
import hashlib
import json
import sys
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
cert = json.loads((ROOT / "EXACT_CERTIFICATE_EC49FMZ.json").read_text(encoding="utf-8"))
assert cert["frozen_science"] == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
vec = zlib.decompress(base64.b64decode(cert["cost_vector"]["data"], validate=True))
assert hashlib.sha256(vec).hexdigest() == cert["cost_vector"]["uncompressed_sha256"]
assert len(vec) == cert["enumeration"]["count"] == 900
start, end = cert["enumeration"]["start"], cert["enumeration"]["end_inclusive"]
assert (start, end) == (15400, 16299)
lo, hi = min(vec), max(vec)
assert (lo, hi) == (cert["min"], cert["max"]) == (104, 202)
assert [start+i for i,x in enumerate(vec) if x == lo] == cert["minimizers"] == [15740]
assert [start+i for i,x in enumerate(vec) if x == hi] == cert["maximizers"] == [15604, 16047]
for key, expected in cert["python_independent_exact_checks"].items():
    assert vec[int(key)-start] == expected
case = cert["case_15740"]
assert vec[15740-start] == 104
raw = zlib.decompress(base64.b64decode(case["witness_file_data"], validate=True))
assert hashlib.sha256(raw).hexdigest() == case["witness_file_sha256"]
w = json.loads(raw)
assert w["pin"] == cert["frozen_science"]
assert w["seven_key_indices"] == case["keys"]
assert w["case_index"] == 15740
assert w["exact_optimal_cost"] == 104
assert w["label_count"] == 24
labels, all_pref, roots, word_count = set(), set(), {}, 0
for root in w["root_certificates"]:
    r = root["root_hex"]
    assert r not in roots
    root_pref = set()
    for rec in root["witnesses"]:
        word_count += 1
        labels.add(tuple(rec["label"]))
        assert isinstance(rec["word"], str) and rec["word"]
        path = rec["path_hex"]
        assert path and path[0] == r
        previous = ""
        for p in path:
            assert len(p) == len(previous)+2 and p.startswith(previous)
            bytes.fromhex(p)
            previous = p
            root_pref.add(p)
        assert path[-1].startswith(r)
    assert len(root_pref) == root["root_min_cost"]
    all_pref.update(root_pref)
    roots[r] = len(root_pref)
assert roots == case["first_step_root_counts"] == {"05":45,"06":39,"07":20}
assert len(labels) == 24
assert word_count == case["legal_word_count"] == 24
assert len(all_pref) == case["native_prefix_count"] == 104
assert sum(roots.values()) == 104
print("PASS 900 exact costs, min 104@15740, max 202@15604,16047")
print("PASS 24 lawfully sourced words; preserved signed ordered prefixes 45+39+20=104")
print("Frozen catalogue membership and independent lower-bound reruns require full evidence bundle.")
