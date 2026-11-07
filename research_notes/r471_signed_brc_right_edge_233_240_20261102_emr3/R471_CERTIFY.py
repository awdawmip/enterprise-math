#!/usr/bin/env python3
"""R471 exact signed BRC parameter-polynomial checks, frozen R462 E/O/R via R468 acceleration."""
from pathlib import Path
import sys,json,time
from R468_EXACT_KERNEL import core
start=int(sys.argv[1]) if len(sys.argv)>1 else 233
stop=int(sys.argv[2]) if len(sys.argv)>2 else 240
assert 233<=start<=stop<=240
for s in range(start,stop+1):
    t=time.perf_counter()
    evidence=core.s_certificate(s,detail=True)
    assert evidence['degree_p2']==4*s and evidence['degree_p3']==6*s
    assert evidence['strict_positive_coefficients']==10*s+2
    output={'result':'R471_EXACT_PASS','model':'signed BRC auxiliary scalar only','arithmetic':'Python exact integers; R462 frozen formulas; R468 integer Kronecker/GMP accelerator','evidence':evidence}
    Path(f'R471_S{s}_EVIDENCE.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print('R471_EXACT_PASS',s,evidence['sha256'],'wall',round(time.perf_counter()-t,2),flush=True)
