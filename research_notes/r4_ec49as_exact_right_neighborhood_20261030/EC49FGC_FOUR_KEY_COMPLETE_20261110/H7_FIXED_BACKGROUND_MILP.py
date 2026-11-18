#!/usr/bin/env python3
"""Independent exact H7-low fixed-background word/prefix MILP for original
24-label mother-signature pattern. Frozen science: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Requires SciPy/NumPy; outputs a complete mathematical witness and MILP optimum."""
from collections import defaultdict
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix
from VERIFY_EC49FGC import STEPS,T,OPS,SIG
import numpy as np
import json
FIX={
 2:{16:'fe',32:'ge'},
 3:{16:'feg',32:'gef'},
 4:{1:'gefd',2:'fegd',4:'cefg',8:'gefc'},
 5:{16:'feggf',32:'geffg'},
 6:{1:'gefdfg',2:'fegdgf',4:'feggfc',8:'geffgc'},
 8:{1:'geffgfgd',2:'feggffgd',4:'feggfcfg',8:'geffgcgf'},
 9:{16:'feggffggf',32:'geffgfggf'}
}
def native(word):
    return tuple(s for ch in word for s in STEPS[ch])
def signature(word):
    q=0
    for ch in word:q=T[q][OPS.index(ch)]
    return SIG[q]
def prefix_union(words):
    P=set()
    for w in words:
        st=native(w)
        P.update(st[:i] for i in range(1,len(st)+1))
    return P

def run(time_limit=60):
    baseline=prefix_union(w for group in FIX.values() for w in group.values())
    assert len(baseline)==89
    pool={s:[] for s in (1,2,4,8)}
    for c in range(3):
        rem={'c':c,'d':2-c,'e':1,'f':2,'g':2}
        def walk(word,q):
            if len(word)==7:
                if SIG[q] in pool:pool[SIG[q]].append(word)
                return
            for ch in 'cdefg':
                if rem[ch]:
                    q2=T[q][OPS.index(ch)]
                    if q2==8:continue
                    rem[ch]-=1
                    walk(word+ch,q2)
                    rem[ch]+=1
        walk('',0)
    assert {s:len(v) for s,v in pool.items()}=={1:360,2:270,4:360,8:270}
    words=[];demands={};prefixes={}
    for s in (1,2,4,8):
        demands[s]=[]
        for w in pool[s]:
            j=len(words);words.append(w);demands[s].append(j)
            st=native(w)
            for i in range(1,len(st)+1):
                p=st[:i]
                if p not in baseline and p not in prefixes:
                    prefixes[p]=len(prefixes)
    n=len(words);m=len(prefixes)
    row=[];col=[];val=[];lb=[];ub=[]
    for s in (1,2,4,8):
        r=len(lb)
        for j in demands[s]:row.append(r);col.append(j);val.append(1)
        lb.append(1);ub.append(np.inf)
    for j,w in enumerate(words):
        st=native(w)
        for i in range(1,len(st)+1):
            p=st[:i]
            if p in baseline:continue
            r=len(lb)
            row.extend([r,r]);col.extend([j,n+prefixes[p]]);val.extend([1,-1])
            lb.append(-np.inf);ub.append(0)
    A=coo_matrix((np.asarray(val,dtype=float),(np.asarray(row),np.asarray(col))),
                 shape=(len(lb),n+m)).tocsr()
    result=milp(c=np.r_[np.zeros(n),np.ones(m)],
        integrality=np.ones(n+m),bounds=Bounds(np.zeros(n+m),np.ones(n+m)),
        constraints=LinearConstraint(A,np.asarray(lb),np.asarray(ub)),
        options={'time_limit':time_limit,'mip_rel_gap':0})
    assert result.status==0 and abs(result.fun-15)<1e-6
    assert abs(result.mip_dual_bound-15)<1e-6 and result.mip_gap<=1e-6
    chosen={s:next(words[j] for j in demands[s] if result.x[j]>.5) for s in (1,2,4,8)}
    assert all(signature(w)==s for s,w in chosen.items())
    assert len(prefix_union([w for group in FIX.values() for w in group.values()]+list(chosen.values())))==104
    return {'status':'OPTIMAL','baseline_prefixes':len(baseline),
       'new_edges':round(result.fun),'total_native_prefixes':104,
       'objective':result.fun,'dual':result.mip_dual_bound,'gap':result.mip_gap,
       'eligible_words':n,'new_prefix_variables':m,'constraints':len(lb),
       'candidates_per_signature':{str(k):len(v) for k,v in pool.items()},
       'H7_key':[6,4,1],'H7_witness':chosen}
if __name__=='__main__':
    print(json.dumps(run(),indent=2))
