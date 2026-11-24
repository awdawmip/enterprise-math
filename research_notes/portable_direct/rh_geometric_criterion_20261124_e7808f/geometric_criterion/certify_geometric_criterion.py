#!/usr/bin/env python3
"""Finite exact checks for the fixed 9:12:16 one-sided criterion.

The proof of the unbounded criterion is analytic, in PROOF.md. This program
verifies rational source kernels and deterministic outward local arithmetic
intervals only. It makes no zero query and assumes no instance of RH.
"""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import argparse
import hashlib
import importlib.util
import json


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_interval_module(prior):
    path = prior / 'dependencies' / 'certify_fast_harmonic_energy.py'
    spec = importlib.util.spec_from_file_location('fixed_outward_intervals', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, path


def phi(n, k):
    if 9*n < k <= 12*n:
        return F(k-9*n, 3*n)
    if 12*n < k < 16*n:
        return F(16*n-k, 4*n)
    return F(0)


def prime_factors(n):
    result = {}
    p = 2
    while p*p <= n:
        if n % p == 0:
            result[p] = 0
            while n % p == 0:
                n //= p
                result[p] += 1
        p += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def exact_kernels(parameters):
    pulses = 0
    rows = []
    for n in parameters:
        for k in range(1, 16*n+2):
            values = [max(F(y, k)-1, F(0)) for y in (9*n, 12*n, 16*n)]
            t = (values[1]-values[0])/(3*n) - (values[2]-values[1])/(4*n)
            assert t == -phi(n, k)/k
            assert 7*values[1]-4*values[0]-3*values[2] == 12*n*t
            pulses += 1
        total_phi = sum((phi(n, k) for k in range(9*n, 16*n+1)), F(0))
        total_v = sum((phi(n, k)/k for k in range(9*n, 16*n+1)), F(0))
        assert total_phi == F(7*n, 2)
        assert total_v <= F(7, 18)
        # The sharper pointwise kernel maximum is also exact, though the proof
        # deliberately retains its already stated coarse prime-power payment.
        assert max(phi(n, k)/k for k in range(9*n, 16*n+1)) == F(1, 12*n)
        log_coefficients = defaultdict(int)
        for y, coefficient in ((9*n, 3), (12*n, -7), (16*n, 4)):
            for p, exponent in prime_factors(y).items():
                log_coefficients[p] += coefficient*exponent
        log_coefficients = {p: v for p, v in log_coefficients.items() if v}
        assert log_coefficients == {2: 2, 3: -1}
        rows.append({'n': n, 'hat_sum': str(total_phi),
                     'weighted_hat_sum': str(total_v),
                     'background_log_coefficients': {'2': 2, '3': -1}})

    # Polynomial identity 7z-4-3z^2 = -3(z-1)(z-4/3).
    product = [F(0)]*3
    for i, a in enumerate((-F(1), F(1))):
        for j, b in enumerate((-F(4, 3), F(1))):
            product[i+j] += -3*a*b
    assert product == [F(-4), F(7), F(-3)]
    assert 7*12-4*9-3*16 == 0
    assert 7*12-3*16 == 36
    assert -3*16 == -48
    assert F(7**3, 9**2*12**2) == F(343, 11664)
    assert F(7, 18)*F(40, 7) == F(20, 9)
    return {'source_impulse_checks': pulses,
            'parameters': rows,
            'multiplier_polynomial_coefficients': list(map(str, product)),
            'derivative_source_coefficients': [0, 36, -48],
            'budget_G_squared_over_n_factor': '343/11664',
            'matching_payment_factor': '20/9'}


def prime_power_events(bound):
    sieve = bytearray(b'\x01')*(bound+1)
    sieve[0:2] = b'\x00\x00'
    p = 2
    while p*p <= bound:
        if sieve[p]:
            start = p*p
            sieve[start:bound+1:p] = b'\x00'*((bound-start)//p+1)
        p += 1
    primes = [p for p in range(2, bound+1) if sieve[p]]
    events = []
    for p in primes:
        k, exponent = p, 1
        while k <= bound:
            events.append((k, p, exponent))
            k *= p
            exponent += 1
    events.sort()
    assert len({k for k, p, exponent in events}) == len(events)
    return events, len(primes)


def numeric_checks(parameters, iv):
    bound = 16*max(parameters)
    events, prime_count = prime_power_events(bound)
    queries = sorted({j*n for n in parameters for j in (9, 12, 16)})
    log_values = {p: iv.log_int(p) for k, p, exponent in events}
    prefix_a, prefix_b = iv.ZERO, iv.ZERO
    event_index = 0
    values = {}
    for y in queries:
        while event_index < len(events) and events[event_index][0] <= y:
            k, p, exponent = events[event_index]
            prefix_a = iv.add(prefix_a, iv.qmul(log_values[p], F(1, k)))
            prefix_b = iv.add(prefix_b, log_values[p])
            event_index += 1
        # Q(y)-gamma*y: gamma is removed only from this comparison because
        # its triangular moment vanishes exactly, as proved analytically.
        values[y] = iv.sub(iv.add(iv.rat(y), iv.qmul(prefix_a, y)),
                           iv.add(iv.qmul(iv.log_int(y), y), prefix_b))

    log_ratio = iv.sub(iv.qmul(iv.log_int(2), 2), iv.log_int(3))
    rows = []
    signs = {'positive': 0, 'negative': 0, 'contains_zero': 0}
    for n in parameters:
        local_lambda = iv.ZERO
        local_prime = iv.ZERO
        local_powers = iv.ZERO
        active_prime_events = 0
        active_higher_powers = 0
        for k, p, exponent in events:
            weight = phi(n, k)/k
            if not weight:
                continue
            term = iv.qmul(log_values[p], weight)
            local_lambda = iv.add(local_lambda, term)
            if exponent == 1:
                local_prime = iv.add(local_prime, term)
                active_prime_events += 1
            else:
                local_powers = iv.add(local_powers, term)
                active_higher_powers += 1
        t = iv.sub(log_ratio, local_lambda)
        delta = iv.sub(log_ratio, local_prime)
        t_endpoint = iv.sub(iv.qmul(iv.sub(values[12*n], values[9*n]), F(1, 3*n)),
                            iv.qmul(iv.sub(values[16*n], values[12*n]), F(1, 4*n)))
        assert iv.overlap(t, t_endpoint)
        assert iv.overlap(delta, iv.add(t, local_powers))
        assert local_powers[0] >= 0
        assert F(local_powers[1], iv.S)**2*n <= F(256, 9)
        # Stronger observed finite kernel payment, separate from the universal
        # analytic proof: max(phi/k)=1/(12n) would give 4/sqrt(n).
        assert F(local_powers[1], iv.S)**2*n <= 16
        sign = ('positive' if t[0] > 0 else 'negative' if t[1] < 0 else 'contains_zero')
        signs[sign] += 1
        rows.append({'n': n, 'packet': [9*n, 12*n, 16*n],
                     't_lambda_local': iv.record(t),
                     't_lambda_three_endpoints': iv.record(t_endpoint),
                     'ordinary_prime_deficit': iv.record(delta),
                     'higher_prime_power_payment': iv.record(local_powers),
                     'normalized_positive_budget': iv.record(iv.qmul(iv.square(iv.positive(t)), F(343*n, 81))),
                     'active_ordinary_primes': active_prime_events,
                     'active_higher_prime_powers': active_higher_powers,
                     'local_and_endpoint_intervals_overlap': True,
                     'prime_power_payment_squared_times_n_le_256_over_9': True})

    beta = iv.qmul(iv.sub(iv.sub(iv.log_int(28), iv.log_int(5)), iv.ONE), F(7, 10))
    assert beta[0] > iv.rat(F(1, 2))[1]
    return {'largest_integer_examined': bound, 'prime_sieve_count': prime_count,
            'prime_power_event_count': len(events), 'sparse_endpoint_count': len(queries),
            'arithmetic_sample_count': len(parameters), 'sample_signs': signs,
            'beta_interval': iv.record(beta), 'beta_strictly_exceeds_half': True,
            'background_log_4_over_3': iv.record(log_ratio), 'rows': rows}


def rh_constant_checks(prior, iv):
    """Certify explicit real constants, without querying a zeta zero.

    Their use as a bound for t is conditional on RH. The numerical interval
    calculation itself uses only the frozen gamma enclosure and rational tails.
    """
    family_path = prior/'prefix_compute'/'fixed_matched_family.json'
    gamma_record = json.loads(family_path.read_text())['gamma']
    gamma = (iv.rat(F(gamma_record['lower']))[0],
             iv.rat(F(gamma_record['upper']))[1])

    def atan_interval(q, terms=100):
        x = F(1, q)
        value = sum(((-1)**j*x**(2*j+1)/F(2*j+1)
                     for j in range(terms)), F(0))
        remainder = x**(2*terms+1)/F(2*terms+1)
        if terms % 2:
            return value-remainder, value
        return value, value+remainder

    a, b = atan_interval(5), atan_interval(239)
    pi_exact = (16*a[0]-4*b[1], 16*a[1]-4*b[0])
    pi_iv = (iv.rat(pi_exact[0])[0], iv.rat(pi_exact[1])[1])
    assert 3*iv.S < pi_iv[0] < pi_iv[1] < 4*iv.S
    # Rational verification of the Machin angle: tan(4 atan(1/5)-atan(1/239))=1.
    z = F(1, 5)
    z2 = 2*z/(1-z*z)
    z4 = 2*z2/(1-z2*z2)
    assert (z4-F(1, 239))/(1+z4/F(239)) == 1
    log_pi = (iv.add(iv.LOG_TWO, iv.log_unit(pi_iv[0], 2*iv.S))[0],
              iv.add(iv.LOG_TWO, iv.log_unit(pi_iv[1], 2*iv.S))[1])
    root3_floor = isqrt(3*iv.S*iv.S)
    root3 = (root3_floor, root3_floor+1)
    assert root3_floor**2 <= 3*iv.S**2 < (root3_floor+1)**2
    bracket = iv.sub(iv.sub(iv.sub(iv.qmul(iv.log_int(7), 7),
                                  iv.qmul(iv.log_int(2), 4)),
                           iv.qmul(iv.log_int(3), 8)), iv.add(gamma, log_pi))
    a43 = iv.qmul(bracket, F(1, 3))
    c_geo = iv.qmul(iv.mul(root3, bracket), F(1, 6))
    assert a43[0] > 0 and c_geo[0] > 0
    c_uniform = iv.add(c_geo, iv.rat(F(1, 1440)))
    c0 = iv.sub(iv.add(iv.rat(2), gamma),
                iv.add(iv.qmul(iv.log_int(2), 2), log_pi))
    old_uniform = iv.add(iv.mul(c0, iv.add(iv.rat(2), iv.qmul(root3, F(7, 6)))),
                         iv.rat(F(1, 1440)))
    assert c_uniform[1] < old_uniform[0]
    return {'status': 'FINITE_CONSTANT_CERTIFICATION_RH_BOUND_IS_CONDITIONAL',
            'gamma_input_sha256': digest(family_path),
            'gamma_interval': iv.record(gamma),
            'pi_interval': iv.record(pi_iv),
            'log_pi_interval': iv.record(log_pi),
            'sqrt_three_interval': iv.record(root3),
            'A_four_over_three': iv.record(a43),
            'C_geo_leading': iv.record(c_geo),
            'C_geo_uniform_including_trivial_zero_tail': iv.record(c_uniform),
            'previous_uniform_RH_constant': iv.record(old_uniform),
            'machin_arctan_terms_each': 100,
            'zero_queries': 0}


def main():
    here = Path(__file__).resolve().parent
    root = here.parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument('--prior', type=Path,
                        default=root/'prior/extracted/riemann_cumulative_haar_20261123')
    parser.add_argument('--input', type=Path, default=here/'fixed_input.json')
    parser.add_argument('--output', type=Path, default=here/'geometric_criterion_certificate.json')
    args = parser.parse_args()
    fixed = json.loads(args.input.read_text())
    assert fixed['geometry'] == [9, 12, 16]
    iv, dependency = load_interval_module(args.prior)
    exact = exact_kernels(fixed['source_pulse_parameters'])
    numeric = numeric_checks(fixed['arithmetic_parameters'], iv)
    constants = rh_constant_checks(args.prior, iv)
    result = {'schema': 'FIXED_GEOMETRIC_CRITERION_CERTIFICATE_V1',
              'status': 'AUTHOR_FINITE_CHECKS_NOT_INDEPENDENT_REVIEW',
              'researcher_id': 'EM-DIRECT-E7808F',
              'activity_id': 'RA-0B92AAF774CA466C1C1BC38B',
              'scope': 'No finite calculation is used to infer RH or any unbounded bound.',
              'source_hashes': {'fixed_input_sha256': digest(args.input),
                                'script_sha256': digest(Path(__file__)),
                                'outward_interval_dependency_sha256': digest(dependency)},
              'arithmetic': {'interval_digits': iv.DIGITS,
                             'log_series_terms': iv.LOG_TERMS,
                             'rounding': 'outward integer intervals with exact rational remainder',
                             'full_thickness_road_cache_generated_or_read': False,
                             'zero_queries': 0},
              'exact_kernel_checks': exact, 'finite_local_arithmetic': numeric,
              'conditional_RH_constants': constants}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'source_impulse_checks': exact['source_impulse_checks'],
                      'background_checks': len(exact['parameters']),
                      'arithmetic_samples': numeric['arithmetic_sample_count'],
                      'largest_integer_examined': numeric['largest_integer_examined'],
                      'sample_signs': numeric['sample_signs'],
                      'beta_interval': numeric['beta_interval'],
                      'C_geo_leading': constants['C_geo_leading'],
                      'C_geo_uniform': constants['C_geo_uniform_including_trivial_zero_tail'],
                      'all_checks_passed': True}, ensure_ascii=False))


if __name__ == '__main__':
    main()
