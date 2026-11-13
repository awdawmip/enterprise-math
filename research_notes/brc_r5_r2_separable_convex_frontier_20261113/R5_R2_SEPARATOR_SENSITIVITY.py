#!/usr/bin/env python3
"""Exact counterfactual sensitivity of frozen R5 radius2 separators; no repin."""
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from VERIFY_R5_R2_COMPONENTS import frozen,split_by_radius,frontier_dp
x=frozen();r=2
blks=split_by_radius(x,r)
results=[]
for i in range(len(blks)-1):
    left=blks[i];right=blks[i+1]
    original_gap=right[0]-left[-1]
    assert original_gap==3
    right_modified=[t-1 for t in right]
    combined=left+right_modified
    original_fL=frontier_dp(left,r)[0]
    original_fR=frontier_dp(right,r)[0]
    composed={}
    for k1,v1 in original_fL.items():
        for k2,v2 in original_fR.items():
            k=k1+k2; v=v1+v2
            if k not in composed or v<composed[k]:composed[k]=v
    merged=frontier_dp(combined,r)[0]
    orig_D=min(composed);new_D=min(merged)
    # for budget feasible on both, old/new cost change
    diffs={k:composed[k]-merged[k] for k in composed if k in merged}
    assert all(v>=0 for v in diffs.values())
    results.append({'separator_index':i+1,'left_N':len(left),'right_N':len(right), 'orig_minK':orig_D, 'new_minK':new_D,'saved_minK':orig_D-new_D,'max_cost_saving':max(diffs.values()),'budget_at_max':min(k for k,v in diffs.items() if v==max(diffs.values())), 'changed_feasible_budget_count':sum(v>0 for v in diffs.values()), 'cost_saving_at_orig_minK':diffs[orig_D]})
assert frontier_dp([0,1,2,4,7],2)[0][2]==5
assert frontier_dp([0,1,2,4,6],2)[0][2]==4
print(json.dumps({'counterexample':{'old':[0,1,2,4,7],'new':[0,1,2,4,6],'K':2,'J_old':5,'J_new':4},'total_separators':len(results),'reduces_minK_count':sum(z['saved_minK']>0 for z in results),'nontrivial_cost_count':sum(z['max_cost_saving']>0 for z in results),'max_saving':max(z['max_cost_saving'] for z in results),'all':results},indent=2))
