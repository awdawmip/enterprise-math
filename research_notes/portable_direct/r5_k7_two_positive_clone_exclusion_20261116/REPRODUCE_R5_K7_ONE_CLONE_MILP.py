#!/usr/bin/env python3
"""Exact Boolean modeling, numerical MILP probe for k=7 two positive actions, one duplicated output label.
This does NOT certify infeasibility independently of SciPy/HiGHS.
"""
import argparse, json, time
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix
K=7; X=range(1<<K); Q=lambda u:sum(((u>>i)&1)*((u>>((i+1)%K))&1) for i in range(K))
F={r:frozenset(u for u in X if (u&~r)==0 and 0<=Q(r)-Q(u)<=2) for r in X}
C=tuple(r for r in X if not any(F[r]<F[t] for t in X))
assert len(C)==57

def test(duplicate, time_limit=30):
    assert duplicate in C
    labels=list(C)+[duplicate]; S=range(len(labels)); m=len(labels)
    Fpos=[F[r] for r in labels]
    cols=[]; rows=[]; data=[]; lo=[]; hi=[]; vi={}; count=0
    def var(key):
        nonlocal count
        if key not in vi:
            vi[key]=count;count+=1
        return vi[key]
    def row(terms,l=-np.inf,h=np.inf):
        i=len(lo);lo.append(l);hi.append(h)
        for key,val in terms:
            cols.append(var(key));rows.append(i);data.append(val)
    for s in S: var(('x',s))
    for s in S:
        for a in range(2):
            for t in S:
                var(('y',s,a,t))
    for u in X:
        for s in S:
            if u in Fpos[s]:var(('z',u,s))
    assert count==len(vi)
    # fixed duplicate slot on; exactly 18 states; distinct labels 17.
    row([(('x',s),1) for s in S],18,18)
    row([(('x',m-1),1)],1,1)
    row([(('x',m-1),1),(('x',C.index(duplicate)),-1)],-np.inf,0)
    for u in X:
        row([(('z',u,s),1) for s in S if u in Fpos[s]],1,np.inf)
        for s in S:
            if u not in Fpos[s]:continue
            row([(('z',u,s),1),(('x',s),-1)],-np.inf,0)
            for a in range(2):
                v=u|(1<<a)
                terms=[(('z',u,s),1)] + [(('y',s,a,t),-1) for t in S if v in Fpos[t]]
                row(terms,-np.inf,0)
    for s in S:
        for a in range(2):
            row([(('y',s,a,t),1) for t in S] + [(('x',s),-1)],0,0)
            for t in S:row([(('y',s,a,t),1),(('x',t),-1)],-np.inf,0)
    nrows=len(lo);A=coo_matrix((data,(rows,cols)),shape=(nrows,count)).tocsr()
    start=time.time();res=milp(c=np.zeros(count),integrality=np.ones(count),bounds=Bounds(0,1),constraints=LinearConstraint(A,np.array(lo),np.array(hi)),options={'time_limit':time_limit,'mip_rel_gap':0})
    out=dict(duplicate=duplicate,center_candidates=len(C),variables=count,constraints=nrows,nonzeros=A.nnz,
             status=res.status,message=res.message,elapsed=round(time.time()-start,3),gap=getattr(res,'mip_gap',None))
    if res.x is not None:
        active=[s for s in S if res.x[vi[('x',s)]]>0.5]
        states=[labels[s] for s in active]
        succ={str(s):[next(t for t in active if res.x[vi[('y',s,a,t)]]>.5) for a in range(2)] for s in active}
        valid={u:[s for s in active if u in Fpos[s] and res.x[vi[('z',u,s)]]>.5] for u in X}
        assert len(active)==18 and len(set(states))==17 and all(valid.values())
        for u in X:
            for s in valid[u]:
                assert all((u|(1<<a)) in Fpos[succ[str(s)][a]] for a in (0,1))
        out.update(active_state_indices=active,labels=states,succ=succ,certificate='EXACT_ONE_STEP_DIRECT_RECHECK')
    return out

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--duplicate',type=int,default=127);ap.add_argument('--time',type=float,default=40);ap.add_argument('--all-orbits',action='store_true');args=ap.parse_args()
    if args.all_orbits:
        flip=lambda r:sum(((r>>i)&1)<<((1-i)%K) for i in range(K))
        reps=sorted({min(r,flip(r)) for r in C})
        assert len(reps)==32 and {z for r in reps for z in (r,flip(r))}==set(C)
        results=[test(r,args.time) for r in reps]
        print(json.dumps({'reflection_orbit_representatives':reps,'results':results},indent=2))
    else:
        print(json.dumps(test(args.duplicate,args.time),indent=2))
