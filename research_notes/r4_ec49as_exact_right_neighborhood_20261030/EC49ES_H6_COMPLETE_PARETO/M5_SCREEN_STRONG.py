from VERIFY_EC49ER import *
from itertools import product
from collections import Counter
import time,json
fs=fibers();T4=frozenset(signature(w) for w in BASE);p0=poscount('ce');F={h:{p:essential(w) for p,w in fs[h].items() if essential(w)} for h in range(3,7)}
P={h:tuple(sorted(p for p in F[h] if F[h][p]==T4)) for h in F};t=time.time();lows={}
for ps in product(P[3],P[4],P[5]):
    lows[ps]=exact_trie_opt(fs,dict(zip(range(3,6),ps)))['E']
for m,bound in ((4,80),(5,60)):
    cs=[];ctr=Counter();eligible=Counter()
    for ps in product(*(P[h] for h in range(3,7))):
        if len({p0,*ps})!=m:continue
        ctr[lows[ps[:3]]]+=1
        if lows[ps[:3]]+4<=bound:cs.append(ps);eligible[lows[ps[:3]]]+=1
    print('M',m,'total',sum(ctr.values()),'screened',len(cs),'strata',dict(sorted(eligible.items())),'elapsed',round(time.time()-t,2),flush=True)
    with open(f'EC49ES_M{m}_SCREENED.json','w') as f:json.dump({'m':m,'bound':bound,'total':sum(ctr.values()),'screened':[list(map(list,ps)) for ps in cs], 'H5_lower_distribution':dict(ctr),'eligible_distribution':dict(eligible)},f)
