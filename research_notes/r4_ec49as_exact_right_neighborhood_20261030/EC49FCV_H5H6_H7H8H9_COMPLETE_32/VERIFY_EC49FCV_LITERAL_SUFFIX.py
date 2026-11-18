#!/usr/bin/env python3
"""Literal-prefix EC49FCV exact checker. Original frozen_model.py blob:
7e97065ac9a0ff70435b92ee2f4bd718c9bf1859. No integer bitsets.
"""
from frozen_model import build,primpref,candidates
from itertools import combinations,product
import json,sys,time

def minima(values):
    a=[]
    for x in sorted(set(values),key=lambda s:(len(s),tuple(sorted(s)))):
        if not any(y.issubset(x) for y in a):a.append(x)
    return a

def literal_run(keys,chosen,lit_pools):
    fixed=frozenset().union(*(primpref(w) for k,w in chosen.items() if k not in keys))
    cap=158-len(fixed)
    opts=[minima(p-fixed for p in lit_pools[k] if len(p-fixed)<cap) for k in keys]
    suffix=[frozenset()]*(len(keys)+1)
    mandatory=frozenset()
    for i in range(len(keys)-1,-1,-1):
        intersect=frozenset.intersection(*opts[i]) if opts[i] else frozenset()
        mandatory|=intersect
        suffix[i]=mandatory
    states=[frozenset()];sizes=[];tests=0
    for i,op in enumerate(opts):
        nexts=[]
        for state in states:
            for p in op:
                tests+=1
                m=state|p
                if len(m|suffix[i+1])<cap:nexts.append(m)
        states=minima(nexts)
        sizes.append(len(states))
        if not states:
            sizes.extend([0]*(len(keys)-i-1));break
    return {'fixed':len(fixed),'strict_cap':cap,'option_antichain_counts':[len(x) for x in opts],'states':sizes,'improvement':bool(states),'combination_tests':tests}

def main():
    indices=[int(v) for v in sys.argv[1:]] or [993]
    chosen,early,late,_,_=build()
    s7=[k for k in late if k.startswith('7:')]
    s8=[k for k in late if k.startswith('8:')]
    s9=[k for k in late if k.startswith('9:')]
    groups=[tuple(pair)+(a,b,c) for pair in combinations(early,2) for a,b,c in product(s7,s8,s9)]
    keys=set().union(*(set(groups[i]) for i in indices))
    pools={k:[frozenset(primpref(w)) for w in candidates(int(k.split(':')[0]))[int(k.split(':')[1])]] for k in keys}
    out=[];ts=time.perf_counter()
    for idx in indices:
        res=literal_run(groups[idx],chosen,pools)
        out.append({'index':idx,'slots':groups[idx], 'result':res})
        print(idx,res,'elapsed',round(time.perf_counter()-ts,3),flush=True)
    with open('EC49FCV_LITERAL_SUFFIX.json','w') as f:
        json.dump(out,f,sort_keys=True,indent=2)

if __name__=='__main__':main()
