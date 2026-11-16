#!/usr/bin/env python3
"""R478: exact full coefficient certificates for signed BRC auxiliary scalar.
Fixed frozen formulas R462_VERIFY_FROZEN_KERNEL.py; R468_EXACT_KERNEL.py performs exact Kronecker/GMP arithmetic.
"""
import json,sys,time
from pathlib import Path
from R468_EXACT_KERNEL import core
s=int(sys.argv[1]); assert 257<=s<=264
start=time.monotonic()
result=core.s_certificate(s,detail=True)
assert result['degree_p2']==4*s
assert result['degree_p3']==6*s
assert result['strict_positive_coefficients']==10*s+2
out={'schema':'R478_S_CERT_V1','status':'AUTHOR_SIDE_EXACT_CERTIFICATE','scientific_pin':'18783e01e3646c72b7aab3b16d3f565e83e6446f','arithmetic':'exact integers; R462 frozen E/O/R + R468 exact Kronecker/GMP','result':'R478_EXACT_PASS','s_certificate':result}
Path(f'R478_S{s}_EVIDENCE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('R478_S_CERT_PASS',s,result['sha256'],'wall',round(time.monotonic()-start,2),flush=True)
