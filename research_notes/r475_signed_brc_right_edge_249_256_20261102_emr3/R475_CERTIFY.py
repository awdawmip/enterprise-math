#!/usr/bin/env python3
"""R475 actual executed exact signed BRC polynomial certificates; frozen R462/R468 imports."""
from R468_EXACT_KERNEL import core
from pathlib import Path
import json,sys
lo=int(sys.argv[1]) if len(sys.argv)>1 else 249
hi=int(sys.argv[2]) if len(sys.argv)>2 else 256
assert 249<=lo<=hi<=256
for s in range(lo,hi+1):
    e=core.s_certificate(s,detail=True)
    assert e['degree_p2']==4*s and e['degree_p3']==6*s
    assert e['strict_positive_coefficients']==10*s+2
    Path(f'R475_S{s}_EVIDENCE.json').write_text(json.dumps(e,sort_keys=True,indent=2)+'\n',encoding='utf8')
    print('R475_EXACT_PASS',s,e['sha256'],e['elapsed_seconds'],flush=True)
