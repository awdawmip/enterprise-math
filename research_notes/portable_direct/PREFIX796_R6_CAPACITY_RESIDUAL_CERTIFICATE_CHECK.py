#!/usr/bin/env python3
"""Exact finite checks for PREFIX-796 capacity-sensitive residual graph theorem.
Only Python standard library. No randomness and no floating-point operations.
"""
from itertools import product
import json

def directed_arcs(b,c,K,x,excluded=None):
    adj=[[] for _ in range(b+c)]
    for e,(k,a) in enumerate(zip(K,x)):
        if e==excluded: continue
        r=e//c; co=b+e%c
        if a<k: adj[r].append((co,k-a))
        if a>0: adj[co].append((r,a))
    return adj

def nontrivial_cycle(b,c,K,x):
    # Enumerate simple directed cycles with >=4 distinct nodes; ignore 2-arc backtracks.
    adj=directed_arcs(b,c,K,x)
    for start in range(b+c):
        todo=[(start,(start,))]
        while todo:
            u,path=todo.pop()
            for v,cap in adj[u]:
                if v==start and len(path)>=4: return True
                if v not in path and len(path)<b+c:
                    todo.append((v,path+(v,)))
    return False

def maxflow(adj,source,sink):
    n=len(adj); r=[[0]*n for _ in range(n)]
    for u in range(n):
        for v,cap in adj[u]: r[u][v]+=cap
    total=0
    while True:
        parent=[-1]*n; parent[source]=source; queue=[source]
        for u in queue:
            if parent[sink]>=0: break
            for v,cap in enumerate(r[u]):
                if cap>0 and parent[v]<0:
                    parent[v]=u; queue.append(v)
        if parent[sink]<0: return total
        d=10**12; v=sink
        while v!=source:
            u=parent[v]; d=min(d,r[u][v]); v=u
        v=sink
        while v!=source:
            u=parent[v]; r[u][v]-=d; r[v][u]+=d; v=u
        total+=d

def bounds(b,c,K,x,e):
    row=e//c; col=b+e%c
    adj=directed_arcs(b,c,K,x,excluded=e)
    upward=min(K[e]-x[e],maxflow(adj,col,row))
    downward=min(x[e],maxflow(adj,row,col))
    return x[e]-downward,x[e]+upward

def margins(b,c,x):
    return (tuple(sum(x[i*c+j] for j in range(c)) for i in range(b)),
            tuple(sum(x[i*c+j] for i in range(b)) for j in range(c)))

def run(b,c):
    options=[(k,a) for k in range(3) for a in range(k+1)]
    cases=0; assertions=0; ambiguity=0; direction_checks=0
    for choices in product(options,repeat=b*c):
        K=tuple(t[0] for t in choices); x=tuple(t[1] for t in choices)
        target=margins(b,c,x)
        fiber=[y for y in product(*(range(k+1) for k in K)) if margins(b,c,y)==target]
        has_other=len(fiber)>1
        pred=nontrivial_cycle(b,c,K,x)
        assert pred==has_other,('cycle',b,c,K,x,fiber)
        assertions+=1; ambiguity+=int(has_other)
        for e in range(b*c):
            actual=(min(y[e] for y in fiber),max(y[e] for y in fiber))
            computed=bounds(b,c,K,x,e)
            assert actual==computed,('bounds',b,c,K,x,e,actual,computed)
            assertions+=1; direction_checks+=1
            values={y[e] for y in fiber}
            assert values==set(range(actual[0],actual[1]+1)),('interval',b,c,K,x,e,values)
            assertions+=1
        cases+=1
    return {'grid':[b,c],'cases':cases,'assertions':assertions,
            'ambiguous_cases':ambiguity,'coordinate_bounds_checked':direction_checks}

def main():
    results=[run(2,2),run(2,3)]
    K=(2,)*4; x=(1,)*4
    assert nontrivial_cycle(2,2,K,x)
    assert bounds(2,2,K,x,0)==(0,2)
    assert not nontrivial_cycle(2,2,(0,)*4,(0,)*4)
    assert not nontrivial_cycle(2,2,(1,)*4,(0,)*4)
    result={'name':'PREFIX796_CAPACITY_RESIDUAL_DIRECTED_CYCLE',
            'arithmetic':'exact Python integers',
            'domain':'all 2x2 cell pairs 0<=x<=K<=2; all 2x3 cell pairs 0<=x<=K<=2',
            'tests':results,'explicit_witness_assertions':4,
            'assertions_total':sum(r['assertions'] for r in results)+4,
            'status':'ALL_CHECKS_PASS'}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':main()
