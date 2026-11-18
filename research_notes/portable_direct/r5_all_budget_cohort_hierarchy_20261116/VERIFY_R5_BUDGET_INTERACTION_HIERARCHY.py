#!/usr/bin/env python3
"""Exact 101-budget, 256-mask R5 cohort hierarchy; 24 independent mask DPs.
Run from a checkout containing the cited predecessor source in its sibling directory.
Scientific pin 435e77af0d180eac32bd1f9c4c464bc4010b7551. Indexed auxiliary model only.
"""
import importlib.util
import json
from pathlib import Path
from collections import defaultdict
P=Path(__file__).resolve().parent.parent/'r5_single_sweep_cohort_zeta_20261116'/'R5_PATH_REQUIREMENT_DP_20261116.py'
spec=importlib.util.spec_from_file_location('frozen_r5_core',P)
core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)
U=core.U; INF=core.INF
K_VALUES=range(214,315)
CHECK_MASKS=(0,1,2,3,4,7,8,15,16,17,31,32,63,64,65,85,127,128,129,170,192,223,254,255)
x,cuts=core.frozen()
pred,init,suffix,requirements=core.parametric_kernel(x,cuts)
assert len(x)==954 and len(cuts)==28 and len(requirements)==16
cost=init[:];poly=[({0:1} if d<INF else {}) for d in init]
answers={};supports=defaultdict(list);patterns=defaultdict(list);union=set()
for k in range(1,315):
    if k>1:
        next_cost=[INF]*len(x)
        for j,edges in enumerate(pred):
            next_cost[j]=min((cost[i]+w for i,w,r in edges if cost[i]<INF),default=INF)
        next_poly=[{} for _ in x]
        for j,edges in enumerate(pred):
            target=next_poly[j];d=next_cost[j]
            if d==INF:continue
            for i,w,r in edges:
                if cost[i]+w!=d:continue
                for mask,num in poly[i].items():
                    m=mask|r;target[m]=target.get(m,0)+num
        cost,poly=next_cost,next_poly
    if k<214:continue
    best=min((cost[j]+v for j,v in enumerate(suffix) if cost[j]<INF and v<INF),default=INF)
    coeff={}
    for j,v in enumerate(suffix):
        if cost[j]+v!=best:continue
        for m,num in poly[j].items():coeff[m]=coeff.get(m,0)+num
    coeff={m:v for m,v in coeff.items() if v}
    counts=core.zeta(coeff)
    assert sum(coeff.values())==counts[255]
    signature=tuple(sorted(coeff));patterns[signature].append(k)
    support=tuple(U[j] for j in range(8) if any(m&(1<<j) for m in coeff))
    supports[support].append(k);union.update(signature)
    answers[k]={'best':best,'coefficients':coeff,'counts':counts,
                'degree':max(map(int.bit_count,signature))}
for mask in CHECK_MASKS:
    reference=core.masked_cost_count(x,cuts,mask,K_VALUES)
    for k in K_VALUES:
        assert reference[k]==(answers[k]['best'],answers[k]['counts'][mask]),(mask,k)
expected_degree={214:4,219:4,220:3,221:2,222:1,223:2,290:2,291:1,292:0,293:1,294:2,313:2,314:1}
for k,v in expected_degree.items():assert answers[k]['degree']==v,(k,answers[k]['degree'])
assert len(union)==25 and len(patterns)==9
assert sum(1 for k in K_VALUES if answers[k]['degree']==4)==6
assert sorted(m for m in union if m.bit_count()==4)==[139]
assert answers[214]['counts'][255]==4573020854769248525038387200000
assert answers[223]['counts'][255]==209661782760358268989540757667840000
assert answers[294]['counts'][255]==342162737216429487140162764800
out={'status':'PASS_R5_101_BUDGET_INTERACTION_HIERARCHY',
     'scientific_input':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
     'budgets':[214,314],'masks':256,'zeta_values':101*256,
     'independent_checked_masks':list(CHECK_MASKS),
     'independent_checked_cost_and_count_pairs':len(CHECK_MASKS)*101,
     'distinct_cohort_support_patterns':len(patterns),
     'union_positive_requirement_masks':sorted(union),
     'fourth_order_requirement_mask':139,
     'degree_by_budget':{str(k):answers[k]['degree'] for k in K_VALUES},
     'support_intervals':{','.join(map(str,s)) if s else 'empty': [min(ks),max(ks)] for s,ks in supports.items()},
     'cohort_patterns': [{'positive_masks':list(m),'budgets':ks} for m,ks in sorted(patterns.items(), key=lambda a:a[1][0])],
     'all_budget_coefficients':{str(k):{str(m):str(c) for m,c in sorted(answers[k]['coefficients'].items())} for k in K_VALUES}}
print(json.dumps(out,ensure_ascii=False,sort_keys=True,separators=(',',':')))
