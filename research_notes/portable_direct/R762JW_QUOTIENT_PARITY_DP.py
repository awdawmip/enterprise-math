#!/usr/bin/env python3
"""R762JW exact quotient parity feasibility for five singleton supports of six-axis Port-Euler.
No optimizer, integer-only enumeration. Not an Euler connectivity proof.
"""
from itertools import combinations
from collections import Counter
import json
A=tuple(range(6))
P=tuple(combinations(A,2));S=tuple(combinations(A,3));PI={p:i for i,p in enumerate(P)}
SP=tuple(tuple(PI[x] for x in combinations(s,2)) for s in S)
MS=((),(PI[(0,1)],),(PI[(0,1)],PI[(2,3)]),(PI[(0,1)],PI[(2,3)],PI[(4,5)]))

def components(active, D):
    parent=list(range(15))
    def find(x):
        while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
        return x
    def union(x,y):
        x=find(x);y=find(y)
        if x!=y:parent[y]=x
    for s,sp in enumerate(SP):
        if s in D:continue
        if all(x in active for x in sp):union(sp[0],sp[1]);union(sp[1],sp[2])
    roots=sorted({find(x) for x in active})
    root_to_id={root:i for i,root in enumerate(roots)}
    comp={x:root_to_id[find(x)] for x in active}
    return comp,len(roots)

def evaluate(m,Ds):
    inactive=set(MS[m]); active=set(range(15))-inactive
    D=set(Ds); comp,c=components(active,D)
    smasks=[(None if len(ends:=tuple(x for x in sp if x in active))==0 else [((1<<comp[a])^(1<<comp[b])) for a,b in combinations(ends,2)]) for sp in SP]
    assert all(q is not None and len(q) in (1,3) for q in smasks)
    single={0}
    for s in Ds:
        single={a^b for a in single for b in smasks[s]}
    remaining=tuple(i for i in range(20) if i not in D)
    dp=[set() for _ in range(8)];dp[0]={0}
    for i,s in enumerate(remaining):
        o=smasks[s][0] if len(smasks[s])==1 else 0
        for k in range(min(i+1,7),0,-1):dp[k].update(x^o for x in dp[k-1])
    seven=dp[7]
    missing=seven-single
    return c,len(single),len(seven),len(missing),min(missing) if missing else None,len(single & seven),comp

def main():
    results=[]
    for m in range(4):
        counts=Counter();first=None;bad=0;total_bad_masks=0
        for D in combinations(range(20),5):
            c,a,b,f,ex,overlap,_=evaluate(m,D)
            counts[(c,a,b,f)]+=1
            if f:
                bad+=1;total_bad_masks+=f
                if first is None:first={'D':[S[i] for i in D],'components':c,'singleton_reachable_count':a,'forced_reachable_count':b,'unreachable_forced_masks':f,'example_mask':ex,'Dindices':list(D)}
        results.append({'m':m,'D_count':15504,'bad_D_count':bad,'total_unreachable_quotient_masks_across_D':total_bad_masks,'first_obstruction':first,'spectrum':{'/'.join(map(str,k)):v for k,v in sorted(counts.items())}})
        print('m',m,'bad',bad,'spectrum',results[-1]['spectrum'],'first',first,flush=True)
    with open('/mnt/data/r762jw_results.json','w') as f:json.dump({'schema':'R762JW_PARITY_QUOTIENT_SCREEN_V1','results':results},f,indent=2)

if __name__=='__main__':main()
