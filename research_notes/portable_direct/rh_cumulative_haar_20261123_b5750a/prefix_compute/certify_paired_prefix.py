#!/usr/bin/env python3
"""Controlled-error point oracle and exact divisor-prefix grouping.

The actual road is retained via the already proved thickness matching bound.
No full-road cache, D array, c array, thickness exponential, or actual q prefix
is read or generated. Historical q samples are used only after the new oracle
has run, as a finite comparison. All signed arithmetic is outward integer.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial, isqrt, prod
import argparse
import hashlib
import importlib.util
import json
import sys
import time

sys.dont_write_bytecode = True


def load_module(path):
    spec = importlib.util.spec_from_file_location('pinned_harmonic_evaluator', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start::p] = b'\x00' * ((n - start) // p + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


def floor_blocks(n):
    left = 1
    while left <= n:
        k = n // left
        right = n // k
        yield left, right, k
        left = right + 1


def exact_group_checks(limit=96):
    # A signed rational coefficient population, unit retained.
    c = [F(0)] + [F((17 * d * d + 11 * d) % 23 - 11, d % 5 + 1)
                   for d in range(1, limit + 1)]
    r = [F(0)] * (limit + 1)
    for d in range(1, limit + 1):
        for n in range(d, limit + 1, d):
            r[n] += c[d]
    h = [F(0)]
    c0, c1 = [F(0)], [F(0)]
    for n in range(1, limit + 1):
        h.append(h[-1] + F(1, n))
        c0.append(c0[-1] + c[n])
        c1.append(c1[-1] + c[n] / n)
    affine = F(7, 5)
    maximum_blocks = 0
    for y in range(1, limit + 1):
        source = affine * y + sum((F(y, n) - 1) * r[n]
                                  for n in range(1, y + 1))
        coefficient = affine * y + sum(c[d] * (F(y, d) * h[y // d] - y // d)
                                       for d in range(1, y + 1))
        blocks = list(floor_blocks(y))
        grouped = affine * y + sum(y * h[k] * (c1[v] - c1[u - 1])
                                   - k * (c0[v] - c0[u - 1])
                                   for u, v, k in blocks)
        assert source == coefficient == grouped
        s = isqrt(y)
        assert len(blocks) == s + y // (s + 1)
        maximum_blocks = max(maximum_blocks, len(blocks))
        # All coefficients below y really affect this scalar observer.
        assert all(F(y, d) * h[y // d] - y // d > 0 for d in range(1, y))
        assert F(y, y) * h[1] - 1 == 0
    return {'all_integer_y_through': limit, 'exact_rational_equalities': limit,
            'maximum_floor_blocks': maximum_blocks,
            'coefficient_below_y_has_strictly_positive_kernel': True,
            'unit_coefficient_retained': True}


def interval_power(m, x, k):
    answer = m.ONE
    while k:
        if k & 1:
            answer = m.mul(answer, x)
        x = m.mul(x, x)
        k //= 2
    return answer


def point_oracle(m, nodes, family):
    started = time.perf_counter()
    aa, bb = nodes[0], nodes[-1]
    thickness = list(map(F, family['nodes']))
    weights = list(map(F, family['weights']))
    count = len(thickness)
    assert count == len(weights) and count > 0
    assert len(set(thickness)) == count and all(a > 0 for a in thickness)
    assert sum(weights) == 1
    assert all(sum(w * a ** j for a, w in zip(thickness, weights)) == 0
               for j in range(1, count))
    k = count + 1
    coefficient = prod(thickness) / factorial(k)
    assert m.log_int(bb)[1] <= k * m.S
    eta_bb = m.qmul(interval_power(m, m.log_int(bb), k), coefficient)
    assert eta_bb[1] <= m.rat(F(1, 10**6))[0]
    assert m.add(m.log_int(bb), m.rat(F(1, 10**6)))[1] <= 12*m.S
    gamma_record = family['gamma']
    if 'integer_bounds' in gamma_record:
        gamma = m.decode(gamma_record)
    else:
        gamma = (m.rat(F(gamma_record['lower']))[0],
                 m.rat(F(gamma_record['upper']))[1])
    primes = primes_upto(bb)
    events = []
    for p in primes:
        power = p
        while power <= bb:
            events.append((power, p))
            power *= p
    events.sort()
    prime_logs = {p: m.log_int(p) for p in primes}
    s0, s1 = m.ZERO, m.ZERO
    index = 0
    reference, errors, lowers, uppers = {}, {}, {}, {}
    for y in nodes:
        while index < len(events) and events[index][0] <= y:
            n, p = events[index]
            logp = prime_logs[p]
            s0 = m.add(s0, logp)
            s1 = m.add(s1, m.qmul(logp, 1, n))
            index += 1
        logy = m.log_int(y)
        qstar = m.add(m.sub(m.qmul(s1, y), s0),
                     m.qmul(m.sub(m.add(m.ONE, gamma), logy), y))
        eta_y = m.qmul(interval_power(m, logy, k), coefficient)
        radius = m.qmul(eta_y, F((y - 1) * (y - 2), 2 * y))[1]
        reference[y] = qstar
        errors[y] = (radius, radius)
        # Exact rational endpoint bounds: sign searches need no wide
        # uncertain actual-q parameter once these deterministic bounds are set.
        lowers[y] = (qstar[0] - radius, qstar[0] - radius)
        uppers[y] = (qstar[1] + radius, qstar[1] + radius)
    elapsed = time.perf_counter() - started
    return reference, errors, lowers, uppers, {
        'seconds': elapsed, 'sieve_limit': bb, 'prime_count': len(primes),
        'prime_power_event_count': len(events), 'point_count': len(nodes),
        'thickness_count': count, 'matching_exponent': k,
        'matching_coefficient_exact': str(coefficient),
        'log_B_less_than_matching_exponent_certified': True,
        'eta_B': m.record(eta_bb),
        'curvature_constants_verified': {
            'upper': str(1 + F(1, 2*aa*aa) + F(1, 10**6)),
            'lower': '-12',
            'eta_B_at_most_one_millionth': True,
            'log_B_plus_one_millionth_at_most_12': True,
        },
        'global_matching_error_square_norm_upper': m.record(
            m.qmul(m.square(eta_bb), bb-aa+1, 4)),
        'thickness_exponential_calls': 0, 'thickness_product_updates': 0,
        'full_D_or_q_array_built': False, 'full_source_cache_read': False,
        'distinct_logarithm_arguments': m.log_int.cache_info().misses,
        'point_error_radius_at_B': m.record(errors[bb]),
        'uniform_old_error_radius_at_B': m.record(m.qmul(
            interval_power(m, m.log_int(bb), k + 1), coefficient * bb)),
    }


def linear_error_energy(m, nodes, errors):
    # Positive linear interpolation of the exact rational radius table.
    result = m.qmul(m.square(errors[nodes[0]]), 1, nodes[0] ** 2)
    for left, right in zip(nodes, nodes[1:]):
        a = m.qmul(m.sub(errors[right], errors[left]), 1, right - left)
        b = m.sub(errors[left], m.qmul(a, left))
        result = m.add(result, m.segment_energy(left + 1, right, a, b, F(0)))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--harmonic-module', type=Path, required=True)
    parser.add_argument('--family', type=Path, required=True)
    parser.add_argument('--nodes', type=Path, required=True)
    parser.add_argument('--comparison-samples', type=Path)
    args = parser.parse_args()
    m = load_module(args.harmonic_module)
    family = json.loads(args.family.read_text())
    geometry = json.loads(args.nodes.read_text())
    nodes = sorted(geometry['nodes'])
    assert len(nodes) == len(set(nodes))
    assert [nodes[0], nodes[-1]] == geometry['window']
    # No file containing actual q samples is read before point_oracle.
    reference, errors, lower, upper, cost = point_oracle(m, nodes, family)
    comparison, observed = None, None
    if args.comparison_samples:
        observations = json.loads(args.comparison_samples.read_text())
        old = {row['n']: m.decode(row['value']) for row in observations['samples']}
        assert all(lower[n][0] <= old[n][0] <= old[n][1] <= upper[n][1] for n in nodes)
        comparison = True
        error_max_n = max(nodes, key=lambda n: max(abs(old[n][0] - reference[n][1]),
                                                   abs(old[n][1] - reference[n][0])))
        observed = {'n': error_max_n,
                    'q_minus_reference': m.record(m.sub(old[error_max_n], reference[error_max_n]))}
    start = time.perf_counter()
    upper_constant = 1 + F(1, 2 * nodes[0] ** 2) + F(1, 10 ** 6)
    upper_energy, _ = m.evaluate_partition(nodes, upper, upper_constant)
    lower_energy, _ = m.evaluate_partition(nodes, lower, F(-12))
    error_energy = linear_error_energy(m, nodes, errors)
    energy_seconds = time.perf_counter() - start
    prefix_endpoints, harmonic_arguments = {0}, set()
    all_block_count = 0
    for n in nodes:
        for u, v, k in floor_blocks(n):
            all_block_count += 1
            prefix_endpoints.update((u - 1, v))
            harmonic_arguments.add(k)
    certificate = {
        'status': 'PASS', 'schema': 'RH_PAIRED_PREFIX_ORACLE_V1',
        'scope': 'Controlled-error observation of the actual matched road; no unbounded positive-energy claim.',
        'input_files': [{'path': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
                        for p in [args.harmonic_module, args.family, args.nodes]],
        'optional_comparison_file': ({'path': str(args.comparison_samples),
            'sha256': hashlib.sha256(args.comparison_samples.read_bytes()).hexdigest()}
            if args.comparison_samples else None),
        'arithmetic': {'decimal_digits': m.DIGITS, 'method': 'outward integer intervals; rational matching-error upper radius'},
        'window': [nodes[0], nodes[-1]], 'cost': cost,
        'all_historical_actual_sample_intervals_contained': comparison,
        'historical_samples_used_only_for_checking': True,
        'largest_observed_sample_difference': observed,
        'new_upper_positive_energy': m.record(upper_energy),
        'new_lower_positive_energy': m.record(lower_energy),
        'interpolated_radius_square_energy': m.record(error_energy),
        'energy_aggregation_seconds': energy_seconds,
        'exact_floor_grouping_checks': exact_group_checks(),
        'floor_group_count_at_B': len(list(floor_blocks(nodes[-1]))),
        'floor_group_count_for_all_requested_points': all_block_count,
        'floor_group_distinct_prefix_endpoints': len(prefix_endpoints),
        'floor_group_distinct_harmonic_arguments': len(harmonic_arguments),
        'query_cost_qualification': 'floor grouping presupposes C0/C1 prefix access. Dense preparation remains O(B), and a known D table supports O(B+K) batch point evaluation.',
        'samples_denominator_power_of_10': m.DIGITS,
        'samples': [{'n': n, 'reference_integer_bounds': list(map(str, reference[n])),
                     'matching_radius_integer_upper': str(errors[n][1]),
                     'certified_lower_endpoint': str(lower[n][0]),
                     'certified_upper_endpoint': str(upper[n][1])} for n in nodes],
    }
    output = Path(__file__).with_name('paired_prefix_certificate.json')
    output.write_text(json.dumps(certificate, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: certificate[k] for k in ['status', 'window', 'cost',
          'largest_observed_sample_difference', 'new_upper_positive_energy',
          'new_lower_positive_energy', 'interpolated_radius_square_energy',
          'energy_aggregation_seconds', 'exact_floor_grouping_checks',
          'floor_group_count_at_B', 'floor_group_count_for_all_requested_points',
          'floor_group_distinct_prefix_endpoints',
          'floor_group_distinct_harmonic_arguments']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
