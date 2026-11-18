#!/usr/bin/env python3
"""Independent exhaustive confirmation of all 620 endpoint-ambiguous split pairs.
All 18 noise strata and all 101 budgets, using integer doubled endpoint sweep.
"""
from pathlib import Path
import csv,json,hashlib,collections
P=Path(__file__).resolve().parent
raw=(P/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes();HSH=hashlib.sha256(raw).hexdigest()
assert HSH=='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
o=json.loads(raw)['counts_and_cohorts'];counts={k:tuple(map(int,o[str(k)]['counts'])) for k in range(214,315)}
stages=list(map(int,json.loads((P/'stages_18.json').read_text())['stage_taus']))
rows=list(csv.DictReader((P/'interior_distinguishing_budget_witnesses.csv').open()));assert len(rows)==620

def maxi(values,diam):
    starts=sorted(set(2*v+diam for v in values));cand=set()
    for p in starts:
        mask=0
        for i,v in enumerate(values):
            if 2*v-diam<=p<=2*v+diam:mask|=1<<i
        cand.add(mask)
    return tuple(sorted(m for m in cand if not any(m!=n and m&n==m for n in cand)))

dist=collections.Counter();first=collections.Counter();stageBudget=collections.Counter();total=0
for n,r in enumerate(rows):
    A=(18,24,82,34,17,int(r['xA']),144,208,int(r['yA']))
    B=(18,24,82,34,17,int(r['xB']),144,208,int(r['yB']))
    diff=set();fst=None
    for k in range(214,315):
        va=[counts[k][i] for i in A];vb=[counts[k][i] for i in B]
        for s,tau in enumerate(stages):
            fa=maxi(va,tau);fb=maxi(vb,tau);total+=1
            if fa!=fb:
                diff.add(k);stageBudget[(s,k)]+=1
                if fst is None or s<fst:fst=s
    exp={int(x) for x in r['witness_budget_list'].split(';')}
    assert diff==exp,(n,diff,exp)
    assert fst==int(r['first_split_stage']), (n,fst)
    dist.update(diff);first[fst]+=1
result={'status':'PASS_ALL_BUDGETS_ALL_CHAMBERS','frozen_sha256':HSH,'pair_instances':len(rows),'pair_budget_stage_compares':total,'exact_families_evaluated':2*total,'budget_witness_counts':dict(sorted(dist.items())),'first_difference_stage_counts':dict(sorted(first.items())),'per_stage_budget_counts':{f'{s},{k}':v for (s,k),v in sorted(stageBudget.items())}}
assert dict(dist)=={214:448,220:172}
assert dict(first)=={2:172,3:112,4:224,8:112}
(P/'INDEPENDENT_ALL_BUDGETS_RESULT.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print('PASS_ALL_620_PAIRS_X_18_STAGES_X_101_BUDGETS',total,'budget_witnesses',dict(dist),'first',dict(first))
