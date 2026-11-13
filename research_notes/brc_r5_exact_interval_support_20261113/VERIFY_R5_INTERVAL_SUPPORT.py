#!/usr/bin/env python3
"""Exact successor-interval theorem on frozen R5 rational-event data.
Standard library only; no task CLAIM or theorem admission is implied.
"""
from bisect import bisect_left, bisect_right
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from hashlib import sha256
import json

PIN = '435e77af0d180eac32bd1f9c4c464bc4010b7551'
WEIGHTS = (336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0 = (-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)

def frozen_events():
    groups = {3:set(),12:set(),15:set()}
    for mask in range(1, 1 << len(WEIGHTS)):
        n = -sum(w for i,w in enumerate(WEIGHTS) if mask >> i & 1)
        k = -sum(w for i,w in enumerate(K0) if mask >> i & 1)
        if n >= 3 and k % 36 == 0 and k // 36 in groups:
            groups[k // 36].add(n)
    assert {q:len(v) for q,v in groups.items()} == {3:538,12:298,15:229}
    walls = Counter((1 - Fraction(36*q,n))/23 for q in groups for n in groups[q])
    assert len(walls)==953 and Counter(walls.values()) == {1:869,2:56,3:28}
    x = [0]
    for wall in sorted(walls):
        x.append(x[-1]+walls[wall])
    assert (len(x), x[-1]) == (954,1065)
    return x

def graph_and_predecessors(x, r):
    n=len(x)
    u=[bisect_right(x,x[p]+r)-1 for p in range(n)]
    v=[bisect_left(x,x[q]-r) for q in range(n)]
    ell=[None]*n
    pointer=0
    for q in range(1,n):
        while u[pointer]+1 < v[q]:
            pointer += 1
        assert pointer <= q-1
        ell[q]=pointer
    assert all(ell[q] <= ell[q+1] for q in range(1,n-1))
    return u,v,ell

def support_intervals(x,r,k):
    u,v,ell=graph_and_predecessors(x,r)
    a=bisect_left(x,x[-1]-r)
    b=len(x)-1
    spans=[]
    for t in range(1,k+1):
        if a>b or b<0:
            spans.append(None)
            continue
        spans.append((a,b))
        if b>=1:
            a,b=ell[max(a,1)],b-1
        else:
            a,b=1,0
    return spans,(u,v,ell)

def exact_support(x,r,k,u,v):
    prev={p for p in range(len(x)) if x[-1]-x[p] <= r}
    layers=[prev]
    for _ in range(2,k+1):
        prev={p for p in range(len(x)) if any(q in prev and p<q and v[q] <= u[p]+1 for q in range(p+1,len(x)))}
        layers.append(prev)
    return layers

def check_small():
    cases=layers=brute=0
    # All 1,093 event arrays of 0..6 positive increments in {1,2,3}.
    for width in range(7):
        for increments in product((1,2,3),repeat=width):
            x=[0]
            for d in increments:x.append(x[-1]+d)
            n=len(x)
            for r in range(4):
                spans,(u,v,ell)=support_intervals(x,r,n)
                dense=exact_support(x,r,n,u,v)
                suffix_starts=[set() for _ in range(n)]
                # Independent definition: enumerate every t-center suffix and its actual coverage.
                for t in range(1,n+1):
                    for chosen in combinations(range(n),t):
                        p=chosen[0]
                        if all(min(abs(x[b]-x[s]) for s in chosen)<=r for b in range(p,n)):
                            suffix_starts[t-1].add(p)
                        brute+=1
                for t,(s,actual,oracle) in enumerate(zip(spans,dense,suffix_starts),1):
                    predicted=set(range(s[0],s[1]+1)) if s is not None else set()
                    assert predicted==actual==oracle, (x,r,t,s,actual,oracle)
                    if s is not None:assert s[1]==n-t
                    layers+=1
                cases+=1
    return dict(small_instances=cases, layers_checked=layers, explicit_subsets_checked=brute)

def main():
    small=check_small()
    x=frozen_events()
    spans,(u,v,ell)=support_intervals(x,2,213)
    assert all(s is not None for s in spans)
    assert (spans[0],spans[1],spans[-1]) == ((951,953),(946,952),(1,741))
    assert sum(b-a+1 for a,b in spans)==83813
    # Check every 213th-layer state against the actual edge relation, not just a derived length.
    actual=exact_support(x,2,213,u,v)
    assert all(layer == set(range(a,b+1)) for layer,(a,b) in zip(actual,spans))
    assert sum(map(len,actual))==83813
    assert sum(sum(v[q]<=u[p]+1 for q in range(p+1,min(len(x),p+6))) for p in range(len(x)))==4383
    return dict(status='PASS_EXACT_INTERVAL_SUPPORT',frozen_science_pin=PIN,
                theorem='Every suffix-reachable support is a single closed integer-index interval',
                formula='S_t=[ell(max(1,a_(t-1))),b_(t-1)-1]',
                frozen_boundaries=len(x),frozen_events=x[-1],radius=2,centers=213,
                legal_edges=4383,retained_cells=83813,dense_cells=len(x)*213,
                layers_from_first=[list(spans[0]),list(spans[1])],last_layer=list(spans[-1]),
                adjacent_ell_monotone=True,small_exhaustive=small,
                event_array_sha256=sha256(json.dumps(x,separators=(',',':')).encode()).hexdigest())

if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,sort_keys=True,indent=2))
