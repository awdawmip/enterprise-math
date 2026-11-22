#!/usr/bin/env python3
"""Reproduce R762JL t4d16 44-to-42 exact Port-Euler integer witnesses.

Requires NumPy and SciPy (HiGHS MILP). Standard-library verifier is separate.
Usage: python PORT44_T4D16_GENERATE.py PORT44_T4D16_CERTS.b64
"""
from itertools import combinations, permutations
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix
import time,lzma,base64,sys

P=list(combinations(range(6),2)); S=list(combinations(range(6),3))
port_index={p:i for i,p in enumerate(P)}
support_index={s:i for i,s in enumerate(S)}
T=[tuple(port_index[p] for p in combinations(s,2)) for s in S]
E=[list(combinations(t,2)) for t in T]
PERM=[tuple(support_index[tuple(sorted(q[a] for a in s))] for s in S)
      for q in permutations(range(6))]
A=lil_matrix((35,75),dtype=float)
for s in range(20):
    for k,(u,v) in enumerate(E[s]):
        A[s,3*s+k]=1
        A[20+u,3*s+k]=1
        A[20+v,3*s+k]=1
for u in range(15):
    A[20+u,60+u]=-2
A=A.tocsr()

def comps(alloc,active):
    graph={v:set() for v in active}
    for s in range(20):
        for k,(u,v) in enumerate(E[s]):
            if alloc[3*s+k]:
                graph[u].add(v); graph[v].add(u)
    unseen=set(active); parts=[]
    while unseen:
        p={min(unseen)}; todo=list(p); unseen-=p
        for u in todo:
            for v in graph[u]&unseen:
                unseen.remove(v); p.add(v); todo.append(v)
        parts.append(p)
    return parts

def verify(alloc,count,inactive):
    assert len(alloc)==60 and sum(alloc)==42
    assert all(type(v) is int and 0<=v<=3 for v in alloc)
    deg=[0]*15
    for s in range(20):
        assert sum(alloc[3*s:3*s+3])==count[s]
        for k,(u,v) in enumerate(E[s]):
            deg[u]+=alloc[3*s+k]
            deg[v]+=alloc[3*s+k]
    assert all((d==0 if i in inactive else d>=2 and d%2==0)
               for i,d in enumerate(deg))
    assert len(comps(alloc,set(range(15))-set(inactive)))==1

def propose(count,inactive):
    active=set(range(15))-set(inactive)
    upper=[count[s] if all(v in active for v in E[s][k]) else 0
           for s in range(20) for k in range(3)]
    upper += [0 if i in inactive else 21 for i in range(15)]
    lower=[0]*60+[0 if i in inactive else 1 for i in range(15)]
    eq=LinearConstraint(A,count+[0]*15,count+[0]*15)
    cuts=[]
    for _ in range(10):
        r=milp(np.zeros(75),integrality=np.ones(75),
               bounds=Bounds(lower,upper),constraints=[eq]+cuts,
               options={'time_limit':3})
        if r.x is None:
            return None
        alloc=[int(round(float(v))) for v in r.x[:60]]
        parts=comps(alloc,active)
        if len(parts)==1:
            verify(alloc,count,inactive)
            return alloc
        for part in parts:
            cut=np.zeros(75)
            for s in range(20):
                for k,(u,v) in enumerate(E[s]):
                    if (u in part)!=(v in part):
                        cut[3*s+k]=1
            cuts.append(LinearConstraint(cut,1,np.inf))
    return None

unseen={sum(1<<s for s in ss) for ss in combinations(range(20),4)}
reps=[]
while unseen:
    m=min(unseen)
    orbit={sum(1<<q[s] for s in range(20) if m>>s&1) for q in PERM}
    assert orbit<=unseen
    reps.append((m,len(orbit)))
    unseen-=orbit
matchings=[m for k in range(4) for m in combinations(range(15),k)
           if len({a for i in m for a in P[i]})==2*k]
assert len(reps)==21 and sum(o for _,o in reps)==4845
assert len(matchings)==76
start=time.time()
data=bytearray()
for i,(mask,orbit) in enumerate(reps):
    triples=[s for s in range(20) if mask>>s&1]
    for inactive in matchings:
        for j in triples:
            count=[2+(s in triples)-2*(s==j) for s in range(20)]
            allocation=propose(count,inactive)
            if allocation is not None:
                break
        else:
            raise AssertionError((i,triples,inactive))
        data.append(j)
        for k in range(0,60,4):
            a,b,c,d=allocation[k:k+4]
            data.append(a|(b<<2)|(c<<4)|(d<<6))
    print('orbit',i+1,'of',len(reps),'size',orbit,flush=True)
assert len(data)==16*1596
out=sys.argv[1] if len(sys.argv)>1 else 'PORT44_T4D16_CERTS.b64'
with open(out,'w',encoding='ascii') as f:
    f.write(base64.b64encode(lzma.compress(data,preset=9)).decode('ascii')+'\n')
print('PASS: 1596/1596 certificate constructions; 368220 labelled pairs',
      'seconds=',round(time.time()-start,3),flush=True)
