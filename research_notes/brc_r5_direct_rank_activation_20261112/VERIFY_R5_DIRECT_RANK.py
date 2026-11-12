#!/usr/bin/env python3
"""R5 external P/Q–BRC 15-label first-zero activation: exact rank index.
No native X6 claim. Frozen W,K pin inherited from PR #2155 at d37154e5.
Python standard library; rational boundary comparisons throughout.
"""
from collections import defaultdict, Counter
from fractions import Fraction as F

W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
Q=(3,12,15)
M=1<<len(W)
weights=[0]*M
ports=[0]*M
for mask in range(1,M):
    bit=mask&-mask
    j=bit.bit_length()-1
    prev=mask^bit
    weights[mask]=weights[prev]+W[j]
    ports[mask]=ports[prev]+K[j]
fixed={-v for v in weights if v<=-3}
pairs=defaultdict(list)
for mask in range(1,M):
    n,k=-weights[mask],-ports[mask]
    if n in fixed and k in (108,432,540):
        pairs[k//36,n].append(mask)
assert len(fixed)==1144 and len(pairs)==1065
assert sum(len(v) for v in pairs.values())==2935

# Three q-level integer membership sets, no duplicates.
ns={q:sorted(n for qq,n in pairs if qq==q) for q in Q}
B={q:max(ns[q]) for q in Q}
C={q:len(ns[q]) for q in Q}
assert B=={3:844,12:592,15:508}
assert C=={3:538,12:298,15:229}
width={q:C[q].bit_length() for q in Q}
blocks={q:(B[q]+63)//64 for q in Q}
assert width=={3:10,12:9,15:8}
assert blocks=={3:14,12:10,15:8}

# Payload: membership bits indexed by n-1 then 64-bit block-prefix
# checkpoints for blocks 1..k, low bits first in each packed field.
# First block's checkpoint is zero implicitly. Header: three uint16 max-n.
def write_bits(bits):
    buf=bytearray((len(bits)+7)//8)
    for i,v in enumerate(bits):
        assert v in (0,1)
        buf[i//8]|=v<<(i%8)
    return bytes(buf)

def integer_bits(value,bits):
    assert 0<=value<(1<<bits)
    return [(value>>i)&1 for i in range(bits)]

body_bits=[]
for q in Q:
    v=sum(1<<(n-1) for n in ns[q])
    body_bits.extend(integer_bits(v,B[q]))
    for k in range(1,blocks[q]):
        rank=(v&((1<<(64*k))-1)).bit_count()
        body_bits.extend(integer_bits(rank,width[q]))
assert len(body_bits)==2211
payload=write_bits(body_bits)
assert len(payload)==277
header=b''.join(B[q].to_bytes(2,'little') for q in Q)
index_bytes=header+payload
assert len(index_bytes)==283

# Decode strictly from packed bytes, recomputing each checkpoint.
def read_bits(raw,offset,bits):
    value=0
    for j in range(bits):
        pos=offset+j
        value|=((raw[pos//8]>>(pos%8))&1)<<j
    return value,offset+bits

def decode(raw):
    assert len(raw)>=6
    bound={q:int.from_bytes(raw[2*i:2*i+2],'little') for i,q in enumerate(Q)}
    assert all(bound[q]>0 for q in Q)
    offset=0
    data={}
    for q in Q:
        nmax=bound[q]
        bitset,offset=read_bits(raw[6:],offset,nmax)
        count=bitset.bit_count()
        w=count.bit_length()
        nb=(nmax+63)//64
        checkpoints=[]
        for k in range(1,nb):
            rank,offset=read_bits(raw[6:],offset,w)
            checkpoints.append(rank)
            assert rank==(bitset&((1<<(64*k))-1)).bit_count()
        data[q]=(bitset,checkpoints,nmax,count)
    assert len(raw)==6+(offset+7)//8
    if offset%8:
        assert raw[6+offset//8]>>(offset%8)==0
    return data

index=decode(index_bytes)
for q in Q:
    v,checks,nmax,count=index[q]
    assert nmax==B[q] and count==C[q]
    assert [j+1 for j in range(nmax) if v>>j&1]==ns[q]

def rank_upto(q,t):
    bitset,checks,nmax,count=index[q]
    if t<=0:return 0
    if t>=nmax:return count
    block=(t-1)//64
    before=checks[block-1] if block else 0
    rem=t-64*block
    return before+((bitset>>(64*block))&((1<<rem)-1)).bit_count()

def active_count(r):
    r=F(r)
    if r>=F(1,23):return len(pairs)  # zero-scale endpoint
    delta=1-23*r
    assert delta>0
    return sum(rank_upto(q,36*q*delta.denominator//delta.numerator) for q in Q)

def direct_count(r):
    return sum((F(1)-F(36*q,n))/23<=r for q,n in pairs)

thresholds=sorted(set((1-F(36*q,n))/23 for q,n in pairs))
assert len(thresholds)==953
multiplicities=Counter((1-F(36*q,n))/23 for q,n in pairs)
assert Counter(multiplicities.values())=={1:869,2:56,3:28}
left=F(-427508577031693280,628800490619)
right=F(1,23)
assert left<thresholds[0] and thresholds[-1]<right
samples=[left,(left+thresholds[0])/2,right]
for i,t in enumerate(thresholds):
    samples.append(t)
    if i:
        samples.append((thresholds[i-1]+t)/2)
    if i+1<len(thresholds):
        samples.append((t+thresholds[i+1])/2)
for r in samples:
    assert active_count(r)==direct_count(r),(r,active_count(r),direct_count(r))
assert len(samples)==2860  # 953 events + 2*952 neighboring midpoints + 3
assert active_count(left)==0 and active_count(right)==1065
assert active_count(F(0))==605
assert active_count(F(-1))==32
assert active_count(F(1,100))==655
for i,t in enumerate(thresholds):
    before=active_count((thresholds[i-1]+t)/2 if i else (left+t)/2)
    assert active_count(t)-before==multiplicities[t]

print('FROZEN_MASKS',M,'FIXED_N',len(fixed),'ELIGIBLE_PAIRS',len(pairs))
print('Q_N_MAX',B,'Q_PAIR_COUNTS',C,'RANK_WIDTH_BITS',width)
print('BITVECTOR_BITS',sum(B.values()),'CHECKPOINT_BITS',sum((blocks[q]-1)*width[q] for q in Q))
print('INDEX_PAYLOAD_BITS',len(body_bits),'INDEX_PAYLOAD_BYTES',len(payload))
print('SELF_DESCRIBING_INDEX_BYTES',len(index_bytes))
print('ACTIVATION_EVENTS',len(thresholds),'MULTIPLICITIES',dict(Counter(multiplicities.values())))
print('EXACT_RATIONAL_TEST_POINTS',len(samples))
for r in (F(-10),F(-1),F(0),F(1,100),F(1,23)):
    print('QUERY',str(r),active_count(r))
print('PASS_R5_3FAMILY_EXACT_DIRECT_RANK_INDEX')
