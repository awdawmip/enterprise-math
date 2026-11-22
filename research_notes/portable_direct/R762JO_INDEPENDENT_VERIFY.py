#!/usr/bin/env python3
"""R762JO standalone exact verifier for all 92 inactive Port classes.
Run: python R762JO_INDEPENDENT_VERIFY.py MATCHING.b64 ACTIVE.b64 NONMATCHING.b64
All three inputs are Base64(LZMA(packed 16-byte certificate records)).
Requires Python standard library only; independent of the SciPy proposer.
"""
import base64, hashlib, itertools, json, lzma, sys

A=tuple(range(6))
ports=tuple(itertools.combinations(A,2))
supports=tuple(itertools.combinations(A,3))
port_id={p:i for i,p in enumerate(ports)}
support_id={s:i for i,s in enumerate(supports)}
tri=tuple(tuple(port_id[p] for p in itertools.combinations(s,2)) for s in supports)
edges=tuple(tuple(itertools.combinations(t,2)) for t in tri)
z=0  # Missing support {0,1,2}; all others by axis permutations.
perms=[]
for p in itertools.permutations(A):
    if set(p[:3])==set(supports[z]):
        perms.append(tuple(support_id[tuple(sorted(p[a] for a in s))] for s in supports))
assert len(perms)==36

def reps():
    unseen={sum(1<<s for s in T) for T in itertools.combinations(range(1,20),6)}
    out=[]
    while unseen:
        mask=min(unseen)
        orbit={sum(1<<g[s] for s in range(20) if mask&(1<<s)) for g in perms}
        assert orbit<=unseen
        unseen.difference_update(orbit)
        out.append((tuple(s for s in range(20) if mask&(1<<s)),len(orbit)))
    assert len(out)==885 and sum(w for _,w in out)==27132
    return out

def inactive_sets():
    out=[]
    for k in range(16):  # All 2**15 subsets, no implicit size bound.
        for M in itertools.combinations(range(15),k):
            if all(len(set(M).intersection(t))<=1 for s,t in enumerate(tri) if s!=z):
                out.append(M)
    assert len(out)==92
    return out

def kind(M):
    if not M:return 'active'
    return 'matching' if len({a for v in M for a in ports[v]})==2*len(M) else 'nonmatching'

def check(T,M,rec):
    assert len(rec)==16
    j=rec[0]
    assert j in T
    a=[(b>>(2*k))&3 for b in rec[1:] for k in range(4)]
    assert len(a)==60
    n=[0 if s==z else 2+int(s in T)-2*int(s==j) for s in range(20)]
    assert sorted(n)==[0,1]+[2]*13+[3]*5 and sum(n)==42
    active=set(range(15))-set(M)
    degree=[0]*15
    adj=[set() for _ in range(15)]
    for s in range(20):
        assert sum(a[3*s:3*s+3])==n[s]
        for k,(u,v) in enumerate(edges[s]):
            count=a[3*s+k]
            degree[u]+=count;degree[v]+=count
            if count:adj[u].add(v);adj[v].add(u)
    assert all(degree[v]>=2 and degree[v]%2==0 for v in active)
    assert all(degree[v]==0 for v in M)
    visited=set()
    todo=[min(active)]
    while todo:
        v=todo.pop()
        if v not in visited:
            visited.add(v)
            todo.extend(adj[v]-visited)
    assert visited==active

def verify(path,reps_,Ms):
    encoded=open(path,'rt',encoding='ascii').read().strip()
    raw=lzma.decompress(base64.b64decode(encoded,validate=True))
    assert len(raw)==len(reps_)*len(Ms)*16
    for i,(T,_) in enumerate(reps_):
        for k,M in enumerate(Ms):
            offset=16*(i*len(Ms)+k)
            check(T,M,raw[offset:offset+16])
    return {'records':len(reps_)*len(Ms),'raw_bytes':len(raw),
            'raw_sha256':hashlib.sha256(raw).hexdigest(),
            'encoded_sha256':hashlib.sha256((encoded+'\n').encode()).hexdigest()}

if __name__=='__main__':
    if len(sys.argv)!=4:
        raise SystemExit(__doc__)
    R=reps();E=inactive_sets()
    matching=[M for M in E if kind(M)=='matching']
    special=[M for M in E if kind(M)=='nonmatching']
    assert len(matching)==75 and len(special)==16
    results={
        'matching':verify(sys.argv[1],R,matching),
        'fully_active':verify(sys.argv[2],R,[()]),
        'nonmatching':verify(sys.argv[3],R,special)}
    out={'result':'PASS','records':sum(d['records'] for d in results.values()),
         'labelled_instances':20*27132*92,'inactive_sets_per_absent_support':92,
         'claim_scope':'AUTHOR_EXACT_FINITE_CHECKED_NOT_REVIEWED','archives':results}
    print(json.dumps(out,indent=2))
