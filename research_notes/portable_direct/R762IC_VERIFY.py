#!/usr/bin/env python3
"""R762IC independent finite-certificate checker: exact signed sets, not floats.
Visits every nonsignable Q (a down-set). Signability only increases with Q.
Port GF(2) parity is checked via connected components rather than elimination.
"""
from itertools import combinations
from collections import Counter

T = list(combinations(range(6), 3))
E = list(combinations(range(6), 2))
ep = {v: i for i, v in enumerate(E)}
D = [sum(1 << (7*a) for a in t) for t in T]
CTR = sum(32 << (7*a) for a in range(6))
reps = (
    ('024','035','125','134'),
    ('012','015','025','034','123','124'),
    ('012','013','014','025','035','045','125','135','145','234')
)
ids = {''.join(map(str,t)): i for i,t in enumerate(T)}
adj = [sum((1<<j) for j,t in enumerate(T) if len(set(s)&set(t)) == 2) for s in T]
ports = [tuple(ep[x] for x in combinations(t,2)) for t in T]
edge_options = [
    tuple((1<<p[i])^(1<<p[j]) for i,j in combinations(range(3),2))
    for p in ports
]

def base_parities(core):
    d = {0}
    for j in core:
        d = {x^e for x in d for e in edge_options[j]}
    return d

def core_targets(core):
    ans = set()
    for sig in range(1 << len(core)):
        co = [
            sum((1 if (sig>>k)&1 else -1)*int(a in T[j])
                for k,j in enumerate(core))
            for a in range(6)
        ]
        assert all(v%2 == 0 for v in co)
        ans.add(CTR - sum((v//2) << (7*a) for a,v in enumerate(co)))
    return ans

def support_connected(q,coremask):
    allm = q | coremask
    seen = allm & -allm
    while True:
        nxt = seen
        for k in range(20):
            if (seen>>k)&1:
                nxt |= adj[k] & allm
        if nxt == seen:
            return seen == allm
        seen = nxt

def parity_possible_components(q,baselines):
    parent = list(range(15))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for j in range(20):
        if (q>>j)&1:
            a,b,c = ports[j]
            parent[find(a)] = find(b)
            parent[find(b)] = find(c)
    blocks = {}
    for v in range(15):
        root = find(v)
        blocks[root] = blocks.get(root,0) ^ (1<<v)
    return any(all(((x&b).bit_count() % 2) == 0 for b in blocks.values())
               for x in baselines)

expected = [
    (4,16,81,3824,64,0,{3:8,4:24,5:24,6:8}),
    (6,64,621,1056,0,0,{}),
    (10,656,6081,1024,0,0,{})
]
for rep,want in zip(reps,expected):
    core = [ids[x] for x in rep]
    coremask = sum(1<<j for j in core)
    targets = core_targets(core)
    bp = base_parities(core)
    allbad, cbad, ppbad = Counter(), Counter(), Counter()
    # Bad-Q recursion is complete: signable Q => all Q supersets signable.
    def walk(q,last,reachable):
        level = q.bit_count()
        allbad[level] += 1
        if support_connected(q,coremask):
            cbad[level] += 1
            if parity_possible_components(q,bp):
                ppbad[level] += 1
        for j in range(last+1,20):
            more = reachable | {x+D[j] for x in reachable} | {x-D[j] for x in reachable}
            if targets.isdisjoint(more):
                walk(q | (1<<j), j, more)
    assert targets.isdisjoint({CTR})
    walk(0,-1,{CTR})
    observed = (
        len(core), len(targets),len(bp),
        sum(allbad.values()),sum(cbad.values()),sum(ppbad.values())
    )
    assert observed == want[:6], (observed,want)
    if want[6]:
        assert dict(cbad) == want[6], (cbad,want[6])
    print('CORE',len(core),'targets',len(targets),'base_parities',len(bp),
          'bad',sum(allbad.values()),'connected_bad',sum(cbad.values()),
          'joint_bad',sum(ppbad.values()),flush=True)
    print('BAD_LEVELS',dict(sorted(allbad.items())),flush=True)
    print('CONNECTED_BAD_LEVELS',dict(sorted(cbad.items())),flush=True)
print('PASS R762IC: independent exact monotone enumeration and Port components')
