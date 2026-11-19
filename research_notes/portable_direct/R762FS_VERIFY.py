#!/usr/bin/env python3
"""R762FS exact finite checker: r fail-stop traces, h total attempts, m named gates."""
from itertools import product
from collections import Counter
from functools import lru_cache
from math import comb
import json


def experiment(states, r, h):
    """Fixed named order; H1 blocks, H0/H2 enabled; rth BLOCK ends all attempts."""
    m = len(states)
    transcript = []
    errors = 0
    for i in range(min(h, m)):
        blocked = (states[i] == 1)
        transcript.append((i, 'BLOCK' if blocked else 'SUCCESS'))
        if blocked:
            errors += 1
            if errors == r:
                break
    return tuple(transcript)


def bound(m, r, h):
    t = min(m, h)
    return 1 if not r or not t else sum(comb(t, a) for a in range(min(r, t) + 1))


@lru_cache(None)
def max_adaptive_leaves(unprobed, remaining_attempts, blocks_left):
    """Exact dynamic search on unknown independent gate statuses and public signals."""
    if unprobed == 0 or remaining_attempts == 0 or blocks_left == 0:
        return 1
    # Any unprobed gate is symmetric. Success leaves same block budget; BLOCK consumes one.
    return max_adaptive_leaves(unprobed-1, remaining_attempts-1, blocks_left) + max_adaptive_leaves(unprobed-1, remaining_attempts-1, blocks_left-1)


def expected_fibers(m, r, h):
    t=min(m,h)
    x=Counter()
    if r<1 or t==0:
        return Counter({3**m: 1})
    for a in range(min(r-1,t)+1):
        x[(2**(t-a))*(3**(m-t))]+=comb(t,a)
    if r<=t:
        for j in range(r,t+1):
            x[(2**(j-r))*(3**(m-j))]+=comb(j-1,r-1)
    return x


def work():
    records=[]
    checks=0
    checked_states=0
    for m in range(1,7):
        states=list(product(range(3),repeat=m))
        for r in range(1,m+2):
            for h in range(0,m+2):
                counts=Counter(experiment(s,r,h) for s in states)
                actual=Counter(counts.values())
                expected=expected_fibers(m,r,h)
                calc=bound(m,r,h)
                dp=max_adaptive_leaves(m,h,r)
                assert len(counts)==calc==dp, (m,r,h,len(counts),calc,dp)
                assert actual==expected, (m,r,h,actual,expected)
                assert sum(n*c for n,c in actual.items())==3**m
                checks+=1;checked_states+=len(states)
                if (m,r,h) in [(6,1,6),(6,2,6),(6,3,6),(6,6,6),(4,2,3)]:
                    records.append({'m':m,'block_budget':r,'attempt_budget':h,'distinct_transcripts':calc,'bits':(calc-1).bit_length(),'fiber_size_histogram':{str(k):v for k,v in sorted(actual.items())},'history_total':3**m})
        # Across all choices of a first gate, the complete binary status is observable.
        signatures={tuple('BLOCK' if s[i]==1 else 'SUCCESS' for i in range(m)) for s in states}
        assert len(signatures)==2**m
        assert Counter(Counter('BLOCK' if s[i]==1 else 'SUCCESS' for i in range(m)).get('BLOCK',0) for s in states)==Counter({b:comb(m,b)*2**(m-b) for b in range(m+1)})
    return {'schema':'EM_R762FS_EXACT_ENUM_V1','mode':'EXACT_INTEGER_EXHAUSTIVE','m_range':[1,6],'block_budget_range':'1..m+1','attempt_budget_range':'0..m+1','fixed_order_history_checks':checked_states,'regime_checks':checks,'adaptive_upper_bound':'independent gate symmetry recurrence L(m,h,r)=L(m-1,h-1,r)+L(m-1,h-1,r-1), bases 1','cross_policy_signatures':'2^m for h>=1,r>=1','sample_cases':records,'result':'PASS','limitations':['candidate three-axis named-source positive BRC model','no certified signed native Cell/Link/Port action','finite enumerations do not substitute for all-m proof']}

if __name__=='__main__':
    result=work()
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
