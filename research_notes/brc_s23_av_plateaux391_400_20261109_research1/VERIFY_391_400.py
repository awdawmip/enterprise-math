#!/usr/bin/env python3
"""Exact S23/AV critical-cell endpoint checks 391..400, using unchanged upstream checker."""
import argparse, hashlib, importlib.util
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'brc_s23_av_plateau20_20261108_r1'/'VERIFY_PLATEAUX20_200.py'
raw=p.read_bytes()
blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
assert blob=='261d7e22da0e62d667009cb50acfe77ac4e35c3f',blob
spec=importlib.util.spec_from_file_location('s23_pinned_checker',p)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
parser=argparse.ArgumentParser()
parser.add_argument('--start',type=int,default=391)
parser.add_argument('--end',type=int,default=400)
args=parser.parse_args()
assert 391<=args.start<=args.end<=400
cells=0
for i in range(args.start,args.end+1):
    row=m.check(i)
    assert row is not None,('coverage_failed',i)
    ix,H,M,n,bmax,critical,usage,_=row
    a=m.get_witnesses(i)[-1][1]
    assert ix==i and a*m.EU<i*m.DL and i*m.DU<(a+1)*m.EL
    cells+=critical
    print('CERTIFIED_PLATEAU',ix,'H',H,'M',M,'narrow',n,
          'beta_bound',bmax,'critical_cells',critical,
          'witnesses_used',usage,flush=True)
print('PASS_SEGMENT',args.start,args.end,'count',args.end-args.start+1,'cells',cells,flush=True)
