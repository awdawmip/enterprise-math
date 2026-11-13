#!/usr/bin/env python3
"""Exact finite test of radius-R single-gap closure theorem.
No external dependencies; center candidates are event coordinates and objective is sum of nearest distances.
"""
from itertools import combinations
from collections import Counter
from json import dump

def frontier(x, radius):
    n=len(x); best={}
    for k in range(1,n+1):
        for ids in combinations(range(n), k):
            ds=[min(abs(y-x[i]) for i in ids) for y in x]
            if max(ds)>radius: continue
            cost=sum(ds)
            if cost<best.get(k,10**15):best[k]=cost
    return best

def evaluate(x, cut, radius):
    assert x[cut+1]-x[cut]==radius+1
    y=x[:cut+1]+tuple(t-1 for t in x[cut+1:])
    old=frontier(x,radius); new=frontier(y,radius)
    oldmin=min(old); newmin=min(new)
    assert oldmin-1<=newmin<=oldmin, (x,cut,radius,oldmin,newmin)
    for k,cost in old.items():
        assert new[k]<=cost,(x,cut,radius,k,old,new)
        if k+1 in old:
            assert new[k]>=min(cost,old[k+1]+radius),(x,cut,radius,k,old,new)
            if cost-old[k+1]<=radius:
                assert new[k]==cost,(x,cut,radius,k,old,new)
        if k==len(x):assert new[k]==cost==0
    return old,new

def main():
    cases=checks=stable=improvements=potential_not_sufficient=0
    witnesses={}
    # all sorted integer sequences with first coordinate 0, 2..7 distinct coordinates
    for radius in (1,2,3):
        for n in range(2,8):
            for tail in combinations(range(1,11),n-1):
                x=(0,)+tail
                for cut in range(n-1):
                    if x[cut+1]-x[cut]!=radius+1: continue
                    old,new=evaluate(x,cut,radius)
                    cases+=1
                    for k,old_cost in old.items():
                        checks+=1
                        if old_cost==new[k]:stable+=1
                        else:
                            improvements+=1
                            witnesses.setdefault('strict_improvement',{'radius':radius,'x':x,'cut':cut,'k':k,'old':old_cost,'new':new[k], 'old_gain':old_cost-old.get(k+1,old_cost)})
                        if k+1 in old and old_cost-old[k+1]>radius and new[k]==old_cost:
                            potential_not_sufficient+=1
                            witnesses.setdefault('gain_exceeds_radius_but_stable',{'radius':radius,'x':x,'cut':cut,'k':k,'old':old_cost,'new':new[k], 'gain':old_cost-old[k+1]})
    assert improvements>0 and potential_not_sufficient>0
    data={'status':'PASS_EXHAUSTIVE_FINITE','test_domain':'R in {1,2,3}, N in [2,7], x0=0 and other x in {1,...,10}, all adjacent gaps R+1 tested','cases':cases,'budget_checks':checks,'unchanged_budget_values':stable,'strict_improvements':improvements,'large_gain_stable_checks':potential_not_sufficient,'witnesses':witnesses}
    with open('EXACT_OUTPUT.json','w') as f:dump(data,f,indent=2,ensure_ascii=False)
    print(data)
if __name__=='__main__':main()
