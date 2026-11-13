#!/usr/bin/env python3
"""Verify EC49FMV exact 700-vector and ordered signed native BRC 24-word witness.
Full scientific membership check is enabled with frozen generator and catalogue.
"""
from pathlib import Path
from collections import Counter, defaultdict
import base64, hashlib, json, zlib
D = Path(__file__).resolve().parent
v = json.loads((D / "EXACT_VECTOR_EC49FMV.json").read_text())
w = json.loads((D / "WITNESS_12396_EC49FMV.json").read_text())
cost = zlib.decompress(base64.b64decode(v["cost_uint8_zlib_base64"], validate=True))
assert len(cost) == v["case_count"] == 700
assert (v["index_start"], v["index_end_inclusive"]) == (12100, 12799)
assert hashlib.sha256(cost).hexdigest() == v["cost_uint8_sha256"]
assert min(cost) == v["min_cost"] == 110 and max(cost) == v["max_cost"] == 205
assert [12100+i for i,c in enumerate(cost) if c == 110] == v["argmins"] == [12396]
assert [12100+i for i,c in enumerate(cost) if c == 205] == v["argmaxs"]
assert {str(k):n for k,n in Counter(cost).items()} == v["histogram"]
assert cost[0] == 130 and cost[-1] == 148
p = D / "EXACT_NATIVE_OUTPUT_12100_12799.txt"
if p.exists():
    assert hashlib.sha256(p.read_bytes()).hexdigest() == v["complete_raw_rows_sha256"]
    rr = [x.split() for x in p.read_text().splitlines()]
    assert len(rr) == 700
    assert [int(x[0]) for x in rr] == list(range(12100,12800))
    assert cost == bytes(int(x[1]) for x in rr)
    assert {str(k):n for k,n in Counter(int(x[3]) for x in rr).items()} == v["first_root_counts"]
for name,field in [
    ("master_and_radius3_cases.txt","frozen_catalogue_sha256"),
    ("cases.json","frozen_cases_sha256"),
    ("scan_cached_radius3.cpp","solver_source_sha256"),
    ("EC49FGW_RADIUS5_SCREEN.py","frozen_generator_sha256"),
    ("EC49FGJ_SEVEN_KEY_94_WITNESSES.json","catalogue_original_witness_sha256")]:
    f = D / name
    if f.exists(): assert hashlib.sha256(f.read_bytes()).hexdigest() == v[field],name
assert w["scientific_input_pin"] == v["scientific_input_pin"] == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert w["case_index"] == 12396 and w["cost"] == 110 and len(w["words"]) == 24
assert sum(w["root_costs"].values()) == 110
STEPS = {"a":(-1,-1),"c":(1,2,-1,-2),"d":(2,1,-2,-1),"e":(3,1,1,-3),"f":(1,-1),"g":(2,-2)}
assert set("".join(x[2] for x in w["words"])) <= set(STEPS)
prefixes = set()
roots = defaultdict(set)
seen = set()
for h,s,word in w["words"]:
    assert len(word) == h and (h,s) not in seen
    seen.add((h,s))
    pre = b""
    for ch in word:
        for d in STEPS[ch]:
            pre += bytes([d+4])
            prefixes.add(pre)
            roots[pre[:1].hex()].add(pre)
assert len(seen) == 24 and len(prefixes) == 110
assert {k:len(x) for k,x in roots.items()} == w["root_costs"]
try:
    from EC49FGW_RADIUS5_SCREEN import all_words,raw_key,PIN
    assert PIN == v["scientific_input_pin"]
    cat = set(all_words()); assert len(cat) == 178850
    keys = sorted({raw_key(word) for _,word in cat}); assert len(keys) == 94
    cases = json.loads((D / "cases.json").read_text())
    assert len(cases["cases"]) == 38169
    assert cases["cases"][12396] == w["seven_key_indices"]
    allowed = {keys[k] for k in w["seven_key_indices"]}
    for h,s,word in w["words"]:
        assert ((h,s),word) in cat and raw_key(word) in allowed
except ImportError:
    print("FROZEN_GENERATOR_MISSING: structural witness only")
print("EC49FMV_VERIFY_PASS",len(cost),min(cost),v["argmins"],max(cost),len(seen),len(prefixes))
