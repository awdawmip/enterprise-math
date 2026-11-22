#!/usr/bin/env python3
"""Exact one-inactive-Port rainbow parity classification (R762JQ).
Enumerates all C(20,3) exclusions, computes 14-Port rainbow trees by
matroid-intersection augmenting paths, and validates 3300 Euler witnesses.
Forty cases are failures only of this sufficient rainbow-tree criterion.
"""
import itertools, json, hashlib
A=range(6)
PORTS=list(itertools.combinations(A,2))
SUPPORTS=list(itertools.combinations(A,3))
PID={p:i for i,p in enumerate(PORTS)}
TRIS=[tuple(PID[t] for t in itertools.combinations(s,2)) for s in SUPPORTS]
EDGES=[tuple(itertools.combinations(t,2)) for t in TRIS]
INACTIVE=PID[(0,1)]
V=set(range(15))-{INACTIVE}
FULL={s for s,t in enumerate(TRIS) if INACTIVE not in t}
AWING={s for s in FULL if 0 in SUPPORTS[s]}
BWING={s for s in FULL if 1 in SUPPORTS[s]}
assert len(FULL)==16 and len(AWING)==len(BWING)==6

def rainbow(labels):
    candidates=[(s,u,v) for s in sorted(labels) for u,v in EDGES[s]
                if u in V and v in V]
    chosen=set()
    def components(J):
        p={v:v for v in V}
        def find(v):
            while p[v]!=v:
                p[v]=p[p[v]];v=p[v]
            return v
        for k in J:
            _,u,v=candidates[k]
            x,y=find(u),find(v)
            assert x!=y
            p[x]=y
        return {v:find(v) for v in V}
    while len(chosen)<len(V)-1:
        cc=components(chosen)
        used={candidates[k][0]:k for k in chosen}
        outside=[k for k in range(len(candidates)) if k not in chosen]
        sources=[k for k in outside
                 if cc[candidates[k][1]]!=cc[candidates[k][2]]]
        sinks={k for k in outside if candidates[k][0] not in used}
        pred={k:None for k in sources}
        queue=sources[:]
        goal=None
        for k in queue:
            if k in sinks:goal=k;break
            if k not in chosen:
                c=candidates[k][0]
                if c in used:
                    nxt=used[c]
                    if nxt not in pred:pred[nxt]=k;queue.append(nxt)
            else:
                cc0=components(chosen-{k})
                for nxt in outside:
                    if nxt not in pred and cc0[candidates[nxt][1]]!=cc0[candidates[nxt][2]]:
                        pred[nxt]=k;queue.append(nxt)
        if goal is None:break
        path=[]
        while goal is not None:
            path.append(goal)
            goal=pred[goal]
        for k in path:
            if k in chosen:chosen.remove(k)
            else:chosen.add(k)
        assert len(set(candidates[k][0] for k in chosen))==len(chosen)
        assert len(set(components(chosen).values()))==len(V)-len(chosen)
    return {candidates[k][0]:(candidates[k][1],candidates[k][2])
            for k in chosen}

def witness(D,j,R):
    singles=set(D)
    extras=[s for s in range(20) if s not in singles][:5]
    triples=set(extras)|{j}
    counts=[3 if s in triples else 1 if s in singles-{j} else 2
            for s in range(20)]
    assert sum(counts)==44
    counts[j]-=2
    out=[[0]*3 for _ in range(20)]
    parity={v:0 for v in V}
    for s in range(20):
        if counts[s]==1 or s not in FULL:
            k=next(k for k,(u,v) in enumerate(EDGES[s]) if u in V and v in V)
            out[s][k]=counts[s]
            u,v=EDGES[s][k]
            parity[u]^=counts[s]%2
            parity[v]^=counts[s]%2
    tree={v:[] for v in V}
    for s,(u,v) in R.items():
        tree[u].append((v,s))
        tree[v].append((u,s))
    root=min(V)
    parents={root:None};edge_color={}
    order=[root]
    for u in order:
        for v,s in tree[u]:
            if v not in parents:
                parents[v]=u
                edge_color[v]=s
                order.append(v)
    assert len(order)==14
    active=set()
    for v in reversed(order[1:]):
        if parity[v]:
            active.add(edge_color[v])
            parity[parents[v]]^=1
    assert parity[root]==0
    for s in FULL:
        if counts[s]==1:continue
        k=EDGES[s].index(R[s]) if s in R else 0
        if s in active:
            if counts[s]==2:
                for h in range(3):
                    if h!=k:out[s][h]=1
            else:out[s][k]=3
        else:
            if counts[s]==2:out[s][k]=2
            else:out[s]=[1,1,1]
    deg=[0]*15;adj=[set() for _ in range(15)]
    for s in range(20):
        assert len(out[s])==3 and sum(out[s])==counts[s]
        for (u,v),n in zip(EDGES[s],out[s]):
            assert isinstance(n,int) and 0<=n<=3
            deg[u]+=n;deg[v]+=n
            if n:adj[u].add(v);adj[v].add(u)
    assert sum(map(sum,out))==42
    assert deg[INACTIVE]==0
    assert all(deg[v]>0 and deg[v]%2==0 for v in V)
    seen={root};queue=[root]
    for u in queue:
        for v in adj[u]:
            if v not in seen:seen.add(v);queue.append(v)
    assert seen==V
    return bytes(n for row in out for n in row)

def main():
    positive=0;excluded=[];instances=0
    digest=hashlib.sha256()
    for D in itertools.combinations(range(20),3):
        R=rainbow(FULL-set(D))
        if len(R)!=13:
            excluded.append(D)
            continue
        positive+=1
        for j in D:
            digest.update(bytes(D));digest.update(bytes([j]))
            digest.update(witness(D,j,R))
            instances+=1
    exceptional=set(itertools.combinations(sorted(AWING),3)) | set(
        itertools.combinations(sorted(BWING),3))
    assert set(excluded)==exceptional
    assert positive==1100 and len(excluded)==40 and instances==3300
    print(json.dumps({
       'status':'PASS','inactive_port':PORTS[INACTIVE],
       'full_triangle_colors':len(FULL),
       'all_three_color_exclusions':1140,
       'positive_rainbow_tree_patterns':positive,
       'exceptional_rainbow_tree_patterns':len(excluded),
       'exceptional_form':'three labels in same six-color wing',
       'exact_42_event_witnesses':instances,
       'witness_stream_sha256':digest.hexdigest(),
       'scope':'one inactive Port, 1100/1140 positive sufficient patterns'
    },indent=2))
if __name__=='__main__':main()
