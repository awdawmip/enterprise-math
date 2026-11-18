#!/usr/bin/env python3
"""Verify every exact C++ result row against the lossless stored vector and source digest."""
import base64,hashlib,json,sys,zlib,collections
from pathlib import Path
P=Path(__file__).resolve().parent
report=json.loads((P/'EXACT_REPORT_EC49FMC.json').read_text())
raw=Path(sys.argv[1]).read_bytes()
rows=raw.decode().splitlines()
assert len(rows)==1137
cost=[int(row.split()[1]) for row in rows]
assert all(int(row.split()[0])==i for i,row in enumerate(rows))
assert bytes(cost)==zlib.decompress(base64.b64decode(report['costs_zlib_base64']))
assert hashlib.sha256(raw).hexdigest()==report['raw_solver_output_sha256']
assert dict(sorted(collections.Counter(cost).items()))=={int(k):v for k,v in report['cost_histogram'].items()}
print('EC49FMC_ALL_1137_EXACT_PREFIX_OPTIMA_MATCH')
