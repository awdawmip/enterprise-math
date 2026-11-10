#!/usr/bin/env python3
"""EC49FHA: exhaustive five-path replacement at exact new-prefix budget B=19.
Source: EC49FGJ seven-key A witness, frozen nine-state BRC and native signed X6.
Requires sibling EC49FGW and EC49FGX folders on PR #1730 research branch.
"""
import collections
import itertools
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path[:0] = [
    str(ROOT / 'EC49FGX_RADIUS5_PAIR_FIVE_DP_20261110'),
    str(ROOT / 'EC49FGW_RADIUS5_EXACT_SCREENS_20261110'),
]
from EC49FGW_RADIUS5_SCREEN import W, PIN, all_words, raw_key, validate_profile, pref
from VERIFY_EC49FGX import candidates, five_possible

assert PIN == 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
profile = next(p for p in W['profiles'] if p['profile_id'] == 'A')
rows, paths = validate_profile(profile)
labels = [(r['window'], r['signature']) for r in rows]
keys = [raw_key(r['word']) for r in rows]
present = set(keys)
assert len(present) == 7
supports = collections.defaultdict(int)
key_supports = collections.defaultdict(int)
for i, (ps, k) in enumerate(zip(paths, keys)):
    key_supports[k] |= 1 << i
    for p in ps:
        supports[p] |= 1 << i
assert len(supports) == 94

catalog = list(all_words())
assert len(catalog) == 178850
index = collections.defaultdict(list)
for label, word in catalog:
    if raw_key(word) not in present:
        continue
    ps = pref(word)
    index[label].append(
        (len(ps), ps[-1], [(len(p), supports[p]) for p in ps if p in supports])
    )
assert sum(len(group) for group in index.values()) == 9838

cases = []
for Q in itertools.combinations(range(24), 5):
    mask = sum(1 << i for i in Q)
    if any((s & mask) == s for s in key_supports.values()):
        continue
    budget = sum((s & mask) == s for s in supports.values()) - 1
    if budget != 19:
        continue
    groups = [candidates(index[labels[i]], mask, budget) for i in Q]
    assert all(groups)
    feasible = five_possible(groups, budget)
    cases.append({
        'positions': Q,
        'candidate_counts': [len(g) for g in groups],
        'can_reach_C93': feasible
    })
assert len(cases) == 144
assert not any(x['can_reach_C93'] for x in cases)
report = {
    'schema': 'EC49FHA_A_B19_EXACT_V1',
    'frozen_scientific_pin': PIN,
    'scientific_model': 'original nine-state BRC, ordered signed native X6 prefix',
    'witness': 'EC49FGJ_A',
    'target_native_edges': 93,
    'changed_paths': 5,
    'fixed_19_paths_retain_all_7_raw_cache_keys': True,
    'replacement_prefix_budget': 19,
    'catalog_words': len(catalog),
    'admissible_fixed_key_words': sum(map(len, index.values())),
    'positions_exhausted': len(cases),
    'positions_reaching_93': 0,
    'cases': cases
}
(HERE / 'EXACT_REPORT_EC49FHA.json').write_text(
    json.dumps(report, indent=2) + '\n'
)
print('EC49FHA_A_B19_EXACT_PASS: 144 positions, zero 93-edge completions')
