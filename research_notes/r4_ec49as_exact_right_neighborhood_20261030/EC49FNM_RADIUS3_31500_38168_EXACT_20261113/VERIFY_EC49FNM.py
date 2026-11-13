#!/usr/bin/env python3
"""Verify EC49FNM 6669-case lossless cost vector and any local original raw evidence."""
from pathlib import Path
import json, hashlib, zlib, base64
D = Path(__file__).resolve().parent
c = json.loads((D/'EXACT_CERTIFICATE_EC49FNM.json').read_text())
assert c['schema']=='EC49FNM_BRC_RADIUS3_FINAL_6669_EXACT_V1'
assert c['frozen_science']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
lo, hi = c['interval']
assert (lo,hi)==(31500,38169)
values = json.loads(zlib.decompress(base64.b85decode(c['cost_vector_b85'])))
assert len(values)==hi-lo and all(type(v) is int and v>0 for v in values)
assert (min(values),max(values))==(c['min'],c['max'])==(106,234)
assert [lo+j for j,v in enumerate(values) if v==106]==c['argmin']==[31503]
assert [lo+j for j,v in enumerate(values) if v==234]==c['argmax']==[34796]
assert {k:values[int(k)-lo] for k in c['independent_python_verifications']}==c['independent_python_verifications']
for filename, field in [('master_and_radius3_cases.txt','frozen_master_sha256'),('cases.json','frozen_cases_sha256')]:
    f = D/filename
    if f.is_file(): assert hashlib.sha256(f.read_bytes()).hexdigest()==c[field]
raw = D/'scan_next/EXACT_NATIVE_OUTPUT_31500_38168.txt'
if raw.is_file():
    assert hashlib.sha256(raw.read_bytes()).hexdigest()==c['raw_output_sha256']
    rows = [s.split() for s in raw.read_text().splitlines()]
    assert [(int(x[0]),int(x[1])) for x in rows]==list(zip(range(lo,hi),values))
    print('RAW_6669_PASS')
print('COST_VECTOR_6669_PASS',len(values),'min',106,'unique argmin',31503,'max',234,'unique argmax',34796)
