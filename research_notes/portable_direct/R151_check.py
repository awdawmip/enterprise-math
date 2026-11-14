#!/usr/bin/env python3
"""R151: exact CRT gauge collision versus pointwise Sturmian fiber witnesses.

Only Python integers, fractions and exact floor-event partitions; no floats.
"""
from fractions import Fraction as Q
from itertools import product
from math import gcd
import json


def units(n):
    return [r for r in range(n) if gcd(r, n) == 1] if n > 1 else [0]


def covariance(n, s, u, m, t, v):
    g = gcd(n, m)
    A = [2 * ((s * j + u) % g) - (g - 1) for j in range(g)]
    B = [2 * ((t * j + v) % g) - (g - 1) for j in range(g)]
    return tuple(Q(sum(A[j] * B[(j + h) % g] for j in range(g)),
                   4 * g * n * m) for h in range(g))


def support(word):
    m = len(word)
    s = [0]
    for x in word:
        s.append(s[-1] + x)
    alpha, beta = Q(0), Q(1)
    for i in range(m):
        for j in range(i + 1, m + 1):
            alpha = max(alpha, Q(s[j] - s[i] - 1, j - i))
            beta = min(beta, Q(s[j] - s[i] + 1, j - i))
    if not alpha < beta:
        return None
    a, b = alpha.numerator, alpha.denominator
    c, d = beta.numerator, beta.denominator
    U = min(b * (s[j] + 1) - j * a for j in range(m + 1))
    V = max(d * s[j] - j * c for j in range(m + 1))
    return (a, b, c, d, U, V)


def count_from_support(params, L):
    a, b, c, d, U, V = params
    return Q(L * c - V, d).__ceil__() - Q(L * a - U, b).__floor__() - 1


def direct_counts(L, m):
    # Complete rational partition of floor(n*theta), n=L,...,L+m.
    boundaries = {Q(0), Q(1)}
    for n in range(L, L + m + 1):
        boundaries.update(Q(a, n) for a in range(1, n))
    ordered = sorted(boundaries)
    result = {}
    for left, right in zip(ordered, ordered[1:]):
        theta = (left + right) / 2
        word = ''.join(str(((L + i + 1) * theta).__floor__() -
                           ((L + i) * theta).__floor__()) for i in range(m))
        phase = (L * theta).__floor__()
        result.setdefault(word, set()).add(phase)
    return {w: len(phases) for w, phases in result.items()}


def main():
    gauge_configs = gauge_shift_checks = 0
    for g in range(1, 9):
        for s in units(g):
            for t in units(g):
                for u in range(g):
                    for v in range(g):
                        base = covariance(g, s, u, g, t, v)
                        gauge_configs += 1
                        for r in range(g):
                            assert covariance(g, s, u + s * r, g, t, v + t * r) == base
                            gauge_shift_checks += 1

    pair = {'01001': support((0, 1, 0, 0, 1)),
            '10010': support((1, 0, 0, 1, 0))}
    assert pair == {'01001': (1, 4, 1, 2, 3, 0),
                    '10010': (1, 4, 1, 2, 4, 1)}
    wa, wb = pair.keys()

    def wave(word):
        a, b, c, d, U, V = pair[word]
        return covariance(b, a, -U, d, -c, V)

    assert wave(wa) == wave(wb) == (Q(-1, 32), Q(1, 32))

    # First collision, by increasing length: no claim of examining later lengths.
    first_length = None
    inspected = 0
    for length in range(1, 9):
        buckets = {}
        for word in product((0, 1), repeat=length):
            p = support(word)
            if p is None:
                continue
            inspected += 1
            a, b, c, d, U, V = p
            if gcd(b, d) == 1:
                continue
            gamma = covariance(b, a, -U, d, -c, V)
            key = (a, b, c, d, gamma)
            buckets.setdefault(key, []).append((word, p))
        collision = False
        for items in buckets.values():
            if len(items) < 2:
                continue
            if len({count_from_support(p, 1) for _, p in items}) > 1:
                collision = True
        if collision:
            first_length = length
            break
    assert first_length == 5

    exact_pair_checks = direct_pair_checks = 0
    for L in list(range(1, 81)) + [10**40 + 1, 10**100 + 1, 10**100 + 2]:
        ca, cb = count_from_support(pair[wa], L), count_from_support(pair[wb], L)
        assert ca - cb == (1 if L % 4 == 1 else 0)
        exact_pair_checks += 1
    for L in range(1, 49):
        observed = direct_counts(L, 5)
        for word in pair:
            assert observed.get(word, 0) == count_from_support(pair[word], L)
            direct_pair_checks += 1

    theta = Q(67, 200)
    actual = ''.join(str(((2 + i) * theta).__floor__() -
                         ((1 + i) * theta).__floor__()) for i in range(5))
    assert actual == '01001'

    outcome = {
        'marker': 'R151_CRT_GAUGE_POINTWISE_NONFACTOR_PASS',
        'scope': 'external S23 tied-phase scalar observer; no native X6 promotion',
        'frozen_scientific_pin': '43ec6098b1330ae86d0a7863be336c5d97f6ef34',
        'arithmetic': 'Exact Python integers and fractions; direct rational event partitions',
        'exhaustive_gauge_max_g': 8,
        'gauge_configurations': gauge_configs,
        'gauge_shift_comparisons': gauge_shift_checks,
        'first_same_slope_wave_fiber_collision_length_exhaustive_m_1_to_8': first_length,
        'sturmian_words_inspected_before_first_collision': inspected,
        'pair_closed_formula_cases': exact_pair_checks,
        'direct_event_partition_word_cases': direct_pair_checks,
        'pair_words': {
            w: {
                'support': {'alpha': f'{p[0]}/{p[1]}',
                            'beta': f'{p[2]}/{p[3]}', 'U': p[4], 'V': p[5]},
                'wave': [str(x) for x in wave(w)],
                'C_L1': count_from_support(p, 1),
                'C_L5': count_from_support(p, 5)
            } for w, p in pair.items()
        },
        'all_L_difference': 'C_01001(L+1)-C_10010(L+1)=1 iff L mod 4 = 1, else 0; L>=1',
        'explicit_theta_01001_at_L1': '67/200',
        'independent_review': 'NOT_REVIEWED'
    }
    with open('R151_verification.json', 'w', encoding='utf-8') as f:
        json.dump(outcome, f, ensure_ascii=False, indent=2)
    print(json.dumps(outcome, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
