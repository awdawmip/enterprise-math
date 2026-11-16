#!/usr/bin/env python3
"""Exact original-source native X6 BRC double-fiber witnesses, not a full R063 rerun."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

PIN='300a96e3dc24bf6fff73743037a0347a8bc83176'
FROZEN='59538f585d037d09ef687b28715c4bc1a3f9fe03'

def original(path: Path):
    raw=path.read_bytes()
    oid=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if oid!=PIN: raise ValueError(f'Wrong frozen original signed_brc.py: {oid}')
    spec=importlib.util.spec_from_file_location('x6_unit71_frozen',str(path))
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def check(path):
    m=original(path)
    pairs=[
      ('balanced_all_length',(-2,-1,0),(0,1,2)),
      ('unsigned_named_equal',(-1,-1,-1),(1,1,1)),
      ('unbalanced',(-3,-3,0),(1,1,4))]
    records=[]
    for name,a,b in pairs:
        x=a+(0,0,0);y=b+(0,0,0)
        T=m.shortest_event_count(x)
        if T!=m.shortest_event_count(y) or m.spatial_norm_squared(x)!=m.spatial_norm_squared(y):
            raise ArithmeticError('observer condition mismatch')
        u=[m.endpoint_multiplicity(T+2*k,x) for k in range(4)]
        v=[m.endpoint_multiplicity(T+2*k,y) for k in range(4)]
        if (u==v)!=(name!='unbalanced'): raise ArithmeticError('uniform profile disagreement')
        if u[0]!=m.shortest_path_multiplicity(x) or v[0]!=m.shortest_path_multiplicity(y):
            raise ArithmeticError('native shortest mismatch')
        wp=(2,1,1,1,1,1); wm=(2,1,1,1,1,1)
        unsigned=(int(m.endpoint_weight(T,x,wp,wm)),int(m.endpoint_weight(T,y,wp,wm)))
        p2=(2,1,1,1,1,1);ones=(1,1,1,1,1,1)
        signed=(int(m.endpoint_weight(T,x,p2,ones)),int(m.endpoint_weight(T,y,p2,ones)))
        if name=='balanced_all_length' and unsigned!=(12,3): raise ArithmeticError('named unsigned witness')
        if name=='unsigned_named_equal' and signed[0]==signed[1]: raise ArithmeticError('direction witness')
        records.append({'case':name,'x':x,'y':y,'T':T,'native_counts_x':u,'native_counts_y':v,
                        'unsigned_named_w2_axis1':unsigned,'signed_named_p2_axis1':signed})
    return {'schema':'EM_X6_UNIT71_PINNED_ORIGINAL_BRC_WITNESS_V1',
            'source_commit':FROZEN,'original_source_blob_sha1':PIN,
            'scope':'three witness double-fibers only, k=0..3; native frozen original endpoint_multiplicity and endpoint_weight',
            'cases':records,'result':'PASS','scientific_status':'AUTHOR_EXECUTED_SCOPED_UNREVIEWED_NOT_ADMITTED'}

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--module',type=Path,default=Path('experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py'))
    args=p.parse_args()
    print(json.dumps(check(args.module),sort_keys=True,indent=2))
