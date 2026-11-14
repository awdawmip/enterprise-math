#!/usr/bin/env python3
"""Native signed X6 five-key prefix-cost lower bounds, all 16 frozen BRC key sets."""
import collections
import json
import os
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
INPUT=Path(os.environ.get('EC49FKM_INPUT_DIR', HERE.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
sys.path.insert(0,str(INPUT))
import EC49FGW_RADIUS5_SCREEN as g
PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert g.PIN == PIN
LABELS=sorted((h,s) for h,ss in g.REQ.items() for s in ss)
assert len(LABELS)==24
LI={lab:i for i,lab in enumerate(LABELS)}
K0={(2,1,1),(3,0,1),(3,1,1)}
U=((3,3,1),(4,2,1),(5,1,1),(5,1,2))
V=((5,5,1),(6,4,1),(7,3,1),(7,3,2))
FIVE_KEY_SETS=[tuple(sorted(K0|{u,v})) for u in U for v in V]
WORDS=collections.defaultdict(list)
count=0
for lab,w in g.all_words():
    count+=1
    key=g.raw_key(w)
    # The BRC generator's native typed path produces a signed X6 microstep stream.
    literal=tuple(x for ch in w for x in g.STEPS[ch])
    assert literal and all(-3<=x<=3 and x for x in literal)
    WORDS[key].append((LI[lab],literal))
assert count==178850 and len(WORDS)==94

RESULTS=[]
for K in FIVE_KEY_SETS:
    mlen=[100000]*24
    layers=collections.defaultdict(lambda:collections.defaultdict(int))
    for key in K:
        for idx,literal in WORDS[key]:
            mlen[idx]=min(mlen[idx],len(literal))
            for d in range(1,len(literal)+1):
                # Tuple retains every signed native microstep, not endpoint positions.
                layers[d][literal[:d]]|=1<<idx
    assert all(z<100000 for z in mlen)
    bins=[]
    for d in range(1,max(mlen)+1):
        forced=sum(1<<i for i,L in enumerate(mlen) if L>=d)
        forced_n=forced.bit_count()
        max_support=max((m&forced).bit_count() for m in layers[d].values())
        assert 1<=max_support<=forced_n
        lower=(forced_n+max_support-1)//max_support
        bins.append(dict(depth=d,forced_labels=forced_n,maximum_labels_per_prefix=max_support,
                         guaranteed_prefix_count=lower))
    total=sum(row['guaranteed_prefix_count'] for row in bins)
    RESULTS.append(dict(keys=[list(k) for k in K],lower_bound=total,per_depth=bins))
assert len(RESULTS)==16
assert min(x['lower_bound'] for x in RESULTS)==99
assert all(x['lower_bound']>93 for x in RESULTS)
print('EC49FKN_ALL_FIVE_KEY_PREFIX_LOWER_BOUNDS_PASS',len(RESULTS),
      'global_min_bound',min(x['lower_bound'] for x in RESULTS),
      'bounds', [x['lower_bound'] for x in RESULTS])
result=dict(schema='EC49FKN_FIVE_KEY_PREFIX_LOWER_V1',
            frozen_pin=PIN,word_count=count,key_count=len(WORDS),label_count=24,
            method='Per-depth forced-label coverage / maximum labels-per-prefix bound (exact signed native microsteps)',
            theorem='All solutions on five full raw keys need at least 99 distinct native signed ordered nonempty prefixes',
            lower_bound_for_all_five_key_solutions=99,results=RESULTS)
output=Path(os.environ.get('EC49FKN_OUT',HERE/'EXACT_RESULT_EC49FKN.json'))
output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('RESULT_WRITTEN',output,len(output.read_bytes()))

if __name__ == "__main__":
    pass
