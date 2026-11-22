#!/usr/bin/env python3
"""R762JP integer witness proposer for (6,12,2,0) with disjoint singles.
Requires SciPy/NumPy for candidates; independently verify exported raw records.
Usage: python R762JP_COMPLEMENTARY_GENERATE.py output.raw
Can resume from a raw file containing a whole number of 16-byte records.
"""
import itertools as I
import os, sys, time
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix

P=tuple(I.combinations(range(6),2))
S=tuple(I.combinations(range(6),3))
PI={v:i for i,v in enumerate(P)}
SI={s:i for i,s in enumerate(S)}
EDGES=tuple(tuple(I.combinations(tuple(PI[v] for v in I.combinations(s,2)),2)) for s in S)
U=(0,19)

PERMS=[]
for p in I.permutations(range(6)):
    g=tuple(SI[tuple(sorted(p[v] for v in s))] for s in S)
    if set(g[u] for u in U)==set(U):PERMS.append(g)
assert len(PERMS)==72

def representatives():
    unseen={sum(1<<j for j in T) for T in I.combinations(range(1,19),6)}
    out=[]
    while unseen:
        m=min(unseen)
        orbit={sum(1<<g[j] for j in range(20) if m&(1<<j)) for g in PERMS}
        assert orbit<=unseen
        unseen.difference_update(orbit)
        out.append((tuple(j for j in range(20) if m&(1<<j)),len(orbit)))
    assert len(out)==307 and sum(w for _,w in out)==18564
    return out

def matchings():
    out=[]
    for size in range(4):
        for M in I.combinations(range(15),size):
            endpoints=[v for p in M for v in P[p]]
            if len(endpoints)==len(set(endpoints)):out.append(M)
    assert len(out)==76
    return out

A=lil_matrix((35,75),dtype=float)
for s in range(20):
    for k,(u,v) in enumerate(EDGES[s]):
        A[s,3*s+k]=1
        A[20+u,3*s+k]=1
        A[20+v,3*s+k]=1
for u in range(15):A[20+u,60+u]=-2
A=A.tocsr()

def components(a,active):
    adj=[set() for _ in range(15)]
    for s in range(20):
        for k,(u,v) in enumerate(EDGES[s]):
            if a[3*s+k]:
                adj[u].add(v)
                adj[v].add(u)
    unseen=set(active)
    out=[]
    while unseen:
        stack=[min(unseen)]
        comp=set()
        while stack:
            u=stack.pop()
            if u in comp:continue
            comp.add(u)
            unseen.discard(u)
            stack.extend(adj[u]-comp)
        out.append(comp)
    return out

def candidate(counts,M):
    inactive=set(M)
    active=set(range(15))-inactive
    lower=[0]*60+[0 if u in inactive else 1 for u in range(15)]
    upper=[0 if u in inactive or v in inactive else counts[s]
           for s in range(20) for u,v in EDGES[s]]
    upper += [0 if u in inactive else 21 for u in range(15)]
    bounds=Bounds(lower,upper)
    exact=LinearConstraint(A,counts+[0]*15,counts+[0]*15)
    cuts=[]
    for iteration in range(8):
        result=milp(np.zeros(75),integrality=np.ones(75),
                    bounds=bounds,constraints=[exact]+cuts,
                    options={"time_limit":1.0})
        if result.x is None:return None
        alloc=[int(round(x)) for x in result.x[:60]]
        parts=components(alloc,active)
        if len(parts)==1:return alloc
        for part in parts:
            v=np.zeros(75)
            for s in range(20):
                for k,(u,w) in enumerate(EDGES[s]):
                    if (u in part)!=(w in part):v[3*s+k]=1
            cuts.append(LinearConstraint(v,1,np.inf))
    return None

def check_candidate(T,M,j,a):
    assert j in T and len(a)==60 and all(0<=x<=3 for x in a)
    counts=[1 if s in U else (1 if s==j else 3) if s in T else 2
            for s in range(20)]
    assert sum(counts)==42
    deg=[0]*15
    for s in range(20):
        assert sum(a[3*s:3*s+3])==counts[s]
        for k,(u,v) in enumerate(EDGES[s]):
            deg[u]+=a[3*s+k]
            deg[v]+=a[3*s+k]
    inactive=set(M)
    active=set(range(15))-inactive
    assert all(deg[u]==0 for u in inactive)
    assert all(deg[u]>=2 and deg[u]%2==0 for u in active)
    assert len(components(a,active))==1

def main(path):
    rs=representatives()
    ms=matchings()
    raw=bytearray(open(path,"rb").read()) if os.path.isfile(path) else bytearray()
    assert len(raw)%16==0 and len(raw)<=16*len(rs)*len(ms)
    for index in range(len(raw)//16,len(rs)*len(ms)):
        r,k=divmod(index,len(ms))
        T=rs[r][0]
        M=ms[k]
        for j in T:
            counts=[1 if s in U else (1 if s==j else 3) if s in T else 2
                    for s in range(20)]
            a=candidate(counts,M)
            if a is not None:
                check_candidate(T,M,j,a)
                raw.append(j)
                for o in range(0,60,4):
                    raw.append(sum(a[o+t] << (2*t) for t in range(4)))
                break
        else:
            open(path,"wb").write(raw)
            raise RuntimeError("No candidate: representative %s matching %s" % (r,k))
        if (index+1)%2000==0:open(path,"wb").write(raw)
    open(path,"wb").write(raw)
    print("Generated",len(raw)//16,"integer-checkable records; run separate verifier.")

if __name__=="__main__":main(sys.argv[1])
