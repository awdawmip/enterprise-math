#!/usr/bin/env python3
"""Stdlib-only replay of C297 125*2 strict 512-bit endpoint signs.
Needs frozen C275,C288,C293,C296 positive-rational auxiliary dependencies.
"""
import base64,hashlib,json,zlib
from fractions import Fraction as R
from pathlib import Path
import C275_STANDALONE_EXACT_REPLAY as src
import C288_ISOLATING_BOXES_EXACT as c288
from C296_DYADIC_INTERVAL_SIGNS import PositiveDyadicEvaluator

CANON=lambda x:json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()

def replay():
    cert256=json.loads(Path('C296_125_EXACT_DYADIC_256_BRACKETS.json').read_text())
    meta=json.loads(Path('C297_COMPACT_CERT_METADATA.json').read_text())
    assert hashlib.sha256(CANON(cert256['records'])).hexdigest()==meta['parent_C296_records_sha256']
    comp=base64.b64decode(Path('C297_K512_SUFFIX256_CERTIFICATE.b64').read_text(),validate=False)
    assert hashlib.sha256(comp).hexdigest()==meta['compressed_sha256']
    data=zlib.decompress(comp)
    assert len(data)==125*32 and hashlib.sha256(data).hexdigest()==meta['payload_sha256']
    paths,_=c288.build_paths();assert len(paths)==125
    W,_=src.floor_fixed_masses()
    evaluator=PositiveDyadicEvaluator(W)
    rows=[];min_slack=None;max_width=0
    for i,(p,old) in enumerate(zip(paths,cert256['records'])):
        assert old['index']==i
        parent=int(old['dyadic_left_integer'])
        suffix=int.from_bytes(data[32*i:32*(i+1)],'big')
        k=(parent<<256)+suffix
        assert parent<<256<=k<(parent+1)<<256
        rows.append({'index':i,'dyadic_left_integer':str(k),'denominator_exponent':512,
                     'parent_C296_K256':str(parent),'candidate_correction_units':0})
        for off in (0,1):
            t=R(k+off,1<<512)
            v=tuple(a+t*b for a,b in zip(p['w'],p['d']))
            assert src.valid(v) and all(lo<=z<=hi for z,(lo,hi) in zip(v,p['box']))
            lo,hi=evaluator.enclose(v,704)
            unit=1<<704
            if off==0:
                assert hi<unit,(i,off)
                slack=R(unit-hi,unit)
            else:
                assert lo>unit,(i,off)
                slack=R(lo-unit,unit)
            min_slack=slack if min_slack is None else min(min_slack,slack)
            max_width=max(max_width,hi-lo)
    assert hashlib.sha256(CANON(rows)).hexdigest()==meta['C297_records_sha256']
    assert min_slack>R(1,1<<528)
    print('C297_REMOTE_125x2_512BIT_STRICT_INTERVAL_PASS',
          'paths=125 signs=250 precision=704 margin_gt_2^-528',
          'max_width_units='+str(max_width))
    return min_slack
if __name__=='__main__':replay()
