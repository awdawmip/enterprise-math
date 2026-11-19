#!/usr/bin/env python3
"""Independent full-vector exact W_2 enumeration and incremental set classification.
Uses array-oriented (a,i,j,t) enumeration, NumPy gcd and searchsorted.
Inputs: verified PREFIX928 U binary and independently regenerated PREFIX930 W1 binary.
"""
import hashlib
import json
from pathlib import Path
import numpy as np

Q0=262145;NQ=131072;N=1<<32
ROOT=Path(__file__).parent
A=np.arange(Q0,524288,2,dtype=np.int64)
ids=[]
raw_t=[0,0,0]
for j in range(19):
    Y=np.bitwise_xor(2*A, 1<<j)
    for i in range(19):
        D=Y-(1<<i)
        assert np.all(D>0)
        for t in range(1,4):
            take=(D%t==0)
            b=D//t
            take &= (b>=Q0)&(b<=524287)&((b&1)==1)
            inds=np.flatnonzero(take)
            if len(inds):
                assert np.all((Y[inds]%b[inds])==((1<<i)%b[inds]))
                ids.append((inds.astype(np.uint64)*NQ+((b[inds]-Q0)//2).astype(np.uint64)))
                raw_t[t-1]+=len(inds)
raw=np.concatenate(ids)
W2=np.unique(raw)
assert len(raw)==sum(raw_t)
p=(ROOT/'PREFIX931_R6_W2_NUMPY_IDS.bin')
p.write_bytes(W2.astype('<u8',copy=False).tobytes())
digest=hashlib.sha256(p.read_bytes()).hexdigest()
U=np.fromfile(ROOT/'PREFIX928_R6_SORTED_PAIR_IDS.bin',dtype='<u8')
W1=np.fromfile(ROOT/'PREFIX931_R6_W1_IDS.bin',dtype='<u8')
assert len(U)==5295478 and len(W1)==29360142
S=[];Dset=[]
for b in range(Q0,524288,2):
    r=1;early=False;late=False
    for d in range(1,53):
        r=(2*r)%b
        if r in (1,b-1):
            if d<=31:early=True
            else:late=True
    if early:S.append(b)
    elif late:Dset.append(b)
assert len(S)==24 and len(Dset)==91
L=set(Dset)|{262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287}
assert len(L)==104
T={Q0+2*((77081*t+12345)%NQ) for t in range(1024)}
assert len(T)==1024
Sflag=np.zeros(NQ,dtype=bool);Lflag=np.zeros(NQ,dtype=bool);Tflag=np.zeros(NQ,dtype=bool)
for b in S:Sflag[(b-Q0)//2]=True
for b in L:Lflag[(b-Q0)//2]=True
for b in T:Tflag[(b-Q0)//2]=True
counts=np.zeros(5,dtype=np.int64)
chunk=500000
for off in range(0,len(W2),chunk):
    arr=W2[off:off+chunk]
    ai=arr//NQ; bi=arr%NQ
    a=Q0+2*ai; b=Q0+2*bi
    ca=(N+a-1)//a;cb=(N+b-1)//b
    gcds=np.gcd(a,b)
    bzs=(b<33*ca)|(a<33*cb)|Sflag[bi]|(((a//gcds)*b)<N)
    posu=np.searchsorted(U,arr)
    isu=np.zeros(len(arr),dtype=bool);good=posu<len(U);isu[good]=U[posu[good]]==arr[good]
    assert not np.any(bzs&isu)
    v=Lflag[ai]|Lflag[bi]|((a>=500001)&Tflag[bi])|((b>=500001)&Tflag[ai])
    posw=np.searchsorted(W1,arr)
    isw=np.zeros(len(arr),dtype=bool);good=posw<len(W1);isw[good]=W1[posw[good]]==arr[good]
    cats=np.select([bzs,isu,v,isw],[0,1,2,3],default=4)
    counts+=np.bincount(cats,minlength=5)
res={
 'schema':'PREFIX931_INDEPENDENT_NUMPY_EXACT_CENSUS_V1',
 'raw_parameter_witnesses':int(len(raw)),
 'raw_parameter_t1_t2_t3':list(map(int,raw_t)),
 'unique_oriented_pairs':len(W2),
 'sorted_W2_sha256':digest,
 'partitions':dict(zip(['overlap_BZS','overlap_U_outside_BZS','overlap_V_outside_BZS_U','overlap_W1_outside_previous','new_outside_PREFIX930'],map(int,counts))),
 'new_certified_union':7522177912+int(counts[-1]),
 'complement':NQ*NQ-(7522177912+int(counts[-1])),
}
print(json.dumps(res,indent=2))
(ROOT/'PREFIX931_R6_NUMPY_OUTPUT.json').write_text(json.dumps(res,indent=2)+'\n')
