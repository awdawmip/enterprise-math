#!/usr/bin/env python3
"""Crosscheck EC49DK closed-return BRC aggregates with the unchanged native signed_brc.py kernel."""
import hashlib,json
from pathlib import Path
from source.native_signed_brc import endpoint_weight, return_multiplicity
from VERIFY_EC49DK import native_aggregate,X,Y
R=Path(__file__).resolve().parent
k=R/'source'/'native_signed_brc.py';b=k.read_bytes()
blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
assert blob=='300a96e3dc24bf6fff73743037a0347a8bc83176'
rows=[]
for n in (0,2,4,6,8):
    cnt=return_multiplicity(n)
    wx=endpoint_weight(n,(0,)*6,X,(1,)*6)
    wy=endpoint_weight(n,(0,)*6,Y,(1,)*6)
    c0,x0=native_aggregate(n,X);c1,y0=native_aggregate(n,Y)
    assert (cnt,wx,wy)==(c0,x0,y0)==(c1,x0,y0)
    rows.append({'n':n,'count':cnt,'x':int(wx),'y':int(wy)})
report={'status':'PASS','kernel_blob_sha1':blob,'kernel_sha256':hashlib.sha256(b).hexdigest(),
        'kernel':'unchanged six signed axis native BRC endpoint_weight','checks':rows}
(R/'EC49DK_NATIVE_CROSSCHECK.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,sort_keys=True))
