#!/usr/bin/env python3
"""Optional SciPy/HiGHS candidate generator for 66,375 matching certificates.
Run: python R762JO_MATCHING_GENERATE.py R762JO_MATCHING_CERTS.b64
Requires scipy, numpy; proof uses separate R762JO_INDEPENDENT_VERIFY.py.
Can resume from <output>.raw. Full run evaluates all 885*75 configurations.
"""
import base64, itertools, lzma, os, sys
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix
from R762JO_INDEPENDENT_VERIFY import ports, supports, edges, z, reps, inactive_sets, kind, check

A=lil_matrix((35,75),dtype=float)
for s in range(20):
    for k,(u,v) in enumerate(edges[s]):
        A[s,3*s+k]=1
        A[20+u,3*s+k]=1
        A[20+v,3*s+k]=1
for u in range(15):A[20+u,60+u]=-2
A=A.tocsr()

def components(a,active):
    nbr={u:set() for u in active}
    for s in range(20):
        for k,(u,v) in enumerate(edges[s]):
            if a[3*s+k]:nbr[u].add(v);nbr[v].add(u)
    comps=[]
    unseen=set(active)
    while unseen:
        stack=[next(iter(unseen))]
        comp=set()
        while stack:
            u=stack.pop()
            if u in comp:continue
            comp.add(u);unseen.discard(u)
            stack.extend(nbr[u]-comp)
        comps.append(comp)
    return comps

def candidate(counts,M):
    active=set(range(15))-set(M)
    lower=[0]*60+[0 if u in M else 1 for u in range(15)]
    upper=[counts[s] if u in active and v in active else 0
           for s in range(20) for u,v in edges[s]] + [0 if u in M else 21 for u in range(15)]
    eq=LinearConstraint(A,counts+[0]*15,counts+[0]*15)
    cuts=[]
    for _ in range(8):
        res=milp(np.zeros(75), integrality=np.ones(75),bounds=Bounds(lower,upper),
                 constraints=[eq]+cuts,options={'time_limit':1.2})
        if res.x is None:return None
        a=[int(round(x)) for x in res.x[:60]]
        parts=components(a,active)
        if len(parts)==1:return a
        for part in parts:
            cut=np.zeros(75)
            for s in range(20):
                for k,(u,v) in enumerate(edges[s]):
                    if (u in part)!=(v in part):cut[3*s+k]=1
            cuts.append(LinearConstraint(cut,1,np.inf))
    return None

def record(j,a):
    out=bytearray([j])
    for k in range(0,60,4):
        out.append(sum(a[k+h] << (2*h) for h in range(4)))
    assert len(out)==16
    return bytes(out)

def main(target):
    R=reps()
    Ms=[M for M in inactive_sets() if kind(M)=='matching']
    assert len(R)==885 and len(Ms)==75
    raw_path=target+'.raw'
    raw=bytearray(open(raw_path,'rb').read()) if os.path.exists(raw_path) else bytearray()
    assert len(raw)%16==0
    total=len(R)*len(Ms)
    done=len(raw)//16
    for ix in range(done,total):
        i,k=divmod(ix,len(Ms))
        T,_=R[i]
        M=Ms[k]
        for j in T:
            counts=[0 if s==z else 2+int(s in T)-2*int(s==j) for s in range(20)]
            alloc=candidate(counts,M)
            if alloc is not None:
                cert=record(j,alloc)
                check(T,M,cert)
                raw.extend(cert)
                break
        else:
            with open(raw_path,'wb') as f:f.write(raw)
            raise RuntimeError(f'Unresolved finite instance: orbit={i}, inactive-index={k}')
        if (ix+1)%750==0 or ix+1==total:
            with open(raw_path,'wb') as f:f.write(raw)
            print('checked',ix+1,'/',total,flush=True)
    with open(target,'wt',encoding='ascii') as f:
        f.write(base64.b64encode(lzma.compress(bytes(raw),preset=6)).decode('ascii')+'\n')
    print('COMPLETE:',total,'verified exact proposals',flush=True)

if __name__=='__main__':main(sys.argv[1])
