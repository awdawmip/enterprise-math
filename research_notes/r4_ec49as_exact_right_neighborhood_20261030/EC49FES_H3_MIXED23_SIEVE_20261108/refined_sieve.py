"""Inventory-specific exact early min + all possible early prefixes + depthwise group packing."""
from functools import lru_cache
from EC49FEJ_SIEVE import pool
from EC49FEJ_CONSTRUCT import prefixes
from EC49FEQ_DEPTH_SIEVE import exact_early_min,EARLY_LOW,H3_HIGH
from packing_sieve import group,independent

@lru_cache(maxsize=1024)
def early_free(K):
    lows=[w for k in K for s in (1,8) for w,t in pool(3,k) if t==s]
    return frozenset().union(*(prefixes(w) for w in EARLY_LOW+H3_HIGH+lows))

def bound(K,high,cap=94):
    grp=[group(h,s,K) for h in range(4,10) for s in ((16,32) if h in high else (1,2,4,8))]
    if any(q is None for q in grp):return None
    base=exact_early_min(K)
    freenodes=early_free(K)
    freebydepth={d:frozenset(p for p in freenodes if len(p)==d) for d in range(1,40)}
    lb=base
    layers=[]
    for d in range(1,max(len(q[1]) for q in grp)+1):
        free=freebydepth[d]
        psets=[q[1][d-1] for q in grp if q[0]>=d and not (q[1][d-1]&free)]
        adj=tuple(sum(1<<j for j,b in enumerate(psets) if i!=j and bool(a&b)) for i,a in enumerate(psets))
        k=independent(adj);lb+=k;layers.append(k)
        if lb>=cap:break
    return lb,base,len(freenodes),layers
if __name__=='__main__':
 import json,time,collections
 p='/mnt/data/EC49FES_work/';raw=json.load(open(p+'early_upgrade.json'))['remaining_cases']; start=time.time(); new=[];remain=[];distribution=collections.Counter()
 for q in raw:
    K=tuple(tuple(k) for k in q['keys']);high=tuple(q['high']);score,early,free,layers=bound(K,high)
    v={**q,'refined_lower':score,'early_free_size':free,'depth_packing':layers}; distribution[score]+=1
    (new if score>=94 else remain).append(v)
 report={'input_unresolved':len(raw),'newly_excluded':len(new),'remaining':len(remain),'lower_distribution':dict(sorted(distribution.items())),'new_cases':new,'remaining_cases':remain,'elapsed_s':time.time()-start}
 json.dump(report,open(p+'refined_result.json','w'),indent=2)
 print({k:v for k,v in report.items() if k not in ('new_cases','remaining_cases')})