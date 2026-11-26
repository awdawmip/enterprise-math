#!/usr/bin/env python3
"""Fixed positive-thickness calibrated roads and their explicit whole-tail bounds.

New certificate only.  No old certificates or road sample tables are rerun.
All decisions use exact fractions and 80-place outward integer intervals.
"""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import argparse
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode = True


def module_at(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--previous', type=Path, required=True,
                        help='riemann_coherent_tail_interval_spectrum_20261126 package')
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('shifted_roads_certificate.json'))
    args = parser.parse_args()
    r5 = args.previous / 'prior/riemann_three_thickness_green_macro_20261126'
    r4 = r5 / 'prior/riemann_calibrated_green_sparse_20261126'
    phase = r4 / 'prior/riemann_signed_green_thickness_phase_20261124'
    older = phase / 'prior/riemann_native_residual_growth_20261124/prior/riemann_matching_isotonic_anchors_20261124'
    early = older / 'prior/riemann_directed_local_20261124/prior/riemann_cumulative_haar_20261123'
    paths = [phase / 'fixed_family/certify_fixed_family_density.py',
             older / 'matching/verify_actual_matching.py',
             early / 'dependencies/certify_fast_harmonic_energy.py',
             r5 / 'three_thickness/three_thickness_certificate.json']
    em = module_at('shifted_roads_em', paths[0])
    helper = module_at('shifted_roads_exp', paths[1])
    m = module_at('shifted_roads_intervals', paths[2])
    old = json.loads(paths[3].read_text())
    gamma = tuple(map(int, old['regular_constants']['gamma']['integer_bounds']))
    assert old['regular_constants']['gamma']['denominator_power_of_10'] == 80

    def add(*xs):
        return m.total(xs)

    def absolute(z):
        if z[0] >= 0:
            return z
        if z[1] <= 0:
            return m.neg(z)
        return 0, max(-z[0], z[1])

    def div(a, b):
        if b[1] < 0:
            return m.neg(m.mul(a, em.reciprocal(m, m.neg(b))))
        assert b[0] > 0
        return m.mul(a, em.reciprocal(m, b))

    def sqrt_interval(z):
        assert z[0] >= 0
        lo = isqrt(z[0]*m.S)
        hi = isqrt(z[1]*m.S)
        if hi*hi < z[1]*m.S:
            hi += 1
        return lo, hi

    def negative_power_of_two(power):
        return em.exp_negative(m, helper, m.qmul(m.log_int(2), power))

    families = []
    all_node_rows = []
    zeta_cache = {}
    extra_zeta_rows = []
    for name, nodes in [('subsquare', [F(3, 5), F(3, 4), F(9, 10)]),
                        ('bounded', [F(2), F(3), F(4)])]:
        errors, constants = [], []
        for a in nodes:
            z, dz, remainder = em.zeta_em(m, helper, 1+a)
            zeta_cache[1+a] = z
            g = em.reciprocal(m, z)
            gp = m.neg(m.mul(m.mul(dz, g), g))
            density = m.qmul(g, 1/a)
            constant = add(m.ONE, gamma, m.mul(m.sub(gamma, m.ONE), density),
                           m.qmul(m.sub(gp, m.ONE), 1/a))
            error = m.sub(density, m.ONE)
            assert error[1] < 0
            errors.append(error)
            constants.append(constant)
            all_node_rows.append({'a': str(a), 'zeta': m.record(z), 'zeta_prime': m.record(dz),
                                  'density_minus_one': m.record(error), 'road_constant': m.record(constant),
                                  **remainder})
        e1, e2, e3 = errors
        c1, c2, c3 = constants
        aa, bb, cc, dd = m.sub(e1, e3), m.sub(e2, e3), m.sub(c1, c3), m.sub(c2, c3)
        determinant = m.sub(m.mul(aa, dd), m.mul(bb, cc))
        assert determinant[0] > 0
        w1 = div(m.sub(m.mul(bb, c3), m.mul(e3, dd)), determinant)
        w2 = div(m.sub(m.mul(e3, cc), m.mul(aa, c3)), determinant)
        ws = [w1, w2, m.sub(m.sub(m.ONE, w1), w2)]
        assert ws[0][0] > 0 and ws[1][1] < 0 and ws[2][0] > 0
        tv = add(*(absolute(w) for w in ws))
        vminus = add(*(m.qmul(w, 1/a) for w, a in zip(ws, nodes)))
        mass = add(*ws)
        density_check = add(*(m.mul(w, e) for w, e in zip(ws, errors)))
        constant_check = add(*(m.mul(w, c) for w, c in zip(ws, constants)))
        assert mass[0] <= m.S <= mass[1]
        assert all(z[0] <= 0 <= z[1] for z in (density_check, constant_check))
        row = {'name': name, 'nodes': list(map(str, nodes)), 'weights': list(map(m.record, ws)),
               'calibration_determinant': m.record(determinant), 'total_variation': m.record(tv),
               'V_minus_one': m.record(vminus), 'mass_consistency': m.record(mass),
               'density_consistency': m.record(density_check), 'constant_consistency': m.record(constant_check)}
        if name == 'subsquare':
            local_costs = [1/(a*a*(1-a))+2/a**3 for a in nodes]
            tail_cost = add(*(m.qmul(absolute(w), c) for w, c in zip(ws, local_costs)))
            assert tail_cost[1] < 1202*m.S
            row['pointwise_bound'] = {
                'formula': '|q(y)-V_minus_one| <= K*y^(2/5), every real y>=1',
                'K': m.record(tail_cost), 'individual_exact_costs': list(map(str, local_costs))}
            tails = []
            for exponent in (128, 512):
                A = 2**exponent
                t2 = m.rat(F(1, A*A)+F(1, A))
                tp = add(negative_power_of_two(F(6*exponent, 5)),
                         m.qmul(negative_power_of_two(F(exponent, 5)), 5))
                root = add(m.mul(absolute(vminus), sqrt_interval(t2)),
                           m.mul(tail_cost, sqrt_interval(tp)))
                tails.append({'A': str(A), 'A_power_of_two': exponent,
                              'whole_absolute_energy_root_upper_enclosure': m.record(root),
                              'interpretation': 'Upper endpoint bounds (sum_(n>=A) q(n)^2/n^2)^(1/2). Lower endpoint is not an actual-error lower bound.'})
            row['whole_tail_bounds'] = tails

            bits = 100
            den = 2**bits
            lower_cells, upper_cells = [], []
            for w in ws[:2]:
                fl, fh = w[0]*den//m.S, w[1]*den//m.S
                assert fl == fh
                lower_cells.append(fl)
                upper_cells.append(fl+1)
            twins = []
            threshold_power = 512
            log_threshold = m.qmul(m.log_int(2), threshold_power)
            inv_threshold = negative_power_of_two(F(threshold_power))
            decay_threshold = negative_power_of_two(F(3*threshold_power, 5))
            for kind, cells in [('floor', lower_cells), ('ceiling', upper_cells)]:
                rat_ws = [F(k, den) for k in cells]
                rat_ws.append(1-sum(rat_ws, F(0)))
                assert sum(rat_ws, F(0)) == 1
                drift = add(*(m.qmul(e, r) for e, r in zip(errors, rat_ws)))
                constant = add(*(m.qmul(c, r) for c, r in zip(constants, rat_ws)))
                rv = sum((r/a for r, a in zip(rat_ws, nodes)), F(0))
                rk = sum((abs(r)*c for r, c in zip(rat_ws, local_costs)), F(0))
                payment = add(m.qmul(inv_threshold, abs(rv)), m.qmul(decay_threshold, rk))
                main = add(m.mul(drift, log_threshold), constant)
                if kind == 'floor':
                    assert drift[1] < 0 and constant[0] > 0
                    sign_bound = add(main, payment)
                    assert sign_bound[1] < 0
                    eventual = 'q(y)<0 for every real y>=2^512; positive dyadic energy eventually zero; absolute whole-tail energy diverges.'
                else:
                    assert drift[0] > 0 and constant[1] < 0
                    sign_bound = m.sub(main, payment)
                    assert sign_bound[0] > 0
                    eventual = 'q(y)>0 for every real y>=2^512; positive and absolute dyadic energy grow asymptotically as (density-1)^2*X*(log X)^2.'
                twins.append({'kind': kind, 'bits': bits, 'weights': list(map(str, rat_ws)),
                              'density_minus_one': m.record(drift), 'road_constant': m.record(constant),
                              'V_minus_one_exact': str(rv), 'K_exact': str(rk),
                              'threshold_power_of_two': threshold_power,
                              'signed_full_road_bound_at_threshold': m.record(sign_bound),
                              'eventual_statement': eventual})
            row['rational_neighbours'] = twins
        else:
            assert all(a.denominator == 1 and a > 1 for a in nodes)
            costs = [1/(a-1)+F(2**a.numerator, a.numerator*a.numerator) for a in nodes]
            bounded_cost = add(*(m.qmul(absolute(w), c) for w, c in zip(ws, costs)))
            bound = add(absolute(vminus), bounded_cost)
            assert bound[1] < 186*m.S
            row['pointwise_bound'] = {'formula': '|q(y)| <= M, every real y>=1',
                                       'M': m.record(bound), 'individual_exact_costs': list(map(str, costs)),
                                       'bound_for_q_minus_V': m.record(bounded_cost)}
            A = 2**128
            root = m.mul(bound, sqrt_interval(m.rat(F(1,A)+F(1,A*A))))
            row['whole_tail_bounds'] = [{'A': str(A), 'A_power_of_two': 128,
                                         'whole_absolute_energy_root_upper_enclosure': m.record(root)}]
            source2 = add(*(m.qmul(w, (1-F(1,2**a.numerator))/a) for w,a in zip(ws,nodes)))
            source_error2 = m.sub(source2, m.log_int(2))
            assert source_error2[1] < 0
            row['finite_return_difference'] = {
                'D_2': m.record(source2), 'D_2_minus_Lambda_2': m.record(source_error2),
                'q_3_minus_q_star_3': m.record(m.qmul(source_error2, F(1,2))),
                'scope': 'Full source identity at n=2 and complete road difference at y=3; D(1)=0, source at n=3 has zero road kernel. Integer thickness powers are exact rational, no additional source exponential calls.'}
            limit_terms = []
            for w, a in zip(ws, nodes):
                if a not in zeta_cache:
                    za, dza, remainder = em.zeta_em(m, helper, a)
                    zeta_cache[a] = za
                    extra_zeta_rows.append({'s': str(a), 'zeta': m.record(za),
                                            'zeta_prime_byproduct': m.record(dza), **remainder})
                inv = em.reciprocal(m, zeta_cache[a])
                la = m.qmul(add(m.ONE, m.qmul(inv, F(1,2))), 1/a)
                limit_terms.append(m.mul(w, la))
            limit_value = add(*limit_terms)
            assert limit_value[0] > m.rat(F(179,100))[1]
            assert limit_value[1] < m.rat(F(9,5))[0]
            remainder_K0 = add(*(m.qmul(absolute(w), c) for w, c in
                                  zip(ws, [F(7,2), F(83,27), F(71,24)])))
            remainder_K1 = m.qmul(absolute(ws[0]), F(1,2))
            assert remainder_K0[0] > remainder_K1[1]
            lower_at_1024 = m.sub(limit_value,
                                  m.qmul(add(remainder_K0, m.mul(remainder_K1, m.log_int(1024))), F(1,1024)))
            assert lower_at_1024[0] > m.rat(F(133,100))[1]
            row['limit_at_infinity'] = {
                'L': m.record(limit_value),
                'formula': 'L=sum_j w_j*(1+1/(2*zeta(a_j)))/a_j',
                'remainder_K0': m.record(remainder_K0), 'remainder_K1': m.record(remainder_K1),
                'whole_real_remainder_bound': '|q(y)-L| <= (K0+K1*log y)/y for every real y>=1',
                'positive_threshold': 1024, 'uniform_lower_from_threshold': m.record(lower_at_1024),
                'dyadic_positive_energy_coefficient_L_squared_over_two': m.record(m.qmul(m.square(limit_value), F(1,2))),
                'dyadic_asymptotic': 'sum_(n=X)^(2X) q(n)_+^2/n^2 = L^2/(2X)+O(log X/X^2)'}
        families.append(row)

    result = {
        'status': 'PASS', 'author': 'EM-DIRECT-E7559A',
        'activity': 'RA-D2F111EA1C0D4B1DBEFBC1B4',
        'review_scope': 'New author certificate, not independent Review or formal Result.',
        'arithmetic': 'Exact fractions and outward integer intervals scaled by 10^80; no floating decisions.',
        'source_scope': 'Full D_a(n)=a^(-1) product_(p|n)(1-p^(-a)), n>=2; D_a(1)=0. Signed exact real weights have mass one; complete background, history and true endpoints retained.',
        'new_zeta_node_count': len(all_node_rows), 'new_nodes': all_node_rows,
        'additional_zeta_evaluations': extra_zeta_rows,
        'new_zeta_evaluations_total': len(all_node_rows)+len(extra_zeta_rows),
        'families': families,
        'old_road_queries': 0, 'old_certificate_reruns': 0,
        'new_direct_source_exponential_factors': 0,
        'new_tail_exponential_bound_evaluations': 6,
        'dependencies': [{'input_package': 'round6', 'path': str(path.relative_to(args.previous)),
                          'sha256': hashlib.sha256(path.read_bytes()).hexdigest()} for path in paths],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'families': [{k:f[k] for k in ('name','nodes','weights','total_variation','pointwise_bound','whole_tail_bounds')} for f in families]}, indent=2))


if __name__ == '__main__':
    main()
