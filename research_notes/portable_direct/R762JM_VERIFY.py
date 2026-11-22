#!/usr/bin/env python3
"""Independent exact, standard-library-only verifier for R762JM.

Usage: python R762JM_VERIFY.py R762JM_CERTS.b64
The archive is LZMA(Base64(bytes)) with one 16-byte record per
orbit-representative/inactive-matching: one support index plus 60
2-bit edge multiplicities packed into 15 bytes.
"""
import base64
import hashlib
import itertools
import json
import lzma
import sys
from collections import Counter

AXES=range(6)
PORTS=list(itertools.combinations(AXES,2))
SUPPORTS=list(itertools.combinations(AXES,3))
PORT_INDEX={p:i for i,p in enumerate(PORTS)}
SUPPORT_INDEX={s:i for i,s in enumerate(SUPPORTS)}
TRIANGLES=[tuple(PORT_INDEX[p] for p in itertools.combinations(t,2)) for t in SUPPORTS]
EDGES=[list(itertools.combinations(tri,2)) for tri in TRIANGLES]
PERMS=[tuple(SUPPORT_INDEX[tuple(sorted(g[a] for a in s))] for s in SUPPORTS)
       for g in itertools.permutations(AXES)]

def pair_orbits():
    unseen={(sum(1<<j for j in T),l)
            for T in itertools.combinations(range(20),5)
            for l in range(20) if l not in T}
    out=[]
    while unseen:
        mask,l=min(unseen)
        T=tuple(j for j in range(20) if mask&(1<<j))
        orbit={(sum(1<<g[j] for j in T),g[l]) for g in PERMS}
        assert orbit <= unseen
        unseen.difference_update(orbit)
        out.append((T,l,len(orbit)))
    return out

def inactive_matchings():
    return [m for k in range(4) for m in itertools.combinations(range(15),k)
            if len({a for port in m for a in PORTS[port]})==2*k]

def exact_check(T,l,M,j,a):
    assert len(T)==5 and len(set(T))==5 and l not in T and j in T
    assert len(a)==60 and all(type(x)==int and 0<=x<=3 for x in a)
    counts=[2+(s in T)-(s==l)-2*(s==j) for s in range(20)]
    assert sorted(Counter(counts).items())==[(1,2),(2,14),(3,4)]
    assert sum(counts)==42 and sum(a)==42
    assert all(sum(a[3*s:3*s+3])==counts[s] for s in range(20))
    deg=[0]*15
    graph=[set() for _ in range(15)]
    for s in range(20):
        for k,(u,v) in enumerate(EDGES[s]):
            w=a[3*s+k]
            deg[u]+=w
            deg[v]+=w
            if w:
                graph[u].add(v)
                graph[v].add(u)
    inactive=set(M)
    active=set(range(15))-inactive
    assert active
    assert all(deg[v]==0 for v in inactive)
    assert all(deg[v]>=2 and deg[v]%2==0 for v in active)
    stack=[min(active)]
    seen=set()
    while stack:
        u=stack.pop()
        if u not in seen:
            seen.add(u)
            stack.extend(graph[u]-seen)
    assert seen==active

def verify(path):
    with open(path,'r',encoding='ascii') as f:
        encoded=f.read().strip()
    raw=lzma.decompress(base64.b64decode(encoded,validate=True))
    reps=pair_orbits()
    matchings=inactive_matchings()
    assert len(reps)==402 and sum(x[2] for x in reps)==232560
    assert len(matchings)==76 and len(raw)==16*402*76
    checks=0
    sizes=Counter()
    for i,(T,l,weight) in enumerate(reps):
        for k,M in enumerate(matchings):
            offset=16*(i*len(matchings)+k)
            j=raw[offset]
            a=[]
            for b in raw[offset+1:offset+16]:
                a.extend((b>>(2*h))&3 for h in range(4))
            exact_check(T,l,M,j,a)
            checks+=1
            sizes[len(M)]+=1
    return {'result':'PASS','case':'(5,14,1,0)','original_events':44,
            'compressed_events':42,'all_positive_supports':True,
            'active_ports':'ALL_ALLOWED_INACTIVE_MATCHINGS',
            'pair_orbits':len(reps),'labelled_(T,L)_pairs':232560,
            'inactive_matchings':len(matchings),
            'exact_integer_certificates':checks,
            'labelled_(T,L,M)_configurations':232560*76,
            'representative_matchings_by_size':dict(sorted(sizes.items())),
            'raw_certificate_sha256':hashlib.sha256(raw).hexdigest(),
            'encoded_certificate_sha256':hashlib.sha256((encoded+'\n').encode('ascii')).hexdigest(),
            'status':'AUTHOR_EXACT_FINITE_CHECKED_NOT_INDEPENDENTLY_REVIEWED'}

if __name__=='__main__':
    print(json.dumps(verify(sys.argv[1]),ensure_ascii=False,indent=2))
