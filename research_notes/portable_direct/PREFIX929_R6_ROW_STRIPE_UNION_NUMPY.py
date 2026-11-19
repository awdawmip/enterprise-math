#!/usr/bin/env python3
"""PREFIX-929 exact independent NumPy implementation.

Requires NumPy and the PREFIX-928 verified sorted 42,363,824-byte uint64 ID
binary from its reproducibility bundle in this script's directory.
Checks one-to-one agreement against the independent C++17 program's totals.
"""
import hashlib
from pathlib import Path
import numpy as np
N=1<<32
Q0=262145
n=131072
Q=np.arange(Q0,524288,2,dtype=np.int64)
assert len(Q)==n
file=Path(__file__).with_name("PREFIX928_R6_SORTED_PAIR_IDS.bin")
assert hashlib.sha256(file.read_bytes()).hexdigest()=="15534b09fa696b5cbeba46f7f644d75c2c3f99b719a88071150fa91357f22bad"
U=np.memmap(file,mode="r",dtype="<u8")
assert len(U)==5295478 and np.all(U[1:]>U[:-1])
S,D=[],[]
for b in Q:
    b=int(b);r=1;early=late=False
    for d in range(1,53):
        r=(r*2)%b
        if r==1 or r==b-1:
            if d<=31:early=True
            else:late=True
    if early:S.append(b)
    elif late:D.append(b)
assert (len(S),len(D))==(24,91)
E=[262145,321651,440667,440669,524273,524275,524277,524279,524281,524283,524285,440665,524287]
L=sorted(set(D+E))
assert len(L)==104
T=sorted({Q0+2*((77081*t+12345)%n) for t in range(1024)})
assert len(T)==1024
Ahi=Q[Q>=500001]
assert len(Ahi)==12144

def in_U(a,b):
    ids=(((a-Q0)//2)*n+(b-Q0)//2).astype(np.uint64)
    pos=np.searchsorted(U,ids)
    return (pos<len(U)) & (U[np.minimum(pos,len(U)-1)]==ids)

def tally(a,b):
    cap=(b<33*((N+a-1)//a))|(a<33*((N+b-1)//b))
    zero=((a//np.gcd(a,b))*b<N)
    same=np.isin(b,S)
    old=cap|zero|same
    present=in_U(a,b)
    return len(a),int(old.sum()),int(present.sum()),int((~(old|present)).sum())

stat=[]
# Four pairwise disjoint domain pieces; each record = (domain,BZS,U,net_new).
for b in L:
    a=Q
    if len(stat)==0:stat=[(0,0,0,0) for _ in range(4)]
    v=tally(a,np.full(len(a),b,dtype=np.int64))
    stat[0]=tuple(x+y for x,y in zip(stat[0],v))
for a in L:
    bs=Q[~np.isin(Q,L)]
    v=tally(np.full(len(bs),a,dtype=np.int64),bs)
    stat[1]=tuple(x+y for x,y in zip(stat[1],v))
for b in T:
    if b in L:continue
    aa=Ahi[~np.isin(Ahi,L)]
    v=tally(aa,np.full(len(aa),b,dtype=np.int64))
    stat[2]=tuple(x+y for x,y in zip(stat[2],v))
for a in T:
    if a in L:continue
    bs=Ahi[~np.isin(Ahi,L)]
    if a>=500001:bs=bs[~np.isin(bs,T)]
    v=tally(np.full(len(bs),a,dtype=np.int64),bs)
    stat[3]=tuple(x+y for x,y in zip(stat[3],v))
expected=[(13631488,6203042,1678,7426768),
          (13620672,6071390,1709,7547573),
          (12404898,810190,0,11594708),
          (12396617,810051,0,11586566)]
assert stat==expected,(stat,expected)
new=sum(row[3] for row in stat)
assert new==38155615
print("S,D,L,T",len(S),len(D),len(L),len(T))
for name,row in zip(["rows","reverse_columns","highband","reverse_highband"],stat):
    print(name, *row)
print("new_certificate_pairs",new)
print("BZS_U_plus_new",7467804449+new)
print("remaining_certificate_complement",n*n-7467804449-new)
