#!/usr/bin/env python3
"""Independent exact interval-stabbing oracle for EC49FFF's original BRC observer quota.
No dependencies; integer operations only; exhaustive brute crosscheck 2**17 masks.
"""
from collections import Counter
from itertools import combinations
from json import dumps
from pathlib import Path

N = 1 << 17
# Low H2..H9: bits 0..7. High H3..H9: 8..14. H2 16:15, H2 32:16.

def key_for_horizon(H):
    if H==2: raise ValueError('H2 has distinct high-label keys')
    f=(H-1)//2
    return (f+2,H-1-f,1)

def covers_key(H):
    m=0
    if H==2: raise ValueError('special H2 labels')
    for h in range(2,10):
        if h+1<=H<=2*h-1: m|=1<<(h-2)
    if 3<=H<=9: m|=1<<(H+5)
    return m

def greedy(mask, positive=False):
    # Forced keys for requested high labels. H2 high16 requires key (3,0,1).
    if positive and (mask & (1<<15)): return None
    fixed=set()
    h2_keys=[]
    if mask & (1<<15): h2_keys.append((3,0,1))
    if mask & (1<<16): h2_keys.append((2,1,1))
    for h in range(3,10):
        if mask & (1<<(h+5)): fixed.add(h)
    # Greedy interval stabbing of uncovered low H2..H9, in increasing right end.
    chosen=set(fixed)
    for h in range(2,10):
        if not mask & (1<<(h-2)): continue
        if any(h+1<=H<=2*h-1 for H in chosen):continue
        chosen.add(2*h-1)
    keys = h2_keys+[key_for_horizon(H) for H in sorted(chosen)]
    assert all(x>=1 for k in keys for x in k) if positive else True
    return keys

def keymask(k):
    if k==(3,0,1):return 1<<15
    if k==(2,1,1):return 1<<16
    H=k[0]+k[1]-1
    assert k==key_for_horizon(H)
    return covers_key(H)

def exhaustive_minima(positive=False):
    # Independent brute-force enumeration of all candidate key subsets and
    # exact min-over-supersets transform; no greedy logic is reused.
    keys=([(2,1,1)] if positive else [(3,0,1),(2,1,1)]) + [key_for_horizon(H) for H in range(3,18)]
    m=[keymask(k) for k in keys]
    costs=[99]*N
    costs[0]=0
    unions=[0]*(1<<len(keys))
    for subset in range(1,1<<len(keys)):
        b=subset&-subset
        j=b.bit_length()-1
        represented=unions[subset^b]|m[j]
        unions[subset]=represented
        costs[represented]=min(costs[represented],subset.bit_count())
    for j in range(17):
        b=1<<j
        for mask in range(N):
            if not mask&b and costs[mask|b]<costs[mask]:
                costs[mask]=costs[mask|b]
    return costs

def main():
    expected={0:1,1:76,2:1146,3:6748,4:20109,5:34152,6:35192,7:22576,8:8896,9:1984,10:192}
    expected_positive={0:1,1:75,2:1071,3:5677,4:14432,5:19720,6:15472,7:7104,8:1792,9:192,99:65536}
    assert sum(expected.values())==N and sum(expected_positive.values())==N
    summaries={}
    for name,positive,exp in [('count_admissible',False,expected),('strict_positive',True,expected_positive)]:
        brute=exhaustive_minima(positive)
        hist=Counter()
        first_error=None
        for mask in range(N):
            keys=greedy(mask,positive)
            got=99 if keys is None else len(keys)
            hist[got]+=1
            if got!=brute[mask] and first_error is None:
                first_error={'mask':mask,'greedy':got,'brute':brute[mask]}
            if keys is not None:
                cov=0
                for k in keys:cov |= keymask(k)
                assert cov & mask == mask
                assert len(keys)==len(set(keys))
        assert hist==exp, (name, dict(hist))
        assert first_error is None, (name, first_error)
        summaries[name]={'histogram':dict(sorted(hist.items())),'at_most_five_masks':sum(v for k,v in hist.items() if k<=5),'exhaustive_masks_checked':N,'independent_subset_counterexample':first_error}

    lowmask=(1<<8)-1
    lowkeys=greedy(lowmask)
    assert len(lowkeys)==4 and [k[0]+k[1]-1 for k in lowkeys]==[3,5,9,17]
    # Demand all 8 low windows plus any of 9 high requirements.
    count_by_high_n=Counter()
    example_by_high_n={}
    for x in range(1<<9):
        mask=lowmask
        for b in range(9):
            if x>>b&1:mask|=1<<(8+b)
        n=x.bit_count()
        kk=greedy(mask)
        cost=len(kk)
        count_by_high_n[(n,cost)]+=1
        if (n,cost) not in example_by_high_n:example_by_high_n[(n,cost)]=[list(k) for k in kk]
    # Hold all eight low quotas, add all 7 high H3-H9 simultaneously.
    all_lows_all_late_high=lowmask|sum(1<<(h+5) for h in range(3,10))
    # A representative new simultaneous quota family with 4 high H3,H5,H7,H9.
    example=lowmask|sum(1<<(h+5) for h in (3,5,7,9))
    witness=greedy(example)
    assert len(witness)==5
    report={
      'schema':'EC49FFG_GREEDY_INTERVAL_CERTIFICATE_V1',
      'date':'2026-11-09',
      'scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
      'domain':'H2..H9, original nine-state BRC observer; exact reachability/minimum full-key cardinality; nonnegative y or strictly-positive domains',
      'algorithm':'force high terminal horizons; greedily stab uncovered low intervals [h+1,2h-1] at right endpoints 2h-1, scanning h=2..9',
      'source_staircase':'EC49FFD at df0dbc54707a6926db858631e5a03fea189dccde',
      'source_canonical_quota':'EC49FFF at 58cdba9c360bc180028183cff711405d2e2f37c0',
      'verification':summaries,
      'all_eight_lows':{'minimum_keys':len(lowkeys),'witness_keys':[list(k) for k in lowkeys]},
      'simultaneous_eight_lows_four_high_3_5_7_9':{'minimum_keys':len(witness),'witness_keys':[list(k) for k in witness]},
      'all_eight_lows_and_H3_to_H9_high':{'minimum_keys':len(greedy(all_lows_all_late_high)),'witness_keys':[list(k) for k in greedy(all_lows_all_late_high)]},
      'all_eight_lows_high_requirements_distribution':[{'high_bit_count':a,'minimum_keys':b,'mask_count':v} for (a,b),v in sorted(count_by_high_n.items())],
      'proof_scope':'exact observation-quota key cardinality, no native ordered-prefix cost conclusion',
      'status':'EXACT_INTEGER_PASS'
    }
    here=Path(__file__).parent
    (here/'EXACT_REPORT_EC49FFG.json').write_text(dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('EXACT_INTEGER_PASS:', N, 'masks x2, independent brute crosscheck')
    print('all eight lows:',lowkeys)
    print('eight lows + high H3,H5,H7,H9:', witness)
    print('at most five cardinality:',[(k,v['at_most_five_masks']) for k,v in summaries.items()])
    print('all-lows high distribution:',sorted(count_by_high_n.items()))

if __name__=='__main__':main()
