#!/usr/bin/env python3
"""Exact author-side signed BRC certificates for s=217..224 using R462 frozen E/O/R construction."""
import sys,json,time
from pathlib import Path
# Use unchanged exact kernel committed in the previous R468 directory.
PREV=Path(__file__).resolve().parent.parent/'r468_signed_brc_right_edge_209_216_20261102_emr3'
if PREV.is_dir():sys.path.insert(0,str(PREV))
from R468_EXACT_KERNEL import core
HERE=Path(__file__).resolve().parent
lo=int(sys.argv[1]) if len(sys.argv)>1 else 217
hi=int(sys.argv[2]) if len(sys.argv)>2 else 224
assert 217<=lo<=hi<=224
for s in range(lo,hi+1):
 t=time.monotonic(); data=core.s_certificate(s,detail=True)
 assert data['degree_p2']==4*s and data['degree_p3']==6*s
 assert data['strict_positive_coefficients']==10*s+2
 p=HERE/f'R469_S{s}_EVIDENCE.json';p.write_text(json.dumps({'result':'R469_EXACT_PASS',**data},sort_keys=True,indent=2)+'\n')
 print('R469_EXACT_PASS',s,data['sha256'],'seconds',round(time.monotonic()-t,1),flush=True)
