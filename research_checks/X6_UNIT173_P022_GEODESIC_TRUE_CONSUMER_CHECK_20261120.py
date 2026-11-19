#!/usr/bin/env python3
"""Independent finite shell census for frozen P022 A_p/SC consumers.
Does not execute the repository's production module or the original R063 benchmark.
Only certifies the explicitly enumerated radii and dimensions.
"""
from functools import lru_cache
from itertools import product
from math import comb, factorial
import json


def stirling(n, k):
    if k < 0 or k > n:
        return 0
    row = [0] * (k + 1)
    row[0] = 1
    for size in range(1, n + 1):
        nxt = [0] * (k + 1)
        for blocks in range(1, min(k, size) + 1):
            nxt[blocks] = blocks * row[blocks] + row[blocks - 1]
        row = nxt
    return row[k]


def a_formula(p, r):
    if r == 0:
        return 1
    n = p + 1
    return sum(comb(n, a) * comb(n-a, b) * factorial(a) * stirling(r, a)
               * factorial(b) * stirling(r, b)
               for a in range(1, min(n-1, r)+1)
               for b in range(1, min(n-a, r)+1))


def sc_formula(d, r):
    if r == 0:
        return 1
    return sum(comb(d, j) * 2**j * factorial(j) * stirling(r, j)
               for j in range(1, min(d, r)+1))


@lru_cache(None)
def a_recursive(v):
    if not any(v):
        return 1
    total = 0
    for i, x in enumerate(v):
        if x <= 0:
            continue
        for j, y in enumerate(v):
            if y >= 0:
                continue
            w = list(v)
            w[i] -= 1
            w[j] += 1
            total += a_recursive(tuple(w))
    return total


@lru_cache(None)
def sc_recursive(v):
    if not any(v):
        return 1
    total = 0
    for i, x in enumerate(v):
        if x:
            w = list(v)
            w[i] -= 1 if x > 0 else -1
            total += sc_recursive(tuple(w))
    return total


def a_shell(p, r):
    if r == 0:
        return [(0,) * (p+1)]
    shell = []
    for w in product(range(-r, r+1), repeat=p):
        z = -sum(w)
        v = w + (z,)
        if -r <= z <= r and sum(x for x in v if x > 0) == r:
            shell.append(v)
    return shell


def sc_shell(d, r):
    if r == 0:
        return [(0,) * d]
    return [v for v in product(range(-r, r+1), repeat=d)
            if sum(abs(x) for x in v) == r]


def main():
    rows = []
    for p in (1, 2, 3):
        for r in range(5):
            v = a_shell(p, r)
            direct = sum(a_recursive(w) for w in v)
            closed = a_formula(p, r)
            if direct != closed:
                raise RuntimeError(f'A_{p} radius {r}: {direct} != {closed}')
            rows.append(dict(geometry=f'A_{p}', radius=r,
                             endpoints=len(v), recursive_mass=direct,
                             closed_mass=closed))
    for d in (1, 2, 3, 6):
        for r in range(5):
            v = sc_shell(d, r)
            direct = sum(sc_recursive(w) for w in v)
            closed = sc_formula(d, r)
            if direct != closed:
                raise RuntimeError(f'SC_{d} radius {r}: {direct} != {closed}')
            rows.append(dict(geometry=f'SC_{d}', radius=r,
                             endpoints=len(v), recursive_mass=direct,
                             closed_mass=closed))
    a3 = [a_formula(3, r) for r in range(6)]
    x6 = [sc_formula(6, r) for r in range(6)]
    if not (a3[:3] == [1, 12, 84] and x6[:3] == [1, 12, 132]):
        raise RuntimeError('P022 root/native-X6 degree-12 separation failed')
    result = {
        'schema':'X6_UNIT173_P022_TYPED_CONSUMER_FINITE_CERT_V1',
        'scope':'independent shell enumeration vs frozen producer formulas; no direct run of frozen module',
        'frozen_source':'fd2bcff10ca6e147348b6c1236027fc0d2877df3',
        'producer':'src/enterprise_math/p022_geodesic_multiplicity.py',
        'consumer':'tests/test_p022_geodesic_multiplicity.py',
        'cases':len(rows),
        'direct_endpoints':sum(row['endpoints'] for row in rows),
        'disagreements':0,
        'a3_shell_masses_r0_to5':a3,
        'native_sc6_shell_masses_r0_to5':x6,
        'first_nontrivial_divergence_radius':2,
        'rows':rows,
        'assessment':'P022_A3_DERIVED_ROOT_GRAPH_NOT_NATIVE_X6; no alleged LP019 signed native BRC subtraction in this examined producer or tests'
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
