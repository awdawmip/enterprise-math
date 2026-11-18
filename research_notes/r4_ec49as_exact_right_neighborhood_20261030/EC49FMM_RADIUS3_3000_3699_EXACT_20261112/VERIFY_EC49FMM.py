#!/usr/bin/env python3
"""Check the lossless EC49FMM 700-cost vector; optionally check raw DP rows."""
import base64,collections,hashlib,json,pathlib,sys,zlib
p=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'EXACT_VECTOR_EC49FMM.json')
v=json.loads(p.read_text()); x=list(zlib.decompress(base64.b64decode(v['values_u8_zlib_base64'],validate=True)))
assert v['scientific_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert v['case_catalog_sha256']=='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
assert len(x)==v['count']==700 and (v['case_start'],v['case_end_inclusive'])==(3000,3699)
assert hashlib.sha256(bytes(x)).hexdigest()==v['value_bytes_sha256']
assert (min(x),max(x))==(v['min_cost'],v['max_cost'])==(128,138)
assert [i+3000 for i,c in enumerate(x) if c==128]==v['min_indices']==[3408,3422]
assert {str(c):n for c,n in collections.Counter(x).items()}==v['histogram']
for index,cost in v['independent_python_checks'].items(): assert x[int(index)-3000]==cost
if len(sys.argv)>2:
    raw=pathlib.Path(sys.argv[2]).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==v['raw_rows_sha256']
    rows=raw.decode().splitlines()
    assert [(int(r.split()[0]),int(r.split()[1])) for r in rows]==[(i+3000,c) for i,c in enumerate(x)]
    assert {str(k):n for k,n in collections.Counter(int(r.split()[3]) for r in rows).items()}==v['first_root_histogram']
    print('RAW_ROWS_PASS',len(rows))
print('EC49FMM_VECTOR_PASS',len(x),min(x),max(x),v['min_indices'])
