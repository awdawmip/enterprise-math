#!/usr/bin/env python3
"""Independent vectorized k=3 audit against the exact U, W2 sources.
Input: PREFIX928_R6_SORTED_PAIR_IDS.bin, W2_sorted.bin, optional exported W3_sorted.bin.
Algorithm uses bit toggling + full-array arithmetic, independent of the C++ scalar enumerator.
"""
import sys, json, hashlib
import numpy as np
Q0, QMAX, NQ = 262145, 524287, 131072
N=1<<32
assert len(sys.argv)==4
U=np.fromfile(sys.argv[1],dtype='<u8');W2=np.fromfile(sys.argv[2],dtype='<u8'); cpp3=np.fromfile(sys.argv[3],dtype='<u8')
assert U.size==5295478 and W2.size==30211412
assert np.all(U[1:]>U[:-1]) and np.all(W2[1:]>W2[:-1])
# Generate via arrays across all a for each bit-j; quotient-divisibility arrays over all i and t.
a=np.arange(Q0,QMAX+1,2,dtype=np.int64)
idx=np.arange(NQ,dtype=np.int64)
powers=(1<<np.arange(19,dtype=np.int64))[None,:]
parts=[];raw_t=[0]*7
for j in range(19):
    y=np.bitwise_xor(3*a, np.int64(1<<j))
    diff=y[:,None]-powers
    assert np.all(diff>0) and np.all(diff < 7*Q0)
    for t in range(1,7):
        b=diff//t
        mask=(diff%t==0)&(b>=Q0)&(b<=QMAX)&((b&1)==1)
        ii,jj=np.nonzero(mask)
        bb=b[ii,jj]
        if len(ii):
            # direct endpoint congruence, start congruence and valid witness labels
            assert np.all(((3*a[ii])%a[ii])==0)
            assert np.all((y[ii]%bb)==((1<<jj)%bb))
            parts.append((idx[ii]*NQ+(bb-Q0)//2).astype(np.uint64))
        raw_t[t]+=len(ii)
ids=np.unique(np.concatenate(parts))
assert ids.size==cpp3.size and np.array_equal(ids,cpp3)
digest=hashlib.sha256(ids.astype('<u8').tobytes()).hexdigest()
assert digest=='3f501ca25d0b8c55b284b621d26251f8be2c8c771ce294206f24b1daa10051a9'
# Independent group priority, vector arithmetic in bounded chunks; uses no old C++ mask routines.
S=set();D=set();L=set();T=set()
for b in range(Q0,QMAX+1,2):
    r=1;early=False;late=False
    for d in range(1,53):
        r=(2*r)%b
        if r in (1,b-1):
            if d<=31: early=True
            else: late=True
    if early:S.add(b)
    elif late:D.add(b)
assert len(S)==24 and len(D)==91
L=D|{262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287}
assert len(L)==104
T={Q0+2*((77081*t+12345)%NQ) for t in range(1024)}
assert len(T)==1024
sarr=np.zeros(NQ,dtype=bool);larr=np.zeros(NQ,dtype=bool);tarr=np.zeros(NQ,dtype=bool)
for k in S:sarr[(k-Q0)//2]=True
for k in L:larr[(k-Q0)//2]=True
for k in T:tarr[(k-Q0)//2]=True
from collections import Counter
c=Counter();example=None
# Chunked independent numpy intersection: neither C++ merge-pointer nor scalar gcd loops.
for start in range(0,ids.size,500000):
    xx=ids[start:start+500000];aa_idx=(xx//NQ).astype(np.int64);bb_idx=(xx%NQ).astype(np.int64)
    aa=Q0+2*aa_idx;bb=Q0+2*bb_idx
    g=np.gcd(aa,bb)
    bzs=(bb<33*((N+aa-1)//aa))|(aa<33*((N+bb-1)//bb))|sarr[bb_idx]|(((aa//g)*bb)<N)
    # vectorized sorted-ID membership via searchsorted with clip
    uidx=np.searchsorted(U,xx); inU=(uidx<len(U))&(U[np.minimum(uidx,len(U)-1)]==xx)
    v=larr[aa_idx]|larr[bb_idx]|((aa>=500001)&tarr[bb_idx])|((bb>=500001)&tarr[aa_idx])
    widx=np.searchsorted(W2,xx); inW2=(widx<len(W2))&(W2[np.minimum(widx,len(W2)-1)]==xx)
    assert not np.any(inU & bzs)
    cat=np.where(bzs,0,np.where(inU,1,np.where(v,2,np.where(inW2,3,4))))
    for category,n in enumerate(np.bincount(cat,minlength=5)):c[category]+=int(n)
    if example is None and np.any(cat==4):
        ix=int(np.flatnonzero(cat==4)[0]);example=(int(aa[ix]),int(bb[ix]))
assert c=={0:8752594,1:6617,2:42286,3:2342742,4:8268849}, c
out={'schema':'PREFIX932_INDEPENDENT_VECTOR_AUDIT_V1','count_raw_by_t':raw_t[1:],'count_raw_total':sum(raw_t),'count_unique':int(ids.size),'sorted_sha256':digest,'priority_partition':{'BZS':c[0],'U':c[1],'V':c[2],'W2':c[3],'new':c[4]},'new_union':7522555296+c[4],'new_complement':NQ*NQ-(7522555296+c[4]),'first_new_pair':example,'method':'NumPy vectorized bit/remainder generation, independent boolean masks and sorted-ID searchsorted'}
print(json.dumps(out,indent=2));open('/mnt/data/r6working/PREFIX932_NUMPY_RESULT.json','w').write(json.dumps(out,indent=2)+'\n')
