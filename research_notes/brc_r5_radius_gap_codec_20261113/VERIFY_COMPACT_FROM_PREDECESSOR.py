#!/usr/bin/env python3
"""Frozen R5 sidecar: exact radius-local gap codec and finite theorem tests.
Requires the genuine predecessor's SIDECAR_BASE64.txt on the stacked branch.
Does not reconstruct the frozen 28-coordinate scientific corpus.
"""
from pathlib import Path
from itertools import product, combinations, pairwise
from collections import Counter
import base64, hashlib, json

HERE=Path(__file__).resolve().parent
PREV=HERE.parent/'brc_r5_bounded_dp_sidecar_20261113'/'SIDECAR_BASE64.txt'
old=base64.b64decode(PREV.read_text().strip(),validate=True)
assert len(old)==1382
assert hashlib.sha256(old).hexdigest()=='94341ccf1aa09eb0eb42c045201b36dc9589008209fe77f446d8a4b93cee68b6'
K=int.from_bytes(old[:2],'little')
centers=[int.from_bytes(old[2+2*i:4+2*i],'little') for i in range(K)]
assert K==213 and len(old[2+2*K:])==954
assert centers[0]==1 and centers[-1]==952
assert Counter(v-u for u,v in pairwise(centers))=={3:16,4:77,5:119}

def pack(centers,R,lo,hi):
    b0=max(1,R.bit_length());bg=max(1,(hi-lo).bit_length())
    if not centers or not 0<=centers[0]<=R:raise ValueError('first')
    gaps=[b-a for a,b in pairwise(centers)]
    if any(not lo<=d<=hi for d in gaps):raise ValueError('gap')
    values=[centers[0]]+[d-lo for d in gaps]
    widths=[b0]+[bg]*len(gaps)
    acc=shift=0
    for x,w in zip(values,widths):
        acc|=x<<shift;shift+=w
    return len(centers).to_bytes(2,'little')+acc.to_bytes((shift+7)//8,'little')

def unpack(raw,R,lo,hi,W):
    if len(raw)<2:raise ValueError('short')
    k=int.from_bytes(raw[:2],'little')
    if k<1:raise ValueError('count')
    b0=max(1,R.bit_length());bg=max(1,(hi-lo).bit_length())
    bits=b0+(k-1)*bg
    if len(raw)!=2+(bits+7)//8:raise ValueError('length')
    acc=int.from_bytes(raw[2:],'little')
    if acc>>bits:raise ValueError('padding')
    first=acc&((1<<b0)-1)
    if first>R:raise ValueError('first')
    acc>>=b0;out=[first]
    for _ in range(k-1):
        digit=acc&((1<<bg)-1);acc>>=bg
        if digit>hi-lo:raise ValueError('digit')
        out.append(out[-1]+lo+digit)
    if out[-1]>W or W-out[-1]>R:raise ValueError('last')
    return out

def directory(E,C):
    j=0;ans=[]
    for x in E:
        while j+1<len(C) and 2*x>E[C[j]]+E[C[j+1]]:j+=1
        ans.append(j)
    return ans

general=pack(centers,2,1,5)
small=pack(centers,2,3,5)
assert len(general)==82 and len(small)==56
assert unpack(general,2,1,5,953)==centers
assert unpack(small,2,3,5,953)==centers
assert b''.join(i.to_bytes(2,'little') for i in unpack(small,2,3,5,953))==old[2:428]
assert small.hex()==(HERE/'R5_CENTERS_56B.hex').read_text().strip()
assert hashlib.sha256(small).hexdigest()=='bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326'

cases=covered=entries=0
for n in range(2,8):
    for inc in product((1,2,3),repeat=n-1):
        E=[0]
        for a in inc:E.append(E[-1]+a)
        for mask in range(1,1<<n):
            C=[i for i in range(n) if mask>>i&1]
            d=directory(E,C)
            assert d==[min(range(len(C)),key=lambda j:(abs(E[b]-E[C[j]]),j)) for b in range(n)]
            cases+=1;entries+=n
            if max(min(abs(E[b]-E[c]) for c in C) for b in range(n))<=2:
                assert C[0]<=2 and n-1-C[-1]<=2
                assert all(1<=b-a<=5 for a,b in pairwise(C))
                assert unpack(pack(C,2,1,5),2,1,5,n-1)==C
                covered+=1
bad=0
for raw in (small[:-1],small+b'\0',small[:2]+b'\xff'*54):
    try:unpack(raw,2,3,5,953)
    except ValueError:bad+=1
assert bad==3
print(json.dumps({'status':'PASS','predecessor_sha256':hashlib.sha256(old).hexdigest(),
'general_bytes':len(general),'frozen_bytes':len(small),'frozen_sha256':hashlib.sha256(small).hexdigest(),
'cases':cases,'covered':covered,'directory_entries':entries,'malformed_rejected':bad},indent=2))
