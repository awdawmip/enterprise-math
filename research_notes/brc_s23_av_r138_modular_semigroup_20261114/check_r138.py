#!/usr/bin/env python3
"""R138: exact modular Farey-gap and two-generator coefficient semigroup tests.
Pure exact Python (Fraction/integer). Scientific scope: auxiliary S23 floor words.
"""
from fractions import Fraction
from math import gcd, lcm


def fl(x):
    return x.numerator // x.denominator


def fraction_word(theta, K, m):
    L = K - 1
    return tuple(fl((L + i + 1) * theta) - fl((L + i) * theta) for i in range(m))


def strict_word(theta, K, m):
    return tuple(int(((K + i) * theta) % 1 < theta % 1) for i in range(m))


def cells(m):
    fs = sorted({Fraction(a, b) for b in range(1, m + 1) for a in range(b + 1)})
    result = []
    for left, right in zip(fs, fs[1:]):
        a, b = left.numerator, left.denominator
        c, d = right.numerator, right.denominator
        assert b * c - a * d == 1
        alpha = (left + right) / 2
        cuts = [(Fraction(0), 0, 0), (Fraction(1), 1, 0)]
        for j in range(1, m + 1):
            p = fl(j * alpha) + 1
            cuts.append((p - j * alpha, p, j))
        cuts.sort()
        for (lv, p, j), (uv, q, k) in zip(cuts, cuts[1:]):
            assert lv < uv
            rho = (lv + uv) / 2
            word = tuple(fl(rho + (i + 1) * alpha) - fl(rho + i * alpha) for i in range(m))
            D = j * b * c - k * a * d + (q - p) * b * d
            result.append((a, b, c, d, p, j, q, k, D, word))
    return result


def modular_feasible(rec, K):
    a, b, c, d, p, j, q, k, D, _ = rec
    L = K - 1
    h = ((L + k) * a) % b
    return L + D > d * (b - h)


def fraction_feasible(rec, K):
    a, b, c, d, p, j, q, k, D, _ = rec
    L = K - 1
    lower = (L + k) * Fraction(a, b) - q
    upper = (L + j) * Fraction(c, d) - p
    return fl(lower) + 1 < upper


def witness(rec, K):
    a, b, c, d, p, j, q, k, D, w = rec
    L = K - 1
    lower = (L + k) * Fraction(a, b) - q
    N = fl(lower) + 1
    ell = max(Fraction(a, b), Fraction(N + p, L + j))
    high = min(Fraction(c, d), Fraction(N + q, L + k))
    assert ell < high
    return (ell + high) / 2


def words(records, K):
    return {rec[-1] for rec in records if modular_feasible(rec, K)}


def last_bad_L_gap(rec):
    a, b, c, d, p, j, q, k, D, _ = rec
    max_bad = None
    for r in range(b):
        h = ((r + k) * a) % b
        H = d * (b - h) - D
        tmin = int(r == 0)  # L >= 1 and L = r + b*t.
        tmax = (H - r) // b
        if tmax >= tmin:
            z = r + b * tmax
            max_bad = z if max_bad is None or z > max_bad else max_bad
    return max_bad


def gap_eventual_K(rec):
    z = last_bad_L_gap(rec)
    return 2 if z is None else z + 2


def run():
    pairs = shifts = modular_checks = witness_checks = gap_thresholds = 0
    all_gap_cases = bound_boundary_checks = 0
    main_thresholds = {}
    for m in range(1, 21):
        R = cells(m)
        full = {r[-1] for r in R}
        for rec in R:
            assert rec[8] >= min(rec[1], rec[3])
            all_gap_cases += 1
        if m >= 2:
            E = (m - 1) ** 2 + 2
            assert max(gap_eventual_K(rec) for rec in R) == E
            assert all(modular_feasible(rec, E) for rec in R)
            assert any(not modular_feasible(rec, E - 1) for rec in R)
            bound_boundary_checks += 1
        F = 1 + sum((m + 1 - q) * sum(gcd(k, q) == 1 for k in range(1, q + 1)) for q in range(1, m + 1))
        assert len(full) == F, ('Sturmian full F', m, len(full), F)
        if m <= 9:
            for K in [2, 3, 4, 7, 11, 17, 29, 10**60 + 137]:
                for rec in R:
                    yes = modular_feasible(rec, K)
                    assert yes == fraction_feasible(rec, K), (m, K, rec)
                    modular_checks += 1
                    if yes and (K == 11 or K == 10**60 + 137):
                        t = witness(rec, K)
                        assert fraction_word(t, K, m) == rec[-1]
                        assert strict_word(t, K, m) == rec[-1]
                        witness_checks += 1
        if m <= 10:
            Q = lcm(*range(1, max(2, m)))
            for K in range(2, 31):
                before = words(R, K)
                assert before <= words(R, K + Q), ('period', m, K, Q)
                pairs += 1
                for rec in R:
                    if modular_feasible(rec, K):
                        assert modular_feasible(rec, K + rec[1])
                        assert modular_feasible(rec, K + rec[3])
                        shifts += 2
            for rec in R:
                E = gap_eventual_K(rec)
                assert modular_feasible(rec, E)
                for K in range(E, E + 4):
                    assert modular_feasible(rec, K)
                if E > 2:
                    assert not modular_feasible(rec, E - 1)
                gap_thresholds += 1
        U = (m * (m - 1) + 1) if m >= 2 else 2
        arr = [len(words(R, K)) for K in range(2, U + 1)]
        assert arr[-1] == F, (m, U, arr[-1], F)
        first = next(i + 2 for i, num in enumerate(arr) if num == F)
        eventual = 2 + max((i for i, num in enumerate(arr) if num < F), default=-1) + 1
        assert all(x == F for x in arr[eventual - 2:])
        main_thresholds[m] = {'F': F, 'first': first, 'eventual': eventual, 'U': U}
    expected = {5: (7,7), 7: (11,16), 10: (25,33), 12: (41,51), 15: (67,92), 18: (99,129), 20: (113,163)}
    for m, e in expected.items():
        assert (main_thresholds[m]['first'], main_thresholds[m]['eventual']) == e, (m, main_thresholds[m], e)
    print('R138_MODULAR_SEMIGROUP_PASS')
    print({'exact_modular_fraction_crosschecks': modular_checks,
           'exact_witnesses': witness_checks,
           'period_K_pairs': pairs,
           'local_b_d_inclusion_checks': shifts,
           'gap_threshold_records': gap_thresholds,
           'all_gap_D_inequality_tests': all_gap_cases,
           'sharp_global_gap_bound_tests': bound_boundary_checks})
    print('THRESHOLDS', main_thresholds)


if __name__ == '__main__':
    run()
