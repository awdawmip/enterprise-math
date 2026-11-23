#!/usr/bin/env python3
"""R762JV: exact component spectrum for five singleton colors in Port-Euler.
Tests parity-flexible non-singleton color graph only; NOT Euler feasibility.
"""
from itertools import combinations
from collections import Counter
import json
A=range(6)
P=tuple(combinations(A,2))
S=tuple(combinations(A,3))
M={0:(),1:((0,1),),2:((0,1),(2,3)),3:((0,1),(2,3),(4,5))}

def sig(m,D):
    V=set(P)-set(M[m]);q={v:v for v in V}
    def find(v):
        while q[v]!=v:
            q[v]=q[q[v]];v=q[v]
        return v
    def union(u,v):
        u,v=find(u),find(v)
        if u!=v:q[v]=u
    for s in S:
        if s in D:continue
        endpoints=[p for p in combinations(s,2) if p in V]
        if len(endpoints)==3:
            for u,v in combinations(endpoints,2):union(u,v)
    roots=Counter(find(v) for v in V)
    return tuple(sorted(roots.values(),reverse=True))

def main():
    cases=[]
    for m in range(4):
        distribution=Counter(sig(m,D) for D in combinations(S,5))
        assert sum(distribution.values())==15504
        cases.append({
            "inactive_matching_size":m,
            "representative_missing_ports":["".join(map(str,p)) for p in M[m]],
            "all_five_singleton_sets":sum(distribution.values()),
            "non_singleton_flexible_connected_count":distribution[(15-m,)],
            "disconnected_count":sum(v for k,v in distribution.items() if len(k)>1),
            "components":{"-".join(map(str,k)):v for k,v in sorted(distribution.items())}
        })
    assert [x["disconnected_count"] for x in cases]==[240,1172,4008,7232]
    print(json.dumps({
        "schema":"R762JV_FIVE_SINGLETON_COMPONENT_SCREEN_V1",
        "scope":"parity-flexible support graph only; not Euler feasibility",
        "cases":cases},ensure_ascii=False,indent=2))
if __name__=="__main__":main()
