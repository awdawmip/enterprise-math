#!/usr/bin/env python3
"""Exact finite depth-2 policy enumeration vs cost-visible wordwise criterion."""
from itertools import product
from random import Random
from pathlib import Path
import json
STOP=-1

def word_cost_obs(T,O,C,z,w):
    s=z; cost=0; os=[O[s]]; costs=[0]
    for a in w:
        cost+=C[a][s];s=T[a][s];os.append(O[s]);costs.append(cost)
    return os,costs

def wordwise_cost_visible(T,O,C,x,Y,H,B):
    for t in range(H+1):
        for word in product(range(len(T)),repeat=t):
            ox,cx=word_cost_obs(T,O,C,x,word)
            if cx[-1]>B:continue
            found=False
            for y in Y:
                oy,cy=word_cost_obs(T,O,C,y,word)
                if oy!=ox or cy[-1]>B:continue
                if (cy[:t+1] if t<H else cy[:t])==(cx[:t+1] if t<H else cx[:t]):
                    found=True;break
            if not found:return False
    return True

def wordwise_ordinary(T,O,C,x,Y,H,B):
    for t in range(H+1):
        for word in product(range(len(T)),repeat=t):
            ox,cx=word_cost_obs(T,O,C,x,word)
            if cx[-1]>B:continue
            if not any((lambda oy,cy:oy==ox and cy[-1]<=B)(*word_cost_obs(T,O,C,y,word)) for y in Y):
                return False
    return True

def run_policy(T,O,C,z,root,second,H=2):
    obs=[O[z]];w=[];spend=0;st=z
    a=root[O[st]]
    if a==STOP:return (tuple(w),tuple(obs)),0
    w.append(a);spend+=C[a][st];st=T[a][st];obs.append(O[st])
    key=(obs[0],a,obs[-1],spend)
    a1=second[key]
    if a1!=STOP:
        w.append(a1);spend+=C[a1][st];st=T[a1][st];obs.append(O[st])
    return (tuple(w),tuple(obs)),spend

def adaptive_cost_visible(T,O,C,x,Y,B):
    choices=[STOP]+list(range(len(T)))
    for root_tuple in product(choices,repeat=len(set(O))):
        root=dict(zip(sorted(set(O)),root_tuple))
        keys=set()
        for z in [x]+list(Y):
            a=root[O[z]]
            if a!=STOP:
                s=T[a][z];keys.add((O[z],a,O[s],C[a][z]))
        keys=sorted(keys)
        for ch in product(choices,repeat=len(keys)):
            second=dict(zip(keys,ch))
            trace_x,cx=run_policy(T,O,C,x,root,second)
            if cx>B:continue
            if not any((lambda tr,cy:tr==trace_x and cy<=B)(*run_policy(T,O,C,y,root,second)) for y in Y):
                return False
    return True

def main():
    T=[[0,1]];O=[0,0];C=[[1,2]];x=0;Y=[1];H=2;B=4
    assert wordwise_ordinary(T,O,C,x,Y,H,B)
    assert not wordwise_cost_visible(T,O,C,x,Y,H,B)
    assert not adaptive_cost_visible(T,O,C,x,Y,B)
    seed=20261119;rng=Random(seed);comparisons=0;ordinary_strict=0
    for _ in range(600):
        n=rng.choice([2,3]);aa=rng.choice([1,2])
        T=[[rng.randrange(n) for _ in range(n)] for _ in range(aa)]
        O=[rng.randrange(2) for _ in range(n)]
        C=[[rng.randrange(3) for _ in range(n)] for _ in range(aa)]
        x=rng.randrange(n)
        Y=[i for i in range(n) if i!=x]
        for B in range(5):
            cv=wordwise_cost_visible(T,O,C,x,Y,2,B)
            adaptive=adaptive_cost_visible(T,O,C,x,Y,B)
            assert cv==adaptive,(T,O,C,x,Y,B,cv,adaptive)
            ordinary_strict+=wordwise_ordinary(T,O,C,x,Y,2,B) and not adaptive
            comparisons+=1
    result={
      "schema":"R5_COST_VISIBLE_ADAPTIVE_BRIDGE_V1",
      "result":"PASS_R5_COST_VISIBLE",
      "random_seed":seed,
      "random_systems":600,
      "budget_comparisons":comparisons,
      "ordinary_wordwise_safe_but_cost_adaptive_unsafe":ordinary_strict,
      "example":{"T":[[0,1]],"O":[0,0],"cost":[[1,2]],"x":0,"Y":[1],"H":2,"B":4},
      "method":"full policy-tree decision enumeration at H=2 vs independent wordwise cost-history criterion; exact integer/Boolean comparisons"
    }
    Path(__file__).with_name('RESULT_COST_VISIBLE.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['result'],comparisons,ordinary_strict)

if __name__=="__main__":main()
