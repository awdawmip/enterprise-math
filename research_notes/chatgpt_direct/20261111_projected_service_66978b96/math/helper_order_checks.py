"""Exhaustively compare mixed tests and helper-then-singleton normal form, all residual sets."""
from argparse import ArgumentParser
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json


def check(n,hc):
    full=(1<<n)-1
    # unique unoriented nontrivial splits: representative excludes world 0
    potential=list(range(2,full,2)); families=[]
    for t in hc: families.extend(combinations(potential,t))
    checks=0;strict=0
    for helpers in families:
        for demand in range(0,full+1,2):
            # demand is subset of nonzero worlds (baseline = world 0)
            def labels(u):
                return (u&demand).bit_count() + int(bool(u&~demand))
            @lru_cache(None)
            def joint(u):
                if labels(u)==1:return 0
                tests=tuple(1<<i for i in range(1,n)) + helpers
                return min(1+max(joint(u&m),joint(u&~m)) for m in tests if u&m and u&~m)
            @lru_cache(None)
            def ordered(u):
                return min([labels(u)-1]+[1+max(ordered(u&m),ordered(u&~m)) for m in helpers if u&m and u&~m])
            for u in range(1,full+1):
                v=ordered(u)
                assert joint(u)==v
                if len(helpers)==1:
                    m=helpers[0]
                    if u&m and u&~m:
                        assert v==min(labels(u)-1,max(labels(u&m),labels(u&~m)))
                checks+=1;strict += int(v<labels(u)-1)
    return dict(worlds=n,helper_family_sizes=list(hc),distinct_helper_families=len(families),
                residual_demand_family_comparisons=checks,strict_savings_comparisons=strict)


def main():
    p=ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).with_name('helper_order_results.json'));a=p.parse_args()
    cases=[check(3,range(4)),check(4,range(8)),check(5,range(3))]
    out=dict(status='PASS',scope='control comparisons, unique splits up to complement, all nonempty residuals and all subsets of nonzero demanded worlds; all helper families for 3,4 worlds and at most two helpers for 5 worlds',cases=cases,total_comparisons=sum(u['residual_demand_family_comparisons'] for u in cases))
    a.out.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print('PASS',out['total_comparisons'])
if __name__=='__main__':main()
