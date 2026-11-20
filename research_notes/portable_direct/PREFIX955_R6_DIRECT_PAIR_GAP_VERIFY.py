#!/usr/bin/env python3
"""Independent fixed-pair verification of PREFIX955 nonresonant joint-core gap classes."""
from collections import Counter
from pathlib import Path
from struct import iter_unpack
import hashlib,json
QMIN=262145
QSIZE=131072
F=Path(__file__).resolve().parent/'PREFIX955_W21_W23_INTERSECTION_IDS.bin'
raw=F.read_bytes()
assert len(raw)==137274*8
assert hashlib.sha256(raw).hexdigest()=='54c35a06874167484f0028443be45d3b03e69bc3bdf0e64fc97cf371522f6223'
gap_members=Counter(); masks=Counter(); raw_gap=Counter();nonresonant_pairs=0;diag_nonresonant=[]
for (pairid,) in iter_unpack('<Q',raw):
    a=QMIN+2*(pairid//QSIZE)
    b=QMIN+2*(pairid%QSIZE)
    dct=[]
    for k in (21,23):
        vals=Counter()
        ka=k*a
        for j in range(19):
            x=ka^(1<<j)
            for i in range(19):
                y=x-(1<<i)
                if y>0 and (y%b)==0:
                    vals[y//b]+=1
        dct.append(vals)
    mask=0
    for t,n1 in dct[0].items():
        for T,n2 in dct[1].items():
            m=T-t
            if 0<=m<=6 and (23*t-21*T)!=0:
                raw_gap[m]+=n1*n2
                mask|=1<<m
    if mask:
        nonresonant_pairs+=1
        masks[mask]+=1
        for m in range(7):
            if mask>>m &1:gap_members[m]+=1
    if mask and a==b:diag_nonresonant.append([a,b,mask])
assert nonresonant_pairs==6204
assert [raw_gap[m] for m in range(7)]==[6,644,6513,1314,231,3,0]
assert [gap_members[m] for m in range(7)]==[6,443,4725,840,190,3,0]
assert masks==Counter({1:6,2:441,4:4723,6:1,8:839,14:1,16:190,32:3})
assert diag_nonresonant==[[262145,262145,14]]
result={"source_sha256":hashlib.sha256(raw).hexdigest(),"raw_by_gap":[raw_gap[m] for m in range(7)],"distinct_pair_memberships_by_gap":[gap_members[m] for m in range(7)],"mask_histogram":dict(sorted(masks.items())),"nonresonant_distinct_pairs":nonresonant_pairs,"diagonal_nonresonant_pairs":diag_nonresonant,"offdiagonal_pairs":nonresonant_pairs-len(diag_nonresonant)}
(Path(__file__).resolve().parent/'PREFIX955_direct_verification.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(result,indent=2,ensure_ascii=False))
