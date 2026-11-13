#!/usr/bin/env python3
"""R5 fixed-span histogram ratio-chain decoder. Exact integer-only verifier.
Frozen R5 center bytes inherited from PR #2232/#2239; no rational E rebuild.
"""
from collections import Counter
from itertools import product
from math import factorial
from hashlib import sha256
from time import perf_counter_ns
from statistics import median
import json

N, SPAN, FIRST = 212, 951, 1
OLD56 = "d500a95a516544511a50596555556a5a441665a66a9195956669611456565551aa5669aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6a00"
OLD35 = "00014b1f759979509038593cf589c89a633140df206d08354b61a6f0b7dbc5639d8ce6"

def multinomial(a,b,c):
    return factorial(a+b+c)//(factorial(a)*factorial(b)*factorial(c))

def slow_classes(n,L):
    for a in range(n+1):
        b=5*n-L-2*a; c=L-4*n+a
        if b>=0 and c>=0:
            yield a,b,c,multinomial(a,b,c)

def fast_classes(n,L):
    amin=max(0,4*n-L)
    amax=min(n,(5*n-L)//2)
    if amin>amax: return
    a=amin; b=5*n-L-2*a; c=L-4*n+a
    m=multinomial(a,b,c)
    while True:
        yield a,b,c,m
        if a==amax: return
        assert b>=2 and (m*b*(b-1))%((a+1)*(c+1))==0
        m=m*b*(b-1)//((a+1)*(c+1))
        a+=1; b-=2; c+=1

def unrank_multiset(rank,counts):
    a,b,c=counts
    m=multinomial(a,b,c)
    if not 0<=rank<m: raise ValueError("out-of-range multiset rank")
    counts=[a,b,c]; n=sum(counts); result=[]
    while n:
        for i,symbol in enumerate((3,4,5)):
            block=m*counts[i]//n
            if rank<block:
                result.append(symbol); m=block; counts[i]-=1; n-=1
                break
            rank-=block
        else: raise AssertionError("prefix blocks")
    assert rank==0
    return result

def unrank_span(rank,n,L,fast=True):
    if rank<0: raise ValueError("negative rank")
    for a,b,c,m in (fast_classes(n,L) if fast else slow_classes(n,L)):
        if rank<m: return unrank_multiset(rank,(a,b,c))
        rank-=m
    raise ValueError("out-of-range span rank")

def rank_span(word):
    if any(v not in (3,4,5) for v in word): raise ValueError("bad symbol")
    n=len(word); L=sum(word); freq=Counter(word); rank=0
    for a,b,c,m in fast_classes(n,L):
        if a!=freq[3]:
            rank+=m; continue
        counts=[a,b,c]; remaining=m; t=n
        for x in word:
            k=x-3
            rank+=sum(remaining*counts[i]//t for i in range(k))
            remaining=remaining*counts[k]//t
            counts[k]-=1; t-=1
        assert remaining==1
        return rank
    raise ValueError("bad histogram")

def centers56(hexval):
    raw=bytes.fromhex(hexval)
    assert len(raw)==56 and int.from_bytes(raw[:2],"little")==213
    packed=int.from_bytes(raw[2:],"little")
    centers=[packed&3]; packed>>=2
    for _ in range(N):
        d=packed&3; packed>>=2
        assert d<3
        centers.append(centers[-1]+3+d)
    assert packed==0
    return centers

def restore(first,gaps):
    out=[first]
    for gap in gaps:out.append(out[-1]+gap)
    return out

original=centers56(OLD56)
assert sha256(bytes.fromhex(OLD56)).hexdigest()=="bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326"
assert original[0]==1 and original[-1]==952 and len(original)==213
gaps=[b-a for a,b in zip(original,original[1:])]
assert Counter(gaps)==Counter({3:16,4:77,5:119})
r=int.from_bytes(bytes.fromhex(OLD35),"big")
assert sha256(bytes.fromhex(OLD35)).hexdigest()=="9a1baae24527efdcb30a208330500e3e6e460c738facc4d39ad26451d03328fa"
assert restore(FIRST,unrank_span(r,N,SPAN))==original
assert unrank_span(r,N,SPAN)==unrank_span(r,N,SPAN,False)
assert rank_span(gaps)==r
assert list(fast_classes(N,SPAN))==list(slow_classes(N,SPAN))
assert sum(z[3] for z in fast_classes(N,SPAN)).bit_length()==275
count=0
for n in range(9):
    for tup in product((3,4,5),repeat=n):
        word=list(tup); L=sum(word); rank=rank_span(word)
        assert unrank_span(rank,n,L)==unrank_span(rank,n,L,False)==word
        assert list(fast_classes(n,L))==list(slow_classes(n,L))
        count+=1
assert count==9841
T=sum(x[3] for x in fast_classes(N,SPAN))
for bad in (-1,T):
    try:unrank_span(bad,N,SPAN);raise AssertionError("invalid rank accepted")
    except ValueError:pass

def timing_us(fn,repeat=150,rounds=17):
    values=[]
    for _ in range(rounds):
        t=perf_counter_ns()
        for __ in range(repeat):fn()
        values.append((perf_counter_ns()-t)/repeat/1000)
    return round(median(values),3)

result={
 "status":"PASS_R5_FIXED_SPAN_RATIO_CHAIN",
 "science_pin":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
 "input":"PR #2239 exact published 35-byte rank and PR #2232 56-byte center payload",
 "original_center_sha256":sha256(bytes.fromhex(OLD56)).hexdigest(),
 "original_span35_sha256":sha256(bytes.fromhex(OLD35)).hexdigest(),
 "histogram_classes":len(list(fast_classes(N,SPAN))),
 "fixed_span_class_cardinality":str(T),"fixed_span_bits":T.bit_length(),
 "center_equivalence":len(original),"exhaustive_small_words":count,
 "invalid_rank_cases":2,
 "median_17_rounds_us":{
   "slow_histogram":timing_us(lambda:unrank_span(r,N,SPAN,False)),
   "ratio_chain":timing_us(lambda:unrank_span(r,N,SPAN,True))
 },
 "scope":"Derivative center decoding and exhaustive n<=8 ternary words; frozen rational E not rebuilt",
 "formal_claim":False,"independent_review":False
}
print(json.dumps(result,indent=2))
