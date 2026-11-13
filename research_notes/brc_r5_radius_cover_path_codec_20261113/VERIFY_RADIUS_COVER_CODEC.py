#!/usr/bin/env python3
"""Exact radius-cover path ranker: standard-library integer arithmetic only.
Proof scope: any strictly increasing integral event coordinate array x.
No claim is made here that synthetic coordinates are the pinned R5 event array.
"""
from bisect import bisect_left, bisect_right
from itertools import combinations, product
from math import ceil
from random import Random
import json


def covers(x, s, radius):
    return max(min(abs(x[b]-x[p]) for p in s) for b in range(len(x))) <= radius


def graph(x, radius):
    n = len(x)
    assert n > 0 and all(isinstance(v,int) for v in x)
    assert all(x[i] < x[i+1] for i in range(n-1)) and radius >= 0
    starts=[i for i in range(n) if x[i]-x[0] <= radius]
    ends=set(i for i in range(n) if x[-1]-x[i] <= radius)
    edges=[[] for _ in range(n)]
    for p in range(n):
        for q in range(p+1,min(n,p+2*radius+2)):
            last_left=bisect_right(x,x[p]+radius)-1
            first_right=bisect_left(x,x[q]-radius)
            if first_right <= last_left+1:
                edges[p].append(q)
    return starts, ends, edges


def index(x,radius,k):
    n=len(x)
    assert 1<=k<=n
    starts,ends,edges=graph(x,radius)
    counts=[[0]*n for _ in range(k+1)]
    for p in ends:counts[1][p]=1
    for t in range(2,k+1):
        for p in range(n-1,-1,-1):
            counts[t][p]=sum(counts[t-1][q] for q in edges[p])
    total=sum(counts[k][p] for p in starts)
    return starts,edges,counts,total


def unrank(cache, k, rank):
    starts,edges,counts,total=cache
    if not 0<=rank<total:raise ValueError('rank outside radius-cover class')
    out=[]
    for p in starts:
        block=counts[k][p]
        if rank < block:
            out=[p];break
        rank -= block
    for remaining in range(k-1,0,-1):
        for q in edges[out[-1]]:
            block=counts[remaining][q]
            if rank < block:
                out.append(q);break
            rank -= block
        else:raise AssertionError('unreachable suffix')
    assert rank==0
    return tuple(out)


def rank_centers(cache, k, centers):
    starts,edges,counts,total=cache
    if len(centers)!=k or not centers or centers[0] not in starts:
        raise ValueError('inadmissible centers')
    r=sum(counts[k][p] for p in starts if p<centers[0])
    for j in range(k-1):
        p,q=centers[j],centers[j+1]
        if q not in edges[p]:raise ValueError('illegal edge')
        r+=sum(counts[k-1-j][v] for v in edges[p] if v<q)
    if counts[1][centers[-1]] != 1:raise ValueError('illegal final center')
    assert 0<=r<total
    return r


def byte_width(t):
    return 0 if t<=1 else (t-1).bit_length().__ceil__()//8 + int((t-1).bit_length()%8!=0)


def small_exhaustive():
    arrays=0; scenarios=0; admissible=0; ranked=0; empty=0
    for w in range(0,7):
        for inc in product((1,2,3),repeat=w):
            x=[0]
            for d in inc:x.append(x[-1]+d)
            arrays+=1
            for r in range(0,4):
                for k in range(1,w+2):
                    cache=index(x,r,k)
                    truth=[c for c in combinations(range(w+1),k) if covers(x,c,r)]
                    scenarios+=1
                    assert cache[3]==len(truth),(x,r,k,cache[3],len(truth))
                    if not truth:empty+=1
                    for i, c in enumerate(truth):
                        assert unrank(cache,k,i)==c
                        assert rank_centers(cache,k,c)==i
                        admissible+=1;ranked+=1
                    for v in (-1,len(truth)):
                        try:unrank(cache,k,v)
                        except ValueError:pass
                        else:raise AssertionError('invalid rank accepted')
    return dict(arrays=arrays,instances=scenarios,admissible_sequences=admissible,rank_unrank_checks=ranked,empty_classes=empty)


def synthetic_result():
    rng=Random(2026111313)
    inc=[3]*50+[2]*12+[1]*891
    assert len(inc)==953 and sum(inc)==1065
    rng.shuffle(inc)
    x=[0]
    for d in inc:x.append(x[-1]+d)
    cache=index(x,2,213)
    count=cache[3]
    return dict(boundaries=len(x),total_events=x[-1],increment_histogram={'1':891,'2':12,'3':50},radius=2,checkpoint_budget=213,count=str(count),bits=(count-1).bit_length() if count else 0,bytes=( (count-1).bit_length()+7)//8 if count else None,scope='deterministic synthetic distribution; not pinned R5 E')


if __name__=='__main__':
    small=small_exhaustive()
    counterexample=dict(x=[0,3,6],R=2,centers=[0,2],gap_bound_satisfied=True,covered=covers([0,3,6],[0,2],2))
    assert not counterexample['covered']
    sample=synthetic_result()
    out=dict(status='PASS_EXACT_RADIUS_COVER_PATH_RANK', theorem='Cover iff admissible path in exact event-coordinate graph',small_exhaustive=small,converse_gap_bound_counterexample=counterexample,synthetic_size_stress=sample,pinned_R5_E_loaded=False,scoped_to='index and combinatorial rank equivalence; no frozen-query recomputation or formal task Result')
    print(json.dumps(out,indent=2,sort_keys=True))
