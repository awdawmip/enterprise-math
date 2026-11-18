#!/usr/bin/env python3
"""Exact checks of EC49FMG published vector and signed-X6 84-prefix witness.
Run adjacent to the two EC49FMG JSON records in the research notes directory.
"""
import base64, collections, hashlib, json, pathlib, sys, zlib, itertools, functools
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / 'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
from EC49FGW_RADIUS5_SCREEN import PIN, all_words, raw_key, pref, T, SIG, OPS, STEPS
V = json.loads((HERE / 'EXACT_VECTOR_EC49FMG.json').read_text())
W = json.loads((HERE / 'WITNESS84_EC49FMG.json').read_text())
assert V['scientific_pin'] == W['scientific_pin'] == PIN == 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
costs = zlib.decompress(base64.b64decode(V['costs_zlib_base64']))
assert len(costs) == V['feasible'] == 6315
assert hashlib.sha256(costs).hexdigest() == V['cost_bytes_sha256']
assert min(costs) == 84 and max(costs) == 204
assert [i for i, c in enumerate(costs) if c == 84] == [5883]
assert costs[2473] == costs[4515] == 86 and costs[5755] == 90
assert V['total_radius_two'] == 78561 and V['infeasible'] == 72246
catalogue = list(all_words())
assert len(catalogue) == 178850
labels = sorted({label for label, _ in catalogue})
assert len(labels) == 24
support, keys_by_word = collections.defaultdict(int), {}
for lab, word in catalogue:
    key = raw_key(word)
    support[key] |= 1 << labels.index(lab)
    keys_by_word[(lab, word)] = key
assert len(support) == 94
BASE = set(map(tuple, V['baseline_keys']))
assert len(BASE) == 7
feasible = []
full = (1 << 24) - 1
for removed in itertools.combinations(sorted(BASE), 2):
    for added in itertools.combinations(sorted(set(support) - BASE), 2):
        K = sorted(BASE - set(removed) | set(added))
        if functools.reduce(int.__or__, (support[k] for k in K), 0) == full:
            feasible.append(K)
assert len(feasible) == 6315
assert feasible[W['case_index']] == list(map(tuple, W['keyset']))
assert W['observation_labels'] == [list(q) for q in labels]
assert len(W['operation_words']) == 24
assert hashlib.sha256(('\n'.join(W['operation_words'])).encode()).hexdigest() == W['word_lines_sha256']
prefixes = set()
for label, word in zip(labels, W['operation_words']):
    assert (label, word) in keys_by_word and keys_by_word[(label, word)] in set(map(tuple, W['keyset']))
    assert len(word) == label[0]
    state, coords = 0, [0] * 6
    for op in word:
        state = T[state][OPS.index(op)]
        assert state != 8
        for axis in STEPS[op]:
            coords[abs(axis) - 1] += 1 if axis > 0 else -1
    assert SIG[state] == label[1] and coords == [2, 0, 0, 0, 0, 0]
    prefixes.update(pref(word))
assert len(prefixes) == W['distinct_nonempty_signed_x6_prefixes'] == 84
print('EC49FMG_VECTOR_AND_84_WITNESS_EXACT_PASS', len(costs), len(feasible), len(prefixes))
