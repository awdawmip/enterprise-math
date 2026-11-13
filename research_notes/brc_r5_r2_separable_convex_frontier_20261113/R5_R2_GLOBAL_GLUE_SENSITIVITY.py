#!/usr/bin/env python3
"""Counterfactual shift of one frozen R5 radius2 gap from 3 to 2; compare global budget frontiers."""
from VERIFY_R5_R2_COMPONENTS import frozen,split_by_radius,frontier_dp,composed_frontier
import json
x=frozen();R=2
blocks=split_by_radius(x,R)
curves=[frontier_dp(b,R)[0] for b in blocks]
orig=frontier_dp(x,R)[0]

def fold(curves):
    d={0:0}
    for c in curves:
        new={}
        for k,v in d.items():
            for h,w in c.items():
                j=k+h; cost=v+w
                if j not in new or cost<new[j]:new[j]=cost
        d=new
    return d

records=[]
for i in range(28):
    left,right=blocks[i],blocks[i+1]
    assert right[0]-left[-1]==3
    fused=left+[z-1 for z in right]
    f,_=frontier_dp(fused,R)
    cf=fold(curves[:i]+[f]+curves[i+2:])
    changed={k:orig[k]-cf[k] for k in orig if k in cf}
    assert all(v>=0 for v in changed.values())
    res={'gap':i+1,'delta_D':min(orig)-min(cf),'merged_min_K':min(cf),'cost_changes_common_K':sum(a>0 for a in changed.values()),'max_common_K_cost_saving':max(changed.values()),'at_old_213_saving':changed[213], 'merged_J_at_212':cf.get(212)}
    records.append(res)
print(json.dumps({'baseline_minK':213,'total_gaps':len(records),'reduces_minK':sum(r['delta_D'] for r in records),'gaps_affect_cost_common_budget':sum(r['cost_changes_common_K']>0 for r in records),'max_global_common_budget_saving':max(r['max_common_K_cost_saving'] for r in records),'records':records},indent=2))
