#!/usr/bin/env python3
"""Exact exhaustive verifier for EC49FWI; stdlib-only, binary words of Z/10."""
import json
from collections import Counter, defaultdict
from math import gcd

N = 10
FULL = (1 << N) - 1
SLOPES = {(0, 0): {3}, (0, 1): {0, 3, 4, 'inf'},
          (1, 0): {2, 3, 4, 'inf'}, (1, 1): {2, 3}}

def positions(mask):
    return {t for t in range(N) if (mask >> t) & 1}

def mask_of(points):
    return sum(1 << t for t in points)

def reflection(mask, c):
    return mask_of((c - t) % N for t in positions(mask))

def half_turn(mask):
    return mask_of((t + 5) % N for t in positions(mask))

def spectrum(mask):
    return tuple((mask ^ reflection(mask, c)).bit_count() for c in range(N))

def correlation(mask):
    S = positions(mask)
    return tuple(sum((c - t) % N in S for t in S) for c in range(N))

def orbit(mask):
    h = half_turn(mask)
    return {mask, h, mask ^ FULL, h ^ FULL}

def p10(h, n):
    h, n = h % N, n % N
    if h % 5 == n % 5 == 0:
        return False
    slope = 'inf' if h % 5 == 0 else (n * pow(h % 5, -1, 5)) % 5
    return slope in SLOPES[(h % 2, n % 2)]

def source_word(a, b):
    h0, n0 = next((h, n) for h in range(N) for n in range(N)
                  if ((b-a)*h - a*n + 1) % N == 0)
    return mask_of(t for t in range(N) if p10(h0+a*t, n0+(b-a)*t))

def crt_defects(mask, missing):
    # missing=None: all mod11 positions occupied; otherwise V=Z11\{missing}.
    W = {t for t in range(110) if (mask >> (t % 10)) & 1
         and (missing is None or t % 11 != missing)}
    return tuple(len(W ^ {(c-t) % 110 for t in W}) for c in range(110))

def predicted_crt_defects(mask, missing):
    d = spectrum(mask)
    k = mask.bit_count()
    if missing is None:
        return tuple(11*d[c % 10] for c in range(110))
    return tuple(10*d[c % 10] if c % 11 == 2*missing % 11
                 else 2*k + 9*d[c % 10] for c in range(110))

def verify():
    fibers = defaultdict(set)
    for mask in range(1 << N):
        s = spectrum(mask)
        fibers[s].add(mask)
        # Exact independent integer definitions: symmetric difference vs convolution.
        assert all(s[c] == 2 * (mask.bit_count() - correlation(mask)[c])
                   for c in range(N))
        assert spectrum(mask ^ FULL) == s
        assert spectrum(half_turn(mask)) == s
    fiber_hist = Counter(map(len, fibers.values()))
    weight_fibers = defaultdict(set)
    for mask in range(1 << N):
        weight_fibers[(spectrum(mask), mask.bit_count())].add(mask)
    weight_hist = Counter(map(len, weight_fibers.values()))
    assert len(weight_fibers) == 473
    assert weight_hist == Counter({1: 32, 2: 386, 4: 55})
    assert len(fibers) == 272
    assert fiber_hist == Counter({2: 32, 4: 240})
    assert all(fiber == orbit(next(iter(fiber))) for fiber in fibers.values())
    # Burnside independent orbit count, including both nonidentity stabilizers.
    fixed_H = sum(half_turn(mask) == mask for mask in range(1 << N))
    fixed_C = sum((mask ^ FULL) == mask for mask in range(1 << N))
    fixed_HC = sum((half_turn(mask) ^ FULL) == mask for mask in range(1 << N))
    assert (fixed_H, fixed_C, fixed_HC) == (32, 0, 32)
    assert (1 << N) + fixed_H + fixed_C + fixed_HC == 4 * len(fibers)

    primitive = [(a, b) for a in range(N) for b in range(N)
                 if gcd(gcd(a, b), N) == 1]
    assert len(primitive) == 72
    actual = {source_word(a, b) for a, b in primitive}
    restricted = defaultdict(set)
    for mask in actual:
        restricted[spectrum(mask)].add(mask)
    rhist = Counter(map(len, restricted.values()))
    restricted_hole = defaultdict(set)
    for mask in actual:
        restricted_hole[(spectrum(mask), mask.bit_count())].add(mask)
    rhist_hole = Counter(map(len, restricted_hole.values()))
    assert len(restricted_hole) == 40
    assert rhist_hole == Counter({1: 30, 2: 10})
    for mask in actual:
        for missing in (None, 0, 6):
            assert crt_defects(mask, missing) == predicted_crt_defects(mask, missing)
    assert sum(p10(h,n) for h in range(N) for n in range(N)) == 44
    assert len(actual) == 50 and len(restricted) == 38
    assert rhist == Counter({1: 26, 2: 12})

    a, b = source_word(1,11), source_word(3,5)
    assert positions(a) == {0,2,3,4,7}
    assert positions(b) == {0,1,3,4,6}
    assert b == (half_turn(a) ^ FULL)
    assert spectrum(a) == spectrum(b) == (4,6,6,6,2,6,4,2,8,6)
    assert all(mask_of((t+d) % N for t in positions(a)) != b
                   and mask_of((d-t) % N for t in positions(a)) != b
                   for d in range(N))
    assert ((a >> 1) & 1) == 0 and ((b >> 1) & 1) == 1
    return {
        'status': 'ALL PASS', 'scientific_pin': 'BRC16943',
        'scope': 'all 1024 binary ten-cycles; 72 frozen primitive mod10 directions',
        'fiber_count': len(fibers), 'fiber_histogram': dict(sorted(fiber_hist.items())),
        'spectrum_plus_weight': {'fiber_count': len(weight_fibers),
                                 'fiber_histogram': dict(sorted(weight_hist.items()))},
        'involution_fixed_points': {'half_turn':fixed_H,'complement':fixed_C,'half_turn_complement':fixed_HC},
        'frozen_p10': {'occupied_cells':44,'primitive_directions':72,'distinct_words':len(actual),
                      'spectral_classes':len(restricted),'fiber_histogram':dict(sorted(rhist.items())),
                      'one_hole_spectral_classes':len(restricted_hole),
                      'one_hole_fiber_histogram':dict(sorted(rhist_hole.items())),
                      'crt_full_checks':len(actual)*3*110},
        'witness':{'a':'1/11','b':'3/5','relation':'B = complement(shift5(A))',
                   'equal_defect_vector':list(spectrum(a)), 'distinguishing_position':1},
        'sharp_extra_bits_general':2, 'sharp_extra_bits_frozen_restricted':1,
        'limits': 'Exact finite support classification; no native moving-Farey transition evaluated.'
    }

if __name__ == '__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2,sort_keys=True))
