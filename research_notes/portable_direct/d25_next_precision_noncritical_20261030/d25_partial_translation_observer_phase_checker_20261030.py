#!/usr/bin/env python3
"""Exact author-side finite-ring checks for the partial-height-translation observer theorem.

This tests an explicitly declared auxiliary candidate, not native heartbeat dynamics.
All integer operations are exact; no external dependencies or random sampling.
"""
from collections import Counter, defaultdict
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def vp(x, p):
    if x == 0:
        return 10**9
    x = abs(x)
    r = 0
    while x % p == 0:
        r += 1
        x //= p
    return r


def predicted_contact(h, hh, p, s, n):
    if h == hh:
        return n
    k = vp(h - hh, p)
    r = min(vp(h, p), vp(hh, p), s)
    v = p * k if k == r else k + (p - 1) * r + 1
    return min(n, v)


def spectrum(signature_groups):
    return dict(sorted(Counter(map(len, signature_groups.values())).items()))


def group_by(items, keys):
    groups = defaultdict(list)
    for item, key in zip(items, keys):
        groups[key].append(item)
    return groups


def main():
    cases = []
    for p, cap in ((3, 6), (5, 4), (7, 3), (11, 2)):
        for L in range(2, cap + 1):
            for e in range(1, L):
                cases.append((p, L, e))
    cases += [(3, 7, 1), (3, 7, 2), (5, 5, 1)]
    counters = Counter()
    parameter_results = []
    illustrative_spectra = {}
    for p, L, e in cases:
        ring = p**L
        n = L - e
        mod = p**n
        heights = list(range(ring))
        base_groups = group_by(heights, (pow(h, p, mod) for h in heights))
        for s in range(L):
            step = p**s
            translations = range(0, ring, step)
            keys = [(pow(h, p, mod), pow(h + step, p, mod)) for h in heights]
            pairs = group_by(heights, keys)
            strict = len(pairs) > len(base_groups)
            predicted_strict = n >= p * s + 3
            assert strict == predicted_strict, (p, L, e, s, 'phase')
            assert sum(len(group) for group in pairs.values()) == ring
            counters['parameter_slices'] += 1
            counters['labeled_height_rows'] += ring
            counters['two_probe_power_evaluations'] += 2 * ring
            # Compare both equivalence relations using all valid translation shifts
            # on the smaller rings, not merely matching their class counts.
            if ring <= 729 or (p, L, e, s) in ((3, 7, 1, 0), (3, 7, 1, 1), (3, 7, 1, 2)):
                full = [tuple(pow(h + c, p, mod) for c in translations) for h in heights]
                seen_forward, seen_reverse = {}, {}
                for key, whole in zip(keys, full):
                    if key in seen_forward:
                        assert seen_forward[key] == whole, (p, L, e, s, 'not sufficient')
                    else:
                        seen_forward[key] = whole
                    if whole in seen_reverse:
                        assert seen_reverse[whole] == key, (p, L, e, s, 'not minimal')
                    else:
                        seen_reverse[whole] = key
                counters['all_translation_rows'] += ring
                counters['all_translation_power_evaluations'] += ring * len(translations)
                counters['fully_verified_slices'] += 1
            # Check every pair and the actual min over every translation on tiny rings.
            if ring <= 125:
                for h in heights:
                    for hh in range(h + 1, ring):
                        target = min(vp(pow(h + c, p) - pow(hh + c, p), p) for c in translations)
                        actual = min(n, target)
                        expected = predicted_contact(h, hh, p, s, n)
                        assert actual == expected, (p, L, e, s, h, hh, actual, expected)
                        assert ((keys[h] == keys[hh]) == (expected == n))
                        counters['exhaustive_pair_contact_checks'] += 1
                        counters['pair_translation_evaluations'] += len(translations)
            # Directly instantiate full six-coordinate sources and the two operation probes.
            for h in heights:
                for t in range(3):
                    q = tuple((h * (j + 1) + t * (j + 3)) % ring for j in range(5))
                    z = tuple((q[j] + h) % ring for j in range(5)) + (h,)
                    def Q(v):
                        return tuple((v[j] - v[5]) % ring for j in range(5))
                    def T(v):
                        v = list(v)
                        v[0] = (v[0] + p**e * pow(v[5], p, ring)) % ring
                        return tuple(v)
                    def U(v):
                        return tuple((x + step) % ring for x in v)
                    assert Q(z) == q
                    out1 = Q(T(z))[0]
                    out2 = Q(T(U(z)))[0]
                    assert (out1 - q[0]) % ring == (p**e * keys[h][0]) % ring
                    assert (out2 - q[0]) % ring == (p**e * keys[h][1]) % ring
                    counters['actual_six_coordinate_source_probes'] += 1
                    counters['actual_operator_calls'] += 3
            if (p, L, e) == (3, 7, 1):
                illustrative_spectra[f's={s}'] = {'classes': len(pairs), 'fiber_size_to_count': spectrum(pairs)}
            parameter_results.append({'p': p, 'L': L, 'e': e, 's': s,
                'n': n, 'height_sources': ring, 'classes': len(pairs),
                'strict_vs_T_only': strict, 'fiber_spectrum': spectrum(pairs)})
    assert illustrative_spectra['s=0']['fiber_size_to_count'] == {9: 243}
    assert illustrative_spectra['s=1']['fiber_size_to_count'] == {9: 162, 81: 9}
    assert illustrative_spectra['s=2']['fiber_size_to_count'] == {9: 162, 81: 6, 243: 1}
    output = {
        'schema': 'D25_PARTIAL_TRANSLATION_X6_AUTHOR_EXACT_CHECK_V1',
        'status': 'PASS',
        'model': 'Auxiliary R=(Z/p^L Z)^6, q_i=z_i-z_6, h=z_6, T=z+p^e h^p e_1, U_s=z+p^s*(1,...,1)',
        'coverage': dict(counters),
        'witness_p3_L7_e1': illustrative_spectra,
        'results': parameter_results,
        'not_native': True,
        'not_independent_review': True,
        'not_source_admitted': True,
    }
    path = HERE / 'd25_partial_translation_observer_phase_author_check_20261030.json'
    path.write_text(json.dumps(output, sort_keys=True, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'PASS','coverage': dict(counters), 'witness': illustrative_spectra}, sort_keys=True))


if __name__ == '__main__':
    main()
