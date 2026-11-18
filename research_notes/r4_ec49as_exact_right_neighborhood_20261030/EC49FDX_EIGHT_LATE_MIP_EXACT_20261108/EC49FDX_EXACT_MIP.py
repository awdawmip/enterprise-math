#!/usr/bin/env python3
"""EC49FDX conditional H7-H9 exact native-prefix MILP, frozen input fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Fix H2-H6 words in each EC49FDW witness, fix final BRC key, enumerate every legal full signed-native H7-H9 word.
Requires numpy/scipy; HiGHS optimum + dual bound is the computational lower-bound certificate.
"""
import json,sys,os,time
from pathlib import Path
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'EC49FDU_THREE_PHASE_RANK_20261107'))
sys.path.insert(0,str(ROOT/'EC49FDV_QUOTA_THREE_PHASE_20261108'))
_CWD=os.getcwd()
os.chdir(ROOT/'EC49FDV_QUOTA_THREE_PHASE_20261108')
from EC49FDV_NATIVE_WITNESSES import word_pool,prefixes,verify_full
os.chdir(_CWD)
CASES=json.loads((ROOT/'EC49FDW_EIGHT_NATIVE_PREFIX_IMPROVEMENTS_20261108'/'WITNESSES_EC49FDW.json').read_text())['cases']

def solve(idx,limit=60):
    case=CASES[idx]
    fixed={str(h):list(case['words'][str(h)]) for h in range(2,7)}
    fixed_prefix=set().union(*(prefixes(w) for ws in fixed.values() for w in ws))
    k=tuple(case['late_keys'][2]);groups={}
    for h in (7,8,9):
        for w,sig in word_pool(h,k):groups.setdefault((h,sig),[]).append(w)
    assert len(groups)==10
    assert {h:sum(g[0]==h for g in groups) for h in (7,8,9)}=={7:4,8:4,9:2}
    words=sorted({w for group in groups.values() for w in group})
    edges=sorted(set().union(*(prefixes(w)-fixed_prefix for w in words)))
    path_id={w:i for i,w in enumerate(words)}
    edge_id={p:len(words)+j for j,p in enumerate(edges)}
    rr=[];cc=[];vv=[];lb=[];ub=[]
    for group,ws in sorted(groups.items()):
        row=len(lb)
        for w in ws:rr.append(row);cc.append(path_id[w]);vv.append(1)
        lb.append(1);ub.append(1)
    for w in words:
        for p in prefixes(w)-fixed_prefix:
            row=len(lb);rr.extend((row,row));cc.extend((path_id[w],edge_id[p]));vv.extend((1,-1))
            lb.append(-np.inf);ub.append(0)
    a=coo_matrix((vv,(rr,cc)),shape=(len(lb),len(words)+len(edges))).tocsr()
    c=np.r_[np.zeros(len(words)),np.ones(len(edges))]
    start=time.monotonic()
    res=milp(c=c,integrality=np.ones(len(c)),bounds=Bounds(np.zeros(len(c)),np.ones(len(c))),constraints=LinearConstraint(a,lb,ub),options={'time_limit':limit,'mip_rel_gap':0})
    out={'case_index':idx,'key':k,'fixed_cost':len(fixed_prefix),'word_candidates':len(words),'unpaid_prefix_variables':len(edges),'constraints':len(lb),'solver_status':int(res.status),'solver_message':res.message,'mip_objective':float(res.fun) if res.fun is not None else None,'mip_dual_bound':float(res.mip_dual_bound) if getattr(res,'mip_dual_bound',None) is not None else None,'mip_gap':float(res.mip_gap) if getattr(res,'mip_gap',None) is not None else None,'seconds':round(time.monotonic()-start,2)}
    if res.x is not None:
        sel=[w for w in words if res.x[path_id[w]]>0.5]
        full={h:list(ws) for h,ws in fixed.items()}
        for w in sel:full.setdefault(str(len(w)),[]).append(w)
        total,actual_keys=verify_full(full)
        assert total==int(round(float(res.fun)))+len(fixed_prefix)
        assert total==case['cost'] and len(actual_keys)==5
        out['validated_cost']=total
        out['literal_words']=full
    return out

if __name__=='__main__':
    idx=int(os.getenv('IDX','0'))
    output=solve(idx,float(os.getenv('LIMIT','60')))
    print(json.dumps(output,ensure_ascii=False,indent=2))
    if os.getenv('WRITE_JSON','1')=='1':
        Path(__file__).with_name('EC49FDX_SOLVER_CASE_'+str(idx)+'.json').write_text(json.dumps(output,indent=2)+'\n')
