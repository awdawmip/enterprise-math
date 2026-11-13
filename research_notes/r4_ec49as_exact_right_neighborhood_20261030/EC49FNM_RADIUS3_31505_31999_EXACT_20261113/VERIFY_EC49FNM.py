#!/usr/bin/env python3
"""Verify EC49FNM compact output and original signed-native witness words.
Run beside the frozen EC49FGW_RADIUS5_SCREEN.py and
EC49FGJ_SEVEN_KEY_94_WITNESSES.json plus the complete raw evidence files.
This checks certificate integrity; the original/independent subset DP
is needed to reproduce optimality from scratch.
"""
import base64, hashlib, json, lzma
from pathlib import Path
from EC49FGW_RADIUS5_SCREEN import all_words, pref, raw_key, PIN

D = Path(__file__).resolve().parent
b64 = (D / 'EXACT_CERTIFICATE_EC49FNM.json.xz.b64').read_text().strip()
c = json.loads(lzma.decompress(base64.b64decode(b64, validate=True)))
assert c['schema'] == 'EC49FNM_31505_31999_EXACT_CERTIFICATE_V1'
assert c['frozen_pin'] == PIN == 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert c['indices'] == [31505, 31999]
assert len(c['costs']) == len(c['optimal_root_assignment_counts']) == 495
assert min(c['costs']) == 108 and max(c['costs']) == 196
assert [31505+i for i, v in enumerate(c['costs']) if v == 108] == list(range(31505, 31532))
assert c['optimal_root_assignment_counts'][:27] == [1]*27
assert c['second_assignment_cost_31505_31531'] == [
    115 if i == 31516 else 116 for i in range(31505, 31532)]
input_path = D/'master_and_radius3_cases.txt'
assert hashlib.sha256(input_path.read_bytes()).hexdigest() == c['full_input_sha256']
cases = json.loads((D/'cases.json').read_text())
assert cases['pin'] == PIN and cases['count'] == 38169
cat = list(all_words())
assert len(cat) == 178850
legal = set(cat)
keytypes = sorted({raw_key(w) for _, w in cat})
for case_str, entries in c['witnesses'].items():
    idx = int(case_str)
    assert idx in (31505, 31516)
    keys = cases['cases'][idx]
    assert keys == c['witness_key_indices'][case_str]
    allowed = {keytypes[j] for j in keys}
    original = {(tuple(entry['label']), entry['word']) for entry in entries}
    assert len(original) == 24 and {lab for lab,_ in original} == {lab for lab,_ in cat}
    assert original <= legal and all(raw_key(w) in allowed for _, w in original)
    prefixes = {p for _, w in original for p in pref(w)}
    assert len(prefixes) == c['costs'][idx-31505] == 108
    print('ORIGINAL_NATIVE_WITNESS_PASS', idx, len(original), len(prefixes))
rows = [line.split() for line in (D/'EXACT_NATIVE_31505_31999.txt').read_text().splitlines()]
assert hashlib.sha256((D/'EXACT_NATIVE_31505_31999.txt').read_bytes()).hexdigest() == c['native_output_sha256']
assert len(rows) == 495 and [int(x[0]) for x in rows] == list(range(31505, 32000))
assert [int(x[1]) for x in rows] == c['costs']
assert [int(x[2]) for x in rows] == c['optimal_root_assignment_counts']
gaps = [line.split() for line in (D/'EXACT_GAP_31505_31531.txt').read_text().splitlines()]
assert len(gaps) == 27 and [int(x[0]) for x in gaps] == list(range(31505, 31532))
assert [int(x[1]) for x in gaps] == c['costs'][:27]
assert [int(x[3]) for x in gaps] == c['second_assignment_cost_31505_31531']
assert all(int(x[2]) == 1 for x in gaps)
print('CERTIFICATE_CONTINUITY_AND_WITNESS_PASS', 495)
print('Reproduce DP lower bounds using the preserved frozen input and C++17 solver.')
