#!/usr/bin/env python3
"""Check exact stored prefix costs; optional --solve recomputes all 600 with C++17.
In a full repository checkout, pass a generated master file to --solve:
  python BUILD_EC49FMI.py /tmp/ec49fmi
  python VERIFY_EC49FMI.py --solve /tmp/ec49fmi/master_and_radius3_cases.txt
"""
import base64
import collections
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import zlib

HERE=Path(__file__).resolve().parent
obj=json.loads((HERE/'EXACT_VECTOR_EC49FMI.json').read_text())
assert obj['science_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
z=base64.b64decode(obj['costs_zlib_base64'],validate=True)
assert hashlib.sha256(z).hexdigest()==obj['zlib_sha256']
v=zlib.decompress(z)
assert len(v)==600
assert hashlib.sha256(v).hexdigest()==obj['raw_600_costs_sha256']
assert min(v)==obj['minimum']==102 and max(v)==obj['max']==194
assert [i for i,n in enumerate(v) if n==102]==[32,93]
assert {str(k):n for k,n in sorted(collections.Counter(v).items())}==obj['cost_histogram']
for s,n in obj['independent_python_checks'].items():assert v[int(s)]==n
for s,n in obj['original_cpp_checks'].items():assert v[int(s)]==n
print('EC49FMI_STORED_VECTOR_EXACT_PASS',len(v),min(v),max(v),flush=True)
if len(sys.argv)>1:
    assert sys.argv[1]=='--solve' and len(sys.argv)==3
    master=Path(sys.argv[2]);assert hashlib.sha256(master.read_bytes()).hexdigest()==obj['master_input_sha256']
    source=HERE.parent/'EC49FMG_RADIUS2_ALL_6315_EXACT_20261112'/'SCAN_CACHED_EC49FMG.cpp'
    src=source.read_text()
    assert 'ncases!=6315' in src
    src=src.replace('ncases!=6315','ncases!=38169')
    with tempfile.TemporaryDirectory() as td:
        cpp=Path(td)/'r3.cpp';exe=Path(td)/'r3'
        cpp.write_text(src)
        subprocess.run(['g++','-O3','-std=c++17',str(cpp),'-o',str(exe)],check=True)
        with master.open('rb') as f:
            r=subprocess.run([str(exe),'0','600'],stdin=f,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True,text=False)
        lines=r.stdout.decode().splitlines()
        assert len(lines)==600
        for i,line in enumerate(lines):
            p=line.split();assert int(p[0])==i and int(p[1])==v[i]
        print('EC49FMI_FULL_600_NATIVE_PREFIX_RECOMPUTE_PASS',flush=True)
