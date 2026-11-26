#!/usr/bin/env python3
"""Finite checks of the interval mean-square transfer; no old road reruns."""
from pathlib import Path
from fractions import Fraction as F
import argparse
import hashlib
import importlib.util
import json


def green(L, R, x, z):
    return F((min(x, z)-L)*(R-max(x, z)), R-L)


def variance(v):
    mean = sum(v, F(0))/len(v)
    return sum(((z-mean)**2 for z in v), F(0))


def interpolate(x, values, n):
    if n == x[-1]:
        return values[-1]
    for j, (a, b) in enumerate(zip(x, x[1:])):
        if a <= n < b:
            return F(b-n, b-a)*values[j]+F(n-a, b-a)*values[j+1]
    raise AssertionError(n)


def exact_checks():
    counts = {'source_vectors': 0, 'Abel_coordinates': 0,
              'long_edge_spectral_checks': 0, 'fine_mesh_transfers': 0,
              'Dirichlet_projection_checks': 0}
    for h in range(2, 25):
        L, R = h+3, 2*h+3
        r = 1+h//8
        gap = h-4*(r-1)
        assert gap >= F(h, 2)
        cases = ([F(1)]*(h-1),
                 [F((-1)**j) for j in range(1, h)],
                 [F(1 if j <= h//2 else -1) for j in range(1, h)],
                 [F((j*j+3*j+2) % 7-3, j+1) for j in range(1, h)])
        for a in cases:
            P, Q = [F(0)], [F(0)]
            for m, z in zip(range(L+1, R), a):
                P.append(P[-1]+z)
                Q.append(Q[-1]+z/m)
            for i, k in enumerate(range(L, R)):
                got = P[i]/k + sum((P[j]/F(m*(m+1))
                                   for j, m in enumerate(range(L, k))), F(0))
                assert got == Q[i]
                counts['Abel_coordinates'] += 1
            vp, vq = variance(P), variance(Q)
            assert vq <= F(R, L*L*(L+1))*vp
            full_edges = sum(((P[j]-P[i])**2
                              for i in range(h) for j in range(i+1, h)), F(0))
            assert full_edges == h*vp
            band = sum(((P[j]-P[i])**2
                        for i in range(h) for j in range(i+r, h)), F(0))
            assert gap*vp <= band
            counts['source_vectors'] += 1
            counts['long_edge_spectral_checks'] += 1
            U = [sum((green(L, R, n, m)*z/m for m, z in zip(range(L+1, R), a)), F(0))
                 for n in range(L, R+1)]
            assert U[0] == U[-1] == 0
            assert sum(((b-a)**2 for a, b in zip(U, U[1:])), F(0)) == vq
            meshes = {tuple(range(L, R+1)), (L, L+h//2, R),
                      tuple(sorted({L, L+1, L+h//3, R-1, R}))}
            for x in meshes:
                values = [U[n-L] for n in x]
                d_fine = sum(((v-u)**2/F(b-a)
                              for a, b, u, v in zip(x, x[1:], values, values[1:])), F(0))
                energy = sum((max(interpolate(x, values, n), F(0))**2/F(n*n)
                              for n in range(L, R+1)), F(0))
                assert d_fine <= vq
                c_upper = F(h*h, 8*L*L)
                upper = c_upper*F(R, L*L*(L+1)*gap)*band
                assert energy <= c_upper*d_fine <= c_upper*vq <= upper
                counts['fine_mesh_transfers'] += 1
                counts['Dirichlet_projection_checks'] += 1
    periodic = []
    for X in (8, 16, 32, 64, 128):
        def source(n):
            residue = (n-1) % X+1
            return 1 if residue <= X//2 else -1
        for u in range(2*X+1):
            assert sum(source(n) for n in range(u+1, u+X+1)) == 0
        c = 3*X//2
        p = sum((green(X, 2*X, c, m)*F(source(m), m)
                 for m in range(X+1, 2*X)), F(0))
        reflection = F(1, 6)+sum((F(m-X, 2)*(F(1, m)-F(1, 3*X-m))
                                  for m in range(X+1, c)), F(0))
        assert p == reflection and p >= F(X, 616)
        energy = sum((interpolate((X, c, 2*X), (F(0), p, F(0)), n)**2/F(n*n)
                      for n in range(X, 2*X+1)), F(0))
        lower = F(X, 32*616*616)
        assert energy >= p*p/(32*X) >= lower
        periodic.append({'X': X, 'single_length': X, 'all_tested_length_deficits': '0',
                         'center_count': 2*X+1, 'midpoint_value': str(p),
                         'positive_energy': str(energy), 'analytic_energy_lower': str(lower),
                         'mass_values': [0, 2]})
    return {'counts': counts, 'bounded_periodic_obstruction': periodic}


def module_at(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def finite_prime_examples(previous):
    helper = (previous/'prior/riemann_calibrated_green_sparse_20261126'
              '/prior/riemann_signed_green_thickness_phase_20261124'
              '/prior/riemann_native_residual_growth_20261124'
              '/prior/riemann_matching_isotonic_anchors_20261124'
              '/prior/riemann_directed_local_20261124'
              '/prior/riemann_cumulative_haar_20261123/dependencies/certify_fast_harmonic_energy.py')
    m = module_at('interval_transfer_outward', helper)
    limit = 512
    is_prime = [True]*(limit+1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, limit+1):
        if is_prime[p]:
            for n in range(p*p, limit+1, p):
                is_prime[n] = False
    logs = {p: m.log_int(p) for p in range(2, limit+1) if is_prime[p]}
    lam = [m.ZERO]*(limit+1)
    for p, logp in logs.items():
        n = p
        while n <= limit:
            lam[n] = logp
            n *= p
    rows = []
    for X in (32, 64, 128, 256):
        L, R, h = X, 2*X, X
        r, gap = 1+h//8, h-4*(h//8)
        x = [L, L+1, L+h//3, L+3*h//4, R]
        for kind in ('ordinary_primes', 'von_mangoldt'):
            P, Q = [m.ZERO], [m.ZERO]
            for n in range(L+1, R):
                mass = logs[n] if kind == 'ordinary_primes' and is_prime[n] else (
                    lam[n] if kind == 'von_mangoldt' else m.ZERO)
                z = m.sub(m.ONE, mass)
                P.append(m.add(P[-1], z))
                Q.append(m.add(Q[-1], m.qmul(z, 1, n)))
            mean_q = m.qmul(m.total(Q), 1, h)
            U = [m.ZERO]
            for q in Q:
                U.append(m.add(U[-1], m.sub(mean_q, q)))
            U[-1] = m.ZERO  # exact Dirichlet boundary, not independent uncertainty
            energy = m.ZERO
            for j, (a, b) in enumerate(zip(x, x[1:])):
                for n in range(a, b):
                    v = m.add(m.qmul(U[a-L], b-n, b-a), m.qmul(U[b-L], n-a, b-a))
                    energy = m.add(energy, m.qmul(m.square(m.positive(v)), 1, n*n))
            # Right endpoint is exactly zero.
            J = [m.ZERO]
            for d in range(1, h):
                J.append(m.total(m.square(m.sub(P[u+d], P[u])) for u in range(h-d)))
            band = m.total(J[r:])
            total = m.total(J[1:])
            c_upper = F(h*h, 8*L*L)
            coefficient = c_upper*F(R, L*L*(L+1)*gap)
            upper = m.qmul(band, coefficient)
            all_center_upper = m.qmul(total, F(h, 2*L**4))
            assert energy[1] <= upper[1] and energy[1] <= all_center_upper[1]
            K_upper = max(F(J[d][1], m.S*X*d) for d in range(1, h))
            rows.append({'X': X, 'source': kind, 'fine_nodes': x,
                         'length_band': [r, h-1], 'edge_graph_gap': gap,
                         'closed_positive_green_square': m.record(energy),
                         'length_band_mean_square_sum': m.record(band),
                         'transfer_coefficient': str(coefficient),
                         'length_band_energy_upper': m.record(upper),
                         'all_center_energy_upper': m.record(all_center_upper),
                         'finite_K_upper': m.record(m.rat(K_upper))})
    return {'scope': 'New small-window ordinary-prime and von-Mangoldt Green potentials; not original matched-road samples.',
            'ordinary_prime_logs_generated': len(logs), 'sieve_limit': limit,
            'windows': rows, 'interval_helper': {
                'path': str(helper.relative_to(previous)),
                'sha256': hashlib.sha256(helper.read_bytes()).hexdigest()}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--previous', type=Path, required=True,
                        help='riemann_three_thickness_green_macro_20261126 directory')
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('interval_transfer_results.json'))
    args = parser.parse_args()
    exact = exact_checks()
    actual = finite_prime_examples(args.previous.resolve())
    result = {'schema': 'EM_FIXED_INTERVAL_MEAN_SQUARE_GREEN_V1', 'status': 'PASS',
              'author': 'EM-DIRECT-E7559A / TASK_RESEARCH',
              'activity': 'RA-D2F111EA1C0D4B1DBEFBC1B4',
              'status_scope': 'Author finite proof checks; no independent Review or formal Result.',
              'original_1270_point_reruns': 0, 'old_55_subwindow_reruns': 0,
              'arithmetic': 'Exact rational structural checks and 80-place outward interval prime examples; no floating-point validity judgments.',
              'exact': exact, 'prime_examples': actual}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'exact_counts': exact['counts'],
                      'bounded_periodic_examples': len(exact['bounded_periodic_obstruction']),
                      'new_prime_examples': len(actual['windows']),
                      'sieve_limit': actual['sieve_limit']}, ensure_ascii=False))
    for row in actual['windows']:
        print(json.dumps({k: row[k] for k in ('X', 'source', 'fine_nodes',
              'closed_positive_green_square', 'length_band_energy_upper',
              'all_center_energy_upper', 'finite_K_upper')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
