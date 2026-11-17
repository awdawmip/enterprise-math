#!/usr/bin/env python3
"""Exact finite regression for a five-source WINDOW-PEEK + bounded-POP path interface.

The interface is a mathematical provenance adapter, not a native physical BRC event.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from math import factorial, prod
from pathlib import Path
import json

ALPHABET = tuple('ABCDE')
WEIGHTS = (1,1,2,3,6)
MAX_LENGTH=7
MAX_WINDOW=3
MAX_BUDGET=3

@lru_cache(None)
def suffix_count(counts,s):
    if s==0: return 1
    if s>sum(counts): return 0
    return sum(suffix_count(counts[:i]+(n-1,)+counts[i+1:],s-1)
               for i,n in enumerate(counts) if n)

def multinomial(a):
    return factorial(sum(a))//prod(factorial(x) for x in a)

def independent_count(n,s):
    return sum(multinomial(a) for a in product(*(range(v+1) for v in n)) if sum(a)==s)

def peek(w,t):
    if not t:return ()
    return tuple(w[-t:])

def observation_signature(w,t,r):
    """Maximal POP trace also includes every shorter POP trace as a prefix.
    Each k-th POP emits a label; each stage exposes PEEK_t. No source APPEND is needed
    to test the full original-history depth; the theorem covers arbitrary public APPEND.
    """
    stack=tuple(w)
    out=[]
    for k in range(min(r,len(w))+1):
        out.append(('peek',peek(stack,t)))
        if k<min(r,len(w)):
            out.append(('pop',stack[-1]))
            stack=stack[:-1]
    return tuple(out)

def rank_suffix(counts,suffix):
    counts=tuple(counts); rank=0; s=len(suffix)
    for letter in suffix:
        pos=ALPHABET.index(letter)
        assert counts[pos]>0
        for j in range(pos):
            if counts[j]:
                alt=list(counts); alt[j]-=1
                rank+=suffix_count(tuple(alt),s-1)
        alt=list(counts); alt[pos]-=1
        counts=tuple(alt); s-=1
    return rank

def unrank_suffix(counts,s,k):
    counts=tuple(counts)
    assert 0<=k<suffix_count(counts,s)
    out=[]
    while s:
        for j,n in enumerate(counts):
            if n==0:continue
            alt=list(counts); alt[j]-=1
            block=suffix_count(tuple(alt),s-1)
            if k<block:
                out.append(ALPHABET[j]);counts=tuple(alt);s-=1;break
            k-=block
        else:raise AssertionError('unrank failed')
    return tuple(out)

def oracle_exhaustive():
    words_total=0; vectors_total=0; cases_total=0; codec_checks=0
    for ell in range(MAX_LENGTH+1):
        by_counts=defaultdict(list)
        for w in product(ALPHABET,repeat=ell):
            counts=tuple(w.count(a) for a in ALPHABET)
            by_counts[counts].append(w)
            words_total+=1
        for n,words in by_counts.items():
            vectors_total+=1
            for t in range(MAX_WINDOW+1):
                for r in range(MAX_BUDGET+1):
                    s=min(ell,t+r)
                    classes=defaultdict(set)
                    for w in words:
                        classes[observation_signature(w,t,r)].add(w[-s:] if s else ())
                    # The trace classes are exactly the feasible length-s suffixes.
                    distinct_suffixes={w[-s:] if s else () for w in words}
                    assert len(classes)==len(distinct_suffixes)==suffix_count(n,s)==independent_count(n,s), (ell,n,t,r)
                    assert all(len(c)==1 for c in classes.values()), (ell,n,t,r)
                    # Decode each rank exactly for the feasible suffix classes.
                    ranks={rank_suffix(n,suf) for suf in distinct_suffixes}
                    assert ranks==set(range(len(distinct_suffixes)))
                    for k in ranks:
                        assert unrank_suffix(n,s,k) in distinct_suffixes
                        codec_checks+=1
                    cases_total+=1
    return words_total,vectors_total,cases_total,codec_checks

def example(n,t,r):
    ell=sum(n)
    old=suffix_count(n,min(r,ell))
    new=suffix_count(n,min(r+t,ell))
    return {"inventory":list(n),"length":ell,"peek_window":t,"pop_budget":r,
            "old_pop_only_classes":old,"window_plus_pop_classes":new,
            "old_fixed_bits":(old-1).bit_length(),"new_fixed_bits":(new-1).bit_length()}

def main():
    w,v,c,codec=oracle_exhaustive()
    assert (w,v)==(97656,792),(w,v)
    assert c==792*16,c
    assert observation_signature(tuple('AB'),1,0)!=observation_signature(tuple('BA'),1,0)
    assert observation_signature(tuple('ABC'),1,1)!=observation_signature(tuple('BAC'),1,1)
    data={
       "status":"PASS",
       "claim":"Fixed composition fiber: total POP budget r and public exact label peek window t identify exactly last min(ell,r+t) original letters; optimal extra bits = ceil(log2 feasible suffix count).",
       "scope":"positive path-formal provenance adapter only, no native BRC Port guard or physical event executed",
       "source_weights":dict(zip(ALPHABET,WEIGHTS)),
       "raw_spatial_dimensions":6,
       "checked_max_word_length":MAX_LENGTH,
       "checked_max_peek_window":MAX_WINDOW,
       "checked_max_pop_budget":MAX_BUDGET,
       "exhaustive_words":w,
       "composition_vectors":v,
       "window_pop_cases":c,
       "rank_unrank_checks":codec,
       "example_six":example((2,1,1,1,1),2,1),
       "example_ten":example((2,2,2,2,2),3,2),
       "falsification_witness":{"same_endpoint_words":["AB","BA"],"r":0,"t":1,"observations":["B","A"]},
       "proof_status":"author exact mathematical proof, independent review not performed",
    }
    output=Path(__file__).with_name('R749STX_WINDOW_PEEK_POP_RESULTS.json')
    output.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(data,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
