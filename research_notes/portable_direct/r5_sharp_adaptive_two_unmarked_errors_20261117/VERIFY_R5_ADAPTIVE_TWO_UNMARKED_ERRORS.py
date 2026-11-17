#!/usr/bin/env python3
"""Exact finite sharp adaptive f=2 certificate; standard-library integers only."""
from functools import lru_cache
from collections import Counter
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'EXACT_R5_ALL_101_BUDGETS.json'
BUDGETS=(294,223,214)
DELTA=76289178155959966960189440
frozen=json.loads((HERE/'COHORTS_3_BUDGETS.json').read_text())
assert frozen['frozen_science_commit']=='435e77af0d180eac32bd1f9c4c464bc4010b7551'

def restore(row):
    v=[0]*256
    for b,n in row.items(): v[int(b)]=int(n)
    for bit in range(8):
        for b in range(256):
            if b&(1<<bit): v[b]+=v[b^(1<<bit)]
    return v

counts={int(k):restore(c) for k,c in frozen['cohorts'].items()}
assert sorted(counts)==[214,223,294]
signatures={tuple(counts[k][b] for k in BUDGETS) for b in range(256)}
assert len(signatures)==256
centers={k:sorted(set(counts[k])) for k in BUDGETS}
spacing={k:min(b-a for a,b in zip(v,v[1:])) for k,v in centers.items()}
assert min(spacing.values())==DELTA

full=json.loads(SOURCE.read_text())
for k in counts:
    assert list(map(int,full['counts_and_cohorts'][str(k)]['counts']))==counts[k]
windows=((16,17,range(214,222)),(16,80,range(223,292)),(16,32,range(294,314)))
for b,c,win in windows:
    support=[k for k in range(214,315) if
      int(full['counts_and_cohorts'][str(k)]['counts'][b])!=
      int(full['counts_and_cohorts'][str(k)]['counts'][c])]
    assert support==list(win),(b,c,support)

def inferred(reads,remaining):
    L=len(reads); freq=Counter(reads)
    if remaining==0:return reads[0] if L==1 else None
    if remaining==1:
        if L==2 and reads[0]==reads[1]:return reads[0]
        if L==3:return reads[2]
        return None
    assert remaining==2
    if L==3 and len(freq)==1:return reads[0]
    if L==4:
        if max(freq.values())>=3:return freq.most_common(1)[0][0]
        if sorted(freq.values())==[1,1,2]:
            return next(x for x,n in freq.items() if n==2)
    if L==5:return next((x for x,n in freq.items() if n>=3),None)
    return None

# True count is symbol 0; 1,2 and '?' represent arbitrary other
# count centers or out-of-alphabet values. This covers every equality type
# of <=2 symbol-changing errors.
@lru_cache(None)
def local_branches(remaining):
    completed=[]
    def rec(reads,err):
        found=inferred(reads,remaining)
        if found is not None:
            assert found==0,(remaining,reads,err)
            completed.append((len(reads),err,reads));return
        assert len(reads)<2*remaining+1,(remaining,reads)
        for answer in (0,1,2,'?'):
            bad=int(answer!=0)
            if err+bad<=remaining:rec(reads+(answer,),err+bad)
    rec(tuple(),0)
    return tuple(completed)

branch_counts={str(r):len(local_branches(r)) for r in (0,1,2)}
assert branch_counts=={'0':1,'1':7,'2':64}
@lru_cache(None)
def worst_from(i,remaining):
    if i==len(BUDGETS):return (0,())
    k=BUDGETS[i]
    candidates=[]
    for reads,spent,_ in local_branches(remaining):
        rest,path=worst_from(i+1,remaining-spent)
        candidates.append((k*reads+rest,((k,reads,spent),)+path))
    return max(candidates,key=lambda t:t[0])

worst,witness=worst_from(0,2)
assert worst==2621

# Four-state exact minimax lower-bound DP.
# h=0 means mask16; alternatives h=1,2,3 correspond 17,80,32.
# Each action j has one binary distinguishing window. Symbol 2 is
# an arbitrary reading distinct from both valid outcomes.
fees=(214,223,294)
state_cache={}
@lru_cache(None)
def star_value(errs):
    if sum(v<3 for v in errs)<=1:return 0
    options=[]
    for axis,k in enumerate(fees):
        outcomes=[]; no_progress=False
        for symbol in (0,1,2):
            dest=tuple(min(3,v+(symbol!=int(h==axis+1)))
                       for h,v in enumerate(errs))
            if dest==errs:
                no_progress=True;break
            if any(v<3 for v in dest):outcomes.append(star_value(dest))
        if not no_progress and outcomes:options.append((k+max(outcomes),axis))
    assert options,errs
    best=min(options)
    state_cache[errs]=best
    return best[0]

lower=star_value((0,0,0,0))
assert lower==2621
for errs,(value,axis) in state_cache.items():
    assert star_value(errs)==value
    for j,k in enumerate(fees):
        outcomes=[]; no_progress=False
        for symbol in (0,1,2):
            dest=tuple(min(3,v+(symbol!=int(h==j+1)))
                       for h,v in enumerate(errs))
            if dest==errs:
                no_progress=True;break
            if any(v<3 for v in dest):outcomes.append(star_value(dest))
        if not no_progress and outcomes:assert k+max(outcomes)>=value

result={
 'status':'PASS_R5_SHARP_ADAPTIVE_TWO_UNMARKED_ERRORS_2621',
 'frozen_science_commit':frozen['frozen_science_commit'],
 'domain':'256 scalar masks, budgets 214..314, 0<=2eta<delta, f=2, e=0',
 'delta':str(DELTA),
 'upper_exact_strategy':'294,223,214; r2=3 reads with discrepancy refinement to 4/5; r1=2 plus third on mismatch; r0=1',
 'upper_worst_cost':worst,
 'upper_worst_witness':[[int(a),int(b),int(c)] for a,b,c in witness],
 'quantized_local_branch_counts':branch_counts,
 'upper_dp_cache_size':worst_from.cache_info().currsize,
 'lower_exact_star_game_cost':lower,
 'lower_star_game_visited_nonterminal_states':len(state_cache),
 'lower_dp_cache_size':star_value.cache_info().currsize,
 'lower_witness_masks':[16,17,80,32],
 'lower_witness_windows':[[214,221],[223,291],[294,313]],
 'frozen_budget_counts_crosschecked':768,
 'frozen_window_budget_comparisons':303,
 'three_budget_signature_count':len(signatures),
 'noise_and_corruption_semantics':'Normal real reading within eta of exact count; two arbitrary unmarked replacements; quantized alphabet centers and one outside marker.',
 'review':'AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED',
 'next':'Adaptive f>=3; noise crossing delta; signed provenance preserving native observer bridge.'
}
(HERE/'RESULTS_TWO_ERRORS_EXACT.json').write_text(
    json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
print(result['status'])
print(json.dumps({k:result[k] for k in
      ['upper_worst_cost','upper_worst_witness','quantized_local_branch_counts',
       'lower_exact_star_game_cost','lower_star_game_visited_nonterminal_states',
       'lower_dp_cache_size']},indent=2))
