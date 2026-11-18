#!/usr/bin/env python3
"""Compute exact onset byte matrix for 18 noise-diameter strata from pinned 101x256 integer centers."""
from pathlib import Path
import json,hashlib,bisect,struct
HERE=Path(__file__).resolve().parent
DATA=HERE/'EXACT_R5_ALL_101_BUDGETS.json'
EXPECTED='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
raw=DATA.read_bytes()
assert hashlib.sha256(raw).hexdigest()==EXPECTED
obj=json.loads(raw)['counts_and_cohorts']
L=25845652773852463277015040000
U=58182461585441404127941754880
centers=[list(map(int,obj[str(k)]['counts'])) for k in range(214,315)]
thresholds=sorted({abs(c[i]-c[j]) for c in centers for i in range(256) for j in range(i+1,256) if L<abs(c[i]-c[j])<U})
assert len(thresholds)==17
stages=[L]+thresholds
# Since all 256 centers are integral, stage 17 and U-1 induce exactly the same compatibility relation.
assert stages[-1]<U-1
onset=bytearray(101*256*256)
orders=bytearray(101*256)
for k,c in enumerate(centers):
    order=sorted(range(256),key=lambda i:(c[i],i))
    for p,i in enumerate(order):orders[k*256+i]=p
    for i in range(256):
        base=(k*256+i)*256
        for j in range(256):
            p=bisect.bisect_left(stages,abs(c[i]-c[j]))
            onset[base+j]=p if p<len(stages) else 255
    if k%25==0:print('PREPARED',k,flush=True)
(HERE/'onset_18.bin').write_bytes(onset)
(HERE/'ranks_18.bin').write_bytes(orders)
(HERE/'stages_18.json').write_text(json.dumps({'frozen_sha256':EXPECTED,'L':L,'U':U,'stage_taus':[str(s) for s in stages]},indent=2)+'\n')
print('PREP_DONE stages=',len(stages),'input_sha256',EXPECTED,'binary_sha256',hashlib.sha256(onset).hexdigest(),'bytes',len(onset),flush=True)
