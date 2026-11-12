#!/usr/bin/env python3
"""Verify EC49FMW exact 700-vector & constructive BRC signed-X6 witness.
Add original frozen cases/generator/raw rows for full source-membership checks.
"""
from pathlib import Path
from collections import Counter, defaultdict
import hashlib, base64, json, zlib
D=Path(__file__).resolve().parent
v=json.loads((D/'EXACT_VECTOR_EC49FMW.json').read_text())
w=json.loads((D/'WITNESS_12875_EC49FMW.json').read_text())
c=zlib.decompress(base64.b64decode(v['cost_uint8_zlib_base64'],validate=True))
assert len(c)==v['case_count']==700
assert (v['index_start'],v['index_end_inclusive'])==(12800,13499)
assert hashlib.sha256(c).hexdigest()==v['cost_uint8_sha256']
assert (min(c),max(c))==(114,205)
assert [12800+i for i,k in enumerate(c) if k==114]==v['argmins']==[12875]
assert [12800+i for i,k in enumerate(c) if k==205]==v['argmaxs']
assert {str(k):n for k,n in Counter(c).items()}==v['histogram']
assert c[0]==171 and c[-1]==146
raw=D/'EXACT_NATIVE_OUTPUT_12800_13499.txt'
if raw.exists():
    assert hashlib.sha256(raw.read_bytes()).hexdigest()==v['complete_raw_rows_sha256']
    rr=[x.split() for x in raw.read_text().splitlines()]
    assert len(rr)==700 and [int(x[0]) for x in rr]==list(range(12800,13500))
    assert c==bytes(int(x[1]) for x in rr)
    assert {str(k):n for k,n in Counter(int(x[3]) for x in rr).items()}==v['first_root_counts']
for name,field in [
    ('master_and_radius3_cases.txt','frozen_catalogue_sha256'),
    ('cases.json','frozen_cases_sha256'),
    ('scan_cached_radius3.cpp','solver_source_sha256'),
    ('EC49FGW_RADIUS5_SCREEN.py','frozen_generator_sha256'),
    ('EC49FGJ_SEVEN_KEY_94_WITNESSES.json','catalogue_original_witness_sha256')]:
    file=D/name
    if file.exists(): assert hashlib.sha256(file.read_bytes()).hexdigest()==v[field]
assert w['scientific_input_pin']==v['scientific_input_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert w['case_index']==12875 and w['cost']==114 and len(w['words'])==24
assert sum(w['root_costs'].values())==114
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
assert set(''.join(z[2] for z in w['words']))<=set(STEPS)
P=set(); roots=defaultdict(set); seen=set()
for h,s,word in w['words']:
    assert len(word)==h and (h,s) not in seen
    seen.add((h,s)); p=b''
    for ch in word:
        for direction in STEPS[ch]:
            p+=bytes([direction+4]); P.add(p); roots[p[:1].hex()].add(p)
assert len(seen)==24 and len(P)==114
assert {k:len(x) for k,x in roots.items()}==w['root_costs']
try:
    from EC49FGW_RADIUS5_SCREEN import all_words, raw_key, PIN
    assert PIN==v['scientific_input_pin']
    catalogue=set(all_words()); assert len(catalogue)==178850
    keys=sorted({raw_key(word) for label,word in catalogue}); assert len(keys)==94
    cases=json.loads((D/'cases.json').read_text()); assert len(cases['cases'])==38169
    assert cases['cases'][12875]==w['seven_key_indices']
    allowed={keys[k] for k in w['seven_key_indices']}
    for h,s,word in w['words']:
        assert ((h,s),word) in catalogue and raw_key(word) in allowed
except ImportError:
    print('FROZEN_GENERATOR_NOT_PRESENT: structural witness verification only')
print('EC49FMW_VERIFY_PASS',len(c),min(c),v['argmins'],max(c),len(seen),len(P))
