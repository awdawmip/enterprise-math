#!/usr/bin/env python3
"""Frozen R5 integer observer: uncertain or per-query varying fifth-chamber tau.
Usage: python3 VERIFY_R5_UNKNOWN_TAU_SEVEN_ACTIONS.py EXACT_R5_ALL_101_BUDGETS.json
"""
import hashlib, json, sys
from pathlib import Path

EXPECTED_SHA256 = '50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
L = 25845652773852463277015040000
P = 42621568083499305947627520000
Q = 45392032647559604256815185920
U = 58182461585441404127941754880
BUDGETS = tuple(range(214,315))
CORE = (214, 215, 216, 217, 223, 295, 296)

def maximal(a):
    a=set(a)
    return tuple(sorted(x for x in a if not any(x!=z and x&z==x for z in a)))

def windows(ns, diameter, strict):
    order=sorted(range(256),key=lambda h:(ns[h],h))
    r=0; out=[]
    for l in range(256):
        r=max(r,l)
        while r<256 and ((ns[order[r]]-ns[order[l]] < diameter) if strict else
                             (ns[order[r]]-ns[order[l]] <= diameter)):
            r+=1
        out.append(sum(1 << order[z] for z in range(l,r)))
    return maximal(out)

def main():
    raw=Path(sys.argv[1]).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==EXPECTED_SHA256
    js=json.loads(raw)
    assert js['budget_range']==[214,314]
    centers={k:tuple(map(int,js['counts_and_cohorts'][str(k)]['counts'])) for k in BUDGETS}
    assert all(len(centers[k])==256 for k in BUDGETS)
    F={k:windows(centers[k],U-1,False) for k in BUDGETS}
    for k in BUDGETS:
        assert F[k]==windows(centers[k],U,True),(k,'strict-open mismatch')
    def dominates(j,k):
        return all(any(s&z==s for z in F[k]) for s in F[j])
    derived=tuple(k for k in BUDGETS if not any(dominates(j,k) for j in range(214,k)))
    assert derived==CORE,(derived,CORE)
    replacement={}
    for k in BUDGETS:
        if k not in CORE:
            options=[j for j in CORE if j<k and dominates(j,k)]
            assert options,k
            replacement[str(k)]=options[0]
    assert len(replacement)==94,len(replacement)
    assert replacement['294']==214
    assert F[294]==((1<<256)-1,),'query 294 unexpectedly informative'
    witnesses={}
    for k in CORE:
        for j in range(214,k):
            s=next((s for s in F[j] if not any(s&z==s for z in F[k])),None)
            assert s is not None,(j,k)
            witnesses[f'{j}->{k}']=hex(s)
    obj={
       'status':'PASS_R5_UNKNOWN_TAU_FIFTH_CHAMBER_SEVEN_ACTIONS_ALL_F',
       'input_sha256':EXPECTED_SHA256,
       'frozen_science_commit':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
       'allowed_budgets':[214,314],'named_hypotheses':256,
       'noise_diameter_set':f'[{L},{U})',
       'uncertainty_model':'tau unknown to policy, fixed or independently varying between queries',
       'upper_envelope':'correct h iff abs(y-N_h(k)) < U/2; strict inequality essential',
       'support_family_identity':'strict U equals closed U-1 for each budget',
       'universal_optimal_core':list(CORE),
       'remaining_cost_nonincreasing_local_actions':7,
       'eliminated_budgets':len(replacement),
       'replacement_map':replacement,
       'core_irreducible_with_respect_to_cheaper_single_queries':True,
       'counter_support_pair_count':len(witnesses),
       'counter_support_sha256':hashlib.sha256(json.dumps(witnesses,sort_keys=True).encode()).hexdigest(),
       'support_family_size_by_core_action':{str(k):len(F[k]) for k in CORE},
       'support_family_size_294':len(F[294]),
       'local_replacement_cost_barrier':'2*214=428 > 314',
       'exact_cost_identity':'C_f^unknown_and_query_varying([L,U))=C_f^known(U-1), all integers f>=0',
       'known_numerical_benchmarks':{'f0':735,'f8_lower':8335,'f8_upper':8343},
       'independent_review':'NOT_REVIEWED'
    }
    print(json.dumps(obj,sort_keys=True,indent=2))
    print(obj['status'],file=sys.stderr)

if __name__=='__main__':
    main()
