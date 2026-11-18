#!/usr/bin/env python3
"""Exact k=7 slack-2 single named-control INERT lower and upper certificate.
All named Set0 commands self-loop; each state covers full {2t,2t+1} pairs.
Standard library only. Frozen pin 435e77af0d180eac32bd1f9c4c464bc4010b7551.
"""
from functools import lru_cache
import json
K,N,S=7,128,2
UPPER=(43,47,55,59,63,75,79,83,85,87,91,93,95,101,103,107,109,111,115,117,119,123,125,127)

def q(u):
    return sum((u>>i&1)*(u>>((i+1)%K)&1) for i in range(K))

def pairset(r):
    assert r&1
    return sum(1<<t for t in range(64) if all(
        (u&~r)==0 and 0<=q(r)-q(u)<=S for u in (2*t,2*t+1)))

def members(mask):
    while mask:
        bit=mask&-mask
        yield bit.bit_length()-1
        mask-=bit

def main():
    full=(1<<64)-1
    allcovers=[pairset(r) for r in range(1,N,2)]
    upper=0
    for r in UPPER: upper|=pairset(r)
    assert len(UPPER)==24 and len(set(UPPER))==24 and upper==full
    keep=[i for i in range(len(allcovers)) if not any(
        i!=j and allcovers[i]&~allcovers[j]==0
        and (allcovers[i]!=allcovers[j] or j>i)
        for j in range(len(allcovers)))]
    covers=[allcovers[i] for i in keep]
    by_t=[[j for j,C in enumerate(covers) if C>>t&1]for t in range(64)]
    assert all(by_t)
    calls=0

    @lru_cache(maxsize=None)
    def possible(rem,m):
        nonlocal calls
        calls+=1
        if not rem: return True
        if not m: return False
        maxcov=max((C&rem).bit_count() for C in covers)
        if rem.bit_count()>m*maxcov:return False
        pivot=min(members(rem),key=lambda t:len(by_t[t]))
        for j in sorted(by_t[pivot],
                        key=lambda j:(covers[j]&rem).bit_count(),reverse=True):
            if possible(rem&~covers[j],m-1):return True
        return False

    assert possible(full,23) is False
    cache=possible.cache_info()
    print(json.dumps({
       "status":"PASS_R5_K7_INERT_24_EXACT_INTEGER_CERTIFICATE",
       "frozen_scientific_input":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
       "model":{"k":7,"slack":2,"controls":[0],"reset_transition":"all self-loops"},
       "exact_minimum":24,
       "upper":{"source_centers":list(UPPER),"covered_raw_pairs":64,
                "covered_raw_masks":128,
                "total_pair_membership_checks":sum(pairset(r).bit_count() for r in UPPER)},
       "lower":{"candidate_odd_centers":64,"undominated_centers":len(keep),
                "excludes_at_most":23,"visited_memoized_states":calls,
                "cache_hits":cache.hits,"cache_misses":cache.misses},
       "review":"NOT_REVIEWED"},sort_keys=True,indent=2))
if __name__=="__main__":main()
