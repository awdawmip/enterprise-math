#!/usr/bin/env python3
"""R284AV: exact distance-graded sparse spanning-tree Port probe schedule.
Requires the R284AU_scalar_port_checker.py companion in the same directory.
"""
import json
from collections import deque
from itertools import combinations
from random import Random
from math import comb
from R284AU_scalar_port_checker import leading_minor_oracle


def reconstruct_distance_graded(A, oriented_edges):
    n=len(A)
    M=max(map(max,A))
    adj=[[] for _ in range(n)]
    orientation={}
    for u,v in oriented_edges:
        adj[u].append(v);adj[v].append(u)
        orientation[frozenset((u,v))]=(u,v)
    assert len(oriented_edges)==n-1
    calls=0;cache={};witnesses=[]
    def query(T, edge=None):
        nonlocal calls
        key=(tuple(sorted(T)),edge)
        if key not in cache:
            co,_,_=leading_minor_oracle(A,T,edge)
            cache[key]=co;calls+=1
        return cache[key]
    alpha=[-query((i,)) for i in range(n)]
    pair={}
    for i,j in combinations(range(n),2):
        pair[i,j]=alpha[i]*alpha[j]-query((i,j))
    prod=lambda i,j:pair[tuple(sorted((i,j)))]
    known=[[None]*n for _ in range(n)]
    for i in range(n):known[i][i]=alpha[i]
    for u,v in oriented_edges:
        reverse=query((u,v))-query((u,v),(u,v))
        assert reverse>0 and prod(u,v)%reverse==0
        known[v][u]=reverse
        known[u][v]=prod(u,v)//reverse
    # Find each unordered pair's tree path and process by ascending distance.
    missing=[]
    for x,y in combinations(range(n),2):
        parent={x:None};queue=deque((x,))
        while y not in parent:
            a=queue.popleft()
            for b in adj[a]:
                if b not in parent:
                    parent[b]=a;queue.append(b)
        path=[y]
        while path[-1]!=x:path.append(parent[path[-1]])
        path.reverse()
        if len(path)>2:missing.append((len(path)-1,x,y,path))
    missing.sort()
    for distance,x,y,path in missing:
        a=path[-2]
        assert known[x][a] is not None and known[a][x] is not None
        u,v=orientation[frozenset((a,y))]
        reverse=known[v][u]
        diff=query((x,u,v),(u,v))-query((x,u,v))
        q=reverse*alpha[x]-diff
        if (u,v)==(a,y):
            assert known[x][a]>0 and q%known[x][a]==0
            known[y][x]=q//known[x][a]
            assert known[y][x]>0 and prod(x,y)%known[y][x]==0
            known[x][y]=prod(x,y)//known[y][x]
        else:
            assert (u,v)==(y,a)
            assert known[a][x]>0 and q%known[a][x]==0
            known[x][y]=q//known[a][x]
            assert known[x][y]>0 and prod(x,y)%known[x][y]==0
            known[y][x]=prod(x,y)//known[x][y]
        witnesses.append((x,y,distance,u,v,a,q))
    assert known==A
    count_expected=3*comb(n,2)+1
    assert calls<=count_expected
    return {"n":n,"query_count":calls,"universal_bound":count_expected,
            "non_tree_pairs":len(missing),"tree_edges":len(oriented_edges),
            "max_distance":max([x[0] for x in missing],default=1),
            "cofactor_witnesses":len(witnesses)}


def run(seed=28420261120):
    rng=Random(seed)
    counts={2:40,3:40,4:45,5:45,6:30,7:22,8:12}
    runs=[]
    for n,count in counts.items():
        for _ in range(count):
            A=[[rng.randrange(1,9) for j in range(n)] for i in range(n)]
            edges=[]
            for y in range(1,n):
                x=rng.randrange(y)
                edges.append((y,x) if rng.randrange(2) else (x,y))
            runs.append(reconstruct_distance_graded(A,edges))
    boundary=[]
    for n in [3,4,6,8]:
        A=[[1 for j in range(n)] for i in range(n)]
        path=[(i,i+1) if i%2 else (i+1,i) for i in range(n-1)]
        star=[(0,i) if i%2 else (i,0) for i in range(1,n)]
        boundary.extend((reconstruct_distance_graded(A,path),reconstruct_distance_graded(A,star)))
    return {"theorem_id":"R284AV", "status":"PASS", "seed":seed,
            "random_cases":len(runs),"dimension_counts":{str(k):v for k,v in counts.items()},
            "boundary_cases":len(boundary),"total_cases":len(runs)+len(boundary),
            "total_calls":sum(x['query_count'] for x in runs+boundary),
            "tree_edges_checked":sum(x['tree_edges'] for x in runs+boundary),
            "non_tree_pair_witnesses_checked":sum(x['non_tree_pairs'] for x in runs+boundary),
            "max_calls":max(x['query_count'] for x in runs+boundary),
            "max_universal_bound":max(x['universal_bound'] for x in runs+boundary),
            "max_tree_distance":max(x['max_distance'] for x in runs+boundary),
            "sample_bound_vs_actual":[{k:x[k] for k in ('n','query_count','universal_bound','non_tree_pairs','max_distance')} for x in boundary],
            "arithmetic":"exact integer Bareiss, one-scale balanced extraction, exact named cofactor products, integer divisibility checks",
            "verification_scope":"random strictly positive integer matrices n=2..8, independent rooted distance-graded non-tree pair schedule, mixed tree orientations, all-ones path/star boundary tests",
            "general_theorem_status":"AUTHOR_PROVED_NOT_INDEPENDENTLY_REVIEWED"}


if __name__=='__main__':
    print(json.dumps(run(),indent=2,ensure_ascii=False))
