"""Bounded typed-BRC arithmetic certificate for one declared family member.

This checks input conditions only. No phase word, Shor trajectory, ideal
distribution, TV calculation, or factorization routine is executed.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import sys
from pathlib import Path
from time import perf_counter_ns

ROOT = Path(__file__).resolve().parent
for directory in ('sparse', 'completion'):
    sys.path.insert(0, str(ROOT.parent / directory))

import sparse_modular as sparse
import typed_integer_prechecks as typed
import stage78.shor_benchmark as benchmark
from stage45.brc_loop_recheck import CALLS, verify_vendor


def packed(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(',', ':')).encode('utf-8')


def typed_gcd(left, right):
    """Euclidean control using actual adder-derived long-division outputs."""
    initial = (left, right)
    steps = []
    while right:
        quotient, remainder, division = typed.divide(left, right)
        steps.append({'left': left, 'right': right, 'quotient': quotient,
                      'remainder': remainder, 'division': division})
        left, right = right, remainder
    return left, {'operation': 'BRC_TYPED_EUCLID', 'inputs': initial,
                  'steps': steps, 'gcd': left}


def source_record(path):
    path = Path(path).resolve()
    return {'path': str(path),
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def build(activity):
    started = perf_counter_ns()
    vendor = verify_vendor()
    first_call = len(CALLS)
    _, native_adder = sparse.native_adder()
    p, m = 5, 0
    eighteen_m, eighteen_m_trace = typed.multiply(18, m)
    a, a_trace = typed.add(eighteen_m, 4)
    relation, minus_trace = typed.compare(a, 1)
    assert relation > 0
    a_minus_one = minus_trace['low_difference']
    a_plus_one, plus_trace = typed.add(a, 1)
    a_power_p, power_trace = typed.power(a, p)
    numerator, numerator_trace = typed.add(a_power_p, 1)
    q, remainder, quotient_trace = typed.divide(numerator, a_plus_one)
    assert remainder == 0
    multiplied_back, multiplication_back = typed.multiply(a_plus_one, q)
    assert multiplied_back == numerator
    N, product_trace = typed.multiply(a_minus_one, q)
    assert (a, q, N, a_power_p, numerator) == (4, 205, 615, 1024, 1025)

    prime_p = typed.wilson_primality(p)
    prime_p_replay = typed.verify_precheck(prime_p)
    assert prime_p['status'] == 'PRIME'
    assert prime_p['factorial_residue'] == 4

    coprime_factors, coprime_trace = typed_gcd(a_minus_one, q)
    unit_gcd, unit_trace = typed_gcd(a, N)
    unnecessary_gcd, unnecessary_trace = typed_gcd(a_plus_one, q)
    assert (coprime_factors, unit_gcd, unnecessary_gcd) == (1, 1, 5)
    n_over_three, n_rem_three, n_div_three = typed.divide(N, 3)
    _, second_rem_three, second_div_three = typed.divide(n_over_three, 3)
    assert n_rem_three == 0 and second_rem_three == 1

    exponents = (1, 2, 5, 10)
    powers = {str(e): sparse.sparse_modular_power_trace(N, a, e)
              for e in exponents}
    assert [powers[str(e)]['value'] for e in exponents] == [4, 16, 409, 1]
    assert powers['10']['value'] == 1
    assert all(powers[str(e)]['value'] != 1 for e in (1, 2, 5))
    two_p, two_p_trace = typed.multiply(2, p)
    assert two_p == 10

    half = powers['5']['value']
    relation, half_minus_trace = typed.compare(half, 1)
    assert relation > 0
    half_minus_one = half_minus_trace['low_difference']
    half_plus_one, half_plus_trace = typed.add(half, 1)
    lower_gcd, lower_gcd_trace = typed_gcd(half_minus_one, N)
    upper_gcd, upper_gcd_trace = typed_gcd(half_plus_one, N)
    relation, n_minus_trace = typed.compare(N, 1)
    n_minus_one = n_minus_trace['low_difference']
    assert 1 < lower_gcd < N and 1 < upper_gcd < N
    assert (lower_gcd, upper_gcd) == (a_minus_one, q)
    assert half != 1 and half != n_minus_one

    # Retain the actual complete column certificates behind every power step,
    # not only their hashes or the few selected endpoint values.
    bases = sorted({step['b'] for trace in powers.values()
                    for step in trace['steps']})
    column_certificates = {}
    column_replays = {}
    for b in bases:
        _, certificate = sparse.compile_modular_permutation(N, b)
        key = sparse.digest(certificate)
        column_certificates[key] = certificate
        column_replays[key] = sparse.verify_modular_certificate(certificate)
    for trace in powers.values():
        for step in trace['steps']:
            assert step['certificate_sha256'] in column_certificates

    certificate = {
        'schema': 'BRC_FAMILY_N615_INPUT_CERTIFICATE_V1',
        'activity': activity,
        'status': 'AUTHOR_EXECUTED_BOUNDED_INPUT_CHECK_UNREVIEWED_NOT_ADMITTED',
        'global_knowledge_canonical': '441ebefd3ba2372abf9044d802fa816b4c4ef895',
        'registration_source': 'f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf',
        'frozen_stage87_source_head': '0852cad130c1d877174d235687cf60c19f318c58',
        'fixture': {'m': m, 'p': p, 'a': a, 'q': q, 'N': N},
        'family': 'a=18m+4; q=Phi_(2p)(a)=(a^p+1)/(a+1); N=(a-1)q',
        'family_construction': {
            'eighteen_m': eighteen_m_trace, 'a': a_trace,
            'a_minus_one': minus_trace, 'a_plus_one': plus_trace,
            'a_to_p': power_trace, 'numerator_add_one': numerator_trace,
            'q_exact_quotient': quotient_trace,
            'multiply_back_identity': multiplication_back,
            'N_product': product_trace, 'twice_prime': two_p_trace},
        'prime_p_certificate': prime_p,
        'prime_p_certificate_replay': prime_p_replay,
        'coprime_factor_trace': coprime_trace,
        'unit_base_trace': unit_trace,
        'unneeded_a_plus_one_q_gcd_trace': unnecessary_trace,
        'valuation_three': {'value': 1, 'first_division': n_div_three,
                            'second_division': second_div_three},
        'modular_power_traces': powers,
        'modular_column_certificates': column_certificates,
        'modular_column_certificate_replays': column_replays,
        'half_order_gcds': {
            'half_residue': half, 'half_minus_one': half_minus_trace,
            'half_plus_one': half_plus_trace, 'N_minus_one': n_minus_trace,
            'minus_gcd_trace': lower_gcd_trace,
            'plus_gcd_trace': upper_gcd_trace},
        'conclusions': {
            'p_is_prime': True, 'coprime_a_minus_one_and_q': True,
            'a_is_unit_mod_N': True, 'valuation_three_of_N': 1,
            'N_is_odd_composite': True, 'N_is_not_a_perfect_power': True,
            'N_is_not_a_prime_power': True, 'verified_order': 10,
            'proper_divisors_of_10_checked': [1, 2, 5],
            'half_order_residue': half, 'good_base': True,
            'half_order_gcds': [lower_gcd, upper_gcd]},
        'native_adder': native_adder, 'vendor': vendor,
        'executed_source_files': [source_record(path) for path in (
            __file__, sparse.__file__, typed.__file__, benchmark.__file__)],
        'actual_BRC_core_calls': len(CALLS) - first_call,
        'call_receipts': CALLS[first_call:],
        'resource_counts': {
            'complete_modular_maps': len(column_certificates),
            'complete_modular_basis_columns': sum(c['size'] for c in column_certificates.values()),
            'modular_compile_adder_digit_applications': sum(
                c['resource_counts']['adder_digit_applications']
                for c in column_certificates.values()),
            'modular_power_exponents': list(exponents),
            'wilson_input': p,
            'core_calls_are_not_total_arithmetic_operation_count': True},
        'phase_propagation_run': False, 'ideal_distribution_run': False,
        'TV_measured': False, 'full_factorization_run': False,
        'Wilson_N615_run': False, 'primality_of_q_claimed': False,
        'claim_scope': 'declared family input conditions only; no finite-N TV lower bound or sampled Shor outcome',
        'elapsed_ns': perf_counter_ns() - started,
    }
    return certificate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--activity', required=True)
    args = parser.parse_args()
    certificate = build(args.activity)
    raw = packed(certificate)
    destination = ROOT / 'FAMILY_N615_CERTIFICATE.json.gz'
    temporary = destination.with_suffix(destination.suffix + '.tmp')
    temporary.write_bytes(gzip.compress(raw, mtime=0))
    temporary.replace(destination)
    reread = json.loads(gzip.decompress(destination.read_bytes()))
    assert packed(reread) == raw
    print(json.dumps({'path': str(destination),
        'uncompressed_payload_sha256': hashlib.sha256(raw).hexdigest(),
        'uncompressed_bytes': len(raw), 'compressed_bytes': destination.stat().st_size,
        'conclusions': certificate['conclusions'],
        'actual_BRC_core_calls': certificate['actual_BRC_core_calls'],
        'resource_counts': certificate['resource_counts']}), flush=True)


if __name__ == '__main__':
    main()
