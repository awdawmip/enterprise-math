#!/usr/bin/env python3
"""Focused checks for the Chebyshev thickness bridge.

Rational coefficient identities are exact. Transcendental checks use mpmath
at declared precision and are not interval certificates; general bounds are
proved in CHEBYSHEV_THICKNESS_BRIDGE.md.
"""
from fractions import Fraction
from math import prod
from pathlib import Path
import json
import mpmath as mp


def lagrange_zero(nodes):
    return [prod(nodes[k] / (nodes[k] - a)
                 for k in range(len(nodes)) if k != j)
            for j, a in enumerate(nodes)]


def cheb_t(d, x):
    if d == 0:
        return x * 0 + 1
    t0, t1 = x * 0 + 1, x
    for _ in range(2, d + 1):
        t0, t1 = t1, 2 * x * t1 - t0
    return t1


def nodes_weights(m, maximum, gain):
    d = m - 1
    s = mp.acosh(gain)
    t = s / d
    r = mp.tanh(t / 2) ** 2
    chi = mp.cosh(t)
    half_width = maximum * (1 - r) / 2
    nodes, weights = [], []
    for j in range(m):
        # chi-cos avoids cancellation at the thin endpoint.
        denominator = 2 * mp.sinh(t / 2) ** 2 + 2 * mp.sin(mp.pi * j / (2 * d)) ** 2
        nodes.append(half_width * denominator)
        endpoint = mp.mpf('0.5') if j in (0, d) else mp.mpf(1)
        weights.append((-1) ** j * endpoint * mp.sinh(t) * mp.sinh(s)
                       / (d * denominator))
    return nodes, weights, r, chi


def prime_factors(n):
    factors = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        factors.append(n)
    return factors


def road_value(a, factors):
    return mp.fprod(-mp.expm1(-a * mp.log(p)) for p in factors)


def fmt(x):
    return mp.nstr(x, 45)


def main():
    exact_checks = 0
    exact_examples = [
        [Fraction(1, 4), Fraction(1, 2)],
        [Fraction(1, 3), Fraction(2, 3), Fraction(1)],
        [Fraction(1, 3), Fraction(1, 2), Fraction(5, 6), Fraction(1)],
    ]
    for nodes in exact_examples:
        w = lagrange_zero(nodes)
        m = len(nodes)
        for k in range(m):
            assert sum(wj * a ** k for wj, a in zip(w, nodes)) == int(k == 0)
            exact_checks += 1
        assert sum(wj / a for wj, a in zip(w, nodes)) == sum(1 / a for a in nodes)
        exact_checks += 1
        chi = (nodes[-1] + nodes[0]) / (nodes[-1] - nodes[0])
        assert sum(abs(wj) for wj in w) == cheb_t(m - 1, chi)
        exact_checks += 1

    # Elementary constants sufficient for the universal L>=10 theorem.
    # e=sum 1/k!: lower >5/2; upper <11/4, with a rational geometric tail.
    factorial = 1
    partial = Fraction(1)
    for k in range(1, 9):
        factorial *= k
        partial += Fraction(1, factorial)
    e_upper = partial + Fraction(1, factorial * 9) / (1 - Fraction(1, 10))
    assert partial > Fraction(5, 2)
    assert e_upper < Fraction(11, 4)
    assert Fraction(11, 4) ** 2 < 8
    assert Fraction(128, 3) / Fraction(5, 2) ** 5 < Fraction(1, 2)
    exact_checks += 4

    coefficient_cases = []
    pointwise_cases = 0
    largest_error_ratio = mp.mpf(0)
    sample_numbers = sorted(set(range(2, 90)) | {121, 210, 343, 1024, 2310, 30030})
    for m in [2, 3, 4, 8, 16, 32]:
        mp.mp.dps = 100 + 3 * m
        for maximum, gain in [(mp.mpf('0.5'), mp.mpf(3)),
                              (mp.mpf('0.125'), mp.mpf(2))]:
            nodes, w, r, chi = nodes_weights(m, maximum, gain)
            d = m - 1
            s = mp.acosh(gain)
            product_formula = maximum ** m * 4 ** (1 - mp.mpf(m)) * (1-r) ** m * mp.sinh(s/d) * mp.sinh(s)
            product_direct = mp.fprod(nodes)
            tolerance = mp.mpf(10) ** (-(mp.mp.dps - 30))
            assert abs(product_formula / product_direct - 1) < tolerance
            assert abs(mp.fsum(abs(v) for v in w) - gain) < tolerance
            direct_w = lagrange_zero(nodes)
            assert max(abs(x-y) for x, y in zip(w, direct_w)) < tolerance
            for k in range(m):
                assert abs(mp.fsum(v*a**k for v, a in zip(w, nodes)) - int(k == 0)) < tolerance
            assert abs(mp.fsum(v/a for v, a in zip(w, nodes)) - mp.fsum(1/a for a in nodes)) < tolerance
            for n in sample_numbers:
                factors = prime_factors(n)
                target = mp.log(factors[0]) if len(factors) == 1 else mp.mpf(0)
                value = mp.fsum(v * road_value(a, factors) / a for v, a in zip(w, nodes))
                lograd = mp.fsum(mp.log(p) for p in factors)
                bound = product_direct * lograd ** (m+1) / mp.factorial(m+1)
                ratio = abs(value-target) / bound
                assert ratio <= 1 + mp.mpf('1e-50')
                largest_error_ratio = max(largest_error_ratio, ratio)
                pointwise_cases += 1
            coefficient_cases.append({'m':m, 'maximum':fmt(maximum), 'gain':fmt(gain),
                                      'minimum':fmt(nodes[0]), 'product':fmt(product_direct),
                                      'raw_gain':fmt(mp.fsum(abs(v)/a for v,a in zip(w,nodes)))})

    adaptive = []
    mp.mp.dps = 160
    for Z in [mp.mpf(30000), mp.mpf(10)**6, mp.mpf(10)**12, mp.mpf(10)**30]:
        L = mp.log(Z)
        m = int(mp.ceil(L))
        nodes, w, r, chi = nodes_weights(m, mp.mpf('0.5'), mp.mpf(3))
        product_value = mp.fprod(nodes)
        delta_bound = product_value * L**(m+1)/mp.factorial(m+1)
        simple_delta = mp.mpf(128)/(3*L)*(mp.e/8)**m
        assert delta_bound <= simple_delta
        records=[]
        for theta in [mp.mpf('0.5'),mp.mpf('0.6'),mp.mpf('0.9')]:
            relative_bound=delta_bound*L*Z**(1-theta)
            theorem_bound=mp.mpf(128)/3*Z**(-theta)
            assert relative_bound<=theorem_bound<mp.mpf('0.5')
            records.append({'theta':fmt(theta),'error_over_y_theta_bound':fmt(relative_bound),
                            'simplified_uniform_bound':fmt(theorem_bound)})
        adaptive.append({'Z':fmt(Z),'m':m,'minimum_thickness':fmt(nodes[0]),
                         'maximum_thickness':fmt(nodes[-1]),'normalized_gain':fmt(mp.fsum(abs(v)for v in w)),
                         'raw_gain':fmt(mp.fsum(abs(v)/a for v,a in zip(w,nodes))),
                         'pointwise_bound_all_n_up_to_Z':fmt(delta_bound),'windows':records})

    output={'status':'PASS','proof':'CHEBYSHEV_THICKNESS_BRIDGE.md',
            'arithmetic':'Fraction exact for rational node moments and elementary constant bounds; mpmath 100+3m or 160 digits otherwise, not interval arithmetic.',
            'exact_checks':exact_checks,'coefficient_cases':coefficient_cases,
            'pointwise_road_cases':pointwise_cases,'largest_error_bound_ratio':fmt(largest_error_ratio),
            'adaptive_order_cases':adaptive,
            'scope':'General minimax and window bounds have analytic proofs. Finite checks do not prove the remaining subpower positive-window energy target.'}
    Path(__file__).with_name('chebyshev_results.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':output['status'],'exact_checks':exact_checks,
                      'coefficient_cases':len(coefficient_cases),'pointwise_cases':pointwise_cases,
                      'max_ratio':fmt(largest_error_ratio),'adaptive':[{'Z':v['Z'],'m':v['m'],'minimum':v['minimum_thickness'],'gain':v['normalized_gain']}for v in adaptive]},ensure_ascii=False))


if __name__=='__main__':
    main()
