#!/usr/bin/env python3
"""PREFIX-488 certificate: zero-displacement zero-special q=0 BRC source-mask slice.
Unweighted Boolean-support computation, integer-only; retains original path order in
separate exhaustive small-length check. Not a phase/physical-time calculation.
"""
from collections import Counter
from functools import lru_cache
from math import comb

ALPHABET = 'aAbBcCdDeE'

def formula(m):
    if m == 0:
        return {1: 1, 2: 0, 4: 0, 3: 0, 5: 0, 6: 0, 7: 0}
    return {1: m+2, 2: m, 4: 2*m-1, 3: m-1,
            5: 0, 6: (m-1)**2, 7: comb(m,2)}

def polygon_mask(m,v,w):
    n = (v >= w and (v-w)%2 == 0 and v+w <= 2*m)
    b = (0 <= w <= m-1 and 1 <= v <= 2*m-w-1)
    c = (1 <= w <= m and 0 <= v <= 2*m-w-1)
    return n + 2*b + 4*c

def raw_mask(m):
    masks = {}
    for pa in range(m+1):
      for pb in range(m-pa+1):
       for pc in range(m-pa-pb+1):
        for pd in range(m-pa-pb-pc+1):
         pe = m-pa-pb-pc-pd
         key=(pb+2*pd+pe,pc+pe)
         bit = (1 if not(pb or pc) else 0) | (2 if pb else 0) | (4 if pc else 0)
         masks[key]=masks.get(key,0)|bit
    return masks

def all_words_for_counts(counts):
    path=[]
    total=sum(counts)
    def dfs():
        if len(path)==total:
            yield ''.join(path)
            return
        for i in range(len(ALPHABET)):
            if counts[i]:
                counts[i]-=1
                path.append(ALPHABET[i])
                yield from dfs()
                path.pop()
                counts[i]+=1
    yield from dfs()

def final_q(word,gate):
    return max((i for i in range(len(gate)+1) if word.endswith(gate[:i])),default=0)

def first_source(word):
    for v in word:
        if v in 'bB': return 2
        if v in 'cC': return 4
    return 1

def all_ordered_masks(m,gate):
    masks={}
    tested=0
    for pa in range(m+1):
      for pb in range(m-pa+1):
       for pc in range(m-pa-pb+1):
        for pd in range(m-pa-pb-pc+1):
         pe=m-pa-pb-pc-pd
         key=(pb+2*pd+pe,pc+pe)
         counts=[q for p in (pa,pb,pc,pd,pe) for q in (p,p)]
         for word in all_words_for_counts(counts):
            tested+=1
            if final_q(word,gate)==0:
                masks[key]=masks.get(key,0)|first_source(word)
    return masks,tested

def main():
    ordered_count={}
    total_vectors=0
    for m in range(0,35):
        raw=raw_mask(m)
        total_vectors+=comb(m+4,4)
        geo={(v,w):polygon_mask(m,v,w) for w in range(m+1) for v in range(2*m-w+1)}
        assert raw==geo,(m,'image-mismatch',set(raw.items())^set(geo.items()))
        cnt=Counter(raw.values())
        assert all(cnt.get(k,0)==want for k,want in formula(m).items()),(m,cnt,formula(m))
        assert len(raw)==(m+1)*(3*m+2)//2
        assert sum(cnt.values())==len(raw)
        assert cnt.get(5,0)==0
        if m in (0,1,2,3,4,8,16,34):
            print(f'm={m:02d} n={2*m:02d} image={len(raw)} '+
                  ' '.join(f'{k}:{cnt.get(k,0)}' for k in (1,2,4,3,5,6,7)))
    for gate in ('aab','aba'):
        for m in range(0,4):
            ordered,tested=all_ordered_masks(m,gate)
            assert ordered==raw_mask(m),(gate,m,ordered,raw_mask(m))
            ordered_count[(gate,m)]=tested
            print(f'ordered gate={gate} m={m} paths_checked={tested} masks={len(ordered)}')
    print('parikh_integer_vectors_checked=',total_vectors)
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
