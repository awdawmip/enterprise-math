#!/usr/bin/env python3
"""R762IL exact 54-event Port kernel certificate, standard-library only.

Frozen model: six axes, 15 pair-Port vertices, 20 three-axis supports.
Depends on the earlier R762IK reduction and its verified even-size high families.
This script exhausts newly required odd cases, active-set exceptions and
the k=1,T=13 structural extremum. All graph checks are exact integers.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product

PORTS = list(combinations(range(6), 2))
SUP = list(combinations(range(6), 3))
P = {p:i for i,p in enumerate(PORTS)}
SID = {s:i for i,s in enumerate(SUP)}
TRI = [tuple(P[x] for x in combinations(s,2)) for s in SUP]
EDGES = [tuple(combinations(v,2)) for v in TRI]
EDGE_OWNER = {tuple(sorted(e)):s for s in range(20) for e in EDGES[s]}
assert len(EDGE_OWNER)==60
PERM = [tuple(SID[tuple(sorted(p[x] for x in s))] for s in SUP)
        for p in permutations(range(6))]

def connected_components(triangle_supports):
    parent = list(range(15))
    def root(i):
        while i != parent[i]:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for s in triangle_supports:
        a,b,c = TRI[s]
        parent[root(a)] = root(b)
        parent[root(a)] = root(c)
    return [root(i) for i in range(15)]

def verify(edges, histogram, expected_active):
    counts=Counter(s for s,a,b in edges)
    if counts!={s:v for s,v in enumerate(histogram) if v}: return False
    degree=[0]*15
    adj=[set() for _ in range(15)]
    for s,a,b in edges:
        if tuple(sorted((a,b))) not in EDGES[s]: return False
        degree[a]+=1
        degree[b]+=1
        adj[a].add(b)
        adj[b].add(a)
    if any(x%2 for x in degree): return False
    active={i for i,x in enumerate(degree) if x}
    if active != expected_active: return False
    seen={next(iter(active))}
    stack=list(seen)
    while stack:
        for v in adj[stack.pop()]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return seen==active

def paths(edge, allowed, omitted):
    a,b=edge
    for w in range(15):
        if w in edge or w==omitted: continue
        ab=tuple(sorted((a,w)))
        bc=tuple(sorted((w,b)))
        if omitted in ab or omitted in bc: continue
        if ab in EDGE_OWNER and bc in EDGE_OWNER:
            x,y=EDGE_OWNER[ab],EDGE_OWNER[bc]
            if x in allowed and y in allowed:
                yield ((x,ab),(y,bc))

def witness(odd=(), even=(), missing=(), target=53, omitted=None):
    active=set(range(15)) if omitted is None else set(range(15))-{omitted}
    present=set(range(20))-set(missing)
    full=present-set(odd)-set(even)
    original=sum(1 if s in odd else 2 if s in even else 3 for s in present)
    shorten=max(0,(original-target+1)//2)
    if shorten<=0: raise ValueError("witness requested for already-small histogram")
    for selected in combinations(sorted(full),shorten):
        allowed=full-set(selected)
        defects=tuple(odd)+selected
        choices=[tuple(e for e in EDGES[s] if omitted is None or omitted not in e)
                 for s in defects]
        for chosen in product(*choices):
            opts=[tuple(paths(e,allowed,omitted)) for e in chosen]
            if any(not op for op in opts): continue
            for adopted in product(*opts):
                changed=defaultdict(int)
                for route in adopted:
                    for s,(a,b) in route:
                        changed[s]^=(1<<a)^(1<<b)
                edges=[]
                for s in allowed:
                    if changed[s]==0:
                        edges.extend((s,*e) for e in EDGES[s])
                    else:
                        edge=next((e for e in EDGES[s]
                                   if ((1<<e[0])^(1<<e[1]))==changed[s]),None)
                        if edge is None: break
                        doubled=next(e for e in EDGES[s] if e!=edge)
                        edges.extend([(s,*edge),(s,*doubled),(s,*doubled)])
                else:
                    for s in even:
                        e=next(e for e in EDGES[s]
                               if omitted is None or omitted not in e)
                        edges.extend([(s,*e),(s,*e)])
                    edges.extend((s,*e) for s,e in zip(defects,chosen))
                    histogram=[1 if s in defects else 2 if s in even
                               else 3 if s in allowed else 0 for s in range(20)]
                    if verify(edges,histogram,active):
                        return len(edges), selected
    return None

def representatives(cases):
    unseen=set(tuple(tuple(group) for group in entry) for entry in cases)
    result=[]
    while unseen:
        item=min(unseen)
        orbit={tuple(tuple(sorted(p[s] for s in group)) for group in item)
               for p in PERM}
        assert orbit<=unseen
        unseen.difference_update(orbit)
        result.append((item,len(orbit)))
    return result

def main():
    # k=0, original 55: deficits 5 relative to all 20 supports having 3 events.
    families55=[
        ("E5",[((),e,()) for e in combinations(range(20),5)]),
        ("U1E3",[((u,),e,()) for u in range(20)
                   for e in combinations([j for j in range(20) if j!=u],3)]),
        ("U2E1",[(u,(e,),()) for u in combinations(range(20),2)
                   for e in range(20) if e not in u]),
        ("M1E2",[((),e,(m,)) for m in range(20)
                   for e in combinations([j for j in range(20) if j!=m],2)]),
        ("M1U1",[((u,),(),(m,)) for m in range(20)
                   for u in range(20) if u!=m])]
    counts={}
    for name,cases in families55:
        reps=representatives(cases)
        for rep,multiplicity in reps:
            result=witness(*rep,target=53)
            assert result and result[0]==53,(name,rep)
        assert sum(mult for _,mult in reps)==len(cases)
        counts[name]={"histograms":len(cases),"orbits":len(reps)}
    assert sum(x["histograms"] for x in counts.values())==42104
    assert sum(x["orbits"] for x in counts.values())==118

    # k=0, original >55 and odd: previously 55-event cases improve to 53.
    higher=[
        ("E1",[((),(e,),()) for e in range(20)]),
        ("E3",[((),e,()) for e in combinations(range(20),3)]),
        ("U1E1",[((u,),(e,),()) for u in range(20)
                   for e in range(20) if e!=u]),
        ("M1",[((),(),(m,)) for m in range(20)])]
    high_counts={}
    for name,cases in higher:
        reps=representatives(cases)
        for rep,multiplicity in reps:
            result=witness(*rep,target=53)
            assert result and result[0]==53,(name,rep)
        assert sum(n for _,n in reps)==len(cases)
        high_counts[name]={"histograms":len(cases),"orbits":len(reps)}
    assert sum(x["histograms"] for x in high_counts.values())==1560
    assert sum(x["orbits"] for x in high_counts.values())==12

    # Inactive Port: all four incident supports must be non-full.
    special=0
    for port in PORTS:
        v=P[port]
        incident={s for s,trip in enumerate(SUP) if set(port)<=set(trip)}
        assert len(incident)==4
        for extra in set(range(20))-incident:
            assert witness(even=tuple(sorted(incident|{extra})),
                           target=53,omitted=v)[0]==53
            special+=1
        for u in incident:
            assert witness(odd=(u,),even=tuple(sorted(incident-{u})),
                           target=53,omitted=v)[0]==53
            special+=1
    assert special==300

    # k=1,T=13: exact 3-component triangle-support extrema.
    candidates=0
    shapes=Counter()
    for thirteen in combinations(range(20),13):
        roots=connected_components(thirteen)
        if len(set(roots))!=3: continue
        shapes[tuple(sorted(Counter(roots).values()))]+=1
        members=set(thirteen)
        omitted=[s for s in range(20) if s not in members]
        for critical in omitted:
            a,b,c=TRI[critical]
            if len({roots[a],roots[b],roots[c]})!=3: continue
            lone=[v for v in range(15)
                  if sum(x==roots[v] for x in roots)==1]
            assert len(lone)==2
            assert set(lone).issubset(set(TRI[critical]))
            remaining=[s for s in omitted if s!=critical]
            # Fully triangular 13 odd supports, seven doubled supports;
            # attach each isolated Port through a distinct noncritical type.
            connections={}
            for v in lone:
                s=next(s for s in remaining if v in TRI[s])
                e=next(e for e in EDGES[s] if v in e
                       and next(w for w in e if w!=v) not in lone)
                connections[s]=e
            assert len(connections)==2
            graph=[(s,*e) for s in thirteen for e in EDGES[s]]
            for s in omitted:
                e=connections.get(s,EDGES[s][0])
                graph.extend([(s,*e),(s,*e)])
            hist=[3 if s in members else 2 for s in range(20)]
            assert sum(hist)==53
            assert verify(graph,hist,set(range(15)))
            candidates+=1
    assert shapes=={(1,1,13):60},shapes
    assert candidates==60,candidates
    print("PASS R762IL: 54-event universal upper bound, assuming R762IK "
          "terminal reductions and even-case certificates")
    print("k0 original=55:",counts,"total=42104 histograms / 118 orbits")
    print("k0 original=57/59 odd:",high_counts,"1560 histograms / 12 orbits")
    print("14-Port exceptional cases:",special)
    print("k1 T13:",sum(shapes.values()),"three-component 13-subsets,",
          candidates,"critical cases / 77520 total 13-subsets")

if __name__=="__main__":
    main()
