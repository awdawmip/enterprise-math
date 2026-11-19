#!/usr/bin/env python3
"""Exact R5 two-block witness carrier checker; Python stdlib only."""
import hashlib, itertools, json, sys
from pathlib import Path
H = (18,24,82,34,17,144,208)
SHA = '50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
def runs(bits, m):
    out=[]; i=0
    while i<m:
        if not (bits>>i)&1:
            i+=1; continue
        a=i
        while i+1<m and (bits>>(i+1))&1: i+=1
        out.append((a,i)); i+=1
    return out
def support(C,t):
    return sum(1<<i for i, row in enumerate(C) if any(a<=t<=b for a,b in row))
def maximal(masks):
    v=set(masks)-{0}
    return sorted(a for a in v if not any(a!=b and a&b==a for b in v))
def anchors(C):
    return maximal(support(C,t) for t in {a for row in C for a,b in row})
def direct(C,domain):
    return maximal(support(C,t) for t in domain)
def all_subsets(C,domain,B):
    n=len(C)
    for s in range(1,1<<n):
        truth=any(all(any(a<=t<=b for a,b in C[i])
                      for i in range(n) if s>>i&1) for t in domain)
        assert truth==any(s&b==s for b in B), (C,s)
def census():
    result={}
    for n,m in ((3,5),(4,4)):
        opts=[runs(x,m) for x in range(1,1<<m) if len(runs(x,m))<=2]
        cnt=0
        for C in itertools.product(opts,repeat=n):
            B=anchors(C)
            assert B==direct(C,range(m))
            all_subsets(C,range(m),B)
            cnt+=1
        result[f'{n}_states_{m}_responses']={'state_choices':len(opts),'families':cnt}
    return result
def two_block_family(n):
    C=[]
    for i in range(1,n+1):
        l,r=10*i-11,10*i+1
        parts=[]
        if l>=0:parts.append((0,l))
        if r<=10*n:parts.append((r,10*n))
        C.append(parts)
    return C
def high_helly():
    out=[]
    for n in range(3,13):
        C=two_block_family(n)
        allbut=[((1<<n)-1)^(1<<i) for i in range(n)]
        B=anchors(C)
        assert B==sorted(allbut)
        assert all(support(C,10*i-5)==allbut[i-1] for i in range(1,n+1))
        assert all(support(C,t)!=(1<<n)-1 for t in range(10*n+1))
        all_subsets(C,range(10*n+1),B)
        out.append({'n':n,'components_at_most':2,
                    'anchors':len({a for row in C for a,b in row}),
                    'maximal_supports':len(B),'minimal_missing_face_size':n})
    return out
def frozen_bridge(p, stages):
    raw=Path(p).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==SHA
    D=json.loads(raw)['counts_and_cohorts']; meta=json.loads(Path(stages).read_text())
    assert meta['frozen_sha256']==SHA
    T=[int(t) for t in meta['stage_taus']]
    assert len(T)==18
    pairs=((0,1),(0,49),(7,11),(11,14),(11,132),(15,16),(123,124),(250,255))
    budgets=(214,220,231,250,268,294,314)
    cases=0; max_seen=0
    for x,y in pairs:
        assert x<y and x not in H and y not in H
        slots=(18,24,82,34,17,x,144,208,y)
        for k in budgets:
            row=list(map(int,D[str(k)]['counts']))
            c=[row[s] for s in slots]
            for tau in T:
                C=[[(v,v+tau)] for v in c]
                B=anchors(C)
                brute=[]
                for s in range(1,512):
                    selected=[c[i] for i in range(9) if s>>i&1]
                    if max(selected)-min(selected)<=tau:brute.append(s)
                assert B==maximal(brute), (x,y,k,tau)
                cases+=1;max_seen=max(max_seen,len(B))
    return {'input_sha256':SHA,'named_pairs':len(pairs),'budgets':len(budgets),
            'stages':len(T),'support_families_checked':cases,
            'all_511_named_subsets_checked_per_family':True,
            'observed_maximal_supports_max':max_seen}
def main():
    res={'schema':'R5_EXACT_ENDPOINT_ANCHOR_CARRIER_V1',
         'finite_exhaustive':census(),'continuous_two_block_helly':high_helly(),
         'theorem':'Every nonempty feasible named subset has a joint witness at a component left endpoint; canonical antichain contains at most nr masks',
         'finite_method':'All ordered labeled families from <=2 contiguous discrete blocks per state; all nonempty subsets checked'}
    if len(sys.argv)==3:
        res['frozen_r5_bridge']=frozen_bridge(sys.argv[1],sys.argv[2])
    print(json.dumps(res,sort_keys=True,indent=2,ensure_ascii=False))
if __name__=='__main__':main()
