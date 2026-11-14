#!/usr/bin/env python3
"""Exact R5 two-cut optimizer counts from frozen 1D coordinates; radius=2."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from random import Random
import json
from pathlib import Path

W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
PIN="435e77af0d180eac32bd1f9c4c464bc4010b7551"
INF=10**18

def frozen():
    pools={3:set(),12:set(),15:set()}
    n=k=mask=0
    for t in range(1,1<<15):
        bit=t&-t; i=bit.bit_length()-1; mask^=bit
        sign=1 if mask&bit else -1
        n+=sign*W[i]; k+=sign*K0[i]
        if n>=3 and k%36==0 and k//36 in pools:
            pools[k//36].add(n)
    assert [len(pools[q]) for q in (3,12,15)]==[538,298,229]
    events=Counter(Fraction(p,q) for q,nums in pools.items() for p in nums)
    x=[0]
    for v in sorted(events): x.append(x[-1]+events[v])
    cuts=[i for i in range(len(x)-1) if x[i+1]-x[i]>2]
    assert len(x)==954 and x[-1]==1065 and len(cuts)==28
    return x,cuts

def closed(x,cuts,mask):
    S={cuts[i] for i in range(28) if mask>>i&1}
    shift=0; y=[]
    for i,v in enumerate(x):
        y.append(v-shift)
        if i in S: shift+=1
    return y

def optimum_counts(x,maxK=315):
    n=len(x)
    cutoff=4+max(x[i+1]-x[i] for i in range(n-1))
    incoming=[[] for _ in range(n)]
    for j in range(n):
        for i in range(j-1,-1,-1):
            if x[j]-x[i]>cutoff: break
            mid=[min(x[t]-x[i],x[j]-x[t]) for t in range(i+1,j)]
            if not mid or max(mid)<=2: incoming[j].append((i,sum(mid)))
    suffix=[None]*n
    for j in range(n):
        if x[-1]-x[j]<=2:
            suffix[j]=sum(x[t]-x[j] for t in range(j+1,n))
    cost=[INF]*n; count=[0]*n
    for j in range(n):
        if x[j]-x[0]<=2:
            cost[j]=sum(x[j]-x[t] for t in range(j));count[j]=1
    out={}
    for k in range(1,min(maxK,n)+1):
        if k>1:
            nc=[INF]*n; nn=[0]*n
            for j in range(n):
                for i,e in incoming[j]:
                    if not count[i]: continue
                    v=cost[i]+e
                    if v<nc[j]: nc[j]=v; nn[j]=count[i]
                    elif v==nc[j]: nn[j]+=count[i]
            cost,count=nc,nn
        best=INF; ways=0
        for j,z in enumerate(suffix):
            if z is None or not count[j]: continue
            v=cost[j]+z
            if v<best: best=v; ways=count[j]
            elif v==best: ways+=count[j]
        if ways: out[k]=(best,ways)
    return out

def brute(x):
    out={}
    for k in range(1,len(x)+1):
        values=[]
        for inds in combinations(range(len(x)),k):
            ds=[min(abs(x[t]-x[i]) for i in inds) for t in range(len(x))]
            if max(ds)<=2: values.append(sum(ds))
        if values: out[k]=(min(values),values.count(min(values)))
    return out

def verify():
    rng=Random(253467)
    for n in range(3,9):
        for _ in range(18):
            x=[0]
            for _ in range(n-1): x.append(x[-1]+rng.randrange(1,5))
            assert optimum_counts(x,n)==brute(x)
    x,cuts=frozen()
    ALL=(1<<28)-1
    OTHER=ALL^((1<<15)|(1<<17))
    backgrounds=[0,1<<8,1<<16,(1<<8)|(1<<9)|(1<<12)|(1<<13)|(1<<16),OTHER]
    summaries=[]
    for bg in backgrounds:
        cases={}
        for name,mask in (("00",bg),("10",bg|(1<<15)),
                          ("01",bg|(1<<17)),("11",bg|(1<<15)|(1<<17))):
            cases[name]=optimum_counts(closed(x,cuts,mask))
        data={}
        for k in range(292,316):
            assert all(k in v for v in cases.values())
            J={v[k][0] for v in cases.values()}
            assert len(J)==1
            q={name:v[k][1] for name,v in cases.items()}
            assert q["00"]<=q["10"]<=q["11"] and q["00"]<=q["01"]<=q["11"]
            data[k]={"J":J.pop(),"N00":q["00"],"A15":q["10"]-q["00"],
                     "A17":q["01"]-q["00"],
                     "Gamma":q["11"]-q["10"]-q["01"]+q["00"]}
        summaries.append(data)
    assert all(z==summaries[0] for z in summaries)
    ref=summaries[0]
    assert [k for k in ref if ref[k]["A15"]>0]==list(range(293,315))
    assert [k for k in ref if ref[k]["A17"]>0]==list(range(293,315))
    assert [k for k in ref if ref[k]["Gamma"]>0]==list(range(294,314))
    assert all(ref[k]["Gamma"]>=0 for k in ref)
    assert ref[293]["J"]==741
    assert ref[293]["N00"]==12606779601463240519046922240
    assert ref[293]["A15"]==ref[293]["A17"]==495879658013739785241231360
    assert ref[294]["Gamma"]==991759316027479570482462720
    return {"status":"PASS_EXACT_R5_TWO_GAP_CONTEXT_EXPERIMENT","science_pin":PIN,
            "events":len(x),"radius":2,"examined_masks":20,
            "exact_budget_range":[292,315],"bruteforced_small_instances":108,
            "rows":[dict(K=k,J=rec["J"],N00=str(rec["N00"]),
                    A15=str(rec["A15"]),A17=str(rec["A17"]),
                    Gamma=str(rec["Gamma"])) for k,rec in ref.items()],
            "independent_review":"NOT_REVIEWED"}

if __name__=="__main__":
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
