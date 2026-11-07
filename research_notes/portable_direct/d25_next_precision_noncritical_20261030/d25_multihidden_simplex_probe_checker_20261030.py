#!/usr/bin/env python3
"""Exact integer verification of the auxiliary X6 multi-hidden simplex probe theorem.

All counts and operations are integers; no floating arithmetic, randomness, external data,
or native heartbeat execution. A configuration's full signature visits the entire joint
U_i translation period of every labeled hidden source.
"""
from __future__ import annotations

from collections import Counter
from itertools import product
from math import comb, factorial, prod
from pathlib import Path
import json

OUT = Path(__file__).with_name('d25_multihidden_simplex_probe_author_check_20261030.json')


def simplex(r: int, degree: int):
    return [a for a in product(range(degree + 1), repeat=r) if sum(a) <= degree]


def polynomial(h, terms, modulus):
    return sum(coefficient * prod(pow(h[i], exp) for i, exp in enumerate(exps))
               for coefficient, exps in terms) % modulus


def eval_shift(h, j, scales, terms, modulus):
    return polynomial(tuple(h[i] + scales[i] * j[i] for i in range(len(h))), terms, modulus)


def full_config(p, L, e, r, ss, D, terms, tag):
    assert 1 <= r <= 5 and L > e >= 1 and len(ss) == r and len(terms)
    assert all(0 <= s < L for s in ss)
    assert max(sum(exps) for _, exps in terms) == D
    M, n, N = p ** L, L - e, p ** (L - e)
    shifts = [p ** s for s in ss]
    grid = simplex(r, D - 1)
    assert len(grid) == comb(D - 1 + r, r)
    full_steps = list(product(*[range(p ** (L - s)) for s in ss]))
    short_to_full = {}
    full_to_short = {}
    fibers = Counter()
    calls = 0
    for h in product(range(M), repeat=r):
        short = tuple(eval_shift(h, j, shifts, terms, N) for j in grid)
        full = tuple(eval_shift(h, j, shifts, terms, N) for j in full_steps)
        calls += len(grid) + len(full_steps)
        assert short_to_full.setdefault(short, full) == full, (tag, 'unsafe short', h)
        assert full_to_short.setdefault(full, short) == short, (tag, 'unsafe full', h)
        fibers[short] += 1
    counts = Counter(fibers.values())
    assert sum(size * count for size, count in counts.items()) == M ** r
    result = {
        'tag': tag, 'p': p, 'L': L, 'e': e, 'n': n, 'r': r, 's': list(ss), 'total_degree': D,
        'terms': [{'coefficient': c, 'exponents': list(a)} for c, a in terms],
        'labeled_hidden_sources_per_fixed_observation': M ** r,
        'simplex_probe_count': len(grid), 'entire_joint_translation_period_size': len(full_steps),
        'distinct_future_fibers_per_fixed_observation': len(fibers),
        'fiber_size_histogram': {str(k): v for k, v in sorted(counts.items())},
        'exact_polynomial_evaluations': calls,
    }
    if all(s == 0 for s in ss):
        height_mod = list(product(range(N), repeat=r))
        periods = []
        period_evaluations = 0
        for v in height_mod:
            valid_period = True
            for x in height_mod:
                shifted = polynomial(tuple(xi + vi for xi, vi in zip(x, v)), terms, N)
                original = polynomial(x, terms, N)
                period_evaluations += 2
                if shifted != original:
                    valid_period = False
            if valid_period:
                periods.append(v)
        result['unit_translation_period_subgroup_size'] = len(periods)
        result['period_test_polynomial_evaluations'] = period_evaluations
        assert all(k == (p ** (e * r) * len(periods)) for k in counts)
        assert len(fibers) == (p ** (n * r)) // len(periods)
        assert len(periods) * len(fibers) == p ** (n * r)
    else:
        result['period_test_polynomial_evaluations'] = 0
    return result


def mod_rank(matrix, prime):
    a = [[x % prime for x in row] for row in matrix]
    pivot = 0
    for col in range(len(a[0])):
        target = next((i for i in range(pivot, len(a)) if a[i][col] != 0), None)
        if target is None:
            continue
        a[pivot], a[target] = a[target], a[pivot]
        inv = pow(a[pivot][col], -1, prime)
        a[pivot] = [(v * inv) % prime for v in a[pivot]]
        for i in range(len(a)):
            if i != pivot and a[i][col]:
                factor = a[i][col]
                a[i] = [(x - factor * y) % prime for x, y in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def sharp_witness(r, D, p):
    assert r >= 2 and p > D
    index_set = simplex(r, D - 1)
    N = len(index_set)
    matrix = [[prod(comb(j[i], alpha[i]) if j[i] >= alpha[i] else 0
                                       for i in range(r)) for alpha in index_set] for j in index_set]
    assert mod_rank(matrix, p) == N
    # Let f(X) = X_0 prod_{k=0}^{D-2}(X_1-k), source heights 0 and e_0.
    # Their difference at j is prod_{k=0}^{D-2}(j_1-k), zero at every
    # simplex node except the extremal node j=(0,D-1,0,...,0).
    corner = tuple([0, D - 1] + [0] * (r - 2))
    for j in index_set:
        diff = prod(j[1] - k for k in range(D - 1)) % p
        assert (diff != 0) == (j == corner)
    assert factorial(D - 1) % p != 0
    return {'r': r, 'D': D, 'p': p, 'simplex_size': N,
            'binomial_evaluation_matrix_rank_mod_p': N,
            'unique_nonzero_probe_index': list(corner),
            'first_source': [0] * r,
            'second_source': [1] + [0] * (r - 1),
            'separating_value_mod_p': factorial(D - 1) % p}


def main():
    configs = [
        (3, 2, 1, 2, (0, 0), 2, [(1, (2, 0)), (1, (0, 1))], 'quadratic_2hidden_p3'),
        (3, 2, 1, 2, (0, 0), 3, [(1, (1, 2)), (-1, (1, 1))], 'cubic_2hidden_p3'),
        (5, 2, 1, 2, (0, 0), 3, [(1, (1, 2)), (-1, (1, 1))], 'cubic_2hidden_p5'),
        (3, 3, 2, 2, (1, 0), 3, [(1, (1, 2)), (-1, (1, 1))], 'mixed_translation_p3'),
        (3, 2, 1, 3, (0, 1, 0), 2, [(1, (1, 1, 0)), (1, (0, 0, 2))], 'quadratic_3hidden'),
        (5, 3, 2, 1, (0,), 4, [(1, (4,)), (2, (2,)), (1, (0,))], 'quartic_1hidden'),
        (3, 3, 1, 1, (1,), 3, [(1, (3,)), (-1, (1,))], 'partial_shift_1hidden'),
    ]
    cases = [full_config(*c) for c in configs]
    sharp = [sharp_witness(r, D, p) for r in (2, 3, 4) for D in (2, 3, 4, 5)
             for p in ([5] if D < 5 else [7])]
    total_sources = sum(x['labeled_hidden_sources_per_fixed_observation'] for x in cases)
    total_calls = sum(x['exact_polynomial_evaluations'] + x['period_test_polynomial_evaluations'] for x in cases)
    out = {'status': 'PASS', 'model': 'AUXILIARY_SIX_COORDINATE_RING_NOT_NATIVE_X6',
           'arithmetic': 'EXACT_PYTHON_INTEGERS_MOD_PRIME_POWERS',
           'complete_configuration_count': len(cases),
           'complete_labeled_hidden_source_records': total_sources,
           'exact_polynomial_evaluations_including_period_tests': total_calls,
           'simplex_rank_and_essential_corner_witnesses': len(sharp),
           'cases': cases, 'witnesses': sharp,
           'limitations': 'Finite complete enumerations validate only listed configurations. General theorem requires integer Newton interpolation proof. Sharpness lower bound applies to fixed f-independent probe schedules; not adaptive f-dependent schedules.'}
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: out[k] for k in ('status','complete_configuration_count',
                   'complete_labeled_hidden_source_records',
                   'exact_polynomial_evaluations_including_period_tests',
                   'simplex_rank_and_essential_corner_witnesses')}, ensure_ascii=False))
    for x in cases:
        print(x['tag'], x['labeled_hidden_sources_per_fixed_observation'],
              x['distinct_future_fibers_per_fixed_observation'], x['fiber_size_histogram'])


if __name__ == '__main__':
    main()
