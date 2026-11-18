#!/usr/bin/env python3
"""EC49FMJ exact 400-case vector check; optional native C++ full recompute.
Run: python VERIFY_EC49FMJ.py
Optional: python VERIFY_EC49FMJ.py --solve /path/to/master_and_radius3_cases.txt
The master and 38169 indexed cases come from neighboring EC49FMI BUILD_EC49FMI.py.
"""
import base64,collections,hashlib,json,subprocess,sys,tempfile,zlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
r=json.loads((HERE/'EXACT_VECTOR_EC49FMJ.json').read_text())
z=base64.b64decode(r['zlib_base64'],validate=True)
assert hashlib.sha256(z).hexdigest()==r['zlib_sha256']
v=zlib.decompress(z)
assert len(v)==400 and hashlib.sha256(v).hexdigest()==r['raw_400_costs_sha256']
assert min(v)==r['minimum']==110 and max(v)==r['maximum']==168
assert [600+i for i,x in enumerate(v) if x==110]==[865,871]
assert {str(k):q for k,q in sorted(collections.Counter(v).items())}==r['cost_histogram']
for source in ('independent_python_checks','original_cpp_checks'):
    for s,n in r[source].items():assert v[int(s)-600]==n
pre=HERE.parent/'EC49FMI_RADIUS3_FIRST600_20261112'/'EXACT_VECTOR_EC49FMI.json'
p=json.loads(pre.read_text())
first=zlib.decompress(base64.b64decode(p['costs_zlib_base64']))
assert len(first)==600 and min(first)==102
assert len(first+v)==1000 and min(first+v)==102
print('EC49FMJ_400_EXACT_VECTOR_PASS; CONTIGUOUS_1000_MIN_102_PASS')
if len(sys.argv)>1:
    assert len(sys.argv)==3 and sys.argv[1]=='--solve'
    master=Path(sys.argv[2])
    assert hashlib.sha256(master.read_bytes()).hexdigest()==r['master_input_sha256']
    src=(HERE.parent/'EC49FMG_RADIUS2_ALL_6315_EXACT_20261112'/'SCAN_CACHED_EC49FMG.cpp').read_text()
    assert 'ncases!=6315' in src
    src=src.replace('ncases!=6315','ncases!=38169')
    with tempfile.TemporaryDirectory() as d:
        cpp=Path(d)/'r3.cpp';bin=Path(d)/'r3';cpp.write_text(src)
        subprocess.run(['g++','-O3','-std=c++17',str(cpp),'-o',str(bin)],check=True)
        with master.open('rb') as f:
            q=subprocess.run([str(bin),'600','1000'],stdin=f,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
        lines=q.stdout.decode().splitlines();assert len(lines)==400
        for i,line in enumerate(lines):
            cols=line.split()
            assert int(cols[0])==i+600 and int(cols[1])==v[i]
    print('EC49FMJ_FULL_400_SIGNED_NATIVE_RECOMPUTE_PASS')
