#!/usr/bin/env python3
"""R762IV exact finite 47->45 Port-Euler certificates.
Usage: python R762IV_SEVEN_TRIPLE_CHECK.py full-active
       python R762IV_SEVEN_TRIPLE_CHECK.py essential 0
       python R762IV_SEVEN_TRIPLE_CHECK.py essential 1
       python R762IV_SEVEN_TRIPLE_CHECK.py essential 2
       python R762IV_SEVEN_TRIPLE_CHECK.py essential 3
SciPy/HiGHS supplies candidates; the final acceptance is exact integer verification.
"""
import sys, json, time, hashlib
from itertools import combinations
from collections import Counter
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint

AX=tuple(range(6))
PORT=list(combinations(AX,2))
TRI=list(combinations(AX,3))
pi={p:i for i,p in enumerate(PORT)}
ti={t:i for i,t in enumerate(TRI)}
V=[tuple(pi[p] for p in combinations(t,2)) for t in TRI]
ED=[list(combinations(v,2)) for v in V]
M=[m for k in range(4) for m in combinations(range(15),k)
   if len({a for v in m for a in PORT[v]})==2*k]
assert len(M)==76

# Five adjacent transpositions generate the full S6 action.
GENERATORS=[]
for a in range(5):
    perm=list(AX)
    perm[a],perm[a+1]=perm[a+1],perm[a]
    GENERATORS.append(tuple(ti[tuple(sorted(perm[x] for x in t))]
                            for t in TRI))

def permute_mask(mask,mapping):
    out=0
    while mask:
        bit=mask&-mask;mask-=bit
        out|=1<<mapping[bit.bit_length()-1]
    return out

def all_orbits(k):
    seen=set();reps=[]
    for c in combinations(range(20),k):
        mask=sum(1<<j for j in c)
        if mask in seen:continue
        orbit={mask};stack=[mask];seen.add(mask)
        for current in stack:
            for g in GENERATORS:
                nxt=permute_mask(current,g)
                if nxt not in orbit:
                    orbit.add(nxt);stack.append(nxt);seen.add(nxt)
        reps.append((min(orbit),len(orbit)))
    return sorted(reps)

def comp_count(sub):
    parent=list(range(15))
    def root(v):
        while parent[v]!=v:
            parent[v]=parent[parent[v]]
            v=parent[v]
        return v
    for s in sub:
        a,b,c=V[s]
        parent[root(a)]=root(b)
        parent[root(a)]=root(c)
    return len({root(v) for v in range(15)})

def essential(mask):
    sub=tuple(s for s in range(20) if mask>>s&1)
    c=comp_count(sub)
    return all(comp_count(sub[:i]+sub[i+1:])>c for i in range(7))

A=np.zeros((35,75))
for s in range(20):
    for j,(u,v) in enumerate(ED[s]):
        A[s,3*s+j]=1
        A[20+u,3*s+j]=1
        A[20+v,3*s+j]=1
for v in range(15):A[20+v,60+v]=-2

def exact_verify(counts,inactive,x):
    assert len(x)==60 and all(isinstance(a,int) and 0<=a<=3 for a in x)
    inactive=set(inactive);degree=[0]*15;graph=[set() for _ in range(15)]
    for s in range(20):
        assert sum(x[3*s:3*s+3])==counts[s]
        for j,(u,v) in enumerate(ED[s]):
            k=x[3*s+j]
            if k:
                assert u not in inactive and v not in inactive
                degree[u]+=k;degree[v]+=k
                graph[u].add(v);graph[v].add(u)
    active=set(range(15))-inactive
    assert active
    assert all(degree[v]>=2 and degree[v]%2==0 for v in active)
    assert all(degree[v]==0 for v in inactive)
    seen={min(active)};queue=list(seen)
    for u in queue:
        for v in graph[u]:
            if v not in seen:seen.add(v);queue.append(v)
    assert seen==active
    return True

def construct(n,inactive):
    inactive=set(inactive);lo=np.zeros(75);hi=np.full(75,np.inf)
    for s in range(20):
        for j,(u,v) in enumerate(ED[s]):
            hi[3*s+j]=n[s] if u not in inactive and v not in inactive else 0
    for v in range(15):
        if v in inactive:hi[60+v]=0
        else:lo[60+v]=1
    b=np.r_[n,np.zeros(15)]
    constraints=[LinearConstraint(A,b,b)]
    objective=np.r_[np.random.default_rng(150).uniform(-1,1,60),np.zeros(15)]
    cuts=set()
    for iteration in range(30):
        solution=milp(objective,integrality=np.ones(75),
                      bounds=Bounds(lo,hi),constraints=constraints,
                      options={'time_limit':0.3,'mip_rel_gap':0.0})
        if solution.x is None:
            raise RuntimeError(f'missing candidate iteration={iteration}, status={solution.status}')
        rounded=np.rint(solution.x[:60])
        assert max(abs(solution.x[:60]-rounded))<1e-5
        x=[int(a) for a in rounded]
        graph=[set() for _ in range(15)]
        for s in range(20):
            for j,(u,v) in enumerate(ED[s]):
                if x[3*s+j]:graph[u].add(v);graph[v].add(u)
        active=set(range(15))-inactive;unseen=active.copy();parts=[]
        while unseen:
            seen={min(unseen)};queue=list(seen)
            for u in queue:
                for v in graph[u]:
                    if v not in seen:seen.add(v);queue.append(v)
            unseen-=seen;parts.append(seen)
        if len(parts)==1:
            exact_verify(n,inactive,x)
            return x
        for part in parts:
            rest=active-part
            key=min(sum(1<<v for v in part),sum(1<<v for v in rest))
            if key in cuts:continue
            cuts.add(key)
            row=np.zeros(75)
            for s in range(20):
                for j,(u,v) in enumerate(ED[s]):
                    if (u in part)!=(v in part):row[3*s+j]=1
            constraints.append(LinearConstraint(row,1,np.inf))
    raise RuntimeError('Connectivity-cut iteration exhausted')

def main():
    mode=sys.argv[1]
    assert mode in ('full-active','essential')
    missing_size=int(sys.argv[2]) if mode=='essential' else 0
    assert 0<=missing_size<=3
    orbits=all_orbits(7)
    assert len(orbits)==161 and sum(n for _,n in orbits)==77520
    er=[(m,n) for m,n in orbits if essential(m)]
    assert len(er)==55 and sum(n for _,n in er)==23700
    reps=orbits if mode=='full-active' else er
    inactive_cases=[()] if mode=='full-active' else [m for m in M if len(m)==missing_size]
    t0=time.monotonic();digest=hashlib.sha256();count=0
    for rep,orbit_size in reps:
        j=next(s for s in range(20) if rep>>s&1)
        n=[3 if rep>>s&1 else 2 for s in range(20)]
        n[j]=1
        for inactive in inactive_cases:
            x=construct(n,inactive)
            assert sum(n)==45 and exact_verify(n,inactive,x)
            digest.update(bytes(n));digest.update(bytes(inactive));digest.update(bytes(x))
            count+=1
    expected=161 if mode=='full-active' else {0:55,1:825,2:2475,3:825}[missing_size]
    assert count==expected
    print(json.dumps({'result':'PASS R762IV','mode':mode,'missing_size':missing_size,
        'full_orbits':len(orbits),'full_masks':77520,'essential_orbits':len(er),
        'essential_masks':23700,'cases':count,'passed':count,
        'witness_stream_sha256':digest.hexdigest(),
        'seconds':round(time.monotonic()-t0,2)}))

if __name__=='__main__':main()
