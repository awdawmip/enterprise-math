"""Independent EC49FFP binary-prefix-closure exact MIP checks (SciPy HiGHS).
Run after VERIFY_EC49FFP_COMPACT.py, which exposes the original model.
No dependency on the trie DP outputs: only its candidate generator is shared.
"""
from collections import Counter
import json
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
from VERIFY_EC49FFP_COMPACT import original_words,OPS

CASES=[((3,4),(4,2,1),56),((4,5),(4,3,1),62),
       ((4,5),(5,2,1),62),((4,5),(5,3,1),72),
       ((5,6),(5,3,1),60)]

def check(horizons,key,expected):
    needs=tuple((h,s) for h in horizons for s in (1,2,4,8))
    prefixes={():-1};parents=[];terminal=[];counts=Counter()
    for h in horizons:
        for word,s in original_words(h,key):
            seq=tuple(step for op in word for step in OPS[op])
            counts[h]+=1;pr=()
            for j in range(1,len(seq)+1):
                nxt=seq[:j]
                if nxt not in prefixes:
                    prefixes[nxt]=len(parents)
                    parents.append(prefixes[pr]);terminal.append(0)
                pr=nxt
            terminal[prefixes[pr]] |=1<<needs.index((h,s))
    n=len(parents);matrix=lil_matrix((n+8,n),dtype=np.float64)
    lower=np.zeros(n+8);upper=np.full(n+8,np.inf)
    for i,p in enumerate(parents):
        if p>=0:
            matrix[i,p]=1;matrix[i,i]=-1
    for i,m in enumerate(terminal):
        for j in range(8):
            if m&(1<<j):matrix[n+j,i]=1
    lower[n:]=1
    result=milp(c=np.ones(n),integrality=np.ones(n),
        bounds=Bounds(0,1),
        constraints=LinearConstraint(matrix.tocsr(),lower,upper),
        options={'mip_rel_gap':0,'time_limit':150})
    assert result.status==0,(key,result.message)
    assert abs(result.fun-expected)<1e-6 and abs(result.mip_dual_bound-expected)<1e-6,(key,result.fun,result.mip_dual_bound)
    assert result.mip_gap==0
    return {'horizons':list(horizons),'key':list(key),'optimum':expected,
            'model_prefix_variables':n,'candidate_words':dict(counts),
            'mip_status':result.status,'dual_bound':result.mip_dual_bound,
            'mip_gap':result.mip_gap}

if __name__=='__main__':
    reports=[check(*case) for case in CASES]
    print(json.dumps({'status':'INDEPENDENT_MIP_OPTIMAL_PASS','rows':reports},indent=2))
