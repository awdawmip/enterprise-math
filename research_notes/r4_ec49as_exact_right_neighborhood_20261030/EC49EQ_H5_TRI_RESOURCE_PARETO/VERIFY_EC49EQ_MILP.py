#!/usr/bin/env python3
"""Independent optimization cross-check for EC49EQ (SciPy/HiGHS MILP).
Shares the exact native word/observer definitions from VERIFY_EC49EQ.py,
then independently minimizes binary native-prefix-tree edges. The primary
all-integer tree DP does not require this solver.
"""
import json
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix
from VERIFY_EC49EQ import all_fibers,essential_signatures,path,signature,PAID_BASE,poscount

def solve_milp(fibers,p3,p4,p5):
    hs={3:fibers[3][p3],4:fibers[4][p4],5:fibers[5][p5]}
    prefixes=set(PAID_BASE)
    for ws in hs.values():
        for w in ws:
            p=path(w)
            prefixes.update(p[:i] for i in range(1,len(p)+1))
    prefixes=sorted(prefixes,key=lambda p:(len(p),p))
    index={pr:j for j,pr in enumerate(prefixes)}
    rows=[];cols=[];data=[];lo=[];hi=[]
    def constraint(terms,lower,upper):
        i=len(lo)
        for col,val in terms:
            rows.append(i);cols.append(col);data.append(val)
        lo.append(lower);hi.append(upper)
    for pr in prefixes:
        if len(pr)>1 and pr[:-1] in index:
            constraint(((index[pr],1),(index[pr[:-1]],-1)),-np.inf,0)
    for h,ws in hs.items():
        for target in essential_signatures(ws):
            constraint(((index[path(w)],1) for w in ws if signature(w)==target),1,np.inf)
    for pr in PAID_BASE:constraint(((index[pr],1),),1,1)
    A=coo_matrix((data,(rows,cols)),shape=(len(lo),len(prefixes))).tocsr()
    n=len(prefixes)
    ans=milp(np.ones(n),integrality=np.ones(n),bounds=Bounds(np.zeros(n),np.ones(n)),
        constraints=LinearConstraint(A,lo,hi),options={'mip_rel_gap':0.0})
    assert ans.status==0 and ans.mip_gap==0.0 and round(ans.fun)==round(ans.mip_dual_bound)
    return round(ans.fun)

def main():
    fibers=all_fibers()
    with open('EC49EQ_EXECUTED.json') as f:record=json.load(f)
    cases=record['case_results']
    assert len(cases)==281
    # The source vectors in this model always have last three coordinates zero.
    lookup={h:{p[:3]:p for p in fibers[h]} for h in (3,4,5)}
    count=0
    for case in cases:
        p3,p4,p5=(lookup[h][tuple(p)] for h,p in zip((3,4,5),case['p']))
        optimum=solve_milp(fibers,p3,p4,p5)
        assert optimum==case['E'],(case['p'],optimum,case['E'])
        count+=1
    result={'unit':'EC49EQ','method':'SciPy HiGHS 0-1 MILP, independent of integer trie DP',
        'shared_input':'the exact X6 operation and observer generator from VERIFY_EC49EQ.py',
        'status':'PASS','zero_gap_cases':count,'cost_matches_integer_DP_cases':count,
        'finite_scope':'all 8 M=2 cases and all 273 S=4 cases; comparison by complete p3/p4/p5 assignment'}
    with open('EC49EQ_MILP_EXECUTED.json','w') as f:json.dump(result,f,indent=2)
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
