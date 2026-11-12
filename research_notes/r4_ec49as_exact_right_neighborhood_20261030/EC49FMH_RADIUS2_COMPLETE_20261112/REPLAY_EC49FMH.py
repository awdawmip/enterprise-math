#!/usr/bin/env python3
"""EC49FMH complete radius-two signed-X6 proof data and legal witness verifier.

Default: decode/exactly check all 4695 recorded integer minima; reconstruct the
frozen 178850-word BRC catalogue, 6315 coverable configurations and a fully
lawful 24-label / 84-native-prefix witness at global index 5883.

--original-cpp: independently recompute 21 selected fixed-key optima with the
unchanged pre-cache C++ exact solver. --run-all: recompute all 4695 optima.
No floating-point arithmetic is used in either path.
"""
import base64
import collections
import hashlib
import itertools
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import zlib

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "EC49FJD_RELEASE_B11_COMPLETE_20261111"))
from EC49FGW_RADIUS5_SCREEN import PIN, all_words, pref, raw_key

E = json.loads((HERE / "EXACT_VECTOR_EC49FMH.json").read_text())
assert E["scientific_pin"] == PIN == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert E["global_slice"] == [1620, 6315] and E["number_of_records"] == 4695
raw = zlib.decompress(base64.b64decode(E["compressed_cost_vector_b64"], validate=True))
assert len(raw) == 4695
assert hashlib.sha256(raw).hexdigest() == E["decoded_cost_vector_sha256"]
costs = list(raw)
assert min(costs) == 84 and [i + 1620 for i, n in enumerate(costs) if n == 84] == [5883]
assert dict(collections.Counter(str(n) for n in costs)) == E["histogram"]
print("EC49FMH_LOSSLESS_4695_INTEGER_COST_VECTOR_PASS", flush=True)

catalog = list(all_words())
assert len(catalog) == 178850
labels = sorted(set(lab for lab, _ in catalog))
assert [f"{a}:{b}" for a, b in labels] == E["explicit_witness"]["observer_labels"]
lid = {lab: i for i, lab in enumerate(labels)}
catalog_set = set(catalog)
bykey, support = collections.defaultdict(list), collections.defaultdict(int)
for lab, word in catalog:
    key = raw_key(word)
    support[key] |= 1 << lid[lab]
    bykey[key].append((lid[lab], pref(word)[-1].hex()))
assert len(support) == 94
base = {(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}
outside = sorted(set(support) - base)
cases = []
for removed in itertools.combinations(sorted(base), 2):
    for added in itertools.combinations(outside, 2):
        keys = sorted((base - set(removed)) | set(added))
        mask = 0
        for k in keys: mask |= support[k]
        if mask == (1 << 24) - 1: cases.append(keys)
assert len(cases) == 6315
cert = E["explicit_witness"]
idx = cert["global_index"]
assert idx == 5883 and sorted(map(tuple, cert["cache_keys"])) == cases[idx]
assert len(cert["words"]) == cert["word_count"] == len(labels) == 24
unique_prefixes = set()
for lab, word in zip(labels, cert["words"]):
    assert (lab, word) in catalog_set and raw_key(word) in set(cases[idx])
    unique_prefixes.update(pref(word))
assert len(unique_prefixes) == cert["unique_ordered_signed_native_prefixes"] == costs[idx-1620] == 84
print("EC49FMH_FROZEN_CATALOG_6315_COVERABLE_CASES_PASS", flush=True)
print("EC49FMH_24_WORD_NATIVE_SIGNED_PREFIX_WITNESS_PASS", idx, len(unique_prefixes), flush=True)

if "--original-cpp" in sys.argv or "--run-all" in sys.argv:
    src = ROOT / "EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112" / "SCAN_7KEY_GENERAL.cpp"
    selected = list(range(1620, 6315)) if "--run-all" in sys.argv else E["independent_cpp_indices"]
    with tempfile.TemporaryDirectory() as dirname:
        d = Path(dirname)
        with (d/"cases.txt").open("w") as f:
            f.write(str(len(selected)) + "\n")
            for idx in selected:
                rows = [pair for key in cases[idx] for pair in bykey[key]]
                f.write(str(len(rows)) + "\n")
                for lab, native in rows: f.write(f"{lab} {native}\n")
        subprocess.run(["g++","-std=c++17","-O3",str(src),"-o",str(d/"exact")],check=True)
        with (d/"cases.txt").open("rb") as r, (d/"result.txt").open("wb") as w:
            subprocess.run([str(d/"exact")],stdin=r,stdout=w,check=True)
        lines = (d/"result.txt").read_text().splitlines()
        assert len(lines) == len(selected)
        for j, (idx, line) in enumerate(zip(selected, lines)):
            fields = line.split()
            assert int(fields[0]) == j and int(fields[1]) == costs[idx-1620]
    print("EC49FMH_ORIGINAL_CPP_EXACT_PASS", len(selected), flush=True)
