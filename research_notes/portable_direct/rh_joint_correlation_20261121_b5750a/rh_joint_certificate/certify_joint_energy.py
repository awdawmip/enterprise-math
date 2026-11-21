#!/usr/bin/env python3
"""Strict finite joint q / small-divisor-corrected q certificate.

This is a new full-road calculation on the previously fixed rational family.
All certified quantities use integer intervals with denominator 10**60.
Old certificates and the elementary oracle are inputs; none are modified.
Run from any directory: python rh_joint_certificate/certify_joint_energy.py
"""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import hashlib
import json
import pickle
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'rh_correlation_rational'))
from certify_matched_nodes import (  # noqa: E402
    SCALE, DIGITS, ZERO, ONE, Elementary, ceildiv, rat, add, sub, neg,
    scale, mul, divide, floor_root, linear_sieve, render,
)

A, B, H = 1024, 32768, 256
OUT = Path(__file__).resolve().parent
INPUTS = [ROOT / 'rh_correlation_rational/rational_window_certificate.json',
          ROOT / 'rh_correlation_phase/phase_homogenization_checks.json',
          ROOT / 'rh_correlation_rational/certify_matched_nodes.py']


def interval_from_record(record):
    if 'integer_bounds' in record:
        assert record['denominator_power_of_10'] == DIGITS
        return tuple(map(int, record['integer_bounds']))
    return rat(F(record['lower']))[0], rat(F(record['upper']))[1]


def record(x, places=30):
    return {**render(x, places), 'integer_bounds': [str(x[0]), str(x[1])],
            'denominator_power_of_10': DIGITS}


def isum(xs):
    lo = hi = 0
    for x in xs:
        lo += x[0]
        hi += x[1]
    return lo, hi


def positive(x):
    return max(0, x[0]), max(0, x[1])


def square(x):
    lo = 0 if x[0] <= 0 <= x[1] else min(x[0] ** 2, x[1] ** 2)
    hi = max(x[0] ** 2, x[1] ** 2)
    return lo // SCALE, ceildiv(hi, SCALE)


def sqrt_interval(x):
    assert x[0] >= 0
    lo, hi = isqrt(x[0] * SCALE), isqrt(x[1] * SCALE)
    if hi * hi < x[1] * SCALE:
        hi += 1
    return lo, hi


def intersects(x, y):
    return max(x[0], y[0]) <= min(x[1], y[1])


def energy(values, first=A, last=B, mode='full'):
    if mode == 'positive':
        return isum(scale(square(positive(values[n])), F(1, n * n))
                    for n in range(first, last + 1))
    return isum(scale(square(values[n]), F(1, n * n))
                for n in range(first, last + 1))


def cross(x, y, first=A, last=B):
    return isum(scale(mul(x[n], y[n]), F(1, n * n))
                for n in range(first, last + 1))


def green_apply(rhs, left, right, left_value=ZERO, right_value=ZERO):
    """O(right-left) exact-interval Dirichlet Green application."""
    length = right - left
    pre = [ZERO] * (length + 1)
    suf = [ZERO] * (length + 1)
    for i in range(1, length):
        pre[i] = add(pre[i - 1], scale(rhs[left + i], i))
    for i in range(length - 1, 0, -1):
        suf[i] = add(suf[i + 1], scale(rhs[left + i], length - i))
    result = [ZERO] * (right + 1)
    result[left], result[right] = left_value, right_value
    for i in range(1, length):
        affine = add(scale(left_value, F(length - i, length)),
                     scale(right_value, F(i, length)))
        potential = scale(add(scale(pre[i], length - i), scale(suf[i + 1], i)),
                          F(1, length))
        result[left + i] = add(affine, potential)
    return result


def partition(beta):
    cuts = [A]
    while cuts[-1] < B:
        left = cuts[-1]
        step = floor_root(left ** beta.numerator, beta.denominator)
        cuts.append(min(B, left + step))
    return cuts


def coarse_certificate(values, cuts):
    """Retain every signed coarse charge, endpoints, and local potentials."""
    slopes = [scale(sub(values[r], values[l]), F(1, r - l))
              for l, r in zip(cuts, cuts[1:])]
    charges = [sub(slopes[j - 1], slopes[j]) for j in range(1, len(cuts) - 1)]
    base = [ZERO] * (B + 1)
    local = [ZERO] * (B + 1)
    for l, r in zip(cuts, cuts[1:]):
        for n in range(l, r + 1):
            base[n] = add(scale(values[l], F(r - n, r - l)),
                          scale(values[r], F(n - l, r - l)))
            # At coarse nodes the true local potential is exactly zero.
            local[n] = ZERO if n in (l, r) else sub(values[n], base[n])
    positive_rhs = [ZERO] * (B + 1)
    signed_rhs = [ZERO] * (B + 1)
    for n, charge in zip(cuts[1:-1], charges):
        positive_rhs[n], signed_rhs[n] = positive(charge), charge
    coarse_positive = green_apply(positive_rhs, A, B)
    coarse_signed = green_apply(signed_rhs, A, B, values[A], values[B])
    assert all(intersects(base[n], coarse_signed[n]) for n in range(A, B + 1))
    affine = [ZERO] * (B + 1)
    for n in range(A, B + 1):
        affine[n] = add(scale(values[A], F(B - n, B - A)),
                        scale(values[B], F(n - A, B - A)))
    end_energy = energy(affine, A + 1, B - 1, 'positive')
    base_energy = energy(base, A + 1, B - 1, 'positive')
    remainder_energy = energy(local, A + 1, B - 1, 'positive')
    positive_coarse_energy = energy(coarse_positive, A + 1, B - 1)
    signed_budget = add(sqrt_interval(base_energy), sqrt_interval(remainder_energy))
    positive_budget = add(add(sqrt_interval(end_energy), sqrt_interval(positive_coarse_energy)),
                          sqrt_interval(remainder_energy))
    return {
        'nodes': cuts,
        'node_values': [record(values[n]) for n in cuts],
        'signed_coarse_charges': [record(x) for x in charges],
        'charge_definition': 'm_j=(q[x_j]-q[x_{j-1}])/(x_j-x_{j-1})-(q[x_{j+1}]-q[x_j])/(x_{j+1}-x_j)',
        'interior_signed_charge_sum': record(isum(charges)),
        'interior_positive_charge_sum': record(isum(positive(x) for x in charges)),
        'interior_negative_charge_magnitude_sum': record(isum(positive(neg(x)) for x in charges)),
        'endpoint_positive_energy_interior': record(end_energy),
        'signed_base_positive_energy_interior': record(base_energy),
        'local_positive_energy_interior': record(remainder_energy),
        'green_of_positive_charges_energy_interior': record(positive_coarse_energy),
        'signed_plus_local_norm_budget': record(signed_budget),
        'endpoint_plus_positive_charges_plus_local_norm_budget': record(positive_budget),
        'squared_signed_plus_local_norm_budget': record(square(signed_budget)),
        'squared_endpoint_plus_positive_charges_plus_local_norm_budget': record(square(positive_budget)),
        'coarse_green_identity_enclosed_at_every_integer': True,
    }


def main():
    started = time.perf_counter()
    original = json.loads(INPUTS[0].read_text())
    previous_phase = json.loads(INPUTS[1].read_text())
    old_phase = previous_phase['actual_matched_family']['actual_matched_main_window']
    nodes = list(map(F, original['node_certificate']['nodes']))
    weights = list(map(F, original['node_certificate']['weights']))
    gamma = interval_from_record(original['gamma'])
    elementary = Elementary()
    spf, mu = linear_sieve(B)
    primes = [p for p in range(2, B + 1) if spf[p] == p]
    D = [ZERO] * (B + 1)
    road_mults = 0
    for index, (a, weight) in enumerate(zip(nodes, weights)):
        factors = {p: sub(ONE, elementary.exp_negative(scale(elementary.log_integer(p), a)))
                   for p in primes}
        roads = [ONE] * (B + 1)
        for n in range(2, B + 1):
            p = spf[n]
            k = n // p
            if k % p == 0:
                roads[n] = roads[k]
            else:
                roads[n] = mul(roads[k], factors[p])
                road_mults += 1
            D[n] = add(D[n], scale(roads[n], weight / a))
        print(json.dumps({'stage': 'full_prime_factor_roads', 'thickness': index + 1,
                          'of': len(nodes), 'seconds': round(time.perf_counter() - started, 3)}), flush=True)
    q = [ZERO] * (B + 1)
    sum_D_over_n = sum_D = ZERO
    one_plus_gamma = add(ONE, gamma)
    for n in range(1, B + 1):
        if n >= 2:
            sum_D_over_n = add(sum_D_over_n, scale(D[n], F(1, n)))
            sum_D = add(sum_D, D[n])
        q[n] = add(sub(scale(sum_D_over_n, n), sum_D),
                   scale(sub(one_plus_gamma, elementary.log_integer(n)), n))
    endpoint_checks = []
    for old in original['endpoints']:
        n = old['N']
        assert intersects(q[n], interval_from_record(old['F']))
        endpoint_checks.append({'n': n, 'full_road_q': record(q[n]), 'previous_endpoint_enclosure_overlaps': True})
    kappa = [ZERO] * (B + 1)
    kappa[1] = scale(elementary.log_integer(2), 2)
    for n in range(2, B + 1):
        kappa[n] = scale(add(sub(scale(elementary.log_integer(n + 1), n + 1),
                                scale(elementary.log_integer(n), 2 * n)),
                            scale(elementary.log_integer(n - 1), n - 1)), n)
    f = [ZERO] + [scale(sub(kappa[n], D[n]), F(1, n)) for n in range(1, B + 1)]
    c = [ZERO] * (H + 1)
    for d in range(1, H + 1):
        if mu[d]:
            for n in range(d, H + 1, d):
                c[n] = add(c[n], scale(sub(D[n // d], kappa[n // d]), mu[d]))
    assert intersects(c[1], neg(scale(elementary.log_integer(2), 2)))
    sigma = isum(scale(c[d], F(1, d)) for d in range(1, H + 1))
    assert intersects(sigma, interval_from_record(old_phase['sigma_H']))
    mean = isum(scale(c[d], F(1, d)) for d in range(2, H + 1))
    correction_numerator = [neg(mean)] * (B + 1)
    divisor_additions = 0
    for d in range(2, H + 1):
        for n in range(d, B + 1, d):
            correction_numerator[n] = add(correction_numerator[n], c[d])
            divisor_additions += 1
    correction_source = [ZERO] + [scale(correction_numerator[n], F(1, n)) for n in range(1, B + 1)]
    P = green_apply(correction_source, A, B, interval_from_record(old_phase['P_H_at_A']),
                    interval_from_record(old_phase['P_H_at_B']))
    Q = [ZERO] * (B + 1)
    for n in range(A, B + 1):
        Q[n] = add(q[n], P[n])
    corrected_source = [add(x, y) for x, y in zip(f, correction_source)]
    for n in range(A + 1, B):
        assert intersects(sub(scale(q[n], 2), add(q[n - 1], q[n + 1])), f[n])
        assert intersects(sub(scale(P[n], 2), add(P[n - 1], P[n + 1])), correction_source[n])
        assert intersects(sub(scale(Q[n], 2), add(Q[n - 1], Q[n + 1])), corrected_source[n])
    harmonic = [ZERO]
    for n in range(1, B + 1):
        harmonic.append(add(harmonic[-1], rat(F(1, n))))
    harmonic_checks = []
    for n in (A, A + 1, 1296, 4096, 10000, (A + B) // 2, 28561, B - 1, B):
        def Pd(d):
            return add(scale(sub(sub(harmonic[n], harmonic[n // d]), elementary.log_integer(d)), F(n, d)),
                       rat(F(d - 1 - 2 * (n % d), 2 * d)))
        direct = isum(mul(c[d], Pd(d)) for d in range(2, H + 1))
        assert intersects(P[n], direct)
        harmonic_checks.append({'n': n, 'direct_harmonic': record(direct), 'green_reconstructed': record(P[n]),
                                'enclosures_overlap': True})
    cache = {'A': A, 'B': B, 'H': H, 'SCALE': SCALE, 'DIGITS': DIGITS,
             'D': D, 'q': q, 'P': P, 'Q': Q, 'f': f, 'correction_source': correction_source,
             'corrected_source': corrected_source, 'c': c, 'kappa': kappa,
             'validity': 'D,q,f,kappa at 1..B; P,Q only at A..B; c at 1..H',
             'nodes': nodes, 'weights': weights}
    with (OUT / '_scratch_arrays.pkl').open('wb') as handle:
        pickle.dump(cache, handle, protocol=5)
    print(json.dumps({'stage': 'shared_arrays_ready', 'path': str(OUT / '_scratch_arrays.pkl'),
                      'seconds': round(time.perf_counter() - started, 3)}), flush=True)
    metrics = {}
    for label, values in [('q', q), ('P256', P), ('Q', Q)]:
        metrics[label] = {
            'full_square_energy': record(energy(values)),
            'positive_square_energy': record(energy(values, mode='positive')),
            'positive_square_energy_interior': record(energy(values, A + 1, B - 1, 'positive')),
            'full_square_energy_interior': record(energy(values, A + 1, B - 1)),
            'at_A': record(values[A]), 'at_B': record(values[B]),
            'strictly_positive_integer_count': sum(values[n][0] > 0 for n in range(A, B + 1)),
            'strictly_negative_integer_count': sum(values[n][1] < 0 for n in range(A, B + 1)),
            'unresolved_sign_integer_count': sum(values[n][0] <= 0 <= values[n][1] for n in range(A, B + 1)),
            'max_interval_width': record((0, max(values[n][1] - values[n][0] for n in range(A, B + 1)))),
        }
    qE, PE, QE, qP = energy(q), energy(P), energy(Q), cross(q, P)
    assert intersects(QE, add(add(qE, scale(qP, 2)), PE))
    full_joint = {
        'cross_q_P': record(qP),
        'twice_cross_q_P': record(scale(qP, 2)),
        'full_square_identity_residual': record(sub(QE, add(add(qE, scale(qP, 2)), PE))),
        'normalized_full_cross_correlation': record(divide(qP, sqrt_interval(mul(qE, PE)))),
        'Q_positive_to_q_positive_energy_ratio': record(divide(energy(Q, mode='positive'), energy(q, mode='positive'))),
        'previous_generic_infinite_correction_bound_to_actual_finite_P_energy': record(divide(interval_from_record(old_phase['infinite_tail_upper_enclosure']), PE)),
        'q_positive_to_Q_negative_count': sum(q[n][0] > 0 and Q[n][1] < 0 for n in range(A, B + 1)),
        'q_negative_to_Q_positive_count': sum(q[n][1] < 0 and Q[n][0] > 0 for n in range(A, B + 1)),
        'identity': 'sum Q_n^2/n^2 = sum q_n^2/n^2 + 2 sum q_n P_n/n^2 + sum P_n^2/n^2',
    }
    partitions = []
    for beta in (F(1, 2), F(3, 4), F(4, 5)):
        cuts = partition(beta)
        item = {'beta': str(beta), 'rule': 'next=min(B,L+floor(L**beta)); exact integer root',
                'block_count': len(cuts) - 1,
                'q': coarse_certificate(q, cuts), 'Q': coarse_certificate(Q, cuts)}
        partitions.append(item)
        print(json.dumps({'stage': 'coarse_partition_done', 'beta': str(beta),
                          'blocks': len(cuts) - 1, 'seconds': round(time.perf_counter() - started, 3)}), flush=True)
    result = {
        'status': 'AUTHOR_STRICT_FINITE_JOINT_ENERGY_CERTIFICATE_PASSED',
        'scope': 'Fixed rational thickness family and finite integer window only; no RH or all-scale claim.',
        'window': {'A': A, 'B': B, 'H': H, 'theta': '1/2', 'weight': '1/n^2',
                   'whole_energy_includes_both_endpoints': True,
                   'interior_energy_excludes_both_endpoints': True},
        'arithmetic': {'representation': 'integer intervals divided by 10**60',
                       'outward_rounding': True, 'energy_calculation_uses_no_floating_point': True,
                       'gamma': record(gamma), 'c1': record(c[1]), 'sigma_H': record(sigma)},
        'inputs': [{'path': str(path.relative_to(ROOT)), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
                   for path in INPUTS],
        'complete_road': {'definition': 'D_n=sum_j nu_j/a_j prod_{p|n}(1-p**(-a_j)), D_1=0',
                          'nodes': list(map(str, nodes)), 'weights': list(map(str, weights)),
                          'all_integer_and_composite_indices_retained': True,
                          'gamma_unit_and_full_prefix_retained': True},
        'energies': metrics, 'joint': full_joint,
        'partitions': partitions,
        'validation': {'old_endpoint_cross_route_checks': endpoint_checks,
                       'direct_harmonic_vs_green_checks': harmonic_checks,
                       'source_identity_q_P_Q_every_interior_integer': True,
                       'number_of_interior_integer_source_checks_per_sequence': B - A - 1,
                       'sigma_H_previous_certificate_overlap': True,
                       'joint_square_identity_zero_enclosed': True},
        'cost': {'complete_road_max_n': B, 'thickness_count': len(nodes), 'prime_count': len(primes),
                 'prime_factor_multiplications': road_mults, 'exponential_oracle_calls': elementary.exp_calls,
                 'distinct_integer_logarithms': len(elementary.logs), 'correction_divisor_sieve_additions': divisor_additions,
                 'green_reconstruction_integer_points': B - A + 1, 'direct_harmonic_check_points': len(harmonic_checks),
                 'elapsed_seconds_diagnostic_only': time.perf_counter() - started,
                 'large_arrays_regenerable_scratch_cache_not_required_in_deliverable': '_scratch_arrays.pkl'},
    }
    target = OUT / 'joint_energy_certificate.json'
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'report': str(target),
                      'q_positive_energy': metrics['q']['positive_square_energy'],
                      'P_energy': metrics['P256']['full_square_energy'],
                      'Q_positive_energy': metrics['Q']['positive_square_energy'],
                      'cross': full_joint['cross_q_P']}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
