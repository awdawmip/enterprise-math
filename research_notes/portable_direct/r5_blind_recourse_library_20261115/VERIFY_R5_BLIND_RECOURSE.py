#!/usr/bin/env python3
"""Exact R5 indexed-center calculations for blind/adaptive recourse."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json

PIN='435e77af0d180eac32bd1f9c4c464bc4010b7551'
def points(m,mask):
    gaps=[3,2,2,3]+[v for _ in range(m) for v in (2,1)]
    if mask&1: gaps[0]-=1
    if mask&2: gaps[3]-=1
    x=[0]
    for d in gaps: x.append(x[-1]+d)
    return x

def optimal(m,mask):
    x=points(m,mask); k=m+3
    opt_cost=None; opt=[]
    for s in combinations(range(len(x)),k):
        nearest=[min(abs(y-x[j]) for j in s) for y in x]
        if max(nearest)>2: continue
        cost=sum(nearest)
        if opt_cost is None or cost<opt_cost:
            opt_cost=cost; opt=[s]
        elif cost==opt_cost: opt.append(s)
    return opt_cost,opt

def dist(s,t): return len(set(s)-set(t))

def stats(m):
    outcomes=[optimal(m,t) for t in range(4)]
    base=outcomes[0][1]; l=m-1
    assert all(c==m+4 for c,_ in outcomes)
    assert [len(f) for _,f in outcomes]==[z*2**l for z in (5,12,9,17)]
    ans=[]
    for mask,(_,new) in enumerate(outcomes):
        a=max(min(dist(s,t) for t in base) for s in new)
        b=min(max(dist(s,t) for s in new) for t in base)
        core_minimax_by_old=Counter(max(dist(s,t) for s in new) for t in base)
        c=min(max(dist(s,t) for t in base) for s in new)
        if mask==2:
            chosen=[(0,1,3,5),(0,2,4,6)]
            oldcore=sorted(optimal(1,0)[1]); newcore=sorted(optimal(1,2)[1])
            hard=[(0,1,3,6),(0,1,4,6)]
            assert [[t for t in oldcore if dist(s,t)<=1] for s in hard]==[[chosen[0]],[chosen[1]]]
            assert all(min(dist(s,t) for t in chosen)<=1 for s in newcore)
        ans.append(dict(mask=mask,adaptive_maxmin=a,blind_minmax=b,new_precommit_minmax=c,old_response_max_hist=dict(sorted(core_minimax_by_old.items()))))
    return dict(m=m,n=5+2*m,K=m+3,cost=m+4,masks=ans)

def main():
    result=[stats(m) for m in range(1,7)]
    for row in result:
        print(row['m'],[(x['mask'],x['adaptive_maxmin'],x['blind_minmax'],x['new_precommit_minmax']) for x in row['masks']])
    base=result[0]
    for row in result:
        for x,y in zip(row['masks'],base['masks']):
            assert x['adaptive_maxmin']==y['adaptive_maxmin']
            assert x['blind_minmax']==y['blind_minmax']+row['m']-1,(row['m'],x,y)
            assert x['new_precommit_minmax']==y['new_precommit_minmax']+row['m']-1,(row['m'],x,y)
            assert x['old_response_max_hist']=={k+row['m']-1:v*2**(row['m']-1) for k,v in y['old_response_max_hist'].items()}
    data=dict(status='PASS_R5_BLIND_RECOURSE',pin=PIN,arithmetic='exact integers; exhaustive combinations',scope='all center subsets for 4 closure masks and m=1..6',rows=result)
    with open(Path(__file__).with_name('BLIND_RECOURSE_EXACT.json'),'w') as f:json.dump(data,f,ensure_ascii=False,sort_keys=True,indent=2)
    print('PASS_R5_BLIND_RECOURSE')
if __name__=='__main__': main()
