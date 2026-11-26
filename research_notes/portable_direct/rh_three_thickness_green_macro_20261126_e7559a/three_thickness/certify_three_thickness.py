#!/usr/bin/env python3
"""Strict three-thickness double calibration, with a cubic source budget.

All certificate decisions use exact fractions or outward integer intervals.
The exact weights are computable real numbers defined by a nonsingular
three-by-three system; interval residual inclusion is only a consistency check.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial, isqrt
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


def regular_constants(m):
    """Enclose gamma, gamma_1, gamma_2 by differentiated, pole-removed EM.

    For order M, r=|B_(2M)|/(2M*N^(2M)).  The second derivative remainder
    is bounded by r*((H_(2M)+log N)^2 + 2*(H_(2M)+log N)/(2M)
                     + 2/(2M)^2 + H_(2M)^(2)).
    This is an absolute integral bound, not a finite-difference estimate.
    """
    N, order = 64, 24
    ln = m.log_int(N)
    gamma = m.sub(m.rat(sum((F(1, n) for n in range(1, N)), F(0))), ln)
    derivative = m.qmul(m.square(ln), F(1, 2))
    derivative2 = m.qmul(m.mul(m.square(ln), ln), F(-1, 3))
    for n in range(1, N):
        logn = m.log_int(n)
        derivative = m.sub(derivative, m.qmul(logn, F(1, n)))
        derivative2 = m.add(derivative2, m.qmul(m.square(logn), F(1, n)))
    gamma = m.add(gamma, m.rat(F(1, 2 * N)))
    derivative = m.sub(derivative, m.qmul(ln, F(1, 2 * N)))
    derivative2 = m.add(derivative2, m.qmul(m.square(ln), F(1, 2 * N)))
    bernoulli = m.bernoulli(2 * order)
    rising, harmonic, harmonic2 = F(1), F(0), F(0)
    for k in range(1, 2 * order):
        rising *= k
        harmonic += F(1, k)
        harmonic2 += F(1, k * k)
        if k % 2:
            j = (k + 1) // 2
            term = m.rat(bernoulli[2 * j] * rising / F(factorial(2 * j) * N ** (2 * j)))
            diff = m.sub(m.rat(harmonic), ln)
            gamma = m.add(gamma, term)
            derivative = m.add(derivative, m.mul(term, diff))
            derivative2 = m.add(derivative2, m.mul(term, m.sub(m.square(diff), m.rat(harmonic2))))
    remainder = max(abs(term[0]), abs(term[1]))
    two_m = 2 * order
    harmonic += F(1, two_m)
    harmonic2 += F(1, two_m * two_m)
    plus = m.add(ln, m.rat(harmonic))
    first_factor = m.add(plus, m.rat(F(1, two_m)))
    second_factor = m.total([
        m.square(plus), m.qmul(plus, F(2, two_m)),
        m.rat(F(2, two_m * two_m) + harmonic2),
    ])
    first_r = m.mul((remainder, remainder), first_factor)[1]
    second_r = m.mul((remainder, remainder), second_factor)[1]
    gamma = gamma[0] - remainder, gamma[1] + remainder
    gamma1 = m.neg((derivative[0] - first_r, derivative[1] + first_r))
    gamma2 = derivative2[0] - second_r, derivative2[1] + second_r
    return gamma, gamma1, gamma2, {
        'N': N, 'order': order,
        'gamma_remainder_upper': m.record((remainder, remainder)),
        'gamma1_remainder_upper': m.record((first_r, first_r)),
        'gamma2_remainder_upper': m.record((second_r, second_r)),
        'second_derivative_remainder_formula':
            '|R_M(1)|_bound*((H_2M+log N)^2+2*(H_2M+log N)/(2M)+2/(2M)^2+H_2M^(2))',
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--previous', type=Path, required=True,
                        help='riemann_calibrated_green_sparse_20261126 package')
    parser.add_argument('--epsilon-denominator', type=int, default=10**6)
    parser.add_argument('--A', type=int, default=1024)
    parser.add_argument('--B', type=int, default=32768)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('three_thickness_certificate.json'))
    args = parser.parse_args()
    assert args.epsilon_denominator >= 7 and 2 <= args.A <= args.B
    previous = args.previous / 'prior/riemann_signed_green_thickness_phase_20261124'
    older = previous / 'prior/riemann_native_residual_growth_20261124/prior/riemann_matching_isotonic_anchors_20261124'
    early = older / 'prior/riemann_directed_local_20261124/prior/riemann_cumulative_haar_20261123'
    paths = [previous / 'fixed_family/certify_fixed_family_density.py',
             older / 'matching/verify_actual_matching.py',
             early / 'dependencies/certify_fast_harmonic_energy.py']
    em = module_at('three_thickness_zeta_em', paths[0])
    helper = module_at('three_thickness_exp', paths[1])
    m = module_at('three_thickness_intervals', paths[2])

    def add(*xs):
        return m.total(xs)

    def div(a, b):
        if b[1] < 0:
            return m.neg(m.mul(a, em.reciprocal(m, m.neg(b))))
        assert b[0] > 0
        return m.mul(a, em.reciprocal(m, b))

    def abs_interval(z):
        if z[0] >= 0:
            return z
        if z[1] <= 0:
            return m.neg(z)
        return 0, max(-z[0], z[1])

    gamma, gamma1, gamma2, regular_bounds = regular_constants(m)
    d1 = m.neg(gamma)
    d2 = add(m.square(gamma), gamma1)
    c1 = add(gamma, m.qmul(m.square(gamma), 2), m.qmul(gamma1, 3))
    c2 = add(m.qmul(m.mul(m.square(gamma), gamma), -3), m.neg(m.square(gamma)),
             m.qmul(m.mul(gamma, gamma1), -7), m.neg(gamma1), m.qmul(gamma2, -2))
    delta = m.sub(m.mul(d1, c2), m.mul(d2, c1))
    delta_simplified = add(m.square(m.square(gamma)), m.qmul(m.mul(m.square(gamma), gamma1), 2),
                           m.qmul(m.mul(gamma, gamma2), 2), m.qmul(m.square(gamma1), -3))
    assert delta[0] > m.rat(F(3, 100))[1]
    assert delta[1] < m.rat(F(4, 100))[0]
    assert max(delta[0], delta_simplified[0]) <= min(delta[1], delta_simplified[1])
    slope = div(delta, m.square(d1))
    assert d1[1] < 0 and slope[0] > 0

    epsilon = F(1, args.epsilon_denominator)
    nodes = [j * epsilon for j in (1, 2, 3)]
    rows, errors, constants = [], [], []
    for a in nodes:
        zeta, derivative, bounds = em.zeta_em(m, helper, 1 + a)
        g = em.reciprocal(m, zeta)
        gp = m.neg(m.mul(derivative, m.square(g)))
        density = m.qmul(g, 1 / a)
        constant = add(m.ONE, gamma, m.mul(m.sub(gamma, m.ONE), density),
                       m.qmul(m.sub(gp, m.ONE), 1 / a))
        error = m.sub(density, m.ONE)
        errors.append(error)
        constants.append(constant)
        rows.append({'a': str(a), 'zeta': m.record(zeta), 'zeta_prime': m.record(derivative),
                     'density_minus_one': m.record(error), 'road_constant': m.record(constant), **bounds})
    e1, e2, e3 = errors
    v1, v2, v3 = constants
    aa, bb, cc, dd = m.sub(e1, e3), m.sub(e2, e3), m.sub(v1, v3), m.sub(v2, v3)
    determinant = m.sub(m.mul(aa, dd), m.mul(bb, cc))
    assert determinant[0] > 0
    w1 = div(m.sub(m.mul(bb, v3), m.mul(e3, dd)), determinant)
    w2 = div(m.sub(m.mul(e3, cc), m.mul(aa, v3)), determinant)
    w3 = m.sub(m.sub(m.ONE, w1), w2)
    ws = [w1, w2, w3]
    assert w1[0] > 0 and w2[1] < 0 and w3[0] > 0
    mass = add(*ws)
    zero_density = add(*(m.mul(w, e) for w, e in zip(ws, errors)))
    zero_constant = add(*(m.mul(w, c) for w, c in zip(ws, constants)))
    assert mass[0] <= m.S <= mass[1]
    assert all(z[0] <= 0 <= z[1] for z in (zero_density, zero_constant))
    tv = add(*(abs_interval(w) for w in ws))
    assert tv[1] < 8 * m.S
    M1 = add(*(m.qmul(w, a) for w, a in zip(ws, nodes)))
    M2 = add(*(m.qmul(w, a*a) for w, a in zip(ws, nodes)))
    abs_cubic = add(*(m.qmul(abs_interval(w), a**3) for w, a in zip(ws, nodes)))
    assert M1[0] > 0 and M2[0] > 0
    # This example is not a polynomial moment-matching family.
    normalized_M1 = m.qmul(M1, 1 / epsilon**3)
    normalized_M2 = m.qmul(M2, 1 / epsilon**3)

    L = m.log_int(args.B)
    Sbound = add(L, m.qmul(m.log_int(2), 4))
    L2, S2 = m.square(L), m.square(Sbound)
    L3, S3 = m.mul(L2, L), m.mul(S2, Sbound)
    S4 = m.square(S2)
    b1 = m.qmul(add(m.mul(L, Sbound), S2), F(1, 2))
    b2 = add(m.qmul(m.mul(L2, Sbound), F(1, 6)),
             m.qmul(m.mul(L, S2), F(1, 4)), m.qmul(S3, F(1, 6)))
    common = add(m.qmul(m.mul(L3, Sbound), F(1, 24)),
                 m.qmul(m.mul(L2, S2), F(1, 12)),
                 m.qmul(m.mul(L, S3), F(1, 12)))
    cubic_terms = []
    for w, a in zip(ws, nodes):
        exp_as = em.reciprocal(m, em.exp_negative(m, helper, m.qmul(Sbound, a)))
        bracket = add(common, m.qmul(m.mul(S4, exp_as), F(1, 24)))
        cubic_terms.append(m.qmul(m.mul(abs_interval(w), bracket), a**3))
    M1_payment = m.mul(abs_interval(M1), b1)
    M2_payment = m.mul(abs_interval(M2), b2)
    cubic_payment = add(*cubic_terms)
    linear_radius = add(M1_payment, M2_payment, cubic_payment)
    length = args.B - args.A + 1
    sqrt_lower = isqrt(length * m.S * m.S)
    sqrt_length = sqrt_lower, sqrt_lower + 1
    root_radius = m.mul(linear_radius, sqrt_length)
    endpoint_radius = m.qmul(linear_radius, args.B)
    assert m.qmul(L, 3*epsilon)[1] <= m.S
    pointwise_source_radius = add(m.qmul(m.mul(abs_interval(M1), L2), F(1, 2)),
                                 m.qmul(m.mul(abs_interval(M2), L3), F(1, 6)),
                                 m.qmul(m.mul(abs_cubic, m.square(L2)), F(1, 24)))

    # Optional implementable approximation: round w1,w2 downward to 100
    # binary fractional places, then set the third coefficient by exact mass.
    bits = 100
    denominator = 2**bits
    rationals = []
    rounding_cells = []
    for w in (w1, w2):
        cell_lo, cell_hi = w[0]*denominator//m.S, w[1]*denominator//m.S
        assert cell_lo == cell_hi
        rationals.append(F(cell_lo, denominator))
        rounding_cells.append(str(cell_lo))
    rationals.append(1-sum(rationals, F(0)))
    assert sum(rationals, F(0)) == 1
    coefficient_l1_error = add(*(abs_interval(m.sub(m.rat(r), w)) for r, w in zip(rationals, ws)))
    # Full integer support gives sum_(n<=y) D_a(n)/n
    # <= (exp(a*S(y))-1)/a <= S(y)*exp(a*S(y)).
    max_exp = em.reciprocal(m, em.exp_negative(m, helper, m.qmul(Sbound, nodes[-1])))
    rational_linear_extra = m.mul(coefficient_l1_error, m.mul(Sbound, max_exp))
    rational_root_extra = m.mul(rational_linear_extra, sqrt_length)
    rational_density = add(*(m.qmul(e, r) for e, r in zip(errors, rationals)))
    rational_constant = add(*(m.qmul(c, r) for c, r in zip(constants, rationals)))
    assert rational_density[1] < 0 and rational_constant[0] > 0

    result = {
        'status': 'PASS',
        'researcher_id': 'EM-DIRECT-E7559A',
        'activity': 'RA-D2F111EA1C0D4B1DBEFBC1B4',
        'review_status': 'author computation; not independent Review or formal Result',
        'scope': 'New three-thickness family; exact density and complete-road constant calibration, mass one. Original eleven polynomial matching moments are not preserved; original roads and samples are unchanged.',
        'arithmetic': 'Exact rational data and outward integer intervals scaled by 10^80; no floating decisions.',
        'regular_constants': {'gamma': m.record(gamma), 'gamma1': m.record(gamma1),
                              'gamma2': m.record(gamma2), **regular_bounds},
        'local_analytic_data': {'d1': m.record(d1), 'd2': m.record(d2),
                                'c1': m.record(c1), 'c2': m.record(c2),
                                'delta': m.record(delta), 'delta_simplified': m.record(delta_simplified),
                                'ratio_derivative_at_zero': m.record(slope),
                                'quantifiers': 'There exists epsilon_0>0: all 0<epsilon<epsilon_0 give the exact three-node family. There exists a_0>0: no one- or two-node real-weight double calibration with distinct nodes in (0,a_0). No numerical a_0 or epsilon_0 is asserted.'},
        'finite_example': {'epsilon': str(epsilon), 'nodes': rows,
                            'calibration_determinant': m.record(determinant),
                            'weights': list(map(m.record, ws)), 'total_variation': m.record(tv),
                            'mass_consistency': m.record(mass),
                            'density_consistency': m.record(zero_density),
                            'constant_consistency': m.record(zero_constant),
                            'M1': m.record(M1), 'M2': m.record(M2),
                            'M1_over_epsilon_cubed': m.record(normalized_M1),
                            'M2_over_epsilon_cubed': m.record(normalized_M2),
                            'sum_abs_w_a_cubed': m.record(abs_cubic)},
        'complete_window': {'A': args.A, 'B': args.B, 'closed_integer_count': length,
                             'log_B': m.record(L), 'S_upper_enclosure': m.record(Sbound),
                             'M1_linear_payment': m.record(M1_payment),
                             'M2_linear_payment': m.record(M2_payment),
                             'cubic_linear_payment': m.record(cubic_payment),
                             'linear_radius_coefficient_enclosure': m.record(linear_radius),
                             'endpoint_B_radius_enclosure': m.record(endpoint_radius),
                             'weighted_root_radius_enclosure': m.record(root_radius),
                             'pointwise_source_radius_enclosure': m.record(pointwise_source_radius),
                             'interpretation': 'Upper endpoints are rigorous bounds, not lower bounds for the actual error. Full history, all integer support, true endpoints, and arbitrary interpolation are included.'},
        'rational_approximation': {'bits': bits, 'rounding_cells': rounding_cells,
                                   'weights': list(map(str, rationals)),
                                   'mass_exact': '1',
                                   'coefficient_l1_error': m.record(coefficient_l1_error),
                                   'density_minus_one': m.record(rational_density),
                                   'road_constant': m.record(rational_constant),
                                   'extra_weighted_root_radius_enclosure': m.record(rational_root_extra),
                                   'scope': 'Exact rational weights with exact mass only. Density/constant residuals are paid, not declared zero; the displayed bound concerns this finite window.'},
        'dependencies': [{'path': str(p.relative_to(args.previous)),
                          'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'delta': m.record(delta),
                      'weights': list(map(m.record, ws)),
                      'M1_over_epsilon_cubed': m.record(normalized_M1),
                      'M2_over_epsilon_cubed': m.record(normalized_M2),
                      'weighted_root_radius': m.record(root_radius),
                      'rational_extra_root_radius': m.record(rational_root_extra)}, indent=2))


if __name__ == '__main__':
    main()
