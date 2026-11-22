#!/usr/bin/env python3
"""New strict fine-remainder bounds on the existing full road and fine mesh.

The existing road cache is an input; this script never regenerates that road.
All arithmetic uses outward integer intervals with denominator 10**60.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import pickle
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'rh_joint_certificate'))
from certify_joint_energy import (
    A, B, SCALE, DIGITS, ZERO, Elementary, linear_sieve, rat, add, sub, neg,
    scale, mul, divide, positive, square, sqrt_interval, isum, record,
    energy, cross, green_apply, intersects, interval_from_record,
)


def absolute(v):
    return (0 if v[0] <= 0 <= v[1] else min(abs(v[0]), abs(v[1])),
            max(abs(v[0]), abs(v[1])))


def main():
    cache_path = ROOT / 'rh_joint_certificate/_scratch_arrays.pkl'
    if not cache_path.exists():
        raise SystemExit('First reproduce rh_joint_certificate/certify_joint_energy.py to create its road cache.')
    mesh_path = ROOT / 'rh_triangle_certificate_20261122/dyadic_triangle_certificate.json'
    reference_path = ROOT / 'rh_reference_certificate_20261122/reference_split_certificate.json'
    cache = pickle.loads(cache_path.read_bytes())
    mesh = json.loads(mesh_path.read_text())
    reference = json.loads(reference_path.read_text())
    assert cache['A'] == A and cache['B'] == B and cache['DIGITS'] == DIGITS
    q, D, kappa, f = (cache[k] for k in ['q', 'D', 'kappa', 'f'])
    el = Elementary()
    spf, _ = linear_sieve(B)
    Lambda = [ZERO] * (B + 1)
    prime_mask = [False] * (B + 1)
    power_mask = [False] * (B + 1)
    for p in range(2, B + 1):
        if spf[p] != p:
            continue
        prime_mask[p] = True
        power = p
        while power <= B:
            Lambda[power] = el.log_integer(p)
            if power != p:
                power_mask[power] = True
            power *= p
    e = [sub(D[n], Lambda[n]) for n in range(B + 1)]
    epsilon = (0, max(absolute(v)[1] for v in e[1:]))
    epsilon_bound = interval_from_record(reference['pointwise_matching']['eta_B'])
    assert epsilon[1] <= epsilon_bound[1]
    K = scale(el.log_integer(2), 2)
    old_M = add(add(K, el.log_integer(B)), epsilon_bound)
    sources = {
        'kappa': [ZERO] * (B + 1),
        'prime': [ZERO] * (B + 1),
        'higher_prime_power': [ZERO] * (B + 1),
        'matching_error': [ZERO] * (B + 1),
    }
    for n in range(1, B + 1):
        sources['kappa'][n] = scale(kappa[n], F(1, n))
        sources['prime'][n] = scale(Lambda[n], F(1, n)) if prime_mask[n] else ZERO
        sources['higher_prime_power'][n] = scale(Lambda[n], F(1, n)) if power_mask[n] else ZERO
        sources['matching_error'][n] = scale(e[n], F(1, n))
    potentials = {k: [ZERO] * (B + 1) for k in sources}
    actual_P = [ZERO] * (B + 1)
    totals = {k: ZERO for k in ['old_pointwise', 'source_l2', 'source_l1',
                                'prime_mass', 'power_mass', 'bt_prime_mass',
                                'parabolic_unit_cost']}
    all_cells = []
    blocks = []
    identity_count = 0
    for block in mesh['partition']['dyadic_blocks']:
        X, Y, nodes = block['X'], block['Y'], block['nodes']
        block_sum = {k: ZERO for k in totals}
        for L, R in zip(nodes, nodes[1:]):
            h = R - L
            if h == 1:
                continue
            ab = (h * h) // 4
            row_max = F(ab, 2)
            column_sq = F(ab * (2 * ab + 1), 6 * h)
            assert column_sq <= F(h ** 3, 32)
            for key in sources:
                value = green_apply(sources[key], L, R)
                potentials[key][L:R+1] = value[L:R+1]
            for n in range(L + 1, R):
                affine = add(scale(q[L], F(R - n, h)), scale(q[R], F(n - L, h)))
                actual_P[n] = sub(q[n], affine)
                rhs = sub(sub(sub(potentials['kappa'][n], potentials['prime'][n]),
                              potentials['higher_prime_power'][n]), potentials['matching_error'][n])
                assert intersects(actual_P[n], rhs)
                identity_count += 1
            f_square_mass = isum(square(f[n]) for n in range(L+1, R))
            f_abs_mass = isum(absolute(f[n]) for n in range(L+1, R))
            prime_mass = isum(Lambda[n] for n in range(L+1, R) if prime_mask[n])
            power_mass = isum(Lambda[n] for n in range(L+1, R) if power_mask[n])
            bt_prime_mass = divide(scale(el.log_integer(Y), 2*h), el.log_integer(h))
            assert prime_mass[1] <= bt_prime_mass[0]
            unit = rat(F(h**5-h, 120*X**4))
            bounds = {
                'old_pointwise': mul(square(old_M), unit),
                'source_l2': scale(f_square_mass, row_max**2 / X**2),
                'source_l1': scale(square(f_abs_mass), column_sq / X**2),
                'prime_mass': scale(square(prime_mass), column_sq / X**4),
                'power_mass': scale(square(power_mass), column_sq / X**4),
                'bt_prime_mass': scale(square(bt_prime_mass), column_sq / X**4),
                'parabolic_unit_cost': unit,
            }
            actual_energy = energy(actual_P, L+1, R-1)
            for key in ['old_pointwise', 'source_l2', 'source_l1']:
                assert actual_energy[1] <= bounds[key][0]
            for key, value in bounds.items():
                totals[key] = add(totals[key], value)
                block_sum[key] = add(block_sum[key], value)
            all_cells.append({'X': X, 'L': L, 'R': R, 'h': h,
                'green_row_sum_max': str(row_max), 'green_column_square_max': str(column_sq),
                'source_square_mass': record(f_square_mass),
                'source_absolute_mass': record(f_abs_mass),
                'prime_log_mass': record(prime_mass), 'higher_power_log_mass': record(power_mass),
                'bt_prime_log_mass_bound': record(bt_prime_mass),
                'actual_remainder_energy': record(actual_energy),
                'bounds': {k: record(v) for k,v in bounds.items()}})
        blocks.append({'X': X, 'Y': Y, 'cell_count':len(nodes)-1,
                       'bounds': {k:record(v) for k,v in block_sum.items()}})
    total_positive = energy(actual_P, mode='positive')
    total_negative = energy([neg(v) for v in actual_P], mode='positive')
    total_actual = energy(actual_P)
    old_positive = interval_from_record(mesh['roads']['q']['energies']['fine_local_positive_remainder_energy'])
    assert intersects(old_positive, total_positive)
    positive_bound = mul(square(add(K, epsilon_bound)), totals['parabolic_unit_cost'])
    error_root = mul(epsilon_bound, sqrt_interval(totals['parabolic_unit_cost']))
    negative_mass_root = add(add(sqrt_interval(totals['prime_mass']),
                                 sqrt_interval(totals['power_mass'])), error_root)
    negative_sieve_root = add(add(sqrt_interval(totals['bt_prime_mass']),
                                  sqrt_interval(totals['power_mass'])), error_root)
    assert total_positive[1] <= positive_bound[0]
    assert total_negative[1] <= square(negative_mass_root)[0]
    component_energies = {k: energy(v) for k,v in potentials.items()}
    Btotal = [add(potentials['prime'][n], potentials['higher_prime_power'][n]) for n in range(B+1)]
    reference_P = [sub(potentials['kappa'][n], Btotal[n]) for n in range(B+1)]
    ref_diagonal = add(component_energies['kappa'], energy(Btotal))
    ref_cross = scale(cross(potentials['kappa'], Btotal), -2)
    ref_energy = energy(reference_P)
    assert intersects(add(ref_diagonal, ref_cross), ref_energy)
    output = {
        'status': 'PASS',
        'scope': 'Author strict finite certificate; fixed complete road, old mesh, no road regeneration, no RH proof.',
        'window': {'A':A, 'B':B, 'fine_cells':len(all_cells), 'interior_identity_checks':identity_count},
        'arithmetic': {'denominator_power_of_10':DIGITS, 'method':'outward integer intervals and exact rational geometry'},
        'inputs': [{'path':str(p.relative_to(ROOT)), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
                   for p in [mesh_path, reference_path, ROOT/'rh_joint_certificate/certify_joint_energy.py',
                             ROOT/'rh_correlation_rational/certify_matched_nodes.py']],
        'cache': {'path':str(cache_path.relative_to(ROOT)), 'sha256':hashlib.sha256(cache_path.read_bytes()).hexdigest(),
                  'full_road_recomputed_this_run':False},
        'external_theorem': {'authors':'H. L. Montgomery and R. C. Vaughan', 'title':'The large sieve',
            'publication':'Mathematika 20 (1973), 119-134', 'location':'Theorem 2, printed page 121, equation (1.12)',
            'url':'https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf',
            'inequality':'pi(M+N)-pi(M)<=2N/log(N), M>0, N>1'},
        'matching': {'epsilon_D_actual_upper':record(epsilon), 'direct_interpolation_epsilon_bound':record(epsilon_bound)},
        'actual': {'positive_energy':record(total_positive), 'negative_energy':record(total_negative),
                   'full_energy':record(total_actual)},
        'bounds': {**{k:record(v) for k,v in totals.items()},
                   'positive_parabolic':record(positive_bound),
                   'negative_actual_mass':record(square(negative_mass_root)),
                   'negative_sieve_with_actual_power_mass':record(square(negative_sieve_root)),
                   'full_two_sided_actual_mass':record(add(positive_bound,square(negative_mass_root)))},
        'component_energies': {k:record(v) for k,v in component_energies.items()},
        'reference_fine_cross': {'diagonal':record(ref_diagonal), 'signed_cross':record(ref_cross),
                                 'full_reference_energy':record(ref_energy),
                                 'identity_intervals_intersect':True},
        'blocks':blocks, 'cells':all_cells,
        'checks': {'every_cell_l2_and_l1_bound_strictly_above_actual_energy':True,
                   'every_cell_prime_mass_below_source_sieve_bound':True,
                   'all_integer_green_decomposition_intervals_intersect':True,
                   'old_positive_remainder_interval_reused_and_matched':True},
    }
    path = OUT/'arithmetic_fine_bounds_certificate.json'
    path.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':output['status'], 'window':output['window'], 'actual':output['actual'],
          'bounds':output['bounds'], 'reference_fine_cross':output['reference_fine_cross'],
          'output_bytes':path.stat().st_size},ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
