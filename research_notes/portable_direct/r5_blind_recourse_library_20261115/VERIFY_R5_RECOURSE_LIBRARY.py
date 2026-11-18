#!/usr/bin/env python3
"""Exact minimum precompiled old-optimizer library covering each new optimum."""
from itertools import combinations
from VERIFY_R5_BLIND_RECOURSE import optimal,dist
from pathlib import Path
import json

def minimum_library(m,mask,r):
    old=sorted(optimal(m,0)[1]); new=sorted(optimal(m,mask)[1]); full=(1<<len(new))-1
    masks=[sum(1<<i for i,s in enumerate(new) if dist(s,t)<=r) for t in old]
    for k in range(len(old)+1):
        tested=0
        for idxs in combinations(range(len(old)),k):
            tested+=1
            cov=0
            for j in idxs: cov|=masks[j]
            if cov==full:
                return {'minimum':k,'witness_old_indices':list(idxs), 'witness_old_sets':[list(old[j]) for j in idxs], 'candidate_count':len(old),'target_count':len(new),'tested_at_successful_cardinality':tested}
    raise RuntimeError('unreachable')

def main():
    rows=[]
    for m in range(1,4):
        ans={'m':m,'cases':[]}
        for mask,r in [(0,0),(1,2),(2,1),(3,2)]:
            out=minimum_library(m,mask,r)
            out.update({'mask':mask,'radius':r})
            ans['cases'].append(out)
        rows.append(ans)
        print('m',m,[(c['mask'],c['minimum']) for c in ans['cases']])
    result={'status':'PASS_EXACT_R5_RECOURSE_LIBRARY','scope':'m=1..3, all subsets of original optimizer family tested in increasing library size','rows':rows}
    with open(Path(__file__).with_name('RECOURSE_LIBRARY_EXACT.json'),'w') as f:json.dump(result,f,ensure_ascii=False,sort_keys=True,indent=2)
    print('PASS_EXACT_R5_RECOURSE_LIBRARY')
if __name__=='__main__': main()
