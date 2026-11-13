#!/usr/bin/env python3
"""Blockwise exact suffix-rank reconstruction, frozen R5 rational-wall class.
Original pin 435e77af0d180eac32bd1f9c4c464bc4010b7551. Python stdlib only.
The original 28-coordinate legal-path census is prior scientific evidence.
"""
from fractions import Fraction
from collections import Counter
from bisect import bisect_left,bisect_right
from hashlib import sha256
from time import perf_counter
import tracemalloc,json
W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
V=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
OLD='d500a95a516544511a50596555556a5a441665a66a9195956669611456565551aa5669aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6a00'
EXPECTED_T=959842890872466279854034583824629760000
EXPECTED_RANK=291259906744233319113441752826891487978

def construct():
    pairs={3:set(),12:set(),15:set()}
    for mask in range(1,1<<15):
        n=-sum(W[i] for i in range(15) if mask>>i&1)
        weight=-sum(V[i] for i in range(15) if mask>>i&1)
        if n>=3 and weight%36==0 and weight//36 in pairs:
            pairs[weight//36].add(n)
    assert {q:len(v) for q,v in pairs.items()}=={3:538,12:298,15:229}
    histogram=Counter((1-Fraction(36*q,n))/23 for q,ns in pairs.items() for n in ns)
    assert len(histogram)==953 and Counter(histogram.values())==Counter({1:869,2:56,3:28})
    E=[0]
    for tau in sorted(histogram):E.append(E[-1]+histogram[tau])
    assert len(E)==954 and E[-1]==1065
    raw=bytes.fromhex(OLD)
    assert len(raw)==56 and sha256(raw).hexdigest()=='bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326'
    stream=int.from_bytes(raw[2:],'little')
    centers=[stream&3];stream>>=2
    for _ in range(212):
        digit=stream&3;stream>>=2
        assert digit<=2
        centers.append(centers[-1]+3+digit)
    assert stream==0 and len(centers)==213 and centers[-1]==952
    starts=[p for p,x in enumerate(E) if x-E[0]<=2]
    ends={p for p,x in enumerate(E) if E[-1]-x<=2}
    upper=[bisect_right(E,E[p]+2)-1 for p in range(len(E))]
    lower=[bisect_left(E,E[p]-2) for p in range(len(E))]
    edges=[[q for q in range(p+1,min(len(E),p+6)) if lower[q]<=upper[p]+1] for p in range(len(E))]
    assert starts==[0,1,2] and ends=={951,952,953} and sum(map(len,edges))==4383
    return E,centers,starts,ends,edges


# New exact minimum-mean-cost path count, on the original frozen event walls.
# The coefficient/56B-seed fixture above is re-used byte-for-byte from PR #2267.
from itertools import product, combinations

R = 2
K_CENTERS = 213
INF = 10**18

def exact_graph(x, radius):
    n = len(x)
    starts = [p for p in range(n) if x[p]-x[0] <= radius]
    ends = {p for p in range(n) if x[-1]-x[p] <= radius}
    upper = [bisect_right(x, x[p]+radius)-1 for p in range(n)]
    lower = [bisect_left(x, x[p]-radius) for p in range(n)]
    adj = [[] for _ in x]
    weight = [{} for _ in x]
    for p in range(n):
        for q in range(p+1, min(n, p+2*radius+2)):
            if lower[q] <= upper[p]+1:
                adj[p].append(q)
                # b=q is included and contributes 0; internal centers counted once.
                weight[p][q] = sum(min(x[b]-x[p], x[q]-x[b])
                                    for b in range(p+1,q+1))
    first = {p:sum(x[p]-x[b] for b in range(p)) for p in starts}
    last = {p:sum(x[b]-x[p] for b in range(p+1,n)) for p in ends}
    return starts, ends, adj, weight, first, last

def suffix_optimal(graph, K):
    starts, ends, adj, weight, first, last = graph
    n = len(adj)
    cost = [None, [last[p] if p in ends else INF for p in range(n)]]
    count = [None, [int(p in ends) for p in range(n)]]
    for t in range(2,K+1):
        c = [INF]*n
        v = [0]*n
        for p in range(n):
            for q in adj[p]:
                if not count[t-1][q]: continue
                z = weight[p][q]+cost[t-1][q]
                if z < c[p]:
                    c[p],v[p] = z,count[t-1][q]
                elif z == c[p]:
                    v[p] += count[t-1][q]
        cost.append(c)
        count.append(v)
    best = min(first[p]+cost[K][p] for p in starts)
    total = sum(count[K][p] for p in starts if first[p]+cost[K][p] == best)
    return best, total, cost, count

def forward_check(graph, K):
    starts, ends, adj, weight, first, last = graph
    n = len(adj)
    c = [INF]*n
    v = [0]*n
    for p in starts: c[p],v[p] = first[p],1
    for _ in range(2,K+1):
        nc = [INF]*n
        nv = [0]*n
        for p in range(n):
            if v[p] == 0: continue
            for q in adj[p]:
                z = c[p]+weight[p][q]
                if z < nc[q]:
                    nc[q],nv[q] = z,v[p]
                elif z == nc[q]:
                    nv[q] += v[p]
        c,v = nc,nv
    best = min(c[p]+last[p] for p in ends)
    total = sum(v[p] for p in ends if c[p]+last[p] == best)
    return best,total

def rank_optimal(centers, graph, K, best, cost, count):
    starts, ends, adj, weight, first, last = graph
    if first[centers[0]]+cost[K][centers[0]] != best:
        raise ValueError("nonoptimal first center")
    rank = sum(count[K][p] for p in starts
               if p<centers[0] and first[p]+cost[K][p] == best)
    for j,(p,q) in enumerate(zip(centers, centers[1:])):
        t = K-j
        if q not in adj[p] or weight[p][q]+cost[t-1][q] != cost[t][p]:
            raise ValueError("nonoptimal edge")
        rank += sum(count[t-1][v] for v in adj[p] if v<q
                    and weight[p][v]+cost[t-1][v] == cost[t][p])
    if centers[-1] not in ends: raise ValueError("nonterminal center")
    return rank

def unrank_optimal(rank, graph, K, best, total, cost, count):
    if not 0 <= rank < total: raise ValueError("rank out of range")
    starts,ends,adj,weight,first,last = graph
    centers=[]
    for p in starts:
        if first[p]+cost[K][p] != best: continue
        b=count[K][p]
        if rank<b:
            centers.append(p)
            break
        rank-=b
    for t in range(K-1,0,-1):
        p=centers[-1]
        for q in adj[p]:
            if weight[p][q]+cost[t][q] != cost[t+1][p]: continue
            b=count[t][q]
            if rank<b:
                centers.append(q)
                break
            rank-=b
        else:
            raise AssertionError("missing optimal successor")
    assert rank==0 and centers[-1] in ends
    return centers

def small_exhaustive():
    cases=valid_sequences=optimal_sequences=0
    for length in range(1,7):
        for increments in product((1,2,3),repeat=length):
            x=[0]
            for z in increments:x.append(x[-1]+z)
            for radius in range(4):
                graph=exact_graph(x,radius)
                for k in range(1,length+2):
                    best,total,cost,count=suffix_optimal(graph,k)
                    assert forward_check(graph,k)==(best,total)
                    legal=[]
                    for s in combinations(range(length+1),k):
                        errors=[min(abs(x[b]-x[p]) for p in s)
                                for b in range(length+1)]
                        if max(errors)<=radius:legal.append((s,sum(errors)))
                    cases+=1
                    valid_sequences+=len(legal)
                    if not legal:
                        assert total==0
                        continue
                    minimum=min(price for _,price in legal)
                    opts=[s for s,price in legal if price==minimum]
                    optimal_sequences+=len(opts)
                    assert (best,total)==(minimum,len(opts))
                    for idx,s in enumerate(opts):
                        assert rank_optimal(s,graph,k,best,cost,count)==idx
                        assert tuple(unrank_optimal(idx,graph,k,best,total,cost,count))==s
    return {"scenarios":cases,"legal_sets_checked":valid_sequences,
            "optimal_rank_unrank_checks":optimal_sequences}

def main():
    began=perf_counter()
    x,centers,_,_,_=construct()
    assert len(x)==954 and x[-1]==1065 and len(centers)==K_CENTERS
    graph=exact_graph(x,R)
    assert sum(map(len,graph[2]))==4383
    best,total,cost,count=suffix_optimal(graph,K_CENTERS)
    assert (best,total)==(1070,1338767625695954932334592000)
    assert forward_check(graph,K_CENTERS)==(best,total)
    original=sum(min(abs(x[b]-x[p]) for p in centers) for b in range(len(x)))
    assert original==best
    idx=rank_optimal(centers,graph,K_CENTERS,best,cost,count)
    assert idx==417027933051277583800994379
    assert unrank_optimal(idx,graph,K_CENTERS,best,total,cost,count)==centers
    assert len(idx.to_bytes(12,"big"))==12
    payload=idx.to_bytes(12,"big")
    assert payload.hex()=="0158f5198cd12c63a2ba0a4b"
    assert sha256(payload).hexdigest()=="da48ae93cb1e69687bb54f4ffa8bdc16683a3539d7df7ce8591a4bf1a892e87e"
    try: unrank_optimal(total,graph,K_CENTERS,best,total,cost,count)
    except ValueError: pass
    else: raise AssertionError("invalid optimal rank accepted")
    basic_seconds=perf_counter()-began
    tests=small_exhaustive()
    assert tests=={"scenarios":28428,"legal_sets_checked":104562,
                   "optimal_rank_unrank_checks":49627}
    result={
        "status":"AUTHOR_PASS_EXACT_PINNED_R5_MINCOST_COVER_RANK",
        "frozen_scientific_pin":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
        "predecessor_pr":2267,"boundaries":len(x),"events":x[-1],
        "radius":R,"centers":K_CENTERS,"graph_edges":4383,
        "historical_mean_correction":original,
        "minimum_mean_correction":best,
        "number_of_mean_optimal_radius_cover_sets":str(total),
        "capacity_bits":(total-1).bit_length(),
        "capacity_bytes":((total-1).bit_length()+7)//8,
        "original_center_rank":str(idx),
        "original_center_payload_hex":payload.hex(),
        "original_center_payload_sha256":sha256(payload).hexdigest(),
        "forward_backward_min_cost_and_count_agree":True,
        "rank_roundtrip_identical":True,"out_of_range_rank_rejected":True,
        "small_exhaustive":tests,
        "local_fixture_and_dp_seconds":round(basic_seconds,6),
        "scope":"Exact R5 radius-2 and minimum-mean 1070 center class; all costs integers; original 28D legal word census reused, not re-executed; independent formal review pending"
    }
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__=="__main__":
    main()
