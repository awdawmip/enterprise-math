#!/usr/bin/env python3
"""R762IU: finite certificates for k=0 six-axis Port-Euler <=47.
Run all: python R762IU_PORT47_EXHAUSTIVE.py
Reproduce in segments: python R762IU_PORT47_EXHAUSTIVE.py 0 1400
Other checked ranges: 1400:2800, 2800:4200, 4200:5600, 5600:6318.
SciPy/HiGHS proposes; integer-only verifier checks every witness.
"""
import sys, json, time
from itertools import combinations, permutations
from collections import Counter
from hashlib import sha256
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint

P=list(combinations(range(6),2))
T=list(combinations(range(6),3))
pi={p:i for i,p in enumerate(P)}
ti={t:i for i,t in enumerate(T)}
V=[tuple(pi[p] for p in combinations(t,2)) for t in T]
E=[list(combinations(v,2)) for v in V]
M=[m for k in range(4) for m in combinations(range(15),k)
   if len({a for v in m for a in P[v]})==2*k]
maps=[tuple(ti[tuple(sorted(perm[a] for a in t))] for t in T)
      for perm in permutations(range(6))]
assert len(M)==76 and len(maps)==720

def component_count(sub):
    parent=list(range(15))
    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for s in sub:
        a,b,c=V[s]
        for x,y in ((a,b),(a,c)):parent[root(x)]=root(y)
    return len({root(x) for x in range(15)})

def essential(k):
    ans=[]
    for sub in combinations(range(20),k):
        c=component_count(sub)
        if all(component_count(sub[:i]+sub[i+1:])>c for i in range(k)):
            ans.append(sum(1<<x for x in sub))
    return ans

def perm_mask(mask,mapping):
    return sum(1<<mapping[s] for s in range(20) if mask>>s&1)

def orbit_reps(masks):
    remaining=set(masks)
    out=[]
    allm=set(masks)
    while remaining:
        rep=min(remaining)
        orbit={perm_mask(rep,p) for p in maps}
        assert orbit<=allm
        remaining-=orbit
        out.append((rep,len(orbit)))
    assert sum(z for _,z in out)==len(allm)
    return out

# Integer variables: x[s,e] for 60 event-edge allocations, y[v] for 15 half-degrees.
A=np.zeros((35,75))
for s in range(20):
    for k,(u,v) in enumerate(E[s]):
        A[s,3*s+k]=1
        A[20+u,3*s+k]=1
        A[20+v,3*s+k]=1
for v in range(15):A[20+v,60+v]=-2

def verify(counts,missing,x):
    # Separate exact integer witness verifier, independent of optimization reports.
    assert len(x)==60 and all(isinstance(q,int) and 0<=q<=3 for q in x)
    missing=set(missing);degree=[0]*15;graph=[set() for _ in range(15)]
    for s in range(20):
        assert sum(x[3*s:3*s+3])==counts[s]
        for k,(u,v) in enumerate(E[s]):
            q=x[3*s+k]
            if q:
                assert u not in missing and v not in missing
                degree[u]+=q;degree[v]+=q
                graph[u].add(v);graph[v].add(u)
    active=set(range(15))-missing
    assert active and all(degree[v]>0 and degree[v]%2==0 for v in active)
    assert all(degree[v]==0 for v in missing)
    seen={min(active)};todo=list(seen)
    for u in todo:
        for v in graph[u]:
            if v not in seen:seen.add(v);todo.append(v)
    assert seen==active
    return True

def construct(counts,missing):
    missing=set(missing)
    lower=np.zeros(75);upper=np.full(75,np.inf)
    for s in range(20):
        for k,(u,v) in enumerate(E[s]):
            upper[3*s+k]=counts[s] if u not in missing and v not in missing else 0
    for v in range(15):
        if v in missing:upper[60+v]=0
        else:lower[60+v]=1
    b=np.r_[counts,np.zeros(15)]
    constraints=[LinearConstraint(A,b,b)]
    objective=np.r_[np.random.default_rng(0).uniform(-1,1,60),np.zeros(15)]
    cuts=set()
    for iteration in range(32):
        sol=milp(objective,integrality=np.ones(75),bounds=Bounds(lower,upper),
                 constraints=constraints,options={'time_limit':1.0,'mip_rel_gap':0.0})
        if sol.x is None:raise RuntimeError(f'No candidate: {sol.status}: {sol.message}')
        raw=sol.x[:60];rounded=np.rint(raw)
        assert max(abs(raw-rounded))<1e-5
        x=[int(q) for q in rounded]
        assert all(sum(x[3*s:3*s+3])==counts[s] for s in range(20))
        degree=[0]*15;graph=[set() for _ in range(15)]
        for s in range(20):
            for k,(u,v) in enumerate(E[s]):
                q=x[3*s+k]
                if q:
                    assert u not in missing and v not in missing
                    degree[u]+=q;degree[v]+=q
                    graph[u].add(v);graph[v].add(u)
        active=set(range(15))-missing
        assert all(degree[v]>=2 and degree[v]%2==0 for v in active)
        assert all(degree[v]==0 for v in missing)
        unseen=set(active);parts=[]
        while unseen:
            seen={min(unseen)};todo=list(seen)
            for u in todo:
                for v in graph[u]:
                    if v not in seen:seen.add(v);todo.append(v)
            parts.append(seen);unseen-=seen
        if len(parts)==1:
            verify(counts,missing,x)
            return x
        for part in parts:
            complement=active-part
            if not complement:continue
            key=min(sum(1<<x for x in part),sum(1<<x for x in complement))
            if key in cuts:continue
            cuts.add(key)
            row=np.zeros(75)
            for s in range(20):
                for k,(u,v) in enumerate(E[s]):
                    if (u in part)!=(v in part):row[3*s+k]=1
            constraints.append(LinearConstraint(row,1,np.inf))
    raise RuntimeError('Connectivity-cut iteration exhausted')

def cases(rep8,rep9,star):
    # Terminal length 48: (triple,single,absent)=(8,0,0),(9,1,0),(10,2,0),(10,0,1).
    for family,_ in rep8:
        j=next(s for s in range(20) if family>>s&1)
        base=[3 if family>>s&1 else 2 for s in range(20)]
        for m in M:
            n=base.copy();n[j]=1
            yield 'eight_triples',m,n
    for family,_ in rep9:
        j=next(s for s in range(20) if family>>s&1)
        base=[3 if family>>s&1 else 2 for s in range(20)]
        for lone in range(20):
            if family>>lone&1:continue
            for m in M:
                n=base.copy();n[j]=1;n[lone]=1
                yield 'nine_triples_one_single',m,n
    j=next(s for s in range(20) if star>>s&1)
    base=[3 if star>>s&1 else 2 for s in range(20)]
    others=[s for s in range(20) if not star>>s&1]
    for a,b in combinations(others,2):
        for m in M:
            n=base.copy();n[j]=1;n[a]=1;n[b]=1
            yield 'ten_triples_two_single',m,n
    # Fully active axis-star triangles cover all 15 ports: no inactive port is possible.
    for omitted in others:
        n=base.copy();n[j]=1;n[omitted]=0
        yield 'ten_triples_one_absent',(),n

def main():
    start=int(sys.argv[1]) if len(sys.argv)>1 else 0
    end=int(sys.argv[2]) if len(sys.argv)>2 else 6318
    assert 0<=start<end<=6318
    t0=time.monotonic()
    e8=essential(8);e9=essential(9);e10=essential(10)
    o8=orbit_reps(e8)
    o9=[(967489,180),(971528,60)] # R762IT representative supports.
    assert len(e8)==4920 and len(o8)==16
    assert len(e9)==240 and set(e9)==set().union(*(
        {perm_mask(rep,perm) for perm in maps} for rep,_ in o9))
    star=sum(1<<s for s,t in enumerate(T) if 0 in t)
    assert len(e10)==6 and set(e10)=={
        sum(1<<s for s,t in enumerate(T) if a in t) for a in range(6)}
    count=Counter();digest=sha256()
    for i,(kind,missing,n) in enumerate(cases(o8,o9,star)):
        if not start<=i<end:continue
        x=construct(n,missing)
        assert sum(n)==46 and verify(n,missing,x)
        count[kind]+=1
        digest.update(bytes(n));digest.update(bytes(missing));digest.update(bytes(x))
    assert sum(count.values())==end-start
    if (start,end)==(0,6318):
        assert dict(count)=={'eight_triples':1216,
           'nine_triples_one_single':1672,
           'ten_triples_two_single':3420,
           'ten_triples_one_absent':10}
    print(json.dumps({'status':'PASS R762IU','range':[start,end],
       'essential_8':len(e8),'orbit_8':o8,'essential_9':len(e9),
       'essential_10':len(e10),'counts':dict(count),
       'total_checked':sum(count.values()),
       'witness_sha256':digest.hexdigest(),
       'elapsed_seconds':round(time.monotonic()-t0,2)},sort_keys=True))
if __name__=='__main__':main()
