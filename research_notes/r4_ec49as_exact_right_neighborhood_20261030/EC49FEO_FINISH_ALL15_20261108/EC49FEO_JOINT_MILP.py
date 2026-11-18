"""Exact 0-1 joint native X6 signed-prefix optimization in one full five-BRC-key inventory.
Frozen pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Run with extracted EC49FEN model files:
 python EC49FEO_JOINT_MILP.py '[[3,1,1],[4,3,1],[4,4,1],[4,5,1],[4,6,1]]' 0 60 witness.json
Repeat for early variant 0..3 on eight exceptional orbit-representative inventories.
"""
import json,sys,time
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_array
from EC49FEJ_SIEVE import pool
from EC49FEJ_CONSTRUCT import native,prefixes,key,endpoint,sig
from EC49FEJ_DEPTH_FILTER2 import early_variants
HIGH=(3,6,7,8,9)

def solve(K,eidx=0,time_limit=60):
    early=early_variants()[eidx]
    free=frozenset().union(*(prefixes(w) for w in early))
    assert len(free)==42
    groups=[]
    for h in range(4,10):
        for s in ((16,32) if h in HIGH else (1,2,4,8)):
            ws=sorted(set(w for k in K for w,t in pool(h,k) if t==s))
            assert ws,(h,s)
            groups.append((h,s,ws))
    allwords=list(dict.fromkeys(w for h,s,ws in groups for w in ws))
    N={w:native(w) for w in allwords}
    allprefix=set().union(*(prefixes(w) for w in allwords))
    extras=sorted(allprefix-free,key=lambda p:(len(p),p))
    E={p:i for i,p in enumerate(extras)}
    W={w:i+len(E) for i,w in enumerate(allwords)}
    n=len(E)+len(W)
    objective=np.zeros(n);objective[:len(E)]=1
    ri=[];ci=[];data=[];lb=[];ub=[]
    def row(terms,lower,upper):
        r=len(lb);lb.append(lower);ub.append(upper)
        for col,val in terms:ri.append(r);ci.append(col);data.append(float(val))
    for h,s,ws in groups:
        row([(W[w],1) for w in ws],1,1)
    for w in allwords:
        row([(E[N[w]],1),(W[w],-1)],0,np.inf)
    for p,i in E.items():
        if len(p)>1 and p[:-1] not in free:
            assert p[:-1] in E
            row([(E[p[:-1]],1),(i,-1)],0,np.inf)
    mat=coo_array((np.asarray(data,dtype=float),
                   (np.asarray(ri,dtype=np.int32),np.asarray(ci,dtype=np.int32))),
                   shape=(len(lb),n)).tocsc()
    t=time.time()
    result=milp(objective,integrality=np.ones(n,dtype=np.int32),
                bounds=Bounds(np.zeros(n),np.ones(n)),
                constraints=[LinearConstraint(mat,np.asarray(lb),np.asarray(ub))],
                options={'time_limit':float(time_limit),'mip_rel_gap':0})
    out={'keys':K,'early_variant':eidx,
         'prefix_variables':len(E),'word_variables':len(W),'constraints':len(lb),
         'status':int(result.status),'message':str(result.message),
         'elapsed_sec':round(time.time()-t,2),
         'mip_gap':None if result.mip_gap is None else float(result.mip_gap),
         'dual_bound':None if result.mip_dual_bound is None else float(result.mip_dual_bound+42),
         'objective':None if result.fun is None else float(result.fun+42)}
    if result.x is not None:
        selected=list(early)
        win={2:list(early[:4]),3:list(early[4:])}
        for h,s,ws in groups:
            choice=[w for w in ws if result.x[W[w]]>0.5]
            assert len(choice)==1,(h,s,choice)
            selected.extend(choice)
            win.setdefault(h,[]).extend(choice)
        actual=set().union(*(prefixes(w) for w in selected))
        assert len(selected)==22 and len(actual)==round(result.fun)+42
        assert all(endpoint(w)==(2,0,0,0,0,0) and key(w) in K for w in selected)
        for h,ws in win.items():
            assert {sig(w) for w in ws}==set((16,32) if h in HIGH else (1,2,4,8))
        out['verified_cost']=len(actual)
        out['words_by_window']={str(h):ws for h,ws in win.items()}
    return out

if __name__=='__main__':
    K=tuple(tuple(x) for x in json.loads(sys.argv[1]))
    out=solve(K,int(sys.argv[2]),float(sys.argv[3]))
    print(json.dumps({k:v for k,v in out.items() if k!='words_by_window'},indent=2))
    with open(sys.argv[4],'w') as f:json.dump(out,f,indent=2)
