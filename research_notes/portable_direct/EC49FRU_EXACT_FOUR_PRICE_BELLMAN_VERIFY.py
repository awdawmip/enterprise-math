#!/usr/bin/env python3
"""EC49FRU exact all-228 BRC integer Bellman and complete six-tree replay.

Copy this file to code/ inside the extracted EC49FRS–FRT original evidence
archive, alongside EC49FRQ_INDEPENDENT_ALL228.py and EC49FQI_NATIVE_DATA.py.
Retain source/frozen_original_master.txt and source/EC49FPG_PROFILE.csv.
Run: python code/EC49FRU_EXACT_FOUR_PRICE_BELLMAN_VERIFY.py

Pure Python standard library. Both imported original raw reconstructions
assert their own frozen SHA256 and reconstruct all original BRC observations.
"""
from pathlib import Path
import sys, json, collections, time
from functools import cache

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / 'code'))

from EC49FRQ_INDEPENDENT_ALL228 import PARTS, ALL, OBS, subset_keys
from EC49FQI_NATIVE_DATA import V, keys, PIN

assert PIN == 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert len(OBS) == len(V) == 228 and len(OBS[0]) == 141
native = lambda q: q if q < 144 else 144 + keys.index(subset_keys[q - 144])
assert all(tuple(OBS[q]) == tuple(V[native(q)]) for q in range(228))

CH = (32, 34, 140, 142)
DELTA = (3, 3, 1, 1)
UNIT = 141
T0 = time.monotonic()

def solve(parts, index):
    prices = [
        UNIT + DELTA[CH.index(index(i))] if index(i) in CH else UNIT
        for i in range(228)
    ]

    @cache
    def bell(s):
        if s.bit_count() == 1:
            return 0, ()
        best = 10**60
        first = []
        for q, partition in enumerate(parts):
            children = [s & block for block in partition if s & block]
            if len(children) < 2:
                continue
            val = prices[q] * s.bit_count() + sum(bell(t)[0] for t in children)
            if val < best:
                best, first = val, [q]
            elif val == best:
                first.append(q)
        return best, tuple(first)

    val, options = bell(ALL)
    return val, sorted(index(q) for q in options), bell

v1, opt1, dp1 = solve(PARTS, native)
from collections import defaultdict
parts2 = []
for query in V:
    f = defaultdict(int)
    for i, answer in enumerate(query):
        f[answer] |= 1 << i
    parts2.append(tuple(f.values()))
v2, opt2, dp2 = solve(parts2, lambda i: i)
assert v1 == v2 == 42159, (v1, v2)
assert opt1 == opt2 == [32, 34, 46, 93, 140, 142]

def make_tree(mask, first=None):
    if mask.bit_count() == 1:
        return {'leaf': mask.bit_length() - 1}
    q = first if first is not None else dp1(mask)[1][0]
    children = {}
    for part in PARTS[q]:
        subset = mask & part
        if not subset:
            continue
        state = (subset & -subset).bit_length() - 1
        key = str(OBS[q][state])
        assert key not in children
        children[key] = make_tree(subset)
    assert len(children) >= 2
    return {'q': native(q), 'children': children}

expected = {
    32: (296, [141, 0, 0, 0]),
    34: (296, [0, 141, 0, 0]),
    140: (298, [0, 0, 141, 0]),
    142: (298, [0, 0, 0, 141]),
    46: (299, [0, 0, 0, 0]),
    93: (299, [0, 0, 0, 0]),
}
witness = {}
for root in opt1:
    original = root if root < 144 else 144 + subset_keys.index(keys[root - 144])
    tree = make_tree(ALL, original)
    uses = collections.Counter()
    maxdepth = 0
    for i in range(141):
        node = tree
        visited = set()
        depth = 0
        while 'leaf' not in node:
            q = node['q']
            assert 0 <= q < 228 and q not in visited
            visited.add(q)
            uses[q] += 1
            node = node['children'][str(V[q][i])]
            depth += 1
        assert node['leaf'] == i
        maxdepth = max(maxdepth, depth)
    total = sum(uses.values())
    charged = {str(q): uses[q] for q in CH}
    weighted = UNIT * total + sum(DELTA[i] * uses[CH[i]] for i in range(4))
    assert weighted == v1
    assert total == expected[root][0]
    assert [charged[str(q)] for q in CH] == expected[root][1]
    assert maxdepth == 3
    witness[str(root)] = {
        'total_path_uses': total,
        'charged_named_uses': charged,
        'max_depth': maxdepth,
        'tree': tree
    }
    print('tree', root, 'uses', total, 'incidence', charged, 'depth', maxdepth, flush=True)

result = {
    'schema': 'EC49FRU_FOUR_INDEPENDENT_NAMED_SURCHARGE_EXACT_ANCHOR_V1',
    'frozen_pin': PIN,
    'raw_source_sha256': {
        'master': 'cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e',
        'csv': 'a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f'
    },
    'named_observer_count': 228, 'named_state_count': 141,
    'configuration_count': 310,
    'all_228_original_named_responses_matched_between_two_raw_reconstructions': True,
    'price_anchor_deltas': dict(zip(map(str, CH), DELTA)),
    'per_observation_base_price_integer_units': UNIT,
    'independent_bellman_integer_costs': [v1, v2],
    'optimal_first_named_observers': opt1,
    'reached_subsets_each': [dp1.cache_info().currsize, dp2.cache_info().currsize],
    'optimal_complete_trees': witness,
    'proved_formula': '141*V(a,b,c,d)/t=min(296+141*a,296+141*b,298+141*c,298+141*d,299) for nonnegative real a,b,c,d',
    'status': 'AUTHOR_PROVED_EXACT_FINITE_BELLMAN_TWO_RAW_RECONSTRUCTIONS_NOT_INDEPENDENT_REVIEW',
    'elapsed_seconds': round(time.monotonic() - T0, 2)
}
path = BASE / 'evidence/EC49FRU_FOUR_DIMENSIONAL_NATIVE_BRC_ANCHOR_CERTIFICATE.json'
path.parent.mkdir(exist_ok=True, parents=True)
path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print('PASS', v1, opt1, 'subsets', result['reached_subsets_each'],
      'elapsed', result['elapsed_seconds'], 'evidence', path, flush=True)
