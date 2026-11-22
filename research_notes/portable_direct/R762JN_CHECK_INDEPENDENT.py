#!/usr/bin/env python3
"""R762JN: independent, exact, standard-library validation of two certificate archives.
Usage: python R762JN_CHECK_INDEPENDENT.py FULL_ACTIVE_CERTS.b64 NONMATCHING_CERTS.b64
Archives: one 16-byte record per (fixed-z T orbit representative, relevant M).
"""
import sys, itertools, base64, lzma, hashlib, json
axes = tuple(range(6))
ports = list(itertools.combinations(axes,2))
supports = list(itertools.combinations(axes,3))
pi={p:i for i,p in enumerate(ports)}
si={s:i for i,s in enumerate(supports)}
tri=[tuple(pi[x] for x in itertools.combinations(s,2)) for s in supports]
edges=[tuple(itertools.combinations(t,2)) for t in tri]
perms=[]
for p in itertools.permutations(axes):
    if set(p[:3])=={0,1,2}:
        perms.append(tuple(si[tuple(sorted(p[a] for a in s))] for s in supports))
assert len(perms)==36
unseen={sum(1<<s for s in T) for T in itertools.combinations(range(1,20),6)}
reps=[]
while unseen:
    mask=min(unseen)
    orbit={sum(1<<g[s] for s in range(20) if mask&(1<<s)) for g in perms}
    assert orbit<=unseen
    unseen-=orbit
    reps.append((tuple(s for s in range(20) if mask&(1<<s)),len(orbit)))
assert len(reps)==885 and sum(w for _,w in reps)==27132
eligible=[]
for k in range(5):
    for M in itertools.combinations(range(15),k):
        if all(len(set(M)&set(tri[s]))<=1 for s in range(1,20)):
            eligible.append(M)
assert len(eligible)==92
nonmatch=[M for M in eligible if len({a for v in M for a in ports[v]})<2*len(M)]
assert len(nonmatch)==16
def check(T,M,r):
    assert len(r)==16 and r[0] in T
    j=r[0]
    a=[(b>>(2*k))&3 for b in r[1:] for k in range(4)]
    n=[0 if s==0 else 2+int(s in T)-2*int(s==j) for s in range(20)]
    assert sum(n)==42 and len(a)==60
    deg=[0]*15
    adj=[set() for _ in range(15)]
    for s in range(20):
        assert sum(a[3*s:3*s+3])==n[s]
        for k,(u,v) in enumerate(edges[s]):
            w=a[3*s+k]
            deg[u]+=w;deg[v]+=w
            if w:adj[u].add(v);adj[v].add(u)
    V=set(range(15))-set(M)
    assert all(deg[v]>=2 and deg[v]%2==0 for v in V)
    assert all(deg[v]==0 for v in M)
    seen=set();stack=[min(V)]
    while stack:
        v=stack.pop()
        if v not in seen:
            seen.add(v);stack.extend(adj[v]-seen)
    assert seen==V
def verify(filename,sets):
    enc=open(filename,encoding="ascii").read().strip()
    raw=lzma.decompress(base64.b64decode(enc,validate=True))
    assert len(raw)==16*len(reps)*len(sets)
    for i,(T,_) in enumerate(reps):
        for k,M in enumerate(sets):
            q=16*(i*len(sets)+k)
            check(T,M,raw[q:q+16])
    return dict(records=len(reps)*len(sets), raw_sha256=hashlib.sha256(raw).hexdigest())
if __name__=="__main__":
    assert len(sys.argv)==3
    print(json.dumps({"result":"PASS","full_active":verify(sys.argv[1],[()]),
      "nonmatching":verify(sys.argv[2],nonmatch),
      "T_orbits":len(reps),"T_labelled_per_z":27132,
      "eligible_M":92,"remaining_nonempty_matching_M":75,
      "labelled_cases":20*27132*17},indent=2))
