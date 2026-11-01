#!/usr/bin/env python3
"""R465 exact signed BRC PF3 right-edge certificates. Author-side, not admitted.
Frozen proof kernel: R462_VERIFY.py from R462 ZIP, reused in R464 via identical code structure.
R464 nonnegative-polynomial Kronecker multiplication; signed fallback exact schoolbook.
"""
import importlib.util
import json, sys, hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parent
SRC=BASE/'R462_VERIFY_FROZEN_KERNEL.py'
spec=importlib.util.spec_from_file_location('r462_frozen',str(SRC))
core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)
OLD_MUL=core.mul

def mul(a,b):
    if min(a)<0 or min(b)<0 or len(a)*len(b)<1600:
        return OLD_MUL(a,b)
    width=sum(a).bit_length()+sum(b).bit_length()+1
    mask=(1<<width)-1
    def encode(p):
        z=0
        for c in reversed(p):z=(z<<width)+c
        return z
    encoded=encode(a)*encode(b)
    output=[]
    for i in range(len(a)+len(b)-1):
        output.append(encoded&mask)
        encoded>>=width
    assert encoded==0
    return output

core.mul=mul

def run(lo,hi):
    reg=core.s_certificate(175,detail=False)
    assert reg['sha256']=='5a68b3d2ced114ee7744e5a75b8553717314a3d0ea1b5b497b0739ba09847239',reg
    print('R465_FROZEN_R463_REGRESSION_PASS',reg['sha256'],flush=True)
    rows=[]
    for s in range(lo,hi+1):
        data=core.s_certificate(s,detail=True)
        rows.append(data)
        print('R465_CERTIFICATE',json.dumps(data,sort_keys=True),flush=True)
    result={'schema':'EM_R465_SIGNED_BRC_EXACT_CERTIFICATES_V1','result':'R465_AUTHOR_EXACT_PASS',
            'input_pin_R462_kernel_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),
            'source_R464_immutable_commit':'d22650f431aa516feba34f32516fe0e89eb0f597',
            'source_R463_regression_s175_sha256':reg['sha256'],
            'range':[lo,hi], 'positive_coefficient_count':sum(x['strict_positive_coefficients'] for x in rows),
            'desnanot_jacobi_checks':len(rows),
            'signed_raw_checks':10*len(rows), 'catalan_checks':10*len(rows),
            'exact_arithmetic':'Python built-in integers only, no float signs',
            'scope':'fixed s and infinite k >= floor((s+2)/2), signed BRC auxiliary scalar only',
            'status':'AUTHOR_SIDE_EXACT_ONLY; DRIVER_UNREVIEWED; NOT_ADMITTED; REGISTER_PENDING', 'rows':rows}
    out=BASE/f'R465_CERTIFICATES_{lo}_{hi}.json'
    out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print('R465_AUTHOR_EXACT_PASS',json.dumps({k:v for k,v in result.items() if k not in ('rows',)},sort_keys=True),flush=True)
if __name__=='__main__':run(int(sys.argv[1]),int(sys.argv[2]))
