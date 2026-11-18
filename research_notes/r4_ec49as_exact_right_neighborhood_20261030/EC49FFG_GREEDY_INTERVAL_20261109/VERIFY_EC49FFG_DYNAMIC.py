#!/usr/bin/env python3
"""An O(U^2) per-mask exact lexicographic oracle, with exhaustive 17-key audit.
Lexicographic objective: (number of distinct BRC full keys, sum of selected
canonical key native word lengths), not union-prefix edge cost.
"""
from functools import lru_cache
from json import loads, dumps
from pathlib import Path
from VERIFY_EC49FFG import N, greedy
from VERIFY_EC49FFG_SECONDARY import oracle


def interval_dp(mask,positive=False):
    if positive and mask&(1<<15):return None
    high2count=((mask>>15)&1)+((mask>>16)&1)
    forced={h for h in range(3,10) if mask&(1<<(h+5))}
    uncovered=tuple(h for h in range(2,10)
                    if mask&(1<<(h-2)) and not any(h+1<=H<=2*h-1 for H in forced))
    @lru_cache(None)
    def solve(i):
        if i==len(uncovered):return (0,0,())
        h=uncovered[i]
        best=None
        j=i+1
        for H in range(h+1,2*h):
            while j<len(uncovered) and uncovered[j]<H:j+=1
            kc,ln,chosen=solve(j)
            v=(kc+1,ln+2*(H+1),(H,)+chosen)
            if best is None or v[:2]<best[:2]:best=v
        return best
    count,ln,extra=solve(0)
    assert len(set(extra))==len(extra) and not forced.intersection(extra)
    return (high2count+len(forced)+count,
            high2count*6+sum(2*(H+1) for H in forced)+ln,
            tuple(sorted(forced.union(extra))))

def main():
    results={}
    for name,positive in [('count_admissible',False),('strict_positive',True)]:
        keys,optimal,w=oracle(positive)
        agree=0
        for mask in range(N):
            v=interval_dp(mask,positive)
            if v is None:
                assert optimal[mask]==1_000_000
            else:
                assert v[0]*1000+v[1]==optimal[mask],(name,mask,v,optimal[mask])
                agree+=1
        results[name]={'all_requirement_masks':N,'reachable_and_exact_lexicographic_matches':agree,'mismatches':0}
    path=Path(__file__).parent/'EXACT_REPORT_EC49FFG.json'
    report=loads(path.read_text())
    report['dynamic_lexicographic']={'objective':'minimize (complete key count, sum selected canonical key native word lengths)',
                                  'algorithm':'sort low horizons uncovered by forced high keys; F(i)=min_(h_i+1<=H<=2h_i-1) [(1,2(H+1))+F(first j with h_j>=H)]; prepend mandatory H2 high and H3-H9 high keys',
                                  'time_per_mask':'O(U^2) integer operations where low horizons subset of H2..HU (U=9)',
                                  'verification':results}
    path.write_text(dumps(report,indent=2,ensure_ascii=False)+'\n')
    print('DYNAMIC_EXACT_PASS',results)
    print('all low DP (keys, secondary length, horizons)=',interval_dp(255))

if __name__=='__main__':main()
