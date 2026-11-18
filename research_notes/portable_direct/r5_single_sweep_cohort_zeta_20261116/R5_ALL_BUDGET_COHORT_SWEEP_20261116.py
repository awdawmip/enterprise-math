#!/usr/bin/env python3
"""Enumerate exact full-closure optimum cohorts for every high-budget K214..314 in a single exact DAG sweep.
Uses the stored R5_PATH_REQUIREMENT_DP_20261116 source with frozen science pin.
"""
from R5_PATH_REQUIREMENT_DP_20261116 import frozen, parametric_kernel, U, zeta, masked_cost_count, INF
from collections import Counter
import json, time

def main():
    t=time.perf_counter();x,cuts=frozen();pred,init,suf,req=parametric_kernel(x,cuts)
    d=init[:]; pol=[({0:1} if v<INF else {}) for v in init]
    records={};sigs=Counter();pos_patterns=Counter();ops=0;additions=0
    for k in range(1,315):
        if k>1:
            nd=[INF]*len(x)
            for j,edges in enumerate(pred):
                for i,v,r in edges:
                    if d[i]<INF and d[i]+v<nd[j]:nd[j]=d[i]+v
            np=[{} for _ in x]
            for j,edges in enumerate(pred):
                if nd[j]==INF:continue
                for i,v,r in edges:
                    ops+=1
                    if d[i]+v!=nd[j]:continue
                    for mask,count in pol[i].items():
                        key=mask|r
                        np[j][key]=np[j].get(key,0)+count
                        additions+=1
            d,pol=nd,np
        if k<214:continue
        best=INF; a={}
        for j,s in enumerate(suf):
            if s==INF or d[j]==INF:continue
            c=d[j]+s
            if c<best: best=c; a={}
            if c==best:
                for m,n in pol[j].items():a[m]=a.get(m,0)+n
        y=zeta(a);support=0
        for m,n in a.items():
            if n:support|=m
        support_ids=tuple(U[i] for i in range(8) if support>>i&1)
        positivity=tuple(sorted(m for m,n in a.items() if n))
        sigs[support_ids]+=1;pos_patterns[positivity]+=1
        records[str(k)]={'cost':best,'support':support_ids,'cohort_positive_count':len(positivity),
                          'exact_cohorts':{str(m):str(n) for m,n in sorted(a.items()) if n},
                          'N_none':str(y[0]),'N_all':str(y[255])}
        expected = ((3,8,9,10,27) if k<=221 else
                    (27,) if k==222 else
                    (25,27) if k<=291 else
                    () if k==292 else
                    (15,17))
        assert support_ids==expected,(k,support_ids,expected)
    assert sum(sigs.values())==101
    report={'status':'PASS_R5_ALL_101_HIGH_BUDGET_COHORT_SWEEP',
            'input_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
            'budget_range':[214,314],'budgets_checked':101,'masks_per_budget':256,
            'layer_updates':313,'cohort_integer_additions':additions,
            'cohort_pass_predecessor_evaluations':ops,
            'support_bands':[{'support':list(k),'budgets':v} for k,v in sigs.items()],
            'distinct_positive_cohort_patterns':len(pos_patterns),
            'positive_patterns':{'-'.join(map(str,k)):v for k,v in pos_patterns.items()},
            'elapsed_seconds':round(time.perf_counter()-t,3),
            'per_budget':records}
    print(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2))
if __name__=='__main__': main()
