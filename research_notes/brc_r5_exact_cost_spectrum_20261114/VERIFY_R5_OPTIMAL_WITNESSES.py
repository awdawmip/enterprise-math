#!/usr/bin/env python3
"""Exact R5 optimal index-center set multiplicities and all-closure equality bands.

Companion data generator: VERIFY_R5_COST_SPECTRA.py.
Frozen science pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Author-side finite observer theorem; not a native X6 result.
"""
from VERIFY_R5_COST_SPECTRA import frozen,closed_points
from itertools import combinations
import json
import random

INF=10**12

def optimum_counts_spectrum(x):
    n=len(x);gap=max(x[i+1]-x[i] for i in range(n-1))
    incoming=[[] for _ in range(n)]
    for j in range(n):
        for i in range(j-1,-1,-1):
            if x[j]-x[i]>4+gap:break
            edge_cost=0
            for t in range(i+1,j):
                d=min(x[t]-x[i],x[j]-x[t])
                if d>2:break
                edge_cost+=d
            else:incoming[j].append((i,edge_cost))
    costs=[INF]*n;counts=[0]*n;suffix=[INF]*n
    for j in range(n):
        if x[j]-x[0]<=2:
            costs[j]=sum(x[j]-x[t] for t in range(j))
            counts[j]=1
        if x[-1]-x[j]<=2:
            suffix[j]=sum(x[t]-x[j] for t in range(j+1,n))
    out={}
    for k in range(1,n+1):
        if k>1:
            nxt=[INF]*n;cnt=[0]*n
            for j in range(n):
                for i,c in incoming[j]:
                    value=costs[i]+c
                    if value<nxt[j]:
                        nxt[j]=value;cnt[j]=counts[i]
                    elif value==nxt[j]:
                        cnt[j]+=counts[i]
            costs,counts=nxt,cnt
        best=INF;ways=0
        for j in range(n):
            value=costs[j]+suffix[j]
            if value<best:
                best=value;ways=counts[j]
            elif value==best:ways+=counts[j]
        if best<INF:out[k]=(best,ways)
    return out

def brute_small_sequences():
    rng=random.Random(20261114);checked=0
    for n in range(2,10):
        for _ in range(50):
            x=[0]
            for _ in range(n-1):x.append(x[-1]+rng.randint(1,4))
            dp=optimum_counts_spectrum(x)
            for k in range(1,n+1):
                costs=[]
                for ids in combinations(range(n),k):
                    distances=[min(abs(p-x[i]) for i in ids) for p in x]
                    if max(distances)<=2:costs.append(sum(distances))
                if costs:
                    best=min(costs);expect=(best,costs.count(best))
                    assert dp[k]==expect,(x,k,dp[k],expect)
                else:assert k not in dp
                checked+=1
    return checked

def main():
    x,cuts=frozen()
    spectra={
      "none":optimum_counts_spectrum(closed_points(x,cuts,0)),
      "all":optimum_counts_spectrum(closed_points(x,cuts,(1<<28)-1))
    }
    a=spectra["none"];b=spectra["all"]
    assert len(a)==742 and len(b)==748
    assert set(a)==set(range(213,955))
    assert set(b)==set(range(207,955))
    assert all(a[k][0]==b[k][0] for k in range(214,955))
    changed=[k for k in range(213,955) if a[k][1]!=b[k][1]]
    assert changed==[k for k in range(213,315) if k!=292]
    assert len(changed)==101
    assert a[214]==(1064,71400940037117596391178240000)
    assert b[214]==(1064,4573020854769248525038387200000)
    assert a[292]==b[292]==(744,247939829006869892620615680)
    assert a[315]==b[315]==(675,402907218691036544772341760000)
    assert a[954]==b[954]==(0,1)
    small=brute_small_sequences()
    assert small==2200
    output={
      "status":"PASS_EXACT_R5_OPTIMAL_INDEX_WITNESS_INVARIANCE",
      "science_pin":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
      "scope":"derived one-dimensional integer-event radius-two cover observer",
      "closure_patterns":1<<28,
      "common_budget_count":742,
      "endpoint_optimizer_count_difference_budgets":changed,
      "endpoint_optimizer_count_equal_budgets":[292]+list(range(315,955)),
      "all_pattern_identical_optimal_center_index_sets":{
        "isolated_budget":292,"continuous_range":[315,954],
        "proof":"Opt_empty subset Opt_B subset Opt_all for K>=214, equal finite cardinalities at endpoints"
      },
      "K214":{
        "cost":1064,"optimal_sets_none":str(a[214][1]),
        "optimal_sets_all":str(b[214][1]),
        "exact_ratio_all_to_none":"83005/1296"
      },
      "K292":{"cost":744,"optimal_sets_both":str(a[292][1])},
      "K314":{"cost":678,"optimal_sets_none":str(a[314][1]),
              "optimal_sets_all":str(b[314][1])},
      "K315":{"cost":675,"optimal_sets_both":str(a[315][1])},
      "K954":{"cost":0,"optimal_sets_both":"1"},
      "independent_brute_force_small_cases":small,
      "independent_math_review":"NOT_REVIEWED"
    }
    print(json.dumps(output,ensure_ascii=False,indent=2))
    return output

if __name__=="__main__":main()
