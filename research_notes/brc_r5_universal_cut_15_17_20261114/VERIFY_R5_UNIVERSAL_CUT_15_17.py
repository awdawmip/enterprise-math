#!/usr/bin/env python3
"""R5 exact all-context strict optimizer expansion for cuts 15 and 17.

Frozen science input: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Derived event-index radius-two observer. Standard-library-only exact arithmetic.
This script does not claim native-X6 execution or independent review.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from bisect import bisect_left
from random import Random
import hashlib
import json

W = (336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0 = (-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
PIN = '435e77af0d180eac32bd1f9c4c464bc4010b7551'
INF = 10**12


def frozen():
    pools = {3:set(),12:set(),15:set()}
    n = k = mask = 0
    for t in range(1, 1<<15):
        bit = t & -t
        i = bit.bit_length()-1
        mask ^= bit
        sign = 1 if mask & bit else -1
        n += sign * W[i]
        k += sign * K0[i]
        if n >= 3 and k % 36 == 0 and k//36 in pools:
            pools[k//36].add(n)
    assert [len(pools[q]) for q in (3,12,15)] == [538,298,229]
    events = Counter(Fraction(p,q) for q,values in pools.items() for p in values)
    x = [0]
    for v in sorted(events):
        x.append(x[-1]+events[v])
    cuts = [i for i in range(len(x)-1) if x[i+1]-x[i] == 3]
    assert (len(x),x[-1],len(cuts)) == (954,1065,28)
    assert max(b-a for a,b in zip(x,x[1:])) == 3
    return x,cuts


def close(x,cuts,mask):
    changed = {cuts[i] for i in range(len(cuts)) if mask>>i & 1}
    out=[]
    shift=0
    for j,v in enumerate(x):
        out.append(v-shift)
        if j in changed: shift+=1
    return out


def score(x,centers):
    selected=[x[j] for j in centers]
    value=0
    longest=0
    for p in x:
        pos=bisect_left(selected,p)
        left=p-selected[pos-1] if pos else INF
        right=selected[pos]-p if pos<len(selected) else INF
        d=min(left,right)
        longest=max(longest,d)
        value+=d
    return longest,value


def shortest_center_paths(x, max_budget, forced=None, forbidden=frozenset(), recover=()):
    """Exact last-center path DP; force a center by preventing skipped edges."""
    n=len(x)
    jump=4+max(b-a for a,b in zip(x,x[1:]))
    incoming=[[] for _ in range(n)]
    for j in range(n):
        for i in range(j-1,-1,-1):
            if x[j]-x[i]>jump: break
            w=0
            for t in range(i+1,j):
                d=min(x[t]-x[i],x[j]-x[t])
                if d>2:break
                w+=d
            else:
                if forced is None or not (i<forced<j):
                    incoming[j].append((i,w))
    cost=[INF]*n
    parent=[[-1]*n]
    for j in range(n):
        if j not in forbidden and x[j]-x[0]<=2 and (forced is None or j<=forced):
            cost[j]=sum(x[j]-x[t] for t in range(j))
    answers={}
    witnesses={}
    wanted=set(recover)
    for k in range(1,max_budget+1):
        if k>1:
            nxt=[INF]*n
            prev=[-1]*n
            for j in range(n):
                if j in forbidden: continue
                for i,w in incoming[j]:
                    c=cost[i]+w
                    if c<nxt[j]:
                        nxt[j]=c
                        prev[j]=i
            cost=nxt
            parent.append(prev)
        best=INF
        last=-1
        for j in range(n):
            if (forced is not None and j<forced) or x[-1]-x[j]>2: continue
            c=cost[j]+sum(x[t]-x[j] for t in range(j+1,n))
            if c<best:
                best=c
                last=j
        if best<INF:
            answers[k]=best
            if k in wanted:
                chain=[]
                cur=last
                for layer in range(k,0,-1):
                    chain.append(cur)
                    cur=parent[layer-1][cur]
                chain.reverse()
                assert len(chain)==k and len(set(chain))==k
                witnesses[k]=chain
    return answers,witnesses


def brute(x,forced,forbidden):
    result={}
    for k in range(1,len(x)+1):
        best=INF
        for centers in combinations(range(len(x)),k):
            if forced is not None and forced not in centers: continue
            if any(j in centers for j in forbidden): continue
            radius,cost=score(x,centers)
            if radius<=2: best=min(best,cost)
        if best<INF:result[k]=best
    return result


def main():
    x,cuts=frozen()
    assert cuts[15]==194 and cuts[17]==245
    rng=Random(2819)
    small=0
    for n in range(4,10):
        for _ in range(25):
            y=[0]
            for j in range(n-1): y.append(y[-1]+rng.randint(1,4))
            q=rng.randrange(n)
            forbidden=set(rng.sample([a for a in range(n) if a!=q],rng.randrange(min(3,n-1)+1)))
            calc,_=shortest_center_paths(y,n,forced=q,forbidden=forbidden)
            assert calc==brute(y,q,forbidden)
            small+=1
    report={'status':'PASS_EXACT_R5_UNIVERSAL_CUT_15_17_STRICTNESS',
            'science_pin':PIN,'event_count':len(x),
            'scope':'frozen derived integer radius-2 indexed-center observer',
            'all_contexts':1<<27,'budget_interval':[293,314],
            'small_exhaustive_cases':small,'cut_results':{},
            'independent_math_review':'NOT_REVIEWED'}
    for cut in (15,17):
        y=close(x,cuts,1<<cut)
        boundary=cuts[cut]
        baseline,_=shortest_center_paths(y,315)
        constrained,certs=shortest_center_paths(
            y,315,forced=boundary+1,
            forbidden={boundary-2,boundary-1,boundary},recover=range(293,315))
        assert len(certs)==22
        exact_scores=[]
        masks=[]
        swap_masks=[]
        for K in range(293,315):
            assert constrained[K]==baseline[K]==1620-3*K
            S=certs[K]
            assert {boundary-2,boundary-1,boundary}.isdisjoint(S)
            assert boundary+1 in S
            assert score(y,S)==(2,baseline[K])
            assert score(x,S)[0]>2
            assert boundary-3 in S
            corrected=sorted((set(S)-{boundary-3})|{boundary-2})
            assert len(corrected)==K and score(x,corrected)==(2,baseline[K])
            swap_masks.append(format(sum(1<<j for j in corrected),'0240x'))
            mask=sum(1<<j for j in S)
            masks.append(format(mask,'0240x'))
            exact_scores.append(baseline[K])
        # Independent closure-background checks are regression tests; the
        # all-2^27 theorem follows from the local-cut witness argument.
        checks=0
        for K in range(293,315):
            for _ in range(25):
                B=rng.randrange(1<<28)&~(1<<cut)
                a=close(x,cuts,B)
                b=close(x,cuts,B|(1<<cut))
                assert score(b,certs[K])==(2,1620-3*K)
                assert score(a,certs[K])[0]>2
                old=sorted((set(certs[K])-{boundary-3})|{boundary-2})
                assert score(a,old)==(2,1620-3*K)
                checks+=1
        report['cut_results'][str(cut)]={
            'boundary_index':boundary,'forced_selected_center':boundary+1,
            'forbidden_centers':[boundary-2,boundary-1,boundary],
            'exact_optimum_costs':exact_scores,
            'witness_masks_sha256':hashlib.sha256(('\n'.join(masks)+'\n').encode()).hexdigest(),
            'one_swap_old_optimizer_masks_sha256':hashlib.sha256(('\n'.join(swap_masks)+'\n').encode()).hexdigest(),
            'certified_one_swap':{'replace_old_center':boundary-3,'by_center':boundary-2,'minimum_deleted_centers':1},
            'tested_closure_backgrounds':checks,
            'proof':'forced local witness is optimal after cut and infeasible before it for every other closure mask'}
    print(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
