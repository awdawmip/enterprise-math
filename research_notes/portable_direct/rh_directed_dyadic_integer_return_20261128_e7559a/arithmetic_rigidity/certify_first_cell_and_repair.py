#!/usr/bin/env python3
"""Exact finite evidence for first-cell obstruction and a two-pair repair.

Uses integer outward intervals, elementary series and a previously certified
Euler-constant enclosure.  No zeta zeros, old road queries or old scripts run.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import argparse
import hashlib
import json

S = 10**80


def ceildiv(a, b):
    return -((-a)//b)


def rat(x):
    x = F(x)
    return (x.numerator*S//x.denominator,
            ceildiv(x.numerator*S, x.denominator))


def add(*xs):
    return sum(x[0] for x in xs), sum(x[1] for x in xs)


def neg(x):
    return -x[1], -x[0]


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    p = [a*b for a in x for b in y]
    return min(p)//S, ceildiv(max(p), S)


def scale(x, q):
    return mul(x, rat(q))


def div(x, y):
    assert y[0] > 0
    return mul(x, (S*S//y[1], ceildiv(S*S, y[0])))


def sqrt(x):
    assert x[0] >= 0
    lo, hi = isqrt(x[0]*S), isqrt(x[1]*S)
    return lo, hi+(hi*hi < x[1]*S)


def widen(x, r):
    return x[0]-r, x[1]+r


ONE, ZERO = rat(1), rat(0)


def log(x, terms=180):
    assert x[0] >= S
    z = div(sub(x, ONE), add(x, ONE))
    z2 = mul(z, z)
    power, total = z, ZERO
    for k in range(terms):
        total = add(total, scale(power, F(2, 2*k+1)))
        power = mul(power, z2)
    remainder = div(scale(power, F(2, 2*terms+1)), sub(ONE, z2))
    return total[0], total[1]+remainder[1]


def arctan(q, terms=100):
    z = rat(q)
    z2 = mul(z, z)
    power, total = z, ZERO
    for k in range(terms):
        total = add(total, scale(power, F((-1)**k, 2*k+1)))
        power = mul(power, z2)
    remainder = scale(power, F(1, 2*terms+1))[1]
    return widen(total, remainder)


def trig(x, kind, terms=120):
    """Taylor at the exact interval midpoint, then the real 1-Lipschitz bound."""
    mid = (x[0]+x[1])//2
    radius = max(mid-x[0], x[1]-mid)
    center = (mid, mid)
    x2 = mul(center, center)
    term = ONE if kind == 'cos' else center
    total = term
    offset = 0 if kind == 'cos' else 1
    for k in range(1, terms+1):
        term = scale(mul(term, x2), F(-1, (2*k-1+offset)*(2*k+offset)))
        total = add(total, term)
    next_term = scale(mul(term, x2), F(1, (2*terms+1+offset)*(2*terms+2+offset)))
    remainder = max(abs(next_term[0]), abs(next_term[1]))
    return widen(total, radius+remainder)


def record(x, places=40):
    factor = 10**(80-places)
    def decimal(n):
        sign = '-' if n < 0 else ''
        n = abs(n)
        return sign+str(n//10**places)+'.'+str(n%10**places).zfill(places)
    return {'integer_bounds': [str(x[0]), str(x[1])],
            'denominator_power_of_10': 80,
            'lower': decimal(x[0]//factor),
            'upper': decimal(ceildiv(x[1], factor))}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--previous', type=Path, required=True,
                        help='round7 riemann_sparse_lengths_canonical_return package')
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('first_cell_and_repair_certificate.json'))
    args = parser.parse_args()
    gamma_path = args.previous / 'prior/riemann_coherent_tail_interval_spectrum_20261126/prior/riemann_three_thickness_green_macro_20261126/three_thickness/three_thickness_certificate.json'
    data = json.loads(gamma_path.read_text())
    gamma = tuple(map(int, data['regular_constants']['gamma']['integer_bounds']))
    assert data['regular_constants']['gamma']['denominator_power_of_10'] == 80
    pi = sub(scale(arctan(F(1, 5)), 16), scale(arctan(F(1, 239)), 4))
    l2, l3, lp = log(rat(2)), log(rat(3)), log(pi)
    C = sub(add(rat(2), gamma), add(scale(l2, 2), lp))
    A = sub(add(lp, scale(l3, F(3, 2)), scale(l2, 2)), add(rat(3), scale(gamma, 2)))
    root2 = sqrt(rat(2))

    def angle(d, multiplicity):
        return mul(l2, sqrt(sub(div(rat(2*multiplicity), d), rat(F(1, 4)))))

    def weight_cos(d, multiplicity, phase_multiple=1):
        return mul(d, trig(scale(angle(d, multiplicity), phase_multiple), 'cos'))

    def derivative(d, multiplicity):
        u = angle(d, multiplicity)
        coefficient = add(scale(u, F(1, 2)), div(mul(l2, l2), scale(u, 8)))
        return add(trig(u, 'cos'), mul(coefficient, trig(u, 'sin')))

    u_low, u_high = angle(C, 1), angle(scale(C, F(1, 2)), 1)
    assert u_low[0] > rat(F(9, 2))[1]
    assert u_high[1] < rat(F(13, 2))[0]
    assert rat(F(9, 2))[0] > pi[1]
    assert rat(F(13, 2))[1] < scale(pi, 3)[0]
    jends = []
    for u in (rat(F(9, 2)), rat(F(13, 2))):
        j = sub(mul(u, trig(u, 'cos')), trig(u, 'sin'))
        assert j[0] > 0
        jends.append(record(j))
    end_full = weight_cos(C, 1)
    half = scale(C, F(1, 2))
    end_half = sub(weight_cos(half, 1), half)
    assert end_full[1] < end_half[0]
    gap = add(A, mul(root2, end_full))
    assert gap[0] > rat(F(137, 10000))[1]

    # A small but positive preliminary spectrum mass is an allowed r7 choice.
    epsilon = rat(F(1, 10**6))
    Delta = (C[0]-epsilon[1], C[1])
    target = neg(div(A, root2))
    target_range = widen(target, epsilon[1])

    def h(r):
        d1, d4 = mul(Delta, r), mul(Delta, sub(ONE, r))
        return add(weight_cos(d1, 1), weight_cos(d4, 4))

    left, right = h(rat(F(1, 4))), h(rat(F(3, 10)))
    assert left[1] < target_range[0]
    assert right[0] > target_range[1]
    derivative_rows, q4_rows = [], []
    # B4 = log(2*pi)-1+(5/2)log5-(3/2)log3-2log2.
    l5 = log(rat(5))
    B4 = sub(add(lp, scale(l5, F(5, 2))), add(ONE, scale(l3, F(3, 2)), l2))
    q4 = add(scale(add(ONE, gamma, neg(scale(l2, 2))), 4), l2, scale(l3, F(1, 3)))
    for k in range(50):
        r = (rat(F(1, 4)+F(k, 1000))[0], rat(F(1, 4)+F(k+1, 1000))[1])
        d1, d4 = mul(Delta, r), mul(Delta, sub(ONE, r))
        dr = mul(Delta, sub(derivative(d1, 1), derivative(d4, 4)))
        assert dr[0] > rat(F(1, 5))[1]
        derivative_rows.append(record(dr))
        q4gap = sub(add(B4, scale(add(weight_cos(d1, 1, 2), weight_cos(d4, 4, 2)), 2)), q4)
        q4gap = widen(q4gap, 2*epsilon[1])
        assert q4gap[1] < -rat(F(1, 100))[1]
        q4_rows.append(record(q4gap))

    result = {
      'status': 'PASS', 'author': 'EM-DIRECT-E7559A / TASK_RESEARCH',
      'review_scope': 'Author finite evidence; not independent Review or formal Result.',
      'arithmetic': '80-place outward integer intervals; exact rational series remainders; no floating-point decision.',
      'constants': {'C_star': record(C), 'A': record(A), 'pi': record(pi), 'log2': record(l2)},
      'one_pair_obstruction': {'angle_interval': [record(u_low), record(u_high)],
        'u_cos_u_minus_sin_u_at_9_over_2_and_13_over_2': jends,
        'full_mass_endpoint': record(end_full), 'half_mass_endpoint': record(end_half),
        'uniform_q2_gap': record(gap), 'simple_strict_lower_bound': '137/10000'},
      'two_pair_repair': {'preliminary_mass_upper': '1/1000000',
        'positive_height_multiplicities': [1, 4], 'r_interval': ['1/4', '3/10'],
        'target_range': record(target_range), 'left_value': record(left), 'right_value': record(right),
        'derivative_partition_cells': 50, 'derivative_strict_lower_bound': '1/5',
        'derivative_enclosures': derivative_rows,
        'uniform_q4_gap_upper_bound': '-1/100', 'q4_gap_enclosures': q4_rows,
        'scope': 'Existence and computability of the unique exact r for each actual computable preliminary spectrum; no particular infinite spectrum numerically constructed.'},
      'dependencies': [{'path_from_round7': str(gamma_path.relative_to(args.previous)),
          'sha256': hashlib.sha256(gamma_path.read_bytes()).hexdigest(),
          'use': 'Previously certified Euler constant enclosure; source script not rerun.'}],
      'old_calculation_reruns': 0, 'new_zeta_evaluations': 0, 'new_zero_queries': 0,
      'analytic_inputs': ['r7 exact f_off(2^j)=0', 'r7 nonnegative critical coefficient mass bound',
                          'concavity proof in ORDINARY_INTEGER_SOURCE_RIGIDITY.md']}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print('PASS: one-pair first-cell obstruction; exact two-pair repair; all 50 derivative and q4 interval cells.')


if __name__ == '__main__':
    main()
