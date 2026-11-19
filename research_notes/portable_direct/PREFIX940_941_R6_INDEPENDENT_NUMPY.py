"""Independent exact XOR-bit arithmetic and certificate-priority audit for k=11 or k=12.
Run: python PREFIX940_941_R6_INDEPENDENT_NUMPY.py 11|12 DATA_DIR
DATA_DIR must contain the frozen PREFIX928_R6_SORTED_PAIR_IDS.bin, W2, W3,
D4_sorted_cpp, W5, D6, W7, D8, W9, D10, and (for k=12) W11.
"""
import hashlib
import sys
from pathlib import Path
import numpy as np

K=int(sys.argv[1]); P=Path(sys.argv[2]); assert K in (11,12)
LOW=262145; SZ=131072; N=1<<32; A=np.arange(LOW,524288,2,dtype=np.int64)
X=K*A; tmax=22 if K==11 else 24
batches=[]; counts_t=[0]*(tmax+1)
for j in range(19):
    # Instead of XOR, derive new endpoint from the actual state of bit j.
    endpoint=X+np.where(((X>>j)&1)==0,1<<j,-(1<<j))
    for i in range(19):
        if K==12 and i>=2 and j>=2:continue
        difference=endpoint-(1<<i)
        for t in range(1,tmax+1):
            b,rem=np.divmod(difference,t)
            ok=(rem==0)&(b>=LOW)&(b<=524287)&((b&1)==1)
            if ok.any():
                idx=np.flatnonzero(ok)
                batches.append(idx.astype(np.uint64)*SZ+((b[ok]-LOW)//2).astype(np.uint64))
                counts_t[t]+=len(idx)
ids=np.unique(np.concatenate(batches))
expect=(13144330,16974425) if K==11 else (3522575,3719345)
assert (len(ids),sum(counts_t))==expect
raw_path=P/('W11_numpy_unified.bin' if K==11 else 'D12_numpy_unified.bin')
ids.astype('<u8').tofile(raw_path)

Q=np.arange(LOW,524288,2,dtype=np.int64); r=np.ones(SZ,dtype=np.int64)
S=np.zeros(SZ,dtype=bool); D=np.zeros(SZ,dtype=bool)
for step in range(1,53):
    r=(2*r)%Q; hit=(r==1)|(r==Q-1)
    if step<=31:S|=hit
    else:D|=hit
D&=~S
assert S.sum()==24 and D.sum()==91
L=D.copy()
for b in [262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287]:L[(b-LOW)//2]=True
assert L.sum()==104
T=np.zeros(SZ,dtype=bool)
for n in range(1024):T[(77081*n+12345)%SZ]=True
names=['PREFIX928_R6_SORTED_PAIR_IDS.bin','W2.bin','W3.bin','D4_sorted_cpp.bin','W5.bin','D6.bin','W7.bin','D8.bin','W9.bin','D10.bin']
if K==12:names+=['W11.bin']
prior=[np.memmap(P/name,dtype='<u8',mode='r') for name in names]
labels=['BZS','U','V','W2','W3','D4','W5','D6','W7','D8','W9','D10']
if K==12:labels+=['W11']
labels+=['NEW']; counts=dict.fromkeys(labels,0)
new_path=P/('NEW11_numpy_unified.bin' if K==11 else 'NEW12_numpy_unified.bin')
with open(new_path,'wb') as out:
    for lo in range(0,len(ids),400000):
        chunk=ids[lo:lo+400000]; ai=(chunk//SZ).astype(np.int64);bi=(chunk%SZ).astype(np.int64)
        a=LOW+2*ai;b=LOW+2*bi
        unmatched=~((b<33*((N+a-1)//a))|(a<33*((N+b-1)//b))|S[bi]|(np.lcm(a,b)<N))
        counts['BZS']+=len(chunk)-int(unmatched.sum())
        def member(sorted_ids):
            ix=np.searchsorted(sorted_ids,chunk)
            clipped=np.minimum(ix,len(sorted_ids)-1)
            return (ix<len(sorted_ids))&(sorted_ids[clipped]==chunk)
        def take(label,match):
            nonlocal_unmatched=unmatched&match
            counts[label]+=int(nonlocal_unmatched.sum())
            unmatched[nonlocal_unmatched]=False
        take('U',member(prior[0]));take('V',L[ai]|L[bi]|((a>=500001)&T[bi])|((b>=500001)&T[ai]))
        for label,older in zip(labels[3:-1],prior[1:]):take(label,member(older))
        counts['NEW']+=int(unmatched.sum());chunk[unmatched].astype('<u8').tofile(out)
assert sum(counts.values())==len(ids)
assert counts['NEW']==(5888914 if K==11 else 878172)
print('k',K,'raw',sum(counts_t),'unique',len(ids),'counts',counts)
print('sorted_sha',hashlib.sha256(raw_path.read_bytes()).hexdigest())
print('new_sha',hashlib.sha256(new_path.read_bytes()).hexdigest())
