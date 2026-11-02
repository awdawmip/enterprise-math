"""Direct original six-axis signed_brc.endpoint_multiplicity capacity certificate.

Run in a frozen checkout or beside an unchanged pinned_signed_brc.py evidence copy.
"""
from itertools import product
from math import comb
from pathlib import Path
import hashlib, importlib.util

here=Path(__file__).resolve()
paths=[r/'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py' for r in here.parents]+[here.with_name('pinned_signed_brc.py')]
source=next((p for p in paths if p.is_file()),None)
if source is None:raise FileNotFoundError('unchanged original signed_brc.py required')
raw=source.read_bytes()
sha=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
assert sha=='300a96e3dc24bf6fff73743037a0347a8bc83176',sha
spec=importlib.util.spec_from_file_location('pinned_native_x6_signed_brc',source)
brc=importlib.util.module_from_spec(spec);spec.loader.exec_module(brc)
checked=0
for q,d in product((2,3,4),(1,2,3)):
 for n in range(q*d+1,q*d+6):
  if n>14:continue
  for r in (0,1):
   for j in range(d+1):
    k=r+q*j
    want=comb(d,j)
    original=brc.endpoint_multiplicity(n,(n-2*k,0,0,0,0,0))
    assert original>=comb(n,k)>=want,(q,d,n,k)
    checked+=1
assert checked==246,checked
print('PASS original pinned signed_brc.endpoint_multiplicity:',checked,'capacity checks; Git blob',sha)
