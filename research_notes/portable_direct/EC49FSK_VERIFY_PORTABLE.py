#!/usr/bin/env python3
"""Check EC49FSK proof objects (stdlib). Run:
python EC49FSK_VERIFY_PORTABLE.py /path/to/extracted/EC49FSJ_native_evidence [--recompute]
The source package must contain code/EC49FSA_THREE_OBSERVER_SOLVER.py and frozen source/.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import base64, hashlib, json, sys, zlib

HERE = Path(__file__).resolve().parent
SRC = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(SRC / "code"))
from EC49FSA_THREE_OBSERVER_SOLVER import V, PIN, solve
from EC49FRQ_INDEPENDENT_ALL228 import OBS, subset_keys
from EC49FQI_NATIVE_DATA import keys

c = json.loads((HERE / "EC49FSK_EXACT_CERTIFICATE.json").read_text())
assert PIN == c["frozen_pin"] == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert len(V) == len(OBS) == 228
assert all(len(r) == 141 for r in V)
assert all(tuple(OBS[i]) == tuple(V[i if i < 144 else 144 + keys.index(subset_keys[i - 144])]) for i in range(228))
for s in c["source_files"]:
    path = SRC / "source" / s["filename"]
    assert path.stat().st_size == s["bytes"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == s["sha256"]

packed = (HERE / "EC49FSK_EIGHT_WITNESS_TREES_ZLIB_BASE64.txt").read_text().strip().splitlines()[-1]
raw = zlib.decompress(base64.b64decode(packed))
assert hashlib.sha256(raw).hexdigest() == c["lossless_witness_bundle"]["raw_json_sha256"]
trees = json.loads(raw)

def full_tree_vector(tree):
    ctr = Counter()
    deepest = 0
    for state in range(141):
        node, seen, depth = tree, set(), 0
        while "named_observer" in node:
            name = node["named_observer"]
            assert isinstance(name, int) and 0 <= name < 228 and name not in seen
            ctr[name] += 1
            seen.add(name)
            depth += 1
            node = node["children"][str(V[name][state])]
        assert node == {"leaf": state}
        deepest = max(deepest, depth)
    return (sum(ctr.values()), ctr[32] + ctr[34], ctr[140]), deepest

a = Q(15, 32)
def score(p, z): return Q(p[0]) - p[1]*a - p[2]*z
planes = []
for phase in c["phases"]:
    p = (phase["U"], phase["Q"], phase["K"])
    key = "tree_" + "_".join(map(str,p)) + ".json"
    actual, max_depth = full_tree_vector(trees[key])
    assert actual == p and max_depth <= 4
    planes.append(p)
assert len(set(planes)) == 8 and len(set(p[2] for p in planes)) == 8
points = [(Q(z), Q(v)) for z,v in c["exact_vertices"]]
assert len(points) == 9 and points[0][0] == 0 and points[-1][0] == 1
for i,(z,value) in enumerate(points):
    assert min(score(p,z) for p in planes) == value
    if "--recompute" in sys.argv:
        info,_ = solve({32:a,34:a,140:z})
        assert Q(info["numerator"],info["denominator"]) == value
for i,phase in enumerate(c["phases"]):
    l,r = map(Q,phase["z"])
    assert l == points[i][0] and r == points[i+1][0]
    p = planes[i]; m = (l+r)/2
    assert all(score(p,m) < score(q,m) for q in planes if p != q)
print("PASS: frozen inputs; 228 fully named observations; 8 complete 141-profile trees; 9 exact endpoint receipts; 8 real intervals")
print("Independent second-decoder Bellman checks complete at z=0,1/6,39/224,7/24; remainder pending.")
