#!/usr/bin/env python3
"""Reproduce exact block-stride sizes and Python lookup microbenchmark on frozen R5 trie.

From repository root (stacked PR #2166):
python research_notes/brc_r5_variable_skip_full_20261112/VERIFY_R5_STRIDE_BENCH.py

The imported sibling runs its own original-corpus exact roundtrip checks first.
This benchmark deliberately measures only subtree-size lookup with decoded bits in RAM.
It is not a full prefix query, disk I/O, allocator or general runtime benchmark.
"""
from statistics import median
from time import perf_counter_ns
from random import Random
import VERIFY_R5_VARIABLE_SKIP_FULL as full

S=full.sizes
n=len(S)
assert n==2880
bits=[]
for s in S:
    w=2 if s<=3 else 4 if s<=15 else 8 if s<=255 else 12
    tag={2:0,4:1,8:2,12:3}[w]
    bits += [(tag>>1)&1,tag&1]+[(s>>j)&1 for j in range(w-1,-1,-1)]
assert len(bits)==13436
order=list(range(n))
Random(20261112).shuffle(order)
total=sum(S)

for stride in (8,16,32,64,128,256,512):
    offsets=[]
    pos=0
    for i,s in enumerate(S):
        if i%stride==0:offsets.append(pos)
        w=2 if s<=3 else 4 if s<=15 else 8 if s<=255 else 12
        pos+=w+2
    assert pos==len(bits) and max(offsets)<(1<<16)

    def lookup(i):
        p=offsets[i//stride]
        for _ in range(i%stride):
            tag=(bits[p]<<1)|bits[p+1]
            p+=2+(2,4,8,12)[tag]
        tag=(bits[p]<<1)|bits[p+1]
        width=(2,4,8,12)[tag]
        value=0
        for b in bits[p+2:p+2+width]:
            value=(value<<1)|b
        return value

    assert all(lookup(i)==S[i] for i in range(n))
    sequential=[]
    shuffled=[]
    for rep in range(7):
        start=perf_counter_ns()
        sink=sum(lookup(i) for i in range(n))
        sequential.append((perf_counter_ns()-start)/1e6)
        start=perf_counter_ns()
        sink_random=sum(lookup(i) for i in order)
        shuffled.append((perf_counter_ns()-start)/1e6)
        assert sink==sink_random==total
    exactbits=42423+16*((n+stride-1)//stride)
    print('STRIDE',stride,
          'BITS',exactbits,'BYTES',(exactbits+7)//8,
          'MEDIAN_SEQUENTIAL_MS',round(median(sequential),3),
          'MEDIAN_SHUFFLED_MS',round(median(shuffled),3))
print('PASS_R5_ALL_STRIDE_EXACT_DECODE_2880_NODES')
