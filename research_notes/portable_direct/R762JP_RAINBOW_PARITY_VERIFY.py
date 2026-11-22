#!/usr/bin/env python3
"""Exact standard-library check for R762JP full-Port rainbow parity theorem.
Runs all 1140 three-color exclusions and 3420 associated 44-to-42 integer witnesses.
Heuristic tree search is supplemental; the paper proves tree existence mathematically.
"""
import itertools, random, hashlib, json

AXES=range(6)
PORTS=list(itertools.combinations(AXES,2))
SUPPORTS=list(itertools.combinations(AXES,3))
PID={p:i for i,p in enumerate(PORTS)}
TRI=[tuple(PID[p] for p in itertools.combinations(s,2)) for s in SUPPORTS]
EDGES=[tuple(itertools.combinations(t,2)) for t in TRI]

def tree(excluded):
    labels=[s for s in range(20) if s not in excluded]
    for attempt in range(32):
        rng=random.Random(10213+attempt)
        order=labels[:]
        rng.shuffle(order)
        parent=list(range(15)); rank=[0]*15
        def find(v):
            while parent[v]!=v:
                parent[v]=parent[parent[v]]
                v=parent[v]
            return v
        chosen={}
        for s in order:
            edges=list(EDGES[s]); rng.shuffle(edges)
            for u,v in edges:
                a,b=find(u),find(v)
                if a!=b:
                    if rank[a]<rank[b]:a,b=b,a
                    parent[b]=a
                    if rank[a]==rank[b]:rank[a]+=1
                    chosen[s]=(u,v)
                    break
        if len(chosen)==14:
            return chosen,attempt
    raise AssertionError(('unconstructed_tree',excluded))

def witness(counts, singles, R):
    assert len(R)==14 and set(singles)=={s for s,c in enumerate(counts) if c==1}
    x=[[0]*3 for _ in range(20)]
    b={v:0 for v in range(15)}
    for s in singles:
        x[s][0]=1
        u,v=EDGES[s][0]
        b[u]^=1;b[v]^=1
    adj={v:[] for v in range(15)}
    for s,(u,v) in R.items():
        adj[u].append((v,s));adj[v].append((u,s))
    parent={0:-1};pedge={};order=[0]
    for u in order:
        for v,s in adj[u]:
            if v not in parent:
                parent[v]=u;pedge[v]=s;order.append(v)
    assert len(order)==15
    selected=set()
    for v in reversed(order[1:]):
        if b[v]:
            selected.add(pedge[v]);b[parent[v]]^=1
    assert b[0]==0
    for s in range(20):
        if counts[s]==1:continue
        k=EDGES[s].index(R[s]) if s in R else 0
        if s in selected:
            if counts[s]==2:
                for a in range(3):
                    if a!=k:x[s][a]=1
            else:x[s][k]=3
        else:
            if counts[s]==2:x[s][k]=2
            else:x[s]=[1,1,1]
    return x

def check(counts, singles, R, x):
    assert len(x)==20 and len(R)==14
    assert set(singles).isdisjoint(R)
    degrees=[0]*15;adj=[set() for _ in range(15)]
    for s in range(20):
        assert len(x[s])==3 and all(type(v)==int and 0<=v<=3 for v in x[s])
        assert sum(x[s])==counts[s]
        for (u,v),n in zip(EDGES[s],x[s]):
            degrees[u]+=n;degrees[v]+=n
            if n:adj[u].add(v);adj[v].add(u)
    assert sum(map(sum,x))==42
    assert all(d>0 and d%2==0 for d in degrees)
    seen={0};queue=[0]
    for u in queue:
        for v in adj[u]:
            if v not in seen:seen.add(v);queue.append(v)
    assert len(seen)==15
    for s,(u,v) in R.items():
        local={p:set() for p in TRI[s]}
        for (a,b),n in zip(EDGES[s],x[s]):
            if n:local[a].add(b);local[b].add(a)
        seen={u};queue=[u]
        for a in queue:
            for b in local[a]:
                if b not in seen:seen.add(b);queue.append(b)
        assert v in seen
    return min(degrees)

def cuts():
    neighbors=[set() for _ in range(15)]
    for edges in EDGES:
        for u,v in edges:neighbors[u].add(v);neighbors[v].add(u)
    assert all(len(n)==8 for n in neighbors)
    small=999; singleton=0
    for mask in range(1,(1<<15)-1):
        X={u for u in range(15) if mask>>u&1}
        crossing=sum(len(neighbors[u]-X) for u in X)
        if len(X) in (1,14):
            assert crossing==8;singleton+=1
        else:
            assert crossing>8
            small=min(small,crossing)
    return {'checked':32766,'singletons_and_complements':singleton,
            'minimum_other_cut':small}

def main():
    cut_info=cuts()
    total=0;max_attempt=0;hist={};lowest_degree=1000
    stream=hashlib.sha256()
    for excluded in itertools.combinations(range(20),3):
        R,attempt=tree(excluded)
        max_attempt=max(max_attempt,attempt)
        hist[attempt]=hist.get(attempt,0)+1
        for j in excluded:
            singles=tuple(s for s in excluded if s!=j)
            triple={j}|set([s for s in range(20) if s not in excluded][:5])
            n=[3 if s in triple else 1 if s in singles else 2 for s in range(20)]
            assert sum(n)==44
            counts=n[:];counts[j]-=2
            x=witness(counts,excluded,R)
            lowest_degree=min(lowest_degree,check(counts,excluded,R,x))
            stream.update(bytes(excluded));stream.update(bytes([j]))
            stream.update(bytes(v for row in x for v in row))
            total+=1
    print(json.dumps({
        'result':'PASS','three_color_exclusions':1140,
        'rainbow_spanning_trees_verified':1140,
        '44_to_42_integer_witnesses':total,
        'greedy_attempt_histogram':hist,'maximum_attempt':max_attempt,
        'minimum_degree':lowest_degree,'cut_info':cut_info,
        'witness_stream_sha256':stream.hexdigest(),
        'scope':'all_15_ports_active; author_proved; not_independently_reviewed'
    },indent=2,sort_keys=True))
if __name__=='__main__': main()
