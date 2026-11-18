#!/usr/bin/env python3
"""EC49FMO exact 800-case vector and lawful 24-word witness verifier.

Usage:
  python VERIFY_EC49FMO.py
  python VERIFY_EC49FMO.py /path/to/unpacked/EC49FMN_input_directory

The optional directory holds cases.json, EC49FGW_RADIUS5_SCREEN.py,
EC49FGJ_SEVEN_KEY_94_WITNESSES.json and the original C++/master catalog.
"""
import base64
import collections
import hashlib
import json
import sys
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / "EXACT_DATA_EC49FMO.json").read_text())
costs = zlib.decompress(base64.b64decode(data["cost_uint8_zlib_base64"]))
assert len(costs) == 800 == data["cost_uint8_count"]
assert hashlib.sha256(costs).hexdigest() == data["cost_uint8_sha256"]
assert min(costs) == data["min_cost"] == 104
assert max(costs) == data["max_cost"] == 168
assert [i + data["from"] for i, c in enumerate(costs) if c == 104] == [5079]
assert {str(k):v for k,v in collections.Counter(costs).items()} == data["histogram"]
print("VECTOR_PASS", len(costs), min(costs), max(costs))

raw = HERE / "EXACT_NATIVE_OUTPUT_4700_5499.txt"
if raw.is_file():
    assert hashlib.sha256(raw.read_bytes()).hexdigest() == data["raw_output_sha256"]
    lines = [x.split() for x in raw.read_text().splitlines()]
    assert [int(x[0]) for x in lines] == list(range(4700, 5500))
    assert bytes(int(x[1]) for x in lines) == costs
    roots = collections.Counter(int(x[3]) for x in lines)
    assert {str(k):v for k,v in roots.items()} == data["first_root_counts"]
    print("RAW_800_ROWS_PASS")

source = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE
if not (source / "EC49FGW_RADIUS5_SCREEN.py").is_file():
    print("WITNESS_CHECK_PENDING: frozen generator and 94-key catalogue needed")
    sys.exit(0)
sys.path.insert(0, str(source))
from EC49FGW_RADIUS5_SCREEN import PIN, all_words, raw_key, pref
assert PIN == data["frozen_pin"]
cases = json.loads((source / "cases.json").read_text())
assert cases["pin"] == PIN and len(cases["cases"]) == 38169
types = sorted({raw_key(w) for lab, w in all_words()})
allowed = {types[k] for k in cases["cases"][5079]}
cat = {
    (tuple(lab), pref(w)[-1].hex()): pref(w)
    for lab, w in all_words() if raw_key(w) in allowed
}
obs = set()
prefixes = set()
for w in data["case_5079_witness"]["words"]:
    k = (tuple(w["label"]), w["word_hex"])
    assert k in cat, k
    obs.add(k[0])
    prefixes.update(cat[k])
assert len(obs) == 24 and len(prefixes) == 104
assert {p[0] for p in prefixes} == {5, 6}
print("CONSTRUCTIVE_WITNESS_PASS", len(obs), len(prefixes))
