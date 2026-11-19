#!/usr/bin/env python3
"""Independent (j,i,t)->vector-a enumeration of exact k=11 named-XOR certificates.
Scientific pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Prerequisites: sorted uint64 little-endian immutable prior sets as named below.
This is an auxiliary two-port observer, not native X6, reviewed mathematics or a Task CLAIM.
"""
import numpy as np
from pathlib import Path
from hashlib import sha256
Q0, NQ, K = 262145, 131072, 11
A = (Q0 + 2*np.arange(NQ,dtype=np.int64))
base = np.arange(NQ,dtype=np.uint64)*NQ
pairs=[]
raw_t=[0]*23
for j in range(19):
    end = (K*A) ^ (1<<j)
    for i in range(19):
        d = end - (1<<i)
        for t in range(1,23):
            good=(d%t==0)
            if not np.any(good):continue
            candidates=(d//t)
            good &= (candidates>=Q0) & (candidates<=524287) & ((candidates&1)==1)
            idx=np.flatnonzero(good)
            if idx.size:
                raw_t[t]+=len(idx)
                # Consistency check: start, terminal congruences and word cap.
                if not np.all((end[idx] % candidates[idx])==((1<<i) % candidates[idx])):raise AssertionError('observer mismatch')
                pairs.append(base[idx]+(candidates[idx]-Q0)//2)
W=np.unique(np.concatenate(pairs))
Path('W11_numpy.bin').write_bytes(W.astype('<u8',copy=False).tobytes())
print('raw',sum(raw_t),'unique',W.size,flush=True)
print('raw_t',raw_t[1:],flush=True)

def has(items,v):
    # independent numpy binary search in a sorted immutable old-certificate set
    at = np.searchsorted(items,v)
    mask=at<len(items)
    return mask & (items[np.minimum(at,len(items)-1)]==v)

files=[('U','PREFIX928_R6_SORTED_PAIR_IDS.bin'),('W2','W2.bin'),('W3','W3.bin'),('D4','D4_sorted_cpp.bin'),('W5','W5.bin'),('D6','D6.bin'),('W7','W7.bin'),('D8','D8.bin'),('W9','W9.bin'),('D10','D10.bin')]
sets={name:np.memmap(filename,mode='r',dtype='<u8') for name,filename in files}
a=Q0+2*(W//NQ).astype(np.int64)
b=Q0+2*(W%NQ).astype(np.int64)
# independent original B/Z/S classification and L/T row sets.
S=[];D=[]
for q in range(Q0,524288,2):
    r=1; early=False; late=False
    for u in range(1,53):
        r=(r*2)%q
        if r in (1,q-1):
            if u<=31:early=True
            else:late=True
    if early:S.append(q)
    elif late:D.append(q)
assert len(S)==24 and len(D)==91
L=sorted(set(D+[262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287]))
assert len(L)==104
T=np.zeros(NQ,dtype=bool)
for u in range(1024): T[(77081*u+12345)%NQ]=True
from math import gcd
# Use vectorized gcd, no floating point.
BZS=(b < 33*((2**32+a-1)//a)) | (a < 33*((2**32+b-1)//b)) | np.isin(b,S) | ((a//np.gcd(a,b))*b < 2**32)
V=np.isin(a,L) | np.isin(b,L) | ((a>=500001)&T[(b-Q0)//2]) | ((b>=500001)&T[(a-Q0)//2])
remain=~BZS
counts={'BZS':int(BZS.sum())}
for name in ['U','V','W2','W3','D4','W5','D6','W7','D8','W9','D10']:
    hit=V if name=='V' else has(sets[name],W)
    exact=remain&hit
    counts[name]=int(exact.sum());remain&=~hit
NEW=W[remain]
counts['NEW']=int(NEW.size)
assert sum(counts.values())==W.size
Path('NEW11_numpy.bin').write_bytes(NEW.astype('<u8',copy=False).tobytes())
for name in ['W11_numpy.bin','NEW11_numpy.bin']:
    p=Path(name)
    print('SHA256',name,sha256(p.read_bytes()).hexdigest(),flush=True)
print('counts',counts,flush=True)
print('union',7552811074+counts['NEW'],flush=True)
print('remaining',131072**2-7552811074-counts['NEW'],flush=True)
