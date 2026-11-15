#!/usr/bin/env python3
"""PREFIX-799: exact standard-library checks for capacity-fiber residual cycle gcd.

Integer arithmetic only. Deterministic exhaustive families and disclosed subfamilies.
"""
from __future__ import annotations
from collections import defaultdict
from itertools import product
from math import gcd
import json
from pathlib import Path

STATS = defaultdict(int)


def all_tables(K):
    b, c = len(K), len(K[0])
    for flat in product(*(range(k + 1) for row in K for k in row)):
        x = tuple(tuple(flat[i * c:(i + 1) * c]) for i in range(b))
        r = tuple(sum(row) for row in x)
        s = tuple(sum(x[i][j] for i in range(b)) for j in range(c))
        yield r, s, x


def arcs(K, x, w):
    b, c = len(K), len(K[0])
    a = []
    for i in range(b):
        for j in range(c):
            if x[i][j] < K[i][j]:
                a.append((i, b + j, w[i][j], i, j, 1))
            if x[i][j] > 0:
                a.append((b + j, i, -w[i][j], i, j, -1))
    return a


def scc_residual_gcd(K, x, w):
    b, c = len(K), len(K[0]); n = b + c
    a = arcs(K, x, w)
    out = [[] for _ in range(n)]
    rev = [[] for _ in range(n)]
    for u,v,z,*_ in a:
        out[u].append((v,z)); rev[v].append(u)
    seen = set(); order=[]
    def dfs(v):
        seen.add(v)
        for t,_ in out[v]:
            if t not in seen: dfs(t)
        order.append(v)
    for v in range(n):
        if v not in seen: dfs(v)
    components=[]; cid={}
    def back(v,idx):
        cid[v]=idx
        components[idx].append(v)
        for t in rev[v]:
            if t not in cid:back(t,idx)
    for v in reversed(order):
        if v not in cid:
            components.append([]); back(v,len(components)-1)
    distance={}; g=0
    for compid, comp in enumerate(components):
        root=comp[0]; distance[root]=0; stack=[root]
        while stack:
            u=stack.pop()
            for v,z in out[u]:
                if cid[v] == compid and v not in distance:
                    distance[v]=distance[u]+z; stack.append(v)
        assert all(v in distance for v in comp)
    for u,v,z,*_ in a:
        if cid[u]==cid[v]:
            g=gcd(g, distance[u]+z-distance[v])
    return abs(g)


def direct_gcd(fiber, x, w):
    base=weighted(x,w); g=0
    for y in fiber:
        g=gcd(g, weighted(y,w)-base)
    return abs(g)


def weighted(x,w):
    return sum(a*b for row1,row2 in zip(x,w) for a,b in zip(row1,row2))


def monotone_cycle_path(K,x0,y):
    b,c=len(K),len(K[0]); cur=[list(r) for r in x0]; moves=0
    start_l1=sum(abs(y[i][j]-cur[i][j]) for i in range(b) for j in range(c))
    while True:
        demand=[]
        for i in range(b):
            for j in range(c):
                d=y[i][j]-cur[i][j]
                if d>0: demand.append((i,b+j,i,j,+1))
                elif d<0: demand.append((b+j,i,i,j,-1))
        if not demand: break
        edges=defaultdict(list)
        for e in demand: edges[e[0]].append(e)
        found=None
        def dfs(v, path, active):
            nonlocal found
            for edge in edges[v]:
                u,t,_,_,_=edge
                if t == path[0][0] if path else False:
                    found = path+[edge]; return True
                if t in active:continue
                if dfs(t,path+[edge],active|{t}): return True
            return False
        for v in list(edges):
            if dfs(v,[],{v}):break
        assert found is not None, "balanced net difference must contain a directed cycle"
        for _,__,i,j,sgn in found:
            cur[i][j]+=sgn
            assert 0<=cur[i][j]<=K[i][j]
        assert tuple(sum(row) for row in cur)==tuple(sum(row) for row in x0)
        assert tuple(sum(cur[i][j] for i in range(b)) for j in range(c))==tuple(sum(x0[i][j] for i in range(b)) for j in range(c))
        moves+=1
        assert moves<=start_l1//4, "each bipartite cycle length at least four"
    assert tuple(tuple(row) for row in cur)==y
    return moves


def evaluate(K, weights, exhaustive_paths=True):
    groups=defaultdict(list)
    for r,s,x in all_tables(K):groups[r,s].append(x)
    STATS['capacity_cases']+=1
    STATS['feasible_fibers']+=len(groups)
    for fiber in groups.values():
        STATS['tables']+=len(fiber)
        x0=fiber[0]
        for w in weights:
            g1=scc_residual_gcd(K,x0,w)
            g2=direct_gcd(fiber,x0,w)
            assert g1==g2, (K,x0,w,g1,g2)
            STATS['gcd_assertions']+=1
            if g1 == 0:
                assert len({weighted(x,w) for x in fiber})==1
            else:
                assert all((weighted(x,w)-weighted(x0,w))%g1==0 for x in fiber)
            STATS['modular_assertions']+=1
            # State-independence: same actual modulus using every starting table.
            for x in fiber:
                assert scc_residual_gcd(K,x,w)==g1
                STATS['basepoint_assertions']+=1
        if exhaustive_paths:
            for y in fiber:
                monotone_cycle_path(K,x0,y)
                STATS['reachability_checks']+=1


def weights_for(b,c):
    return [
        tuple(tuple(i*c+j for j in range(c)) for i in range(b)),
        tuple(tuple((i+2*j)%4-1 for j in range(c)) for i in range(b)),
        tuple(tuple(2*i*j+i-3*j for j in range(c)) for i in range(b)),
        tuple(tuple(1 if (i,j)==(0,0) else 0 for j in range(c)) for i in range(b)),
    ]


def run():
    for b,c,kmax,stride in [(2,2,2,1),(2,3,1,1),(2,3,2,17),(3,3,1,29)]:
        for index,flat in enumerate(product(range(kmax+1),repeat=b*c)):
            if index%stride: continue
            K=tuple(tuple(flat[i*c:(i+1)*c]) for i in range(b))
            evaluate(K,weights_for(b,c),True)
        STATS[f'family_{b}x{c}_Kmax{kmax}_stride{stride}']=1
    K=tuple(tuple(int((i<2 and j<2) or (i>=2 and j>=2)) for j in range(4)) for i in range(4))
    w=tuple(tuple(2 if (i,j)==(0,0) else (3 if (i,j)==(2,2) else 0) for j in range(4)) for i in range(4))
    r=(1,1,0,0); s=(1,1,0,0)
    fiber=[x for rr,ss,x in all_tables(K) if rr==r and ss==s]
    assert len(fiber)==2
    assert sorted(weighted(x,w) for x in fiber)==[0,2]
    assert scc_residual_gcd(K,fiber[0],w)==2
    # Two disconnected structural four-cycles have gains 2 and 3, so full graph gcd is 1.
    assert gcd(2,3)==1
    STATS['explicit_saturation_counterexample_checks']+=4
    # Forced singleton while the capacity graph has directed structural cycles.
    zero=tuple(tuple(0 for _ in range(4)) for i in range(4))
    assert scc_residual_gcd(K,zero,w)==0
    STATS['explicit_saturation_counterexample_checks']+=1
    result={
        'schema':'PREFIX799_RESIDUAL_CYCLE_GCD_CHECK_V1',
        'arithmetic':'exact Python integers',
        'family_coverage':[
            'all 2x2 capacity matrices with entries 0,1,2',
            'all 2x3 capacity matrices with entries 0,1',
            '2x3 capacity matrices with entries 0,1,2 at zero-based product-index multiples of 17',
            '3x3 capacity matrices with entries 0,1 at zero-based product-index multiples of 29'
        ],
        'weight_patterns':4,
        'counters':dict(sorted(STATS.items())),
        'example':{'graph':'two disjoint K_2,2 blocks in a 4x4 table','margins':[1,1,0,0],'structural_gcd':1,'actual_gcd':2,'attainable_Q':[0,2]},
        'status':'ALL_CHECKS_PASS PREFIX799 CAPACITY_AWARE_CYCLE_GCD'
    }
    p=Path(__file__).with_name('PREFIX799_R6_RESIDUAL_CYCLE_GCD_RESULTS.json')
    p.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__': run()
