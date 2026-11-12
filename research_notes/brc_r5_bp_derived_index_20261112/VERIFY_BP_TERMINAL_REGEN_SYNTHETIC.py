#!/usr/bin/env python3
"""Exact synthetic 3-port prefix-trie pack/rebuild and Wavelet count test."""
from fractions import Fraction as F
from itertools import combinations
W=[0]*15;K=[0]*15
for a,q in enumerate((3,12,15)):
    K[a]=-36*q;W[a]=-1
for a in range(3,15):W[a]=-(1<<(a-3))
words={}
for root,q in enumerate((3,12,15),1):
    for pair in combinations(range(4,16),2):
        path=(root,)+pair
        n=-sum(W[a-1] for a in path)
        words[q,n]=path
assert len(words)==198
trie={}
for pair,path in words.items():
    node=trie
    for a in path:node=node.setdefault(a,{})
    node['_end']=True
bp=[];labels=[];terms=[];paths=[]
def emit(node,path):
    bp.append(1);paths.append(path);terms.append(int('_end' in node))
    for a in sorted(x for x in node if x!='_end'):
        labels.append(a);emit(node[a],path+(a,))
    bp.append(0)
emit(trie,())
N=len(terms)
assert len(bp)==2*N and len(labels)==N-1
bits=bp+[bit for a in labels for bit in ((a>>3)&1,(a>>2)&1,(a>>1)&1,a&1)]+terms
buf=bytearray((len(bits)+7)//8)
for i,v in enumerate(bits):
    if v:buf[i//8]|=1<<(7-i%8)
raw=[(buf[i//8]>>(7-i%8))&1 for i in range(len(bits))]
assert raw==bits
p=2*N;b2=raw[:p];lab=[]
for _ in labels:
    lab.append(sum(raw[p+j]<<(3-j) for j in range(4)));p+=4
term2=raw[p:p+N]
stack=[];decoded=[];sz=[0]*N;li=0
for v in b2:
    if v:
        path=decoded[stack[-1]]+(lab[li],) if stack else ()
        if stack:li+=1
        decoded.append(path);stack.append(len(decoded)-1)
    else:
        i=stack.pop();sz[i]=len(decoded)-i
assert decoded==paths and term2==terms and li==N-1
pairs=[]
for path,t in zip(decoded,term2):
    if not t:continue
    n=-sum(W[a-1] for a in path)
    k=-sum(K[a-1] for a in path)
    assert k%36==0
    pairs.append((k//36,n))
assert {pair:path for pair,path in zip(pairs,(p for p,t in zip(paths,terms) if t))}==words

def wave(nums):
    width=max(nums).bit_length();rows=[];cur=list(nums)
    for bit in reversed(range(width)):
        row=[(v>>bit)&1 for v in cur];rows.append(row)
        cur=[v for v in cur if not ((v>>bit)&1)]+[v for v in cur if (v>>bit)&1]
    return rows

def upto(nums,l,h,t):
    rows=wave(nums);width=len(rows)
    if t<0:return 0
    if t>=(1<<width)-1:return h-l
    ans=0;v=t+1
    for j,row in enumerate(rows):
        left=sum(row[:l]);right=sum(row[:h])
        zl=l-left;zh=h-right
        if (v>>(width-j-1))&1:
            ans+=zh-zl
            l=len(row)-sum(row)+left
            h=len(row)-sum(row)+right
        else:l,h=zl,zh
    return ans

prefix=[0]
for t in term2:prefix.append(prefix[-1]+t)
idx={path:i for i,path in enumerate(decoded)}
qs=(3,12,15)
nums={q:[n for qq,n in pairs if qq==q] for q in qs}
marks={q:[int(qq==q) for qq,n in pairs] for q in qs}
thresholds=sorted({(1-F(36*q,n))/23 for q,n in pairs})
samples=[F(-1),F(0),F(1,100),F(1,23)]+thresholds[::max(1,len(thresholds)//40)]
checks=0
for r in samples:
    direct=[0]*N
    for (q,n),path in words.items():
        if r==F(1,23) or r>=(1-F(36*q,n))/23:
            for h in range(len(path)+1):
                direct[idx[path[:h]]]+=1
    for i in range(N):
        l,h=prefix[i],prefix[i+sz[i]]
        if r==F(1,23):actual=h-l
        else:
            d=1-23*r
            actual=0
            for q in qs:
                a=sum(marks[q][:l]);b=sum(marks[q][:h])
                actual+=upto(nums[q],a,b,(36*q*d.denominator)//d.numerator)
        assert actual==direct[i]
        checks+=1
print('SYNTHETIC_3_PORT_PAIRS',len(words),'TRIE_NODES',N)
print('SYNTHETIC_PREFIX_ACTIVATION_CHECKS',checks)
print('PASS_BP_TERMINAL_REGEN_SYNTHETIC')