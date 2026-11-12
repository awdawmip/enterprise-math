#!/usr/bin/env python3
"""Exact R5 four-class Huffman width-tag arithmetic and synthetic codec check.

Independent of the 28-coordinate source. Takes four class counts as
frozen evidence from PR #2166. Synthetic values have those exact class
counts; full original-corpus integration is in VERIFY_HUFFMAN_WIDTH_FULL.py.
"""
from collections import Counter
from random import Random

N=2880
COUNTS={2:2182,4:572,8:122,12:4}
CODES={2:'0',4:'10',8:'110',12:'111'}
LABELS={2:1,4:4,8:16,12:256}

def width(s): return 2 if s<=3 else 4 if s<=15 else 8 if s<=255 else 12

values=[LABELS[k] for k,c in COUNTS.items() for _ in range(c)]
Random(20261112).shuffle(values)
assert len(values)==N and Counter(map(width,values))==COUNTS

def enc(B):
    bits='';off=[]
    for i,s in enumerate(values):
        if i%B==0: off.append(len(bits))
        k=width(s);bits+=CODES[k]+format(s,f'0{k}b')
    return bits,off

def dec(bits,offs,B,i):
    p=offs[i//B]
    for _ in range(i%B+1):
        if bits[p]=='0':k=2;p+=1
        elif bits[p+1]=='0':k=4;p+=2
        elif bits[p+2]=='0':k=8;p+=3
        else:k=12;p+=3
        v=int(bits[p:p+k],2);p+=k
    return v

tagbits=sum(COUNTS[k]*len(CODES[k]) for k in COUNTS)
payloadbits=sum(COUNTS[k]*k for k in COUNTS)
assert tagbits==3704 and payloadbits==7676
assert sum(COUNTS.values())==N
# Huffman's merging cost proves optimality among binary prefix-code tags.
assert (4+122)+(4+122+572)+(4+122+572+2182)==3704
assert 2*N-tagbits==2056
print('FROZEN_CLASS_COUNTS',COUNTS)
print('HUFFMAN_TAG_BITS',tagbits,'OLD_TWO_BIT_TAG_BITS',2*N)
print('UNMODIFIED_PAYLOAD_BITS',payloadbits)
for B in (8,16,32,64,128,256,512):
    bits,off=enc(B)
    assert len(bits)==tagbits+payloadbits==11380
    assert max(off)<(1<<16)
    assert all(dec(bits,off,B,i)==s for i,s in enumerate(values))
    total=payloadbits+tagbits+28987+16*len(off)
    assert total==40367+16*((N+B-1)//B)
    print('STRIDE',B,'BITS',total,'BYTES',(total+7)//8,'ROUNDTRIPS',N)
assert (40367+16*45+7)//8==5136
print('PASS_R5_HUFFMAN_ARITHMETIC_SYNTHETIC_2880')
