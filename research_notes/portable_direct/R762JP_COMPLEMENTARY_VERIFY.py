#!/usr/bin/env python3
"""R762JP independent exact integer checker. No SciPy/solver dependency.
Usage: python R762JP_COMPLEMENTARY_VERIFY.py <raw_16_byte_record_file>
The certificate is external to this text-only PR: raw SHA256 is pinned below.
"""
import itertools as I
import hashlib, json, sys

AXES=range(6)
P=tuple(I.combinations(AXES,2))
S=tuple(I.combinations(AXES,3))
PI={p:i for i,p in enumerate(P)}
SI={s:i for i,s in enumerate(S)}
EDGES=tuple(tuple(I.combinations(tuple(PI[p] for p in I.combinations(s,2)),2)) for s in S)
U=(0,19)

GROUP=[]
for p in I.permutations(AXES):
    g=tuple(SI[tuple(sorted(p[x] for x in s))] for s in S)
    if set(g[u] for u in U)==set(U):GROUP.append(g)
assert len(GROUP)==72

unseen={sum(1<<j for j in T) for T in I.combinations(range(1,19),6)}
REPS=[]
while unseen:
    m=min(unseen)
    orbit={sum(1<<g[j] for j in range(20) if m & (1<<j)) for g in GROUP}
    assert orbit <= unseen
    unseen.difference_update(orbit)
    REPS.append((tuple(j for j in range(20) if m&(1<<j)),len(orbit)))
assert len(REPS)==307 and sum(w for _,w in REPS)==18564

MATCHINGS=[]
for size in range(4):
    for M in I.combinations(range(15),size):
        ends=[a for i in M for a in P[i]]
        if len(ends)==len(set(ends)):MATCHINGS.append(M)
assert len(MATCHINGS)==76
assert [sum(len(M)==i for M in MATCHINGS) for i in range(4)]==[1,15,45,15]

def check(T,M,record):
    assert len(record)==16
    j=record[0]
    assert j in T
    mult=[(byte>>(2*i)) & 3 for byte in record[1:] for i in range(4)]
    assert len(mult)==60
    counts=[1 if s in U else (1 if s==j else 3) if s in T else 2 for s in range(20)]
    assert sum(counts)==42
    assert sorted(counts)==[1]*3+[2]*12+[3]*5
    deg=[0]*15
    adj=[set() for _ in range(15)]
    for s in range(20):
        assert sum(mult[3*s:3*s+3])==counts[s]
        for k,(u,v) in enumerate(EDGES[s]):
            x=mult[3*s+k]
            deg[u]+=x
            deg[v]+=x
            if x:
                adj[u].add(v)
                adj[v].add(u)
    inactive=set(M)
    active=set(range(15))-inactive
    assert all(deg[u]==0 for u in inactive)
    assert all(deg[u]>=2 and deg[u]%2==0 for u in active)
    seen=set()
    stack=[min(active)]
    while stack:
        u=stack.pop()
        if u in seen:continue
        seen.add(u)
        stack.extend(adj[u]-seen)
    assert seen==active

def main(path):
    b=open(path,'rb').read()
    assert len(b)==16*len(REPS)*len(MATCHINGS)
    assert hashlib.sha256(b).hexdigest()=="ec4fbf12a906d2a6179d33974645523e6ffcbd0b165742208e45a2337cc4ff0f"
    for i,(T,weight) in enumerate(REPS):
        for k,M in enumerate(MATCHINGS):
            off=16*(i*len(MATCHINGS)+k)
            check(T,M,b[off:off+16])
    print(json.dumps({
       "result":"PASS", "certificates":len(b)//16, "reps":len(REPS),
       "fixed_U_T_choices":sum(w for _,w in REPS), "matchings":len(MATCHINGS),
       "S6_complementary_U_choices":10,
       "labelled_cover":10*sum(w for _,w in REPS)*len(MATCHINGS),
       "sha256":hashlib.sha256(b).hexdigest()
    },sort_keys=True))

if __name__=="__main__":main(sys.argv[1])
