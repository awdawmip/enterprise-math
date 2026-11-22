#!/usr/bin/env python3
"""Strict actual-road dyadic-local triangle and skeleton certificate.

Run from any directory.  Reuses (or deterministically regenerates) the full-road
60-decimal outward-interval cache.  Every integer in the closed window remains
in the observation.  No asymptotic statement is inferred from this certificate.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import pickle
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'rh_joint_certificate'))
from certify_joint_energy import (  # noqa: E402
    A, B, H, DIGITS, SCALE, ZERO, ONE, add, sub, neg, scale, mul,
    rat, square, positive, sqrt_interval, isum, record, energy,
    green_apply, intersects, floor_root, linear_sieve, cross, divide,
)

OUT = Path(__file__).resolve().parent
CACHE = ROOT / 'rh_joint_certificate/_scratch_arrays.pkl'
BASE_CERT = ROOT / 'rh_joint_certificate/joint_energy_certificate.json'


def phi(L, x, R, n):
    return F(n-L, x-L) if n <= x else F(R-n, R-x)


def T(L, x, R, n):
    return F((n-L)*(R-x), R-L) if n <= x else F((x-L)*(R-n), R-L)


def abs_interval(v):
    if v[0] >= 0:
        return v
    if v[1] <= 0:
        return neg(v)
    return 0, max(-v[0], v[1])


def harmonic_kernel(L, x, R, d, harmonic):
    """Independent closed form of sum_{d|n} Phi(n)/n, x counted left."""
    a, b = x-L, R-x
    l, u, v = L//d, x//d, (R-1)//d
    if l == v:
        return ZERO
    left = sub(rat(F(u-l, a)), scale(sub(harmonic[u],harmonic[l]), F(L,a*d)))
    right = sub(scale(sub(harmonic[v],harmonic[u]), F(R,b*d)), rat(F(v-u,b)))
    return add(left,right)


def interpolate(values, cuts):
    out = [ZERO]*(B+1)
    for L, R in zip(cuts, cuts[1:]):
        for n in range(L, R+1):
            out[n] = add(scale(values[L], F(R-n, R-L)),
                         scale(values[R], F(n-L, R-L)))
    return out


def charges_at(values, cuts):
    slopes = [scale(sub(values[R], values[L]), F(1, R-L))
              for L, R in zip(cuts, cuts[1:])]
    return {cuts[j]: sub(slopes[j-1], slopes[j])
            for j in range(1, len(cuts)-1)}


def dyadic_grid():
    backbone = [A]
    while backbone[-1] < B:
        backbone.append(min(B, 2*backbone[-1]))
    blocks = []
    for X, Y in zip(backbone, backbone[1:]):
        h = floor_root(X**3, 4)
        nodes = list(range(X, Y, h)) + [Y]
        assert nodes[0] == X and nodes[-1] == Y
        blocks.append({'X': X, 'Y': Y, 'fine_step': h, 'nodes': nodes})
    cuts = sorted(set(n for block in blocks for n in block['nodes']))
    return backbone, blocks, cuts


def condense_block(nodes, original):
    mass = {x: (original[x] if x not in (nodes[0], nodes[-1]) else ZERO)
            for x in nodes}
    current = list(nodes)
    levels = []
    while len(current) > 2:
        retained = current[::2]
        if retained[-1] != current[-1]:
            retained.append(current[-1])
        keep = set(retained)
        packets = []
        for k in range(1, len(current)-1):
            x = current[k]
            if x in keep:
                continue
            L, R = current[k-1], current[k+1]
            t = mass[x]
            packets.append((L, x, R, t))
            mass[L] = add(mass[L], scale(t, F(R-x, R-L)))
            mass[R] = add(mass[R], scale(t, F(x-L, R-L)))
            del mass[x]
        assert all(a[2] <= b[0] for a, b in zip(packets, packets[1:]))
        levels.append(packets)
        current = retained
    return levels, {x: mass[x] for x in current}


def main():
    started = time.perf_counter()
    road_recomputations = 0
    if not CACHE.exists():
        subprocess.run([sys.executable,
                        str(ROOT/'rh_joint_certificate/certify_joint_energy.py')], check=True)
        road_recomputations = 1
    data = pickle.loads(CACHE.read_bytes())
    assert (data['A'], data['B'], data['H'], data['SCALE']) == (A, B, H, SCALE)
    assert data['DIGITS'] == DIGITS == 60
    sigma = isum(scale(data['c'][d], F(1, d)) for d in range(1, H+1))
    harmonic = [ZERO]
    for n in range(1,B+1):
        harmonic.append(add(harmonic[-1],rat(F(1,n))))

    # Reconstruct every actual arithmetic coefficient, not an envelope or a
    # prime-only subsequence, then check the exact corrected source everywhere.
    _, mu = linear_sieve(B)
    full_c = [ZERO]*(B+1)
    Dmk = [sub(data['D'][n], data['kappa'][n]) for n in range(B+1)]
    mobius_additions = 0
    for d in range(1, B+1):
        if mu[d]:
            for n in range(d, B+1, d):
                full_c[n] = add(full_c[n], scale(Dmk[n//d], mu[d]))
                mobius_additions += 1
    assert all(intersects(full_c[d], data['c'][d]) for d in range(1, H+1))
    tail_divisor = [ZERO]*(B+1)
    tail_additions = 0
    for d in range(H+1, B+1):
        for n in range(d, B+1, d):
            tail_divisor[n] = add(tail_divisor[n], full_c[d])
            tail_additions += 1
    tail_source = [ZERO]+[scale(neg(tail_divisor[n]), F(1, n)) for n in range(1, B+1)]
    arithmetic_corrected = [ZERO]+[
        add(scale(neg(sigma), F(1, n)), tail_source[n]) for n in range(1, B+1)]
    assert all(intersects(data['corrected_source'][n], arithmetic_corrected[n])
               for n in range(A+1, B))
    backbone, blocks, cuts = dyadic_grid()
    result = {
        'status': 'AUTHOR_STRICT_FINITE_DYADIC_TRIANGLE_CERTIFICATE_PASSED',
        'scope': 'One complete actual matched road, q and Q=q+P256; no unbounded-window estimate or RH claim.',
        'window': {'A': A, 'B': B, 'H': H, 'theta': '1/2', 'closed_integer_count': B-A+1},
        'arithmetic': {'method': 'outward integer intervals', 'denominator_power_of_10': DIGITS},
        'inputs': [{'path': str(p.relative_to(ROOT)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
                   for p in (BASE_CERT, ROOT/'rh_joint_certificate/certify_joint_energy.py',
                             ROOT/'rh_correlation_rational/certify_matched_nodes.py')],
        'cache': {'path': str(CACHE.relative_to(ROOT)),
                  'sha256': hashlib.sha256(CACHE.read_bytes()).hexdigest(),
                  'regenerate_if_absent': 'python3 rh_joint_certificate/certify_joint_energy.py',
                  'portable_bundle_policy': 'regenerable cache is not included'},
        'partition': {'backbone': backbone, 'fine_nodes': cuts,
                      'fine_block_count': len(cuts)-1, 'dyadic_blocks': blocks,
                      'rule': 'inside [X,min(2X,B)] use step floor(X^(3/4)), include real right boundary; retain local even indices each round'},
        'sigma_H': record(sigma),
        'complete_arithmetic_check': {
            'all_c_d_reconstructed_through': B,
            'definition': 'c=mu*(D-kappa), including c(1)=-2log(2)',
            'corrected_source_check_at_every_internal_integer': True,
            'full_tail_definition': 'tail_n=-(1/n) sum_{d|n,d>H} c(d)',
            'mobius_convolution_interval_additions': mobius_additions,
            'large_divisor_sieve_interval_additions': tail_additions},
        'roads': {},
    }
    for road in ('q', 'Q'):
        values = data[road]
        source = data['f' if road == 'q' else 'corrected_source']
        coarse = charges_at(values, cuts)
        skeleton = {x: coarse.get(x, ZERO) for x in backbone}
        incoming = {x: [] for x in backbone}
        fine_interp = interpolate(values, cuts)
        J = interpolate(values, backbone)
        affine = interpolate(values, [A, B])
        local_remainder = [ZERO]*(B+1)
        for n in range(A+1, B):
            local_remainder[n] = ZERO if n in coarse else sub(values[n], fine_interp[n])
        reconstructed = [ZERO]*(B+1)
        U = [ZERO]*(B+1)
        block_records = []
        all_level_roots = []
        all_packet_count = 0
        for block in blocks:
            X, Y = block['X'], block['Y']
            levels, end_flow = condense_block(block['nodes'], coarse)
            for x, flow in end_flow.items():
                skeleton[x] = add(skeleton[x], flow)
                incoming[x].append({'from_block': [X, Y], 'charge': record(flow)})
            lr = []
            for index, packets in enumerate(levels, 1):
                layer = [ZERO]*(B+1)
                packets_out = []
                sqsum, signed_sqsum = ZERO, ZERO
                sigma_sqsum = tail_sqsum = cross_sum = ZERO
                predicted_layer_energy = ZERO
                kernel_bound_layer_energy = ZERO
                delta = max(R-L for L, x, R, t in packets)
                for L, x, R, t in packets:
                    all_packet_count += 1
                    a, b, h = x-L, R-x, R-L
                    tp = positive(t)
                    sqsum = add(sqsum, square(tp))
                    signed_sqsum = add(signed_sqsum, square(t))
                    # This is the true full-integer triangular moment.
                    moment = isum(scale(source[n], phi(L, x, R, n)) for n in range(L+1, R))
                    middle = add(scale(values[L], F(b, h)), scale(values[R], F(a, h)))
                    secant_charge = scale(sub(values[x], middle), F(h, a*b))
                    assert intersects(t, moment) and intersects(t, secant_charge)
                    kernel_sq = ZERO
                    K1 = ZERO
                    for n in range(L+1, R):
                        kernel = T(L, x, R, n)
                        reconstructed[n] = add(reconstructed[n], scale(t, kernel))
                        v = scale(tp, kernel)
                        layer[n] = add(layer[n], v)
                        U[n] = add(U[n], v)
                        kernel_sq = add(kernel_sq, rat(kernel*kernel/F(n*n)))
                        K1 = add(K1, rat(phi(L, x, R, n)/n))
                    unweighted = F(a*b*(2*a*b+1), 6*h)
                    bound = unweighted/F(L*L)
                    K1_closed = harmonic_kernel(L,x,R,1,harmonic)
                    assert intersects(K1,K1_closed)
                    predicted_layer_energy = add(predicted_layer_energy, mul(square(tp), kernel_sq))
                    kernel_bound_layer_energy = add(kernel_bound_layer_energy, scale(square(tp), bound))
                    pr = {'L': L, 'x': x, 'R': R, 'support_length': h,
                          'signed_charge': record(t), 'full_source_hat_moment': record(moment),
                          'three_point_secant_charge': record(secant_charge),
                          'weighted_kernel_square': record(kernel_sq),
                          'unweighted_kernel_square_exact': str(unweighted),
                          'weighted_kernel_square_upper_bound': str(bound)}
                    if road == 'Q':
                        sigma_part = mul(neg(sigma), K1)
                        tail_part = isum(scale(tail_source[n], phi(L,x,R,n)) for n in range(L+1,R))
                        tail_via_kernels = ZERO
                        tail_absolute = ZERO
                        nonzero_divisor_kernels = 0
                        for d in range(H+1,R):
                            if (R-1)//d == L//d:
                                continue
                            Kd = harmonic_kernel(L,x,R,d,harmonic)
                            value = mul(full_c[d],Kd)
                            tail_via_kernels = sub(tail_via_kernels,value)
                            tail_absolute = add(tail_absolute,abs_interval(value))
                            nonzero_divisor_kernels += 1
                        assert intersects(tail_part,tail_via_kernels)
                        assert intersects(t, add(sigma_part, tail_part))
                        sigma_sqsum = add(sigma_sqsum, square(sigma_part))
                        tail_sqsum = add(tail_sqsum, square(tail_part))
                        cross_sum = add(cross_sum, mul(sigma_part, tail_part))
                        pr['arithmetic_components'] = {
                            'K1': record(K1), 'minus_sigma_times_K1': record(sigma_part),
                            'complete_large_divisor_tail': record(tail_part),
                            'complete_large_divisor_tail_via_harmonic_Kd':record(tail_via_kernels),
                            'sum_absolute_divisor_kernel_terms':record(tail_absolute),
                            'nonzero_large_divisor_kernel_count':nonzero_divisor_kernels,
                            'combined_charge_enclosures_overlap': True}
                    packets_out.append(pr)
                actual_layer_energy = energy(layer, X+1, Y-1)
                assert intersects(actual_layer_energy, predicted_layer_energy)
                all_level_roots.append(sqrt_interval(actual_layer_energy))
                level = {'level': index, 'packet_count': len(packets),
                         'delta_max_support_length': delta,
                         'positive_charge_count': sum(t[0]>0 for L,x,R,t in packets),
                         'negative_charge_count': sum(t[1]<0 for L,x,R,t in packets),
                         'unresolved_charge_signs': sum(t[0]<=0<=t[1] for L,x,R,t in packets),
                         'sum_positive_charge_squares': record(sqsum),
                         'old_C_squared_required_X_times_sum': record(scale(sqsum, X)),
                         'scale_C_squared_required_delta_cubed_over_X_squared_times_sum': record(scale(sqsum,F(delta**3,X*X))),
                         'exact_positive_layer_energy': record(actual_layer_energy),
                         'exact_diagonal_kernel_energy': record(predicted_layer_energy),
                         'kernel_upper_bound_layer_energy': record(kernel_bound_layer_energy),
                         'sum_signed_charge_squares': record(signed_sqsum),
                         'packets': packets_out}
                if road == 'Q':
                    joint = add(add(sigma_sqsum, scale(cross_sum,2)), tail_sqsum)
                    assert intersects(joint,signed_sqsum)
                    level['arithmetic_joint_square'] = {
                        'sigma_component_squares': record(sigma_sqsum),
                        'tail_component_squares': record(tail_sqsum),
                        'twice_sigma_tail_cross': record(scale(cross_sum,2)),
                        'signed_sum_squares_identity_overlap': True,
                        'warning': 'These are squares before positive-part selection; no components are independently positive-parted.'}
                lr.append(level)
            block_records.append({'X': X, 'Y': Y, 'fine_step': block['fine_step'],
                                  'levels': lr, 'end_flows': incoming[X][-1:]+incoming[Y][-1:]})
        assert all_packet_count == len(cuts)-len(backbone)
        skeleton_direct = charges_at(values, backbone)
        assert all(intersects(skeleton[x], skeleton_direct[x]) for x in backbone[1:-1])
        signed_skeleton_rhs, positive_skeleton_rhs = ([ZERO]*(B+1) for _ in range(2))
        for x in backbone[1:-1]:
            signed_skeleton_rhs[x] = skeleton[x]
            positive_skeleton_rhs[x] = positive(skeleton[x])
        signed_skeleton = green_apply(signed_skeleton_rhs, A, B)
        positive_skeleton = green_apply(positive_skeleton_rhs, A, B)
        assert all(intersects(J[n], add(affine[n],signed_skeleton[n])) for n in range(A,B+1))
        assert all(intersects(fine_interp[n], add(J[n],reconstructed[n])) for n in range(A,B+1))
        # Exact algebra proves the inequalities; interval intersection verifies
        # implementations without pretending overlapping intervals prove order.
        local_energy = energy(local_remainder,A+1,B-1,'positive')
        local_root = sqrt_interval(local_energy)
        full_envelope = [add(J[n],U[n]) for n in range(B+1)]
        positive_skeleton_envelope = [add(add(affine[n],positive_skeleton[n]),U[n]) for n in range(B+1)]
        envelope_energy = energy(full_envelope,A+1,B-1,'positive')
        positive_skeleton_envelope_energy = energy(positive_skeleton_envelope,A+1,B-1,'positive')
        budget = square(add(sqrt_interval(envelope_energy),local_root))
        positive_skeleton_budget = square(add(sqrt_interval(positive_skeleton_envelope_energy),local_root))
        actual_interior = energy(values,A+1,B-1,'positive')
        actual_closed = energy(values,A,B,'positive')
        endpoints = add(scale(square(positive(values[A])),F(1,A*A)),
                        scale(square(positive(values[B])),F(1,B*B)))
        assert intersects(actual_closed,add(actual_interior,endpoints))
        assert actual_interior[1] <= budget[0]
        # Positive endpoint samples can be used without erasing the signed
        # source: this is an explicit, separately labelled upper observer.
        positive_samples = [positive(v) for v in values]
        Jplus = interpolate(positive_samples,backbone)
        J_energy = energy(J,A+1,B-1,'positive')
        Jplus_energy = energy(Jplus,A+1,B-1)
        layer_triangle = isum(all_level_roots)
        separate_budget = square(add(add(sqrt_interval(J_energy),layer_triangle),local_root))
        positive_sample_budget = square(add(add(sqrt_interval(Jplus_energy),layer_triangle),local_root))
        maximal_diagnostics={}
        for key in ('old_C_squared_required_X_times_sum',
                    'scale_C_squared_required_delta_cubed_over_X_squared_times_sum'):
            choices=[(b,l) for b in block_records for l in b['levels']]
            winner_b,winner_l=max(choices,key=lambda v:int(v[1][key]['integer_bounds'][1]))
            maximal_diagnostics[key]={
                'X':winner_b['X'],'Y':winner_b['Y'],'level':winner_l['level'],
                'delta':winner_l['delta_max_support_length'],
                'value':winner_l[key],
                'required_C':record(sqrt_interval(tuple(map(int,winner_l[key]['integer_bounds']))))}
        # Explicit global signed Green reconstruction of the full road, with
        # actual global endpoints, supplements the local reconstructions.
        source_green = green_apply(source,A,B,values[A],values[B])
        assert all(intersects(values[n],source_green[n]) for n in range(A,B+1))
        result['roads'][road] = {
            'true_dyadic_endpoint_samples': [{'n':x,'value':record(values[x])} for x in backbone],
            'original_fine_charges': [{'n':x,'charge':record(coarse[x])} for x in cuts[1:-1]],
            'dyadic_blocks': block_records,
            'skeleton': [{'n':x,'original_fine_charge':record(coarse.get(x,ZERO)),
                         'incoming_flows':incoming[x], 'combined_charge':record(skeleton[x]),
                         'direct_dyadic_slope_jump': record(skeleton_direct[x]) if x in skeleton_direct else None,
                         'normalized_positive_charge_sqrt_n':None if x in (A,B) else record(mul(positive(skeleton[x]),sqrt_interval(rat(x)))),
                         'global_boundary_zero_Green_image':x in (A,B)} for x in backbone],
            'maximal_finite_layer_diagnostics':maximal_diagnostics,
            'energies': {
                'actual_positive_energy_interior':record(actual_interior),
                'actual_positive_energy_closed':record(actual_closed),
                'true_two_endpoint_direct_energy':record(endpoints),
                'fine_local_positive_remainder_energy':record(local_energy),
                'dyadic_interpolant_positive_energy':record(J_energy),
                'dyadic_positive_sample_interpolant_energy':record(Jplus_energy),
                'sum_positive_local_packets_energy':record(energy(U,A+1,B-1)),
                'J_plus_positive_local_packets_positive_energy':record(envelope_energy),
                'squared_budget_J_plus_local_packets_plus_actual_local_remainder':record(budget),
                'closed_squared_budget_J_plus_local_packets_plus_actual_local_remainder':record(add(budget,endpoints)),
                'squared_budget_with_skeleton_charges_positive_parted':record(positive_skeleton_budget),
                'sum_individual_block_layer_norms':record(layer_triangle),
                'squared_separate_J_and_layer_triangle_budget':record(separate_budget),
                'squared_positive_samples_and_layer_triangle_budget':record(positive_sample_budget),
                'budget_to_actual_interior_ratio':record(divide(budget,actual_interior)),
                'fine_interpolant_positive_energy':record(energy(fine_interp,A+1,B-1,'positive'))},
            'checks': {
                'all_packet_source_hat_moments_overlap_transfer':True,
                'all_packet_three_point_secants_overlap_transfer':True,
                'all_K1_harmonic_closed_forms_overlap_complete_integer_sum':True,
                'all_complete_Q_tail_harmonic_divisor_kernel_sums_overlap_source_sum':True if road=='Q' else 'not_applicable_to_q',
                'all_level_diagonal_kernel_energies_overlap_direct':True,
                'combined_skeleton_charges_overlap_dyadic_slope_jumps':True,
                'fine_equals_dyadic_plus_local_signed_packets_at_every_integer':True,
                'dyadic_equals_true_global_affine_plus_signed_skeleton_at_every_integer':True,
                'full_road_equals_true_endpoint_Green_source_at_every_integer':True,
                'no_composites_or_unit_background_deleted':True,
                'order_basis':'exact algebraic envelope theorem; independently strict actual interior energy < certified budget lower endpoint'}
        }
        print(json.dumps({'road':road,'packet_count':all_packet_count,
                          'local_cells':len(cuts)-1,
                          'dyadic_signed_skeleton_budget':record(budget)['upper'],
                          'positive_skeleton_budget':record(positive_skeleton_budget)['upper'],
                          'actual_energy':record(actual_interior)['upper'],
                          'seconds':round(time.perf_counter()-started,3)}),flush=True)
    result['cost']={'seconds':time.perf_counter()-started,'road_recomputations':road_recomputations,
                    'window_integer_visits':'all integers, multiple exact checking passes',
                    'local_packet_count_per_road':len(cuts)-len(backbone)}
    output=OUT/'dyadic_triangle_certificate.json'
    output.write_text(json.dumps(result,ensure_ascii=False,separators=(',',':'))+'\n')
    assert output.stat().st_size < 1024*1024
    print(json.dumps({'output_bytes':output.stat().st_size,'sha256':hashlib.sha256(output.read_bytes()).hexdigest()}),flush=True)


if __name__ == '__main__':
    main()
