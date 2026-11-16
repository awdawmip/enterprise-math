#!/usr/bin/env python3
"""R5 k=7 genuine-source s=2, positive named Set on bits 0 and 1.
Exact integer witness verifier; no third-party dependencies.
"""
import json
K=7
N=1<<K
CENTRES=(23,31,39,43,59,90,91,108,109,110,111,116,117,118,119,124,125,126,127)
TARGETS={23:(23,23),31:(31,31),39:(39,39),43:(43,43),59:(59,59),
         90:(91,90),91:(91,91),108:(109,110),109:(109,111),
         110:(111,110),111:(111,111),116:(117,118),117:(117,119),
         118:(119,118),119:(119,119),124:(125,126),125:(125,127),
         126:(127,126),127:(127,127)}
assert len(CENTRES)==len(set(CENTRES))==19
assert set(TARGETS)==set(CENTRES)
assert all(set(ts)<=set(CENTRES) for ts in TARGETS.values())
def edge_count(u):
    return sum(((u>>i)&1)*((u>>((i+1)%K))&1) for i in range(K))
def genuine(r,u):
    return (u&~r)==0 and 0<=edge_count(r)-edge_count(u)<=2
def raw_set(u,a):
    return u|(1<<a)
# Greatest forward-invariant simulation relation over all 128*19 pairs.
valid={(u,r) for u in range(N) for r in CENTRES if genuine(r,u)}
initial_pairs=len(valid)
iterations=0
while True:
    new={(u,r) for u,r in valid if all((raw_set(u,a),TARGETS[r][a]) in valid for a in (0,1))}
    if new==valid: break
    valid=new
    iterations+=1
assert all(any((u,r) in valid for r in CENTRES) for u in range(N))
# For every admissible initial pair all finite positive Set words remain source-correct.
assert all(genuine(r,u) and all((raw_set(u,a),TARGETS[r][a]) in valid for a in (0,1)) for u,r in valid)
# The explicit action table in fact satisfies commuting and idempotent positive resets.
assert all(TARGETS[TARGETS[r][a]][a]==TARGETS[r][a] for r in CENTRES for a in (0,1))
assert all(TARGETS[TARGETS[r][0]][1]==TARGETS[TARGETS[r][1]][0] for r in CENTRES)
report={'status':'PASS_R5_K7_TWO_RAISES_NINETEEN_UPPER',
        'frozen_science_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
        'model':'genuine-source 7-cycle q(u)=sum adjacent products, slack=2, only Set_0(1),Set_1(1)',
        'raw_snapshots':N,'states':len(CENTRES),'initial_feasible_pairs':initial_pairs,
        'greatest_simulation_pairs':len(valid),'pruning_rounds':iterations,
        'valid_initials':sum(any((u,r) in valid for r in CENTRES) for u in range(N)),
        'idempotent_commuting':True,
        'centres':list(CENTRES),'targets':{str(r):list(t) for r,t in TARGETS.items()},
        'claim':'N_H(7,{S_0^+,S_1^+},2)<=19 for every integer H>=0',
        'review':'NOT_REVIEWED'}
print(json.dumps(report,indent=2,sort_keys=True))
