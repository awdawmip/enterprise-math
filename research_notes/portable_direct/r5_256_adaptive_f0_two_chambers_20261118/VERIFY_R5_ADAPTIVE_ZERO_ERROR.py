#!/usr/bin/env python3
"""Exact finite certified zero-corruption adaptive minimax, frozen 256-state R5 observer.

Usage: python VERIFY_R5_ADAPTIVE_ZERO_ERROR.py EXACT_R5_ALL_101_BUDGETS.json
Uses only standard Python library and arbitrary-precision integers.
"""
import hashlib, itertools, json, sys
from functools import lru_cache
from pathlib import Path

EXPECTED_SHA='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
L=25845652773852463277015040000
U=58182461585441404127941754880
T=1876919155234970890319953920000
D=1882951873548292168718745600000
A=tuple(range(214,315))
FULL=(1<<256)-1
INF=1_000_000

def maximal(support_sets):
    unique=set(support_sets)
    return tuple(sorted(m for m in unique if not any(m!=n and (m&n)==m for n in unique)))

def support_windows(ns,tau):
    order=sorted(range(256),key=lambda h:(ns[h],h)); r=0; masks=[]
    for l in range(256):
        r=max(r,l)
        while r<256 and ns[order[r]]-ns[order[l]]<=tau:r+=1
        masks.append(sum(1<<order[t] for t in range(l,r)))
    return maximal(masks)

def support_endpoint_sweep(ns,tau):
    # Observation z=2*y is correct for h iff 2*N_h-tau<=z<=2*N_h+tau.
    # At an event endpoint, closed intervals on both sides may meet exactly.
    events=sorted(set(itertools.chain.from_iterable(((2*n-tau),(2*n+tau)) for n in ns)))
    candidate=[]
    for i,z in enumerate(events):
        candidate.append(sum(1<<h for h,n in enumerate(ns) if 2*n-tau<=z<=2*n+tau))
        if i+1<len(events):
            zz=z+events[i+1] # midpoint in units of 2*z
            candidate.append(sum(1<<h for h,n in enumerate(ns) if 2*(2*n-tau)<zz<2*(2*n+tau)))
    return maximal(candidate)

def solve(counts,tau,depth,bound):
    C={k:support_windows(counts[k],tau) for k in A}
    # Cross-check all 101 response-support families using an independently
    # derived sweep of closed correct-response intervals.
    for k in A:
        assert C[k]==support_endpoint_sweep(counts[k],tau),(tau,k,'support disagreement')
    choice={}; calls=[0]; transitions=[0]
    @lru_cache(None)
    def V(S,d):
        calls[0]+=1
        if S.bit_count()<=1:return 0
        if d==0:return INF
        best=INF;which=None
        for k in A:
            if k>=best:break
            worst=0
            for region in C[k]:
                child=S&region
                if not child:continue
                transitions[0]+=1
                # If an outcome leaves S unchanged, the query cannot reduce
                # the worst-case cost of a positive-cost minimax strategy.
                if child==S:worst=INF;break
                w=V(child,d-1)
                worst=max(worst,w)
                if k+worst>=best:break
            if k+worst<best:best=k+worst;which=k
        if which is not None:choice[(S,d)]=which
        return best
    best=V(FULL,depth)
    assert best<INF,(tau, 'no finite policy')
    assert best<=bound,(tau,best,bound)
    roots=[]
    for k in A:
        if k>best:break
        if FULL in C[k]:continue
        worst=max(V(region,depth-1) for region in C[k])
        if k+worst==best:roots.append(k)
    # Reconstruct and exhaustively verify an actual worst-case policy.
    seen=set(); budgets=set(); ends=[]
    def audit(S,d):
        if S.bit_count()<=1:
            ends.append(0);return 0
        node=(S,d)
        if node in seen:return V(S,d)
        seen.add(node)
        k=choice[node];budgets.add(k)
        children=set(S&region for region in C[k])-{0}
        assert all(child!=S for child in children)
        child_costs=[audit(child,d-1) for child in children]
        assert k+max(child_costs)==V(S,d)
        return k+max(child_costs)
    assert audit(FULL,depth)==best
    return {'tau':str(tau),'depth_max':depth,'optimal_cost':best,'optimal_first_budgets':roots,
        'root_support_counts':{str(k):len(C[k]) for k in roots},
        'dp_cached_states':V.cache_info().currsize,'dp_transitions_evaluated':transitions[0],
        'policy_unique_states':len(seen),'policy_budget_types':sorted(budgets),
        'max_policy_actions':max((d for s,d in seen),default=0),'min_query_cost':214,
        'safe_decoding_rule':'stop when exactly one named hypothesis remains compatible',
        'response_model':'all closed intervals [N_h(k)-tau/2,N_h(k)+tau/2], zero corruptions'}

def main():
    path=Path(sys.argv[1]); raw=path.read_bytes(); assert hashlib.sha256(raw).hexdigest()==EXPECTED_SHA
    data=json.loads(raw);assert data['budget_range']==[214,314]
    counts={k:tuple(int(v) for v in data['counts_and_cohorts'][str(k)]['counts']) for k in A}
    assert all(len(v)==256 for v in counts.values())
    probes=[('fifth_left',L,3,735),('fifth_right_last_integer',U-1,3,735),
            ('near_critical_left',T,4,957),('near_critical_right_last_integer',D-1,4,957)]
    results={name:solve(counts,tau,d,b) for name,tau,d,b in probes}
    assert all(results[z]['optimal_cost']==735 for z in ('fifth_left','fifth_right_last_integer'))
    assert all(results[z]['optimal_cost']==955 for z in ('near_critical_left','near_critical_right_last_integer'))
    assert results['fifth_left']['optimal_first_budgets']==[216,223,296]
    assert results['near_critical_left']['optimal_first_budgets']==[215,224,298]
    ans={'status':'PASS_R5_256_ADAPTIVE_F0_EXACT_TWO_CHAMBERS',
         'frozen_science_commit':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
         'frozen_json_sha256':EXPECTED_SHA,
         'hypotheses':256,'queries':101,
         'fifth_exact_cost_all_real_tau':735,'near_critical_exact_cost_all_real_tau':955,
         'near_critical_prepaid_fixed_batch_cost':957,
         'monotonic_extension':'Each endpoint minimax value is monotone in tau; with equal endpoint values it holds throughout the closed-left/open-right interval.',
         'endpoint_results':results}
    print(json.dumps(ans,ensure_ascii=False,sort_keys=True,indent=2))
    print(ans['status'],file=sys.stderr)

if __name__=='__main__':main()
