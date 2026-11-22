#!/usr/bin/env python3
"""Certify the residual-order optimum using the original 44-node q mesh.

Only existing triangle and ancestor-envelope certificates are read. All nodal
values are reconstructed from their certified integer intervals; no source or
complete arithmetic road is recomputed.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT/'rh_joint_certificate'))
from certify_joint_energy import (A, B, DIGITS, ZERO, add, sub, scale, mul,
    positive, square, sqrt_interval, isum, record, energy, intersects,
    interval_from_record)


def tent(p, n):
    L, x, R = p
    if not L <= n <= R:
        return F(0)
    return F((n-L)*(R-x), R-L) if n <= x else F((x-L)*(R-n), R-L)


def imax(x, y):
    return max(x[0], y[0]), max(x[1], y[1])


def interpolate(values, nodes):
    out = {}
    for L, R in zip(nodes, nodes[1:]):
        for n in range(L, R+1):
            out[n] = add(scale(values[L], F(R-n, R-L)),
                         scale(values[R], F(n-L, R-L)))
    return out


def cartesian_tree(spatial_nodes, ranks):
    """Linear stack construction once the certified ranks are known."""
    tree = {n: {'left': None, 'right': None} for n in spatial_nodes}
    stack = []
    for n in spatial_nodes:
        last = None
        while stack and ranks[n] < ranks[stack[-1]]:
            last = stack.pop()
        if stack:
            tree[stack[-1]]['right'] = n
        if last is not None:
            tree[n]['left'] = last
        stack.append(n)
    return (stack[0] if stack else None), tree


def minimum_depth_optimal_tree(nodes, residuals):
    """Certify visibility under max(0,r), then exact minimax-height DP.

    A chord can fail between fine nodes at a zero crossing of r, so those
    additional breakpoints are checked by a denominator-free expression.
    """
    visibility, edge_records = {}, []
    for length in range(1, len(nodes)):
        for i in range(len(nodes)-length):
            j = i+length
            L, R = nodes[i], nodes[j]
            reason = None
            tests = []
            if length == 1:
                reason = 'original_fine_edge'
            elif residuals[L][1] <= 0 and residuals[R][1] <= 0:
                reason = 'both_endpoint_residuals_nonpositive'
            else:
                chord = {n: add(scale(residuals[L], F(R-n, R-L)),
                                scale(residuals[R], F(n-L, R-L)))
                         for n in nodes[i:j+1]}
                for n in nodes[i+1:j]:
                    tests.append(('fine_node', [n], sub(chord[n], positive(residuals[n]))))
                for u, v in zip(nodes[i:j], nodes[i+1:j+1]):
                    ru, rv = residuals[u], residuals[v]
                    if ru[1] < 0 < rv[0]:
                        gap = sub(mul(rv, chord[u]), mul(ru, chord[v]))
                        tests.append(('zero_crossing_positive_denominator', [u, v], gap))
                    elif rv[1] < 0 < ru[0]:
                        gap = sub(mul(ru, chord[v]), mul(rv, chord[u]))
                        tests.append(('zero_crossing_positive_denominator', [u, v], gap))
            violation = next((t for t in tests if t[2][0] > 0), None)
            if violation is not None:
                visible = False
                witness = {'kind': violation[0], 'nodes': violation[1],
                           'strict_positive_gap_or_numerator': record(violation[2])}
                if violation[0] == 'fine_node':
                    witness['integer_violation_node'] = violation[1][0]
                    witness['integer_violation_gap'] = record(violation[2])
                else:
                    u, v = violation[1]
                    ru_sum = sum(residuals[u])
                    rv_sum = sum(residuals[v])
                    approximate_crossing = F(u*rv_sum-v*ru_sum, rv_sum-ru_sum)
                    floor_crossing = approximate_crossing.numerator//approximate_crossing.denominator
                    integer_witness = None
                    for n in range(max(u, floor_crossing-1), min(v, floor_crossing+2)+1):
                        chord_value = add(scale(residuals[L], F(R-n, R-L)),
                                          scale(residuals[R], F(n-L, R-L)))
                        fine_value = add(scale(residuals[u], F(v-n, v-u)),
                                         scale(residuals[v], F(n-u, v-u)))
                        integer_gap = sub(chord_value, positive(fine_value))
                        if integer_gap[0] > 0:
                            integer_witness = (n, integer_gap)
                            break
                    assert integer_witness is not None, ('continuous_only_obstruction_requires_separate_discrete_DP', L, R)
                    witness['integer_violation_node'] = integer_witness[0]
                    witness['integer_violation_gap'] = record(integer_witness[1])
            else:
                assert reason is not None or all(t[2][1] <= 0 for t in tests), (L, R, tests)
                visible = True
                witness = {'kind': reason or 'all_envelope_breakpoints_certified_nonpositive'}
            visibility[(i, j)] = visible
            edge_records.append({'L': L, 'R': R, 'visible': visible, 'witness': witness})
    depth, split = {}, {}
    for length in range(1, len(nodes)):
        for i in range(len(nodes)-length):
            j = i+length
            if length == 1:
                depth[(i, j)] = 0
            elif not visibility[(i, j)]:
                depth[(i, j)] = None
            else:
                choices = [(1+max(depth[(i, k)], depth[(k, j)]), nodes[k], k)
                           for k in range(i+1, j)
                           if depth[(i, k)] is not None and depth[(k, j)] is not None]
                if choices:
                    best = min(choices)
                    depth[(i, j)], _, split[(i, j)] = best
                else:
                    depth[(i, j)] = None
    tree = {}

    def build(i, j):
        if j == i+1:
            return None
        k = split[(i, j)]
        x = nodes[k]
        tree[x] = {'left': build(i, k), 'right': build(k, j)}
        return x

    root = build(0, len(nodes)-1)
    return root, tree, {
        'minimum_depth': depth[(0, len(nodes)-1)],
        'all_chord_visibilities_decided_without_tolerance': True,
        'integer_and_continuous_chord_visibility_agree_on_this_input': True,
        'visibility_edges': edge_records,
        'minimax_depth_table': [{'L': nodes[i], 'R': nodes[j], 'minimum_depth': d,
                                'chosen_split': nodes[split[(i, j)]] if (i, j) in split else None}
                               for (i, j), d in depth.items()]}


def main():
    start = time.perf_counter()
    old_path = ROOT/'rh_triangle_certificate_20261122/dyadic_triangle_certificate.json'
    ancestor_path = ROOT/'rh_phase_dominance_20261122/ancestor_compression_certificate.json'
    old = json.loads(old_path.read_bytes())
    ancestor = json.loads(ancestor_path.read_bytes())
    road = old['roads']['q']
    assert (old['window']['A'], old['window']['B']) == (A, B)
    assert old['arithmetic']['denominator_power_of_10'] == DIGITS
    samples = {p['n']: interval_from_record(p['value'])
               for p in road['true_dyadic_endpoint_samples']}
    backbone = old['partition']['backbone']
    J = interpolate(samples, backbone)
    global_final_residual = {}
    global_recursive_Z = {}
    blocks = []
    new_packet_count = 0
    for old_block, mesh_block in zip(road['dyadic_blocks'], old['partition']['dyadic_blocks']):
        X, Y = old_block['X'], old_block['Y']
        assert (X, Y) == (mesh_block['X'], mesh_block['Y'])
        nodes = mesh_block['nodes']
        inside = nodes[1:-1]
        old_packets = [p for lev in old_block['levels'] for p in lev['packets']]
        r = {n: isum(scale(interval_from_record(p['signed_charge']),
                          tent((p['L'], p['x'], p['R']), n)) for p in old_packets)
             for n in nodes}
        assert r[X] == r[Y] == ZERO
        assert all(v[0] > 0 or v[1] < 0 for n, v in r.items() if n in inside)
        insertion_order = sorted(inside, key=lambda n: (r[n][0], n))
        assert all(r[left][1] < r[right][0]
                   for left, right in zip(insertion_order, insertion_order[1:]))
        ranks = {n: index for index, n in enumerate(insertion_order)}
        root, tree = cartesian_tree(inside, ranks)
        final_r = interpolate(r, nodes)
        new_packets = []
        visited = set()

        def visit(x, L, R, depth):
            if x is None:
                assert not any(L < n < R for n in inside)
                return {'S': {}, 'Z': {}, 'depth': depth-1}
            assert L < x < R and x not in visited
            visited.add(x)
            left = visit(tree[x]['left'], L, x, depth+1)
            right = visit(tree[x]['right'], x, R, depth+1)
            t = sub(scale(sub(r[x], r[L]), F(1, x-L)),
                    scale(sub(r[R], r[x]), F(1, R-x)))
            arr_s, arr_z = {}, {}
            for n in range(L, R+1):
                own = scale(t, tent((L, x, R), n))
                arr_s[n] = add(own, add(left['S'].get(n, ZERO), right['S'].get(n, ZERO)))
                arr_z[n] = positive(add(own, add(left['Z'].get(n, ZERO), right['Z'].get(n, ZERO))))
            new_packets.append({'L': L, 'x': x, 'R': R, 'depth': depth,
                'residual_value_rank': ranks[x], 'residual_at_peak': record(r[x]),
                'new_tree_signed_charge': record(t),
                'left_child_peak': tree[x]['left'], 'right_child_peak': tree[x]['right']})
            return {'S': arr_s, 'Z': arr_z, 'depth': max(depth, left['depth'], right['depth'])}

        rebuilt = visit(root, X, Y, 1)
        assert visited == set(inside)
        assert len(new_packets) == len(old_packets)
        new_packet_count += len(new_packets)
        for n in range(X, Y+1):
            assert intersects(rebuilt['S'][n], final_r[n])
            assert intersects(rebuilt['Z'][n], positive(final_r[n]))
            global_final_residual[n] = final_r[n]
            global_recursive_Z[n] = rebuilt['Z'][n]

        # Directly check every stage of the sorted insertion algorithm. The
        # phase inequalities follow analytically; these are enclosure checks.
        stage_max = {n: ZERO for n in range(X, Y+1)}
        stages = []
        for k in range(len(insertion_order)+1):
            selected = insertion_order[:k]
            selected_set = set(selected)
            stage = interpolate(r, sorted([X, Y]+selected))
            phase = 'below_initial_J' if k == 0 or r[insertion_order[k-1]][1] < 0 else 'below_final_I'
            if phase == 'below_initial_J':
                assert all(r[n][1] <= 0 for n in [X, Y]+selected)
                assert all(stage[n][1] <= 0 for n in range(X, Y+1))
            else:
                threshold = r[insertion_order[k-1]]
                assert threshold[0] > 0
                assert all(r[n][1] <= threshold[1] for n in [X, Y]+selected)
                assert all(threshold[1] < r[n][0] for n in inside if n not in selected_set)
                assert all(stage[n][1] < r[n][0] for n in inside if n not in selected_set)
                assert all(stage[n][0] <= final_r[n][1] for n in range(X, Y+1))
            for n in stage:
                stage_max[n] = imax(stage_max[n], stage[n])
            stages.append({'inserted_count': k, 'last_inserted': None if k == 0 else insertion_order[k-1],
                           'analytic_domination_phase': phase})
        assert all(intersects(stage_max[n], positive(final_r[n]))
                   and intersects(stage_max[n], rebuilt['Z'][n]) for n in range(X, Y+1))
        sorted_tree_packets = new_packets
        dp_root, dp_tree, dp_certificate = minimum_depth_optimal_tree(nodes, r)
        tree, new_packets, visited = dp_tree, [], set()
        dp_rebuilt = visit(dp_root, X, Y, 1)
        assert visited == set(inside)
        assert dp_rebuilt['depth'] == dp_certificate['minimum_depth']
        assert all(intersects(dp_rebuilt['S'][n], final_r[n])
                   and intersects(dp_rebuilt['Z'][n], positive(final_r[n]))
                   for n in range(X, Y+1))
        dp_certificate['optimal_tree_packets'] = sorted(new_packets, key=lambda p: (p['depth'], p['L']))
        e_opt = energy({n: add(J[n], positive(final_r[n])) for n in range(X, Y+1)}, X+1, Y-1, 'positive')
        e_signed = energy({n: add(J[n], final_r[n]) for n in range(X, Y+1)}, X+1, Y-1, 'positive')
        old_ancestor_block = next(b for b in ancestor['roads']['q']['blocks'] if b['X'] == X)
        e_old_z = interval_from_record(old_ancestor_block['interior_J_plus_envelope_positive_energies']['Z'])
        blocks.append({'X': X, 'Y': Y, 'fine_node_count': len(nodes),
            'interior_node_count': len(inside), 'old_tree_depth': len(old_block['levels']),
            'residual_order_tree_depth': rebuilt['depth'],
            'insertion_order': insertion_order,
            'negative_residual_node_count': sum(r[n][1] < 0 for n in inside),
            'positive_residual_node_count': sum(r[n][0] > 0 for n in inside),
            'residual_nodes': [{'n': n, 'residual': record(r[n])} for n in nodes],
            'all_adjacent_sorted_residual_intervals_strictly_separated': True,
            'new_tree_packets': sorted(sorted_tree_packets, key=lambda p: (p['depth'], p['L'])),
            'minimum_depth_among_all_optimal_envelope_trees': dp_certificate,
            'insertion_stage_checks': stages,
            'old_Z_interior_positive_energy': record(e_old_z),
            'optimal_tree_interior_positive_energy': record(e_opt),
            'signed_fine_interior_positive_energy': record(e_signed),
            'energy_reduction_from_old_Z': record(positive(sub(e_old_z, e_opt))),
            'unavoidable_initial_skeleton_energy_excess': record(positive(sub(e_opt, e_signed)))})

    assert new_packet_count == 38
    assert len(old['partition']['fine_nodes']) == 44
    E_opt = energy({n: add(J[n], positive(global_final_residual[n])) for n in range(A, B+1)}, A+1, B-1, 'positive')
    E_recursive = energy({n: add(J[n], global_recursive_Z[n]) for n in range(A, B+1)}, A+1, B-1, 'positive')
    E_signed = energy({n: add(J[n], global_final_residual[n]) for n in range(A, B+1)}, A+1, B-1, 'positive')
    E_excess_direct = isum(scale(positive(sub(square(positive(J[n])),
                                           square(positive(add(J[n], global_final_residual[n]))))), F(1, n*n))
                          for n in range(A+1, B))
    assert intersects(E_opt, E_recursive)
    assert intersects(E_signed, interval_from_record(road['energies']['fine_interpolant_positive_energy']))
    assert intersects(sub(E_opt, E_signed), E_excess_direct)
    remainder = interval_from_record(road['energies']['fine_local_positive_remainder_energy'])
    endpoints = interval_from_record(road['energies']['true_two_endpoint_direct_energy'])
    budget = add(square(add(sqrt_interval(E_opt), sqrt_interval(remainder))), endpoints)
    budget_recursive = add(square(add(sqrt_interval(E_recursive), sqrt_interval(remainder))), endpoints)
    assert intersects(budget, budget_recursive)
    old_budgets = ancestor['roads']['q']['closed_squared_budgets']
    assert budget[1] < interval_from_record(old_budgets['Z'])[0]
    assert interval_from_record(old_budgets['S'])[1] < budget[0]
    output = {
        'schema': 'EM_OPTIMAL_RESIDUAL_ORDER_TREE_V1', 'status': 'PASS',
        'scope': 'All legal binary insertion trees on the same fixed fine mesh and true dyadic skeleton; finite actual q certificate only.',
        'science_freeze': '9fc068244e4f1117f1e75df5eb0285c6697d21d7',
        'window': old['window'],
        'arithmetic': {'denominator_power_of_10': DIGITS, 'method': 'outward integer intervals; exact rational interpolation'},
        'inputs': [{'path': str(p.relative_to(ROOT)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
                   for p in [old_path, ancestor_path, ROOT/'rh_joint_certificate/certify_joint_energy.py',
                             ROOT/'rh_correlation_rational/certify_matched_nodes.py']],
        'fine_node_count': 44, 'dyadic_block_count': 5, 'new_tree_packet_count': new_packet_count,
        'optimality_identity': 'J+Z = max(J,I_Pi q); hence (J+Z)_+ = max(J_+,(I_Pi q)_+)',
        'exact_signed_energy_gap': 'E_opt-E_signed = sum_n (J_+^2-(I_Pi q)_+^2)_+/n^2',
        'interior_optimal_positive_envelope_energy': record(E_opt),
        'interior_recursive_new_tree_positive_envelope_energy': record(E_recursive),
        'interior_signed_fine_positive_energy': record(E_signed),
        'unavoidable_initial_skeleton_energy_excess': record(E_excess_direct),
        'fine_positive_remainder_energy_unchanged': record(remainder),
        'true_two_endpoint_energy_unchanged': record(endpoints),
        'closed_optimal_tree_budget': record(budget),
        'closed_actual_positive_energy_unchanged': road['energies']['actual_positive_energy_closed'],
        'prior_closed_budgets': old_budgets,
        'strict_separations': {
            'optimal_order_upper_less_than_old_Z_lower': budget[1] < interval_from_record(old_budgets['Z'])[0],
            'signed_budget_upper_less_than_optimal_order_lower': interval_from_record(old_budgets['S'])[1] < budget[0]},
        'blocks': blocks,
        'checks': {
            'same_44_fine_nodes_and_6_true_skeleton_nodes': True,
            'all_38_new_tree_charges_recomputed_from_same_signed_samples': True,
            'all_residual_sort_orders_certified_by_strict_interval_separation': True,
            'every_insertion_stage_obeys_analytic_two_phase_domination': True,
            'all_integer_new_tree_S_final_interpolation_consistency': True,
            'all_integer_new_tree_Z_direct_positive_residual_consistency': True,
            'all_integer_sequential_prefix_max_consistency': True,
            'all_chord_visibilities_certified_at_fine_nodes_and_zero_crossings': True,
            'minimum_depth_optimal_tree_DP_exhausts_all_legal_splits': True,
            'all_integer_minimum_depth_tree_Z_direct_positive_residual_consistency': True,
            'analytic_optimality_not_inferred_from_interval_overlap': True,
            'no_complete_arithmetic_road_recomputed': True,
            'same_author_check_not_independent_review': True},
        'cost': {'wall_seconds': time.perf_counter()-start, 'complete_roads_recomputed': 0},
    }
    path = OUT/'optimal_tree_order_certificate.json'
    path.write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n')
    print('closed optimal order budget', output['closed_optimal_tree_budget']['upper'])
    print('optimal interior energy', output['interior_optimal_positive_envelope_energy']['upper'])
    print('unavoidable skeleton excess', output['unavoidable_initial_skeleton_energy_excess']['upper'])
    for b in blocks:
        print('block', b['X'], 'depth', b['old_tree_depth'], '->', b['residual_order_tree_depth'],
              'minimum optimal depth', b['minimum_depth_among_all_optimal_envelope_trees']['minimum_depth'],
              'order', b['insertion_order'], 'gain', b['energy_reduction_from_old_Z']['lower'])
    print('PASS', path, 'seconds', output['cost']['wall_seconds'])


if __name__ == '__main__':
    main()
