#!/usr/bin/env python3
"""Finite combinatorial radius-six key-forcing screen on frozen two witnesses."""
import sys, itertools, collections, json
from pathlib import Path
here=Path(__file__).resolve().parent
root=here.parent/'EC49FGW_RADIUS5_EXACT_SCREENS_20261110'
sys.path.insert(0,str(root))
from EC49FGW_RADIUS5_SCREEN import W,raw_key,pref,validate_profile,all_words,PIN

# Exactly unique legal H2 word per frozen label.
h2=collections.defaultdict(list)
for label,word in all_words():
    if label[0]==2: h2[label].append(word)
assert {lab:len(words) for lab,words in h2.items()}=={(2,16):1,(2,32):1}
report=[]
for profile in W['profiles']:
    rows,ps=validate_profile(profile)
    keys=collections.defaultdict(int)
    supports=collections.defaultdict(int)
    for i,(r,pp) in enumerate(zip(rows,ps)):
        keys[raw_key(r['word'])]|=1<<i
        for p in pp:supports[p]|=1<<i
    assert len(keys)==7 and len(supports)==94
    labels=[(r['window'],r['signature']) for r in rows]
    count=collections.Counter()
    budget_hist=collections.Counter()
    for Q in itertools.combinations(range(24),6):
        mask=sum(1<<i for i in Q)
        released={key for key,support in keys.items() if support & mask==support}
        B=sum(support & mask == support for support in supports.values())-1
        if B<0:
            count['fixed94_trivial']+=1
            continue
        count['nontrivial_background']+=1
        forced={raw_key(h2[labels[i]][0]) for i in Q if labels[i] in h2}
        if released<=forced:
            count['all_released_keys_forced_back']+=1
            budget_hist[B]+=1
        else:
            count['at_least_one_released_key_unforced']+=1
    assert sum(count[x] for x in ('fixed94_trivial','all_released_keys_forced_back','at_least_one_released_key_unforced'))==134596
    report.append({'profile':profile['profile_id'],'counts':dict(count),'key_forced_budget_hist':dict(sorted(budget_hist.items()))})
result={'schema':'EC49FHI_RADIUS6_KEY_FORCING_SCREEN_V1','frozen_pin':PIN,'combinations_per_profile':134596,'profiles':report}
print(json.dumps(result,indent=2))
(here/'EXACT_SUMMARY_EC49FHI.json').write_text(json.dumps(result,indent=2)+'\n')
