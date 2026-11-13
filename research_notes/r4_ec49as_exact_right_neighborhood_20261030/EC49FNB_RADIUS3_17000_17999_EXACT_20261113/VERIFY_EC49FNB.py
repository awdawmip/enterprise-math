#!/usr/bin/env python3
"""EC49FNB certificate validation. Place frozen EC49FGW_RADIUS5_SCREEN.py and cases.json beside this file.
Independent exact lower bounds: python VERIFY_RADIUS3_SELECTED.py cases.json 17000 17965 17999.
"""
from pathlib import Path
import base64, hashlib, json, zlib
from EC49FGW_RADIUS5_SCREEN import PIN, all_words, pref, raw_key

P = Path(__file__).resolve().parent
d = json.loads((P / "EXACT_CERTIFICATE_EC49FNB.json").read_text())
assert d["source_pin"] == PIN == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
s = zlib.decompress(base64.b85decode(d["cost_vector_zlib_base85"])).decode("ascii")
assert hashlib.sha256(s.encode("ascii")).hexdigest() == d["cost_vector_ascii_sha256"]
v = list(map(int, s.split()))
assert len(v) == 1000 and d["range"] == [17000,17999]
assert min(v) == 96 and [17000+i for i,x in enumerate(v) if x == 96] == [17965]
assert max(v) == 204 and [17000+i for i,x in enumerate(v) if x == 204] == [17038,17212,17423]
cases = json.loads((P / "cases.json").read_text())
assert cases["pin"] == PIN and cases["count"] == 38169
assert cases["cases"][17965] == d["key_indices_17965"]
cat = list(all_words())
assert len(cat) == 178850
lawful = set(cat)
keys = sorted({raw_key(w) for _,w in cat})
assert len(keys) == 94
selected = {keys[i] for i in d["key_indices_17965"]}
assert len(d["legal_witness_17965"]) == 24
labels = set()
root_prefix = {}
for row in d["legal_witness_17965"]:
    label, word = tuple(row["label"]), row["word"]
    assert (label,word) in lawful and raw_key(word) in selected
    assert label not in labels
    labels.add(label)
    pp = pref(word)
    assert pp
    root_prefix.setdefault(pp[0].hex(),set()).update(pp)
assert len(labels)==24 and {r:len(p) for r,p in root_prefix.items()} == {"05":48, "06":48}
raw = P / "EXACT_NATIVE_OUTPUT_17000_17999.txt"
if raw.exists():
    b = raw.read_bytes()
    assert hashlib.sha256(b).hexdigest() == d["cpp_output_sha256"]
    rows = b.decode("utf-8").splitlines()
    assert len(rows) == 1000
    assert [(int(t[0]),int(t[1])) for line in rows if (t:=line.split())] == list(zip(range(17000,18000),v))
print("EC49FNB_PASS: 1000 costs, 24 lawful words, 96 distinct nonempty native prefixes")
