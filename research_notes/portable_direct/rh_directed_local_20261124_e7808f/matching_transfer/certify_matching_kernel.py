#!/usr/bin/env python3
"""Certified all-order matching kernel and sharper actual-road point intervals.

The source bound is the existing direct thickness interpolation estimate.
The new radius uses a closed-form integral and a proved unimodal sum remainder.
Only two actual thickness source values (n=2,6) are evaluated for the sign test.
The actual road cache is never generated or read; old samples are postchecks.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial, prod
import argparse
import hashlib
import importlib.util
import json
import sys
import time

sys.dont_write_bytecode = True


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def power(m, x, k):
    out = m.ONE
    while k:
        if k & 1:
            out = m.mul(out, x)
        x = m.mul(x, x)
        k //= 2
    return out


def exp_negative_small(m, x):
    """Outward e^(-x), 0<=x<=1, using Taylor degree 100/101.

    The signed Taylor integral remainder establishes the even upper and odd
    lower partial sums.  Input interval dependence is retained throughout.
    """
    assert 0 <= x[0] <= x[1] <= m.S
    term = total = m.ONE
    even = total
    for j in range(1, 102):
        term = m.qmul(m.mul(term, x), 1, j)
        total = m.add(total, m.neg(term) if j % 2 else term)
        if j == 100:
            even = total
    return total[0], even[1]


def integral_kernel(m, y, k):
    """Integral_1^y (y/t-1) log(t)^k dt, outward rational interval."""
    logy = m.log_int(y)
    j = m.rat(y - 1)  # J_0(y) = integral_1^y 1 dt.
    lp = m.ONE
    for r in range(1, k + 1):
        lp = m.mul(lp, logy)
        j = m.sub(m.qmul(lp, y), m.qmul(j, r))
    return m.sub(m.qmul(m.mul(lp, logy), y, k + 1), j)


def maximum_bound(m, y, k):
    """Certified bound for the peak of (y/t-1) log(t)^k."""
    logy = m.log_int(y)
    high_order = power(m, logy, k)
    if logy[1] <= k * m.S:
        return high_order
    low_order = m.qmul(power(m, exp_negative_small(m, m.ONE), k),
                      y * k ** k)
    if k * m.S < logy[0]:
        return low_order
    return min(high_order[0], low_order[0]), max(high_order[1], low_order[1])


def kernel_checks(m, ymax=128, kmax=24):
    """Direct logarithmic sums verify the claimed finite implementation range."""
    checks = 0
    for k in range(1, kmax + 1):
        s0 = s1 = m.ZERO
        for y in range(2, ymax + 1):
            # The n=y term has coefficient zero, so insert before the query.
            lp = power(m, m.log_int(y), k)
            s0 = m.add(s0, lp)
            s1 = m.add(s1, m.qmul(lp, 1, y))
            direct = m.sub(m.qmul(s1, y), s0)
            integ = integral_kernel(m, y, k)
            peak = maximum_bound(m, y, k)
            assert m.sub(integ, peak)[0] <= direct[0]
            assert direct[1] <= m.add(integ, peak)[1]
            checks += 1
    return {'integer_y_range': [2, ymax], 'integer_k_range': [1, kmax],
            'sum_integral_enclosure_checks': checks,
            'input_is_logarithmic_envelope_not_actual_D': True}


def sign_examples(m, family):
    thickness = list(map(F, family['nodes']))
    weights = list(map(F, family['weights']))
    rows = []
    exponential_calls = 0
    for n, factors in [(2, [2]), (6, [2, 3])]:
        value = m.ZERO
        for a, w in zip(thickness, weights):
            r = m.ONE
            for p in factors:
                r = m.mul(r, m.sub(m.ONE,
                    exp_negative_small(m, m.qmul(m.log_int(p), a))))
                exponential_calls += 1
            value = m.add(value, m.qmul(r, w / a))
        reference = m.log_int(2) if n == 2 else m.ZERO
        difference = m.sub(value, reference)
        assert difference[1] < 0 if n == 2 else difference[0] > 0
        rows.append({'n': n, 'distinct_prime_factors': factors,
                     'D_minus_Lambda': m.record(difference)})
    return {'rows': rows, 'mixed_sign_certified': True,
            'thickness_terms_evaluated': 2 * len(thickness),
            'exponential_factor_calls': exponential_calls,
            'full_road_built': False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prior', type=Path, required=True)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('matching_kernel_certificate.json'))
    args = parser.parse_args()
    paths = {
        'harmonic': args.prior / 'dependencies/certify_fast_harmonic_energy.py',
        'oracle': args.prior / 'prefix_compute/certify_paired_prefix.py',
        'family': args.prior / 'prefix_compute/fixed_matched_family.json',
        'nodes': args.prior / 'prefix_compute/fixed_node_positions.json',
        'old_certificate': args.prior / 'prefix_compute/paired_prefix_certificate.json',
        'old_samples': args.prior / 'inputs/rh_partial_frontier_20261122/sparse_sample_observations.json',
    }
    m = load_module('harmonic_kernel', paths['harmonic'])
    old = load_module('paired_prefix_kernel', paths['oracle'])
    family = json.loads(paths['family'].read_text())
    geometry = json.loads(paths['nodes'].read_text())
    nodes = sorted(geometry['nodes'])
    k = len(family['nodes']) + 1
    coefficient = prod(map(F, family['nodes'])) / factorial(k)
    reference, old_errors, _, _, oracle_cost = old.point_oracle(m, nodes, family)
    started = time.perf_counter()
    errors, lower, upper = {}, {}, {}
    new_only = {}
    for y in nodes:
        integ = integral_kernel(m, y, k)
        peak = maximum_bound(m, y, k)
        radius = m.qmul(m.add(integ, peak), coefficient)[1]
        new_only[y] = radius
        radius = min(radius, old_errors[y][1])
        assert radius >= 0
        errors[y] = radius, radius
        lower[y] = reference[y][0] - radius, reference[y][0] - radius
        upper[y] = reference[y][1] + radius, reference[y][1] + radius
    radius_seconds = time.perf_counter() - started
    # Historical actual q values enter only after the new intervals exist.
    sample_data = json.loads(paths['old_samples'].read_text())
    actual = {row['n']: m.decode(row['value']) for row in sample_data['samples']}
    assert all(lower[n][0] <= actual[n][0] <= actual[n][1] <= upper[n][1]
               for n in nodes)
    assert all(new_only[n] < old_errors[n][0] for n in nodes)
    curvature = 1 + F(1, 2 * nodes[0] ** 2) + F(1, 10 ** 6)
    energy_started = time.perf_counter()
    upper_energy, _ = m.evaluate_partition(nodes, upper, curvature)
    lower_energy, _ = m.evaluate_partition(nodes, lower, F(-12))
    radius_energy = old.linear_error_energy(m, nodes, errors)
    energy_seconds = time.perf_counter() - energy_started
    previous = json.loads(paths['old_certificate'].read_text())
    assert lower_energy[0] > m.decode(previous['new_lower_positive_energy'])[1]
    assert upper_energy[1] < m.decode(previous['new_upper_positive_energy'])[0]
    result = {
        'status': 'PASS', 'schema': 'RH_ALL_ORDER_MATCHING_KERNEL_V1',
        'scope': 'Actual fixed matched-road enclosure via the proved full-prefix matching error; author checks, not independent Review.',
        'window': [nodes[0], nodes[-1]], 'node_count': len(nodes),
        'matching_exponent': k, 'matching_coefficient': str(coefficient),
        'arithmetic': {'decimal_digits': m.DIGITS, 'method': 'outward integer intervals'},
        'input_files': [{'role': name, 'path': str(path),
                         'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
                        for name, path in paths.items()],
        'old_actual_samples_used_only_after_new_point_generation': True,
        'all_historical_sample_intervals_contained': True,
        'all_new_radii_strictly_smaller_than_previous_radii': True,
        'radius_at_B': m.record(errors[nodes[-1]]),
        'previous_radius_at_B': m.record(old_errors[nodes[-1]]),
        'new_radius_over_previous_radius_at_B_exact': str(F(errors[nodes[-1]][0], old_errors[nodes[-1]][0])),
        'lower_positive_energy': m.record(lower_energy),
        'upper_positive_energy': m.record(upper_energy),
        'interpolated_radius_square_energy': m.record(radius_energy),
        'source_curvature_constants_unchanged': {'upper': str(curvature), 'lower': '-12'},
        'oracle_cost': oracle_cost,
        'new_radius_seconds': radius_seconds,
        'energy_aggregation_seconds': energy_seconds,
        'kernel_checks': kernel_checks(m),
        'actual_source_sign_examples': sign_examples(m, family),
        'samples_denominator_power_of_10': m.DIGITS,
        'samples': [{'n': n, 'reference': list(map(str, reference[n])),
                     'new_error_radius': str(errors[n][0]),
                     'lower': str(lower[n][0]), 'upper': str(upper[n][0])}
                    for n in nodes],
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({key: result[key] for key in [
        'status', 'node_count', 'radius_at_B', 'previous_radius_at_B',
        'lower_positive_energy', 'upper_positive_energy',
        'interpolated_radius_square_energy', 'new_radius_seconds',
        'energy_aggregation_seconds', 'kernel_checks', 'actual_source_sign_examples']},
        ensure_ascii=False))


if __name__ == '__main__':
    main()
