#!/usr/bin/env python3
"""X6 Unit119: exact square-radius signed pair-chart/full-shell rho-alias census.
Independent integer checker for immutable P000 V5 spatial component rules;
not the original R063 C3/C4 benchmark or native program integration.
"""
from itertools import combinations, product
from math import factorial, isqrt
import json


def require(condition, detail):
    if not condition:
        raise RuntimeError(detail)


def roots(r):
    ans = []
    for a in range(r + 1):
        square = r * r - a * a
        b = isqrt(square)
        if b * b == square:
            ans.append((a, b))
    return ans


def rho(z):
    level = min(z)
    return tuple(v - level for v in z)


def g(z):
    return sum(v * v for v in z)


def brc(z):
    n = sum(abs(v) for v in z)
    denominator = 1
    for v in z:
        denominator *= factorial(abs(v))
    return factorial(n) // denominator


def run():
    total_root_count = 0
    total_labelled = 0
    labelled_aliases = 0
    native_aliases = 0
    divisible_radii = 0
    sample_rows = {}
    for r in range(1, 129):
        rr = roots(r)
        total_root_count += len(rr)
        pair_endpoints = set()
        paired_endpoints = set()
        labelled_count = 0
        for i, j in combinations(range(6), 2):
            for a, b in rr:
                for si, sj in product((-1, 1), repeat=2):
                    z = [0] * 6
                    z[i], z[j] = si * a, sj * b
                    z = tuple(z)
                    require(g(z) == r*r, 'invalid positive root lift')
                    pair_endpoints.add(z)
                    labelled_count += 1
                    s = sum(z)
                    if s != 0 and s % 3 == 0:
                        depth = -s // 3
                        y = tuple(v + depth for v in z)
                        require(y != z and g(y) == g(z) == r*r, 'norm alias invalid')
                        require(rho(y) == rho(z), 'observer alias invalid')
                        require(sum(v != 0 for v in y) >= 4, 'alias must leave pair chart')
                        require(brc(z) > 0 and brc(y) > 0, 'BRC must be natural positive')
                        paired_endpoints.add(z)
                        labelled_aliases += 1
        require(labelled_count == 60 * len(rr), 'labelled chart count')
        require(len(paired_endpoints) == (len(pair_endpoints) if r % 3 == 0 else 0),
                f'3-divisibility dichotomy r={r}')
        # Pair-chart rho injectivity independently checked at each radius.
        require(len({rho(z) for z in pair_endpoints}) == len(pair_endpoints),
                f'pair-chart observer injectivity r={r}')
        if r % 3 == 0:
            divisible_radii += 1
        native_aliases += len(paired_endpoints)
        total_labelled += labelled_count
        if r in (1, 3, 5, 6, 9, 50, 128):
            sample_rows[str(r)] = {
                'ordered_positive_roots': len(rr),
                'native_pair_endpoints': len(pair_endpoints),
                'native_pair_endpoints_with_full_shell_alias': len(paired_endpoints),
                'labelled_pair_chart_cases': labelled_count,
            }
    witness_z = (-3, 0, 0, 0, 0, 0)
    witness_y = (-2, 1, 1, 1, 1, 1)
    require(g(witness_z) == g(witness_y) == 9, 'first square-norm witness norm')
    require(rho(witness_z) == rho(witness_y) == (0, 3, 3, 3, 3, 3),
            'first square-norm witness observer')
    require(brc(witness_z) == 1 and brc(witness_y) == 2520,
            'first square-norm witness BRC')
    require(total_root_count == 398 and total_labelled == 23880,
            'total original R063 ordered chart counts')
    require(labelled_aliases == 7080 and native_aliases == 2544 and divisible_radii == 42,
            'complete finite census crosscheck')
    return {
        'schema': 'X6_UNIT119_SIGNED_R063_RHO_SQUARE_RADIUS_CERTIFICATE_V1',
        'classification': 'AUTHOR_EXACT_INTEGER_ENUMERATION_NOT_ORIGINAL_NATIVE_BENCHMARK',
        'frozen_P000_V5': '59538f585d037d09ef687b28715c4bc1a3f9fe03',
        'historical_source': 'fd2bcff10ca6e147348b6c1236027fc0d2877df3',
        'radii': [1, 128],
        'original_ordered_root_count_total': total_root_count,
        'labelled_chart_cases': total_labelled,
        'labelled_chart_alias_cases': labelled_aliases,
        'unique_native_pair_alias_cases': native_aliases,
        'radii_divisible_by_three': divisible_radii,
        'exact_equivalence': 'pair-endpoint has distinct same-norm same-rho full-native alias iff radius divisible by 3',
        'first_square_radius': 3,
        'first_witness': {
            'x': witness_z,
            'y': witness_y,
            'G': 9,
            'rho': rho(witness_z),
            'N_BRC_x': brc(witness_z),
            'N_BRC_y': brc(witness_y),
        },
        'sample_radii': sample_rows,
    }


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, ensure_ascii=False, separators=(',', ':')))
