#!/usr/bin/env python3
"""EC49FMP exact full-vector verifier. Python standard library only."""
import base64, collections, hashlib, json, zlib
from pathlib import Path
D=Path(__file__).resolve().parent
a=json.loads((D/'EXACT_VECTOR_EC49FMP.json').read_text(encoding='utf-8'))
v=zlib.decompress(base64.b64decode(a['cost_uint8_zlib_base64']))
assert len(v)==a['count']==1000
assert hashlib.sha256(v).hexdigest()==a['cost_uint8_sha256']
assert (min(v),max(v))==(a['min_cost'],a['max_cost'])==(116,168)
assert [5500+i for i,c in enumerate(v) if c==116]==a['argmins']
assert {str(k):n for k,n in collections.Counter(v).items()}==a['histogram']
assert sum(a['histogram'].values())==1000
print('VECTOR_PASS',len(v),min(v),max(v))
p=D/'EXACT_NATIVE_OUTPUT_5500_6499.txt'
if p.exists():
    raw=p.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==a['raw_output_sha256']
    lines=[s.split() for s in raw.decode('utf-8').splitlines()]
    assert len(lines)==1000 and [int(r[0]) for r in lines]==list(range(5500,6500))
    assert bytes(int(r[1]) for r in lines)==v
    assert {str(k):n for k,n in collections.Counter(int(r[3]) for r in lines).items()}==a['first_root_counts']
    print('RAW_ROWS_PASS',len(lines))
for name,key in [('master_and_radius3_cases.txt','frozen_catalogue_sha256'),('scan_cached_radius3.cpp','solver_source_sha256')]:
    p=D/name
    if p.exists():
        assert hashlib.sha256(p.read_bytes()).hexdigest()==a[key], name
        print('FROZEN_FILE_PASS',name)
print('COMPLETE_VALIDATOR_PASS')
