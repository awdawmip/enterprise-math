#!/usr/bin/env python3
"""Exact checks for reciprocal-measure cumulative flux and Haar identities.

All non-timing calculations use fractions. Optional actual-road check reads
only the two already certified finite input files and propagates intervals.
"""
from fractions import Fraction as Q
from pathlib import Path
from random import Random
import argparse
import hashlib
import json


def mu(u, v):
    return Q(1, u) - Q(1, v)


def average(e, u, v):
    return sum((e[n] * Q(1, n * (n + 1)) for n in range(u, v)), Q(0)) / mu(u, v)


def lerp(yu, yv, u, v, n):
    return (yu * (v - n) + yv * (n - u)) / (v - u)


def tree(nodes, rng):
    if len(nodes) <= 2:
        return []
    k = rng.randrange(1, len(nodes) - 1)
    return [(nodes[0], nodes[k], nodes[-1])] + tree(nodes[:k + 1], rng) + tree(nodes[k:], rng)


def deterministic_checks():
    rng = Random(20261123)
    totals = {'roads': 0, 'packets': 0, 'kernel_checks': 0, 'hardy_checks': 0}
    for case in range(48):
        a = 2 + case % 11
        b = a + 3 + case % 16
        q = {n: Q(rng.randrange(-30, 31), rng.randrange(1, 10)) for n in range(a, b + 1)}
        e = {n: n * q[n + 1] - (n + 1) * q[n] for n in range(a, b)}
        eb = average(e, a, b)
        chord = {n: lerp(q[a], q[b], a, b, n) for n in range(a, b + 1)}
        p = {n: q[n] - chord[n] for n in q}
        assert eb == (a * q[b] - b * q[a]) / (b - a)
        assert sum((e[n] * Q(1, n * (n + 1)) for n in e), Q(0)) == q[b] / b - q[a] / a
        var = sum(((e[n] - eb) ** 2 * Q(1, n * (n + 1)) for n in e), Q(0))
        assert var == sum(((p[n + 1] - p[n]) ** 2 for n in e), Q(0))
        nodes = [a] + [n for n in range(a + 1, b) if rng.randrange(3)] + [b]
        f = {}
        for u, v in zip(nodes, nodes[1:]):
            for n in range(u, v + 1):
                f[n] = lerp(q[u], q[v], u, v, n)
        cell_means = [(u, v, average(e, u, v)) for u, v in zip(nodes, nodes[1:])]
        projected_var = sum((mu(u, v) * (em - eb) ** 2 for u, v, em in cell_means), Q(0))
        fine_var = sum(((e[n] - em) ** 2 * Q(1, n * (n + 1)) for u, v, em in cell_means for n in range(u, v)), Q(0))
        assert var == projected_var + fine_var
        assert projected_var == sum((((f[n + 1] - chord[n + 1]) - (f[n] - chord[n])) ** 2 for n in e), Q(0))
        assert fine_var == sum((((q[n + 1] - f[n + 1]) - (q[n] - f[n])) ** 2 for n in e), Q(0))
        packets = tree(nodes, rng)
        haars = []
        for l, x, r in packets:
            t = (q[x] - q[l]) / (x - l) - (q[r] - q[x]) / (r - x)
            d = average(e, l, x) - average(e, x, r)
            assert d == x * t
            vh = mu(l, x) * mu(x, r) / mu(l, r) * d ** 2
            assert vh == Q((x - l) * (r - x), r - l) * t ** 2
            vp = Q((x - l) * (r - x), r - l) * max(t, Q(0)) ** 2
            assert (r - l) ** 3 * max(t, Q(0)) ** 2 == Q((r - l) ** 4, (x - l) * (r - x)) * vp
            haars.append(vh)
        assert sum(haars, Q(0)) == projected_var

        rb = q[b] / b
        an = {n: e[n] * Q(1, n * (n + 1)) for n in e}
        for n in q:
            assert q[n] / n == rb - sum((an[k] for k in range(n, b)), Q(0))
        for support in [list(q), [n for n in q if q[n] > 0]]:
            count = lambda k: sum(n <= k for n in support)
            quadratic = len(support) * rb ** 2 - 2 * rb * sum((count(k) * an[k] for k in e), Q(0))
            quadratic += sum((count(min(k, l)) * an[k] * an[l] for k in e for l in e), Q(0))
            assert quadratic == sum(((q[n] / n) ** 2 for n in support), Q(0))
            totals['kernel_checks'] += 1
        tnorm = sum(((q[n] / n - rb) ** 2 for n in q), Q(0))
        hnorm = sum(((e[n] / n) ** 2 for n in e), Q(0))
        assert tnorm <= 4 * hnorm
        totals['hardy_checks'] += 1
        totals['roads'] += 1
        totals['packets'] += len(packets)
    return totals


def two_families(a):
    assert a % 2 == 0
    b = 2 * a
    out = {}
    e_vectors = []
    for name in ['clustered', 'alternating']:
        e = {n: Q(0) for n in range(b + 1)}
        for n in range(a, b):
            sign = (1 if n < a + a // 2 else -1) if name == 'clustered' else (-1) ** n
            e[n] = Q(n * (n + 1) * sign, b ** 2)
        r = {b: Q(0)}
        for n in range(b - 1, 0, -1):
            r[n] = r[n + 1] - e[n] * Q(1, n * (n + 1))
        q = {0: Q(0), **{n: n * r[n] for n in r}, b + 1: Q(0)}
        assert q[a] == q[b] == 0
        assert all(q[n] == 0 for n in range(a))
        for n in range(1, b + 1):
            assert abs(q[n + 1] - 2 * q[n] + q[n - 1]) <= Q(2, n)
            assert n * q[n + 1] - (n + 1) * q[n] == e[n]
        energy = sum((max(q[n], Q(0)) ** 2 / n ** 2 for n in range(a, b + 1)), Q(0))
        expected = Q(a * (a * a + 2), 12 * b ** 4) if name == 'clustered' else Q(a, 2 * b ** 4)
        assert energy == expected
        variance = sum((e[n] ** 2 * Q(1, n * (n + 1)) for n in range(a, b)), Q(0))
        assert average(e, a, b) == 0
        out[name] = {'positive_energy_exact': str(energy), 'variance_exact': str(variance)}
        e_vectors.append(e)
    assert all(abs(e_vectors[0][n]) == abs(e_vectors[1][n]) for n in range(b + 1))
    assert out['clustered']['variance_exact'] == out['alternating']['variance_exact']
    ratio = Q(out['clustered']['positive_energy_exact']) / Q(out['alternating']['positive_energy_exact'])
    assert ratio == Q(a * a + 2, 6)
    return {'A': a, 'B': b, 'same_endpoints_and_zero_skeleton': True,
            'same_entire_absolute_flux': True, 'source_bound': '2/n',
            'energy_ratio_exact': str(ratio), **out}


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def scale(a, c):
    return (a[0] * c, a[1] * c) if c >= 0 else (a[1] * c, a[0] * c)


def square(a):
    return (Q(0) if a[0] <= 0 <= a[1] else min(a[0] ** 2, a[1] ** 2), max(a[0] ** 2, a[1] ** 2))


def positive(a):
    return max(a[0], Q(0)), max(a[1], Q(0))


def isect(a, b):
    return max(a[0], b[0]) <= min(a[1], b[1])


def isum(xs):
    result = Q(0), Q(0)
    for x in xs:
        result = add(result, x)
    return result


def encoded_interval(a, digits=30):
    scale10 = 10 ** digits
    lo = (a[0] * scale10).__floor__()
    hi = (a[1] * scale10).__ceil__()
    def fixed(z):
        sign = '-' if z < 0 else ''
        z = abs(z)
        return f'{sign}{z // scale10}.{z % scale10:0{digits}d}'
    return {'lower': fixed(lo), 'upper': fixed(hi), 'exact_lower': str(a[0]), 'exact_upper': str(a[1])}


def read_interval(row):
    den = 10 ** row['denominator_power_of_10']
    return tuple(Q(int(x), den) for x in row['integer_bounds'])


def actual_check(source_root):
    op = source_root / 'rh_tree_order_20261122/optimal_tree_order_certificate.json'
    tp = source_root / 'rh_triangle_certificate_20261122/dyadic_triangle_certificate.json'
    old = json.loads(op.read_text())
    tri = json.loads(tp.read_text())
    endpoints = {row['n']: read_interval(row['value']) for row in tri['roads']['q']['true_dyadic_endpoint_samples']}
    result = []
    count = 0
    for block, old_block in zip(old['blocks'], tri['roads']['q']['dyadic_blocks']):
        a, b = block['X'], block['Y']
        residual = {row['n']: read_interval(row['residual']) for row in block['residual_nodes']}
        nodes = sorted(residual)
        mean = scale(sub(scale(endpoints[b], a), scale(endpoints[a], b)), Q(1, b - a))
        # Residual flux mean is zero. Each fine-cell conditional flux mean follows
        # from endpoint differences, without reading or rebuilding the full road.
        cells = []
        for u, v in zip(nodes, nodes[1:]):
            em = scale(sub(scale(residual[v], u), scale(residual[u], v)), Q(1, v - u))
            cells.append((u, v, em))
        variance = isum(scale(square(em), mu(u, v)) for u, v, em in cells)
        direct_dirichlet = isum(scale(square(sub(residual[v], residual[u])), Q(1, v - u)) for u, v in zip(nodes, nodes[1:]))
        assert isect(variance, direct_dirichlet)
        packet_energies = []
        packet_positive_energies = []
        levels = []
        for level in old_block['levels']:
            weighted_old = []
            weighted_new = []
            for p in level['packets']:
                l, x, r = p['L'], p['x'], p['R']
                em_l = scale(sub(scale(residual[x], l), scale(residual[l], x)), Q(1, x - l))
                em_r = scale(sub(scale(residual[r], x), scale(residual[x], r)), Q(1, r - x))
                d = sub(em_l, em_r)
                t = scale(d, Q(1, x))
                old_t = read_interval(p['signed_charge'])
                assert isect(t, old_t)
                factor = mu(l, x) * mu(x, r) / mu(l, r)
                packet_energies.append(scale(square(d), factor))
                vp = scale(square(positive(d)), factor)
                packet_positive_energies.append(vp)
                weighted_old.append(scale(square(positive(old_t)), (r - l) ** 3))
                weighted_new.append(scale(vp, Q((r - l) ** 4, (x - l) * (r - x))))
                count += 1
            old_sum, new_sum = isum(weighted_old), isum(weighted_new)
            assert isect(old_sum, new_sum)
            levels.append({'level': level['level'], 'directed_weighted_moment_over_X2': encoded_interval(scale(new_sum, Q(1, a * a))), 'matches_old_triangle_moment': True})
        assert isect(isum(packet_energies), variance)
        result.append({'X': a, 'Y': b, 'whole_flux_mean': encoded_interval(mean),
                       'fine_projected_flux_variance': encoded_interval(variance),
                       'fine_interpolant_dirichlet_energy': encoded_interval(direct_dirichlet),
                       'positive_oriented_haar_energy': encoded_interval(isum(packet_positive_energies)),
                       'levels': levels})
    return {'scope': 'Re-expresses the existing 44-node actual q data and 38 original packets; no new full-road generation or arithmetic bound.',
            'input_files': [{'path': p.relative_to(source_root).as_posix(), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in [op, tp]],
            'packet_count': count, 'all_harmonic_haar_interval_checks_passed': True, 'blocks': result}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--source-root', type=Path)
    args = p.parse_args()
    result = {'schema': 'RH_CUMULATIVE_FLUX_HAAR_CERTIFICATE_V1', 'status': 'PASS',
              'arithmetic': 'exact Fraction arithmetic; optional actual data propagated as rational endpoint intervals',
              'structural_checks': deterministic_checks(),
              'same_absolute_flux_families': [two_families(a) for a in [4, 8, 16, 32, 64, 128, 256, 1024]],
              'actual_road': actual_check(args.source_root) if args.source_root else None}
    target = Path(__file__).with_name('cumulative_flux_certificate.json')
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'structural_checks': result['structural_checks'],
                      'same_absolute_flux_family_count': len(result['same_absolute_flux_families']),
                      'actual_packets': result['actual_road']['packet_count'] if result['actual_road'] else None,
                      'output': str(target)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
