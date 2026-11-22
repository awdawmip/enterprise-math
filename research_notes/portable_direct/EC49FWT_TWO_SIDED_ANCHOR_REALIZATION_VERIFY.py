#!/usr/bin/env python3
"""EC49FWT: exact integer census of Farey +/-1 traces, frozen BRC16943.
The modulo-10 support and modulo-11 single-hole factor are retained jointly.
"""
from collections import defaultdict
from itertools import combinations, product
from math import comb, gcd
import json

SLOPES = {(0, 0): {3}, (0, 1): {0, 3, 4, 5},
          (1, 0): {2, 3, 4, 5}, (1, 1): {2, 3}}
FULL = (1 << 11) - 1
GROUPS = ((1, 4, 6, 9), (2, 7), (3, 8))


def p10(h, n):
    h, n = h % 10, n % 10
    if h % 5 == 0 and n % 5 == 0:
        return False
    slope = 5 if h % 5 == 0 else n * pow(h, -1, 5) % 5
    return slope in SLOPES[(h % 2, n % 2)]


def c11(h, n):
    return p10(h, n) and (9 * h + 10 * n) % 11 != 0


def normalized(a, y, sign):
    """Unique Euclidean seed 0<=h0<a; then lexicographic mod-10 rephasing."""
    assert a > 0 and y > 0 and gcd(a, y) == 1 and sign in (-1, 1)
    h0 = sign * pow(y, -1, a) % a if a > 1 else 0
    n0 = (y * h0 - sign) // a
    assert y * h0 - a * n0 == sign
    x, z = next((x, z) for x, z in product(range(10), repeat=2)
                if (y * x - a * z - sign) % 10 == 0)
    shifts = [t for t in range(10)
              if (h0 + a * t - x) % 10 == 0
              and (n0 + y * t - z) % 10 == 0]
    assert len(shifts) == 1
    t0 = shifts[0]
    h1, n1 = h0 + a * t0, n0 + y * t0
    mask = sum(1 << t for t in range(10) if p10(h1 + a * t, n1 + y * t))
    D, L0 = (9 * a + 10 * y) % 11, (9 * h1 + 10 * n1) % 11
    assert D or L0
    hole = (-L0 * pow(D, -1, 11)) % 11 if D else None
    for t in range(110):
        direct = c11(h1 + a * t, n1 + y * t)
        crt = bool(mask >> (t % 10) & 1) and (hole is None or t % 11 != hole)
        assert direct == crt
    return mask, hole, h1, n1


def frozen_left():
    words = set()
    directions = 0
    for a, y in product(range(10), repeat=2):
        if gcd(gcd(a, y), 10) != 1:
            continue
        directions += 1
        x, z = next((x, z) for x, z in product(range(10), repeat=2)
                    if (y * x - a * z + 1) % 10 == 0)
        words.add(sum(1 << t for t in range(10)
                      if p10(x + a * t, z + y * t)))
    assert directions == 72 and len(words) == 50
    return words


def correlation(word, size):
    return tuple(sum((word >> i & 1) * (word >> ((c - i) % size) & 1)
                     for i in range(size)) for c in range(size))


def spectrum(u, v):
    ku, kv = correlation(u, 10), correlation(v, 11)
    return tuple(2 * (u.bit_count() * v.bit_count() - x * y)
                 for x in ku for y in kv)


def census(limit):
    found = {-1: {}, 1: {}}
    sign_masks = {-1: set(), 1: set()}
    anchors = 0
    for b in range(2, limit + 1):
        for a in range(1, b):
            if gcd(a, b) != 1:
                continue
            anchors += 1
            for sign in (-1, 1):
                u, hole, h, n = normalized(a, b - a, sign)
                key = (u, hole)
                found[sign].setdefault(key, (a, b))
                sign_masks[sign].add(u)
                assert (b - a) * h - a * n == sign
    return found, sign_masks, anchors


def main():
    found, masks, count = census(139)
    frozen = frozen_left()
    assert masks[-1] == frozen
    assert len(masks[-1]) == len(masks[1]) == 50
    assert len(masks[-1] & masks[1]) == 24
    assert len(found[-1]) == len(found[1]) == 600
    max_den = {str(s): max(b for a, b in found[s].values()) for s in (-1, 1)}
    assert max_den == {'-1': 139, '1': 125}
    assert all({v for u, v in found[s] if u == word} == {None, *range(11)}
               for s in (-1, 1) for word in masks[s])
    # Check the reflection bridge using the same integer seed, not an inferred
    # relationship between independently chosen canonical phases.
    mirror_checks = 0
    for b in range(2, 140):
        for a in range(1, b):
            if gcd(a, b) != 1:
                continue
            u, hole, h, n = normalized(a, b - a, -1)
            for t in range(110):
                assert c11(-h + a * t, -n + (b - a) * t) == \
                       c11(h - a * t, n - (b - a) * t)
                mirror_checks += 1
    # The three same-spectrum, same-mass minimal difference pairs actually
    # occur among reduced anchors with each identical missing-column factor.
    evidence = {}
    for group in GROUPS:
        group_pairs = [(u, w) for u, w in combinations(sorted(frozen), 2)
                       if tuple(j for j in range(10) if (u ^ w) >> j & 1) == group
                       and u.bit_count() == w.bit_count()
                       and correlation(u, 10) == correlation(w, 10)]
        assert group_pairs
        u, w = group_pairs[0]
        witness = []
        for hole in range(11):
            v = FULL ^ (1 << hole)
            assert spectrum(u, v) == spectrum(w, v)
            assert (u, hole) in found[-1] and (w, hole) in found[-1]
            witness.append({'hole': hole, 'first_anchor_1': found[-1][(u, hole)],
                            'first_anchor_2': found[-1][(w, hole)]})
        evidence[','.join(map(str, group))] = {
            'masks': [u, w], 'sample_hole_zero': witness[0],
            'max_witness_denominator': max(b for item in witness
                                            for a, b in (item['first_anchor_1'],
                                                         item['first_anchor_2']))}
    # Reuse the exact existing 600-state complete-spectrum population.
    fibers = defaultdict(list)
    for u in sorted(frozen):
        for hole in [None, *range(11)]:
            v = FULL if hole is None else FULL ^ (1 << hole)
            fibers[spectrum(u, v)].append((u, hole))
    assert len(fibers) == 478
    assert sorted(len(v) for v in fibers.values()).count(2) == 122
    assert max(map(len, fibers.values())) == 2
    for k in (1, 2, 3, 4):
        sites = [(j, column) for column in range(k) for j in (1, 2, 3)]
        minimum = min(sum(bool((u ^ w) >> j & 1) and
                          (hole is None or column != hole)
                          for j, column in sites)
                      for f in fibers.values() if len(f) == 2
                      for (u, hole), (w, hole2) in [f]
                      if hole == hole2)
        assert minimum == k - 1
    return {
        'status': 'ALL PASS', 'research_unit': 'EC49FWT',
        'frozen_science_pin': 'BRC16943',
        'population': 'reduced rational a/b in (0,1), 2<=b<=139, Euclidean/lexicographic normalized determinant +/-1 lines',
        'anchors_tested': count, 'direct_C11_CRT_site_checks': count * 110 * 2,
        'mirror_site_checks': mirror_checks,
        'left_masks': len(masks[-1]), 'right_masks': len(masks[1]),
        'mask_intersection': len(masks[-1] & masks[1]),
        'left_actual_states': len(found[-1]), 'right_actual_states': len(found[1]),
        'left_max_first_witness_denominator': max_den['-1'],
        'right_max_first_witness_denominator': max_den['1'],
        'spectrum_fibers': len(fibers), 'two_state_fibers': 122,
        'minimal_difference_pair_witnesses': evidence,
        'actual_left_anchor_fixed_site_minima': {str(r): 3 * (r + 1) for r in range(1, 11)},
        'scope': 'anchor hidden; indexed trace physical sites; H>16b for nearest certified fractions; no six-dimensional native dynamics',
        'status_of_proof': 'AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED'
    }


if __name__ == '__main__':
    print(json.dumps(main(), ensure_ascii=False, indent=2))
