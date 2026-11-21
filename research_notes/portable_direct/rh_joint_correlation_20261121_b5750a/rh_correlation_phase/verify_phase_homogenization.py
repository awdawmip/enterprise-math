#!/usr/bin/env python3
"""Exact identities and directed interval checks for divisor-phase removal.

Run from any directory with the sibling rh_correlation_rational directory present.
The general theorems are proved in PHASE_HOMOGENIZATION.md. Finite checks below
exercise jumps, common factors, anchored windows, and actual matched-road data.
Only integers and Fraction enter certificates; elapsed time is diagnostic only.
"""
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path
import hashlib
import json
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from rh_correlation_rational.certify_matched_nodes import (  # noqa: E402
    Elementary, ZERO, ONE, SCALE, DIGITS, rat, add, sub, neg, scale,
    mul, ceildiv, floor_root, linear_sieve, render,
)


def isum(xs):
    result = ZERO
    for x in xs:
        result = add(result, x)
    return result


def square(x):
    lo = 0 if x[0] <= 0 <= x[1] else min(x[0] ** 2, x[1] ** 2)
    return lo // SCALE, ceildiv(max(x[0] ** 2, x[1] ** 2), SCALE)


def overlap(x, y):
    return max(x[0], y[0]) <= min(x[1], y[1])


def output(x):
    return {**render(x, 28), 'integer_bounds': [str(x[0]), str(x[1])],
            'denominator_power_of_10': DIGITS}


def B(d, n):
    r = n % d
    return F(d * d - 1, 12 * d) - F(r * (d - r), 2 * d)


def gram(d, e):
    g = gcd(d, e)
    return F(g ** 4 + 10 * g * g - 11, 720 * d * e)


def jordan(n, exponent, spf):
    value = n ** exponent
    k = n
    while k > 1:
        p = spf[k]
        value = value // p ** exponent * (p ** exponent - 1)
        while k % p == 0:
            k //= p
    return value


def p_add(x, y):
    z = [F(0)] * max(len(x), len(y))
    for i, a in enumerate(x):
        z[i] += a
    for i, a in enumerate(y):
        z[i] += a
    while len(z) > 1 and not z[-1]:
        z.pop()
    return z


def p_mul(x, y):
    z = [F(0)] * (len(x) + len(y) - 1)
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            z[i + j] += a * b
    return z


def p_scale(x, k):
    return [k * a for a in x]


def exact_checks():
    poisson = 0
    for d in range(1, 25):
        assert sum(B(d, r) for r in range(d)) == 0
        for r in range(d):
            assert 2 * B(d, r) - B(d, r - 1) - B(d, r + 1) == F(int(r == 0)) - F(1, d)
            poisson += 1
    gram_count = 0
    for d in range(1, 25):
        for e in range(1, 25):
            period = lcm(d, e)
            direct = sum(B(d, r) * B(e, r) for r in range(period)) / period
            assert direct == gram(d, e)
            gram_count += 1

    a1 = [F(-1, 2), F(1, 2)]
    a2 = [F(2, 6), F(-3, 6), F(1, 6)]
    a3 = [F(-6, 24), F(11, 24), F(-6, 24), F(1, 24)]
    a4 = [F(24, 120), F(-50, 120), F(35, 120), F(-10, 120), F(1, 120)]
    a12 = p_mul(a1, a1)
    S2 = p_add(a12, p_scale(a2, -2))
    S3 = p_add(p_add(p_mul(a12, a1), p_scale(p_mul(a1, a2), -3)), p_scale(a3, 3))
    S4 = p_add(p_add(p_add(p_add(p_mul(a12, a12), p_scale(p_mul(a12, a2), -4)),
                                      p_scale(p_mul(a2, a2), 2)),
                                p_scale(p_mul(a1, a3), 4)), p_scale(a4, -4))
    polynomial = p_add(p_add(S4, p_scale(S3, -2)), S2)
    assert polynomial == [F(-11, 720), F(0), F(10, 720), F(0), F(1, 720)]

    H = 8
    spf, _ = linear_sieve(H)
    coeff = {d: F((-1) ** d * (d + 3), d + 1) for d in range(2, H + 1)}
    period = lcm(*range(2, H + 1))
    direct = sum(sum(coeff[d] * B(d, n) for d in coeff) ** 2 for n in range(period)) / period
    via_gram = sum(coeff[d] * coeff[e] * gram(d, e) for d in coeff for e in coeff)
    via_roads = sum(F(jordan(s, 4, spf) + 10 * jordan(s, 2, spf), 720)
                    * sum(coeff[k] / k for k in range(s, H + 1, s)) ** 2 for s in coeff)
    assert direct == via_gram == via_roads

    harmonic = [F(0)]
    for n in range(1, 258):
        harmonic.append(harmonic[-1] + F(1, n))

    def P_without_affine_log(d, n):
        return F(n, d) * (harmonic[n] - harmonic[n // d]) - F(n % d, d) + F(d - 1, 2 * d)

    differences = 0
    for d in range(2, 33):
        for n in range(1, 257):
            p = P_without_affine_log(d, n)
            plus = P_without_affine_log(d, n + 1)
            minus = P_without_affine_log(d, n - 1)
            assert plus - p == (harmonic[n] - harmonic[n // d]) / d
            assert 2 * p - plus - minus == (F(int(n % d == 0)) - F(1, d)) / n
            differences += 1
    return {
        'periodic_Poisson_residue_identities': poisson,
        'common_period_Gram_pairs': gram_count,
        'universal_root_sum_polynomial_identity': True,
        'three_way_joint_variance_exact': str(direct),
        'three_way_joint_variance_period': period,
        'harmonic_first_and_second_difference_pairs': differences,
        'arithmetic': 'exact Fraction; no tolerance',
    }


def actual_coefficients(elementary, nodes, weights, limit):
    spf, mu = linear_sieve(limit)
    kappa = [ZERO] * (limit + 1)
    kappa[1] = scale(elementary.log_integer(2), 2)
    for n in range(2, limit + 1):
        kappa[n] = scale(add(sub(scale(elementary.log_integer(n + 1), n + 1),
                                    scale(elementary.log_integer(n), 2 * n)),
                                scale(elementary.log_integer(n - 1), n - 1)), n)
    b_kappa = [ZERO] * (limit + 1)
    for k in range(1, limit + 1):
        if mu[k]:
            for n in range(k, limit + 1, k):
                b_kappa[n] = add(b_kappa[n], scale(kappa[n // k], mu[k]))
    c = [ZERO] * (limit + 1)
    c[1] = neg(kappa[1])
    for n in range(2, limit + 1):
        ln = elementary.log_integer(n)
        psi = isum(scale(sub(ONE, elementary.exp_negative(scale(ln, a))), w / a)
                   for a, w in zip(nodes, weights))
        c[n] = sub(scale(psi, -mu[n]), b_kappa[n])
        envelope = add(ln, sub(scale(elementary.log_integer(2), 2), ONE))
        assert max(abs(c[n][0]), abs(c[n][1])) <= envelope[0]

    # Cross-route check: original prime-factor roads, then finite Mobius inversion.
    prime_values = {}
    D = [ZERO] * (limit + 1)
    for n in range(2, limit + 1):
        k, primes = n, []
        while k > 1:
            p = spf[k]
            primes.append(p)
            while k % p == 0:
                k //= p
        rows = []
        for j, (a, w) in enumerate(zip(nodes, weights)):
            value = ONE
            for p in primes:
                if (p, j) not in prime_values:
                    prime_values[p, j] = sub(ONE, elementary.exp_negative(scale(elementary.log_integer(p), a)))
                value = mul(value, prime_values[p, j])
            rows.append(scale(value, w / a))
        D[n] = isum(rows)
    direct = [ZERO] * (limit + 1)
    for k in range(1, limit + 1):
        if mu[k]:
            for n in range(k, limit + 1, k):
                direct[n] = add(direct[n], scale(sub(D[n // k], kappa[n // k]), mu[k]))
    assert all(overlap(c[n], direct[n]) for n in range(1, limit + 1))
    return c, D, kappa, spf


def variance(c, H, spf):
    total = ZERO
    for s in range(2, H + 1):
        bs = isum(scale(c[k], F(1, k)) for k in range(s, H + 1, s))
        total = add(total, scale(square(bs), F(jordan(s, 4, spf) + 10 * jordan(s, 2, spf), 720)))
    return total


def tail_bound(elementary, V, A, H):
    Q = scale(add(ONE, scale(elementary.log_integer(H), 2)), H * H)
    factor = add(rat(F(8, 7 * A ** 3)), scale(Q, F(16, 15 * A ** 4)))
    return Q, mul(V, factor)


def actual_checks():
    source = ROOT / 'rh_correlation_rational' / 'rational_window_certificate.json'
    raw = source.read_bytes()
    certificate = json.loads(raw)
    nodes = [F(x) for x in certificate['node_certificate']['nodes']]
    weights = [F(x) for x in certificate['node_certificate']['weights']]
    limit, max_n = 256, certificate['window']['Z']
    elementary = Elementary()
    c, D, kappa, spf = actual_coefficients(elementary, nodes, weights, limit)
    harmonic = [ZERO]
    for n in range(1, max_n + 1):
        harmonic.append(add(harmonic[-1], rat(F(1, n))))

    def P(d, n):
        if n == 0:
            return rat(F(d - 1, 2 * d))
        return add(scale(sub(sub(harmonic[n], harmonic[n // d]), elementary.log_integer(d)), F(n, d)),
                   rat(F(d - 1 - 2 * (n % d), 2 * d)))

    def combined(H, n):
        return isum(mul(c[d], P(d, n)) for d in range(2, H + 1))

    actual_grams = []
    for H in [8, 16, 32, 64, 256]:
        V = variance(c, H, spf)
        envelope = add(elementary.log_integer(H), sub(scale(elementary.log_integer(2), 2), ONE))
        generic = scale(square(envelope), F(H ** 3, 60))
        assert V[1] <= generic[0]
        item = {'H': H, 'joint_variance_via_R2_R4': output(V), 'generic_variance_upper_enclosure': output(generic)}
        if H <= 64:
            direct = isum(scale(mul(c[d], c[e]), gram(d, e))
                          for d in range(2, H + 1) for e in range(2, H + 1))
            assert overlap(V, direct)
            item['direct_gcd_Gram_overlaps'] = True
        actual_grams.append(item)

    examples = []
    point_bound_checks = 0
    for A, B_end in [(64, 512), (128, 1024)]:
        H = floor_root(A ** 4, 5)
        values = {}
        for n in range(A, B_end + 1):
            terms = []
            for d in range(2, H + 1):
                p = P(d, n)
                bound = rat(F(d * d - 1, 12 * d * n))
                assert max(abs(p[0]), abs(p[1])) <= bound[0]
                point_bound_checks += 1
                terms.append(mul(c[d], p))
            values[n] = isum(terms)
        energy = isum(scale(square(p), F(1, n * n)) for n, p in values.items())
        V = variance(c, H, spf)
        Q, bound = tail_bound(elementary, V, A, H)
        assert energy[1] <= bound[0]
        examples.append({'A': A, 'B': B_end, 'H': H, 'theta': '1/2',
                         'anchored_finite_correction_energy': output(energy),
                         'infinite_tail_upper_enclosure': output(bound),
                         'V_H': output(V), 'Q_H': output(Q),
                         'P_H_at_A': output(values[A]), 'P_H_at_B': output(values[B_end])})

    A, B_end, H = 1024, 32768, 256
    V = variance(c, H, spf)
    Q, bound = tail_bound(elementary, V, A, H)
    sigma = isum(scale(c[d], F(1, d)) for d in range(1, H + 1))
    main_window = {'A': A, 'B': B_end, 'H': H, 'theta': '1/2',
                   'H_is_exact_A_to_four_fifths': H ** 5 == A ** 4,
                   'V_H': output(V), 'Q_H': output(Q),
                   'infinite_tail_upper_enclosure': output(bound),
                   'sigma_H': output(sigma),
                   'P_H_at_A': output(combined(H, A)), 'P_H_at_B': output(combined(H, B_end)),
                   'finite_energy_not_evaluated': True}

    # Check transformed-source identity via original D-kappa and harmonic P.
    H = 16
    sigma16 = isum(scale(c[d], F(1, d)) for d in range(1, H + 1))
    source_checks = 0
    for n in range(2, limit):
        original_source = scale(sub(kappa[n], D[n]), F(1, n))
        correction_source = sub(sub(scale(combined(H, n), 2), combined(H, n - 1)), combined(H, n + 1))
        transformed = add(original_source, correction_source)
        predicted = scale(add(sigma16, isum(c[d] for d in range(H + 1, n + 1) if n % d == 0)), F(-1, n))
        assert overlap(transformed, predicted)
        source_checks += 1
    return {
        'input': {'path': 'rh_correlation_rational/rational_window_certificate.json',
                  'sha256': hashlib.sha256(raw).hexdigest(), 'window': certificate['window'],
                  'nodes': certificate['node_certificate']['nodes'],
                  'weights': certificate['node_certificate']['weights']},
        'complete_residual_inversion_crosschecks': limit,
        'unit_coefficient_c1': output(c[1]),
        'actual_phase_variances': actual_grams,
        'anchored_windows': examples,
        'actual_matched_main_window': main_window,
        'pointwise_harmonic_bound_checks': point_bound_checks,
        'transformed_source_identity_checks': source_checks,
        'log_values': len(elementary.logs), 'exp_evaluations': elementary.exp_calls,
        'scope': ['Finite interval comparisons do not prove an infinite arithmetic cancellation estimate.',
                  'All c values include kappa and the unit correction.',
                  'The same matched nodes as the sparse positive-energy certificate are used.',
                  'The infinite-tail number is a certified upper bound, not its observed energy.',
                  'Directed interval helper is imported unchanged from the sibling rational-node branch.'],
    }


def main():
    started = time.monotonic()
    report = {'status': 'EXACT_PHASE_IDENTITIES_AND_DIRECTED_INTERVAL_CHECKS_PASSED',
              'exact_checks': exact_checks(), 'actual_matched_family': actual_checks(),
              'elapsed_seconds_diagnostic_only': time.monotonic() - started}
    target = Path(__file__).with_name('phase_homogenization_checks.json')
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': report['status'], 'exact_checks': report['exact_checks'],
                      'actual_main_window': report['actual_matched_family']['actual_matched_main_window'],
                      'elapsed_seconds_diagnostic_only': report['elapsed_seconds_diagnostic_only']},
                     ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
