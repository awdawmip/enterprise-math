#!/usr/bin/env python3
"""Exact S23/AV index-412 capacity check, reusing pinned all-endpoint checker.
Execute from this note directory with VERIFY_PLATEAUX20_200.py beside it,
or pass the original checker path as the first positional argument.
"""
import hashlib
import importlib.util
from pathlib import Path
import sys
src=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('VERIFY_PLATEAUX20_200.py')
raw=src.read_bytes()
blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
assert blob=='261d7e22da0e62d667009cb50acfe77ac4e35c3f',blob
spec=importlib.util.spec_from_file_location('s23_pinned',src)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
res=mod.check(412)
assert res is not None
ix,H,M,n,bound,cells,used,_=res
assert ix==412 and H==156701089 and M==855291132
assert n==126 and bound==413 and cells==82252 and used==52
w=mod.get_witnesses(412)
start=w[-2][2]+511
end=w[-1][2]+510
assert start==156320716 and end==H and end-start+1==380374
print('PINNED_CHECKER_GIT_BLOB',blob)
print('CERTIFIED_PLATEAU',ix,'H',H,'N',M,'narrow',n,'beta_bound',bound,'critical_cells',cells,'witnesses_used',used)
print('EXACT_INTEGER_HORIZON_INTERVAL',start,end,'length',end-start+1)
print('PASS_S23_AV_PLATEAU_412')
