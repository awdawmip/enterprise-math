#!/usr/bin/env python3
"""Independent word-selector MILP and exact native-X6 witness checks for EC49FGC.
Reproduces the best case without relying on previously saved solver arrays.
Frozen scientific input fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
from VERIFY_EC49FGC import BASE,PROFILE,SIGS,STEPS,OPS,T,SIG,by_key
from collections import Counter,defaultdict
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix
import numpy as np
KEYS=((4,2,1),(5,3,1),(6,4,1))
WITNESS={
 (2,1):'de',(2,2):'ed',(2,4):'ce',(2,8):'ec',
 (3,16):'feg',(3,32):'gef',
 (4,1):'gefd',(4,2):'fegd',(4,4):'cefg',(4,8):'gefc',
 (5,16):'feggf',(5,32):'geffg',
 (6,1):'gefdfg',(6,2):'fegdgf',(6,4):'feggfc',(6,8):'geffgc',
 (7,16):'feggffg',(7,32):'geffgfg',
 (8,1):'geffgfgd',(8,2):'feggffgd',(8,4):'feggfcfg',(8,8):'geffgcgf',
 (9,16):'feggffggf',(9,32):'geffgfggf'
}
def key(w):
    h=len(w);cnt=Counter(w)
    assert cnt['e']==cnt['a']+1
    return (h+1-cnt['g'],h+1-2*cnt['e']-cnt['f'],cnt['e'])
def signature(w):
    state=0
    for c in w:state=T[state][OPS.index(c)]
    return SIG[state]
def native(w):
    return tuple(s for c in w for s in STEPS[c])
def audit_witness():
    prefixes=set()
    keys=set()
    for (h,s),w in WITNESS.items():
        assert len(w)==h and signature(w)==s
        k=key(w)
        assert min(k)>0
        assert k == ((3,1,1) if h<=3 else KEYS[(h-4)//2])
        n=native(w)
        assert tuple(n.count(i)-n.count(-i) for i in range(1,7))==(2,0,0,0,0,0)
        prefixes.update(n[:j] for j in range(1,len(n)+1))
        keys.add(k)
    assert len(WITNESS)==24 and len(keys)==4 and len(prefixes)==108
    return len(prefixes)

def independent_word_milp(keys=KEYS,time_limit=60):
    """Word binaries y_j; prefix binaries x_p; add y_j <= x_p for every prefix on word j."""
    pool={k:[v] for k,v in BASE.items()}
    for h in range(4,10):
        for label in SIGS[PROFILE[h]]:
            pool[h,label]=by_key(h,PROFILE[h],keys[(h-4)//2])[label]
    allwords=[];labels=defaultdict(list);prefixes={}
    for (h,label),options in sorted(pool.items()):
        for w in options:
            i=len(allwords);allwords.append(w);labels[h,label].append(i)
            n=native(w)
            for j in range(1,len(n)+1):
                p=n[:j]
                if p not in prefixes:prefixes[p]=len(prefixes)
    m=len(allwords);n=len(prefixes)
    rr=[];cc=[];vv=[];lo=[];hi=[]
    for _,choices in sorted(labels.items()):
        row=len(lo)
        for i in choices:rr.append(row);cc.append(i);vv.append(1)
        lo.append(1);hi.append(np.inf)
    for i,w in enumerate(allwords):
        v=native(w)
        for j in range(1,len(v)+1):
            row=len(lo)
            rr.extend([row,row]);cc.extend([i,m+prefixes[v[:j]]]);vv.extend([1,-1])
            lo.append(-np.inf);hi.append(0)
    a=coo_matrix((np.asarray(vv,dtype=float),(np.asarray(rr),np.asarray(cc))),
        shape=(len(lo),m+n)).tocsr()
    out=milp(c=np.r_[np.zeros(m),np.ones(n)],integrality=np.ones(m+n),
        bounds=Bounds(np.zeros(m+n),np.ones(m+n)),
        constraints=LinearConstraint(a,np.asarray(lo),np.asarray(hi)),
        options={'time_limit':time_limit,'mip_rel_gap':0.0})
    return {'status':int(out.status),'primal':out.fun,'dual':out.mip_dual_bound,
       'gap':out.mip_gap,'word_variables':m,'prefix_variables':n,'constraints':len(lo)}
if __name__=='__main__':
    import json
    witness=audit_witness()
    audit=independent_word_milp()
    assert audit['status']==0 and audit['gap']<=1e-6
    assert abs(audit['primal']-108)<1e-5 and abs(audit['dual']-108)<1e-5
    assert audit['word_variables']==3358 and audit['prefix_variables']==18742
    assert audit['constraints']==64616
    print(json.dumps({'result':'PASS','witness_prefixes':witness,
        'independent_integer_program':audit},indent=2))
