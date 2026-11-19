"""PREFIX-935: independent vectorized k=6 boundary census and prior-union mask.
Scientific pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Inputs: PREFIX928_R6_SORTED_PAIR_IDS.bin, W2.bin, W3.bin, D4_sorted_cpp.bin,
W5.bin, D6.bin, NEW6.bin.
"""
import numpy as np, hashlib, json
from pathlib import Path
P=Path(__file__).resolve().parent
Q0,QMAX,NQ,N=262145,524287,131072,2**32
A=np.arange(Q0,QMAX+1,2,dtype=np.int64)
chunks=[];raw_t={t:0 for t in range(1,13)}
for j in range(19):
    y=np.bitwise_xor(6*A,1<<j)
    I=np.array([1<<i for i in range(19)],dtype=np.int64) if j==0 else np.array([1],dtype=np.int64)
    d=y[:,None]-I[None,:]
    assert d.min()>0 and d.max()<13*Q0
    for t in range(1,13):
        b=d//t; mask=(d%t==0)&(b>=Q0)&(b<=QMAX)&((b&1)==1)
        rows,cols=np.nonzero(mask);raw_t[t]+=len(rows)
        if len(rows):chunks.append(rows.astype(np.uint64)*NQ+(b[mask].astype(np.uint64)-Q0)//2)
D6=np.unique(np.concatenate(chunks));del chunks
sha=lambda x:hashlib.sha256(x.astype('<u8',copy=False).tobytes()).hexdigest()
assert len(D6)==1771013 and sha(D6)=='718e94ea98ba2931760b473a04eaf38ef189b4444548d9160ab5d861d1fc9c60'
assert np.array_equal(D6,np.fromfile(P/'D6.bin',dtype='<u8'))
rem=np.ones(NQ,dtype=np.int64);S=np.zeros(NQ,dtype=bool);late=np.zeros(NQ,dtype=bool)
for d in range(1,53):
    rem=2*rem%A; h=(rem==1)|(rem==A-1)
    if d<=31:S|=h
    else:late|=h
assert S.sum()==24
L=np.unique(np.concatenate([A[late & ~S],np.array([262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287])]))
assert len(L)==104
Lflag=np.isin(A,L)
T=np.zeros(NQ,dtype=bool);T[(77081*np.arange(1024)+12345)%NQ]=True
ai=(D6//NQ).astype(np.int64);bi=(D6%NQ).astype(np.int64);a=A[ai];b=A[bi]
BZS=(b<33*((N+a-1)//a))|(a<33*((N+b-1)//b))|S[bi]|(((a//np.gcd(a,b))*b)<N)
V=Lflag[ai]|Lflag[bi]|((a>=500001)&T[bi])|((b>=500001)&T[ai])
def contains(filename):
    x=np.fromfile(P/filename,dtype='<u8');assert np.all(x[1:]>x[:-1]);idx=np.searchsorted(x,D6)
    return (idx<len(x)) & (x[np.minimum(idx,len(x)-1)]==D6)
flags=[('BZS',BZS),('U',contains('PREFIX928_R6_SORTED_PAIR_IDS.bin')),('V',V),('W2',contains('W2.bin')),('W3',contains('W3.bin')),('D4',contains('D4_sorted_cpp.bin')),('W5',contains('W5.bin'))]
remaining=np.ones(len(D6),dtype=bool);counts={}
for name,mask in flags:
    counts[name]=int((remaining & mask).sum());remaining &= ~mask
counts['NEW']=int(remaining.sum())
new=D6[remaining]
assert counts==dict(BZS=952813,U=280,V=3115,W2=21638,W3=145,D4=0,W5=54,NEW=792968)
assert sha(new)=='d35aea32ca618b232d81fcbade86c42112f6d7541571d6ab66f0a020a8ecd6aa'
assert np.array_equal(new,np.fromfile(P/'NEW6.bin',dtype='<u8'))
result={'schema':'PREFIX935_K6_BOUNDARY_EXACT_V1','frozen_scientific_input':'f42f2906d77f24085c123f3ccfe9667d41caa96d','W6_boundary':{'raw':int(sum(raw_t.values())),'unique':len(D6),'raw_t':raw_t,'sha256':sha(D6)},'priority_disjoint':counts,'new_only_sha256':sha(new),'prior_union':7537850206,'new_union':7537850206+counts['NEW'],'remaining':NQ*NQ-7537850206-counts['NEW'],'verification':'TWO_ALGORITHMS_BYTE_IDENTICAL','independent_review':'NOT_REVIEWED'}
(P/'PREFIX935_R6_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
