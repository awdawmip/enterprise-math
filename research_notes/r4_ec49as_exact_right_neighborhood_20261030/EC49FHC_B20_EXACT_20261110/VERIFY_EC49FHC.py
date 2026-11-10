#!/usr/bin/env python3
"""EC49FHC: exact B=20 five-path C<=93 exclusion for EC49FGJ A/B witnesses.
No native-key release; frozen original nine-state BRC and ordered signed X6 prefixes.
Requires EC49FGW and EC49FGX sibling research folders in the same parent.
"""
import collections
import itertools
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path[:0] = [str(ROOT/'EC49FGX_RADIUS5_PAIR_FIVE_DP_20261110'),
                 str(ROOT/'EC49FGW_RADIUS5_EXACT_SCREENS_20261110')]
from EC49FGW_RADIUS5_SCREEN import W, PIN, all_words, pref, raw_key, validate_profile
from VERIFY_EC49FGX import candidates, pair_possible, five_possible

assert PIN == 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
full = list(all_words())
assert len(full) == 178850
report = {
    'schema':'EC49FHC_B20_FIVE_PATH_EXACT_V1',
    'scientific_pin':PIN,
    'scope':'A/B witness; exactly 5 modified labels; 19 fixed labels retain all 7 complete raw keys; B=20; C<=93',
    'legal_words':len(full),
    'profiles':[]
}
for profile in W['profiles']:
    rows, paths = validate_profile(profile)
    labels = [(r['window'],r['signature']) for r in rows]
    keys = [raw_key(r['word']) for r in rows]
    old_keys = set(keys)
    assert len(old_keys) == 7
    support = collections.defaultdict(int)
    key_support = collections.defaultdict(int)
    for i, (ps,k) in enumerate(zip(paths,keys)):
        key_support[k] |= 1<<i
        for prefix in ps:
            support[prefix] |= 1<<i
    assert len(support) == 94
    indexed = collections.defaultdict(list)
    for lab,word in full:
        if raw_key(word) not in old_keys:
            continue
        ps = pref(word)
        indexed[lab].append((len(ps), ps[-1],
                             [(len(p),support[p]) for p in ps if p in support]))
    assert sum(map(len,indexed.values())) == 9838
    cases = []
    for Q in itertools.combinations(range(24),5):
        mask = sum(1<<i for i in Q)
        if any((s & mask) == s for s in key_support.values()):
            continue
        B = sum((s & mask) == s for s in support.values())-1
        if B != 20:
            continue
        groups = [candidates(indexed[labels[i]],mask,B) for i in Q]
        assert all(groups)
        pair_ok = all(pair_possible(groups[i],groups[j],B)
                      for i,j in itertools.combinations(range(5),2))
        feasible = five_possible(groups,B) if pair_ok else False
        cases.append({'Q':list(Q),'candidate_counts':list(map(len,groups)),
                      'pair_ok':pair_ok,'C93_feasible':feasible})
    assert len(cases) == 116
    assert not any(c['C93_feasible'] for c in cases)
    report['profiles'].append({'witness':profile['profile_id'],
                               'checked':len(cases),'C93_feasible':0,'cases':cases})
    print('EC49FHC', profile['profile_id'], 'EXACT_PASS', len(cases), flush=True)
(HERE/'EXACT_REPORT_EC49FHC.json').write_text(json.dumps(report,indent=2)+'\n')
print('EC49FHC_COMPLETE')
