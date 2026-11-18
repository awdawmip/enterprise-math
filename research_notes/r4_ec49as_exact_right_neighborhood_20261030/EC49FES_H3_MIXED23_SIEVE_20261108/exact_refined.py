"""Exact-by-depth SET COVER strengthening of refined_sieve, still a valid relaxation."""
from collections import defaultdict
from EC49FEJ_DEPTH_FILTER2 import cover
from refined_sieve import group,early_free,exact_early_min

def bound(K,high,cap=94):
    groups=[group(h,s,K) for h in range(4,10) for s in ((16,32) if h in high else (1,2,4,8))]
    free=early_free(K)
    free_by_d={d:frozenset(p for p in free if len(p)==d) for d in range(1,40)}
    cost=exact_early_min(K);byd=[]
    for d in range(1,max(len(q[1]) for q in groups)+1):
        active=[q[1][d-1] for q in groups if q[0]>=d]
        if not active:continue
        masks=defaultdict(int)
        for j,pset in enumerate(active):
            for p in pset:masks[p]|=1<<j
        free_mask=0
        for p in free_by_d[d]:free_mask|=masks.get(p,0)
        need=((1<<len(active))-1)&~free_mask
        if need:
            indices=[j for j in range(len(active)) if (need>>j)&1]
            choices=tuple(sorted(frozenset(sum(1<<i for i,j in enumerate(indices) if (m>>j)&1) for p,m in masks.items() if p not in free_by_d[d])))
            c=cover(choices,(1<<len(indices))-1)
            cost+=c;byd.append([d,c])
            if cost>=cap:break
    return cost,byd

if __name__=='__main__':
 import json,time,collections
 p='/mnt/data/EC49FES_work/';raw=json.load(open(p+'refined_result.json'))['remaining_cases']; start=time.time(); new=[];remain=[];distribution=collections.Counter()
 for q in raw:
    K=tuple(tuple(k) for k in q['keys']);high=tuple(q['high']);score,layers=bound(K,high)
    v={**q,'exact_refined_lower':score,'exact_per_depth_charges':layers};distribution[score]+=1
    (new if score>=94 else remain).append(v)
 report={'input_unresolved':len(raw),'newly_excluded':len(new),'remaining':len(remain),'lower_distribution':dict(sorted(distribution.items())),'new_cases':new,'remaining_cases':remain,'elapsed_s':time.time()-start}
 json.dump(report,open(p+'exact_refined_result.json','w'),indent=2)
 print({k:v for k,v in report.items() if k not in ('new_cases','remaining_cases')})