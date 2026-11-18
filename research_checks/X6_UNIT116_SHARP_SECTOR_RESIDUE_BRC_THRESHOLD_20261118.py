#!/usr/bin/env python3
"""Unit116: exact fixed-positive R063 sector residue and native N-BRC thresholds.

Original frozen reference: experiments/tool_discovery_native_geometry_of_numbers_minima_calculus_20260822.py
at fd2bcff10ca6e147348b6c1236027fc0d2877df3, Git blob
643b2bac659a445891dcb5588b647972977104e0, lines 77-98, 101-132.
This independent checker does not execute the original source or the R063 C3/C4 benchmark.
"""
import json
from math import comb, isqrt


def require(ok, note):
    if not ok:
        raise RuntimeError(note)


def sector_ball(radius):
    return [(a, b, 0) for a in range(radius + 1)
            for b in range(isqrt(radius * radius - a * a) + 1)]


def residue(point, mod):
    return (point[0] % mod, point[1] % mod)


def brc(point):
    a, b, c = point
    require(c == 0 and a >= 0 and b >= 0, 'OUT_OF_FIXED_POSITIVE_CHART')
    return comb(a + b, a)


def analyze(mod):
    previous = sector_ball(mod - 1)
    threshold = sector_ball(mod)
    successor = sector_ball(mod + 1)
    require(len({residue(p, mod) for p in previous}) == len(previous), 'early residue alias')
    buckets = {}
    for p in threshold:
        buckets.setdefault(residue(p, mod), []).append(p)
    colliding_pairs = []
    for points in buckets.values():
        for i, a in enumerate(points):
            for b in points[i + 1:]:
                colliding_pairs.append((a, b))
                require(brc(a) == brc(b), 'early BRC mismatch')
    require(len(colliding_pairs) == 3, 'unexpected threshold collision count')
    require(set(tuple(x) for x in colliding_pairs) == {
        ((0, 0, 0), (0, mod, 0)), ((0, 0, 0), (mod, 0, 0)),
        ((0, mod, 0), (mod, 0, 0))
    }, 'unexpected threshold collision endpoints')
    # The original function returns the first colliding pair in a-major, b-minor order.
    seen = {}
    first = None
    for p in threshold:
        q = residue(p, mod)
        if q in seen:
            first = [list(seen[q]), list(p), list(q)]
            break
        seen[q] = p
    require(first == [[0, 0, 0], [0, mod, 0], [0, 0]], 'original first_collision ordering mismatch')
    x, y = (0, 1, 0), (mod, 1, 0)
    require(x in successor and y in successor, 'BRC witness outside radius m+1')
    require(residue(x, mod) == residue(y, mod), 'BRC witness not same residue')
    require(brc(x) == 1 and brc(y) == mod + 1, 'BRC witness count mismatch')
    cap_r = 0
    while len(sector_ball(cap_r)) <= mod * mod:
        cap_r += 1
    require(cap_r >= mod, 'pigeonhole bound earlier than first collision')
    return {'modulus': mod, 'first_residue_collision_radius': mod,
            'first_BRC_mismatch_radius': mod + 1,
            'threshold_sector_point_count': len(threshold),
            'unordered_colliding_pairs_at_threshold': 3,
            'first_collision': first,
            'BRC_witness': {'points': [list(x), list(y)], 'values': [1, mod + 1]},
            'original_capacity_guarantee_radius': cap_r,
            'capacity_radius_gap': cap_r - mod}


def main():
    rows = [analyze(m) for m in range(2, 101)]
    report = {'schema': 'X6_UNIT116_FIXED_CHART_RESIDUE_BRC_THRESHOLD_V1',
              'frozen_original_blob_sha1': '643b2bac659a445891dcb5588b647972977104e0',
              'check_type': 'INDEPENDENT_EXACT_INTEGER_REIMPLEMENTATION',
              'modulus_range': [2, 100], 'verified_moduli': len(rows),
              'all_sharp_threshold_tests_passed': True,
              'original_check_spatial_moduli': [2, 20],
              'original_check_spatial_comparison': rows[:19],
              'capacity_lags_first_collision_moduli_2_to_20': [row['modulus'] for row in rows[:19] if row['capacity_radius_gap'] > 0],
              'max_capacity_gap_2_to_20': max(row['capacity_radius_gap'] for row in rows[:19])}
    print(json.dumps(report, sort_keys=True, ensure_ascii=False, separators=(',', ':')))


if __name__ == '__main__':
    main()
