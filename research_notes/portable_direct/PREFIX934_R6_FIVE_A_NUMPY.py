"""PREFIX-934: independent vectorized k=5 enumeration against frozen prior certificate IDs.
Run after PREFIX-932 regenerates W2.bin/W3.bin and PREFIX-933 supplies D4_sorted_cpp.bin.
Input: PREFIX928_R6_SORTED_PAIR_IDS.bin, W2.bin, W3.bin, D4_sorted_cpp.bin, W5.bin, NEW5.bin.
Frozen input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from pathlib import Path
import hashlib, json
import numpy as np
P=Path(__file__).resolve().parent
Q0=262145; QMAX=524287; NQ=131072; N=2**32
A=np.arange(Q0,QMAX+1,2,dtype=np.int64)
I=1<<np.arange(19,dtype=np.int64)
raw_t={t:0 for t in range(1,11)}; chunks=[]
for j in range(19):
    d=np.bitwise_xor(5*A,1<<j)[:,None]-I[None,:]
    assert d.min()>0 and d.max()<11*Q0
    for t in range(1,11):
        b=d//t
        valid=(d%t==0)&(b>=Q0)&(b<=QMAX)&((b&1)==1)
        rows,_=np.nonzero(valid)
        raw_t[t]+=len(rows)
        if len(rows):
            chunks.append(rows.astype(np.uint64)*NQ+(b[valid].astype(np.uint64)-Q0)//2)
w=np.unique(np.concatenate(chunks)); del chunks
sha=lambda x:hashlib.sha256(x.astype('<u8',copy=False).tobytes()).hexdigest()
assert len(w)==15406809 and sha(w)=='ed2ff4c1961e29a619ccb404e834150028b4a689d5816ae03b2fa41fbc49de95'
assert np.array_equal(w,np.fromfile(P/'W5.bin',dtype='<u8'))
aix=(w//NQ).astype(np.int64); bix=(w%NQ).astype(np.int64)
a=A[aix]; b=A[bix]
r=np.ones(NQ,dtype=np.int64); S=np.zeros(NQ,dtype=bool); late=np.zeros(NQ,dtype=bool)
for d in range(1,53):
    r=(r*2)%A; hit=(r==1)|(r==A-1)
    if d<=31:S|=hit
    else:late|=hit
assert S.sum()==24
L=np.unique(np.concatenate([A[late & ~S],np.array([262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287])]))
assert len(L)==104
lf=np.isin(A,L)
T=np.zeros(NQ,dtype=bool); T[(77081*np.arange(1024)+12345)%NQ]=True
oldBZS=(b<33*((N+a-1)//a))|(a<33*((N+b-1)//b))|S[bix]|(((a//np.gcd(a,b))*b)<N)
oldV=lf[aix]|lf[bix]|((a>=500001)&T[bix])|((b>=500001)&T[aix])
def found(path):
    hay=np.fromfile(P/path,dtype='<u8')
    assert np.all(hay[1:]>hay[:-1])
    loc=np.searchsorted(hay,w)
    return (loc<len(hay)) & (hay[np.minimum(loc,len(hay)-1)]==w)
flags=[('BZS',oldBZS),('U',found('PREFIX928_R6_SORTED_PAIR_IDS.bin')),('V',oldV),('W2',found('W2.bin')),('W3',found('W3.bin')),('D4',found('D4_sorted_cpp.bin'))]
remaining=np.ones(len(w),dtype=bool); counts={}
for name,flag in flags:
    counts[name]=int((remaining&flag).sum())
    remaining &= ~flag
counts['NEW']=int(remaining.sum())
new=w[remaining]
assert len(new)==6200406 and sha(new)=='d3857354c1016485dcf365d7769e84c2f1e6c9a27f7a3d9aa6d57a7258f81377'
assert np.array_equal(new,np.fromfile(P/'NEW5.bin',dtype='<u8'))
assert counts==dict(BZS=7548662,U=3229,V=33831,W2=1405996,W3=214543,D4=142,NEW=6200406)
print(json.dumps({'raw':int(sum(raw_t.values())),'raw_t':raw_t,'unique':len(w),'counts':counts,'new_union':7531649800+counts['NEW'],'complement':NQ*NQ-7531649800-counts['NEW'],'W5_sha256':sha(w),'new_sha256':sha(new)},indent=2))
