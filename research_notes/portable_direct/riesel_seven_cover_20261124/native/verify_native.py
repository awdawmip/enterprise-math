#!/usr/bin/env python3
"""Native BRC trajectories of the minimum R2 seven-cover and ternary minimum.

Both complete residue-value periods are executed. The integer register is never
replaced by its residues. Native joint mixed-radix/cofactor readouts retain an
invertible description of each state in addition to individual prime readouts.
The all-prime classification and minimum proof are separate mathematical inputs.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha1, sha256
import json
from math import gcd, lcm, prod
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
BASE_REL = Path('research_notes/portable_direct/riesel_mixed_20261119/certificate.json')
GAP_REL = Path('research_notes/portable_direct/riesel_spectrum_20261121/gap/small_gap_certificate.json')
BASE_BLOB = 'c1909a5e2e209b0f6bd5f613d0f758dde45caee9'
NATIVE_COMMIT = 'b1efc6c805661ed7b476e6e730107da6043176ee'
V10_COMMIT = 'f57dd6fd49d5b3f0a12abb3703c76edd6dbd37b5'
V = (5, 13, 11, 61, 331)
W = (19, 37, 73, 109)
FIXED_BINARY = (433, 38737)
L, L2 = 80754838636615, 1354510679787418425415
R1_RESIDUE, R2_RESIDUE = 12926327728523, 602924359709868072943
EXTRA_ORDERS = {5: 4, 13: 12, 11: 10, 61: 60, 331: 30,
                19: 18, 37: 36, 73: 9, 109: 36, 433: 72, 38737: 72,
                181: 180, 631: 45, 23311: 45,
                262657: 27, 87211: 54, 246241: 108}
CASES = [
    {'label': 'R2_minimum_complete_cost_seven',
     'family': 'modulo_five',
     'a': 168515727251568031139784117408423468924151126118048106286760549300706338389494633573,
     'rows': [(5, 1), (13, 0), (19, 4), (73, 1),
              (631, 16), (23311, 25), (181, 34)],
     'coverage_period_n': 1260,
     'residue_value_period_n': 20160,
     'expected_missing_per_coverage_period': [216, 108, 39, 26, 13, 8, 3, 0]},
    {'label': 'R2_minimum_ternary_cost_seven',
     'family': 'ternary',
     'a': 1046533155647696956851681902279650889819246480725727047415947079817885251912744029965820233,
     'rows': [(5, 1), (13, 0), (19, 4), (73, 1),
              (262657, 16), (87211, 7), (246241, 52)],
     'coverage_period_n': 3780,
     'residue_value_period_n': 60480,
     'expected_missing_per_coverage_period': [648, 324, 117, 78, 39, 26, 13, 0]},
]


def blob(data):
    return sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def prime_factors(n):
    result, p = set(), 2
    while p*p <= n:
        while n % p == 0:
            result.add(p)
            n //= p
        p += 1
    if n > 1:
        result.add(n)
    return result


def unsigned_bytes(value):
    return value.to_bytes((value.bit_length()+7)//8, 'big')


def digest_integer(target, value):
    data = unsigned_bytes(value)
    target.update(len(data).to_bytes(8, 'big'))
    target.update(data)


def main():
    root = next(p for p in HERE.parents if (p/BASE_REL).is_file())
    source_default = next((p for p in (root/'src', root/'vendor_src')
                           if (p/'enterprise_math/brc_transport.py').is_file()), None)
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-dir', type=Path, default=source_default)
    parser.add_argument('--output', type=Path, default=HERE/'native_certificate.json')
    args = parser.parse_args()
    if args.source_dir is None:
        parser.error('Pass --source-dir for the pinned native source directory.')

    # One source-identity check for the shared execution, before import.
    base_bytes = (root/BASE_REL).read_bytes()
    assert blob(base_bytes) == BASE_BLOB
    base = json.loads(base_bytes)
    assert base['project_source_commit'] == NATIVE_COMMIT
    source_checks = []
    for filename, expected in base['project_source_blobs'].items():
        observed = blob((args.source_dir/'enterprise_math'/filename).read_bytes())
        assert observed == expected
        source_checks.append({'module': filename, 'git_blob': observed})
    gap_bytes = (root/GAP_REL).read_bytes()
    gap = json.loads(gap_bytes)
    astar, M = int(gap['a_star']), int(gap['M'])
    P, H = set(gap['P']), set(gap['H'])
    assert prod(P) == M and len(P) == 20 and len(H) == 36
    assert prod(V+W) == L and prod(V+W+FIXED_BINARY) == L2
    common31 = sorted(P | set(V+W+FIXED_BINARY))
    assert len(common31) == 31
    fixed_joint_modulus = prod(common31)
    assert fixed_joint_modulus == M*L2
    assert (CASES[1]['a']-CASES[0]['a']) % (6*M*L2) == 0
    orders = {row['p']: row['order'] for row in base['original']['rows']}
    assert set(orders) == P
    orders.update(EXTRA_ORDERS)
    for q, d in orders.items():
        assert pow(2, d, q) == 1
        assert all(pow(2, d//p, q) != 1 for p in prime_factors(d))
    assert lcm(*(orders[q] for q in P)) == 6720

    sys.path.insert(0, str(args.source_dir))
    from enterprise_math.brc_transport import Affine, EffectHistogram, euclidean_digits, recompose
    step = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])
    twice = step.then(step)
    assert step.entries == ((Fraction(1), Affine(((2,),), (1,)), 1),)
    assert twice.entries == ((Fraction(1), Affine(((4,),), (3,)), 1),)

    def evaluate(effect, value):
        (point, weight), = effect.evaluate((value,)).items()
        assert weight.entries == ((Fraction(1), 1),)
        assert point[0].denominator == 1
        return int(point[0])

    references31 = {}
    direct_comparisons31 = 0
    records = []
    for case_index, case in enumerate(CASES):
        started = time.monotonic()
        a, rows = case['a'], case['rows']
        assert a >= astar and a % 2 == 1 and (a-astar) % (6*M) == 0
        assert a % L == R1_RESIDUE and a % L2 == R2_RESIDUE
        assert (a % 433, a % 38737) == (0, 38733)
        channels = sorted(set(common31) | {q for q, _ in rows})
        assert len(channels) == 34 and len({q for q, _ in rows}) == 7
        selected = {q for q, _ in rows}
        assert not selected.intersection(P)
        period = lcm(*(orders[q] for q in channels))
        selected_full_period = lcm(*(orders[q] for q in P | selected))
        coverage_period = lcm(210, *(orders[q] for q, _ in rows))
        assert period == selected_full_period == case['residue_value_period_n']
        assert coverage_period == case['coverage_period_n']
        assert period // coverage_period == 16
        for q, c in rows:
            assert a*a*pow(4, c, q) % q == 1
        assert 2*a*a-1 > max(channels)
        joint_modulus = prod(channels)
        radix_weights, radix_product = [], 1
        for q in channels:
            radix_weights.append(radix_product)
            radix_product *= q
        assert radix_product == joint_modulus
        prefix_sets = [set(q for q, _ in rows[:t]) for t in range(8)]
        missing, private = [0]*8, {}
        x = scalar_x = previous_even = a*a-1
        native_states_digest = sha256()
        joint_digest = sha256()
        prime_readout_digest = sha256()
        readouts = joint_readouts = formula_checks = scalar_checks = 0
        old_equalities = fiber_equalities = even_evaluations = 0
        joint_recompositions = joint_scalar_equalities = 0
        last_record = None
        for n in range(1, period+1):
            x = evaluate(step, x)
            scalar_x = 2*scalar_x+1
            assert x == scalar_x == (a*a << n)-1
            scalar_checks += 1
            if n % 2 == 0:
                assert evaluate(twice, previous_even) == x
                previous_even = x
                even_evaluations += 1
            digest_integer(native_states_digest, x)
            hits, residues, scalar_cofactors = set(), {}, {}
            for q in channels:
                quotient, (residual,) = euclidean_digits(x, (q,))
                assert (quotient, residual) == divmod(scalar_x, q)
                assert quotient*q+residual == x and 0 <= residual < q
                assert residual == (a*a*pow(2, n, q)-1) % q
                readouts += 1
                formula_checks += 1
                residues[q] = residual
                scalar_cofactors[q] = quotient
                prime_readout_digest.update(residual.to_bytes(8, 'big'))
                if residual == 0:
                    assert 1 < q < x
                    hits.add(q)
                if q in P:
                    assert residual == (astar*astar*pow(2, n, q)-1) % q
                    old_equalities += 1
                else:
                    if q in V+W+FIXED_BINARY:
                        assert residual == (R2_RESIDUE*R2_RESIDUE*pow(2, n, q)-1) % q
                        fiber_equalities += 1

            # These native mixed-radix digits differ from the prime residues.
            # The common cofactor and all digits form one invertible readout.
            joint_quotient, digits = euclidean_digits(x, tuple(channels))
            joint_readouts += 1
            assert len(digits) == len(channels)
            assert all(0 <= d < q for d, q in zip(digits, channels))
            packed_remainder = sum(d*w for d, w in zip(digits, radix_weights))
            assert (joint_quotient, packed_remainder) == divmod(scalar_x, joint_modulus)
            assert x == joint_quotient*joint_modulus+packed_remainder
            assert recompose(joint_quotient, digits, tuple(channels)) == x
            joint_recompositions += 1
            joint_scalar_equalities += 1
            digest_integer(joint_digest, joint_quotient)
            for d in digits:
                joint_digest.update(d.to_bytes(8, 'big'))

            vector31 = tuple(residues[q] for q in common31)
            if case_index == 0:
                references31[n] = vector31
            elif n in references31:
                assert vector31 == references31[n]
                direct_comparisons31 += len(common31)
            old_hole = not bool(hits.intersection(P))
            assert old_hole == (n % 2 == 0 and (n//2) % 105 in H)
            for q, c in rows:
                assert (q in hits) == (n % orders[q] == 2*c % orders[q])
            if old_hole:
                for t, prefix in enumerate(prefix_sets):
                    if not hits.intersection(prefix):
                        missing[t] += 1
                selected_hits = hits.intersection(selected)
                if len(selected_hits) == 1:
                    q, = selected_hits
                    if q not in private:
                        private[q] = {'n': n, 'cofactor_hex': hex(scalar_cofactors[q]),
                                      'state_hex': hex(x), 'residue': 0}
            if n == period:
                assert all(residues[q] == (a*a-1) % q for q in channels)
                assert packed_remainder == (a*a-1) % joint_modulus
                last_record = {
                    'state_hex': hex(x), 'state_bits': x.bit_length(),
                    'state_sha256_unsigned_big_endian': sha256(unsigned_bytes(x)).hexdigest(),
                    'joint_cofactor_hex': hex(joint_quotient),
                    'joint_mixed_radix_digits': digits,
                    'joint_packed_remainder': str(packed_remainder),
                    'prime_residues': residues,
                    'all_native_prime_cofactors_hex': {q: hex(c) for q, c in scalar_cofactors.items()},
                    'residue_value_period_closed': True}
            if n % 10080 == 0:
                print(json.dumps({'progress': case['label'], 'native_steps': n,
                                  'target': period, 'elapsed_seconds': round(time.monotonic()-started, 3)}),
                      flush=True)
        expected = [16*v for v in case['expected_missing_per_coverage_period']]
        assert missing == expected and missing[-1] == 0
        assert set(private) == selected
        assert readouts == formula_checks == 34*period
        assert joint_readouts == joint_recompositions == joint_scalar_equalities == scalar_checks == period
        assert even_evaluations == period//2
        records.append({
            'label': case['label'], 'family': case['family'],
            'root': str(a), 'root_digits': len(str(a)), 'fixed_fiber': 'R2',
            'ordered_rows': [{'q': q, 'phase_u': c, 'order2': orders[q],
                              'root_residue': a % q} for q, c in rows],
            'coverage_period_n': coverage_period, 'executed_residue_value_period_n': period,
            'complete_coverage_periods_executed': 16,
            'readout_channels': channels, 'joint_channel_count': len(channels),
            'joint_modulus': str(joint_modulus),
            'uncovered_counts_per_coverage_period': case['expected_missing_per_coverage_period'],
            'uncovered_counts_in_native_execution': missing,
            'proper_private_old_hole_witnesses': private,
            'all_assigned_divisors_proper': True,
            'native_single_step_updates': period,
            'native_two_step_evaluations': even_evaluations,
            'native_effect_evaluations': period+even_evaluations,
            'scalar_full_state_comparisons': scalar_checks,
            'closed_form_full_state_comparisons': period,
            'native_individual_prime_readouts': readouts,
            'scalar_individual_prime_readout_comparisons': readouts,
            'closed_form_prime_readout_comparisons': formula_checks,
            'native_joint_readouts': joint_readouts,
            'native_joint_recompositions': joint_recompositions,
            'scalar_joint_division_comparisons': joint_scalar_equalities,
            'old_projection_equalities': old_equalities,
            'additional_fixed_fiber_equalities': fiber_equalities,
            'native_state_stream_sha256': native_states_digest.hexdigest(),
            'native_joint_cofactor_digit_stream_sha256': joint_digest.hexdigest(),
            'native_prime_residue_stream_sha256': prime_readout_digest.hexdigest(),
            'full_final_state_and_joint_readout': last_record,
            'elapsed_seconds': round(time.monotonic()-started, 6)})

    count_keys = ['native_single_step_updates', 'native_two_step_evaluations',
                  'native_effect_evaluations', 'scalar_full_state_comparisons',
                  'closed_form_full_state_comparisons', 'native_individual_prime_readouts',
                  'scalar_individual_prime_readout_comparisons', 'closed_form_prime_readout_comparisons',
                  'native_joint_readouts', 'native_joint_recompositions',
                  'scalar_joint_division_comparisons', 'old_projection_equalities',
                  'additional_fixed_fiber_equalities']
    totals = {key: sum(c[key] for c in records) for key in count_keys}
    assert totals['native_single_step_updates'] == 80640
    assert totals['native_two_step_evaluations'] == 40320
    assert totals['native_individual_prime_readouts'] == 2741760
    assert direct_comparisons31 == 624960
    result = {
        'schema': 'riesel-r2-all-seven-cover-minima-native-v1',
        'status': 'AUTHOR_NATIVE_EXECUTION; NOT_INDEPENDENT_REVIEW',
        'researcher': 'EM-DIRECT-970E1C', 'activity': 'RA-D2EC212845B63844081F9A14',
        'native_source_commit': NATIVE_COMMIT, 'native_source_blobs': source_checks,
        'base_certificate_git_blob': BASE_BLOB,
        'old_hole_certificate_git_blob_observed': blob(gap_bytes),
        'reused_prior_native_harness': {'commit': V10_COMMIT,
            'path': 'research_notes/portable_direct/riesel_finite_observers_20261124/native/verify_native.py',
            'scope': 'Pinned EffectHistogram state update, composition and per-prime readout pattern; new execution adds the complete residue-value periods and native joint cofactor readouts.'},
        'old_prime_order_lcm': 6720, 'exact_base2_orders': orders,
        'cases': records, 'totals': totals,
        'native_euclidean_digits_calls': totals['native_individual_prime_readouts']+totals['native_joint_readouts'],
        'between_root_fixed31_channel_equalities': direct_comparisons31,
        'between_root_comparison_indices': [1, 20160],
        'all_future_root_congruence_modulus': str(6*M*L2),
        'fixed31_joint_modulus': str(fixed_joint_modulus),
        'all_future_fixed31_equality_proof': 'Equal root residues modulo each fixed prime imply equal F_n residues for every n>=0; the root difference is divisible by 6*M*L2.',
        'coverage_bridge': 'The old-hole predicate has period210. Selected prime-zero predicates have the verified base-two orders. The coverage periods1260 and3780 divide the actually executed complete residue-value periods20160 and60480. Each has zero terminal uncovered count and all divisors proper.',
        'integer_retention': 'Every native step receives the entire previous integer. Each state is compared with a scalar integer recurrence and the closed formula. Native joint (cofactor, mixed-radix digits) recomposes to that same integer; final full integers, every final prime cofactor, native joint digits/cofactor, and stream digests are retained.',
        'joint_readout_distinction': 'Mixed-radix digits are quotient-chain digits, not the independent residues x mod q. Both readouts are recorded and checked against the same integer.',
        'native_semantics': 'Fixed X6, typed integer register, positive singleton weight1/multiplicity1; one step2x+1 and native composed two-step4x+3. Arithmetic index is not physical time; prime channels are observations, not axes.',
        'mathematical_scope': 'Native execution verifies these two concrete trajectories, coverage counts and lossless readouts. All-prime classification, minimum-root scope and delta_P=7 require the companion analytic proof and exact CRT certificate. No total-minimum equality tau=27 is inferred.',
        'review_boundary': 'Shared-context author execution only; no independent project Review, formal acceptance or Foundation promotion.'}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'cases': len(records), 'totals': totals,
                      'native_euclidean_digits_calls': result['native_euclidean_digits_calls'],
                      'between_root_fixed31_channel_equalities': direct_comparisons31,
                      'output': str(args.output)}, indent=2))


if __name__ == '__main__':
    main()
