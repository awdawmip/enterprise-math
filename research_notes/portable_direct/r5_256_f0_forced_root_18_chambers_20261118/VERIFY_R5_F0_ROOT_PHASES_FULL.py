#!/usr/bin/env python3
"""R5 full256, f=0: exact forced-first-action cost across all fifth-chamber signature intervals.
Usage: python VERIFY_R5_F0_ROOT_PHASES.py EXACT_R5_ALL_101_BUDGETS.json
Python standard library / integer exact. Frozen SHA is mandatory.
"""
import hashlib, json, sys, itertools
from functools import lru_cache
from pathlib import Path
HASH='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
LOW=25845652773852463277015040000
HIGH=58182461585441404127941754880
FULL=(1<<256)-1
A=tuple(range(214,315))

def maximal(supports):
    xs=set(supports)
    return tuple(sorted(s for s in xs if not any(s!=t and (s&t)==s for t in xs)))

def windows(ns,diameter):
    o=sorted(range(256),key=lambda i:(ns[i],i));r=0;ms=[]
    for l in range(256):
        r=max(r,l)
        while r<256 and ns[o[r]]-ns[o[l]]<=diameter:r+=1
        ms.append(sum(1<<o[j] for j in range(l,r)))
    return maximal(ms)

def event_sweep(ns,tau):
    # Exact endpoint sweep independent of sorted-window construction.
    endpoints=sorted(set(itertools.chain.from_iterable((2*n-tau,2*n+tau) for n in ns)))
    masks=[]
    for i,e in enumerate(endpoints):
        masks.append(sum(1<<h for h,n in enumerate(ns) if 2*n-tau<=e<=2*n+tau))
        if i+1<len(endpoints):
            midpoint_twice=e+endpoints[i+1]
            masks.append(sum(1<<h for h,n in enumerate(ns) if 2*(2*n-tau)<midpoint_twice<2*(2*n+tau)))
    return maximal(masks)

def evaluate(counts,tau,core):
    # Unrestricted Bellman: all 101 actions are evaluated at every state.
    C={k:windows(counts[k],tau) for k in A}
    for k in A:
        assert C[k]==event_sweep(counts[k],tau),(tau,k,'independent-support-disagreement')
    core=A
    INF=10**7
    @lru_cache(None)
    def V(S):
        if S.bit_count()<=1:return 0
        best=INF
        for k in core:
            if k>=best:break
            kids={S&b for b in C[k]}-{0}
            if S in kids: continue
            cand=k+max(V(t) for t in kids)
            if cand<best:best=cand
        return best
    optimal=V(FULL)
    forced={}
    for k in A:
        children={FULL&b for b in C[k]}-{0}
        forced[k]=k+max(V(s) for s in children)
    assert min(forced.values())==optimal
    return {'tau_from_inclusive':str(tau),'optimal':optimal,
        'optimal_first_budgets':[k for k in A if forced[k]==optimal],
        'core':list(core),'forced_root_costs':{str(k):forced[k] for k in A},
        'noncore_optimal_first':[k for k in A if k not in core and forced[k]==optimal],
        'dp_states':V.cache_info().currsize,
        'min_forced_root_regret_positive':min((v-optimal for v in forced.values() if v>optimal),default=None)}

def main():
    raw=Path(sys.argv[1]).read_bytes();assert hashlib.sha256(raw).hexdigest()==HASH
    table=json.loads(raw);assert table['budget_range']==[214,314]
    counts={k:tuple(map(int,table['counts_and_cohorts'][str(k)]['counts'])) for k in A}
    changes=set()
    for k in A:
        vals=sorted(set(counts[k]))
        for i,a in enumerate(vals):
            for b in vals[i+1:]:
                d=b-a
                if LOW<d<HIGH:changes.add(d)
    points=[LOW]+sorted(changes)
    assert len(points)==18 and points[0]==LOW and points[-1]<HIGH and points==sorted(set(points))
    results=[evaluate(counts,t,A) for t in points]
    assert all(v['optimal']==735 for v in results)
    distinct=[]
    for p in results:
        if not distinct or p['optimal_first_budgets']!=distinct[-1]['roots']:
            distinct.append({'from':p['tau_from_inclusive'],'roots':p['optimal_first_budgets']})
    summary={
        'status':'PASS_R5_FULL256_F0_FORCED_ROOT_FIFTH_CHAMBERS',
        'science_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
        'table_sha256':HASH,'state_ids':'0..255','action_budgets':'214..314',
        'tau_domain':'[25845652773852463277015040000,58182461585441404127941754880)',
        'support_threshold_chambers':len(points),
        'support_checks':len(points)*len(A),
        'all_chamber_optimum':735,
        'optimal_first_action_regions':distinct,
        'endpoint_root_forced_costs':results[-1]['forced_root_costs'],
        'detail':results,
        'uncertainty_scope':'arbitrary tau_i per query in [L,U) uses last chamber endpoint tau=U-1; adaptive zero-corruption minimax',
        'review':'NOT_REVIEWED'
    }
    print(json.dumps(summary,ensure_ascii=False,indent=2,sort_keys=True))
    print(summary['status'],file=sys.stderr)
if __name__=='__main__':main()
