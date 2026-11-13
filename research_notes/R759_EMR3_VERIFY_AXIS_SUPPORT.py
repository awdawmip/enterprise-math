#!/usr/bin/env python3
"""R759-EMR3 exact candidate X6 zero-area loop/auxiliary S7 frame checker.
Uses exact integer path areas and tuple-permutation BFS; not native force dynamics.
"""
from collections import Counter, deque
from itertools import combinations
from math import factorial, ceil
import json

I=tuple(range(7)) # labels 0=auxiliary star, 1..6=spatial-axis names
AXES=tuple(range(1,7))
PAIRS=tuple(combinations(AXES,2))

def mul(a,b):
    return tuple(a[b[k]] for k in range(7))

def inverse(a):
    return tuple(a.index(k) for k in range(7))

def trans(i):
    p=list(I);p[0],p[i]=p[i],p[0];return tuple(p)

T={i:trans(i) for i in AXES}

def word(i,j):
    assert 1<=i<j<=6
    return ((i,1),(j,1),(i,-1),(j,-1),(i,1),(j,-1),(i,-1),(j,1))

def endpoint_area(w):
    x=[0]*7
    A={p:0 for p in PAIRS}
    for i,s in w:
        for a in range(1,i):
            A[(a,i)]+=x[a]*s
        x[i]+=s
    return tuple(x),tuple(A[p] for p in PAIRS)

def frame(w):
    g=I
    for i,s in w:
        assert i in T and s in (-1,1)
        g=mul(T[i],g)
    return g

def gpair(i,j):
    return frame(word(i,j))

def bfs(generators):
    steps=tuple(generators)+tuple(inverse(g) for g in generators)
    dist={I:0}
    q=deque([I])
    while q:
        f=q.popleft()
        for g in steps:
            nxt=mul(g,f)
            if nxt not in dist:
                dist[nxt]=dist[f]+1
                q.append(nxt)
    return dist

def verify():
    for i,j in PAIRS:
        w=word(i,j)
        assert endpoint_area(w)==((0,)*7,(0,)*15)
        assert frame(w)==mul(T[j],T[i])
        reversed_w=tuple((a,-s) for a,s in reversed(w))
        assert endpoint_area(reversed_w)==((0,)*7,(0,)*15)
        assert frame(reversed_w)==inverse(frame(w))

    support_rows=[]
    for m in range(7):
        S=AXES[:m]
        reach=bfs([gpair(i,j) for i,j in combinations(S,2)])
        size=factorial(m+1)//2 if m>=1 else 1
        assert len(reach)==size
        assert all(all(g[j]==j for j in AXES if j not in S) for g in reach)
        support_rows.append({
            "axis_count":m,
            "frame_states":size,
            "minimum_binary_repair_bits":(size-1).bit_length(),
            "minimum_canonical_pair_block_count":ceil(m/2) if m>=2 else 0
        })

    classes=Counter()
    metrics={}
    total=0
    for k in (1,2,3):
        for E in combinations(PAIRS,k):
            S=set(x for ij in E for x in ij)
            m=len(S)
            d=bfs([gpair(i,j) for i,j in E])
            size=factorial(m+1)//2
            assert len(d)==size,(E,len(d),size)
            assert all(all(g[j]==j for j in AXES if j not in S) for g in d)
            classes[(k,m,size)]+=1
            total+=1
            if k==ceil(m/2):
                hist=[Counter(d.values())[i] for i in range(max(d.values())+1)]
                if m not in metrics:
                    metrics[m]={"block_count":k,"generator_sets":0,
                                "diameter":max(d.values()),"histogram":hist,
                                "sample_pairs":[list(p) for p in E]}
                assert metrics[m]["diameter"]==max(d.values())
                assert metrics[m]["histogram"]==hist
                metrics[m]["generator_sets"]+=1

    assert total==15+105+455==575
    assert {m:r["generator_sets"] for m,r in metrics.items()}=={2:15,3:60,4:45,5:180,6:15}
    assert {m:r["diameter"] for m,r in metrics.items()}=={2:1,3:3,4:6,5:7,6:9}
    result={
       "schema":"R759_EMR3_X6_FLAT_LOOP_AXIS_SUPPORT_EXACT_V1",
       "frozen_science_commit":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
       "predecessor_research_commit":"648672b9d1ed6c4709a346c649cef0c666837ae2",
       "model":"CANDIDATE_X6_ZERO_ENDPOINT_ZERO_15_AREA_AUXILIARY_S7_STAR_TRANSPOSITION",
       "canonical_witnesses_and_reversals_checked":15,
       "support_filtration":support_rows,
       "canonical_pair_block_subsets_checked":total,
       "subset_classification":[
          {"block_count":k,"supported_axes":m,"group_order":sz,"number_of_sets":count}
          for (k,m,sz),count in sorted(classes.items())
       ],
       "minimum_library_metrics":{str(m):metrics[m] for m in sorted(metrics)},
       "native_triadic_closure_verified":False,
       "native_v29_v39_morphism_verified":False,
       "exact_finite_checks":"PASS"
    }
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return result

if __name__=="__main__":
    verify()
