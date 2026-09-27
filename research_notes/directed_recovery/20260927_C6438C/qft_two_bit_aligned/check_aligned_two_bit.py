"""Declared six-tuple actual typed checker; CODE ONLY until authorized."""
from copy import deepcopy
from pathlib import Path
import gzip
import hashlib
import json
import time
import traceback

from aligned_two_bit import (AlignedTwoBitObserver, verify_aligned_certificate,
    TypedFloorMoments, typed_two_power, PROOF, PROOF_PIN, DIRECT, DIRECT_PIN, sha)
from stage45.brc_loop_recheck import CALLS

ROOT = Path(__file__).resolve().parent
CASES = ((2, 0, 1, 1), (3, 0, 1, 3), (3, 1, 2, 2),
         (3, 1, 2, 4), (4, 1, 3, 6), (4, 2, 3, 20))
TARGETS = (ROOT/'TWO_BIT_ALIGNED_RESULTS.json.gz', ROOT/'TWO_BIT_ALIGNED_SUMMARY.json',
           ROOT/'TWO_BIT_ALIGNED_FAILED_EXECUTION.json.gz')
LIVE = {'stage': 'IMPORTED_NOT_STARTED', 'output': None, 'guard': None, 'observer': None,
        'brute_runner': None, 'brute_digits': [], 'brute_pairs': [], 'brute_values': None,
        'replay_capture': [], 'tamper_attempts': [], 'current_tamper': None,
        'input_attempts': [], 'current_input': None, 'call_intervals': []}


def typed_keys(item):
    if type(item) is dict:
        return {'object_entries': [{'key_type': type(key).__name__, 'key': key,
                                   'value': typed_keys(value)} for key, value in item.items()]}
    if type(item) in (tuple, list):
        return [typed_keys(x) for x in item]
    return item


def unfinished_runner(runner):
    return None if runner is None else deepcopy({
        'arithmetic_operations': runner.arithmetic.operations, 'arithmetic_stats': runner.arithmetic.stats,
        'signed_operations': runner.signed_operations, 'moment_nodes': runner.nodes,
        'window_weight_queries': runner.weight_queries, 'stats': runner.stats})


def interval(category, label, first):
    record = {'category': category, 'label': label, 'start': first, 'stop': len(CALLS)}
    LIVE['call_intervals'].append(record)
    return record


def typed_pair_histogram(g, ell, k, R):
    """One ordered-pair pass per tuple, all buckets together; no host reference."""
    runner = TypedFloorMoments()
    LIVE['brute_runner'] = runner
    length = typed_two_power(runner, g)
    low_scale = typed_two_power(runner, ell)
    high_scale = typed_two_power(runner, k)
    digit_rows, digits = [], []
    LIVE['brute_digits'] = digit_rows
    for x in range(length):
        first = len(runner.signed_operations)
        low_quotient, low_remainder = runner.floor_div(x, low_scale)
        _, low_bit = runner.floor_div(low_quotient, 2)
        high_quotient, high_remainder = runner.floor_div(x, high_scale)
        _, high_bit = runner.floor_div(high_quotient, 2)
        bit_sum = runner.add(low_bit, high_bit)
        _, parity = runner.floor_div(bit_sum, 2)
        assert low_bit in (0, 1) and high_bit in (0, 1) and parity in (0, 1)
        digits.append(parity)
        digit_rows.append({'label': x, 'low_quotient': low_quotient, 'low_remainder': low_remainder,
            'low_bit': low_bit, 'high_quotient': high_quotient, 'high_remainder': high_remainder,
            'high_bit': high_bit, 'bit_sum': bit_sum, 'parity': parity,
            'signed_operations_start': first, 'signed_operations_stop': len(runner.signed_operations)})
    buckets = [0 for _ in range(R)]
    pairs = []
    LIVE['brute_pairs'], LIVE['brute_values'] = pairs, buckets
    for x in range(length):
        for y in range(length):
            first = len(runner.signed_operations)
            difference = runner.sub(y, x)
            quotient, residue = runner.floor_div(difference, R)
            sign = 1 if digits[x] == digits[y] else -1
            before = buckets[residue]
            after = runner.add(before, sign)
            buckets[residue] = after
            pairs.append({'x': x, 'y': y, 'difference': difference, 'quotient': quotient,
                'residue': residue, 'sign': sign, 'bucket_before': before, 'bucket_after': after,
                'signed_operations_start': first, 'signed_operations_stop': len(runner.signed_operations)})
    return buckets, {'length': length, 'low_scale': low_scale, 'high_scale': high_scale,
                    'digit_observations': digit_rows, 'pair_observations': pairs,
                    'all_residue_buckets_from_one_pair_pass': True,
                    'actual_integer_evidence': runner.evidence()}


def input_rejections():
    cases = ((True, 0, 1, 1, 0, 1), (1, 0, 1, 1, 0, 1), (3, -1, 2, 2, 0, 1),
             (3, 1, 1, 2, 0, 1), (3, 1, 3, 2, 0, 1), (3, 1, 2, 0, 0, 1),
             (3, 1, 2, 2, -1, 1), (3, 1, 2, 2, 2, 1), (3, 1, 2, 2, 0, 2),
             (3, False, 2, 2, 0, 1))
    records = []
    LIVE['input_attempts'] = records
    for args in cases:
        observer = AlignedTwoBitObserver()
        LIVE.update(observer=observer, current_input={'args': args, 'kind': 'ordinary_pre_rejection'})
        first = len(CALLS)
        try:
            observer.two_negative(*args[:5], stride=args[5])
        except ValueError as error:
            assert not observer.runner.arithmetic.operations and not observer.requests
            assert len(CALLS) == first
            records.append({'args': args, 'kind': 'ordinary_pre_rejection', 'rejected': True,
                            'error': str(error), 'actual_typed_operations': 0,
                            'call_interval': interval('input_pre_rejection', repr(args), first)})
        else:
            raise AssertionError('invalid ordinary input accepted')
    for args in ((3, 1, 2, 3, 0), (4, 2, 3, 6, 1)):
        observer = AlignedTwoBitObserver()
        LIVE.update(observer=observer, current_input={'args': args, 'kind': 'paid_unaligned_rejection'})
        first = len(CALLS)
        try:
            observer.two_negative(*args)
        except ValueError as error:
            receipt = observer.incomplete_snapshot()
            assert receipt['inflight_request']['alignment']['remainder'] > 0
            assert receipt['actual_integer_evidence']['arithmetic_operations'] and not observer.requests
            records.append({'args': args, 'kind': 'paid_unaligned_rejection', 'rejected': True,
                'error': str(error), 'incomplete_receipt': receipt,
                'call_interval': interval('paid_input_rejection', repr(args), first)})
            # A paid failure is terminal for this observer. The retained raw
            # trace is evidence, not an implicit resumable request prefix.
            reuse_args = (3, 1, 2, 2, 0)
            LIVE['current_input'] = {'args': reuse_args, 'kind': 'incomplete_observer_reuse'}
            reuse_first = len(CALLS)
            try:
                observer.two_negative(*reuse_args)
            except ValueError as reuse_error:
                assert observer.incomplete_snapshot() == receipt
                assert len(CALLS) == reuse_first
                records[-1]['reuse_rejection'] = {
                    'args': reuse_args, 'rejected': True, 'error': str(reuse_error),
                    'prior_inflight_and_all_evidence_unchanged': True,
                    'additional_typed_operations': 0,
                    'call_interval': interval('input_reuse_rejection', repr(args), reuse_first)}
            else:
                raise AssertionError('observer with paid incomplete work was reused')
        else:
            raise AssertionError('unaligned input accepted')
    LIVE['current_input'] = None
    return records


def negative_checks(certificates):
    attempts = []
    LIVE['tamper_attempts'] = attempts
    changes = (
        ('drop_half_modulus_orientation', 2, lambda c: c['requests'][1]['orientations'].pop()),
        ('compressed_length', 2, lambda c: c['requests'][0].__setitem__('M', 999)),
        ('shifted_zero_tail', 5, lambda c: c['requests'][13]['orientations'][0]['branches'][0]['shifted_zero_tail'].__setitem__('removed_zero_terms', 0)),
        ('original_branch_sign', 2, lambda c: c['requests'][1]['orientations'][0]['branches'][0].__setitem__('sign', -1)),
        ('compressed_step_parity', 3, lambda c: c['requests'][0]['h_parity'].__setitem__('remainder', 1)),
        ('original_raw_exponent', 2, lambda c: c['requests'][0].__setitem__('raw_denominator_exponent', 2)),
        ('signed_output', 0, lambda c: c['requests'][0].__setitem__('value', 999)),
        ('unaligned_input_paid_partial', 2, lambda c: c['requests'][0]['inputs'].__setitem__('R', 3)),
        ('source_early', 0, lambda c: c.__setitem__('source_sha256', '0'*64)),
        ('schema_early', 0, lambda c: c.__setitem__('schema', 'UNRELATED')),
        ('bool_input_early', 0, lambda c: c['requests'][0]['inputs'].__setitem__('g', True)),
        ('nonstring_key_early', 0, lambda c: c['requests'][0].__setitem__(0, 0)))
    for name, index, update in changes:
        attempted = deepcopy(certificates[index])
        update(attempted)
        encoded = typed_keys(attempted)
        capture = []
        LIVE.update(replay_capture=capture, current_tamper={'name': name, 'source_case_index': index,
                                                          'typed_key_encoding': encoded})
        first = len(CALLS)
        try:
            verify_aligned_certificate(attempted, replay_capture=capture)
        except ValueError as error:
            if name.endswith('_early'):
                assert not capture and len(CALLS) == first
            else:
                assert len(capture) == 1 and capture[0]['actual_integer_evidence']['arithmetic_operations']
                if name == 'unaligned_input_paid_partial':
                    assert capture[0]['complete_certificate'] is False
                    assert capture[0]['inflight_request']['alignment']['remainder'] > 0
                else:
                    assert capture[0]['schema'] == certificates[index]['schema']
            attempts.append({'name': name, 'source_case_index': index, 'rejected': True, 'error': str(error),
                'attempted_certificate_typed_key_encoding': encoded, 'actual_replay_certificates': capture,
                'call_interval': interval('negative_replay', name, first)})
        else:
            raise AssertionError('forged certificate accepted: '+name)
    LIVE['current_tamper'] = None
    return attempts


def cost(evidence):
    return {'arithmetic_stats': deepcopy(evidence['arithmetic_stats']),
            'typed_operations': len(evidence['arithmetic_operations']),
            'signed_operations': len(evidence['signed_operations']),
            'moment_nodes': len(evidence['moment_nodes']),
            'window_queries': len(evidence['window_weight_queries']),
            'moment_stats': deepcopy(evidence['stats'])}


def aggregate_cost(evidences):
    rows = [cost(e) for e in evidences]
    if not rows:
        return {'receipts': 0, 'sum': {}, 'max': {}}
    additive = ('adder_digit_replays', 'typed_operations', 'host_bit_wiring_operations',
                'host_bit_length_calls_in_arithmetic')
    total = {key: sum(row['arithmetic_stats'][key] for row in rows) for key in additive}
    for key in ('typed_operations', 'signed_operations', 'moment_nodes', 'window_queries'):
        # typed_operations is independently counted from the complete trace.
        value = sum(row[key] for row in rows)
        if key == 'typed_operations':
            assert total[key] == value
        total[key] = value
    for key in ('moment_requests', 'cache_hits'):
        total[key] = sum(row['moment_stats'][key] for row in rows)
    maxima = {key: max(row['moment_stats'][key] for row in rows)
              for key in ('max_recursion_depth', 'max_observed_integer_bits')}
    return {'receipts': len(rows), 'sum': total, 'max': maxima,
            'native_calls_counted_from_disjoint_process_intervals': True}


def coverage_checks(certificates):
    requests = [r for c in certificates for r in c['requests']]
    branches = [b for r in requests for o in r['orientations'] for b in o['branches']]
    assert len(requests) == 36
    assert any(r['H'] > 1 for r in requests)
    assert {r['h_parity']['remainder'] for r in requests} == {0, 1}
    assert any(o['empty'] for r in requests for o in r['orientations'])
    assert any(o.get('constant_low_remainder', 0) > 0 for r in requests for o in r['orientations'])
    assert any(b['shifted_zero_tail']['removed_zero_terms'] == 1 and b['shifted_weight'] > 0 for b in branches)
    assert any(b['original']['empty'] is False and b['shifted']['empty'] is True for b in branches)
    assert any(r['value'] < 0 for r in requests)
    for req in requests:
        assert req['raw_denominator_exponent'] == 2*req['inputs']['g']
        assert req['single_progression_calls'] <= 8 and req['top_level_table_calls'] <= 16
        assert [o['orientation'] for o in req['orientations']] == ['nonnegative_difference', 'negative_difference_magnitude']
        if req['inputs']['r'] == 0:
            assert req['orientations'][0]['head']['value'] == 0
            assert req['orientations'][1]['head']['value'] == req['inputs']['R']
        for o in req['orientations']:
            assert o['multiplicity'] == 1
            for b in o['branches']:
                assert b['original']['n'] == b['expected_n']['value']
                for p in (b['original'], b['shifted']):
                    assert len(p['table_calls']) == (0 if p['empty'] else 2)
                    assert all(len(table['outputs']) == 10 for table in p['table_calls'])
                    if not p['empty']:
                        assert p['head']['value'] < req['M']
    half = certificates[2]['requests'][1]['orientations']
    assert half[0]['head']['value'] == half[1]['head']['value'] and len(half) == 2
    return {'requests': len(requests), 'negative_output_seen': True, 'H_greater_than_one_seen': True,
            'both_compressed_step_parities_seen': True, 'nonzero_low_remainder_seen': True,
            'empty_orientation_seen': True, 'shifted_M_zero_tail_with_nonzero_weight_seen': True,
            'half_modulus_both_orientations_retained': True}


def main():
    started = time.perf_counter()
    LIVE['stage'] = 'CHECK_STARTUP_GUARD'
    guard_path = ROOT/'STARTUP_GUARD.json'
    guard = json.loads(guard_path.read_bytes())
    assert guard.get('activity_allowed') is True and guard.get('persistence_allowed') is True
    assert guard.get('activity_id') == 'RA-CAAAC604CB513AEA8BBC1DFC'
    assert guard.get('boundary') == 'startup' and guard.get('mode') == 'TASK_RESEARCH'
    assert guard.get('sync_debt_events') == []
    LIVE['guard'] = {'sha256': sha(guard_path), 'receipt': guard}
    source_names = ('aligned_two_bit.py', 'check_aligned_two_bit.py', 'DESIGN.md')
    sources = {name: sha(ROOT/name) for name in source_names}
    assert sha(PROOF) == PROOF_PIN and sha(DIRECT/'direct_signed_gap.py') == DIRECT_PIN
    output = {'status': 'RUNNING', 'source_sha256': sources, 'startup_guard': LIVE['guard'],
              'two_bit_proof_sha256': PROOF_PIN, 'cases': [],
              'scope': 'V-divides-R two-bit scalar integer observer; one comparator bucket pass per tuple; no full Gram or order search'}
    LIVE['output'] = output
    certificates = []
    for g, ell, k, R in CASES:
        LIVE.update(stage='ALIGNED_PRODUCTION', current_tuple=(g, ell, k, R),
                    brute_runner=None, brute_digits=[], brute_pairs=[], brute_values=None, replay_capture=[])
        observer = AlignedTwoBitObserver()
        LIVE['observer'] = observer
        first = len(CALLS)
        requests = [observer.two_negative(g, ell, k, R, r) for r in range(R)]
        values = [request['value'] for request in requests]
        certificate = observer.export_certificate()
        production_interval = interval('production', repr((g, ell, k, R)), first)
        assert not certificate['actual_integer_evidence']['window_weight_queries']
        LIVE['stage'] = 'ONE_PASS_TYPED_PAIR_COMPARATOR'
        first = len(CALLS)
        expected, brute = typed_pair_histogram(g, ell, k, R)
        brute_interval = interval('typed_pair_comparator', repr((g, ell, k, R)), first)
        assert values == expected
        LIVE['stage'] = 'POSITIVE_FRESH_REPLAY'
        first = len(CALLS)
        verification = verify_aligned_certificate(json.loads(json.dumps(certificate)), replay_capture=LIVE['replay_capture'])
        replay_interval = interval('positive_replay', repr((g, ell, k, R)), first)
        output['cases'].append({'inputs': {'g': g, 'ell': ell, 'k': k, 'R': R}, 'values': values,
            'all_residues_equal': True, 'certificate': certificate, 'typed_enumeration': brute,
            'verification': verification,
            'production_cost': cost(certificate['actual_integer_evidence']),
            'typed_enumeration_cost': cost(brute['actual_integer_evidence']),
            'positive_replay_cost': cost(verification['replay_certificate']['actual_integer_evidence']),
            'call_intervals': [production_interval, brute_interval, replay_interval]})
        certificates.append(certificate)
        print(json.dumps({'stage': 'CASE_COMPLETE', 'tuple': (g, ell, k, R), 'values': values,
                          'typed_pairs': len(brute['pair_observations'])}), flush=True)
    output['coverage'] = coverage_checks(certificates)
    assert sum(len(c['typed_enumeration']['pair_observations']) for c in output['cases']) == 720
    LIVE['stage'] = 'INPUT_REJECTIONS'
    output['input_rejections'] = input_rejections()
    LIVE['stage'] = 'CERTIFICATE_TAMPER_REJECTIONS'
    output['negative_checks'] = negative_checks(certificates)
    assert sources == {name: sha(ROOT/name) for name in source_names}
    assert sha(guard_path) == LIVE['guard']['sha256'] and sha(PROOF) == PROOF_PIN
    assert sha(DIRECT/'direct_signed_gap.py') == DIRECT_PIN
    frontier = 0
    for row in LIVE['call_intervals']:
        assert row['start'] == frontier and row['stop'] >= row['start']
        frontier = row['stop']
    assert frontier == len(CALLS)
    costs = {
        'production': aggregate_cost(c['actual_integer_evidence'] for c in certificates),
        'typed_pair_comparator': aggregate_cost(c['typed_enumeration']['actual_integer_evidence'] for c in output['cases']),
        'positive_replay': aggregate_cost(c['verification']['replay_certificate']['actual_integer_evidence'] for c in output['cases']),
        'paid_input_rejection': aggregate_cost(r['incomplete_receipt']['actual_integer_evidence'] for r in output['input_rejections'] if 'incomplete_receipt' in r),
        'negative_replay': aggregate_cost(c['actual_integer_evidence'] for r in output['negative_checks'] for c in r['actual_replay_certificates'])}
    native_by_category = {}
    for row in LIVE['call_intervals']:
        native_by_category[row['category']] = native_by_category.get(row['category'], 0)+row['stop']-row['start']
    assert sum(native_by_category.values()) == len(CALLS)
    output.update(status='PASS', cost_categories=costs, native_calls_by_category=native_by_category,
                  call_intervals=deepcopy(LIVE['call_intervals']), actual_core_calls=deepcopy(CALLS),
                  actual_core_call_count=len(CALLS), elapsed_seconds_before_serialization=time.perf_counter()-started)
    LIVE['stage'] = 'SERIALIZE_SUCCESS'
    raw = json.dumps(output, sort_keys=True, separators=(',', ':')).encode()+b'\n'
    with TARGETS[0].open('xb') as stream:
        stream.write(gzip.compress(raw, compresslevel=6, mtime=0))
    summary = {'status': 'PASS', 'source_sha256': sources, 'cases': 6, 'residue_equalities': 36,
        'typed_pair_observations': 720, 'input_rejections': len(output['input_rejections']),
        'incomplete_observer_reuse_rejections': sum('reuse_rejection' in r for r in output['input_rejections']),
        'negative_checks': len(output['negative_checks']), 'coverage': output['coverage'],
        'cost_categories': costs, 'actual_core_call_count': len(CALLS),
        'native_calls_by_category': native_by_category, 'call_intervals': LIVE['call_intervals'],
        'values': [c['values'] for c in output['cases']],
        'single_progression_calls': sum(r['single_progression_calls'] for c in certificates for r in c['requests']),
        'top_level_table_calls': sum(r['top_level_table_calls'] for c in certificates for r in c['requests']),
        'per_case': [{'inputs': c['inputs'], 'production': c['production_cost'],
                      'typed_comparator': c['typed_enumeration_cost'], 'positive_replay': c['positive_replay_cost']} for c in output['cases']],
        'raw_bytes': len(raw), 'gzip_bytes': TARGETS[0].stat().st_size,
        'payload_sha256': hashlib.sha256(raw).hexdigest(), 'artifact_sha256': sha(TARGETS[0]),
        'elapsed_seconds_before_serialization': output['elapsed_seconds_before_serialization'],
        'comparison_is_timing_benchmark': False, 'full_gram_integration_performed': False,
        'order_discovery_performed': False, 'quantum_phase_propagation_performed': False,
        'host_cost_scope': 'arithmetic wiring/bit-length counters only; serialization/indexing bookkeeping excluded'}
    with TARGETS[1].open('x', encoding='utf-8') as stream:
        stream.write(json.dumps(summary, indent=2)+'\n')
    LIVE['stage'] = 'COMPLETE'
    print(json.dumps(summary), flush=True)


def preserve_failure(error):
    observer = LIVE.get('observer')
    failure = {'status': 'FAILED_EXECUTION', 'stage': LIVE['stage'],
        'error_type': type(error).__name__, 'error': str(error), 'traceback': traceback.format_exc(),
        'source_sha256': {name: sha(ROOT/name) for name in ('aligned_two_bit.py', 'check_aligned_two_bit.py', 'DESIGN.md')},
        'startup_guard': LIVE['guard'], 'current_tuple': LIVE.get('current_tuple'),
        'completed_output': LIVE['output'],
        'current_observer': None if observer is None else observer.incomplete_snapshot(),
        'current_brute_evidence': unfinished_runner(LIVE['brute_runner']),
        'current_brute_digits': LIVE['brute_digits'], 'current_brute_pairs': LIVE['brute_pairs'],
        'current_brute_values': LIVE['brute_values'], 'current_replay_capture': LIVE['replay_capture'],
        'completed_tamper_attempts': LIVE['tamper_attempts'], 'current_tamper': LIVE['current_tamper'],
        'completed_input_attempts': LIVE['input_attempts'], 'current_input': LIVE['current_input'],
        'call_intervals': LIVE['call_intervals'], 'actual_core_calls': CALLS,
        'scope': 'incomplete retained typed work; no mathematical admission'}
    raw = json.dumps(failure, sort_keys=True, separators=(',', ':')).encode()+b'\n'
    with TARGETS[2].open('xb') as stream:
        stream.write(gzip.compress(raw, compresslevel=6, mtime=0))
    print(json.dumps({'status': 'FAILED_EXECUTION', 'stage': LIVE['stage'],
                     'path': str(TARGETS[2]), 'payload_sha256': hashlib.sha256(raw).hexdigest()}), flush=True)


if __name__ == '__main__':
    # No scientific operation precedes this rejection of existing evidence.
    if any(path.exists() for path in TARGETS):
        raise ValueError('existing success or failure evidence; refusing another run')
    try:
        main()
    except BaseException as error:
        preserve_failure(error)
        raise
