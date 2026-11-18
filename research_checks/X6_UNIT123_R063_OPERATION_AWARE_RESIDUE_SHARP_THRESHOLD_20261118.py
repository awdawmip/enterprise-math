#!/usr/bin/env python3
"""Unit123: exact R063 fixed-positive-sector one-step BRC sufficiency threshold.
Scientific input: original R063 sector_ball/residue @fd2bcff10ca6e147348b6c1236027fc0d2877df3;
this standalone independent check uses the identical declared integer formulas.
No native C3/C4 benchmark or GitHub mutation occurs in this program.
"""
import json
from collections import defaultdict
from math import comb, isqrt


def sector_ball(radius):
    return [(a, b) for a in range(radius + 1)
            for b in range(isqrt(radius * radius - a * a) + 1)]


def brc(a, b):
    return comb(a + b, a)


def key(a, b, m):
    return (a % m, b % m, a * a + b * b, a + b, brc(a, b))


def next_brc(a, b, axis):
    return brc(a + (axis == 0), b + (axis == 1))


def check(m):
    lower = sector_ball(m - 1)
    if len({(a % m, b % m) for a, b in lower}) != len(lower):
        raise AssertionError('noninjective below sharp threshold')
    fibers = defaultdict(list)
    for a, b in sector_ball(m):
        fibers[(a % m, b % m)].append((a, b))
    nonsingleton = {r: pts for r, pts in fibers.items() if len(pts) > 1}
    expected = {(0, 0): [(0, 0), (0, m), (m, 0)]}
    if nonsingleton != expected:
        raise AssertionError(('wrong first residue fiber', m, nonsingleton))
    augmented = defaultdict(list)
    for pts in fibers.values():
        for a, b in pts:
            augmented[key(a, b, m)].append((a, b))
    duplicated = [sorted(pts) for pts in augmented.values() if len(pts) > 1]
    if duplicated != [[(0, m), (m, 0)]]:
        raise AssertionError(('wrong augmented equality fiber', m, duplicated))
    a, b = (m, 0)
    c, d = (0, m)
    if key(a, b, m) != key(c, d, m):
        raise AssertionError('different current readouts')
    if (next_brc(a, b, 1), next_brc(c, d, 1)) != (m + 1, 1):
        raise AssertionError('incorrect named next operation witness')
    if (next_brc(a, b, 0), next_brc(c, d, 0)) != (1, m + 1):
        raise AssertionError('incorrect reflected named next operation witness')
    if len({brc(a, b) for pts in fibers.values() for a, b in pts if len(pts)>1}) != 1:
        raise AssertionError('current BRC should still be constant at R=m')
    return {'m': m, 'below_points': len(lower),
            'threshold_points': sum(len(v) for v in fibers.values()),
            'current_ambiguous_augmented_fibers': len(duplicated),
            'named_positive_step_BRC_difference': m,
            'named_positive_step_BRC_ratio': m + 1}


def main():
    results = [check(m) for m in range(1, 101)]
    output = {
        'schema': 'X6_UNIT123_R063_OPERATION_AWARE_SHARP_THRESHOLD_V1',
        'frozen_old_R063_blob': '643b2bac659a445891dcb5588b647972977104e0',
        'm_range': [1, 100],
        'tested_moduli': len(results),
        'below_threshold_points_total': sum(x['below_points'] for x in results),
        'threshold_points_total': sum(x['threshold_points'] for x in results),
        'ambiguous_augmented_fibers_total': sum(x['current_ambiguous_augmented_fibers'] for x in results),
        'max_named_step_BRC_difference': max(x['named_positive_step_BRC_difference'] for x in results),
        'max_named_step_BRC_ratio': max(x['named_positive_step_BRC_ratio'] for x in results),
        'selected': [x for x in results if x['m'] in (1, 2, 3, 20, 50, 100)],
        'status': 'EXACT_ENUMERATION_PYTHON_NORMAL_OPTIMIZED_CHECKED_NO_ORIGINAL_BENCHMARK',
    }
    print(json.dumps(output, ensure_ascii=False, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    main()
