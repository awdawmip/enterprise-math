#!/usr/bin/env python3
"""EC49FGZ: complete no-key-release radius-five five-way test for budgets 16..18.
Run within the PR #1730 EC49FGZ sibling folder; imports existing EC49FGX verifier
and its EC49FGW frozen observer/witness dependency. No floating-point arithmetic.
"""
import collections
import itertools
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'EC49FGX_RADIUS5_PAIR_FIVE_DP_20261110'))
try:
    from VERIFY_EC49FGX import (W, PIN, all_words, pref, raw_key,
                                 validate_profile, candidates, five_possible)
except ModuleNotFoundError:  # standalone evidence bundle with its original files
    from VERIFY_EC49FGX_PORTABLE import (W, PIN, all_words, pref, raw_key,
                                         validate_profile, candidates, five_possible)


def examine(profile, catalog):
    rows, paths = validate_profile(profile)
    labels = [(r['window'], r['signature']) for r in rows]
    keys = [raw_key(r['word']) for r in rows]
    present_keys = set(keys)
    supports = collections.defaultdict(int)
    key_supports = collections.defaultdict(int)
    for i, (native_prefixes, key) in enumerate(zip(paths, keys)):
        key_supports[key] |= 1 << i
        for p in native_prefixes:
            supports[p] |= 1 << i
    assert len(present_keys) == 7 and len(supports) == 94

    index = collections.defaultdict(list)
    for label, word in catalog:
        if raw_key(word) not in present_keys:
            continue
        prefixes = pref(word)
        index[label].append((len(prefixes), prefixes[-1],
                             [(len(p), supports[p]) for p in prefixes if p in supports]))
    assert sum(len(group) for group in index.values()) == 9838

    counts = collections.Counter()
    for Q in itertools.combinations(range(24), 5):
        m = sum(1 << i for i in Q)
        if any((s & m) == s for s in key_supports.values()):
            continue
        B = sum((s & m) == s for s in supports.values()) - 1
        if B not in (16, 17, 18):
            continue
        counts[f'budget_{B}_positions'] += 1
        groups = [candidates(index[labels[i]], m, B) for i in Q]
        if any(not group for group in groups):
            counts[f'budget_{B}_excluded_singleton'] += 1
        elif five_possible(groups, B):
            counts[f'budget_{B}_feasible'] += 1
        else:
            counts[f'budget_{B}_excluded_fiveway'] += 1

    assert [counts[f'budget_{b}_positions'] for b in (16,17,18)] == [32,404,180]
    assert all(counts[f'budget_{b}_feasible'] == 0 for b in (16,17,18))
    return {'witness': profile['profile_id'], 'counts': dict(counts)}


if __name__ == '__main__':
    catalog = list(all_words())
    assert len(catalog) == 178850
    report = {
        'schema': 'EC49FGZ_RADIUS5_HIGH_BUDGET_EXACT_V1',
        'frozen_scientific_pin': PIN,
        'input_profile_count': len(W['profiles']),
        'candidate_word_count': len(catalog),
        'model': 'frozen nine-state BRC, ordered signed native X6 microstep prefix sets',
        'scope': 'A/B EC49FGJ, 5 of 24 words replaced, no original raw-cache-key released, C<=93, B=16..18',
        'profiles': [examine(profile, catalog) for profile in W['profiles']],
    }
    (HERE / 'EXACT_REPORT_EC49FGZ.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    print('EC49FGZ_EXACT_PASS')
