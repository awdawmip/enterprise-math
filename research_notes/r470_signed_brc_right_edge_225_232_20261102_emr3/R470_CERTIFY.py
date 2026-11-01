#!/usr/bin/env python3
"""R470: exact signed BRC P2/P3 polynomial certificates for s=225..232.
Pin: R462 E/O/R mathematical kernel git blob 7c641c985b8c48ef3fb2ddcb2142e38ca0a4ccff;
R468 multiplication kernel git blob 9057a6c46814a06cea45bffc20fe6f44f370b0bb.
Run in R470 directory with installed prior R468 sibling, or place these exact kernels alongside this script.
"""
import json,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
REPO_PREV=HERE.parent/'r468_signed_brc_right_edge_209_216_20261102_emr3'
if REPO_PREV.is_dir(): sys.path.insert(0,str(REPO_PREV))
from R468_EXACT_KERNEL import core
s=int(sys.argv[1]); assert 225<=s<=232
start=time.monotonic()
e=core.s_certificate(s,detail=True)
assert e['degree_p2']==4*s and e['degree_p3']==6*s
assert e['strict_positive_coefficients']==10*s+2
p=HERE/f'R470_S{s}_EVIDENCE.json'
p.write_text(json.dumps({'status':'R470_EXACT_PASS',**e},ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print('R470_EXACT_PASS',s,e['sha256'],'elapsed',round(time.monotonic()-start,2),flush=True)
