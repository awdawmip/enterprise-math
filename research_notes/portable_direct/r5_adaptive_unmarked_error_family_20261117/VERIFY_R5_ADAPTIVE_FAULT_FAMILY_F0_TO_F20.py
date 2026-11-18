#!/usr/bin/env python3
"""Exact finite-star minimax certificate through any user-selected f_max.

The all-f upper is proved separately by a repeat-until-(r+1) strategy.
The restricted four-mask lower uses the already verified frozen R5 witness
difference windows; no new native BRC/X6 equivalence is inferred.
"""
from functools import lru_cache
import json
import sys
from pathlib import Path

DEST=Path(__file__).resolve().parent
WINDOWS=((214,221),(223,291),(294,313))
COSTS=(214,223,294)
BASE=sum(COSTS)
LAST=min(COSTS)
assert BASE==731 and LAST==214
LIMIT=int(sys.argv[1]) if len(sys.argv)>1 else 20
assert 0<=LIMIT<=64

result={
 'schema':'R5_SHARP_ADAPTIVE_F0_FMAX_MINMAX_V1',
 'freeze_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
 'model':'Four-state deterministic window witness: masks(16,17,80,32); f arbitrary unmarked errors; 0<=2eta<delta for 256-state upper',
 'noise_delta':'76289178155959966960189440',
 'windows':[list(x) for x in WINDOWS],
 'costs':list(COSTS),
 'universal_constructive_upper':'C_f <= 731+945*f, for every nonnegative integer f',
 'finite_lower_and_equalities':[],
 'finite_checked_f_max':LIMIT,
 'review':'AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED',
 'continuation':'Prove sharp lower bound for all f or find finite counterexample above tested range; study high-noise.'
}
for f in range(LIMIT+1):
    cap=f+1
    @lru_cache(None)
    def V(d):
        if sum(x<cap for x in d)<=1:return 0
        alternatives=[]
        for j,cost in enumerate(COSTS):
            vals=[];has_stutter=False
            for a in (0,1,2):
                dest=tuple(min(cap,x+(a!=int(h==(j+1)))) for h,x in enumerate(d))
                if dest==d:
                    has_stutter=True;break
                if any(x<cap for x in dest):vals.append(V(dest))
            if vals and not has_stutter:
                alternatives.append(cost+max(vals))
        assert alternatives,d
        return min(alternatives)
    ans=V((0,0,0,0))
    target=BASE+f*(BASE+LAST)
    assert ans==target,(f,ans,target)
    result['finite_lower_and_equalities'].append({
       'f':f,'exact_minmax':ans,'all_f_upper':target,
       'dp_states':V.cache_info().currsize,
       'fixed_repetition_cost':(2*f+1)*BASE,
       'adaptive_saving':(2*f+1)*BASE-ans
    })
    if f%8==0 or f==LIMIT:
        print(f'VERIFIED_F={f} V={ans} states={V.cache_info().currsize}',flush=True)

result['status']=f'PASS_R5_ADAPTIVE_UNMARKED_ERROR_FINITE_F0_TO_F{LIMIT}'
(DEST/'RESULTS_FAMILY_FINITE.json').write_text(
    json.dumps(result,indent=2,sort_keys=True)+'\n')
print(result['status'])
