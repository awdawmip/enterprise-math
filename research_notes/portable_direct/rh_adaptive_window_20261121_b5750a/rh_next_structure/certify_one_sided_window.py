#!/usr/bin/env python3
"""An exact endpoint certificate for the new one-sided full-window repair.

This checks one new case; it does not rerun the preceding numerical suites.
Only integer/Fraction arithmetic is used.
"""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json


@lru_cache(None)
def factors(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return tuple(out)


def log_unit_interval(t, terms=36):
    """log(t) for 1 <= t <= 2, by its positive atanh series."""
    assert 1 <= t <= 2
    z = (t - 1) / (t + 1)
    partial = 2 * sum((z ** (2 * k + 1)) / (2 * k + 1)
                      for k in range(terms))
    remainder = (2 * z ** (2 * terms + 1)
                 / ((2 * terms + 1) * (1 - z * z)))
    return partial, partial + remainder


@lru_cache(None)
def log_integer(n):
    exponent = n.bit_length() - 1
    l2 = log_unit_interval(F(2))
    unit = log_unit_interval(F(n, 2 ** exponent))
    return exponent * l2[0] + unit[0], exponent * l2[1] + unit[1]


def outward_decimal(value, digits=20):
    scale = 10 ** digits
    lower = value[0].numerator * scale // value[0].denominator
    upper = -((-value[1].numerator * scale) // value[1].denominator)

    def render(n):
        sign = '-' if n < 0 else ''
        n = abs(n)
        return f'{sign}{n // scale}.{n % scale:0{digits}d}'

    return {'lower': render(lower), 'upper': render(upper)}


def main():
    Y, Z, h = 25, 125, F(149, 1000)
    total = [F(0), F(0)]
    populations = Counter()
    for n in range(2, Z + 1):
        ps = factors(n)
        r = len(ps)
        populations[r] += 1
        assert r <= 3  # 2 * 3 * 5 * 7 = 210 > 125.
        ramp = F(Z, n) - 1
        if r == 1:
            lp = log_integer(ps[0])
            coefficients = [lp[i] ** 3 / 3 for i in (0, 1)]
        elif r == 3:
            coefficients = [F(2), F(2)]
            for p in ps:
                lp = log_integer(p)
                coefficients = [coefficients[i] * lp[i] for i in (0, 1)]
        else:
            continue  # Its error is nonnegative; this is only the minus envelope.
        total = [total[i] + h * h * coefficients[i] * ramp for i in (0, 1)]

    # h log Z < 2 log 2, using 125 < 2^7 and 7h < 2.
    assert Z < 2 ** 7 and 7 * h < 2
    # C^-(Z) < 37/2 < Z^(3/4)/2, all by exact arithmetic.
    assert total[1] < F(37, 2)
    assert Z ** 3 > 37 ** 4
    decimal_scale = 10 ** 20
    certified_upper = F(-((-total[1].numerator * decimal_scale)
                          // total[1].denominator), decimal_scale)
    assert certified_upper < F(37, 2)

    # Compare with h_generic = sqrt(3/2) * 125^(-1/8) / log(125)^2.
    # The following three rational bounds imply h_generic < generic_upper.
    assert F(49, 40) ** 2 > F(3, 2)
    assert Z * 11 ** 8 > 20 ** 8
    assert log_integer(Z)[0] > F(24, 5)
    generic_upper = F(49, 40) * F(11, 20) / F(24, 5) ** 2
    assert generic_upper < h / 5

    report = {
        'status': 'EXACT_ONE_SIDED_FULL_WINDOW_CERTIFICATE_PASSED',
        'window': [Y, Z],
        'theta': '3/4',
        'h': str(h),
        'thicknesses': [str(h), str(2 * h)],
        'normalized_weights': [2, -1],
        'all_integer_population': Z - 1,
        'omega_population': dict(sorted(populations.items())),
        'C_minus_endpoint_interval': outward_decimal(total),
        'C_minus_endpoint_upper_fraction': str(certified_upper),
        'budget_chain': 'C_minus(125) < 37/2 < 125^(3/4)/2',
        'orientation_chain': 'h log(125) < 7h log(2) < 2 log(2)',
        'generic_h_upper': str(generic_upper),
        'strict_improvement': 'h > 5 h_generic',
        'log_enclosure': '36-term positive atanh series after dyadic scaling',
        'conclusion': 'G(y) <= G_extrapolated(y) + y^(3/4)/2 for all 25 <= y <= 125',
        'scope': [
            'Finite endpoint arithmetic plus the proved monotonicity theorem covers the entire real window.',
            'All 124 integers from 2 through 125 remain in the readout.',
            'The omega=2 layer has zero minus-envelope coefficient because its error is positive; its road contribution is retained.',
            'This certifies a one-sided bridge, not an infinite-window positive-energy estimate.'
        ]
    }
    Path(__file__).with_name('one_sided_window_certificate.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items()
                      if k != 'C_minus_endpoint_upper_fraction'},
                     ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
