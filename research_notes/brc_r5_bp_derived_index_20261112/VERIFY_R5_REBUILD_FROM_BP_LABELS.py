#!/usr/bin/env python3
"""Rebuild full frozen R5 exact prefix index from 2,520-byte BP+labels+terminal stream.
Import of predecessor performs its own full exact validation first.
"""
from fractions import Fraction as F
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'brc_r5_bp_sparse_superrank_20261112'))
import VERIFY_R5_BP_SPARSE_SUPERRANK as prev

bp=list(prev.bp2);labels=list(prev.lab2);term=list(prev.term2)
N=len(term)
assert (N,len(bp),len(labels),sum(term))==(2880,5760,2879,1065)

def pack(bits):
    raw=bytearray((len(bits)+7)//8)
    for i,v in enumerate(bits):
        if v:raw[i//8]|=1<<(7-i%8)
    return bytes(raw)

bits=bp+[v for a in labels for v in ((a>>3)&1,(a>>2)&1,(a>>1)&1,a&1)]+term
assert len(bits)==20156
raw=pack(bits)
assert len(raw)==2520
decoded=[(raw[i//8]>>(7-i%8))&1 for i in range(len(bits))]
assert decoded==bits
off=2*N
bp2=decoded[:off]
labels2=[]
for _ in labels:
    labels2.append(sum(decoded[off+j]<<(3-j) for j in range(4)))
    off+=4
term2=decoded[off:off+N]
assert bp2==bp and labels2==labels and term2==term and off+N==len(decoded)

stack=[];paths=[];sizes=[0]*N;li=0
for v in bp2:
    if v:
        path=paths[stack[-1]]+(labels2[li],) if stack else ()
        if stack:li+=1
        paths.append(path)
        stack.append(len(paths)-1)
    else:
        i=stack.pop();sizes[i]=len(paths)-i
assert not stack and li==N-1 and paths==prev.paths
assert all(sizes[i]==prev.old_size(i) for i in range(N))

# Reconstruct q,n via immutable 15-atom port coefficients, not a stored pair table.
f=prev.old.old.f
W=tuple(a[f.k0] for a in f.atoms)
K=tuple(a[f.k1] for a in f.atoms)
pairs=[]
for path,t in zip(paths,term2):
    if not t:continue
    n=-sum(W[a-1] for a in path)
    k=-sum(K[a-1] for a in path)
    assert n>0 and k%36==0
    q=k//36
    assert q in (3,12,15)
    pairs.append((q,n))
assert len(pairs)==1065 and len(set(pairs))==1065 and pairs==prev.pairs

mask3=[int(q==3) for q,n in pairs]
mask12=[int(q==12) for q,n in pairs]
rows={q:prev.wave([n for qq,n in pairs if qq==q]) for q in (3,12,15)}
assert mask3==prev.mask3 and mask12==prev.mask12 and rows==prev.rows
vec=[term2,mask3,mask12]+[v for q in (3,12,15) for v in rows[q]]
assert len(vec)==32
assert [prev.dirs(v) for v in vec]==[prev.dirs(v) for v in prev.rankvec]

mins=[];anchors=[];total=0
B,G=64,8
for block,start in enumerate(range(0,len(bp2),B)):
    if block%G==0:anchors.append(total)
    e=0;low=0
    for v in bp2[start:start+B]:
        e+=2*v-1;low=min(low,e);total+=v
    mins.append(-low)
assert total==N and mins==prev.mins2 and anchors==prev.anchors2

rv=[prev.Rank(v,prev.dirs(v)) for v in vec]
rt,rm3,rm12=rv[:3]
wr={3:rv[3:13],12:rv[13:23],15:rv[23:32]}

def upto(q,l,h,t):
    r=wr[q];width=len(r)
    if t<0:return 0
    if t>=(1<<width)-1:return h-l
    v=t+1;ans=0
    for j,row in enumerate(r):
        zl=l-row.rank(l);zh=h-row.rank(h)
        if (v>>(width-1-j))&1:
            ans+=zh-zl
            l=row.m-row.total+row.rank(l)
            h=row.m-row.total+row.rank(h)
        else:l,h=zl,zh
    return ans

def count(i,r):
    l=rt.rank(i);h=rt.rank(i+sizes[i])
    if r==F(1,23):return h-l
    delta=1-23*r
    assert delta>0
    a,b=rm3.rank(l),rm3.rank(h)
    c,d=rm12.rank(l),rm12.rank(h)
    filt={3:(a,b),12:(c,d),15:(l-a-c,h-b-d)}
    return sum(upto(q,*filt[q],(36*q*delta.denominator)//delta.numerator) for q in (3,12,15))

index={path:i for i,path in enumerate(paths)}
checks=0
for r in prev.samples:
    direct=[0]*N
    for (q,n),path in prev.old.old.words.items():
        if r==F(1,23) or r>=(1-F(36*q,n))/23:
            for j in range(len(path)+1):
                direct[index[path[:j]]]+=1
    for i in range(N):
        assert count(i,r)==direct[i]
        checks+=1
assert checks==57600 and count(0,F(0))==605 and count(0,F(1,23))==1065
print('R5_BP_LABEL_TERM_BITS',len(bits),'PACKED_BYTES',len(raw))
print('REBUILT_MINIMA',len(mins),'ANCHORS',len(anchors),'WAVELET_LEVELS',sum(map(len,rows.values())))
print('REBUILT_PREFIX_PARAMETER_COMPARISONS',checks)
print('PASS_R5_REBUILD_FROM_BP_LABELS_REAL_1065')