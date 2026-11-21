#!/usr/bin/env python3
"""One directed addition: rigorous gamma and the complete millionth endpoint."""
from fractions import Fraction as F
from pathlib import Path
import json
from certify_arithmetic import (
    ANCHOR, BERNOULLI, DIGITS, EM_ORDER, H, ONE, SCALE,
    MobiusEndpoint, add, interval_fraction, render, scale, sub,
)


def gamma_interval(oracle):
    b = ANCHOR
    result = sub(oracle.power_prefix[4][b], oracle.log_integer(b))
    result = sub(result, interval_fraction(F(1, 2 * b)))
    for r in range(1, EM_ORDER + 1):
        result = add(result, interval_fraction(BERNOULLI[2 * r] / (2 * r * b ** (2 * r))))
    radius = oracle.remainder_radii[4]
    return result[0] - radius, result[1] + radius


def main():
    n = 1000000
    engine = MobiusEndpoint(n)
    T, green, stats = engine.evaluate(n)
    gamma = gamma_interval(engine.oracle)
    endpoint = add(T, scale(add(ONE, gamma), n))
    assert gamma[0] > 0 and gamma[1] < SCALE
    assert endpoint[1] < 0
    assert endpoint[1] - endpoint[0] < 10 ** (DIGITS - 20)
    report = {
        'status': 'EXACT_GAMMA_AND_FULL_ENDPOINT_CERTIFICATE_PASSED',
        'N': n, 'h': str(H), 'thicknesses': [str(H), str(2 * H)],
        'normalized_weights': [2, -1],
        'gamma': render(gamma, places=45),
        'T_equal_H_D_minus_N_log_N': render(T),
        'F_equal_T_plus_N_times_1_plus_gamma': render(endpoint),
        'weighted_residual_sum_n2_toN': render(green),
        'gamma_formula': 'H_b-log(b)-1/(2b)+sum_{r=1}^K B_(2r)/(2r*b^(2r)) plus/minus C_(2K)/(2K*b^(2K))',
        'gamma_anchor': ANCHOR, 'gamma_EM_order': EM_ORDER,
        'gamma_EM_remainder_radius': render((0, engine.oracle.remainder_radii[4]), places=55),
        'algorithm': {k: v for k, v in stats.items()
                      if k not in ['M_n', 'EM_uniform_remainder_radii']},
        'precision': '60 decimal places; exact integer/Fraction enclosures with outward rounding',
        'scope': [
            'Exactly one directed endpoint recomputation; the former full-population test was not rerun.',
            'Gamma uses the already available 256-term harmonic prefix and 16 EM correction terms.',
            'The complete centered road endpoint F(N) is certified, including gamma and all unit corrections.',
            'This is one fixed-thickness endpoint, not a full-window energy certificate or an asymptotic RH claim.'
        ]
    }
    Path(__file__).with_name('gamma_endpoint_certificate.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ('status', 'N', 'gamma',
                     'F_equal_T_plus_N_times_1_plus_gamma', 'algorithm')},
                     ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
