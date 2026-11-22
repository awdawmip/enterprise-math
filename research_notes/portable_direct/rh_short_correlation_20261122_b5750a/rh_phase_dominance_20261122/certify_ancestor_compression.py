#!/usr/bin/env python3
"""Strict ancestor-envelope budgets from the existing 38-packet certificate.

No arithmetic road, source population, endpoint, or fine remainder is rebuilt.
The original certified integer intervals are the only numerical data inputs.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'rh_joint_certificate'))
from certify_joint_energy import (A, B, DIGITS, SCALE, ZERO, add, sub, neg,
    scale, square, positive, sqrt_interval, isum, record, energy,
    intersects, interval_from_record)


def imax(xs):
    return max(x[0] for x in xs), max(x[1] for x in xs)


def imin(x, y):
    return min(x[0], y[0]), min(x[1], y[1])


def tent(p, n):
    L, x, R = p
    if not L <= n <= R:
        return F(0)
    if n <= x:
        return F((n-L)*(R-x), R-L)
    return F((x-L)*(R-n), R-L)


def positive_energy(values, first, last):
    return energy(values, first, last, 'positive')


def weighted_area(values, first, last):
    return isum(scale(values[n], F(1, n*n)) for n in range(first, last+1))


def dirichlet_energy(values, first, last):
    return isum(square(sub(values[n], values[n-1])) for n in range(first+1, last+1))


def main():
    started = time.perf_counter()
    source_path = ROOT / 'rh_triangle_certificate_20261122/dyadic_triangle_certificate.json'
    source = json.loads(source_path.read_bytes())
    assert (source['window']['A'], source['window']['B']) == (A, B)
    assert source['arithmetic']['denominator_power_of_10'] == DIGITS
    output = {
        'schema': 'EM_SIGNED_ANCESTOR_ENVELOPE_V1', 'status': 'PASS',
        'scope': 'Finite fixed-tree envelope comparison only; same native roads, real skeleton, fine positive remainder, and true closed endpoints.',
        'science_freeze': '9fc068244e4f1117f1e75df5eb0285c6697d21d7',
        'window': source['window'],
        'arithmetic': {'denominator_power_of_10': DIGITS,
                       'method': 'outward integer intervals; exact rational geometry'},
        'inputs': [{'path': str(p.relative_to(ROOT)),
                    'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
                   for p in (source_path, ROOT/'rh_joint_certificate/certify_joint_energy.py',
                             ROOT/'rh_correlation_rational/certify_matched_nodes.py')],
        'formulas': {
            'capacity': 'a_p = positive(t_p + max(0, lambda_l*a_l, lambda_r*a_r))',
            'recursive_envelope': 'Z_p = positive(t_p*T_p + Z_l + Z_r)',
            'clipped_single_tent': 'F_root = min(U_root, a_root*T_root)',
            'hierarchy': 'positive(S_p) <= Z_p <= min(U_p,a_p*T_p) <= U_p',
            'local_absorption': 'A_p = min(negative_part(t_p)*T_p, Z_l+Z_r); U_root-Z_root = sum_p A_p',
            'dirichlet_cost': 'E(Z_root) = sum_p tau_p*positive(t_p)^2 - sum_{t_p<0} dissipation_p; every dissipation_p is nonnegative',
            'closed_budget': '(sqrt(interior_energy(positive(J+envelope))) + sqrt(original_fine_positive_remainder_energy))^2 + original_true_two_endpoint_energy',
        },
        'roads': {},
    }
    for road_name, road in source['roads'].items():
        samples = {p['n']: interval_from_record(p['value'])
                   for p in road['true_dyadic_endpoint_samples']}
        backbone = source['partition']['backbone']
        J = [ZERO]*(B+1)
        for L, R in zip(backbone, backbone[1:]):
            for n in range(L, R+1):
                J[n] = add(scale(samples[L], F(R-n, R-L)),
                           scale(samples[R], F(n-L, R-L)))
        global_arrays = {name: [ZERO]*(B+1) for name in ('U', 'F', 'Z', 'S')}
        blocks = []
        packet_total = 0
        positive_total = negative_total = 0
        all_packet_records = []
        for block in road['dyadic_blocks']:
            X, Y = block['X'], block['Y']
            packets = {}
            for level in block['levels']:
                for p in level['packets']:
                    key = (p['L'], p['R'])
                    assert key not in packets
                    packets[key] = {'triple': (p['L'], p['x'], p['R']),
                                    'level': level['level'],
                                    't': interval_from_record(p['signed_charge'])}
            visited = set()
            results = {}

            def visit(key):
                assert key not in visited
                visited.add(key)
                p = packets[key]
                L, x, R = p['triple']
                assert L < x < R
                children = []
                for side, child_key in [('left', (L, x)), ('right', (x, R))]:
                    if child_key in packets:
                        child = visit(child_key)
                        y = child['triple'][1]
                        lam = (F((R-L)*(x-y), (x-L)*(R-x)) if side == 'left'
                               else F((R-L)*(y-x), (x-L)*(R-x)))
                        assert lam == tent(child['triple'], y)/tent(p['triple'], y)
                        # Exact check of the sharp geometry inequality.
                        assert all(tent(child['triple'], n) <= lam*tent(p['triple'], n)
                                   for n in range(child_key[0], child_key[1]+1))
                        children.append((side, lam, child))
                candidates = [ZERO] + [scale(c['a'], lam) for _, lam, c in children]
                child_cap = imax(candidates)
                a = positive(add(p['t'], child_cap))
                winner = None
                if child_cap[1] == 0:
                    winner = 0
                else:
                    for index, candidate in enumerate(candidates):
                        if candidate[0] > max(v[1] for j, v in enumerate(candidates) if j != index):
                            winner = index
                            break
                active_path = None
                if a[1] == 0:
                    active_path = []
                elif a[0] > 0 and winner is not None:
                    tail = [] if winner == 0 else children[winner-1][2]['active_path']
                    if tail is not None:
                        active_path = [list(p['triple'])]+tail
                arrays = {name: {} for name in ('U', 'Z', 'S', 'absorbed', 'total_absorbed')}
                for n in range(L, R+1):
                    T = tent(p['triple'], n)
                    child_z = isum(c['arrays']['Z'].get(n, ZERO) for _, _, c in children)
                    arrays['U'][n] = add(scale(positive(p['t']), T),
                        isum(c['arrays']['U'].get(n, ZERO) for _, _, c in children))
                    arrays['S'][n] = add(scale(p['t'], T),
                        isum(c['arrays']['S'].get(n, ZERO) for _, _, c in children))
                    arrays['Z'][n] = positive(add(scale(p['t'], T), child_z))
                    arrays['absorbed'][n] = imin(scale(positive(neg(p['t'])), T), child_z)
                    arrays['total_absorbed'][n] = add(arrays['absorbed'][n],
                        isum(c['arrays']['total_absorbed'].get(n, ZERO) for _, _, c in children))
                    # Enclosure consistency checks; the inequalities themselves
                    # are proved in the companion note, not by interval overlap.
                    assert positive(arrays['S'][n])[0] <= arrays['Z'][n][1]
                    assert arrays['Z'][n][0] <= arrays['U'][n][1]
                    assert arrays['Z'][n][0] <= scale(a, T)[1]
                    assert intersects(sub(arrays['U'][n], arrays['Z'][n]),
                                      arrays['total_absorbed'][n])
                ez = dirichlet_energy(arrays['Z'], L, R)
                child_ez = isum(c['ez'] for _, _, c in children)
                epacket = scale(square(positive(p['t'])), F((x-L)*(R-x), R-L))
                if p['t'][0] > 0:
                    assert intersects(ez, add(epacket, child_ez))
                    dissipation = ZERO
                else:
                    assert p['t'][1] < 0
                    assert ez[0] <= child_ez[1]
                    dissipation = positive(sub(child_ez, ez))
                etotal_positive = add(epacket, isum(c['epos'] for _, _, c in children))
                dtotal = add(dissipation, isum(c['dtotal'] for _, _, c in children))
                assert intersects(ez, sub(etotal_positive, dtotal))
                rec = {'packet': list(p['triple']), 'local_level': p['level'],
                       'signed_charge': record(p['t']), 'capacity': record(a),
                       'capacity_state': 'zero' if a[1] == 0 else ('positive' if a[0] > 0 else 'unresolved'),
                       'capacity_maximizing_prefix_certified': active_path,
                       'children': [{'side': side, 'packet': list(c['triple']),
                                     'lambda_exact': str(lam)} for side, lam, c in children],
                       'local_absorbed_weighted_area': record(weighted_area(arrays['absorbed'], L, R)),
                       'local_absorbed_weighted_energy': record(energy(arrays['absorbed'], L, R)),
                       'subtree_Z_dirichlet_energy': record(ez),
                       'local_negative_ancestor_dirichlet_dissipation': record(dissipation)}
                out = {**p, 'a': a, 'arrays': arrays, 'record': rec,
                       'active_path': active_path, 'ez': ez,
                       'epos': etotal_positive, 'dtotal': dtotal}
                results[key] = out
                return out

            root = visit((X, Y))
            assert visited == set(packets)
            packet_total += len(packets)
            positive_total += sum(p['t'][0] > 0 for p in packets.values())
            negative_total += sum(p['t'][1] < 0 for p in packets.values())
            assert all(p['t'][0] > 0 or p['t'][1] < 0 for p in packets.values())
            env = {name: {} for name in ('U', 'F', 'Z', 'S')}
            for n in range(X, Y+1):
                for name in ('U', 'Z', 'S'):
                    env[name][n] = root['arrays'][name][n]
                env['F'][n] = imin(env['U'][n], scale(root['a'], tent(root['triple'], n)))
                for name in env:
                    global_arrays[name][n] = env[name][n]
                assert env['Z'][n][0] <= env['F'][n][1]
            energies = {name: positive_energy({n: add(J[n], env[name][n])
                                               for n in range(X, Y+1)}, X+1, Y-1)
                        for name in env}
            no_absorption = all(root['arrays']['total_absorbed'][n] == ZERO for n in range(X, Y+1))
            F_equals_U = all(env['U'][n][1] <= scale(root['a'], tent(root['triple'], n))[0]
                             for n in range(X, Y+1))
            gains = {name: positive(sub(energies['U'], energies[name])) for name in ('F', 'Z')}
            if no_absorption:
                gains['Z'] = ZERO
            if F_equals_U:
                gains['F'] = ZERO
            node_records = [results[key]['record'] for key in sorted(results)]
            all_packet_records.extend(node_records)
            blocks.append({'X': X, 'Y': Y, 'packet_count': len(packets),
                'root_packet': list(root['triple']), 'root_capacity': record(root['a']),
                'root_capacity_state': root['record']['capacity_state'],
                'root_capacity_maximizing_prefix_certified': root['active_path'],
                'Z_equals_U_by_exact_zero_local_absorption': no_absorption,
                'F_equals_U_by_certified_pointwise_order': F_equals_U,
                'interior_J_plus_envelope_positive_energies': {k: record(v) for k, v in energies.items()},
                'interior_energy_reduction_from_U': {k: record(v) for k, v in gains.items()},
                'weighted_removed_envelope_area': record(weighted_area(root['arrays']['total_absorbed'], X, Y)),
                'positive_packet_dirichlet_energy': record(root['epos']),
                'Z_dirichlet_energy': record(root['ez']),
                'total_negative_ancestor_dirichlet_dissipation': record(root['dtotal']),
                'nodes': node_records})

        assert packet_total == len(source['partition']['fine_nodes'])-len(backbone) == 38
        assert all(global_arrays[k][n] == ZERO for k in global_arrays for n in backbone)
        old = road['energies']
        remainder = interval_from_record(old['fine_local_positive_remainder_energy'])
        endpoints = interval_from_record(old['true_two_endpoint_direct_energy'])
        actual = interval_from_record(old['actual_positive_energy_closed'])
        energies = {name: positive_energy([add(J[n], arr[n]) for n in range(B+1)], A+1, B-1)
                    for name, arr in global_arrays.items()}
        assert intersects(energies['U'], interval_from_record(old['J_plus_positive_local_packets_positive_energy']))
        assert intersects(energies['S'], interval_from_record(old['fine_interpolant_positive_energy']))
        budgets = {name: add(square(add(sqrt_interval(v), sqrt_interval(remainder))), endpoints)
                   for name, v in energies.items()}
        assert intersects(budgets['U'], interval_from_record(old['closed_squared_budget_J_plus_local_packets_plus_actual_local_remainder']))
        assert budgets['Z'][1] < budgets['U'][0]
        assert budgets['Z'][1] < budgets['F'][0]
        assert budgets['F'][1] < budgets['U'][0]
        assert actual[1] < budgets['S'][0] <= budgets['Z'][1]
        sorted_absorption = sorted(all_packet_records,
            key=lambda p: int(p['local_absorbed_weighted_area']['integer_bounds'][1]), reverse=True)
        out_road = {
            'packet_count': packet_total, 'positive_packet_count': positive_total,
            'negative_packet_count': negative_total,
            'positive_local_absorption_packet_count': sum(
                int(p['local_absorbed_weighted_area']['integer_bounds'][0]) > 0
                for p in all_packet_records),
            'closed_actual_positive_energy_unchanged': record(actual),
            'fine_positive_remainder_energy_unchanged': record(remainder),
            'true_two_endpoint_energy_unchanged': record(endpoints),
            'interior_J_plus_envelope_positive_energies': {k: record(v) for k, v in energies.items()},
            'closed_squared_budgets': {k: record(v) for k, v in budgets.items()},
            'strict_separations': {
                'F_upper_less_than_U_lower': budgets['F'][1] < budgets['U'][0],
                'Z_upper_less_than_F_lower': budgets['Z'][1] < budgets['F'][0],
                'signed_interpolation_upper_less_than_Z_lower': budgets['S'][1] < budgets['Z'][0],
                'actual_upper_less_than_signed_budget_lower': actual[1] < budgets['S'][0]},
            'blocks': blocks,
            'largest_local_absorptions_by_weighted_removed_area': sorted_absorption[:6],
            'checks': {
                'each_old_packet_visited_once': True,
                'sharp_child_tent_ratio_verified_exactly_at_every_integer': True,
                'all_skeleton_correction_values_exactly_zero': True,
                'original_U_energy_reproduced_as_interval_consistency_check': True,
                'original_fine_interpolant_energy_reproduced_as_interval_consistency_check': True,
                'pointwise_envelope_and_absorption_identity_enclosure_consistency': True,
                'inequality_proofs_are_analytic_not_interval_overlap_claims': True,
                'no_full_road_recomputed': True,
                'same_author_check_not_independent_review': True}}
        output['roads'][road_name] = out_road
    output['cost'] = {'wall_seconds': time.perf_counter()-started,
                      'arithmetic_roads_recomputed': 0, 'old_packets_per_road': 38}
    target = OUT / 'ancestor_compression_certificate.json'
    target.write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n')
    for name, r in output['roads'].items():
        print(name, {k: v['upper'] for k, v in r['closed_squared_budgets'].items()})
        print('block capacities', [(b['X'], b['root_capacity']['upper'],
                                    b['root_capacity_state']) for b in r['blocks']])
        print('block Z energy reductions', [(b['X'], b['interior_energy_reduction_from_U']['Z']['lower'])
                                              for b in r['blocks']])
        print('top absorptions', [(p['packet'], p['local_absorbed_weighted_area']['lower'])
                                  for p in r['largest_local_absorptions_by_weighted_removed_area']])
    print('PASS', target, 'seconds', output['cost']['wall_seconds'])


if __name__ == '__main__':
    main()
