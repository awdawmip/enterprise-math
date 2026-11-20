"""Integer lower bound from native minima and the certified geometric exclusions."""
from functools import cache
from itertools import product
from collections import Counter

@cache
def partitions(total, count, limit=13):
    if not count:
        return [()] if not total else []
    return [(s,)+tail for s in range((total+count-1)//count,min(limit,total-count+1)+1)
            for tail in partitions(total-s,count-1,s)]

def check(minima, ceiling=11059):
    combined=[0,0,12,36,72,120,201,292]
    bounds=[0,13,26,39,52,65,78,85,96,102,112,119,121,125]
    candidates=Counter()
    survivors=0
    for sizes in partitions(125,11):
        if sizes.count(13)>=3: continue  # prior lower bound 11,292
        if sum(combined[s] if s<8 else min(minima[s,True],minima.get((s,False),10**8)) for s in sizes)>ceiling:
            continue
        levels=sorted(set(sizes))
        counts=[sizes.count(s)for s in levels]
        for proper_counts in product(*(range(n+1) if s<13 else (0,) for s,n in zip(levels,counts))):
            proper=tuple(s for s,n in zip(levels,proper_counts)for _ in range(n))
            inside=tuple(s for s,n,x in zip(levels,counts,proper_counts)for _ in range(n-x))
            if len(proper)<4: continue
            if any(sum(inside[-j:])>bounds[j] for j in range(1,len(inside)+1)): continue
            if len(proper)==4 and sum(proper)<=41: continue
            big=inside.count(13);near=inside.count(12)
            # All 12-point subsets of full classes are central/outer punctures.
            # A table with seven such low-cost large classes fails at eleven labels.
            if near+big>=7:continue
            base=sum(combined[s] if s<8 else minima[s,False] for s in proper)
            base+=sum(combined[s] if s<8 else minima[s,True] for s in inside)
            for central in range(near+1):
                if big+central>4:continue
                floor=base+12*(near-central)
                if big+central>=4:floor=max(floor,11036)
                if floor>ceiling:continue
                candidates[proper,inside]+=1
                if proper==(10,10,10,10,11) and inside==(12,12,12,12,13,13):
                    # Two full classes, at most two central punctures, at least
                    # two outer punctures contribute at least 7,032 in total.
                    assert 2*1296+2*1104+2*1116==7032
                    assert ceiling-7032-4*744<=1051
                    assert ceiling-7032-1008-3*744<=787
                    continue
                survivors+=1
    assert not survivors
    return {'budget':ceiling,'lower':ceiling+1,
            'final_size_cases':[[list(p),list(e),n] for (p,e),n in sorted(candidates.items())]}
