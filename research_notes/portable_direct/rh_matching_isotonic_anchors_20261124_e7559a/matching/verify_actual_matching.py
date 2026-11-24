#!/usr/bin/env python3
"""Author checks for shrinking-thickness matching and its positive convolution.

The unbounded statements are proved in ACTUAL_MATCHING_SCALE_AND_LAPLACE.md.
This script checks exact polynomial seams for the prior rational families and
directed interval seams for one complete finite shrinking-thickness source.
It does not claim independent Review or test the unsolved prime deficit bound.
"""
from fractions import Fraction as F
from math import comb, factorial, prod
from pathlib import Path
import argparse
import importlib.util
import json
import sys

sys.dont_write_bytecode = True


def poly_mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def poly_product_linear(nodes):
    out = [F(1)]
    for a in nodes:
        out = poly_mul(out, [a, F(1)])
    return out


def cheb(m, x):
    if m == 0:
        return F(1)
    u, v = F(1), x
    for _ in range(1, m):
        u, v = v, 2*x*v-u
    return v


def log_interval(x, count=160):
    z = (x-1)/(x+1)
    assert 0 < z < 1
    lower = 2*sum((z**(2*j+1)/F(2*j+1) for j in range(count)), F(0))
    tail = 2*z**(2*count+1)/(F(2*count+1)*(1-z*z))
    return lower, lower+tail


def rounded_interval(lo, hi, digits=45):
    scale = 10**digits
    return [str((lo*scale).__floor__())+'/'+str(scale),
            str(-(-hi*scale).__floor__())+'/'+str(scale)]


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def exp_negative_small(m, x):
    assert 0 <= x[0] <= x[1] <= m.S
    term = total = m.ONE
    even = total
    for j in range(1, 102):
        term = m.qmul(m.mul(term, x), 1, j)
        total = m.add(total, m.neg(term) if j % 2 else term)
        if j == 100:
            even = total
    return total[0], even[1]


def exp_positive_small(m, x):
    assert 0 <= x[0] <= x[1] <= m.S
    term = total = m.ONE
    for j in range(1,81):
        term = m.qmul(m.mul(term,x),1,j)
        total = m.add(total,term)
    # Taylor's remainder on [0,1] is at most e/81! < 3/81!.
    return total[0], m.add(total,m.rat(F(3,factorial(81))))[1]


def interval_overlap(x, y):
    return max(x[0], y[0]) <= min(x[1], y[1])


def exact_chebyshev_checks(prior):
    data = json.loads((prior/'matching_order/matching_order_certificate.json').read_text())
    rows = []
    for row in data['families']:
        nodes, weights = list(map(F, row['nodes'])), list(map(F, row['weights']))
        count = len(nodes)
        actual_weights = [prod((b/(b-a) for i,b in enumerate(nodes) if i != j), start=F(1))
                          for j,a in enumerate(nodes)]
        assert weights == actual_weights
        numerator = [F(0)] * count
        for j, (a, v) in enumerate(zip(nodes, weights)):
            poly = poly_product_linear(nodes[:j]+nodes[j+1:])
            for i, coefficient in enumerate(poly):
                numerator[i] += a*v*coefficient
        assert numerator == [prod(nodes, start=F(1))] + [F(0)]*(count-1)
        assert [sum((v*a**k for v,a in zip(weights,nodes)), F(0))
                for k in range(count)] == [F(1)] + [F(0)]*(count-1)
        transforms = []
        for s in (F(2,5), F(1)):
            h = prod((a/(a+s) for a in nodes), start=F(1))
            z = 1+4*s  # theta=1/2.
            perturb_bound = F(32,31)**2/cheb(count,z)
            assert h <= perturb_bound
            if s == F(2,5):
                elementary_bound = F(2048,961)*F(1,5**count)
                assert h <= elementary_bound
            transforms.append({'s':str(s),'H_exact':str(h),
                               'perturbation_bound':str(perturb_bound)})
        rows.append({'m':count,'zero_extrapolation_weights_exact':True,
                     'partial_fraction_polynomial_exact':True,
                     'matching_moments_checked':count,'laplace_bounds':transforms})
    return rows


def fixed_count_checks():
    rows = []
    for count in range(1,13):
        q = 128*count
        nodes = [F(j,q) for j in range(1,count+1)]
        weights = [F((-1)**(j-1)*comb(count,j)) for j in range(1,count+1)]
        direct = [prod((b/(b-a) for i,b in enumerate(nodes) if i != j),start=F(1))
                  for j,a in enumerate(nodes)]
        assert weights == direct
        assert [sum((v*a**r for a,v in zip(nodes,weights)),F(0))
                for r in range(count)] == [F(1)]+[F(0)]*(count-1)
        assert sum(map(abs,weights),F(0)) == 2**count-1
        assert prod(nodes,start=F(1))/factorial(count+1) == F(1,(count+1)*q**count)
        rows.append({'m':count,'Q':q,'moments_checked':count,
                     'weight_total_variation':str(2**count-1),
                     'remainder_coefficient':str(F(1,(count+1)*q**count))})
    return rows


def finite_source_checks(prior, bound=256):
    path = prior/'prior/riemann_cumulative_haar_20261123/dependencies/certify_fast_harmonic_energy.py'
    m = load_module('matching_harmonic_interval', path)
    factors = [[] for _ in range(bound+1)]
    for p in range(2,bound+1):
        if not factors[p]:
            for n in range(p,bound+1,p):
                factors[n].append(p)
    mobius = [0]*(bound+1)
    mobius[1] = 1
    for n in range(2,bound+1):
        mobius[n] = 0 if any(n%(p*p) == 0 for p in factors[n]) else (-1)**len(factors[n])
    a = F(1,bound)
    one_minus = {p:m.sub(m.ONE,exp_negative_small(m,m.qmul(m.log_int(p),a)))
                 for p in range(2,bound+1) if factors[p] == [p]}
    source, error, remainder = {1:m.ZERO}, {1:m.ZERO}, {1:m.ZERO}
    for n in range(2,bound+1):
        value = m.ONE
        for p in factors[n]:
            value = m.mul(value,one_minus[p])
        source[n] = m.qmul(value,bound)
        reference = m.log_int(factors[n][0]) if len(factors[n]) == 1 else m.ZERO
        error[n] = m.sub(source[n],reference)
        l = m.log_int(n)
        f = m.qmul(m.sub(m.ONE,exp_negative_small(m,m.qmul(l,a))),bound)
        remainder[n] = m.sub(l,f)
        assert remainder[n][0] > 0
        radius = m.qmul(m.mul(l,l),1,2*bound)[1]
        assert -radius <= error[n][0] <= error[n][1] <= radius
        assert error[n][1] < 0 if len(factors[n]) == 1 else error[n][0] > 0
    for n in range(1,bound+1):
        lifted = m.ZERO
        for d in range(1,n+1):
            if n%d == 0 and mobius[d]:
                lifted = m.add(lifted,m.qmul(remainder[d],mobius[d]))
        assert interval_overlap(error[n],lifted)
    harmonic = [m.ZERO]
    for n in range(1,bound+1):
        harmonic.append(m.add(harmonic[-1],m.rat(F(1,n))))
    zupper = sum((F(1,j*j) for j in range(1,257)),F(0))+F(1,256)
    elower = sum((F(1,factorial(j)) for j in range(25)),F(0))
    h1 = a/(a+1)
    s0 = s1 = lambda_sum = abs_source_sum = m.ZERO
    endpoint = None
    for y in range(1,bound+1):
        s0 = m.add(s0,error[y])
        s1 = m.add(s1,m.qmul(error[y],1,y))
        if y >= 2:
            reference = m.log_int(factors[y][0]) if len(factors[y]) == 1 else m.ZERO
            lambda_sum = m.add(lambda_sum,m.qmul(reference,1,y))
            absolute_error = m.neg(error[y]) if len(factors[y]) == 1 else error[y]
            abs_source_sum = m.add(abs_source_sum,m.qmul(absolute_error,1,y))
        direct = m.sub(m.qmul(s1,y),s0)
        lifted = m.ZERO
        for d in range(2,y+1):
            if mobius[d]:
                count = y//d
                kernel = m.sub(m.qmul(harmonic[count],y,d),m.rat(count))
                lifted = m.add(lifted,m.qmul(m.mul(remainder[d],kernel),mobius[d]))
        assert interval_overlap(direct,lifted)
        l = m.log_int(y)
        exponent = exp_positive_small(m,m.qmul(lambda_sum,a))
        average_radius = m.qmul(m.add(m.mul(l,lambda_sum),
            m.mul(m.mul(lambda_sum,lambda_sum),exponent)),a/2)
        assert abs_source_sum[1] <= average_radius[1]
        average_point_radius = m.qmul(average_radius,y)[1]
        shrinking_radius = m.qmul(m.mul(m.mul(l,l),l),y,2*bound)[1]
        laplace_radius = m.rat(h1*zupper*F(y*y,1)/(2*elower))[1]
        assert -shrinking_radius <= direct[0] <= direct[1] <= shrinking_radius
        assert -laplace_radius <= direct[0] <= direct[1] <= laplace_radius
        assert -average_point_radius <= direct[0] <= direct[1] <= average_point_radius
        endpoint = {'y':y,'actual_road_difference':m.record(direct),
                    'shrinking_radius_upper':m.record((shrinking_radius,shrinking_radius)),
                    'laplace_radius_upper':m.record((laplace_radius,laplace_radius))}
        endpoint['arithmetic_average_radius_upper'] = m.record((average_point_radius,average_point_radius))
    return {'B':bound,'a':str(a),'unit_convention_D1':0,
            'source_sign_and_radius_checks':bound-1,
            'mobius_source_identity_interval_checks':bound,
            'full_prefix_identity_interval_checks':bound,
            'full_prefix_bound_interval_checks':2*bound,
            'arithmetic_average_source_interval_checks':bound,
            'arithmetic_average_point_interval_checks':bound,
            'arithmetic':'outward fixed-denominator intervals from prior harmonic module; Taylor100/101 exponential enclosure',
            'endpoint':endpoint}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prior',type=Path,required=True,
                        help='root of riemann_directed_local_20261124 prior package')
    parser.add_argument('--output',type=Path,
                        default=Path(__file__).with_name('actual_matching_certificate.json'))
    args = parser.parse_args()
    cheb_rows = exact_chebyshev_checks(args.prior)
    fixed_rows = fixed_count_checks()
    lo,hi = log_interval(F(5))
    exponents = []
    for c in (F(14,25),F(3,5)):
        elo,ehi = c*lo-F(9,10),c*hi-F(9,10)
        assert elo > 0
        exponents.append({'c':str(c),'positive_decay_exponent':rounded_interval(elo,ehi),
                          'strictly_positive':True})
    actual = finite_source_checks(args.prior)
    result = {'schema':'RH_ACTUAL_MATCHING_SCALE_LAPLACE_V1',
              'status':'AUTHOR_EXACT_AND_INTERVAL_CHECKS_NOT_INDEPENDENT_REVIEW',
              'scope':'New scale family and positive-convolution seams; no arithmetic prime-deficit acceptance',
              'coverage':{'chebyshev_families':len(cheb_rows),
                          'partial_fraction_polynomial_identities':len(cheb_rows),
                          'chebyshev_matching_moments':sum(x['m'] for x in cheb_rows),
                          'rational_laplace_bounds':2*len(cheb_rows),
                          'fixed_count_families':len(fixed_rows),
                          'fixed_count_matching_moments':sum(x['m'] for x in fixed_rows)},
              'decay_exponents':exponents,'chebyshev_rows':cheb_rows,
              'fixed_count_rows':fixed_rows,'finite_source':actual}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'coverage':result['coverage'],'decay_exponents':exponents,
                      'finite_source_coverage':{k:v for k,v in actual.items() if k!='endpoint'}},
                     ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
