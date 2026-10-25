#!/usr/bin/env python3
"""C296 portable source replay: certify all 125x2 endpoints at both precisions.

Run from research_handoffs/ in C295-derived GitHub branch. Pure stdlib.
Reports an author-level exact finite result; never asserts Source admission.
"""
from fractions import Fraction as F
from pathlib import Path
import base64,hashlib,zlib
import C275_STANDALONE_EXACT_REPLAY as s
import C288_ISOLATING_BOXES_EXACT as c288
from C296_DYADIC_INTERVAL_SIGNS import PositiveDyadicEvaluator

PARENT_SHA='f254bd0a36235f453ae87dabd6ed84da8a4af551c7115354ec4aacbdc1bb0f2e'
SUFFIX_SHA='8bea5f1a78c224b56a9297d09766b09af9dcb3196b17a6f360bc6862355263be'
COMBINED_SHA='9a6ce046642ff404e8929333dab5c11dcd5e8616e218d09a1370453850649f6e'

def decode_certificates():
    a=Path('C295_125_K128_CERTIFICATE.b64').read_text().splitlines()
    b=Path('C296_125_K256_SUFFIX128_CERTIFICATE.b64').read_text().splitlines()
    assert a[:3]==['EM_C295_125_DYADIC_128_INTEGER_CERTIFICATE_V1',
       'encoding=base64(zlib(125 consecutive unsigned big-endian 16-byte integers))',
       'source_sha256='+PARENT_SHA]
    assert b[:7]==['EM_C296_125_DYADIC_256_SUFFIX128_CERTIFICATE_V1',
       'encoding=base64(zlib(125 consecutive unsigned big-endian 16-byte suffixes))',
       'parent_C295_raw_sha256='+PARENT_SHA,
       'raw_suffix_sha256='+SUFFIX_SHA,
       'combined_K256_sha256='+COMBINED_SHA,
       'root_path_count=125', 'target_exponent=256']
    raw128=zlib.decompress(base64.b64decode(a[-1],validate=True))
    raw_suffix=zlib.decompress(base64.b64decode(b[-1],validate=True))
    assert len(raw128)==len(raw_suffix)==125*16
    assert hashlib.sha256(raw128).hexdigest()==PARENT_SHA
    assert hashlib.sha256(raw_suffix).hexdigest()==SUFFIX_SHA
    ks128=[int.from_bytes(raw128[i*16:(i+1)*16],'big') for i in range(125)]
    ss=[int.from_bytes(raw_suffix[i*16:(i+1)*16],'big') for i in range(125)]
    ks256=[(k<<128)+t for k,t in zip(ks128,ss)]
    raw256=b''.join(k.to_bytes(32,'big') for k in ks256)
    assert hashlib.sha256(raw256).hexdigest()==COMBINED_SHA
    assert all((x>>128)==y for x,y in zip(ks256,ks128))
    return ks128,ks256

def verify():
    ks128,ks256=decode_certificates()
    paths,_=c288.build_paths()
    assert len(paths)==125
    W,_=s.floor_fixed_masses()
    verifier=PositiveDyadicEvaluator(W)
    for bit,prec,ks,margin_exponent in [(128,320,ks128,142),(256,448,ks256,268)]:
        one=1<<prec
        min_gap=None
        count=0
        for i,(k,p) in enumerate(zip(ks,paths)):
            for o in (0,1):
                t=F(k+o,1<<bit)
                v=tuple(w+t*d for w,d in zip(p['w'],p['d']))
                assert s.valid(v) and all(lo<=x<=hi for x,(lo,hi) in zip(v,p['box']))
                low,high=verifier.enclose(v,prec)
                assert (high<one if o==0 else low>one),(bit,i,o,low,high)
                gap=one-high if o==0 else low-one
                assert gap>0
                min_gap=gap if min_gap is None or gap<min_gap else min_gap
                count+=1
        assert count==250
        assert min_gap*(1<<margin_exponent)>one
        print(f'C296_OUTWARD_CERTIFIED_{bit}: 250/250, P={prec}, margin>2^-{margin_exponent}',flush=True)
    print('C296_REMOTE_PORTABLE_125x2_128_AND_256_PASS',flush=True)

if __name__=='__main__':verify()
