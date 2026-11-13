#!/usr/bin/env python3
"""R762H exact Cell-star triad port-covering loops; standard library only."""
from itertools import combinations, product, permutations
from collections import Counter, defaultdict
from functools import lru_cache
import json

DIM=6

def census(axes=(0,1,2), signs=(1,1,1)):
    ports={tuple(signs[j] if k==axes[j] else 0 for k in range(DIM)) for j in range(3)}
    targets=[tuple(signs[j] if k==axes[j] else 0 for k in range(DIM)) for j in range(3)]
    letters=tuple((a,sgn) for a in axes for sgn in (1,-1))
    currents=defaultdict(list)
    return_classes=Counter()
    first_visit_orders=Counter()
    chirality_currents={1:defaultdict(list),-1:defaultdict(list)}
    valid=[]
    for word in permutations(letters):
        z=[0]*DIM
        seen=set(); first_visit=[]; j=Counter(); rt=[]
        for t,(a,sgn) in enumerate(word,1):
            if sgn>0:
                lo=tuple(z)
                z[a]+=1
            else:
                z[a]-=1
                lo=tuple(z)
            j[(lo,a)]+=sgn
            p=tuple(z)
            if p in ports:
                seen.add(p)
                if p not in first_visit:first_visit.append(p)
            if not any(z):rt.append(t)
        assert not any(z)
        if seen==ports:
            sig=tuple(sorted((edge,count) for edge,count in j.items() if count))
            currents[sig].append(word)
            return_classes[tuple(rt)]+=1
            order=tuple(targets.index(p) for p in first_visit)
            parity=(-1)**sum(order[i]>order[j] for i in range(3) for j in range(i+1,3))
            first_visit_orders[order]+=1
            chirality_currents[parity][sig].append(word)
            valid.append(word)
    return valid, currents, return_classes, first_visit_orders, chirality_currents

def dp_count(axes=(0,1,2),signs=(1,1,1)):
    # Independent subset/count DP: no explicit word permutations.
    letters=tuple((a,s) for a in axes for s in (1,-1))
    targets=[tuple(signs[j] if k==axes[j] else 0 for k in range(DIM)) for j in range(3)]
    def position(mask):
        z=[0]*DIM
        for k,(a,s) in enumerate(letters):
            if mask&(1<<k):z[a]+=s
        return tuple(z)
    @lru_cache(None)
    def count(mask,hit):
        if mask==63:return int(hit==7)
        total=0
        for i in range(6):
            if mask&(1<<i):continue
            nm=mask|(1<<i)
            p=position(nm)
            newhit=hit
            for j,target in enumerate(targets):
                if p==target:newhit|=1<<j
            total+=count(nm,newhit)
        return total
    return count(0,0)

def main():
    source_count=0
    fixed=None
    for axes in combinations(range(DIM),3):
        for signs in product((1,-1),repeat=3):
            words,currents,returns,orders,chi_j=census(axes,signs)
            assert len(words)==24
            assert returns==Counter({(2,4,6):6,(2,6):6,(4,6):6,(6,):6})
            assert Counter(map(len,currents.values()))==Counter({1:6,2:6,6:1})
            assert dp_count(axes,signs)==24
            assert len(orders)==6 and all(x==4 for x in orders.values())
            assert all(sum(map(len,chi_j[q].values()))==12 for q in (1,-1))
            assert all(Counter(map(len,chi_j[q].values()))==Counter({1:3,2:3,3:1}) for q in (1,-1))
            if fixed is None:
                fixed={
                    'ports':list(axes), 'signs':list(signs),
                    'all_three_axis_balanced_words':720,
                    'port_covering_words':len(words),
                    'return_times':{','.join(map(str,k)):v for k,v in sorted(returns.items())},
                    'j_fiber_multiplicity':{str(k):v for k,v in sorted(Counter(map(len,currents.values())).items())},
                    'j_observer_distinct_outputs':len(currents),
                    'nonbacktracking_port_covering':sum(all(not (word[t][0]==word[t+1][0] and word[t][1]==-word[t+1][1]) for t in range(5)) for word in words),
                    'dp_count':dp_count(axes,signs),
                    'six_first_visit_orders_each_multiplicity':sorted(set(orders.values())),
                    'each_chirality_path_count':12,
                    'j_plus_chirality_fibers_each':{'1':3,'2':3,'3':1},
                    'j_plus_chirality_values_each':7,
                    'j_plus_chirality_max_fiber':3
                }
            source_count+=1
    assert source_count==160
    print(json.dumps({
      'schema':'R762H_THREE_PORT_CLOSED_SIX_STEP_CENSUS_V1',
      'source':'X6 signed coordinate torsor, frozen input a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'status':'AUTHOR_SIDE_EXACT_COMBINATORICS_NOT_NATIVE_FORCE_LAW',
      'port_configurations':source_count,
      'cyclic_event_orientations_per_configuration':2,
      'independent_oriented_witness_pairs':160*2*24,
      'first_visit_chirality_compatible_pairs':160*24,
      'fixed_configuration':fixed,
      'verification':'enumerated all 160*720 exact six-step balanced three-axis words; independent 6-letter mask DP; exact oriented edge-current histograms',
      'next_question':'native TRIADIC_CLOSURE_E admission and V29/V39 event map on an explicitly typed 3-port force incidence'
    },ensure_ascii=False,indent=2,sort_keys=True))
if __name__=='__main__':main()
