#!/usr/bin/env python3
"""Independent vectorized exact enumeration of the PREFIX-938 k=9 source-bit certificate.
Scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
It verifies the complete W9 sorted set, not the priority overlap calculations.
"""
import hashlib
import sys
from pathlib import Path
import numpy as np
Q0,QMAX,NQ,K=262145,524287,131072,9
base=Path(sys.argv[1]) if len(sys.argv)>1 else Path(".")
A=np.arange(Q0,QMAX+1,2,dtype=np.int64)
assert len(A)==NQ
indices=np.arange(NQ,dtype=np.uint64)
Ibits=(1<<np.arange(19,dtype=np.int64))[:,None]
ids_by_chunk=[]
raw_t=np.zeros(19,dtype=np.int64)
for j in range(19):
    Y=np.bitwise_xor(K*A,np.int64(1<<j))[None,:]
    D=Y-Ibits
    assert np.all(D>0)
    for t in range(1,19):
        ok=(D%t==0)
        B=D//t
        ok &= (B>=Q0)&(B<=QMAX)&((B%2)==1)
        iidx,aidx=np.nonzero(ok)
        raw_t[t]+=len(iidx)
        if len(iidx):
            ids=indices[aidx]*np.uint64(NQ)+((B[iidx,aidx]-Q0)//2).astype(np.uint64)
            ids_by_chunk.append(ids)
ids=np.unique(np.concatenate(ids_by_chunk))
assert int(raw_t.sum())==19710115
assert len(ids)==15456919
path=base/"W9_numpy.bin"
ids.astype("<u8").tofile(path)
sha=hashlib.sha256(path.read_bytes()).hexdigest()
assert sha=="541318dc9a9f6c8d6941f38cf69cb5e873caa1dfb602d70ac5dad9f2fef11888"
print("raw",int(raw_t.sum()),"unique",len(ids))
print("raw_t",raw_t.tolist())
print("W9_sha256",sha)
