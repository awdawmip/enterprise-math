#!/usr/bin/env python3
"""Verify EC49FNE's exact cost vector and six legal native BRC witnesses.

Run beside the frozen original catalogue source EC49FGW_RADIUS5_SCREEN.py,
cases.json, and master_and_radius3_cases.txt from the original EC49FNB
full-evidence archive. This verifies recorded values and 24-word upper
bounds; re-run scan_cached_radius3.cpp for all 1000 optimality lower bounds.
"""
import base64, collections, hashlib, json, lzma, zlib
from pathlib import Path
from EC49FGW_RADIUS5_SCREEN import all_words, pref, raw_key, PIN

D = Path(__file__).resolve().parent
digest = lambda raw: hashlib.sha256(raw).hexdigest()
packed = base64.b64decode((D/'EXACT_CERTIFICATE_EC49FNE.json.xz.b64').read_text().strip())
cert = json.loads(lzma.decompress(packed).decode())
assert cert['pin'] == PIN == 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
master = (D/'master_and_radius3_cases.txt').read_bytes()
assert digest(master) == cert['master_sha256']
cost = zlib.decompress(base64.b85decode(cert['cost_base85']))
assert len(cost) == 2000 and digest(cost) == cert['cost_byte_sha256']
assert cert['range'] == [20000,21999] and cert['count'] == 2000
assert cert['minimum'] == min(cost) == 86
assert cert['maximum'] == max(cost) == 218
assert cert['minimizers'] == [20000+i for i,v in enumerate(cost) if v == 86]
assert cert['maximizers'] == [20000+i for i,v in enumerate(cost) if v == 218]
assert len(set(cost)) == cert['distinct_costs'] == 96

cases = json.loads((D/'cases.json').read_text())
assert cases['pin'] == PIN and len(cases['cases']) == 38169
catalog = list(all_words())
assert len(catalog) == 178850
keytypes = sorted({raw_key(w) for _,w in catalog})
assert len(keytypes) == 94
allowed = {(label, word): raw_key(word) for label,word in catalog}

for witness in cert['witnesses']:
    idx = witness['index']
    assert witness['keys'] == cases['cases'][idx]
    selected = {keytypes[j] for j in witness['keys']}
    labels = set()
    prefixes = set()
    per_root = collections.defaultdict(set)
    assert len(witness['words']) == 24
    for row in witness['words']:
        label = tuple(row['label'])
        word = row['word']
        assert label not in labels
        assert (label,word) in allowed and allowed[(label,word)] in selected
        labels.add(label)
        p = pref(word)
        prefixes.update(p)
        per_root[p[0].hex()].update(p)
    assert len(labels) == 24
    assert len(prefixes) == cost[idx - 20000] == 86
    assert {r:len(s) for r,s in per_root.items()} == {
        r:v for r,v in witness['root_counts'].items() if v>0}
    print('LEGAL_NATIVE_WITNESS_PASS',idx,len(labels),len(prefixes))

for row in cert['root_comparisons']:
    assert row['u_better']+row['equal']+row['v_better']==row['total']
print('LOSSLESS_VECTOR_AND_WITNESS_PASS',len(cost),cert['minimizers'])
