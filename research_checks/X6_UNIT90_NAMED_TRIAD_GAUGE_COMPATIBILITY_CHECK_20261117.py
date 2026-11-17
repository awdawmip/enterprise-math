#!/usr/bin/env python3
"""Unit90: exact named-triad diagonal gauge compatibility audit.

Sources: frozen original named generators at
experiments/x6_triadic_rotation_v1_20260906/check_triadic_rotation.py
and research_checks/20261112_x6_star_triad_group_brc_convolution.py.
The check is standalone; not the original R063/Helly native benchmark.
"""
from collections import Counter
from itertools import combinations, product
import json

N = 6
IDENTITY = tuple(range(1, N + 1))
TRIADS = tuple(combinations(range(N), 3))
STAR = ((0, 2, 5), (0, 3, 4), (1, 2, 4), (1, 3, 5))

def compose(a, b):
    return tuple((1 if v > 0 else -1) * a[abs(v) - 1] for v in b)

def power(a, n):
    out = IDENTITY
    for _ in range(n):
        out = compose(a, out)
    return out

def q_all_negative(t):
    i, j, k = t
    a = list(IDENTITY)
    a[i], a[j], a[k] = -(j + 1), -(k + 1), -(i + 1)
    return tuple(a)

def g_one_negative(t):
    i, j, k = t
    a = list(IDENTITY)
    a[i], a[j], a[k] = j + 1, k + 1, -(i + 1)
    return tuple(a)

def diagonal(s):
    return tuple(v * (i + 1) for i, v in enumerate(s))

def conjugate(a, s):
    d = diagonal(s)
    return compose(compose(d, a), d)

def matches(t, s):
    i, j, k = t
    return s[i] == s[k] == -s[j]

def relative(z):
    h = min(z)
    return tuple(v - h for v in z)

def act(a, z):
    out = [0] * N
    for i, v in enumerate(z):
        im = a[i]
        out[abs(im) - 1] += v * (1 if im > 0 else -1)
    return tuple(out)

def main():
    signs = tuple(product((-1, 1), repeat=N))
    assert len(TRIADS) == 20 and len(signs) == 64
    for t in TRIADS:
        q, g = q_all_negative(t), g_one_negative(t)
        assert power(q, 6) == power(g, 6) == IDENTITY
        assert power(q, 3) == power(g, 3)
        assert sum(conjugate(g, s) == q for s in signs) == 16
        for s in signs:
            assert (conjugate(g, s) == q) == matches(t, s)

    full, star = Counter(), Counter()
    full_max, star_complete = 0, []
    for s in signs:
        count = sum(matches(t, s) for t in TRIADS)
        full[count] += 1
        full_max = max(full_max, count)
        star[sum(matches(t, s) for t in STAR)] += 1
        if all(matches(t, s) for t in STAR):
            star_complete.append(s)
    assert dict(sorted(full.items())) == {0: 12, 4: 12, 6: 24, 8: 16}
    assert dict(sorted(star.items())) == {0: 18, 1: 32, 2: 12, 4: 2}
    assert full_max == 8
    assert sorted(star_complete) == [
        (-1, -1, 1, 1, -1, -1),
        (1, 1, -1, -1, 1, 1),
    ]

    witness = ((0, 1, 2), (0, 2, 3))
    assert not any(all(matches(t, s) for t in witness) for s in signs)
    pair_hist = Counter()
    for x, y in combinations(TRIADS, 2):
        pair_hist[sum(matches(x, s) and matches(y, s) for s in signs)] += 1
    assert dict(sorted(pair_hist.items())) == {0: 30, 4: 100, 8: 60}

    # Conjugacy of all 85 STAR words of length 0..3.
    star_s = (1, 1, -1, -1, 1, 1)
    word_checks = 0
    for length in range(4):
        for word in product(STAR, repeat=length):
            gg, qq = IDENTITY, IDENTITY
            for t in word:
                gg = compose(g_one_negative(t), gg)
                qq = compose(q_all_negative(t), qq)
            assert conjugate(gg, star_s) == qq
            word_checks += 1
    assert word_checks == 85

    z = (0, 0, 1, 0, 0, 0)
    dz = act(diagonal(star_s), z)
    assert dz == (0, 0, -1, 0, 0, 0)
    assert relative(dz) != act(diagonal(star_s), relative(z))
    norm_checks = 0
    for z in product((-1, 0, 1), repeat=6):
        dz = act(diagonal(star_s), z)
        assert sum(v * v for v in dz) == sum(v * v for v in z)
        assert sum(abs(v) for v in dz) == sum(abs(v) for v in z)
        norm_checks += 1

    data = {
        "schema": "X6_UNIT90_NAMED_TRIAD_GAUGE_EXACT_V1",
        "date": "2026-11-17",
        "status": "AUTHOR_FINITE_EXACT_EXECUTED_UNREVIEWED_NOT_ADMITTED",
        "axis_labels": "SIX_NAMED_AXES_ZERO_BASED",
        "q_generator": "q(i)=-j, q(j)=-k, q(k)=-i; complement fixed",
        "g_generator": "g(i)=+j, g(j)=+k, g(k)=-i; complement fixed",
        "allowed_gauge": "GLOBAL_DIAGONAL_SIGN_ONLY_PRESERVING_NAMED_AXES",
        "one_triad_solution_count": 16,
        "all20_gauge_match_histogram": {str(k): v for k, v in sorted(full.items())},
        "all20_max_simultaneous_matches": full_max,
        "all20_single_global_gauge_exists": False,
        "two_triad_obstruction": [list(t) for t in witness],
        "pairwise_simultaneous_gauge_count_histogram":
            {str(k): v for k, v in sorted(pair_hist.items())},
        "star_triples": [list(t) for t in STAR],
        "star_gauge_match_histogram": {str(k): v for k, v in sorted(star.items())},
        "star_complete_gauges": [list(s) for s in sorted(star_complete)],
        "star_word_conjugacy_checks_lengths_0_to_3": word_checks,
        "norm_and_length_checks": norm_checks,
        "relative_observer_intertwines_with_sign_gauge": False,
        "native_R063_Helly_benchmarks_executed": False,
        "event_time_or_primitive_balance_admission": False,
    }
    print(json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")))

if __name__ == "__main__":
    main()
