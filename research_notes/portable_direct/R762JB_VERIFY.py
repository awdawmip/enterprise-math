#!/usr/bin/env python3
"""R762JB: independent standard-library exact verifier for 302 Port-Euler 44-event certificates.
Run from any directory: python R762JB_VERIFY.py
This covers the finite composite observer only, not native P000/BRC dynamics.
"""
from itertools import combinations, permutations
from collections import Counter
from pathlib import Path
from hashlib import sha256
import base64, zlib

PORTS=list(combinations(range(6),2))
SUPPORTS=list(combinations(range(6),3))
pi={p:i for i,p in enumerate(PORTS)}
si={s:i for i,s in enumerate(SUPPORTS)}
TR=[tuple(pi[p] for p in combinations(s,2)) for s in SUPPORTS]
E=[tuple(combinations(t,2)) for t in TR]

def components(ss):
    graph=[set() for _ in range(15)]
    for s in ss:
        a,b,c=TR[s]
        graph[a].update((b,c))
        graph[b].update((a,c))
        graph[c].update((a,b))
    remaining=set(range(15))
    number=0
    while remaining:
        number+=1
        seen={min(remaining)}
        todo=list(seen)
        for v in todo:
            for w in graph[v]:
                if w not in seen:
                    seen.add(w)
                    todo.append(w)
        remaining-=seen
    return number

def representatives():
    essential=set()
    coverage=Counter()
    for t in combinations(range(20),6):
        base=components(t)
        if all(components(t[:i]+t[i+1:])>base for i in range(6)):
            essential.add(sum(1<<s for s in t))
            coverage[len({p for s in t for p in TR[s]})]+=1
    assert len(essential)==27720
    assert dict(coverage)=={10:30,11:2760,12:14940,13:8160,14:1800,15:30}
    transforms=[
        tuple(si[tuple(sorted(q[a] for a in support))] for support in SUPPORTS)
        for q in permutations(range(6))
    ]
    left=set(essential)
    reps=[]
    while left:
        m=min(left)
        orbit={sum(1<<q[s] for s in range(20) if m>>s&1) for q in transforms}
        assert orbit<=essential
        left-=orbit
        reps.append((m,len(orbit)))
    assert len(reps)==67 and sum(n for _,n in reps)==27720
    return reps

def matchings():
    m=[tuple(p) for k in range(4) for p in combinations(range(15),k)
        if len({axis for i in p for axis in PORTS[i]})==2*k]
    assert len(m)==76
    return m

def verify(mask,missing,deleted,alloc):
    assert len(alloc)==60 and all(0<=v<=3 for v in alloc)
    assert mask>>deleted&1
    counts=[3 if mask>>s&1 else 2 for s in range(20)]
    assert sum(counts)==46
    counts[deleted]=1
    assert sum(counts)==44
    assert all(sum(alloc[3*s:3*s+3])==counts[s] for s in range(20))
    active=set(range(15))-set(missing)
    degree=[0]*15
    graph=[set() for _ in range(15)]
    for s in range(20):
        for e,(u,v) in enumerate(E[s]):
            k=alloc[3*s+e]
            if k:
                assert u in active and v in active
                degree[u]+=k
                degree[v]+=k
                graph[u].add(v)
                graph[v].add(u)
    assert all(degree[p]>=2 and degree[p]%2==0 for p in active)
    assert all(degree[p]==0 for p in missing)
    reached={min(active)}
    queue=list(reached)
    for u in queue:
        for v in graph[u]:
            if v not in reached:
                reached.add(v)
                queue.append(v)
    assert reached==active

def main():
    raw_compressed=base64.b64decode(Path(__file__).with_name("R762JB_CERTS.b64").read_text())
    assert sha256(raw_compressed).hexdigest()=="2a7315a8e187a6412da439725f309434880a0e5487ad6ca20e1843965cca9c7c"
    raw=zlib.decompress(raw_compressed)
    assert len(raw)==4530
    assert sha256(raw).hexdigest()=="bc4604217678f2abb252731b7afc32efccb738fcd06a21b0d26fbb884de00411"
    pos=0
    cases=0
    labelled=0
    for mask,orbit_size in representatives():
        triples=[s for s in range(20) if mask>>s&1]
        used={p for s in triples for p in TR[s]}
        for missing in matchings():
            if not set(missing).isdisjoint(used):
                continue
            block=raw[15*pos:15*(pos+1)]
            alloc=[(b>>(2*j))&3 for b in block for j in range(4)]
            verify(mask,missing,triples[0],alloc)
            cases+=1
            labelled+=orbit_size
            pos+=1
    assert pos==302 and cases==302 and labelled==123690
    print("PASS R762JB: 38,760 masks; 27,720 all-essential; 67 S6 orbits; 302/302 44-event certificates")
    print("labelled all-essential/inactive-matching cases:",labelled)
    print("raw bytes:",len(raw),"; raw sha256:",sha256(raw).hexdigest())

if __name__=="__main__":
    main()
