#!/usr/bin/env python3
"""R762JQ: supplemental, scoped 120-case probe.
Prerequisite pinned sources (place next to this file):
  R762JM_GENERATE.py (candidate function; SciPy/HiGHS with connectivity cuts)
  R762JM_VERIFY.py   (EDGES Port graph)
Source: awdawmip/enterprise-math @ c63e8cdc2fea3cca8bd33a6d311d18b8424550b4
This finite probe uses one canonical choice of five other triple supports.
It is NOT a universal theorem over all inventory choices.
"""
from itertools import combinations
from R762JM_GENERATE import candidate
from R762JM_VERIFY import EDGES
PORTS=list(combinations(range(6),2))
SUPPORTS=list(combinations(range(6),3))
def exception_sets():
    wings=[]
    for a in (0,1):
        wing=[s for s,t in enumerate(SUPPORTS) if a in t and (1-a) not in t]
        assert len(wing)==6
        wings.extend(combinations(wing,3))
    assert len(wings)==40
    return sorted(set(wings))
def check(n,result):
    assert result is not None and len(result)==60
    deg=[0]*15
    adj=[set() for _ in range(15)]
    for s in range(20):
        assert sum(result[3*s:3*s+3])==n[s]
        for k,(u,v) in enumerate(EDGES[s]):
            x=result[3*s+k]
            assert isinstance(x,int) and 0<=x<=3
            deg[u]+=x;deg[v]+=x
            if x:adj[u].add(v);adj[v].add(u)
    assert sum(result)==42 and deg[0]==0
    assert all(deg[v]>0 and deg[v]%2==0 for v in range(1,15))
    seen={1};todo=[1]
    for u in todo:
        for v in adj[u]:
            if v not in seen:seen.add(v);todo.append(v)
    assert seen==set(range(1,15))
if __name__=='__main__':
    passed=0
    for D in exception_sets():
        for j in D:
            extras=[s for s in range(20) if s not in D][:5]
            triples=set(extras)|{j}
            n=[3 if s in triples else 1 if s in set(D)-{j} else 2 for s in range(20)]
            assert sum(n)==44
            n[j]-=2
            value=candidate(n,[0])
            check(n,value)
            passed+=1
    assert passed==120
    print('PASS: 120/120 exact connected, positive-even, zero-inactive, 42-event witnesses')
