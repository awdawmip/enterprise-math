#!/usr/bin/env python3
"""Exact EC49FML 2000..2999 vector and optional raw solver-row verifier."""
import base64,collections,hashlib,json,pathlib,sys,zlib
v=json.loads(pathlib.Path(sys.argv[1]).read_text())
assert v['scientific_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert v['case_catalog_sha256']=='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
assert (v['case_start'],v['case_end_inclusive'],v['count'])==(2000,2999,1000)
x=list(zlib.decompress(base64.b64decode(v['values_u8_zlib_base64'],validate=True)))
assert len(x)==1000
assert hashlib.sha256(bytes(x)).hexdigest()==v['value_bytes_sha256']=='15e593dde7bb47ff74a96a3d29692830f58f8bb960d37fefd008e24197a9b9bf'
assert min(x)==v['min_cost']==110 and max(x)==v['max_cost']==138
assert [2000+i for i,c in enumerate(x) if c==110]==v['min_indices']==[2439]
assert {str(k):n for k,n in collections.Counter(x).items()}==v['histogram']
for k,c in v['independent_python_checks'].items():assert x[int(k)-2000]==c
if len(sys.argv)>2:
 raw=pathlib.Path(sys.argv[2]).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==v['raw_rows_sha256']=='c3e4983e81ba66b979ccd6defe7833234fa468d2f68ad6f580725a652a7967e5'
 rows=raw.decode().splitlines();assert len(rows)==1000
 assert [(int(r.split()[0]),int(r.split()[1])) for r in rows]==[(i+2000,c) for i,c in enumerate(x)]
 assert {str(k):n for k,n in collections.Counter(int(r.split()[3]) for r in rows).items()}==v['first_root_histogram']
 print('EC49FML_RAW_ROWS_PASS',len(rows))
print('EC49FML_VECTOR_PASS',len(x),min(x),max(x),v['min_indices'])
