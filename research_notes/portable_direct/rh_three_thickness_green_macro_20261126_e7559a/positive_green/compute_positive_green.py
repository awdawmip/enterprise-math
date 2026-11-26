#!/usr/bin/env python3
"""Closed-integer Green dual, mesh constants, and existing 11-anchor comparison.

No original road/source queries are made.  The original 1270-point certificate
is not recomputed.  Geometry is summed once on the original 11-anchor window;
the old 55 positive-residual energy intervals are reused for comparisons.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse
import hashlib
import importlib.util
import json


def module_at(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def green(L, R, x, z):
    return F((min(x, z) - L) * (R - max(x, z)), R - L)


def hat(a, b, c, x):
    if a <= x <= b:
        return F(x - a, b - a)
    if b <= x <= c:
        return F(c - x, c - b)
    return F(0)


def exact_checks():
    """A small exact check of the genuinely different source/obstacle interfaces."""
    checks = []
    for x in ([2, 3, 4, 5, 6], [2, 3, 5, 6]):
        L, R = x[0], x[-1]
        d = {3: F(1), 4: F(-4), 5: F(3)}
        t = [sum((hat(x[k - 1], x[k], x[k + 1], n) * d[n]
                  for n in d), F(0)) for k in range(1, len(x) - 1)]
        v = [F(0)] + [sum((green(L, R, a, b) * c
                           for b, c in zip(x[1:-1], t)), F(0))
                       for a in x[1:-1]] + [F(0)]
        observations = {}
        for k in range(len(x) - 1):
            for n in range(x[k], x[k + 1]):
                observations[n] = (F(x[k + 1] - n, x[k + 1] - x[k]) * v[k]
                                   + F(n - x[k], x[k + 1] - x[k]) * v[k + 1])
        observations[R] = F(0)
        energy = sum((max(z, F(0)) ** 2 / (n * n)
                      for n, z in observations.items()), F(0))
        psi = {a: sum((green(L, R, a, n) * max(z, 0) / (n * n)
                       for n, z in observations.items()), F(0))
               for a in range(L, R + 1)}
        paired = sum((c * psi[a] for a, c in zip(x[1:-1], t)), F(0))
        source_paired = sum((d[n] * sum((hat(x[k-1], x[k], x[k+1], n) * psi[x[k]]
                                        for k in range(1, len(x)-1)), F(0))
                             for n in d), F(0))
        assert energy == paired == source_paired
        assert all(2*psi[n] - psi[n-1] - psi[n+1]
                   == max(observations[n], 0)/(n*n) for n in range(L+1, R))
        checks.append({'nodes': x, 'positive_energy': str(energy),
                       'source_pairing': str(source_paired)})
    # V=(0,1,-1,0) on [2,5].  The H1 obstacle optimizer is (0,3/2,0,0).
    v = list(map(F, (0, 1, -1, 0)))
    t = [2*v[k]-v[k-1]-v[k+1] for k in (1, 2)]
    dp = sum((t[k-1]*max(v[k], 0) for k in (1, 2)), F(0))
    dh = sum((max(v[k+1], 0)-max(v[k], 0))**2 for k in range(3))
    cross = sum(max(v[k], 0)*max(-v[k+1], 0)
                + max(-v[k], 0)*max(v[k+1], 0) for k in range(3))
    u = [F(3, 2), F(0)]
    residual = [2*u[0]-u[1]-t[0], 2*u[1]-u[0]-t[1]]
    assert all(z >= 0 for z in residual)
    assert all(a*b == 0 for a, b in zip(u, residual))
    obstacle = 2*sum((a*b for a, b in zip(t, u)), F(0)) - (2*u[0]**2+2*u[1]**2-2*u[0]*u[1])
    assert dp == dh + cross == 3 and obstacle == F(9, 2)
    return {'green_source_identities': checks, 'obstacle_counterexample': {
        'nodes': [2, 3, 4, 5], 'V': list(map(str, v)),
        'signed_moments': list(map(str, t)), 'positive_dirichlet': str(dp),
        'positive_nodal_interpolant_dirichlet': str(dh),
        'crossing_subtraction': str(cross), 'H1_obstacle_supremum': str(obstacle)}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--previous', type=Path, required=True,
                        help='riemann_calibrated_green_sparse_20261126 directory')
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('positive_green_results.json'))
    args = parser.parse_args()
    previous = args.previous.resolve()
    base = (previous/'prior/riemann_signed_green_thickness_phase_20261124'
            '/prior/riemann_native_residual_growth_20261124'
            '/prior/riemann_matching_isotonic_anchors_20261124')
    anchor_path = base/'seams/saved_anchor_certificate.json'
    helper_path = (base/'prior/riemann_directed_local_20261124'
                   '/prior/riemann_cumulative_haar_20261123/dependencies/certify_fast_harmonic_energy.py')
    old_path = previous/'group_arithmetic/grouped_dirichlet_certificate.json'
    m = module_at('positive_green_interval', helper_path)
    old = json.loads(old_path.read_text())['saved_actual']
    old_rows = {(r['L'], r['R']): r for r in old['subintervals']}
    anchors = json.loads(anchor_path.read_text())['anchors']
    x = [a['x'] for a in anchors]
    q = [(m.rat(F(a['actual']['exact_bounds'][0]))[0],
          m.rat(F(a['actual']['exact_bounds'][1]))[1]) for a in anchors]
    size = len(x)-2
    mass = [[m.ZERO for _ in range(size)] for _ in range(size)]
    geometry_points = 0
    for k in range(len(x)-1):
        a, b = x[k], x[k+1]
        h = b-a
        for n in range(a, b):
            terms = []
            if 0 < k < len(x)-1:
                terms.append((k-1, F(b-n, h)))
            if 0 < k+1 < len(x)-1:
                terms.append((k, F(n-a, h)))
            for i, vi in terms:
                for j, vj in terms:
                    mass[i][j] = m.add(mass[i][j], m.rat(vi*vj/(n*n)))
            geometry_points += 1
    geometry_points += 1  # closed right endpoint, all basis values zero
    # H_n is generated once.  This is geometry for the sharp unit source radius.
    harmonic = m.ZERO
    g = {}
    for n in range(1, x[-1]+1):
        harmonic = m.add(harmonic, m.rat(F(1, n)))
        if n in x:
            g[n] = m.qmul(harmonic, n)

    def square_form(indices, values):
        return m.total(m.mul(mass[a-1][b-1], m.mul(u, v))
                       for a, u in zip(indices, values)
                       for b, v in zip(indices, values)
                       if abs(a-b) <= 1)

    def square_root(z):
        low = isqrt(max(0, z[0])*m.S)
        high = isqrt(max(0, z[1])*m.S)
        if high*high < max(0, z[1])*m.S:
            high += 1
        return low, high

    spectral_cache = {}

    def spectral_constant(indices):
        key = tuple(indices)
        if key in spectral_cache:
            return spectral_cache[key]
        if not indices:
            result = {'upper': F(0), 'lower': F(0), 'components': []}
            spectral_cache[key] = result
            return result
        runs = []
        for k in indices:
            if runs and k == runs[-1][-1]+1:
                runs[-1].append(k)
            else:
                runs.append([k])
        parts = []
        for run in runs:
            L, R = x[run[0]-1], x[run[-1]+1]
            inv = [[green(L, R, x[i], x[j]) for j in run] for i in run]
            mf = [[float(F(sum(mass[i-1][j-1]), 2*m.S)) for j in run] for i in run]
            kf = [[sum(float(inv[i][k])*mf[k][j] for k in range(len(run)))
                   for j in range(len(run))] for i in range(len(run))]
            yy = [1.0]*len(run)
            for _ in range(160):
                zz = [sum(row[j]*yy[j] for j in range(len(run))) for row in kf]
                scale = max(zz)
                yy = [z/scale for z in zz]
            y = [F(format(z, '.17g')) for z in yy]
            assert all(z > 0 for z in y)
            my = [m.total(m.qmul(mass[i-1][j-1], yj)
                          for j, yj in zip(run, y)) for i in run]
            ky = [m.total(m.qmul(my[j], inv[i][j]) for j in range(len(run)))
                  for i in range(len(run))]
            upper = max(F(z[1], m.S)/yj for z, yj in zip(ky, y))
            # Exact rational Rayleigh denominator with zero values at run boundaries.
            ext_y = [F(0)] + y + [F(0)]
            ext_x = [L] + [x[k] for k in run] + [R]
            denom = sum(((b-a)**2/F(d-c)
                         for a, b, c, d in zip(ext_y, ext_y[1:], ext_x, ext_x[1:])), F(0))
            numer = m.total(m.qmul(z, yj) for z, yj in zip(my, y))
            lower = F(numer[0], m.S)/denom
            assert 0 < lower <= upper
            parts.append({'nodes': [x[k] for k in run], 'boundary': [L, R],
                          'positive_rational_test_vector': list(map(str, y)),
                          'lower': lower, 'upper': upper})
        result = {'upper': max(p['upper'] for p in parts),
                  'lower': max(p['lower'] for p in parts), 'components': parts}
        spectral_cache[key] = result
        return result

    rows = []
    lookup = {}
    strict_improvements = 0
    crossing_blocks = 0
    singleton_exact = 0
    uncertain_signs = 0
    for i in range(len(x)-1):
        for j in range(i+1, len(x)):
            L, R = x[i], x[j]
            prior = old_rows[L, R]
            v = [m.ZERO] + [m.sub(q[k], m.add(m.qmul(q[i], R-x[k], R-L),
                                             m.qmul(q[j], x[k]-L, R-L)))
                                  for k in range(i+1, j)] + [m.ZERO]
            u = [m.positive(z) for z in v]
            support = [k for k in range(i+1, j) if v[k-i][1] > 0]
            uncertain_signs += sum(v[k-i][0] <= 0 < v[k-i][1] for k in support)
            dh = m.total(m.qmul(m.square(m.sub(u[k+1-i], u[k-i])), 1, x[k+1]-x[k])
                         for k in range(i, j))
            crossing = m.total(m.qmul(m.add(m.mul(u[k-i], m.positive(m.neg(v[k+1-i]))),
                                                   m.mul(m.positive(m.neg(v[k-i])), u[k+1-i])),
                                            1, x[k+1]-x[k]) for k in range(i, j))
            reconstructed_dp = m.add(dh, crossing)
            old_dp = m.decode(prior['signed_positive_dirichlet_energy'])
            assert max(reconstructed_dp[0], old_dp[0]) <= min(reconstructed_dp[1], old_dp[1])
            if crossing[0] > 0:
                crossing_blocks += 1
            spectral = spectral_constant(support)
            old_constant = m.decode(prior['closed_constant_upper'])
            cupper = min(spectral['upper'], F(old_constant[1], m.S))
            bound = m.qmul(dh, cupper)
            old_bound = m.decode(prior['directional_energy_upper'])
            old_energy = m.decode(prior['positive_residual_square_energy'])
            assert old_energy[0] <= bound[1]
            if bound[1] < old_bound[0]:
                strict_improvements += 1
            h_energy = square_form(list(range(i+1, j)), u[1:-1])
            assert old_energy[0] <= h_energy[1] and h_energy[0] <= bound[1]
            if j-i == 2 and support:
                singleton_exact += 1
                assert max(old_energy[0], h_energy[0]) <= min(old_energy[1], h_energy[1])
            radius = [m.sub(m.add(m.qmul(g[L], R-x[k], R-L),
                                 m.qmul(g[R], x[k]-L, R-L)), g[x[k]])
                      for k in range(i+1, j)]
            radius_square = square_form(list(range(i+1, j)), radius)
            radius_square = (max(0, radius_square[0]), max(0, radius_square[1]))
            old_radius_square = m.rat(F((R-L)**5-(R-L), 120*L**4))
            assert radius_square[1] <= old_radius_square[1]
            row = {'L': L, 'R': R, 'possible_positive_nodes': [x[k] for k in support],
                   'positive_nodal_interpolant_dirichlet': m.record(dh),
                   'crossing_subtraction': m.record(crossing),
                   'spectral_constant_lower': m.record(m.rat(spectral['lower'])),
                   'spectral_constant_upper': m.record(m.rat(cupper)),
                   'mesh_positive_energy_upper': m.record(bound),
                   'old_directional_energy_upper': prior['directional_energy_upper'],
                   'actual_positive_residual_energy_reused': prior['positive_residual_square_energy'],
                   'positive_nodal_interpolant_square_energy': m.record(h_energy),
                   'sharp_unit_source_radius_square': m.record(radius_square),
                   'old_unit_source_radius_square': m.record(old_radius_square)}
            rows.append(row)
            lookup[L, R] = row
    partitions = []
    for p in old['partitions']:
        nodes = p['coarse_nodes']
        selected = [lookup[a, b] for a, b in zip(nodes, nodes[1:])]
        names = ('mesh_positive_energy_upper', 'old_directional_energy_upper',
                 'actual_positive_residual_energy_reused', 'sharp_unit_source_radius_square',
                 'old_unit_source_radius_square')
        totals = {name: m.record(m.total(m.decode(r[name]) for r in selected)) for name in names}
        new_radius = m.total(m.decode(r['sharp_unit_source_radius_square']) for r in selected)
        old_radius = m.total(m.decode(r['old_unit_source_radius_square']) for r in selected)
        totals['sharp_unit_source_root_radius'] = m.record(square_root(new_radius))
        totals['old_unit_source_root_radius'] = m.record(square_root(old_radius))
        partitions.append({'coarse_nodes': nodes, 'totals': totals})
    spectral_records = []
    for key, record in sorted(spectral_cache.items()):
        spectral_records.append({'nodes': [x[k] for k in key],
            'constant_lower': str(record['lower']), 'constant_upper': str(record['upper']),
            'components': [{**part, 'lower': str(part['lower']), 'upper': str(part['upper'])}
                           for part in record['components']]})
    result = {
        'schema': 'EM_POSITIVE_GREEN_MESH_V1', 'status': 'PASS',
        'author': 'EM-DIRECT-E7559A / TASK_RESEARCH',
        'activity': 'RA-D2F111EA1C0D4B1DBEFBC1B4',
        'status_scope': 'Author calculation and proof checks; not independent Review or formal Result.',
        'fixed_scope': 'Fixed Heartbeat X6 auxiliary scalar; full integer/composite source, real endpoints and signed moments retained.',
        'arithmetic': '80-place outward integer intervals; exact rational Green inverse and Collatz upper ratios. Floating power iteration chooses rational positive vectors only; validity never depends on its convergence.',
        'exact_interface_checks': exact_checks(),
        'new_road_queries': 0, 'new_source_queries': 0, 'original_1270_point_reruns': 0,
        'input_anchor_count': len(x), 'reused_subinterval_energy_intervals': len(rows),
        'closed_geometry_points_summed_once': geometry_points,
        'strictly_improved_old_nonzero_bounds': strict_improvements,
        'strict_crossing_subtraction_blocks': crossing_blocks,
        'single_positive_hat_exact_cases': singleton_exact,
        'uncertain_internal_signs': uncertain_signs,
        'partitions': partitions, 'subintervals': rows,
        'spectral_geometry': spectral_records,
        'dependencies': [{'path': str(p.relative_to(previous)),
                          'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
                         for p in (anchor_path, helper_path, old_path)]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in (
        'status', 'input_anchor_count', 'reused_subinterval_energy_intervals',
        'closed_geometry_points_summed_once', 'strictly_improved_old_nonzero_bounds',
        'strict_crossing_subtraction_blocks', 'single_positive_hat_exact_cases',
        'uncertain_internal_signs')}, ensure_ascii=False))
    for p in partitions:
        print(json.dumps(p, ensure_ascii=False))


if __name__ == '__main__':
    main()
