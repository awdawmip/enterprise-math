#!/usr/bin/env python3
"""Targeted coauthor crosscheck of saved interval endpoints.

This does not regenerate zeta enclosures and is not an independent Review.
It uses exact Fraction intervals, verifies the rational algebra, and uses
the exact identity (2**400000)**(-1/2000) = 2**(-200) at the final threshold.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import argparse
import hashlib
import json


def interval(record):
    scale = 10 ** record['denominator_power_of_10']
    return tuple(F(int(x), scale) for x in record['integer_bounds'])


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def sub(x, y):
    return x[0] - y[1], x[1] - y[0]


def mul(x, y):
    values = [a * b for a in x for b in y]
    return min(values), max(values)


def scale(x, q):
    return mul(x, (q, q))


def divide(x, y):
    assert y[0] > 0 or y[1] < 0
    return mul(x, (1 / y[1], 1 / y[0]))


def contains(outer, inner):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def linear(coefficients, values):
    out = F(0), F(0)
    for c, x in zip(coefficients, values):
        out = add(out, scale(x, c))
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--certificate', type=Path,
                        default=Path(__file__).with_name('calibrated_family_certificate.json'))
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text())
    nodes = list(map(F, data['all_nodes']))
    bases = [list(map(F, b)) for b in data['basis_weights']]
    one = F(1), F(1)
    moment_count = 0
    for size, base in zip((11, 12, 13), bases):
        for k in range(size):
            assert sum(w * a**k for w, a in zip(base, nodes)) == int(k == 0)
            moment_count += 1
    values_d = [interval(r['mean_density']) for r in data['node_certificates']]
    values_c = [interval(r['road_constant']) for r in data['node_certificates']]
    es = [interval(x) for x in data['basis_density_errors']]
    cs = [interval(x) for x in data['basis_road_constants']]
    for base, e, c in zip(bases, es, cs):
        assert contains(e, sub(linear(base, values_d), one))
        assert contains(c, linear(base, values_c))
    assert es[0][1] < es[1][0] < es[1][1] < es[2][0] < es[2][1] < 0
    assert cs[0][0] > cs[1][1] > cs[1][0] > cs[2][1] > cs[2][0] > 0
    aa, bb = sub(es[0], es[2]), sub(es[1], es[2])
    cc, dd = sub(cs[0], cs[2]), sub(cs[1], cs[2])
    det = sub(mul(aa, dd), mul(bb, cc))
    saved_det = interval(data['calibration_determinant'])
    assert contains(saved_det, det) and saved_det[1] < 0
    lam = [interval(x) for x in data['real_mixture_coefficients']]
    assert contains(lam[0], divide(sub(mul(bb, cs[2]), mul(es[2], dd)), saved_det))
    assert contains(lam[1], divide(sub(mul(es[2], cc), mul(aa, cs[2])), saved_det))
    assert contains(lam[2], sub(sub(one, lam[0]), lam[1]))
    shrinking = data['shrinking_family']
    rd = interval(shrinking['first_new_node_density_derivative'])
    rc = interval(shrinking['first_new_node_constant_derivative'])
    boundary = sub(mul(es[0], rc), mul(cs[0], rd))
    saved_boundary = interval(shrinking['boundary_determinant'])
    assert contains(saved_boundary, boundary) and saved_boundary[1] < 0

    # An independently summed atanh series encloses log(2).
    z = F(1, 3)
    log2_lo = 2 * sum(z**(2*j+1) / (2*j+1) for j in range(100))
    log2_hi = log2_lo + 2 * z**201 / (201 * (1-z*z))
    log2 = log2_lo, log2_hi
    bernoulli = [F(1)]
    for n in range(1, 49):
        bernoulli.append(-sum(F(comb(n+1, k))*bernoulli[k] for k in range(n))/(n+1))
    r = abs(bernoulli[48]) / (48*64**48)
    regular = data['regular_constants']
    assert interval(regular['gamma_remainder_upper'])[0] >= r
    derivative_factor = add(scale(log2, 6), (sum(F(1, j) for j in range(1, 49)) + F(1, 48),)*2)
    assert interval(regular['gamma1_remainder_upper'])[0] >= scale(derivative_factor, r)[1]

    rational_checks = []
    q = F(1, 2**100)
    for name, positive in [('rational_approximation', True), ('rational_ceiling_twin', False)]:
        twin = data[name]
        mix = list(map(F, twin['mixture_coefficients']))
        ws = list(map(F, twin['weights']))
        assert sum(mix) == 1
        assert ws == [sum(mix[i]*bases[i][j] for i in range(3)) for j in range(13)]
        for k in range(11):
            assert sum(w*a**k for w, a in zip(ws, nodes)) == int(k == 0)
            moment_count += 1
        if positive:
            for v, l in zip(mix[:2], lam[:2]):
                assert v < l[0] <= l[1] < v + q
        density = interval(twin['density_error'])
        constant = interval(twin['road_constant'])
        assert contains(density, sub(linear(ws, values_d), one))
        assert contains(constant, linear(ws, values_c))
        assert density[0] > 0 and constant[1] < 0 if positive else density[1] < 0 and constant[0] > 0
        eventual = twin['eventual_sign']
        v = sum(w/a for w, a in zip(ws, nodes))
        k = sum(abs(w)*(1/(a*a*(1-a)) + 2/a**3) for w, a in zip(ws, nodes))
        assert v == F(eventual['exact_V_minus1']) and k == F(eventual['exact_K'])
        assert min(nodes) == F(1, 2000)
        tail = abs(v)/2**400000 + k/2**200
        main_term = add(mul(density, scale(log2, 400000)), constant)
        threshold = sub(main_term, (tail, tail)) if positive else add(main_term, (tail, tail))
        assert contains(interval(eventual['monotone_bound_at_threshold']), threshold)
        assert threshold[0] > 0 if positive else threshold[1] < 0
        rational_checks.append({'family': name, 'strict_density_sign': '+' if positive else '-',
                                'strict_road_sign_for_every_real_y_ge_2pow400000': '+' if positive else '-',
                                'exact_threshold_tail_power': '1/2^200'})
    floor = list(map(F, data['rational_approximation']['mixture_coefficients']))
    ceiling = list(map(F, data['rational_ceiling_twin']['mixture_coefficients']))
    assert [b-a for a, b in zip(floor, ceiling)] == [q, q, -2*q]
    print(json.dumps({'status': 'PASS', 'role': 'author crosscheck; not independent Review',
                      'certificate_sha256': hashlib.sha256(args.certificate.read_bytes()).hexdigest(),
                      'exact_matching_moments_rechecked': moment_count,
                      'method': 'Fraction interval algebra on saved source enclosures; no zeta rerun; exact threshold tail power',
                      'twins': rational_checks}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
