#!/usr/bin/env python3
"""Verify the complete 1,200-value cost vector and two full native BRC witness choices.

This verifies complete vector conservation / finite-range extrema and explicit
constructive upper bounds. Matching exact lower bounds rely on the frozen
C++17 native prefix-trie/subset DP and independent Python computation.
When original catalogue and cases.json are available beside this script,
the legality and key-admissibility of both witnesses are also verified.
"""
from pathlib import Path
import base64, hashlib, json, zlib
P = Path(__file__).resolve().parent
x = json.loads((P / "EXACT_DATA_EC49FMX.json").read_text())
assert x["schema"] == "EC49FMX_EXACT_NATIVE_FINITE_CERTIFICATE_V1"
assert x["scientific_pin"] == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert x["range"] == [13300,14499] and x["count"] == 1200
v = zlib.decompress(base64.b64decode(x["cost_vector_zlib_base64"], validate=True))
assert len(v) == 1200 and hashlib.sha256(v).hexdigest() == x["cost_vector_sha256"]
assert min(v) == x["min_cost"] == 110 and max(v) == x["max_cost"] == 205
assert [i for i in range(13300,14500) if v[i-13300] == 110] == x["argmin"] == [14472,14473]
assert [i for i in range(13300,14500) if v[i-13300] == 205] == x["argmax"]
for k,c in x["sample_independent_python_costs"].items():
    assert v[int(k)-13300] == c
if (P / "EXACT_NATIVE_OUTPUT_13300_14499.txt").exists():
    b = (P / "EXACT_NATIVE_OUTPUT_13300_14499.txt").read_bytes()
    assert hashlib.sha256(b).hexdigest() == x["raw_original_output_sha256"]
    rows = [r.split() for r in b.decode().splitlines()]
    assert [int(r[0]) for r in rows] == list(range(13300,14500))
    assert bytes(int(r[1]) for r in rows) == v
letters = x["native_microsteps_per_letter"]
assert set(letters) == set("acdefg")
legal = keytypes = cases = None
if (P / "EC49FGW_RADIUS5_SCREEN.py").exists() and (P / "cases.json").exists():
    import sys
    sys.path.insert(0,str(P))
    from EC49FGW_RADIUS5_SCREEN import all_words, raw_key, PIN
    assert PIN == x["scientific_pin"]
    catalogue = list(all_words())
    assert len(catalogue) == 178850
    legal = set(catalogue)
    keytypes = sorted({raw_key(w) for lab,w in catalogue})
    assert len(keytypes) == 94
    cases = json.loads((P/"cases.json").read_text())
    assert cases["pin"] == PIN and len(cases["cases"]) == 38169
for i in x["argmin"]:
    d = x["witnesses"][str(i)]
    entries = d["label_word_pairs"]
    assert len(entries) == 24 and len({(h,lab) for h,lab,w in entries}) == 24
    assert all(len(w)==h for h,lab,w in entries)
    pref=set(); roots={}
    for h,lab,word in entries:
        if legal is not None:
            assert ((h,lab),word) in legal
            assert raw_key(word) in {keytypes[j] for j in d["key_indices"]}
        p=b""
        for c in word:
            for step in letters[c]:
                p += bytes([step+4])
                pref.add(p)
                roots.setdefault(f"{p[0]:02x}",set()).add(p)
    assert len(pref) == 110
    assert {r:len(t) for r,t in roots.items()} == x["first_root_prefix_costs"]
    if cases is not None:
        assert cases["cases"][i] == d["key_indices"]
    print("WITNESS_PASS",i,d["key_indices"],len(pref),{r:len(t) for r,t in roots.items()})
print("EC49FMX_PASS",len(v),min(v),x["argmin"],max(v),x["argmax"])
