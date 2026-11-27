#!/usr/bin/env python3
"""Certify new logarithmic-energy constants, reusing saved gamma/gamma_1.

No zeros, road values, prime sieve or previous scientific calculation is rerun.
All new decisions use exact fractions and 80-place outward integer intervals.
"""
from fractions import Fraction as F
from pathlib import Path
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


def atan_reciprocal(q, terms):
    """Alternating arctan series with the exact first omitted term bound."""
    value = sum((F((-1)**k, (2*k+1)*q**(2*k+1))
                 for k in range(terms)), F(0))
    omitted = F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(value, value+omitted), max(value, value+omitted)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--previous', type=Path, required=True,
                        help='riemann_sparse_lengths_canonical_return_20261126 package')
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('log_energy_constants_certificate.json'))
    args = parser.parse_args()
    r6 = args.previous / 'prior/riemann_coherent_tail_interval_spectrum_20261126'
    r5 = r6 / 'prior/riemann_three_thickness_green_macro_20261126'
    r4 = r5 / 'prior/riemann_calibrated_green_sparse_20261126'
    r3 = r4 / 'prior/riemann_signed_green_thickness_phase_20261124'
    r2 = r3 / 'prior/riemann_native_residual_growth_20261124'
    r1 = r2 / 'prior/riemann_matching_isotonic_anchors_20261124'
    early = r1 / 'prior/riemann_directed_local_20261124/prior/riemann_cumulative_haar_20261123'
    interval_path = early / 'dependencies/certify_fast_harmonic_energy.py'
    old_path = r5 / 'three_thickness/three_thickness_certificate.json'
    m = module_at('log_energy_intervals', interval_path)
    old = json.loads(old_path.read_text())
    gamma, gamma1 = [m.decode(old['regular_constants'][key])
                     for key in ('gamma', 'gamma1')]

    def reciprocal(z):
        assert z[0] > 0
        return m.S*m.S//z[1], m.ceildiv(m.S*m.S, z[0])

    a5, a239 = atan_reciprocal(5, 64), atan_reciprocal(239, 20)
    pi_fraction = 16*a5[0]-4*a239[1], 16*a5[1]-4*a239[0]
    pi = m.rat(pi_fraction[0])[0], m.rat(pi_fraction[1])[1]
    # Machin's identity: pi = 16 arctan(1/5) - 4 arctan(1/239).
    assert 3*m.S < pi[0] < pi[1] < 4*m.S
    log_pi_half = (m.log_unit(pi[0], 2*m.S)[0],
                   m.log_unit(pi[1], 2*m.S)[1])
    log4pi = m.add(m.qmul(m.LOG_TWO, 3), log_pi_half)
    c = m.sub(m.add(m.rat(2), gamma), log4pi)
    v = m.total([m.rat(6), m.qmul(gamma, 2), m.qmul(gamma1, 4),
                 m.qmul(m.square(gamma), 2), m.qmul(log4pi, -2),
                 m.qmul(m.square(pi), F(-1, 4))])
    assert c[0] > 0 and v[0] > 0
    assert v[1] < m.square(c)[0]
    sign_floor = m.mul(m.square(v), reciprocal(m.qmul(m.square(c), 4)))
    dyadic_absolute_floor = m.mul(m.LOG_TWO, v)
    dyadic_sign_floor = m.mul(m.LOG_TWO, sign_floor)

    # Exact finite witness: F(t)=cos t+cos 2t has positive Fourier coefficients,
    # mean zero and mean square one, but unequal positive/negative square means.
    fourier = {-2:F(1, 2), -1:F(1, 2), 1:F(1, 2), 2:F(1, 2)}
    square = {}
    for i, a in fourier.items():
        for j, b in fourier.items():
            square[i+j] = square.get(i+j, F(0)) + a*b
    expected = {0:F(1), -4:F(1, 4), 4:F(1, 4),
                -3:F(1, 2), 3:F(1, 2), -2:F(1, 4), 2:F(1, 4),
                -1:F(1, 2), 1:F(1, 2)}
    assert square == expected
    # On c=cos t in [-1,1], F=(2c-1)(c+1), so its positive arc is |t|<pi/3.
    # Integrating the verified trigonometric square on that arc gives
    # M(F_+^2)=1/3+9sqrt(3)/(16pi), M(F_-^2)=1-M(F_+^2).
    from math import isqrt
    q = isqrt(3*m.S*m.S)
    sqrt3 = q, q+1
    positive_mean = m.add(m.rat(F(1, 3)),
                         m.qmul(m.mul(sqrt3, reciprocal(pi)), F(9, 16)))
    negative_mean = m.sub(m.ONE, positive_mean)
    assert positive_mean[0] > m.S//2 > negative_mean[1] > 0

    result = {
        'status':'PASS',
        'arithmetic':'exact fractions; outward integer intervals; no floating-point decisions',
        'constants':{
            'C_star':m.record(c),
            'V_simple_zero_baseline':m.record(v),
            'one_sided_logarithmic_floor':m.record(sign_floor),
            'dyadic_absolute_mean_floor':m.record(dyadic_absolute_floor),
            'dyadic_one_sided_mean_floor':m.record(dyadic_sign_floor),
            'pi':m.record(pi),
            'log_4pi':m.record(log4pi),
            'log_2':m.record(m.LOG_TWO),
        },
        'calculation_scope':{
            'reused_regular_constants':['gamma','gamma1'],
            'new_zero_evaluations':0,
            'new_zeta_evaluations':0,
            'new_road_values':0,
            'new_sieve':False,
            'new_arctangent_series':{'1/5':64,'1/239':20},
            'new_logarithm_series':3,
            'logarithm_terms_per_series':m.LOG_TERMS,
        },
        'dependencies':[
            {'path':str(p.relative_to(args.previous)),
             'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
            for p in (old_path, interval_path)
        ],
        'non_half_witness':{
            'function':'cos(t)+cos(2t)',
            'mean_square':'1',
            'positive_formula':'1/3+9*sqrt(3)/(16*pi)',
            'negative_formula':'2/3-9*sqrt(3)/(16*pi)',
            'positive_mean':m.record(positive_mean),
            'negative_mean':m.record(negative_mean),
            'scope':'finite auxiliary trigonometric witness; not a claim about zeta ordinate relations',
        },
        'logical_scope':{
            'V_equals_RH_spectral_variance':'requires RH and simplicity of all nontrivial zeros',
            'V_bounds_RH_spectral_variance_below':'RH; arbitrary zero multiplicities retained',
            'displayed_limsup_floors':'unconditional via RH/non-RH dichotomy proved in the accompanying note',
            'not_asserted':'unconditional existence of the finite energy limit; equal one-sided means',
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status':result['status'],
                      'constants':{k:{'lower':v['lower'],'upper':v['upper']}
                                   for k,v in result['constants'].items()}}, ensure_ascii=False))


if __name__ == '__main__':
    main()
