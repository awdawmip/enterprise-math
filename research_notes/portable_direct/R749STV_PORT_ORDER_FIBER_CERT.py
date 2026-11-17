#!/usr/bin/env python3
"""R749STV exact finite checks of proposed source-order Port/Cell carrier.
This is structural combinatorics, not actual BRC kernel/heartbeat execution.
"""
from itertools import product
from math import comb
from pathlib import Path
import json

WEIGHTS = (1,1,2,3,6)  # frozen model, first two are distinct named labels A/B

def rank(w):
    a=w.count("A"); b=len(w)-a; r=0
    for label in w:
        if label=="B":
            if a: r+=comb(a+b-1,a-1)
            b-=1
        else: a-=1
    return r

def unrank(n,k,r):
    assert 0<=k<=n and 0<=r<comb(n,k)
    a=k; b=n-k; w=[]
    while a+b:
        before=comb(a+b-1,a-1) if a else 0
        if r<before:
            w.append("A"); a-=1
        else:
            w.append("B"); r-=before; b-=1
    assert r==0
    return "".join(w)

def endpoint(w):
    return (w.count("A"), w.count("B"), 0, 0, 0, 0)

def scalar_prefix(w):
    return tuple(range(1,len(w)+1))

def pop_outputs(w):
    out=[]
    while w:
        out.append(w[-1]); w=w[:-1]
    return "".join(out)

per_length=[]
for n in range(15):
    fibers={k:[] for k in range(n+1)}
    for letters in product("AB",repeat=n):
        w="".join(letters); k=w.count("A")
        assert endpoint(w)==(k,n-k,0,0,0,0)
        assert scalar_prefix(w)==tuple(range(1,n+1))
        assert pop_outputs(w)==w[::-1]
        fibers[k].append(w)
    for k,words in fibers.items():
        assert len(words)==comb(n,k)
        assert words==sorted(words)
        assert [rank(w) for w in words]==list(range(comb(n,k)))
        assert [unrank(n,k,r) for r in range(comb(n,k))]==words
    M=comb(n,n//2)
    per_length.append({"n":n,"total_scalar_fiber":2**n,
       "max_endpoint_fiber":M,"max_extra_bits":(M-1).bit_length()})

examples=[{"n":n,"k":n//2,"fiber":comb(n,n//2),
   "bits":(comb(n,n//2)-1).bit_length()} for n in (10,20,40)]
assert examples==[
    {"n":10,"k":5,"fiber":252,"bits":8},
    {"n":20,"k":10,"fiber":184756,"bits":18},
    {"n":40,"k":20,"fiber":137846528820,"bits":38}]
result={
  "unit":"R749STV","status":"AUTHOR_EXACT_NOT_REVIEWED",
  "frozen_science_pin":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
  "domain":"two named frozen weight-one sources, symbolic words on chosen X6 chart",
  "observer_scopes":["endpoint_after_append","endpoint_and_provenance_pop"],
  "no_actual_brc_execution":True,
  "exhaustively_checked_lengths":list(range(15)),
  "enumerated_words":32767,
  "rank_unrank_pairs_checked":32767,
  "per_length":per_length,"examples":examples,
  "proof":"exact binomial fibers, output separation and rank/unrank induction in MD",
  "next":"match proposed port operations against actual permitted typed BRC Cell/Link/Port dynamics"}
Path(__file__).with_name("R749STV_PORT_ORDER_FIBER_RESULTS.json").write_text(
    json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print("PASS: 32767 exact words; ranks, endpoints, prefixes and pop traces")
