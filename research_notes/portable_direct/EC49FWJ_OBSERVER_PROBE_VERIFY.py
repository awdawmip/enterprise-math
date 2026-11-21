#!/usr/bin/env python3
"""EC49FWJ, exact membership-probe reconstruction on the ten-cycle.
Frozen certificate: BRC16943; inherited four-slope decoder EC49FWE/FWI.
Pure Python 3 standard library, all arithmetic exact.
"""
import json
from collections import Counter, defaultdict
from itertools import combinations
from math import gcd

N, FULL = 10, (1 << 10) - 1
SLOPES = {(0, 0): {3}, (0, 1): {0, 3, 4, 'inf'},
          (1, 0): {2, 3, 4, 'inf'}, (1, 1): {2, 3}}

def positions(m):
    return {t for t in range(N) if (m >> t) & 1}

def reflected(m, c):
    return sum(1 << ((c-t) % N) for t in positions(m))

def shifted5(m):
    return sum(1 << ((t+5) % N) for t in positions(m))

def defects(m):
    return tuple((m ^ reflected(m, c)).bit_count() for c in range(N))

def orbit(m):
    h = shifted5(m)
    return {m, h, m ^ FULL, h ^ FULL}

def p10(h, n):
    h, n = h % N, n % N
    if h % 5 == n % 5 == 0:
        return False
    s = 'inf' if h % 5 == 0 else (n * pow(h % 5, -1, 5)) % 5
    return s in SLOPES[(h % 2, n % 2)]

def source_word(a, b):
    h0, n0 = next((h, n) for h in range(N) for n in range(N)
                  if ((b-a)*h-a*n+1) % N == 0)
    return sum(1 << t for t in range(N)
               if p10(h0+a*t, n0+(b-a)*t))

def make_fibers(words, with_weight):
    d = defaultdict(list)
    for m in sorted(words):
        key = (defects(m), m.bit_count()) if with_weight else defects(m)
        d[key].append(m)
    return d

def separates(probes, fs):
    return all(len({tuple((m >> t) & 1 for t in probes) for m in group})
               == len(group) for group in fs.values())

def minimal_probes(fs):
    for count in range(N+1):
        good = [list(Q) for Q in combinations(range(N), count)
                if separates(Q, fs)]
        if good:
            return count, good
    raise AssertionError('unreachable')

def difference_patterns(fs):
    d = Counter()
    for group in fs.values():
        for a, b in combinations(group, 2):
            d[tuple(sorted(positions(a ^ b)))] += 1
    return [{'support':list(k), 'count':v} for k, v in sorted(d.items())]

def main():
    all_words = set(range(1024))
    frozen = {source_word(a,b) for a in range(N) for b in range(N)
              if gcd(gcd(a,b),N) == 1}
    assert len(frozen) == 50
    universal = {}; restricted = {}
    for with_weight in (False, True):
        fs = make_fibers(all_words, with_weight)
        assert all(set(group) == orbit(group[0]) if not with_weight
                   else set(group).issubset(orbit(group[0])) for group in fs.values())
        k, sets = minimal_probes(fs)
        expected = [list(q) for q in combinations(range(N),5)
                    if all((i in q) or (i+5 in q) for i in range(5))]
        assert k == 5 and sets == expected and len(sets) == 32
        assert max(map(len,fs.values())) == 4
        universal['with_weight' if with_weight else 'defect_only'] = {
            'fiber_count':len(fs), 'maximum_fiber_size':4,
            'minimum_fixed_probes':k, 'optimal_fixed_sets':len(sets),
            'first_optimal_set':sets[0], 'adaptive_worst_case_probes':2}

        rs = make_fibers(frozen, with_weight)
        k2, sets2 = minimal_probes(rs)
        assert k2 == 3 and len(sets2) == 16
        assert [1,2,3] in sets2
        expected2 = [list(q) for q in combinations(range(N),3)
                     if len(set(q) & {1,4,6,9}) == 1
                     and len(set(q) & {2,7}) == 1
                     and len(set(q) & {3,8}) == 1]
        assert sets2 == expected2
        patterns = difference_patterns(rs)
        assert {tuple(p['support']) for p in patterns} == {
            (1,4,6,9), (3,8), (1,2,6,7), (2,7),
            (3,4,8,9), tuple(range(N)), (2,4,7,9)}
        assert max(map(len,rs.values())) == 2
        assert separates([1,2,3],rs)
        restricted['with_weight' if with_weight else 'defect_only'] = {
            'fiber_count':len(rs), 'maximum_fiber_size':2,
            'minimum_fixed_probes':k2, 'optimal_fixed_sets':len(sets2),
            'first_optimal_set':sets2[0], 'adaptive_worst_case_probes':1,
            'pairwise_difference_patterns':patterns}
    # An explicit sharp witness even if cardinality is supplied.
    q = {0, 5}
    m = (1 << 0) | (1 << 1) | (1 << 6) | (1 << 2) | (1 << 7)
    n = shifted5(m)
    assert m != n and m.bit_count() == n.bit_count() == 5
    assert defects(m) == defects(n)
    assert positions(m ^ n) == q
    # With single-hole V = Z11\{0}, the lifted sites 1,12,23 read U(1),U(2),U(3).
    assert [(t%10,t%11) for t in (1,12,23)] == [(1,1),(2,1),(3,1)]
    result = {
        'status':'ALL PASS', 'scientific_pin':'BRC16943',
        'domain':'all 1024 ten-bit supports and 50 distinct frozen P10 supports',
        'universal':universal, 'frozen_p10':restricted,
        'sharp_witness':{'S':sorted(positions(m)), 'H(S)':sorted(positions(n)),
                         'same_weight':5,'difference':sorted(q)},
        'single_hole_z0_probe_sites':[1,12,23],
        'limits':'Finite support reconstruction; no native moving-Farey map evaluated.'}
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))

if __name__ == '__main__':
    main()
