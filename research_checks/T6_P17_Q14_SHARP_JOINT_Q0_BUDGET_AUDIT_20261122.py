#!/usr/bin/env python3
"""Exact author-side pre-affine cost ceiling for T6 p17 order(7,7).
The identified cofactor model is the original 2026-11-16 pinned side-roster model.
No congruence feasibility, affine enumeration or formal task claim is assumed.
"""
import itertools, json, time, hashlib
from collections import Counter
from functools import lru_cache
P=17; Q=7; B=2331; PS=(2,3,5,7,11,13,17)
def smooth(n):
    for p in PS:
        while n%p==0: n//=p
    return n==1
atoms=tuple((q,r) for q in range(1,8) for r in range(1,17) if smooth(17*q+r))
weights=tuple(289*q+17*r-1 for q,r in atoms)
@lru_cache(None)
def sides(total=Q,last=0,remaining=B):
    if total==0:
        return ((),)
    out=[]
    for i in range(last,len(atoms)):
        q,_=atoms[i]; w=weights[i]
        if q>total:break
        if w>remaining:continue
        for tail in sides(total-q,i,remaining-w):out.append((i,)+tail)
    return tuple(out)
start=time.perf_counter();rosters=sides(); data=[]
for r in rosters:
    cost=sum(weights[i] for i in r)
    assert cost<=B and sum(atoms[i][0] for i in r)==Q
    mask=0
    for i in r:mask|=1<<i
    data.append((cost,mask,r))
data.sort(); hist=Counter(); min_pair=10**20; min_pairs=[]; n=0; max_q0_count=-1; max_q0_pairs=[]
for j,(c,mask,r) in enumerate(data):
    for c2,mask2,r2 in data[j+1:]:
        if mask & mask2:continue
        n+=1
        total=c+c2
        hist[total]+=1
        bb1,bb2=B-c,B-c2
        q0_cap=max(bb1//16+bb2//33,bb1//33+bb2//16)
        if q0_cap>max_q0_count:
            max_q0_count=q0_cap;max_q0_pairs=[(r,r2,c,c2)]
        elif q0_cap==max_q0_count:max_q0_pairs.append((r,r2,c,c2))
        if total<min_pair:
            min_pair=total;min_pairs=[(r,r2,c,c2)]
        elif total==min_pair:min_pairs.append((r,r2,c,c2))
mins=[(c,[(atoms[k],weights[k]) for k in r]) for c,_,r in data[:10]]
# useful distribution summaries and exact secondary quantiles in integers
pair_budget_hist={str(2*B-total):freq for total,freq in sorted(hist.items())}
result={"model":"T6_P17_Q14_7_7_ONE_POWER_CANCELLATION_NORMALIZED", "p":P,"vertical_order_each_side":Q,"side_budget":B,"smooth_atom_count":len(atoms),"side_rosters":len(rosters),"disjoint_unordered_pairs":n,"global_min_disjoint_pair_vertical_cost":min_pair,"global_max_joint_q0_mass_budget":2*B-min_pair,"minimizer_count":len(min_pairs),"max_budget_only_cancellation_normalized_q0_atom_count":max_q0_count,"max_q0_count_pair_count":len(max_q0_pairs),"max_q0_count_pairs":[{"A":[list(atoms[k]) for k in r1],"B":[list(atoms[k]) for k in r2],"remaining_BA":B-c1,"remaining_BB":B-c2} for r1,r2,c1,c2 in max_q0_pairs],"minimizers":[{"A":[list(atoms[k]) for k in r1],"B":[list(atoms[k]) for k in r2],"cost_A":c1,"cost_B":c2,"remaining_q0_budget_A":B-c1,"remaining_q0_budget_B":B-c2} for r1,r2,c1,c2 in min_pairs],"first_ten_side_rosters_by_cost":[{"cost":c,"atoms":[list(a) for a,w in rr]} for c,rr in mins],"joint_q0_mass_budget_frequency":pair_budget_hist,"elapsed_seconds":round(time.perf_counter()-start,4),"scope":"exact combinatorial cost bound only; no q0 congruences/affine tests/native acceptance"}
assert len(atoms)==60 and len(rosters)==1907 and n==809566
assert min_pair==4095 and len(min_pairs)==1
assert max_q0_count==26 and len(max_q0_pairs)==1
with open('/mnt/data/t6_q14_mass_budget_audit.json','w') as f:json.dump(result,f,sort_keys=True,indent=2)
print(json.dumps({k:v for k,v in result.items() if k not in ('joint_q0_mass_budget_frequency','first_ten_side_rosters_by_cost')},indent=2))
print('sha256',hashlib.sha256(open('/mnt/data/t6_q14_mass_budget_audit.json','rb').read()).hexdigest())
