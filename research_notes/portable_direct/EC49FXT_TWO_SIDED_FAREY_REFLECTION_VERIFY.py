#!/usr/bin/env python3
"""Exact BRC16943 C11/Farey two-sided reflection and 7-miss bound.

Standard library only. The predicate is the frozen EC49FWS P10 44-residue
projective readout. This verifies the rational-anchor trace, not native X6.
"""
import itertools
import collections
import json
import math

SLOPES = {(0, 0): {3}, (0, 1): {0, 3, 4, 5},
          (1, 0): {2, 3, 4, 5}, (1, 1): {2, 3}}

def p10(h, n):
    h, n = h % 10, n % 10
    if h % 5 == n % 5 == 0:
        return False
    slope = 5 if h % 5 == 0 else n * pow(h, -1, 5) % 5
    return slope in SLOPES[(h % 2, n % 2)]

def c11(h, n):
    return p10(h, n) and (9*h + 10*n) % 11 != 0

def words():
    result = set()
    primitive = 0
    for a, b in itertools.product(range(10), repeat=2):
        if math.gcd(math.gcd(a, b), 10) != 1:
            continue
        primitive += 1
        h, n = next((h, n) for h, n in itertools.product(range(10), repeat=2)
                    if ((b-a)*h-a*n+1) % 10 == 0)
        result.add(sum(int(p10(h+a*t, n+(b-a)*t)) << t for t in range(10)))
    assert primitive == 72 and len(result) == 50
    return result

def trace(u, hole):
    return tuple(bool((u >> (t % 10)) & 1) and
                 (hole is None or t % 11 != hole) for t in range(110))

def max_misses(bits):
    good = [t for t in range(110) if bits[t]]
    assert good
    return max((good[(i+1) % len(good)]-good[i]-1) % 110
               for i in range(len(good)))

def bases(a, b):
    assert 0 < a < b and math.gcd(a, b) == 1
    dminus = pow(a, -1, b)
    dplus = b-dminus
    hminus = (a*dminus-1)//b
    hplus = (a*dplus+1)//b
    left = (hminus, dminus-hminus, dminus)
    right = (hplus, dplus-hplus, dplus)
    assert left[0]+right[0] == a
    assert left[1]+right[1] == b-a
    assert left[2]+right[2] == b
    return left, right

def anchor_trace(a, b, side):
    h, n, _ = bases(a, b)[0 if side == -1 else 1]
    return tuple(c11(h+a*t, n+(b-a)*t) for t in range(110))

def last_certified(a, b, side, height):
    h, n, d = bases(a, b)[0 if side == -1 else 1]
    top = (height-d)//b
    assert top >= 8
    times = [t for t in range(top-7, top+1)
             if h+a*t > 0 and n+(b-a)*t > 0 and c11(h+a*t, n+(b-a)*t)]
    assert times, (a, b, side, height)
    t = max(times)
    hh, dd = h+a*t, d+b*t
    assert b*hh-a*dd == side
    assert dd <= height and height-dd <= 8*b-1
    return {'t':t, 'numerator':hh, 'denominator':dd,
            'phase_misses':top-t, 'denominator_deficit':height-dd}

def main():
    ws = words()
    assert all(p10(h, n) == p10(-h, -n)
               for h, n in itertools.product(range(10), repeat=2))
    stats = collections.Counter()
    worst = []
    for u in ws:
        for hole in (None, *range(11)):
            mm = max_misses(trace(u, hole))
            stats[mm] += 1
            if mm == 7:
                worst.append([u, hole])
    assert sum(stats.values()) == 600
    assert max(stats) == 7
    assert max(max_misses(trace(u, None)) for u in ws) == 5
    assert sorted(worst) == sorted([[u, z] for u in [23, 833] for z in range(11)])
    checks = []
    for a, b in ((1, 2), (1, 3), (2, 3), (3, 7), (5, 11), (8, 13), (11, 37)):
        left, right = anchor_trace(a, b, -1), anchor_trace(a, b, 1)
        assert all(right[s] == left[(-s-1) % 110] for s in range(110))
        assert max_misses(left) <= 7 and max_misses(right) <= 7
        at = 16*b
        low = last_certified(a, b, -1, at)
        high = last_certified(a, b, +1, at)
        assert high['numerator']*low['denominator'] - low['numerator']*high['denominator'] == low['t']+high['t']+1
        checks.append({'anchor':[a,b], 'left_gap':max_misses(left),
                       'right_gap':max_misses(right), 'at_height_16b':at,
                       'nearest_left':low, 'nearest_right':high})
    low = last_certified(3,7,-1,1096)
    high = last_certified(3,7,+1,1096)
    assert low == {'t':148,'numerator':446,'denominator':1041,'phase_misses':7,'denominator_deficit':55}
    assert high['numerator'] == 460 and high['denominator'] == 1073
    assert 460*1041-446*1073 == 302 == 148+153+1
    return {'result':'ALL PASS', 'scientific_pin':'BRC16943',
            'population':'50 frozen P10 masks times 12 full/one-hole factors',
            'primitive_directions':72, 'distinct_masks':len(ws),
            'factor_cases':12, 'period':110, 'cases':sum(stats.values()),
            'max_consecutive_missing_phases':max(stats),
            'max_misses_full_factor':5,
            'missing_run_histogram':{str(k):stats[k] for k in sorted(stats)},
            'sharp_mask_hole_pairs':len(worst),
            'sharp_mask_ids':sorted(set(p[0] for p in worst)),
            'explicit_anchor':[3,7], 'sharp_height':1096,
            'sharp_left':low, 'sharp_right':high,
            'checked_anchor_reflections':checks,
            'scope':'exact rational-anchor C11 branch, not native X6 dynamics; author crosscheck not independent review'}

if __name__ == '__main__':
    print(json.dumps(main(), indent=2, ensure_ascii=False))
