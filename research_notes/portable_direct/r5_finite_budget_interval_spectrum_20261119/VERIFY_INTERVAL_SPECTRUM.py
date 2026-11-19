#!/usr/bin/env python3
"""Finite-horizon budget spectrum: exact word-interval vs independent replay."""
import itertools
import json
import random
from collections import Counter

def words(actions, horizon):
    for length in range(horizon+1):
        yield from itertools.product(range(actions), repeat=length)

def one_word(word, trans, cost, label, x, Y):
    states = [x, *Y]
    totals = [0]*len(states)
    compatible = [(label[x] & ~label[y]) == 0 for y in Y]
    for action in word:
        for i, state in enumerate(states):
            totals[i] += cost[action][state]
            states[i] = trans[action][state]
        for i in range(len(Y)):
            compatible[i] = compatible[i] and (label[states[0]] & ~label[states[i+1]]) == 0
    valid_costs = [totals[i+1] for i, valid in enumerate(compatible) if valid]
    return totals[0], min(valid_costs) if valid_costs else None

def bad_intervals(trans, cost, label, x, Y, horizon):
    raw = []
    for w in words(len(trans), horizon):
        original, best = one_word(w, trans, cost, label, x, Y)
        if best is None or best > original:
            raw.append((original, None if best is None else best-1))
    raw.sort(key=lambda p: (p[0], p[1] is None, 0 if p[1] is None else p[1]))
    merged=[]
    for lo, hi in raw:
        if merged and (merged[-1][1] is None or lo <= merged[-1][1]+1):
            last_lo,last_hi=merged[-1]
            merged[-1] = (last_lo,None if last_hi is None or hi is None else max(last_hi,hi))
        else:
            merged.append((lo,hi))
    return merged

def direct_safe(B, trans, cost, label, x, Y, horizon):
    # Separate budget-first replay, with no use of one_word() or bad_intervals().
    for word in words(len(trans), horizon):
        source=x
        source_spent=0
        for a in word:
            source_spent += cost[a][source]
            source=trans[a][source]
        if source_spent>B:
            continue
        witnessed=False
        for y in Y:
            src,dst,spent=x,y,0
            valid=(label[src] & ~label[dst])==0
            for a in word:
                spent += cost[a][dst]
                src=trans[a][src]
                dst=trans[a][dst]
                valid=valid and (label[src] & ~label[dst])==0
            if valid and spent<=B:
                witnessed=True
                break
        if not witnessed:
            return False
    return True

def certificate_safe(B, intervals):
    return not any(lo<=B and (hi is None or B<=hi) for lo,hi in intervals)

def check():
    N=0; checks=0; histogram=Counter(); infinite=0; max_components=0
    # Exhaustive class 27*64*8 = 13,824, one action, H=5.
    for t in itertools.product(range(3),repeat=3):
        for L in itertools.product(range(4),repeat=3):
            for c in itertools.product(range(2),repeat=3):
                T=(t,); C=(c,)
                intervals=bad_intervals(T,C,L,0,(1,2),5)
                histogram[len(intervals)]+=1
                infinite+=int(bool(intervals and intervals[-1][1] is None))
                max_components=max(max_components,len(intervals))
                for B in range(9):
                    assert certificate_safe(B,intervals)==direct_safe(B,T,C,L,0,(1,2),5), (t,L,c,B)
                    checks+=1
                N+=1
    assert N==13824 and checks==124416
    # Deterministic 4-state, 2-action sample; fixed seed and scope.
    rng=random.Random(20261119)
    multi=4096; multi_checks=0
    for _ in range(multi):
        T=tuple(tuple(rng.randrange(4) for _ in range(4)) for a in range(2))
        C=tuple(tuple(rng.randrange(3) for _ in range(4)) for a in range(2))
        L=tuple(rng.randrange(4) for _ in range(4))
        Y=tuple(y for y in (1,2,3) if rng.randrange(2)) or (1,)
        intervals=bad_intervals(T,C,L,0,Y,4)
        for B in range(11):
            assert certificate_safe(B,intervals)==direct_safe(B,T,C,L,0,Y,4)
            multi_checks+=1
    # Unary sharpness witness q=2, d=1, H=8.
    T=((0,2,2),); C=((2,3,2),); L=(1,1,1)
    actual=bad_intervals(T,C,L,0,(1,),8)
    expected=[(2*t,2*t) for t in range(1,9)]
    assert actual==expected
    for B in range(26):
        assert certificate_safe(B,actual)==direct_safe(B,T,C,L,0,(1,),8)
    result={
        "schema":"R5_FINITE_HORIZON_BUDGET_INTERVAL_RESULT_V1",
        "status":"AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED",
        "scientific_pin":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
        "unary_exhaustive":{"models":N,"budget_checks":checks,"states":3,"actions":1,"horizon":5,
            "label_bits":2,"cost_values":[0,1],"component_histogram":dict(sorted(histogram.items())),
            "infinite_bad_models":infinite,"max_components":max_components},
        "two_action_sample":{"seed":20261119,"models":multi,"budget_checks":multi_checks,
            "states":4,"actions":2,"horizon":4,"label_bits":2,"cost_values":[0,1,2]},
        "sharp_unary_example":{"q":2,"d":1,"horizon":8,
            "bad_intervals":expected,"permanently_safe_from":17}
    }
    print("PASS_R5_INTERVAL_SPECTRUM",N,checks,multi,multi_checks,max_components,infinite)
    return result

if __name__=="__main__":
    print(json.dumps(check(),sort_keys=True,ensure_ascii=False))
