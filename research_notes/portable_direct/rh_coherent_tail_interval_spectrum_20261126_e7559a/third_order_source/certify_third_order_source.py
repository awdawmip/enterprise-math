#!/usr/bin/env python3
"""Third-order common source, nonuniform three-node shapes, strict finite budgets.

No floating value is used in a certificate decision.  The old gamma through
gamma_2 enclosures are read; only the new gamma_3 EM remainder is computed.
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


def gamma3_em(m):
    N, order = 64, 24
    ln = m.log_int(N)
    third = m.qmul(m.square(m.square(ln)), F(1, 4))
    for n in range(1, N):
        z = m.log_int(n)
        third = m.sub(third, m.qmul(m.mul(m.square(z), z), F(1, n)))
    third = m.sub(third, m.qmul(m.mul(m.square(ln), ln), F(1, 2*N)))
    bernoulli = m.bernoulli(2*order)
    rising, h1, h2, h3 = F(1), F(0), F(0), F(0)
    for k in range(1, 2*order):
        rising *= k
        h1 += F(1, k)
        h2 += F(1, k*k)
        h3 += F(1, k*k*k)
        if k % 2:
            j = (k+1)//2
            term = m.rat(bernoulli[2*j]*rising/F(factorial(2*j)*N**(2*j)))
            diff = m.sub(m.rat(h1), ln)
            factor = m.total([m.mul(m.square(diff), diff), m.qmul(diff, -3*h2), m.rat(2*h3)])
            third = m.add(third, m.mul(term, factor))
    remainder = max(abs(term[0]), abs(term[1]))
    q = 2*order
    h1 += F(1, q)
    h2 += F(1, q*q)
    h3 += F(1, q*q*q)
    plus = m.add(m.rat(h1), ln)
    factor = m.total([
        m.mul(m.square(plus), plus), m.qmul(m.square(plus), F(3, q)),
        m.qmul(plus, F(6, q*q)), m.rat(F(6, q*q*q)),
        m.qmul(m.add(plus, m.rat(F(1, q))), 3*h2), m.rat(2*h3),
    ])
    error = m.mul((remainder, remainder), factor)[1]
    value = m.neg((third[0]-error, third[1]+error))
    return value, {'N': N, 'order': order, 'remainder_upper': m.record((error, error)),
                   'formula': 'r0*((H+logN)^3+3*(H+logN)^2/q+6*(H+logN)/q^2+6/q^3+3*H2*(H+logN+1/q)+2*H3), q=2M'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--previous', type=Path, required=True,
                        help='riemann_calibrated_green_sparse_20261126 package')
    parser.add_argument('--round5', type=Path, default=Path('research_round5/three_thickness'))
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('third_order_source_certificate.json'))
    args = parser.parse_args()
    previous = args.previous / 'prior/riemann_signed_green_thickness_phase_20261124'
    older = previous / 'prior/riemann_native_residual_growth_20261124/prior/riemann_matching_isotonic_anchors_20261124'
    early = older / 'prior/riemann_directed_local_20261124/prior/riemann_cumulative_haar_20261123'
    paths = [previous / 'fixed_family/certify_fixed_family_density.py',
             older / 'matching/verify_actual_matching.py',
             early / 'dependencies/certify_fast_harmonic_energy.py',
             args.round5 / 'three_thickness_certificate.json']
    em = module_at('third_source_em', paths[0])
    helper = module_at('third_source_exp', paths[1])
    m = module_at('third_source_intervals', paths[2])
    old = json.loads(paths[3].read_text())

    def decode(rec):
        assert rec['denominator_power_of_10'] == 80
        return tuple(map(int, rec['integer_bounds']))

    def add(*z):
        return m.total(z)

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

    def exp_positive(z):
        return em.reciprocal(m, em.exp_negative(m, helper, z))

    gamma, gamma1, gamma2 = [decode(old['regular_constants'][k]) for k in ('gamma', 'gamma1', 'gamma2')]
    gamma3, gamma3_data = gamma3_em(m)
    assert gamma3[0] > 0
    zeta_coefficients = [m.ONE, gamma, m.neg(gamma1), m.qmul(gamma2, F(1, 2)), m.qmul(gamma3, F(-1, 6))]
    d = [m.ONE]
    for k in range(1, 5):
        d.append(m.neg(add(*(m.mul(zeta_coefficients[i], d[k-i]) for i in range(1, k+1)))))
    c = [m.ZERO] + [add(m.mul(m.sub(gamma, m.ONE), d[k]), m.qmul(d[k+1], k+2)) for k in range(1, 4)]
    delta = m.sub(m.mul(d[1], c[2]), m.mul(d[2], c[1]))
    assert delta[0] > 0
    lam1 = div(m.sub(m.mul(d[2], c[3]), m.mul(c[2], d[3])), delta)
    lam2 = div(m.sub(m.mul(c[1], d[3]), m.mul(d[1], c[3])), delta)
    assert lam1[0] > 0 and lam2[0] > 0
    density_check = add(m.mul(lam1, d[1]), m.mul(lam2, d[2]), d[3])
    constant_check = add(m.mul(lam1, c[1]), m.mul(lam2, c[2]), c[3])
    assert all(z[0] <= 0 <= z[1] for z in (density_check, constant_check))

    def poly(t):
        t2 = m.square(t)
        return add(m.qmul(m.square(t2), F(1, 24)),
                   m.qmul(m.mul(lam2, m.mul(t2, t)), F(-1, 6)),
                   m.qmul(m.mul(lam1, t2), F(1, 2)))

    source2 = m.neg(poly(m.log_int(2)))
    source210 = m.ONE
    for prime in (2, 3, 5, 7):
        source210 = m.mul(source210, m.log_int(prime))
    assert source2[1] < 0 and source210[0] > 0

    A, B = 1024, 32768
    L = m.log_int(B)
    S = add(L, m.qmul(m.log_int(2), 4))
    lp = [m.ONE, L]
    sp = [m.ONE, S]
    for _ in range(4):
        lp.append(m.mul(lp[-1], L))
        sp.append(m.mul(sp[-1], S))
    b1 = m.qmul(add(m.mul(L, S), sp[2]), F(1, 2))
    b2 = add(m.qmul(m.mul(lp[2], S), F(1, 6)),
             m.qmul(m.mul(L, sp[2]), F(1, 4)), m.qmul(sp[3], F(1, 6)))
    b3 = add(m.qmul(m.mul(lp[3], S), F(1, 24)),
             m.qmul(m.mul(lp[2], sp[2]), F(1, 12)),
             m.qmul(m.mul(L, sp[3]), F(1, 12)), m.qmul(sp[4], F(1, 24)))
    common4 = add(m.qmul(m.mul(lp[4], S), F(1, 120)),
                  m.qmul(m.mul(lp[3], sp[2]), F(1, 48)),
                  m.qmul(m.mul(lp[2], sp[3]), F(1, 36)),
                  m.qmul(m.mul(L, sp[4]), F(1, 48)))
    source_unit_budget = add(m.mul(absolute(lam1), b1), m.mul(absolute(lam2), b2), b3)
    sqlo = isqrt((B-A+1)*m.S*m.S)
    sqrt_count = sqlo, sqlo+1
    epsilon = F(1, 10**6)

    def lagrange_weights(nodes):
        out = []
        for a in nodes:
            value = F(1)
            for b in nodes:
                if b != a:
                    value *= b/(b-a)
            out.append(value)
        return out

    def shape_data(shapes):
        classical = lagrange_weights(shapes)
        vinf = max(sum((x**k for x in shapes), F(0)) for k in range(3))
        inverse_infinity = F(0)
        for i in range(3):
            others = [x for j, x in enumerate(shapes) if j != i]
            den = abs((shapes[i]-others[0])*(shapes[i]-others[1]))
            inverse_infinity = max(inverse_infinity, (1+others[0])*(1+others[1])/den)
        vandermonde = (shapes[1]-shapes[0])*(shapes[2]-shapes[0])*(shapes[2]-shapes[1])
        return {'ratios': list(map(str, shapes)), 'limiting_weights': list(map(str, classical)),
                'limiting_total_variation': str(sum(map(abs, classical), F(0))),
                'product': str(shapes[0]*shapes[1]*shapes[2]),
                'scaled_polynomial_matrix_condition_infinity': str(vinf*inverse_infinity),
                'vandermonde': str(vandermonde)}

    families = []
    source_evaluations = 0
    zeta_cache = {}

    def at_node(a):
        if a in zeta_cache:
            return zeta_cache[a]
        z, dz, bounds = em.zeta_em(m, helper, 1+a)
        g = em.reciprocal(m, z)
        # Multiply dz*g first.  Forming g^2 before multiplying by dz would
        # amplify an absolute fixed-scale rounding cell by a^(-2), needlessly
        # widening the hierarchical a=10^(-12) example.
        gp = m.neg(m.mul(m.mul(dz, g), g))
        density = m.qmul(g, 1/a)
        constant = add(m.ONE, gamma, m.mul(m.sub(gamma, m.ONE), density),
                       m.qmul(m.sub(gp, m.ONE), 1/a))
        result = m.sub(density, m.ONE), constant, {
            'a': str(a), 'density_minus_one': m.record(m.sub(density, m.ONE)),
            'road_constant': m.record(constant), **bounds,
        }
        zeta_cache[a] = result
        return result

    for name, shapes in [('equal_spacing', [F(1), F(2), F(3)]),
                         ('moderate_shape', [F(1), F(7, 4), F(3)]),
                         ('tv_nine_limit', [F(1), F(3, 2), F(3)]),
                         ('hierarchical', [epsilon, F(1), F(2)])]:
        nodes = [epsilon*x for x in shapes]
        p = nodes[0]*nodes[1]*nodes[2]
        evaluated = [at_node(a) for a in nodes]
        e1, e2, e3 = [row[0] for row in evaluated]
        c1, c2, c3 = [row[1] for row in evaluated]
        aa, bb = m.sub(e1, e3), m.sub(e2, e3)
        cc, dd = m.sub(c1, c3), m.sub(c2, c3)
        determinant = m.sub(m.mul(aa, dd), m.mul(bb, cc))
        assert determinant[0] > 0
        w1 = div(m.sub(m.mul(bb, c3), m.mul(e3, dd)), determinant)
        w2 = div(m.sub(m.mul(e3, cc), m.mul(aa, c3)), determinant)
        ws = [w1, w2, m.sub(m.sub(m.ONE, w1), w2)]
        assert ws[0][0] > 0 and ws[1][1] < 0 and ws[2][0] > 0
        moments = [add(*(m.qmul(w, a**k) for w, a in zip(ws, nodes))) for k in range(4)]
        tv = add(*(absolute(w) for w in ws))
        deviations = [m.sub(moments[1], m.qmul(lam1, p)),
                      m.sub(moments[2], m.qmul(lam2, p)),
                      m.sub(moments[3], m.rat(p))]
        remainder4 = m.ZERO
        for w, a in zip(ws, nodes):
            bracket = add(common4, m.qmul(m.mul(sp[5], exp_positive(m.qmul(S, a))), F(1, 120)))
            remainder4 = add(remainder4, m.qmul(m.mul(absolute(w), bracket), a**4))
        remainder_linear = add(m.mul(absolute(deviations[0]), b1),
                               m.mul(absolute(deviations[1]), b2),
                               m.mul(absolute(deviations[2]), b3), remainder4)
        leading_linear = m.qmul(source_unit_budget, p)
        complete_linear = add(leading_linear, remainder_linear)
        root_bound = m.mul(complete_linear, sqrt_count)
        remainder_root = m.mul(remainder_linear, sqrt_count)
        assert m.qmul(L, nodes[-1])[1] <= m.S

        checks = []
        for n, primes, leading in ((2, (2,), source2), (210, (2, 3, 5, 7), source210)):
            actual_source = m.ZERO
            for w, a in zip(ws, nodes):
                actual_d = m.ONE
                for prime in primes:
                    factor = m.sub(m.ONE, em.exp_negative(m, helper, m.qmul(m.log_int(prime), a)))
                    actual_d = m.mul(actual_d, factor)
                    source_evaluations += 1
                actual_source = add(actual_source, m.mul(w, m.qmul(actual_d, 1/a)))
            if n == 2:
                actual_source = m.sub(actual_source, m.log_int(2))
                assert actual_source[1] < 0
            else:
                assert actual_source[0] > 0
            logn = m.log_int(n)
            l2, l3 = m.square(logn), m.mul(m.square(logn), logn)
            l4, l5 = m.square(l2), m.mul(m.square(l2), logn)
            point_remainder = add(m.qmul(m.mul(absolute(deviations[0]), l2), F(1, 2)),
                                  m.qmul(m.mul(absolute(deviations[1]), l3), F(1, 6)),
                                  m.qmul(m.mul(absolute(deviations[2]), l4), F(1, 24)),
                                  m.qmul(m.mul(add(*(m.qmul(absolute(w), a**4) for w, a in zip(ws, nodes))), l5), F(1, 120)))
            difference = m.sub(actual_source, m.qmul(leading, p))
            assert absolute(difference)[1] <= point_remainder[1], (name, n, m.record(difference), m.record(point_remainder), m.record(leading))
            checks.append({'n': n, 'actual_source_error': m.record(actual_source),
                           'error_over_product': m.record(m.qmul(actual_source, 1/p)),
                           'leading_source': m.record(leading),
                           'direct_common_source_remainder': m.record(difference),
                           'point_remainder_budget': m.record(point_remainder)})
        family = {'name': name, 'nodes': list(map(str, nodes)), 'product': str(p),
                  'shape': shape_data(shapes), 'calibration_determinant': m.record(determinant),
                  'weights': list(map(m.record, ws)), 'total_variation': m.record(tv),
                  'moment_M1_over_product': m.record(m.qmul(moments[1], 1/p)),
                  'moment_M2_over_product': m.record(m.qmul(moments[2], 1/p)),
                  'moment_M3_over_product': m.record(m.qmul(moments[3], 1/p)),
                  'common_field_linear_budget': m.record(leading_linear),
                  'fourth_order_linear_remainder': m.record(remainder_linear),
                  'fourth_order_root_remainder': m.record(remainder_root),
                  'complete_matching_root_budget': m.record(root_bound),
                  'direct_source_checks': checks}
        families.append(family)
    old_root = decode(old['complete_window']['weighted_root_radius_enclosure'])
    assert decode(families[0]['complete_matching_root_budget'])[1] < old_root[0]
    assert decode(families[1]['complete_matching_root_budget'])[1] < decode(families[0]['complete_matching_root_budget'])[0]
    assert decode(families[2]['complete_matching_root_budget'])[1] < decode(families[1]['complete_matching_root_budget'])[0]
    assert decode(families[3]['complete_matching_root_budget'])[1] < decode(families[2]['complete_matching_root_budget'])[0]

    result = {
        'status': 'PASS', 'author': 'EM-DIRECT-E7559A', 'activity': 'RA-D2F111EA1C0D4B1DBEFBC1B4',
        'status_scope': 'Author derivation and computation, not independent Review or formal Result.',
        'arithmetic': 'Exact rational data and outward integer intervals scaled by 10^80; no floating certificate decisions.',
        'gamma3': {'value': m.record(gamma3), **gamma3_data},
        'density_taylor_coefficients_0_to_4': list(map(m.record, d)),
        'constant_taylor_coefficients_1_to_3': list(map(m.record, c[1:])),
        'delta': m.record(delta), 'lambda1': m.record(lam1), 'lambda2': m.record(lam2),
        'equal_spacing_alpha': m.record(m.qmul(lam1, 6)),
        'equal_spacing_beta': m.record(m.qmul(lam2, 6)),
        'calibration_consistency': {'density': m.record(density_check), 'constant': m.record(constant_check)},
        'source_polynomial': 'P(t)=t^4/24-lambda2*t^3/6+lambda1*t^2/2; S=1*(mu P(log))',
        'source_signs': {'S_2': m.record(source2), 'S_210': m.record(source210)},
        'window': {'A': A, 'B': B, 'closed_integer_count': B-A+1, 'epsilon': str(epsilon)},
        'families': families, 'old_equal_spacing_root_budget': m.record(old_root),
        'new_zeta_nodes': [entry[2] for _, entry in sorted(zeta_cache.items())],
        'new_exponential_source_factors': source_evaluations,
        'scope': 'All finite families have exact computable real calibration weights. Rational input nodes do not imply rational exact weights; old eleven polynomial matching moments are not preserved. Displayed budgets are upper bounds, not lower bounds on actual error. No old road samples or old energy windows are recomputed.',
        'dependencies': [
            {'input_package': 'round4', 'path': str(path.relative_to(args.previous)),
             'sha256': hashlib.sha256(path.read_bytes()).hexdigest()} for path in paths[:3]
        ] + [
            {'input_package': 'round5', 'path': str(paths[3].relative_to(args.round5)),
             'sha256': hashlib.sha256(paths[3].read_bytes()).hexdigest()}
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'lambda1': m.record(lam1), 'lambda2': m.record(lam2),
                      'families': [{k: f[k] for k in ('name', 'shape', 'total_variation', 'complete_matching_root_budget', 'fourth_order_root_remainder')} for f in families],
                      'new_exponential_source_factors': source_evaluations}, indent=2))


if __name__ == '__main__':
    main()
