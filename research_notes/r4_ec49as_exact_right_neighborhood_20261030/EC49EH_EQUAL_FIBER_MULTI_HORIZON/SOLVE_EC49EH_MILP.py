#!/usr/bin/env python3
"""EC49EH: finite exact 0-1 prefix/rank model, solved with SciPy/HiGHS.
Requires numpy, scipy >=1.10 and VERIFY_EC49EH.py in the same directory.
MILP gap 0 is the solver's computational optimality report, not a formal proof trace.
"""
import json, sys
from collections import defaultdict
from time import perf_counter
import numpy as np
import scipy
from scipy.sparse import coo_matrix
from scipy.optimize import milp,Bounds,LinearConstraint
from VERIFY_EC49EH import (groups, transfer, native, counts, prefixes, columns,
                           rank_mod, det_witness, trie_cost)

BASE=('ce','de','ec','ed')
BASEPREFIX=set().union(*(prefixes(native(w)) for w in BASE))
assert len(BASEPREFIX)==28


def fullrank_type_subsets(type_columns):
    types=list(type_columns)
    valid=[]
    for mask in range(1,1<<len(types)):
        cc=[c for j,t in enumerate(types) if (mask>>j)&1 for c in type_columns[t]]
        if rank_mod(cc)<9:continue
        if any((mask & old)==old for old in valid): continue
        valid.append(mask)
    return [tuple(types[j] for j in range(len(types)) if (mask>>j)&1) for mask in valid]


def build(H):
    # All returning operation words in the frozen a..g grammar are enumerated.
    domains={}
    sizes={}
    for h in range(3,H+1):
        r=groups(h)
        sizes[h]=sum(map(len,r.values()))
        options=[]
        for fiber,ws in r.items():
            types=defaultdict(list)
            for w in ws:types[transfer(native(w))].append(w)
            if rank_mod([c for t in types for c in columns(t)])<9:continue
            masks=fullrank_type_subsets({t:columns(t) for t in types})
            for required in masks:
                options.append((fiber,required,types))
        domains[h]=options
    allpref=set(BASEPREFIX)
    for options in domains.values():
        for fiber,need,types in options:
            for words in types.values():
                for w in words:allpref.update(prefixes(native(w)))
    edge=sorted(allpref-BASEPREFIX,key=lambda x:(len(x),x))
    eid={p:i for i,p in enumerate(edge)}
    n_edges=len(edge)
    candidates=[]
    rows=[]; lb=[]; ub=[]
    for h,options in domains.items():
        group_ids=[]
        for fiber,required,types in options:
            opt_id=n_edges+len(candidates)
            candidates.append((h,fiber,required,types))
            group_ids.append(opt_id)
            for t in required:
                row={opt_id:-1}
                for w in types[t]:row[eid[native(w)]]=1
                rows.append(row);lb.append(0);ub.append(np.inf)
        assert group_ids
        rows.append({i:1 for i in group_ids});lb.append(1);ub.append(np.inf)
    for p,j in eid.items():
        parent=p[:-1]
        if not parent or parent in BASEPREFIX:continue
        rows.append({j:1,eid[parent]:-1});lb.append(-np.inf);ub.append(0)
    a_i=[];a_j=[];a_v=[]
    for i,row in enumerate(rows):
        for j,v in row.items():a_i.append(i);a_j.append(j);a_v.append(v)
    A=coo_matrix((a_v,(a_i,a_j)),shape=(len(rows),n_edges+len(candidates))).tocsr()
    return domains, sizes, edge, eid, candidates, A, lb, ub


def solve(H):
    domains,sizes,edge,eid,candidates,A,lb,ub=build(H)
    n_edges=len(edge);nvars=A.shape[1]
    c=np.r_[np.ones(n_edges),np.zeros(nvars-n_edges)]
    t0=perf_counter()
    res=milp(c,integrality=np.ones(nvars,dtype=np.uint8),
             bounds=Bounds(np.zeros(nvars),np.ones(nvars)),
             constraints=LinearConstraint(A,np.array(lb),np.array(ub)),
             options={'mip_rel_gap':0.0,'time_limit':180.0})
    t=round(perf_counter()-t0,3)
    assert res.status==0 and res.x is not None, str(res.message)
    assert abs(res.fun-round(res.fun))<1e-6
    assert abs(res.fun-res.mip_dual_bound)<1e-6
    assert res.mip_gap==0.0
    existing=BASEPREFIX|{p for p,i in eid.items() if res.x[i]>.5}
    selections={}
    for h in range(3,H+1):
        chosen=[]
        for i,(oh,fiber,required,types) in enumerate(candidates):
            if oh!=h or res.x[n_edges+i]<.5:continue
            selected=[]
            for ty in required:
                names=[w for w in types[ty] if native(w) in existing]
                assert names
                selected.append(names[0])
            assert len({counts(native(w)) for w in selected})==1
            assert counts(native(selected[0]))==fiber
            assert rank_mod([cc for w in selected for cc in columns(transfer(native(w)))])==9
            det,cols=det_witness(selected)
            assert det!=0
            chosen.append({'fiber':list(fiber),'words':selected,'determinant':det,'independent_observation_columns':len(cols)})
        assert chosen
        selections[h]=chosen
    witness=list(BASE)+[w for h in range(3,H+1) for row in selections[h] for w in row['words']]
    assert trie_cost(witness)==28+round(res.fun)
    return {'H':H,'status':'OPTIMAL','native_trie_cost':28+round(res.fun),
            'additional_cost_after_h2':round(res.fun),'solver_mip_dual_bound':float(res.mip_dual_bound),
            'solver_mip_gap':float(res.mip_gap),'returning_word_counts':sizes,
            'num_0_1_variables':nvars,'num_new_prefix_edges':n_edges,
            'num_constraints':A.shape[0], 'num_fiber_rank_options':len(candidates),
            'selected_certificates':selections,'witness_union_cost_exact':trie_cost(witness),
            'seconds':t}

if __name__=='__main__':
    maxh=int(sys.argv[1]) if len(sys.argv)>1 else 6
    result={'status':'PASS','method':'finite exact 0-1 prefix closure + complete transfer-rank fiber options, HiGHS zero MIP gap',
        'solver_versions':{'python':sys.version.split()[0],'numpy':np.__version__,'scipy':scipy.__version__},
        'base_h2':{'returning_words':8,'mandatory_words':list(BASE),'cost':28},
        'results':[solve(H) for H in range(3,maxh+1)],
        'limitation':'Numerical MILP optimality report; independently exact Python enumeration proves H2/H3, and integer witnesses exactly verify H4..maxH.'}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
