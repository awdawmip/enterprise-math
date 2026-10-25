#!/usr/bin/env python3
"""C293 exact brackets. Needs the pinned matching C275/C284/C288 inputs in the
portable package. Deterministic no-float proof checks, Fraction semantics.
The full-4D gradient/Hessian conditions are separate author-level C290/C292
evidence, not consequences of these finite endpoint evaluations.
"""
from fractions import Fraction as R
import hashlib, json, time
import C288_ISOLATING_BOXES_EXACT as c288
import C275_STANDALONE_EXACT_REPLAY as s

D_FINE=2**24
PAD=R(1,2**26)
R_NEWTON=PAD/8
LAMBDA=R(2125,6)
UPPER_DIR_L1=R(1,40)

def at(p,t):
    return tuple(w+t*d for w,d in zip(p['w'],p['d']))

def load_certificate():
    with open('C293_125_REFINED_BRACKETS.json',encoding='utf-8') as h: cert=json.load(h)
    assert cert['schema']=='EM_C293_125_REFINED_DYADIC_BRACKETS_V1'
    assert cert['fine_denominator']==D_FINE
    assert cert['original_c284_record_sha256']==c288.SOURCE_CERT_SHA
    records=cert['records']
    assert len(records)==125
    digest=hashlib.sha256(json.dumps(records,ensure_ascii=False,separators=(',',':')).encode('utf-8')).hexdigest()
    assert digest==cert['records_sha256']
    return records,cert

def verify():
    records,cert=load_certificate()
    paths,_=c288.build_paths()
    W,_=s.floor_fixed_masses()
    assert len(paths)==len(records)==125
    assert LAMBDA*R_NEWTON<R(1,2**20)
    assert R_NEWTON==R(1,2**29)
    assert UPPER_DIR_L1*R(1,2**25)==PAD/20
    assert 3*UPPER_DIR_L1*R(1,2**25)==R(3,20)*PAD
    assert R(6,5)*R_NEWTON==R(3,20)*PAD
    min_gap=None
    since=time.monotonic()
    for i,(p,record) in enumerate(zip(paths,records)):
        idx,k2=record
        assert idx==i and type(k2) is int
        assert p['k']*4096<=k2<(p['k']+1)*4096
        lo=R(k2,D_FINE); hi=R(k2+1,D_FINE)
        assert 0<lo<hi<1 and hi-lo==R(1,D_FINE)
        assert sum(map(abs,p['d']))<UPPER_DIR_L1
        v0,v1=at(p,lo),at(p,hi)
        assert s.valid(v0) and s.valid(v1)
        for k in range(4):
            assert p['box'][k][0]<=v0[k]<=p['box'][k][1]
            assert p['box'][k][0]<=v1[k]<=p['box'][k][1]
        f0=s.original_F(v0,W);f1=s.original_F(v1,W)
        assert f0<s.Q<f1,(i,k2,'bracket signs')
        gap=(f1-f0)/s.Q
        min_gap=gap if min_gap is None else min(min_gap,gap)
        if (i+1)%25==0:print('CERTIFIED',i+1,'/125, elapsed',round(time.monotonic()-since,1),'s',flush=True)
    assert min_gap>R(1,2**50)
    print('C293_125_EXACT_DYADIC_NEWTON_PASS', '125 strict brackets', '250 original_F signs','r',R_NEWTON)
    return min_gap

if __name__=='__main__':verify()
