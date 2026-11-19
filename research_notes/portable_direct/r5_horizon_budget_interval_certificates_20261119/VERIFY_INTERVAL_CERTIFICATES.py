#!/usr/bin/env python3
"""Exact R5 horizon budget verifier: direct original predicate versus interval certificates."""
import json
import itertools
import random
from pathlib import Path

def words(actions, h):
    yield ()
    for n in range(1, h + 1):
        yield from itertools.product(range(actions), repeat=n)

def path_data(transition, label, cost, word, start):
    state = start
    cumulative = 0
    history = [label[state]]
    for a in word:
        cumulative += cost[a][state]
        state = transition[a][state]
        history.append(label[state])
    return cumulative, history

def interval_basis(transition, label, cost, source, alternatives, h):
    candidate_windows = []
    for w in words(len(transition), h):
        cx, hx = path_data(transition, label, cost, w, source)
        feasible_alt_costs = []
        for y in alternatives:
            cy, hy = path_data(transition, label, cost, w, y)
            if all((lx & ly) == lx for lx, ly in zip(hx, hy)):
                feasible_alt_costs.append(cy)
        upper = min(feasible_alt_costs) - 1 if feasible_alt_costs else None
        if upper is None or cx <= upper:
            candidate_windows.append((cx, upper, w))
    return candidate_windows

def direct_safe(transition, label, cost, source, alternatives, h, b):
    for w in words(len(transition), h):
        cx, hx = path_data(transition, label, cost, w, source)
        if cx > b:
            continue
        ok = False
        for y in alternatives:
            cy, hy = path_data(transition, label, cost, w, y)
            if cy <= b and all((lx & ly) == lx for lx, ly in zip(hx, hy)):
                ok = True
                break
        if not ok:
            return False
    return True

def compact_intervals(windows):
    seq = sorted(((lo,hi) for lo,hi,_ in windows), key=lambda e:(e[0],e[1] is not None,-1 if e[1] is None else e[1]))
    if not seq:
        return []
    result=[]
    for lo,hi in seq:
        if not result:
            result.append([lo,hi]); continue
        prev=result[-1]
        if prev[1] is None or lo<=prev[1]+1:
            if hi is None or prev[1] is None:
                prev[1]=None
            else:
                prev[1]=max(hi,prev[1])
        else:
            result.append([lo,hi])
    return result

def from_intervals(windows,budget):
    return not any(lo<=budget and (hi is None or budget<=hi) for lo,hi,_ in windows)

def verify_family(q,d,h):
    trans=[[0,2,2]]
    cost=[[q,q+d,q]]
    label=[1,1,1]
    windows=interval_basis(trans,label,cost,0,[1],h)
    compact=compact_intervals(windows)
    predicted=[[q*t,q*t+d-1] for t in range(1,h+1)]
    assert compact==predicted,(q,d,h,compact,predicted)
    maxb=q*(h+2)+d
    for b in range(maxb+1):
        expected=not any(q*t<=b<=q*t+d-1 for t in range(1,h+1))
        assert from_intervals(windows,b)==expected
        assert direct_safe(trans,label,cost,0,[1],h,b)==expected
    return maxb+1

def run():
    trials=comparisons=raw_windows=interval_components=cases_with_no_alternative=0
    rng=random.Random(20261119)
    for _ in range(1800):
        n=rng.choice([2,3,4,5])
        a_count=rng.choice([1,2,3])
        h=rng.choice([0,1,2,3,4])
        trans=[[rng.randrange(n) for _ in range(n)] for _ in range(a_count)]
        cost=[[rng.randrange(4) for _ in range(n)] for _ in range(a_count)]
        label=[rng.randrange(8) for _ in range(n)]
        source=rng.randrange(n)
        candidates=[i for i in range(n) if i!=source]
        alts=rng.sample(candidates,rng.randrange(1,len(candidates)+1))
        win=interval_basis(trans,label,cost,source,alts,h)
        compact=compact_intervals(win)
        assert all(lo>=0 and (hi is None or lo<=hi) for lo,hi in compact)
        assert len(compact)<=sum(a_count**j for j in range(h+1))
        raw_windows+=len(win)
        interval_components+=len(compact)
        cases_with_no_alternative+=any(hi is None for lo,hi,_ in win)
        for b in range(3*h+8):
            assert direct_safe(trans,label,cost,source,alts,h,b)==from_intervals(win,b)
            comparisons+=1
        trials+=1
    family_checks=family_instances=0
    for q in range(2,10):
        for d in range(1,q):
            for h in range(0,9):
                family_checks+=verify_family(q,d,h)
                family_instances+=1
    out={
      "schema":"R5_HORIZON_BUDGET_INTERVAL_CERTIFICATES_V1",
      "result":"PASS_R5_HORIZON_INTERVALS",
      "random_seed":20261119,
      "independent_random_systems":trials,
      "independent_per_budget_comparisons":comparisons,
      "raw_nonempty_bad_windows":raw_windows,
      "merged_bad_interval_components":interval_components,
      "systems_with_permanent_bad_tail":cases_with_no_alternative,
      "sharp_family_instances":family_instances,
      "sharp_family_per_budget_checks":family_checks,
      "family_parameter_range":{"q":[2,9],"d":"1 <= d < q","h":[0,8]},
      "method":"exact integer and bitmask arithmetic, direct word-budget check vs interval-union certificate",
      "correctness_basis":"symbolic proof of the interval theorem and sharp switching family; randomized tests are validation, not proof of universal quantified statements"
    }
    Path(__file__).with_name('RESULT.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
    print(out['result'],trials,comparisons,family_instances,family_checks)

if __name__=="__main__":
    run()
