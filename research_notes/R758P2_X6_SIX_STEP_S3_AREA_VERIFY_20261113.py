#!/usr/bin/env python3
"""Exact exhaustive X6 three-axis six-step loop / candidate S3 transport checker.
Only the declared optional link-to-frame assignment is tested, not a native V39 claim.
"""
import itertools
import json
from collections import Counter, defaultdict

WORDS = tuple(itertools.permutations([(a, s) for a in range(3) for s in (+1, -1)]))
E = (0, 1, 2)
T = ((1, 0, 2), (0, 2, 1), (2, 1, 0))
C3 = {(1, 2, 0), (2, 0, 1)}

def mul(p, q):
    return tuple(p[q[i]] for i in range(3))

def holonomy(word, labels):
    h = E
    for axis, _ in word:
        h = mul(labels[axis], h)  # V39's later-on-left composition convention
    return h

def simple(word):
    pos = [0, 0, 0]
    visited = {(0, 0, 0)}
    for k, (axis, sign) in enumerate(word):
        pos[axis] += sign
        current = tuple(pos)
        if k < 5 and current in visited:
            return False
        visited.add(current)
    return tuple(pos) == (0, 0, 0)

def area(word):
    pos = [0, 0, 0]
    out = [0, 0, 0]
    for axis, sign in word:
        if axis == 1: out[0] += pos[0] * sign
        if axis == 2:
            out[1] += pos[0] * sign
            out[2] += pos[1] * sign
        pos[axis] += sign
    assert pos == [0, 0, 0]
    return tuple(out)

def hname(h):
    return 'e' if h == E else ('r' if h == (1, 2, 0) else 'r2')

patterns = {
    'one_label': (T[0], T[0], T[0]),
    'two_labels': (T[0], T[0], T[1]),
    'three_labels': T,
}
result = {'model': 'X6 Z^6 three selected axes; six signed unit steps one +/- of each',
          'assignment': 'candidate based-frame transport with one axis-involutive S3 transposition per signed direction',
          'words_per_fixed_three_axes': len(WORDS)}
simple_words = [word for word in WORDS if simple(word)]
assert len(WORDS) == 720 and len(simple_words) == 192
result['simple_words_per_fixed_three_axes'] = len(simple_words)
result['all_three_axis_support_over_X6'] = {'axis_triplets': 20, 'all_closed': 14400, 'simple': 3840}
result['by_transposition_pattern'] = {}
for key, labels in patterns.items():
    overall = Counter(hname(holonomy(w, labels)) for w in WORDS)
    simple_ct = Counter(hname(holonomy(w, labels)) for w in simple_words)
    assert set(overall) <= {'e','r','r2'}
    result['by_transposition_pattern'][key] = {'all': dict(sorted(overall.items())), 'simple': dict(sorted(simple_ct.items()))}
    expected = {
        'one_label': ((720, 0, 0), (192, 0, 0)),
        'two_labels': ((432, 144, 144), (96, 48, 48)),
        'three_labels': ((288, 216, 216), (48, 72, 72)),
    }[key]
    assert tuple(overall.get(t, 0) for t in ('e','r','r2')) == expected[0]
    assert tuple(simple_ct.get(t, 0) for t in ('e','r','r2')) == expected[1]

fibers = defaultdict(Counter)
examples = defaultdict(dict)
for w in simple_words:
    a = area(w)
    h = hname(holonomy(w, T))
    fibers[a][h] += 1
    examples[a].setdefault(h, [[axis,sign] for axis,sign in w])
assert len(fibers) == 20
by_nonzero = Counter()
for a, d in fibers.items():
    nnz = sum(v != 0 for v in a)
    by_nonzero[nnz] += sum(d.values())
    if nnz == 3: assert d == {'e': 6}
    elif nnz == 2: assert d == {'r': 6, 'r2': 6}
    else: raise AssertionError((a, d))
assert dict(by_nonzero) == {2: 144, 3: 48}
result['simple_signed_area_fibers'] = {
    'distinct_area_vectors': len(fibers),
    'nonzero_area_component_counts': dict(sorted(by_nonzero.items())),
    'area_111_vector_count': 8, 'area_110_vector_count': 12,
    'each_111_fiber': {'e': 6},
    'each_110_fiber': {'r': 6, 'r2': 6},
    'identity_iff_three_nonzero_areas': True,
}
a = (1, 0, 1)
assert a in examples and set(examples[a]) == {'r','r2'}
result['same_signed_area_distinct_based_frame_witness'] = {'area': list(a), 'r_word': examples[a]['r'], 'r2_word': examples[a]['r2']}
print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
