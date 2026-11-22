#!/usr/bin/env python3
"""Independent, standard-library-only verifier of R762JL exact certificates.

Usage: python PORT44_T4D16_VERIFY.py PORT44_T4D16_CERTS.b64
The certificate format contains 1596 records, each 16 bytes after lzma decoding:
one support index j, then 15 packed bytes for 60 two-bit edge counts.
Records are ordered by least-mask S6 orbit representative, then all inactive
pair-Port matchings in lexicographic (size, combination) order.
"""
import base64
import itertools as it
import json
import sys
import lzma
from collections import Counter

AXES=range(6)
PORTS=list(it.combinations(AXES,2))
SUPPORTS=list(it.combinations(AXES,3))
PID={x:i for i,x in enumerate(PORTS)}
SID={x:i for i,x in enumerate(SUPPORTS)}
TRI=[tuple(PID[p] for p in it.combinations(t,2)) for t in SUPPORTS]
EDGES=[list(it.combinations(tri,2)) for tri in TRI]
PERMS=[tuple(SID[tuple(sorted(g[a] for a in s))] for s in SUPPORTS)
       for g in it.permutations(AXES)]

def orbit_representatives():
    unseen={sum(1<<i for i in t) for t in it.combinations(range(20),4)}
    ans=[]
    while unseen:
        mask=min(unseen)
        rep=tuple(i for i in range(20) if mask & (1<<i))
        orbit={sum(1<<g[i] for i in rep) for g in PERMS}
        assert orbit<=unseen,'Invalid orbit partition'
        ans.append((rep,len(orbit)))
        unseen-=orbit
    return ans

def inactive_matchings():
    return [m for k in range(4) for m in it.combinations(range(15),k)
            if len({axis for p in m for axis in PORTS[p]})==2*k]

def verify(triples,inactive,removed,alloc):
    assert len(alloc)==60 and all(type(x) is int and 0<=x<=3 for x in alloc)
    assert len(triples)==4 and len(set(triples))==4 and removed in triples
    assert len(set(inactive))==len(inactive)
    assert sum(alloc)==42
    counts=[2+(s in triples)-2*(s==removed) for s in range(20)]
    assert sum(counts)==42 and all(c>0 for c in counts)
    degrees=[0]*15
    graph=[set() for _ in range(15)]
    for s in range(20):
        assert sum(alloc[3*s:3*s+3])==counts[s]
        for k,(u,v) in enumerate(EDGES[s]):
            m=alloc[3*s+k]
            degrees[u]+=m
            degrees[v]+=m
            if m:
                graph[u].add(v)
                graph[v].add(u)
    inactive=set(inactive)
    active=set(range(15))-inactive
    assert active
    assert all(degrees[u]>=2 and degrees[u]%2==0 for u in active)
    assert all(degrees[u]==0 for u in inactive)
    reached=set()
    todo=[min(active)]
    while todo:
        u=todo.pop()
        if u in reached:
            continue
        reached.add(u)
        todo.extend(graph[u]-reached)
    assert reached==active

def main():
    with open(sys.argv[1],'rt',encoding='ascii') as f:
        data=lzma.decompress(base64.b64decode(f.read().strip()))
    reps=orbit_representatives()
    matchings=inactive_matchings()
    assert len(reps)==21 and sum(n for _,n in reps)==4845
    assert len(matchings)==76
    assert len(data)==16*21*76
    count=Counter()
    for i,(triples,orbit_size) in enumerate(reps):
        for m_idx,missing in enumerate(matchings):
            pos=16*(i*len(matchings)+m_idx)
            removed=data[pos]
            allocation=[]
            for b in data[pos+1:pos+16]:
                allocation.extend(((b>>(2*j))&3) for j in range(4))
            verify(triples,missing,removed,allocation)
            count[len(missing)]+=1
    assert sum(count.values())==1596
    print(json.dumps({
        'status':'PASS',
        'support_subsets':4845,
        'S6_orbits':21,
        'inactive_matching_sets':76,
        'verified_exact_integer_certificates':sum(count.values()),
        'labelled_cases':4845*76,
        'inactive_size_distribution':dict(sorted(count.items()))
    },indent=2))

if __name__=='__main__':
    main()
