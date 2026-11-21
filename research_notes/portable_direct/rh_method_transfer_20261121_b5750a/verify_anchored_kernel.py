#!/usr/bin/env python3
"""Reproduce anchored-kernel checks; mpmath 1.3-compatible, no network.

The finite periodic tests use exact Fraction arithmetic. The analytic-kernel
tests use high precision and an explicit truncation error bound. They are
checks of the written proof, not a proof of the RH road estimate.
"""
from fractions import Fraction
from pathlib import Path
import json
import math

import mpmath as mp

mp.mp.dps = 60


def kernel(theta, phi):
    z = mp.exp(1j * theta)
    v = mp.exp(-1j * phi)
    return z * v / ((1 - z) * (1 - v)) * (
        mp.zeta(2) - mp.polylog(2, z) - mp.polylog(2, v)
        + mp.polylog(2, z * v)
    )


def cos_kernel(theta, phi):
    return mp.re(kernel(theta, phi) + kernel(theta, -phi)) / 2


def low_limit(x, y):
    def tlog(t):
        return mp.mpf(0) if t == 0 else t * mp.log(abs(t))
    return (mp.pi / 2 * (abs(x) + abs(y) - abs(x - y))
            + 1j * (tlog(x) - tlog(y) - tlog(x - y))) / (x * y)


def mobius(n):
    result = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            result = -result
            if n % p == 0:
                return 0
        p += 1
    return -result if n > 1 else result


def ramanujan(q, n):
    # c_q(n) = sum_{d | gcd(q,n)} d mu(q/d), exact integer.
    g = math.gcd(q, n)
    return sum(d * mobius(q // d) for d in range(1, g + 1) if g % d == 0)


def beta_at_one(q):
    factors = [p for p in range(2, q + 1)
               if q % p == 0 and all(p % d for d in range(2, math.isqrt(p) + 1))]
    return Fraction(mobius(q), math.prod(p * p - 1 for p in factors))


def num(value):
    return mp.nstr(value, 30)


def main():
    data = {"normalization": "h_N(theta)=sum_{n=1}^N exp(i*n*theta); angles in radians",
            "precision_decimal_digits": mp.mp.dps}

    finite_checks = []
    cutoff = 30000
    pairs = [(mp.mpf('0.7'), mp.mpf('1.9')),
             (mp.mpf('0.7'), mp.mpf('0.7')),
             (mp.mpf('0.7'), mp.mpf('-1.9'))]
    for theta, phi in pairs:
        z, w = mp.exp(1j * theta), mp.exp(1j * phi)
        zn = wn = mp.mpc(1)
        hn = kn = mp.mpc(0)
        direct = mp.mpc(0)
        for n in range(1, cutoff + 1):
            zn *= z
            wn *= w
            hn += zn
            kn += wn
            direct += hn * mp.conj(kn) / (n * n)
        closed = kernel(theta, phi)
        error = abs(closed - direct)
        # |h_N| <= 2/|1-z| and sum_{N>M} N^-2 <= 1/M.
        bound = 4 / (abs(1 - z) * abs(1 - w) * cutoff)
        assert error <= bound
        finite_checks.append({"theta": num(theta), "phi": num(phi),
                              "cutoff": cutoff, "absolute_error": num(error),
                              "proved_tail_bound": num(bound), "pass": True})
    data["closed_kernel_vs_direct_prefix_sum"] = finite_checks

    low_checks = []
    for x, y in [(mp.mpf(1), mp.mpf(2)), (mp.mpf(1), mp.mpf(-2)),
                 (mp.mpf(1), mp.mpf(1)), (mp.mpf(1), mp.mpf('1.01'))]:
        target = low_limit(x, y)
        values = []
        errors = []
        for eps in [mp.mpf('0.01'), mp.mpf('0.001'), mp.mpf('0.0001')]:
            scaled = eps * kernel(eps * x, eps * y)
            err = abs(scaled - target)
            errors.append(err)
            values.append({"epsilon": num(eps), "scaled_real": num(mp.re(scaled)),
                           "scaled_imag": num(mp.im(scaled)), "absolute_error": num(err)})
        assert errors[2] < errors[1] < errors[0]
        assert errors[2] < mp.mpf('0.002')
        low_checks.append({"x": num(x), "y": num(y),
                           "limit_real": num(mp.re(target)),
                           "limit_imag": num(mp.im(target)), "values": values, "pass": True})
    data["low_frequency_complex_limit"] = low_checks

    eps = mp.mpf('0.0001')
    cos_checks = []
    for x, y in [(mp.mpf(1), mp.mpf(2)), (mp.mpf(1), mp.mpf('1.01'))]:
        kxy = cos_kernel(eps * x, eps * y)
        kxx = cos_kernel(eps * x, eps * x)
        kyy = cos_kernel(eps * y, eps * y)
        rho = kxy / mp.sqrt(kxx * kyy)
        limit = mp.sqrt(min(x, y) / max(x, y))
        assert abs(rho - limit) < mp.mpf('0.002')
        cos_checks.append({"x": num(x), "y": num(y), "epsilon": num(eps),
                           "scaled_kernel": num(eps * kxy),
                           "scaled_limit": num(mp.pi / (2 * max(x, y))),
                           "correlation": num(rho), "correlation_limit": num(limit),
                           "off_diagonal_over_diagonal_for_equal_coefficients": num(2*kxy/(kxx+kyy)),
                           "pass": True})
    data["paired_real_frequency_limit"] = cos_checks

    # Exact certificate for the scaled, real low-frequency Gram kernel.
    xs = [Fraction(1), Fraction(2), Fraction(3), Fraction(5)]
    amplitudes = [Fraction(2), Fraction(-3), Fraction(5), Fraction(-2)]
    variances = [1/x for x in xs] + [Fraction(0)]
    quadratic = sum(amplitudes[i]*amplitudes[j]*min(variances[i], variances[j])
                    for i in range(len(xs)) for j in range(len(xs)))
    prefix_square = sum((variances[k]-variances[k+1])*sum(amplitudes[:k+1])**2
                        for k in range(len(xs)))
    assert quadratic == prefix_square
    data["exact_low_frequency_min_kernel_certificate"] = {
        "frequencies": [str(x) for x in xs],
        "signed_amplitudes": [str(v) for v in amplitudes],
        "quadratic_without_pi_over_two": str(quadratic),
        "prefix_square_sum_without_pi_over_two": str(prefix_square),
        "pass": True}

    # Exact finite-frequency positive-integral certificates, including the
    # distinguished constant port. Compare different formulae and direct sums.
    angles = [mp.mpf('0.17'), mp.mpf('0.53'), mp.mpf('1.9')]
    real_amplitudes = [mp.mpf('1.25'), mp.mpf('-0.75'), mp.mpf('2')]
    anchor = mp.mpf('0.4')
    us = [aa*mp.cot(th/2)/2 for aa, th in zip(real_amplitudes, angles)]
    mean = sum(uu*th for uu, th in zip(us, angles))/mp.pi
    es_gram = mp.pi/2*sum(us[i]*us[j]*min(angles[i], angles[j])
                          for i in range(3) for j in range(3))
    es_gram -= sum(uu*th for uu, th in zip(us, angles))**2/2
    er_gram = mp.pi/8*sum(real_amplitudes[i]*real_amplitudes[j]*min(angles[i], angles[j])
                          for i in range(3) for j in range(3))
    er_gram += anchor*sum(aa*(mp.pi*th/2-th*th/4)
                          for aa, th in zip(real_amplitudes, angles))
    er_gram += anchor*anchor*mp.zeta(2)
    endpoints = [mp.mpf(0)] + angles + [mp.pi]
    es_integral = er_integral = mp.mpf(0)
    for k, (left, right) in enumerate(zip(endpoints[:-1], endpoints[1:])):
        tail_u = sum(us[k:])
        tail_a = sum(real_amplitudes[k:])
        es_integral += mp.pi/2*(right-left)*(tail_u-mean)**2
        const = tail_a+2*anchor
        slope = -2*anchor/mp.pi
        er_integral += mp.pi/8*(const**2*(right-left)
                               +const*slope*(right**2-left**2)
                               +slope**2*(right**3-left**3)/3)
    assert abs(es_integral-es_gram) < mp.mpf('1e-55')
    assert abs(er_integral-er_gram) < mp.mpf('1e-55')
    full = sum(real_amplitudes[i]*real_amplitudes[j]*cos_kernel(angles[i], angles[j])
               for i in range(3) for j in range(3))
    for aa, th in zip(real_amplitudes, angles):
        z = mp.exp(1j*th)
        ell = z/(1-z)*(mp.zeta(2)-mp.polylog(2,z))
        full -= 2*anchor*aa*mp.re(ell)
    full += anchor*anchor*mp.zeta(2)
    def cl2(t):
        return mp.im(mp.polylog(2, mp.exp(1j*t)))
    cross = sum(us[i]*(sum(real_amplitudes[j]*(cl2(angles[i]+angles[j])
                        +cl2(angles[i]-angles[j])-2*cl2(angles[i]))/4 for j in range(3))
                        -anchor*cl2(angles[i])) for i in range(3))
    assert abs(full-es_gram-er_gram-2*cross) < mp.mpf('1e-55')
    lower, upper = (mp.sqrt(es_gram)-mp.sqrt(er_gram))**2, (mp.sqrt(es_gram)+mp.sqrt(er_gram))**2
    assert lower <= full <= upper
    cutoff3 = 20000
    direct_es = direct_er = mp.mpf(0)
    for n in range(1, cutoff3+1):
        sine_value = sum(uu*mp.sin(n*th) for uu, th in zip(us, angles))
        rest_value = sum(aa*(mp.cos(n*th)-1)/2 for aa, th in zip(real_amplitudes, angles))-anchor
        direct_es += sine_value*sine_value/(n*n)
        direct_er += rest_value*rest_value/(n*n)
    bound_s = sum(abs(uu) for uu in us)**2/cutoff3
    bound_r = (sum(abs(aa) for aa in real_amplitudes)+abs(anchor))**2/cutoff3
    assert 0 <= es_gram-direct_es <= bound_s
    assert 0 <= er_gram-direct_er <= bound_r
    data["finite_frequency_positive_integral_certificate"] = {
        "angles": [num(t) for t in angles],
        "real_amplitudes": [num(a) for a in real_amplitudes],
        "anchor": num(anchor), "cutoff": cutoff3,
        "sine_energy": num(es_gram), "rest_and_anchor_energy": num(er_gram),
        "sine_direct_tail": num(es_gram-direct_es), "sine_proved_tail_bound": num(bound_s),
        "rest_direct_tail": num(er_gram-direct_er), "rest_proved_tail_bound": num(bound_r),
        "gram_matches_piecewise_polynomial_integrals": True,
        "sine_rest_cross_term": num(cross), "clausen_matches_full_complex_kernel": True,
        "full_energy_from_complex_kernel": num(full),
        "cauchy_schwarz_lower": num(lower), "cauchy_schwarz_upper": num(upper), "pass": True}

    # Exact finite-Ramanujan projection retains the anchor and all cross terms.
    qs = [2, 3, 5, 6]
    coeffs = [beta_at_one(q) for q in qs]
    b = Fraction(7, 5)
    period = math.lcm(*qs)
    cutoff = 127
    cumulative = [0] * len(qs)
    gram = [[Fraction(0) for _ in qs] for _ in qs]
    linear = [Fraction(0) for _ in qs]
    constant = Fraction(0)
    direct_energy = Fraction(0)
    prefix_values = []
    for n in range(1, cutoff + 1):
        cumulative = [v + ramanujan(q, n) for q, v in zip(qs, cumulative)]
        weight = Fraction(1, n*n)
        centered = sum(c*v for c, v in zip(coeffs, cumulative)) - b
        direct_energy += weight * centered*centered
        if n <= period:
            prefix_values.append(centered)
        for i in range(len(qs)):
            linear[i] += weight*cumulative[i]
            for j in range(len(qs)):
                gram[i][j] += weight*cumulative[i]*cumulative[j]
        constant += weight
    assembled = sum(coeffs[i]*coeffs[j]*gram[i][j]
                    for i in range(len(qs)) for j in range(len(qs)))
    assembled -= 2*b*sum(c*l for c, l in zip(coeffs, linear))
    assembled += b*b*constant
    residue_assembled = sum(prefix_values[(n-1) % period]**2 * Fraction(1, n*n)
                            for n in range(1, cutoff+1))
    assert direct_energy == assembled == residue_assembled
    # Diagonal-only calculation is not the same anchored observer.
    diagonal_only = sum(c*c*gram[i][i] for i, c in enumerate(coeffs))
    diagonal_only -= 2*b*sum(c*l for c, l in zip(coeffs, linear))
    diagonal_only += b*b*constant
    assert diagonal_only != direct_energy
    data["exact_ramanujan_gram_and_residue_check"] = {
        "moduli": qs, "coefficients": [str(c) for c in coeffs],
        "anchor_constant": str(b), "period": period, "cutoff": cutoff,
        "direct_equals_full_gram_equals_residue_formula": True,
        "off_diagonal_contribution_exact": str(direct_energy-diagonal_only),
        "direct_energy_decimal": num(mp.mpf(direct_energy.numerator)/direct_energy.denominator),
        "diagonal_only_decimal": num(mp.mpf(diagonal_only.numerator)/diagonal_only.denominator),
        "pass": True}

    # Infinite periodic formula checked against a directly summed finite prefix
    # with a rigorous upper bound for the omitted, nonnegative tail.
    infinite_periodic = sum(mp.mpf(f.numerator)**2/(f.denominator*f.denominator)
                            * mp.polygamma(1, mp.mpf(r)/period)/(period*period)
                            for r, f in enumerate(prefix_values, start=1))
    # Directly sum 100000 entries using the exactly constructed periodic values.
    cutoff2 = 100000
    periodic_numeric = [mp.mpf(f.numerator)/f.denominator for f in prefix_values]
    direct_numeric = sum(periodic_numeric[(n-1) % period]**2/(n*n)
                         for n in range(1, cutoff2+1))
    tail_bound = max(abs(f)**2 for f in periodic_numeric)/cutoff2
    assert 0 <= infinite_periodic-direct_numeric <= tail_bound
    data["infinite_periodic_formula_check"] = {
        "period": period, "direct_cutoff": cutoff2,
        "infinite_energy": num(infinite_periodic),
        "direct_energy": num(direct_numeric),
        "nonnegative_difference": num(infinite_periodic-direct_numeric),
        "proved_tail_bound": num(tail_bound), "pass": True}

    # Check the exact n=1 anchor reconstruction, where all tail signs agree.
    anchor_checks = []
    for thickness in [mp.mpf('0.5'), mp.mpf('0.25'), mp.mpf('0.1')]:
        qmax = 256
        ca = 1/mp.zeta(1+thickness)
        positive_sum = mp.mpf(0)
        for q in range(2, qmax+1):
            if mobius(q) == 0:
                continue
            prime_factors = [p for p in range(2, q+1) if q % p == 0
                             and all(p % d for d in range(2, math.isqrt(p)+1))]
            positive_sum += 1/mp.fprod(p**(1+thickness)-1 for p in prime_factors)
        tail = 1-ca*(1+positive_sum)
        cut_anchor = ca*positive_sum-1-ca/2
        true_anchor = -3*ca/2
        bound = mp.power(qmax, -thickness)/(32*mp.log(2))
        assert tail >= bound
        assert abs(cut_anchor+tail-true_anchor) < mp.mpf('1e-55')
        anchor_checks.append({"thickness": num(thickness), "cutoff": qmax,
                              "positive_anchor_tail": num(tail),
                              "proved_lower_bound": num(bound),
                              "uncompensated_anchor": num(cut_anchor),
                              "true_and_compensated_anchor": num(true_anchor),
                              "pass": True})
    data["anchor_tail_and_exact_compensation"] = anchor_checks
    data["all_checks_passed"] = True
    target = Path(__file__).with_name('anchored_kernel_results.json')
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({"all_checks_passed": True, "output": str(target)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
