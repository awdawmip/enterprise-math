#!/usr/bin/env python3
"""Exact R5 prefix activation index; imports pinned 28-coordinate source verifier.
From repo root: python research_notes/brc_r5_bp_wavelet_prefix_20261112/VERIFY_R5_BP_WAVELET_PORTABLE.py
"""
from fractions import Fraction as F
from pathlib import Path
import sys

base=Path(__file__).resolve().parents[1]/'brc_r5_dual_zero_right_persistence_20261112'
sys.path.insert(0,str(base))
import VERIFY_TRIE_CODEC as old
f=old.f
Q=(3,12,15)
assert len(old.words)==1065 and old.N==2880 and old.E==2879

bp=[]; labels=[]; terminals=[]
def preorder(node):
    bp.append(1);terminals.append(int('_term' in node))
    for a in sorted(k for k in node if k!='_term'):
        labels.append(a);preorder(node[a])
    bp.append(0)
preorder(old.root)
assert (len(bp),len(labels),len(terminals),sum(terminals))==(5760,2879,2880,1065)

def pack(bits):
    v=bytearray((len(bits)+7)//8)
    for i,b in enumerate(bits):
        if b:v[i//8]|=1<<(7-i%8)
    return bytes(v)
def unpack(raw,count):
    assert len(raw)==(count+7)//8
    assert not count%8 or raw[-1]&((1<<(8-count%8))-1)==0
    return [(raw[i//8]>>(7-i%8))&1 for i in range(count)]
def label_bits(a):return [(a>>b)&1 for b in (3,2,1,0)]

# Source-derived DFS pair keys and three stable-partition wavelet matrices.
class Wavelet:
    def __init__(self,nums):
        self.length=len(nums);self.width=max(nums).bit_length()
        self.rows=[];self.zeros=[]
        cur=list(nums)
        for d in reversed(range(self.width)):
            row=sum(((v>>d)&1)<<i for i,v in enumerate(cur))
            self.rows.append(row)
            self.zeros.append(len(cur)-row.bit_count())
            cur=[v for v in cur if not (v>>d)&1]+[v for v in cur if (v>>d)&1]
    def upto(self,l,r,t):
        if t<=0:return 0
        if t>=2**self.width-1:return r-l
        v=t+1;acc=0
        for i,d in enumerate(reversed(range(self.width))):
            row=self.rows[i]
            ol=(row&((1<<l)-1)).bit_count();orr=(row&((1<<r)-1)).bit_count()
            zl=l-ol;zr=r-orr
            if (v>>d)&1:
                acc+=zr-zl;l=self.zeros[i]+ol;r=self.zeros[i]+orr
            else:l,r=zl,zr
        return acc

# The authoritative selected pair-word relation comes from predecessor.
# This construction independent of its LOUDS byte representation.
wordpairs={word:pair for pair,word in old.words.items()}
assert len(wordpairs)==1065
pairs=[];paths=[]
def walk(node,path=()):
    paths.append(path)
    if '_term' in node:pairs.append(wordpairs[path])
    for a in sorted(k for k in node if k!='_term'):
        walk(node[a],path+(a,))
walk(old.root)
assert len(paths)==2880 and len(pairs)==1065
numbers={q:[n for qq,n in pairs if qq==q] for q in Q}
wave={q:Wavelet(numbers[q]) for q in Q}
assert [(q,len(numbers[q]),wave[q].width) for q in Q]==[(3,538,10),(12,298,10),(15,229,9)]

# Serialize exact bits: balanced parentheses + 4-bit labels + terminal flags
# + wavelet rows (LSB-first by position); no duplicated terminal pair keys.
wavebits=[(row>>j)&1 for q in Q for row in wave[q].rows for j in range(wave[q].length)]
bits=bp+sum((label_bits(a) for a in labels),[])+terminals+wavebits
blob=pack(bits)
assert len(bits)==30577 and len(blob)==3823
replay=unpack(blob,len(bits))

# Decode the entire word corpus from actual packed bits and frozen W/K port sums.
pos=0
bp2=replay[pos:pos+len(bp)];pos+=len(bp)
label2=[]
for i in range(len(labels)):
    label2.append(sum((replay[pos+j]<<(3-j)) for j in range(4)));pos+=4
term2=replay[pos:pos+len(terminals)];pos+=len(terminals)
stack=[];paths2=[];close=[-1]*len(term2);opened=0;li=0
for i,b in enumerate(bp2):
    if b:
        if stack:
            a=label2[li];li+=1
            path=paths2[stack[-1]]+(a,)
        else:path=()
        paths2.append(path);stack.append(opened);opened+=1
    else:
        close[stack.pop()]=i
assert not stack and li==len(labels) and paths2==paths and bp2==bp and term2==terminals
pairs2=[]
for path,t in zip(paths2,term2):
    if t:
        n=-sum(f.W[j-1] for j in path)
        q=-sum((-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)[j-1] for j in path)//36
        pairs2.append((q,n))
assert pairs2==pairs and {pair:word for pair,word in zip(pairs2,(p for p,t in zip(paths2,term2) if t))}==old.words
for q in Q:
    vals=[n for qq,n in pairs2 if qq==q]
    for row in wave[q].rows:
        assert row==sum(replay[pos+j]<<j for j in range(len(vals)))
        pos+=len(vals)
assert pos==len(bits)

# Balanced-parentheses subtree = contiguous preorder node interval;
# terminal ranks yield [lo,hi) without storing per-node endpoints.
opened_prefix=[0]
for b in bp2:opened_prefix.append(opened_prefix[-1]+b)
terminal_prefix=[0]
for t in term2:terminal_prefix.append(terminal_prefix[-1]+t)
rank={path:i for i,path in enumerate(paths2)}
qmask={q:sum(1<<i for i,(qq,n) in enumerate(pairs2) if qq==q) for q in Q}
def bounds(path):
    i=rank[path]
    return terminal_prefix[i],terminal_prefix[opened_prefix[close[i]+1]]
def count(path,r):
    r=F(r);lo,hi=bounds(path)
    if r==F(1,23):return hi-lo
    assert f.L<=r<F(1,23)
    delta=1-23*r
    return sum(wave[q].upto((qmask[q]&((1<<lo)-1)).bit_count(),
                            (qmask[q]&((1<<hi)-1)).bit_count(),
                            (36*q*delta.denominator)//delta.numerator) for q in Q)

thresholds=sorted({(1-F(36*q,n))/23 for q,n in pairs})
assert len(thresholds)==953
samples=[f.L,F(-1),F(0),F(1,100),F(1,23)]
samples += [thresholds[j] for j in (0,1,17,132,310,501,777,950,952)]
samples += [(thresholds[j]+thresholds[j+1])/2 for j in (0,9,110,330,640,950)]
assert len(samples)==20
for r in samples:
    direct=[0]*len(paths2)
    for (q,n),word in old.words.items():
        if r==F(1,23) or r>=(1-F(36*q,n))/23:
            for j in range(len(word)+1):direct[rank[word[:j]]]+=1
    assert all(count(path,r)==direct[i] for i,path in enumerate(paths2))
for r in thresholds:
    assert count((),r)==sum((1-F(36*q,n))/23<=r for q,n in pairs)
assert count((),F(0))==605 and count((),F(1,23))==1065
print('BP_TOPOLOGY_BITS',len(bp),'LABEL_BITS',4*len(labels),'TERMINAL_BITS',len(terminals))
print('WAVELET_ROWS_BITS',len(wavebits))
print('BP_WAVELET_BITS',len(bits),'BYTES',len(blob))
print('PREFIX_NODES',len(paths2),'FULL_PREFIX_COMPARISONS',len(samples)*len(paths2))
print('ROOT_EVENT_COMPARISONS',len(thresholds))
print('ROUNDTRIP_PAIR_WORDS',len(pairs2),'A_ZERO',count((),F(0)))
print('PASS_R5_BP_WAVELET_STATIC_PREFIX_COUNT')
