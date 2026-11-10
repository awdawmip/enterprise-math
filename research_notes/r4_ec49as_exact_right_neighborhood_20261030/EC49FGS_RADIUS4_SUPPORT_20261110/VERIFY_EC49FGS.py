#!/usr/bin/env python3
"""EC49FGS exact support-hypergraph / radius-four key-forcing checker.
Input: Git blob e65c1598ad9fa2680558046ed1e59d83806536b8
at EC49FGJ_SEVEN_KEY_94_20261110/WITNESSES_EC49FGJ.json.
Only frozen nine-state BRC and exact ordered signed-X6 native prefixes.
"""
import collections
import itertools
import json
import sys
from pathlib import Path

PIN = 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
OPS = 'acdefg'
T = ((1, 2, 3, 1, 4, 5), (1, 6, 7, 1, 1, 1),
     (2, 2, 8, 2, 2, 2), (3, 8, 3, 3, 3, 3),
     (4, 2, 7, 4, 4, 4), (5, 6, 3, 5, 5, 5),
     (6, 6, 8, 6, 6, 6), (7, 8, 7, 7, 7, 7),
     (8, 8, 8, 8, 8, 8))
SIG = (0, 0, 4, 1, 16, 32, 8, 2, 0)
STEPS = {'a': (-1, -1), 'c': (1, 2, -1, -2),
         'd': (2, 1, -2, -1), 'e': (3, 1, 1, -3),
         'f': (1, -1), 'g': (2, -2)}
REQUIRED = {2: (16, 32), 3: (16, 32), 4: (1, 2, 4, 8),
            5: (16, 32), 6: (1, 2, 4, 8), 7: (1, 2, 4, 8),
            8: (1, 2, 4, 8), 9: (16, 32)}


def native(word):
    q = 0
    disp = [0] * 6
    positive = [0] * 3
    path = []
    prefixes = set()
    for op in word:
        q = T[q][OPS.index(op)]
        assert q != 8
        for signed_axis in STEPS[op]:
            path.append(signed_axis)
            prefixes.add(tuple(path))
            disp[abs(signed_axis) - 1] += (signed_axis > 0) - (signed_axis < 0)
            if signed_axis > 0:
                positive[signed_axis - 1] += 1
    return SIG[q], tuple(disp), tuple(positive), prefixes


def native_if_legal(word):
    q = 0
    disp = [0] * 6
    count = [0] * 3
    for op in word:
        q = T[q][OPS.index(op)]
        if q == 8:
            return None, None, None, None
        for a in STEPS[op]:
            disp[abs(a) - 1] += (a > 0) - (a < 0)
            if a > 0:
                count[a - 1] += 1
    return SIG[q], tuple(disp), tuple(count), None


def early_signatures():
    out = {}
    for h in (2, 3):
        for word in map(''.join, itertools.product(OPS, repeat=h)):
            sig, disp, key, _ = native_if_legal(word)
            if disp == (2, 0, 0, 0, 0, 0) and sig in REQUIRED[h]:
                out.setdefault((h, sig), set()).add(key)
    expected = {(2, 16): {(3, 0, 1)}, (2, 32): {(2, 1, 1)},
                (3, 16): {(3, 1, 1), (4, 0, 1)},
                (3, 32): {(3, 1, 1), (2, 2, 1)}}
    assert out == expected, (out, expected)
    return {str(k): [list(v) for v in sorted(values)] for k, values in sorted(out.items())}


def verify(profile):
    rows = sorted(profile['demands'], key=lambda d: (d['window'], d['signature']))
    assert len(rows) == 24
    assert {(d['window'], d['signature']) for d in rows} == {
        (h, s) for h, ss in REQUIRED.items() for s in ss}
    labels = [(d['window'], d['signature']) for d in rows]
    supports = collections.defaultdict(int)
    key_supports = collections.defaultdict(int)
    pathsets = []
    for i, row in enumerate(rows):
        sig, disp, key, prefixes = native(row['word'])
        assert len(row['word']) == row['window']
        assert sig == row['signature']
        assert disp == (2, 0, 0, 0, 0, 0)
        pathsets.append(prefixes)
        key_supports[key] |= 1 << i
        for p in prefixes:
            supports[p] |= 1 << i
    full = set.union(*pathsets)
    assert len(full) == len(supports) == 94
    assert len(key_supports) == 7
    late = set.union(*(pathsets[i] for i, (h, _) in enumerate(labels) if h in (8, 9)))
    h8 = set.union(*(pathsets[i] for i, (h, _) in enumerate(labels) if h == 8))
    h9 = set.union(*(pathsets[i] for i, (h, _) in enumerate(labels) if h == 9))
    assert late == full and (len(h8), len(h9), len(h8 & h9)) == (72, 40, 18)
    support_counts = collections.Counter(supports.values())
    assert sum(support_counts.values()) == 94
    hist = collections.Counter()
    released = collections.Counter()
    exceptions = []
    for quad in itertools.combinations(range(24), 4):
        q = sum(1 << i for i in quad)
        vanished = sum(cnt for s, cnt in support_counts.items() if s & q == s)
        fixed_cost = 94 - vanished
        # Independent direct construction of unchanged-path union.
        fixed = set.union(*(pathsets[i] for i in range(24) if i not in quad))
        assert len(fixed) == fixed_cost
        budget = vanished - 1
        hist[budget] += 1
        if budget < 0:
            continue
        removed_keys = tuple(sorted(k for k, s in key_supports.items() if s & q == s))
        released[removed_keys] += 1
        seventh = (7, 4, 1) if profile['profile_id'] == 'A' else (6, 5, 1)
        if seventh in removed_keys:
            exceptions.append(tuple(labels[i] for i in quad))
        assert set(removed_keys) - {(2, 1, 1), (3, 0, 1), (3, 1, 1), seventh} == set()
    assert hist[-1] == 3060
    assert sum(v for k, v in hist.items() if k >= 0) == 7566
    assert exceptions == [((8, 1), (8, 2), (8, 4), (8, 8))]
    expected_release = {
        (): 5395,
        ((2, 1, 1),): 974,
        ((3, 0, 1),): 974,
        ((3, 1, 1),): 99,
        ((2, 1, 1), (3, 0, 1)): 111,
        ((2, 1, 1), (3, 1, 1)): 6,
        ((3, 0, 1), (3, 1, 1)): 6,
        (seventh,): 1,
    }
    assert dict(released) == expected_release, (released, expected_release)
    assert sum(released.values()) == 7566
    return {'profile': profile['profile_id'], 'baseline_cost': 94,
            'late_H8_H9_cost': len(late), 'H8_cost': len(h8),
            'H9_cost': len(h9), 'H8_H9_overlap': len(h8 & h9),
            'four_label_sets': sum(hist.values()),
            'fixed_prefix_blocked': hist[-1], 'remaining_key_forcing_cases': 7565,
            'unrestricted_H8_exception': len(exceptions),
            'budget_histogram': dict(sorted(hist.items())),
            'support_size_histogram': dict(sorted(collections.Counter(
                m.bit_count() for m in supports.values()).items()))}


def main():
    data = json.loads(Path(sys.argv[1]).read_text(encoding='utf8'))
    assert data['frozen_scientific_pin'] == PIN
    print('H2_H3_SUPPORT', json.dumps(early_signatures(), sort_keys=True))
    results = [verify(p) for p in data['profiles']]
    assert len(results) == 2
    assert results[0]['budget_histogram'] == results[1]['budget_histogram']
    print(json.dumps({'schema': 'EC49FGS_AUTHOR_EXACT_AUDIT_V1', 'pin': PIN,
                      'profiles': results}, indent=2))
    print('EC49FGS_EXACT_PASS')


if __name__ == '__main__':
    main()
