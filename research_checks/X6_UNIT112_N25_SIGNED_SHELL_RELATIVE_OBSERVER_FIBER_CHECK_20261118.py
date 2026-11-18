#!/usr/bin/env python3
"""Unit112: frozen signed Z^3 norm-25 shell vs min-zero observer and N-BRC.

Pure exact-integer checker of a finite source-pinned mathematical submodel.
Not an execution of frozen R063/Helly C3/C4 benchmark.
No bare asserts, so all validations run with python -O and -OO.
"""
import json
from collections import Counter, defaultdict
from itertools import product
from math import factorial


def require(cond, label):
    if not cond:
        raise AssertionError(label)


def norm2(z):
    return sum(v * v for v in z)


def rho(z):
    h = min(z)
    return tuple(v - h for v in z)


def words(z):
    t = sum(abs(v) for v in z)
    n = factorial(t)
    for v in z:
        n //= factorial(abs(v))
    return n


def run():
    shell = tuple(z for z in product(range(-5, 6), repeat=3) if norm2(z) == 25)
    by_readout = defaultdict(list)
    for z in shell:
        by_readout[rho(z)].append(z)

    positive_section = tuple(z for z in product(range(6), repeat=3)
                             if min(z) == 0 and norm2(z) == 25)
    require(len(shell) == 30, 'SIGNED_SHELL_30')
    require(len(by_readout) == 30 and all(len(v) == 1 for v in by_readout.values()),
            'OBSERVER_RESTRICTED_INJECTION_30')
    require(len(positive_section) == 9, 'POSITIVE_MIN_ZERO_N25_9')
    require(set(positive_section) == {q for q in by_readout if norm2(q) == 25},
            'N25_INTERSECTION_EXACT')

    # Independent arithmetic obstruction to any nonzero diagonal shift within
    # this shell: 2*k*sum(z)+3*k*k=0 and sum(z) not divisible by three.
    possible_sums = sorted(set(sum(z) for z in shell))
    require(possible_sums == [-7, -5, -1, 1, 5, 7], 'SHELL_SUM_RESIDUES')
    require(all(sum(z) % 3 != 0 for z in shell), 'NO_DIAGONAL_SHELL_ALIAS')
    pairs_checked = 0
    for a in shell:
        for b in shell:
            pairs_checked += 1
            require((rho(a) != rho(b)) or a == b, 'PAIRWISE_FIBER_INJECTION')

    native_mass = sum(words(z) for z in shell)
    section_mass = sum(words(z) for z in positive_section)
    naive_observer_mass = sum(words(q) for q in by_readout)
    require((native_mass, section_mass, naive_observer_mass) == (846, 213, 3699),
            'DISTINGUISH_NATIVE_VS_OBSERVER_MASS')

    buckets = Counter(norm2(q) for q in by_readout)
    require(dict(sorted(buckets.items())) == {17: 6, 25: 9, 50: 3, 58: 6, 65: 6},
            'OBSERVER_GAUGE_DISTRIBUTION')
    neg = (-3, -4, 0)
    require(rho(neg) == (1, 0, 4), 'SINGLE_OBSERVER_EXAMPLE')
    require((norm2(neg), norm2(rho(neg)), words(neg), words(rho(neg))) ==
            (25, 17, 35, 5), 'SINGLE_PATH_COUNT_CONTRAST')

    return {
        'schema': 'X6_UNIT112_EXACT_SIGNED_SHELL_OBSERVER_CERTIFICATE_V1',
        'input': {'native_model': 'signed selected Z3 sub-torsor of X6',
                  'frozen_P000_V5': '59538f585d037d09ef687b28715c4bc1a3f9fe03',
                  'square_norm': 25, 'enumeration_cube': [-5, 5],
                  'observer': 'rho(z)=z-min(z)*(1,1,1)'},
        'native_shell_states': len(shell),
        'observer_distinct_states': len(by_readout),
        'observer_fiber_cardinalities': dict(sorted(Counter(map(len, by_readout.values())).items())),
        'shell_coordinate_sums': possible_sums,
        'pairwise_injectivity_comparisons': pairs_checked,
        'positive_minzero_shell_states': len(positive_section),
        'positive_minzero_path_mass': section_mass,
        'native_signed_shell_path_mass': native_mass,
        'naive_observer_image_path_mass': naive_observer_mass,
        'observer_image_norm_squared_histogram': dict(sorted(buckets.items())),
        'single_counterexample': {
            'native': list(neg), 'observer': list(rho(neg)),
            'native_squared_norm': norm2(neg),
            'observer_squared_norm': norm2(rho(neg)),
            'native_shortest_N_BRC': words(neg),
            'naive_observer_shortest_N_BRC': words(rho(neg))},
        'status': 'EXACT_FINITE_EXECUTED / AUTHOR_PROOF / UNREVIEWED / NOT_ADMITTED',
        'native_R063_C3_C4_benchmark_executed': False
    }


if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, sort_keys=True, separators=(',', ':')))
