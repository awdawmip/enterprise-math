#!/usr/bin/env python3
"""Regenerate R762JM 42-event exact witness archive (SciPy/HiGHS proposer).

Usage: python R762JM_GENERATE.py R762JM_CERTS.b64
Then use R762JM_VERIFY.py to check all resulting integer certificates.
"""
import base64
import lzma
import sys
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix
from R762JM_VERIFY import EDGES, pair_orbits, inactive_matchings, exact_check

A=lil_matrix((35,75),dtype=float)
for s in range(20):
    for k,(u,v) in enumerate(EDGES[s]):
        A[s,3*s+k]=1
        A[20+u,3*s+k]=1
        A[20+v,3*s+k]=1
for u in range(15):
    A[20+u,60+u]=-2
A=A.tocsr()

def components(alloc,active):
    graph={v:set() for v in active}
    for s in range(20):
        for k,(u,v) in enumerate(EDGES[s]):
            if alloc[3*s+k]:
                graph[u].add(v)
                graph[v].add(u)
    unseen=set(active)
    result=[]
    while unseen:
        stack=[min(unseen)]
        component=set()
        while stack:
            u=stack.pop()
            if u in component:
                continue
            component.add(u)
            unseen.discard(u)
            stack.extend(graph[u]-component)
        result.append(component)
    return result

def candidate(counts,inactive):
    active=set(range(15))-set(inactive)
    lower=[0]*60+[0 if u in inactive else 1 for u in range(15)]
    upper=[counts[s] if u in active and v in active else 0
           for s in range(20) for u,v in EDGES[s]] + [0 if u in inactive else 21 for u in range(15)]
    bounds=Bounds(lower,upper)
    eq=LinearConstraint(A,counts+[0]*15,counts+[0]*15)
    cuts=[]
    for iteration in range(8):
        result=milp(np.zeros(75),integrality=np.ones(75),bounds=bounds,
                    constraints=[eq]+cuts,options={'time_limit':1.2})
        if result.x is None:
            return None
        alloc=[int(round(float(v))) for v in result.x[:60]]
        parts=components(alloc,active)
        if len(parts)==1:
            return alloc
        for part in parts:
            cut=np.zeros(75)
            for s in range(20):
                for k,(u,v) in enumerate(EDGES[s]):
                    if (u in part)!=(v in part):
                        cut[3*s+k]=1
            cuts.append(LinearConstraint(cut,1,np.inf))
    return None

def main(path):
    reps=pair_orbits()
    matchings=inactive_matchings()
    packed=bytearray()
    for i,(T,l,_) in enumerate(reps):
        for M in matchings:
            for j in T:
                counts=[2+(s in T)-(s==l)-2*(s==j) for s in range(20)]
                alloc=candidate(counts,M)
                if alloc is not None:
                    exact_check(T,l,M,j,alloc)
                    packed.append(j)
                    for start in range(0,60,4):
                        packed.append(sum(alloc[start+k]<<(2*k) for k in range(4)))
                    break
            else:
                raise RuntimeError(f'No witnessed allocation at orbit {i}, singleton {l}, matching {M}')
        if (i+1)%25==0:
            print(f'Completed {i+1}/{len(reps)} orbits',flush=True)
    assert len(packed)==16*len(reps)*len(matchings)
    with open(path,'w',encoding='ascii') as f:
        f.write(base64.b64encode(lzma.compress(packed,preset=9)).decode('ascii')+'\n')
    print(f'Wrote {len(reps)*len(matchings)} exact certificates to {path}')

if __name__=='__main__':
    main(sys.argv[1])
