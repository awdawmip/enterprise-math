#!/usr/bin/env python3
"""Reproduce exact finite checks for the R5 (2,1) coupled-suffix recourse spectrum.
Standard library only; exact integer brute force, independent of the prior R5 verifier.
"""
from collections import Counter
from itertools import combinations
from math import comb
import json

PREFIX = (3, 2, 2, 3)
RADIUS = 2

def position_vector(m, mask):
    gaps = list(PREFIX + (2, 1) * m)
    if mask & 1:
        gaps[0] -= 1
    if mask & 2:
        gaps[3] -= 1
    xs = [0]
    for gap in gaps:
        xs.append(xs[-1] + gap)
    return xs

def optimizers(m, mask):
    xs = position_vector(m, mask)
    n, k = len(xs), m + 3
    minimum, family = None, set()
    for chosen in combinations(range(n), k):
        nearest = [min(abs(x - xs[j]) for j in chosen) for x in xs]
        if max(nearest) > RADIUS:
            continue
        cost = sum(nearest)
        if minimum is None or cost < minimum:
            minimum, family = cost, {chosen}
        elif cost == minimum:
            family.add(chosen)
    assert minimum is not None
    return minimum, family

def distance(s, t):
    return len(set(s).difference(t))

def pair_spectrum(a, b):
    return Counter(distance(s, t) for s in a for t in b)

def nearest_spectrum(a, b):
    return Counter(min(distance(s, t) for t in b) for s in a)

def expected_pair_spectrum(base, pairs):
    result = Counter()
    for d, count in base.items():
        for h in range(pairs + 1):
            result[d + h] += count * 2 ** pairs * comb(pairs, h)
    return result

def jsonify(counter):
    return {str(k): counter[k] for k in sorted(counter)}

def check():
    costs1 = [optimizers(1, mask) for mask in range(4)]
    assert [v for v, _ in costs1] == [5] * 4
    base_f0 = costs1[0][1]
    base_pairs = [pair_spectrum(f, base_f0) for _, f in costs1]
    base_nearest = [nearest_spectrum(f, base_f0) for _, f in costs1]
    expected_base_pairs = [
        {0:5, 1:12, 2:6, 3:2},
        {0:5, 1:23, 2:22, 3:10},
        {0:5, 1:19, 2:17, 3:4},
        {0:5, 1:30, 2:37, 3:13},
    ]
    expected_base_nearest = [
        {0:5}, {0:5,1:6,2:1}, {0:5,1:4}, {0:5,1:10,2:2}
    ]
    assert base_pairs == expected_base_pairs, base_pairs
    assert base_nearest == expected_base_nearest, base_nearest
    rows = []
    for m in range(1, 7):
        outcomes = [optimizers(m, mask) for mask in range(4)]
        f0 = outcomes[0][1]
        assert [cost for cost, _ in outcomes] == [m + 4] * 4
        assert [len(f) for _, f in outcomes] == [v * 2 ** (m - 1) for v in (5,12,9,17)]
        each = []
        for mask, (_, f) in enumerate(outcomes):
            actual_pair = pair_spectrum(f, f0)
            actual_nearest = nearest_spectrum(f, f0)
            expected_pair = expected_pair_spectrum(base_pairs[mask], m - 1)
            expected_nearest = Counter({d: c * 2 ** (m - 1)
                                        for d, c in base_nearest[mask].items()})
            assert actual_pair == expected_pair, (m,mask,'pair',actual_pair,expected_pair)
            assert actual_nearest == expected_nearest, (m,mask,'nearest')
            each.append({'mask':mask, 'count':len(f), 'pair_spectrum':jsonify(actual_pair),
                         'nearest_spectrum':jsonify(actual_nearest),
                         'worst_nearest':max(actual_nearest)})
        q = outcomes[3][1] - outcomes[1][1] - outcomes[2][1]
        assert len(q) == 2 ** (m - 1)
        assert nearest_spectrum(q,f0) == {2:len(q)}
        rows.append({'m':m, 'n':5+2*m, 'K':3+m, 'cost':m+4, 'Q_count':len(q), 'masks':each})
    return {'status':'PASS_R5_EXACT_RECOURSE_SPECTRUM',
            'scientific_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
            'coverage':'exhaustive all indexed-center choices for m=1..6, masks 0,1,2,3',
            'arithmetic':'Python exact integer (no floating point)',
            'base_pair_spectra':[jsonify(c) for c in base_pairs],
            'base_nearest_spectra':[jsonify(c) for c in base_nearest],
            'rows':rows,
            'independent_review':'NOT_REVIEWED'}

if __name__ == '__main__':
    print(json.dumps(check(), sort_keys=True, ensure_ascii=False, indent=2))
