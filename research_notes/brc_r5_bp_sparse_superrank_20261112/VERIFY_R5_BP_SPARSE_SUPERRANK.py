#!/usr/bin/env python3
"""R5 full frozen original-corpus bitstream, variable subtree skip + rank/wavelet.
Run at repository root after checking out this stacked research branch.
Imports already-pinned VERIFY_R5_BP_WAVELET_PORTABLE.py from PR #2161 ancestry.
"""
from fractions import Fraction as F
from pathlib import Path
import sys
bpdir=Path(__file__).resolve().parents[1]/'brc_r5_bp_wavelet_prefix_20261112'
sys.path.insert(0,str(bpdir))
import VERIFY_R5_BP_WAVELET_PORTABLE as old
paths,terms,labels,pairs=old.paths,old.terminals,old.labels,old.pairs
assert len(paths)==2880 and sum(terms)==len(pairs)==1065
N=len(paths);stack=[];sizes=[0]*N
for i,path in enumerate(paths):
    while len(stack)>len(path):
        top=stack.pop();sizes[top]=i-top
    assert len(stack)==len(path)
    stack.append(i)
while stack:
    top=stack.pop();sizes[top]=N-top
assert sizes[0]==2880

def sw(s):return 2 if s<=3 else 4 if s<=15 else 8 if s<=255 else 12
counts=tuple(sum(sw(s)==w for s in sizes) for w in (2,4,8,12))
assert counts==(2182,572,122,4)
class B:
    def __init__(self):self.v=[]
    def write(self,x,w):
        assert 0<=x<1<<w
        self.v.extend((x>>j)&1 for j in range(w-1,-1,-1))
    def extend(self,x):self.v.extend(x)

def dirs(v):
    a=[];b=[];tot=0
    for block in range((len(v)+63)//64):
        if block%8==0:
            base=tot
            if block:a.append(tot)
        else:b.append(tot-base)
        tot+=sum(v[block*64:(block+1)*64])
    return a,b

def wave(nums):
    seq=list(nums);ret=[]
    for bit in reversed(range(max(seq).bit_length())):
        row=[(x>>bit)&1 for x in seq];ret.append(row)
        seq=[x for x in seq if not ((x>>bit)&1)]+[x for x in seq if (x>>bit)&1]
    return ret
var=B();offsets=[]
for i,s in enumerate(sizes):
    if i%64==0:offsets.append(len(var.v))
    w=sw(s);var.write({2:0,4:1,8:2,12:3}[w],2);var.write(s,w)
assert len(var.v)==13436 and len(offsets)==45 and max(offsets)<65536
mask3=[int(q==3) for q,n in pairs]
mask12=[int(q==12) for q,n in pairs]
rows={q:wave([n for qq,n in pairs if qq==q]) for q in (3,12,15)}
assert [len(rows[q]) for q in (3,12,15)]==[10,10,9]
rankvec=[terms,mask3,mask12]+[x for q in (3,12,15) for x in rows[q]]
assert len(rankvec)==32
w=B()
for o in offsets:w.write(o,16)
w.extend(var.v)
for a in labels:w.write(a,4)
w.extend(terms);w.extend(mask3);w.extend(mask12)
for q in (3,12,15):
    for row in rows[q]:w.extend(row)
for v in rankvec:
    a,b=dirs(v)
    for x in a:w.write(x,len(v).bit_length())
    for x in b:w.write(x,9)
assert len(w.v)==43143
blob=bytearray((len(w.v)+7)//8)
for i,b in enumerate(w.v):
    if b:blob[i//8]|=1<<(7-i%8)
assert len(blob)==5393
# Decode all fields from actual byte stream, including every rank directory.
raw=[(blob[i//8]>>(7-i%8))&1 for i in range(len(w.v))]
class R:
    def __init__(self,raw):self.v=raw;self.pos=0
    def take(self,n):
        x=self.v[self.pos:self.pos+n];assert len(x)==n;self.pos+=n;return x
    def get(self,n):
        a=0
        for x in self.take(n):a=(a<<1)|x
        return a
r=R(raw)
off2=[r.get(16) for _ in offsets]
var2=r.take(len(var.v))
lab2=[r.get(4) for _ in labels]
term2=r.take(N);m3=r.take(1065);m12=r.take(1065)
rows2={q:[r.take(len([n for qq,n in pairs if qq==q])) for _ in rows[q]] for q in (3,12,15)}
rankdir=[]
for v in rankvec:
    Bn=(len(v)+63)//64;Sn=(len(v)+511)//512
    rankdir.append(([r.get(len(v).bit_length()) for _ in range(Sn-1)],
                    [r.get(9) for _ in range(Bn-Sn)]))
assert r.pos==len(raw) and off2==offsets and var2==var.v and lab2==labels
assert term2==terms and m3==mask3 and m12==mask12 and rows2==rows
assert rankdir==[dirs(x) for x in rankvec]

def size(i):
    pos=off2[i//64]
    for _ in range(i%64):
        tag=2*var2[pos]+var2[pos+1];pos+=2+(2,4,8,12)[tag]
    tag=2*var2[pos]+var2[pos+1];n=(2,4,8,12)[tag]
    return sum(var2[pos+2+j]<<(n-1-j) for j in range(n))
assert all(size(i)==s for i,s in enumerate(sizes))
# Walk decoded structure to reconstruct all original path labels.
recovered=[]
def walk(i,p):
    recovered.append(p);j=i+1
    while j<i+size(i):
        walk(j,p+(lab2[j-1],));j+=size(j)
    assert j==i+size(i)
walk(0,())
assert recovered==paths
assert {p for p,b in zip(recovered,term2) if b}==set(old.old.words.values())

class Rank:
    def __init__(self,arr,d):
        self.m=len(arr);self.a,self.b=d;self.total=sum(arr)
        self.bl=[sum(x<<j for j,x in enumerate(arr[i:i+64])) for i in range(0,len(arr),64)]
    def rank(self,i):
        if i==self.m:return self.total
        block=i//64;sup=block//8
        x=(self.a[sup-1] if sup else 0)
        if block%8:x+=self.b[block-sup-1]
        if i%64:x+=(self.bl[block]&((1<<(i%64))-1)).bit_count()
        return x
rv=[Rank(arr,d) for arr,d in zip(rankvec,rankdir)]
checks=0
for arr,rr in zip(rankvec,rv):
    s=0
    for i in range(len(arr)+1):
        assert rr.rank(i)==s;checks+=1
        if i<len(arr):s+=arr[i]
assert checks==15463
rt,rm3,rm12=rv[:3];wr={3:rv[3:13],12:rv[13:23],15:rv[23:32]}
def upto(q,l,h,t):
    row=wr[q];width=len(row)
    if t<0:return 0
    if t>=(1<<width)-1:return h-l
    t+=1;count=0
    for i,v in enumerate(row):
        zl=l-v.rank(l);zh=h-v.rank(h)
        if (t>>(width-i-1))&1:
            count+=zh-zl;l=v.m-v.total+v.rank(l);h=v.m-v.total+v.rank(h)
        else:l,h=zl,zh
    return count

def query(i,r):
    l=rt.rank(i);h=rt.rank(i+size(i))
    if r==F(1,23):return h-l
    t=1-23*r;assert t>0
    a,b=rm3.rank(l),rm3.rank(h)
    c,d=rm12.rank(l),rm12.rank(h)
    rr={3:(a,b),12:(c,d),15:(l-a-c,h-b-d)}
    return sum(upto(q,*rr[q],(36*q*t.denominator)//t.numerator) for q in (3,12,15))

ths=sorted({(1-F(36*q,n))/23 for q,n in pairs})
assert len(ths)==953
samples=[F(-1),F(-1,10),F(0),F(1,100),F(1,23)]
samples += [ths[j] for j in (0,1,17,132,310,501,777,950,952)]
samples += [(ths[j]+ths[j+1])/2 for j in (0,9,110,330,640,950)]
assert len(samples)==20
idx={p:i for i,p in enumerate(paths)}
qchecks=0
for t in samples:
    direct=[0]*N
    for (q,n),p in old.old.words.items():
        if t==F(1,23) or t>=(1-F(36*q,n))/23:
            for j in range(len(p)+1):direct[idx[p[:j]]]+=1
    for i in range(N):
        assert query(i,t)==direct[i];qchecks+=1
assert qchecks==57600 and query(0,F(0))==605
print('WORDS',len(pairs),'NODES',N,'SUBTREE_WIDTH_COUNTS',counts)
print('VARIABLE_BITS',len(var.v),'BLOCK_OFFSET_BITS',16*len(offsets))
print('PACKED_BITS',len(raw),'PACKED_BYTES',len(blob))
print('RANK_BOUNDARIES',checks,'PREFIX_QUERIES',qchecks)
print('PASS_R5_VARSKIP_REAL_CORPUS_PACKED_INDEX')


# --- New BP block minima with sparse superblock opening-rank anchors (R5) ---
# Reuses the *same* frozen corpus, complete query suffix, and exact comparator.
# No mutable Source data, no floating-point input, no new scientific pin.
from bisect import bisect_right
bp=old.bp
assert len(bp)==2*N==5760
B=64
G=8
mins=[]
for start in range(0,len(bp),B):
    depth=0
    smallest=0
    for bit in bp[start:start+B]:
        depth+=2*bit-1
        smallest=min(smallest,depth)
    mins.append(-smallest)
anchors=[sum(bp[:j*B]) for j in range(0,len(mins),G)]
assert len(mins)==90 and len(anchors)==12
assert max(mins)<(1<<7) and max(anchors)<(1<<12)

# Carry over every prior exact label / terminal / q / wavelet / rank-dir field.
# w.v is the previously verified variable-skip complete bitstream; its tail
# starts just after the width-codes and 16-bit block-offsets.
old_nav_bits=16*len(offsets)+len(var.v)
suffix=w.v[old_nav_bits:]
assert len(suffix)==28987
index=list(bp)
for m in mins:index.extend((m>>i)&1 for i in range(6,-1,-1))
for a in anchors:index.extend((a>>i)&1 for i in range(11,-1,-1))
index.extend(suffix)
assert len(index)==35521
raw=bytearray((len(index)+7)//8)
for i,b in enumerate(index):
    if b:raw[i//8]|=1<<(7-i%8)
assert len(raw)==4441
replay=[(raw[i//8]>>(7-i%8))&1 for i in range(len(index))]
assert replay==index
p=0
bp2=replay[p:p+len(bp)];p+=len(bp)
def field(width):
    global p
    v=0
    for b in replay[p:p+width]:v=2*v+b
    p+=width
    return v
mins2=[field(7) for _ in mins]
anchors2=[field(12) for _ in anchors]
assert bp2==bp and mins2==mins and anchors2==anchors
assert replay[p:]==suffix

def sparse_rank(pos):
    assert 0<=pos<=len(bp2)
    superidx=min(pos//(B*G),len(anchors2)-1)
    return anchors2[superidx]+sum(bp2[superidx*B*G:pos])

def sparse_select(i):
    assert 0<=i<N
    k=bisect_right(anchors2,i)-1
    assert k>=0
    v=anchors2[k]
    for pos in range(k*B*G,len(bp2)):
        if bp2[pos]:
            if v==i:return pos
            v+=1
    raise AssertionError('sparse_select failed')

def sparse_match(pos):
    assert bp2[pos]==1
    target=2*sparse_rank(pos)-pos
    excess=target+1
    boundary=min(len(bp2),(pos//B+1)*B)
    for j in range(pos+1,boundary):
        excess+=2*bp2[j]-1
        if excess==target:return j
    for k in range(boundary//B,len(mins2)):
        start=k*B;end=min((k+1)*B,len(bp2))
        if excess-mins2[k]>target:
            excess+=2*sum(bp2[start:end])-(end-start)
        else:
            for j in range(start,end):
                excess+=2*bp2[j]-1
                if excess==target:return j
    raise AssertionError('sparse_match failed')

# Original variable-skip size() was already validated against the frozen words.
old_size=size
def size(i):
    z=sparse_select(i)
    return (sparse_match(z)-z+1)//2
for i in range(N):
    assert sparse_rank(sparse_select(i))==i
    assert size(i)==old_size(i)
# Use the existing full packed-suffix Wavelet/rank query, but force it through
# *new* BP navigation because query() resolves global size() at call time.
qc=0
for t in samples:
    direct=[0]*N
    for (qq,nn),path in old.old.words.items():
        if t==F(1,23) or t>=(1-F(36*qq,nn))/23:
            for h in range(len(path)+1):direct[idx[path[:h]]]+=1
    for i in range(N):
        assert query(i,t)==direct[i]
        qc+=1
assert qc==57600 and query(0,F(0))==605
print('SPARSE_BP_REAL_CORPUS_BITS',len(index),'BYTES',len(raw))
print('SPARSE_BP_ANCHORS',len(anchors2),'MINIMA',len(mins2))
print('SPARSE_BP_NAV_NODES',N,'PREFIX_PARAMETER_CHECKS',qc)
print('PASS_R5_BP_SPARSE_SUPERRANK_REAL_1065')
