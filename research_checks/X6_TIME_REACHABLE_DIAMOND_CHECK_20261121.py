#!/usr/bin/env python3
"""Exact source-guarded event-order safety vs affine environment; no physical admission."""
from itertools import combinations, permutations, product
from math import factorial
import json

def run(actions, maps, x0):
    x=x0
    for i,r in actions:
        a,b=maps[(i,r)]
        x=a*x+b
    return x

def check(m,maps,x0):
    configs=0;traces=0;bad=[];max_outputs=1
    for q in product([-1,0,1,2],repeat=m):
        acts=[(i,r) for i,r in enumerate(q) if r>=0]
        values={run(seq,maps,x0) for seq in permutations(acts)}
        traces+=factorial(len(acts));configs+=1
        max_outputs=max(max_outputs,len(values))
        if len(values)>1:
            bad.append({"q":list(q),"outputs":sorted(values)})
    failures=[]
    for i,j in combinations(range(m),2):
        for r in range(3):
            for s in range(3):
                ai,bi=maps[(i,r)];aj,bj=maps[(j,s)]
                delta=(aj-1)*bi-(ai-1)*bj
                if delta: failures.append([i,r,j,s,delta])
    assert (len(bad)==0)==(len(failures)==0)
    return {"m":m,"configs":configs,"traces":traces,
            "unsafe_q_count":len(bad),
            "max_distinct_environment_outputs_per_q":max_outputs,
            "global_diamond_failures":len(failures),
            "first_bad":bad[0] if bad else None,
            "first_diamond_failure":failures[0] if failures else None}

def main():
    rows=[]
    for m in range(1,6):
        translations={(i,r):(1,3*i+r+1) for i in range(m) for r in range(3)}
        affine={(i,r):(i+1,r+1) for i in range(m) for r in range(3)}
        rows.append({"translation":check(m,translations,0),"affine":check(m,affine,0)})
    maps={(0,0):(1,1),(1,1):(2,0)}
    assert run([(0,0),(1,1)],maps,0)==2
    assert run([(1,1),(0,0)],maps,0)==1
    print(json.dumps({"schema":"X6_TIME_REACHABLE_DIAMOND_CERT_V1",
       "arithmetic":"exact integer affine maps; all labeled configurations and all orderings m=1..5",
       "rows":rows,"witness":{"m":2,"first_order":[[0,0],[1,1]],
       "first_final_environment":2,"second_order":[[1,1],[0,0]],
       "second_final_environment":1,"same_q":[0,1]},"mismatch_count":0},
       indent=2,ensure_ascii=False))
if __name__=="__main__":main()
