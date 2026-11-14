#!/usr/bin/env python3
"""EC49FHH: close the last released-key radius-five cases for EC49FGJ A/B.
Exact finite model: frozen nine-state BRC, ordered signed X6 native prefixes.
"""
import collections
import itertools
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
sys.path.insert(0, str(BASE / 'EC49FGW_RADIUS5_EXACT_SCREENS_20261110'))
sys.path.insert(0, str(BASE / 'EC49FHD_PREFIX_TRIE_RADIUS5_20261110'))
from EC49FGW_RADIUS5_SCREEN import W, PIN, all_words, pref, raw_key, validate_profile
from VERIFY_EC49FHD import solve_group_tree, native_word, brute_crosscheck


def verify():
    brute_crosscheck()
    catalog = list(all_words())
    assert len(catalog) == 178850
    profiles = []
    for profile in W['profiles']:
        rows, paths = validate_profile(profile)
        labels = [(r['window'], r['signature']) for r in rows]
        keys = {raw_key(r['word']) for r in rows}
        assert len(keys) == 7
        support = collections.defaultdict(int)
        key_support = collections.defaultdict(int)
        for i, (row, path) in enumerate(zip(rows, paths)):
            key_support[raw_key(row['word'])] |= 1 << i
            for p in path:
                support[p] |= 1 << i
        assert len(support) == 94
        candidate = collections.defaultdict(list)
        h2_words = collections.defaultdict(list)
        for label, word in catalog:
            if label[0] == 2:
                h2_words[label].append(word)
            if raw_key(word) in keys:
                candidate[label].append(native_word(word))
        assert sum(map(len, candidate.values())) == 9838
        assert len(h2_words[(2, 16)]) == len(h2_words[(2, 32)]) == 1
        cases = []
        for Q in itertools.combinations(range(24), 5):
            mask = sum(1 << i for i in Q)
            released = {k for k, s in key_support.items() if s & mask == s}
            if not released:
                continue
            B = sum((s & mask) == s for s in support.values()) - 1
            if B not in (17, 19, 20):
                continue
            if B == 17 and 22 in Q and 23 in Q:
                continue  # already excluded by EC49FHG
            h2 = [i for i in Q if labels[i][0] == 2]
            assert len(released) == len(h2) == 1
            h2i = h2[0]
            assert h2_words[labels[h2i]][0] == rows[h2i]['word']
            assert released == {raw_key(h2_words[labels[h2i]][0])}
            fixed = {p for p, s in support.items() if s & mask != s}
            assert len(fixed) == 93 - B
            opt, stats = solve_group_tree([candidate[labels[i]] for i in Q], fixed)
            assert opt == B + 1, (profile['profile_id'], Q, B, opt)
            cases.append({'Q': list(Q), 'budget': B, 'exact_min_added': opt,
                          'exact_min_total': len(fixed) + opt,
                          'released_key_forced_back_by_H2': True,
                          'trie_nodes': stats['trie_nodes']})
        counts = collections.Counter(c['budget'] for c in cases)
        assert counts == {17: 16, 19: 20, 20: 16}, counts
        profiles.append({'profile': profile['profile_id'], 'cases': cases,
                         'counts_by_budget': {str(k): v for k, v in sorted(counts.items())}})
    report = {'schema': 'EC49FHH_FIVE_PATH_RELEASE_KEY_CLOSURE_V1',
              'frozen_scientific_pin': PIN, 'catalog_words': len(catalog),
              'seven_key_words_per_profile': 9838,
              'scope': 'Remaining 52 released-key radius-five fixed-background positions per witness',
              'profiles': profiles}
    (HERE / 'EXACT_REPORT_EC49FHH.json').write_text(json.dumps(report, indent=2) + '\n')
    print('EC49FHH_EXACT_PASS', [(p['profile'], len(p['cases']), p['counts_by_budget']) for p in profiles])
    return report


if __name__ == '__main__':
    verify()
