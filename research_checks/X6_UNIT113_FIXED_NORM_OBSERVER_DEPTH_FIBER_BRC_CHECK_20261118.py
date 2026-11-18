#!/usr/bin/env python3
"""Unit113: exact depth-root fiber theorem under fixed native norm in signed Z3.

This is a portable finite check (0 <= N <= 100), not an original R063
benchmark, and its universal algebraic theorem is proved separately.
"""
import json
from collections import defaultdict
from itertools import product
from math import factorial, isqrt


def require(ok, name):
    if not ok:
        raise AssertionError(name)


def G(z):
    return sum(a * a for a in z)


def rho(z):
    h = min(z)
    return tuple(a-h for a in z)


def B(z):
    n = sum(abs(a) for a in z)
    v = factorial(n)
    for a in z:
        v //= factorial(abs(a))
    return v


def depths_for(q, N):
    s = sum(q)
    d = s*s - 3 * (G(q) - N)
    if d < 0:
        return ()
    t = isqrt(d)
    if t*t != d:
        return ()
    hs = {(-s + eps*t)//3 for eps in (-1, 1)
          if (-s + eps*t) % 3 == 0}
    return tuple(sorted(hs))


def run():
    limit = 100
    shells = defaultdict(list)
    enumerated_cube = 0
    for z in product(range(-10, 11), repeat=3):
        enumerated_cube += 1
        n = G(z)
        if n <= limit:
            shells[n].append(z)
    per_N = {}
    aliasing_norms = []
    nonconstant_B_norms = []
    max_fiber = 0
    checked_fibers = 0
    for N in range(limit + 1):
        fs = defaultdict(list)
        for z in shells[N]:
            fs[rho(z)].append(z)
        alias_count = 0
        B_bad_count = 0
        for q, vectors in fs.items():
            checked_fibers += 1
            expected = depths_for(q, N)
            actual = tuple(sorted(min(z) for z in vectors))
            require(expected == actual, 'COMPLETE_EXACT_QUADRATIC_DEPTH_ROOTS')
            require(len(vectors) <= 2, 'MAX_TWO_ROOTS')
            max_fiber = max(max_fiber, len(vectors))
            if len(vectors) == 2:
                alias_count += 1
                if len(set(B(z) for z in vectors)) > 1:
                    B_bad_count += 1
        if N % 3 == 1:
            require(alias_count == 0, 'MOD3_ONE_INJECTIVITY')
        if alias_count:
            aliasing_norms.append(N)
        if B_bad_count:
            nonconstant_B_norms.append(N)
        per_N[str(N)] = {
            'signed_cells': len(shells[N]),
            'observer_images': len(fs),
            'double_depth_fibers': alias_count,
            'B_inconsistent_fibers': B_bad_count,
        }

    q = (0, 3, 3)
    x, y = (-3, 0, 0), (-1, 2, 2)
    require(G(x) == G(y) == 9, 'N9_PAIR_NATIVE_NORM')
    require(rho(x) == rho(y) == q, 'N9_PAIR_SAME_RELATIVE_OBSERVER')
    require(depths_for(q, 9) == (-3, -1), 'N9_DEPTH_ROOTS')
    require(B(x) == 1 and B(y) == 30, 'N9_BRC_NON_DESCENT')
    require(nonconstant_B_norms[0] == 9, 'N9_FIRST_OBSERVED_B_NON_DESCENT')

    return {
        'schema': 'X6_UNIT113_FIXED_SQUARED_NORM_DEPTH_FIBER_CERTIFICATE_V1',
        'frozen_P000_V5': '59538f585d037d09ef687b28715c4bc1a3f9fe03',
        'selected_native_model': 'signed Z3 affine subtorsor',
        'checked_norm_range': [0, limit],
        'native_coordinate_cube': [-10, 10],
        'lattice_points_enumerated': enumerated_cube,
        'fibers_checked': checked_fibers,
        'max_fiber_size': max_fiber,
        'N_with_two_depths': aliasing_norms,
        'N_with_B_nonconstant_on_fiber': nonconstant_B_norms,
        'N9_witness': {
            'native_cells': [list(x), list(y)],
            'observer': list(q),
            'allowed_depths': list(depths_for(q, 9)),
            'same_native_squared_norm': 9,
            'native_shortest_BRC_counts': [B(x), B(y)]},
        'N25_reuse': per_N['25'],
        'N9_summary': per_N['9'],
        'scope': 'FINITE_EXHAUSTIVE_N_0_THROUGH_100_PLUS_UNIVERSAL_ALGEBRAIC_PROOF_IN_REPORT',
        'status': 'AUTHOR-PROVED / EXACT-FINITE-EXECUTED / UNREVIEWED / NOT_ADMITTED',
        'original_native_R063_benchmark_executed': False
    }


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, separators=(',', ':')))
