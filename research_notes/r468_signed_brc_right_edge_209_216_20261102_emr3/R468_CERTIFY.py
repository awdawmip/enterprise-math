#!/usr/bin/env python3
"""Exact author-side signed BRC certificates for s=209..216 using R462 frozen E/O/R construction."""
import sys,json,time
from pathlib import Path
from R468_EXACT_KERNEL import core
HERE=Path(__file__).resolve().parent
lo=int(sys.argv[1]) if len(sys.argv)>1 else 209
hi=int(sys.argv[2]) if len(sys.argv)>2 else 216
assert 209<=lo<=hi<=216
for s in range(lo,hi+1):
 t=time.monotonic(); data=core.s_certificate(s,detail=True)
 assert data['degree_p2']==4*s and data['degree_p3']==6*s
 assert data['strict_positive_coefficients']==10*s+2
 p=HERE/f'R468_S{s}_EVIDENCE.json';p.write_text(json.dumps({'result':'R468_EXACT_PASS',**data},sort_keys=True,indent=2)+'\n')
 print('R468_EXACT_PASS',s,data['sha256'],'seconds',round(time.monotonic()-t,1),flush=True)
