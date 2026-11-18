#!/usr/bin/env python3
"""Verify exact EC49FMQ costs and optional frozen native source/raw rows."""
from pathlib import Path
import base64, collections, hashlib, json, zlib
D=Path(__file__).resolve().parent
a=json.loads((D/'EXACT_VECTOR_EC49FMQ.json').read_text(encoding='utf-8'))
v=zlib.decompress(base64.b64decode(a['cost_uint8_zlib_base64']))
assert len(v)==a['count']==500
assert hashlib.sha256(v).hexdigest()==a['cost_uint8_sha256']
assert (min(v),max(v))==(a['min_cost'],a['max_cost'])==(102,138)
assert [6500+i for i,c in enumerate(v) if c==102]==a['argmins']==[6589]
assert {str(k):n for k,n in collections.Counter(v).items()}==a['histogram']
r=D/'EXACT_NATIVE_OUTPUT_6500_6999.txt'
if r.exists():
    b=r.read_bytes()
    assert hashlib.sha256(b).hexdigest()==a['raw_output_sha256']
    rows=[s.split() for s in b.decode('utf-8').splitlines()]
    assert len(rows)==500 and [int(s[0]) for s in rows]==list(range(6500,7000))
    assert bytes(int(s[1]) for s in rows)==v
    assert {str(k):n for k,n in collections.Counter(int(s[3]) for s in rows).items()}==a['first_root_counts']
    print('RAW_ROWS_PASS',len(rows))
for name,key in [('master_and_radius3_cases.txt','frozen_catalogue_sha256'),('scan_cached_radius3.cpp','solver_source_sha256')]:
    p=D/name
    if p.exists():
        assert hashlib.sha256(p.read_bytes()).hexdigest()==a[key]
        print('SOURCE_PASS',name)
print('VECTOR_PASS',len(v),min(v),max(v))
