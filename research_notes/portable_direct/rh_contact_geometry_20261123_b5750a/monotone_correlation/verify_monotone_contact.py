#!/usr/bin/env python3
"""Exact author checks for reciprocal isotonic regression and contact-pool energy.

No old file or remote state is written. All assertions use Fraction; displayed
decimals only summarize the exact rational checks. This is not an independent
review or evidence for unbounded arithmetic cancellation.
"""
from fractions import Fraction as F
from pathlib import Path
from random import Random
import hashlib
import json
import sys

sys.dont_write_bytecode = True
sys.set_int_max_str_digits(0)


def record(x, digits=35):
    scale = 10 ** digits
    lo = x.numerator * scale // x.denominator
    hi = -((-x.numerator * scale) // x.denominator)
    return {'lower_integer': str(lo), 'upper_integer': str(hi),
            'denominator_power_of_10': digits}


def flux_means(nodes, values):
    mass = [F(1, a) - F(1, b) for a, b in zip(nodes, nodes[1:])]
    means = [(a * values[b] - b * values[a]) / (b - a)
             for a, b in zip(nodes, nodes[1:])]
    return mass, means


def pava(weights, values):
    blocks = []
    for i, (weight, value) in enumerate(zip(weights, values)):
        blocks.append([i, i + 1, weight, weight * value])
        while len(blocks) > 1 and blocks[-2][3] * blocks[-1][2] > blocks[-1][3] * blocks[-2][2]:
            a, b = blocks[-2:]
            blocks[-2:] = [[a[0], b[1], a[2] + b[2], a[3] + b[3]]]
    fit = [F(0)] * len(values)
    for first, last, weight, moment in blocks:
        for i in range(first, last):
            fit[i] = moment / weight
    return fit


def interpolate(nodes, values, n):
    for a, b in zip(nodes, nodes[1:]):
        if a <= n <= b:
            return ((b - n) * values[a] + (n - a) * values[b]) / (b - a)
    raise ValueError(n)


def lower_hull(nodes, values):
    hull = []
    for x in nodes:
        hull.append(x)
        while len(hull) >= 3:
            a, b, c = hull[-3:]
            if (values[b] - values[a]) * (c - b) < (values[c] - values[b]) * (b - a):
                break
            hull.pop(-2)
    return hull


def trace(left, right):
    h = right - left
    return sum((F((n - left) * (right - n), h * n * n)
                for n in range(left + 1, right)), F(0))


def analyze(nodes, values, scan=True):
    weights, means = flux_means(nodes, values)
    fit = pava(weights, means)
    assert all(a <= b for a, b in zip(fit, fit[1:]))
    cumulative = F(0)
    residual = {nodes[0]: F(0)}
    greatest = {nodes[0]: values[nodes[0]]}
    for i, (a, b) in enumerate(zip(nodes, nodes[1:])):
        cumulative += weights[i] * (means[i] - fit[i])
        residual[b] = b * cumulative
        greatest[b] = values[b] - residual[b]
        assert cumulative >= 0
        if i + 1 < len(fit) and fit[i] < fit[i + 1]:
            assert cumulative == 0
    assert cumulative == 0
    hull = lower_hull(nodes, values)
    for n in nodes:
        assert greatest[n] == interpolate(hull, values, n)
    regression_energy = sum((w * (z - m) ** 2 for w, z, m in zip(weights, means, fit)), F(0))
    dirichlet = sum(((residual[b] - residual[a]) ** 2 / (b - a)
                     for a, b in zip(nodes, nodes[1:])), F(0))
    assert regression_energy == dirichlet
    contacts = [i for i, n in enumerate(nodes) if residual[n] == 0]
    pool_rows, pool_budget, critical_energy = [], F(0), F(0)
    for i, j in zip(contacts, contacts[1:]):
        left, right = nodes[i], nodes[j]
        energy = sum((weights[k] * (means[k] - fit[k]) ** 2 for k in range(i, j)), F(0))
        assert energy == sum(((residual[nodes[k + 1]] - residual[nodes[k]]) ** 2 /
                              (nodes[k + 1] - nodes[k]) for k in range(i, j)), F(0))
        assert all(fit[k] == fit[i] for k in range(i, j))
        if not energy:
            continue
        h = right - left
        gamma = trace(left, right)
        assert gamma <= F(h * h - 1, 6 * left * left)
        actual = F(0)
        if scan:
            for n in range(left + 1, right):
                r = interpolate(nodes[i:j + 1], residual, n)
                assert r > 0
                assert r * r <= F((n - left) * (right - n), h) * energy
                actual += r * r / (n * n)
            assert actual <= gamma * energy
            critical_energy += actual
        pool_budget += gamma * energy
        pool_rows.append({'endpoints': [left, right], 'width': h,
                          'dirichlet_energy': record(energy),
                          'trace_weight': record(gamma), 'budget': record(gamma * energy)})
    return {'fit': fit, 'means': means, 'weights': weights, 'contacts': contacts,
            'residual': residual, 'greatest': greatest,
            'distance_square': regression_energy, 'pool_budget': pool_budget,
            'critical_residual_square': critical_energy, 'pools': pool_rows}


def tree_packets(nodes):
    if len(nodes) <= 2:
        return []
    middle = len(nodes) // 2
    return [(nodes[0], nodes[middle], nodes[-1])] + tree_packets(nodes[:middle + 1]) + tree_packets(nodes[middle:])


def packet_t(values, left, middle, right):
    return (values[middle] - values[left]) / (middle - left) - (values[right] - values[middle]) / (right - middle)


def random_checks():
    rng = Random(2026112302)
    pools = packets = 0
    for _ in range(40):
        first = rng.randrange(2, 20)
        last = first + rng.randrange(8, 45)
        interior = sorted(rng.sample(range(first + 1, last), rng.randrange(2, min(15, last - first))))
        nodes = [first] + interior + [last]
        values = {n: F(rng.randrange(-90, 91), rng.randrange(1, 10)) for n in nodes}
        data = analyze(nodes, values)
        directed = F(0)
        for left, middle, right in tree_packets(nodes):
            t = packet_t(values, left, middle, right)
            a, b = middle - left, right - middle
            directed += F(a * b, a + b) * max(t, F(0)) ** 2
            packets += 1
        assert directed <= data['distance_square']
        pools += len(data['pools'])
    # The nondecreasing cone is a proper subset of the fixed-tree negative cone.
    nodes = list(range(4, 9))
    values = {4: F(0), 5: F(-10), 6: F(-1), 7: F(-10), 8: F(0)}
    assert all(packet_t(values, *p) < 0 for p in tree_packets(nodes))
    assert analyze(nodes, values)['distance_square'] > 0
    return {'rational_roads': 40, 'packets': packets, 'positive_contact_pools': pools,
            'independent_lower_hull_matches_pava': True,
            'kkt_and_exact_energy_identities': True,
            'directed_haar_distance_bound': True,
            'proper_cone_inclusion_example': True}


def single_peak(s):
    x, h, step = s ** 5, s ** 4, s ** 2
    middle = 3 * x // 2
    left, right = middle - h // 2, middle + h // 2
    def q(n):
        if n <= left or n >= right:
            return F(0)
        r = n - left
        return F(r * r * (h - r) ** 2, x * h * h)
    nodes = list(range(x, 2 * x + 1, step))
    assert all(n in nodes for n in (left, middle, right))
    values = {n: q(n) for n in nodes}
    data = analyze(nodes, values)
    assert all(v == 0 for v in data['greatest'].values())
    assert len(data['pools']) == 1 and data['pools'][0]['endpoints'] == [left, right]
    assert data['pool_budget'] <= F(1, 315)
    assert data['distance_square'] >= F(s * s, 64)
    coarse_t = packet_t(values, x, middle, 2 * x)
    assert x * coarse_t * coarse_t == F(s, 16)
    actual = F(0)
    fine_error = F(0)
    prior = q(left - 1)
    current = q(left)
    for n in range(left, right + 1):
        after = q(n + 1)
        second = after - 2 * current + prior
        assert abs(second) <= F(4, n)
        actual += current * current / (n * n)
        f = interpolate(nodes, values, n)
        fine_error += (current - f) ** 2 / (n * n)
        prior, current = current, after
    assert F(81, 524288) <= actual <= F(1, 256)
    assert fine_error <= F(1, 30 * s ** 8)
    return {'s': s, 'window': [x, 2 * x], 'peak_support': [left, right],
            'peak_width': h, 'fine_step': step, 'sample_count': len(nodes),
            'all_integer_source_bound': 'abs(Delta^2 q_n) <= 4/n',
            'positive_contact_pools': data['pools'],
            'ordinary_isotonic_distance_square': record(data['distance_square']),
            'contact_pool_budget': record(data['pool_budget']),
            'actual_positive_energy': record(actual),
            'fine_interpolation_error_square': record(fine_error),
            'old_coarse_budget_normalized_by_X_square': str(F(s, 16))}


def main():
    rows = [single_peak(s) for s in (2, 4, 8)]
    result = {'status': 'PASS', 'schema': 'RH_MONOTONE_CONTACT_POOL_V1',
              'scope': 'Author checks for arbitrary scalar roads; no real matching arithmetic bound or independent review.',
              'random_checks': random_checks(), 'single_peak_family': rows,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    path = Path(__file__).with_name('monotone_contact_certificate.json')
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'random_checks': result['random_checks'],
                      'single_peak_parameters': [r['s'] for r in rows],
                      'certificate': str(path)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
