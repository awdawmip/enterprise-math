"""Declared hybrid-only 31-value check; compile only until new guard/authorization."""
from copy import deepcopy
from pathlib import Path
from datetime import datetime, timezone
import gzip
import hashlib
import json
import sys
import time
import traceback

from hybrid_signed_gap import (HybridSignedGapObserver, verify_hybrid_certificate,
    runner_evidence, strict_json, sha, DESIGN_PIN, DIRECT_DIR, DIRECT_PIN,
    ENDPOINT_PIN, DEPENDENCY_PINS)
from stage45.brc_loop_recheck import CALLS

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parent
CASES = ((1, 0, 3), (2, 0, 3), (2, 1, 3), (3, 0, 6), (3, 1, 3),
         (3, 2, 2), (4, 1, 7), (4, 2, 1), (5, 4, 3))
HISTORY_GZIP_SHA = '3ac0ebc17112afb9f068e39c1ebb91afd8f6e3f6aeb3d6cd46044d0733b26354'
HISTORY_RAW_SHA = '48780f175bc4bcf673345ee8c0b9e0240cc1c2a0e166037720c5fc06b8483157'
SOURCE_NAMES = ('hybrid_signed_gap.py', 'check_hybrid_signed_gap.py')
OUTPUT_NAMES = ('HYBRID_RESULTS.json.gz', 'HYBRID_SUMMARY.json', 'HYBRID_FAILED_EXECUTION.json.gz')
LIVE = {'stage': 'IMPORTED_NOT_STARTED', 'guard': None, 'output': None,
        'observer': None, 'replay_capture': [], 'tamper_attempts': [],
        'current_tamper': None, 'current_tuple': None}


def read_history():
    data = (DIRECT_DIR/'DIRECT_RESULTS.json.gz').read_bytes()
    assert hashlib.sha256(data).hexdigest() == HISTORY_GZIP_SHA
    raw = gzip.decompress(data)
    assert hashlib.sha256(raw).hexdigest() == HISTORY_RAW_SHA
    history = json.loads(raw)
    assert history['status'] == 'PASS'
    assert history['source_sha256'] == {
        'direct_signed_gap.py': DIRECT_PIN,
        'check_direct_signed_gap.py': 'be69a1937c9ab1e04ad4fe6f650c412c5cad5def247b2d40f97042b926e5ce6f'}
    assert len(history['cases']) == len(CASES)
    for case, (g, k, R) in zip(history['cases'], CASES):
        assert case['inputs'] == {'g': g, 'k': k, 'R': R}
        assert len(case['values']) == R and case['all_residues_equal'] is True
        assert case['verification']['verified'] is True
        assert case['certificate']['source_sha256'] == DIRECT_PIN
    return history


def cost(certificate):
    """Metadata aggregation only. Each actual runner appears exactly once."""
    result = {}
    for name, evidence in runner_evidence(certificate).items():
        result[name] = {'arithmetic_stats': deepcopy(evidence['arithmetic_stats']),
            'signed_operations': len(evidence['signed_operations']),
            'moment_nodes': len(evidence['moment_nodes']),
            'moment_stats': deepcopy(evidence['stats']),
            'window_queries': len(evidence['window_weight_queries'])}
    stats_keys = tuple(result['routing']['arithmetic_stats'])
    result['arithmetic_totals'] = {
        key: sum(result[name]['arithmetic_stats'][key] for name in ('routing', 'endpoint', 'direct'))
        for key in stats_keys}
    return result


def validate_routing(certificate):
    running = 0
    seen = {'endpoint': [], 'direct': []}
    counts = {'endpoint': 0, 'interior_direct': 0, 'interior_divisible_zero': 0}
    for req in certificate['requests']:
        g, k = req['inputs']['g'], req['inputs']['k']
        assert req['routing_operations_start'] == running
        running = req['routing_operations_stop']
        counts[req['branch']] += 1
        if k == g-1 or k == 0:
            assert req['branch'] == 'endpoint' and req['divisibility'] is None
            assert req['routing_operations_start'] == req['routing_operations_stop']
        else:
            proof = req['divisibility']
            assert proof['R'] == req['inputs']['R']
            operation = certificate['routing_integer_evidence']['signed_operations'][
                proof['division_signed_operation_index']]
            assert operation['operation'] == 'signed_euclidean_division'
            assert list(operation['inputs']) == [proof['U'], proof['R']]
            assert list(operation['result']) == [proof['quotient'], proof['remainder']]
            if proof['remainder'] == 0:
                assert req['branch'] == 'interior_divisible_zero'
                assert req['value'] == 0 and req['nested_request'] is None
                zero = certificate['routing_integer_evidence']['signed_operations'][
                    req['zero_proof']['zero_signed_operation_index']]
                assert zero['operation'] == 'signed_add' and zero['result'] == 0
                assert list(zero['inputs']) == [proof['U'], -proof['U']]
            else:
                assert req['branch'] == 'interior_direct' and req['zero_proof'] is None
        name = req['nested_kind']
        if name is not None:
            nested = certificate[name+'_certificate']['requests']
            index = req['nested_request_index']
            assert index == len(seen[name])
            assert strict_json(req['nested_request']) == strict_json(nested[index])
            assert req['value'] == nested[index]['value']
            seen[name].append(index)
    assert running == len(certificate['routing_integer_evidence']['signed_operations'])
    for name in seen:
        assert len(seen[name]) == len(certificate[name+'_certificate']['requests'])
    # All runners preserve the same actual shared primitive columns, not three observations.
    sources = [e['native_source'] for e in runner_evidence(certificate).values()]
    assert all(strict_json(item) == strict_json(sources[0]) for item in sources)
    return counts


def input_rejections():
    observer = HybridSignedGapObserver()
    LIVE['observer'] = observer
    bad = ((True, 0, 3, 0, 1), (0, 0, 3, 0, 1), (2, -1, 3, 0, 1),
           (2, 2, 3, 0, 1), (2, 0, 0, 0, 1), (2, 0, 3, -1, 1),
           (2, 0, 3, 3, 1), (2, 0, 3, 0, 2))
    records = []
    calls_before = len(CALLS)
    for g, k, R, r, stride in bad:
        try:
            observer.one_negative(g, k, R, r, stride=stride)
        except ValueError as error:
            records.append({'inputs': {'g': g, 'k': k, 'R': R, 'r': r, 'stride': stride},
                            'rejected': True, 'error': str(error)})
        else:
            raise AssertionError('invalid hybrid input accepted')
    snapshot = observer.incomplete_snapshot()
    assert all(not e['arithmetic_operations'] for e in runner_evidence(snapshot).values())
    assert len(CALLS) == calls_before
    return records


def negative_checks(certificates):
    attempts = []
    LIVE['tamper_attempts'] = attempts
    mutations = (
        ('wrong_schema', 0, lambda c: c.__setitem__('schema', 'UNRELATED')),
        ('wrong_source', 0, lambda c: c.__setitem__('source_sha256', '0'*64)),
        ('wrong_dependency', 0, lambda c: c['dependency_sha256'].__setitem__('direct_signed_gap.py', '0'*64)),
        ('boolean_input', 0, lambda c: c['requests'][0]['inputs'].__setitem__('g', True)),
        ('false_direct_branch', 7, lambda c: c['requests'][0].__setitem__('branch', 'interior_direct')),
        ('wrong_zero_quotient', 7, lambda c: c['requests'][0]['divisibility'].__setitem__('quotient', 999)),
        ('wrong_zero_remainder', 7, lambda c: c['requests'][0]['divisibility'].__setitem__('remainder', 1)),
        ('wrong_zero_U', 7, lambda c: c['requests'][0]['divisibility'].__setitem__('U', 999)),
        ('missing_zero_proof', 7, lambda c: c['requests'][0].__setitem__('zero_proof', None)),
        ('boolean_zero_output', 7, lambda c: c['requests'][0].__setitem__('value', False)),
        ('wrong_zero_subtraction', 7, lambda c: c['routing_integer_evidence']['signed_operations'][
            c['requests'][0]['zero_proof']['zero_signed_operation_index']].__setitem__('result', 999)),
        ('wrong_routing_division', 7, lambda c: c['routing_integer_evidence']['signed_operations'][
            c['requests'][0]['divisibility']['division_signed_operation_index']].__setitem__('result', [999, 0])),
        ('wrong_endpoint_nested_value', 0, lambda c: c['endpoint_certificate']['requests'][0].__setitem__('value', 999)),
        ('wrong_direct_nested_value', 4, lambda c: c['direct_certificate']['requests'][0].__setitem__('value', 999)),
        ('wrong_nested_provenance', 0, lambda c: c['endpoint_certificate'].__setitem__('source_sha256', '0'*64)))
    for name, index, mutate in mutations:
        forged = deepcopy(certificates[index])
        mutate(forged)
        capture = []
        LIVE.update(replay_capture=capture,
                    current_tamper={'name': name, 'case_index': index, 'attempted_certificate': forged})
        before = len(CALLS)
        try:
            verify_hybrid_certificate(forged, replay_capture=capture)
        except ValueError as error:
            attempts.append({'name': name, 'case_index': index, 'attempted_certificate': forged,
                'rejected': True, 'error': str(error), 'actual_replay_certificates': capture,
                'native_core_calls_delta': len(CALLS)-before,
                'replay_costs': [cost(item) for item in capture]})
        else:
            raise AssertionError('forged hybrid certificate accepted: '+name)
    LIVE['current_tamper'] = None
    return attempts


def main():
    started = time.perf_counter()
    started_utc = datetime.now(timezone.utc).isoformat()
    LIVE['stage'] = 'CHECK_STARTUP_GUARD'
    guard_path = ROOT.parent/'STARTUP_GUARD.json'
    guard = json.loads(guard_path.read_text(encoding='utf-8'))
    assert guard.get('activity_allowed') is True and guard.get('persistence_allowed') is True
    assert guard.get('activity_id') == 'RA-CAAAC604CB513AEA8BBC1DFC'
    assert guard.get('boundary') == 'startup' and guard.get('mode') == 'TASK_RESEARCH'
    assert guard.get('sync_debt_events') == []
    LIVE['guard'] = {'sha256': sha(guard_path), 'receipt': guard}
    sources = {name: sha(ROOT/name) for name in SOURCE_NAMES}
    assert sha(ROOT.parent/'DESIGN.md') == DESIGN_PIN
    LIVE['stage'] = 'READ_FROZEN_DIRECT_HISTORY'
    history = read_history()
    output = {'status': 'RUNNING', 'source_sha256': sources,
        'dependency_sha256': DEPENDENCY_PINS, 'startup_guard': LIVE['guard'],
        'started_utc': started_utc,
        'history': {'artifact': str(DIRECT_DIR/'DIRECT_RESULTS.json.gz'),
            'artifact_sha256': HISTORY_GZIP_SHA, 'payload_sha256': HISTORY_RAW_SHA,
            'whole_payload_read_and_hash_checked': True, 'historical_science_reexecuted': False},
        'scope': 'structural scalar dispatcher only; no aligned route, two-bit query or full Gram propagation',
        'cases': []}
    LIVE['output'] = output
    output['input_rejections'] = input_rejections()
    certificates = []
    total_branches = {'endpoint': 0, 'interior_direct': 0, 'interior_divisible_zero': 0}
    for index, (g, k, R) in enumerate(CASES):
        LIVE.update(stage='HYBRID_PRODUCTION', current_tuple=(g, k, R), replay_capture=[])
        observer = HybridSignedGapObserver()
        LIVE['observer'] = observer
        before = len(CALLS)
        records = [observer.one_negative(g, k, R, r) for r in range(R)]
        values = [record['value'] for record in records]
        prior = history['cases'][index]
        assert values == prior['values']
        certificate = observer.export_certificate()
        production_calls = len(CALLS)-before
        branch_counts = validate_routing(certificate)
        for name, count in branch_counts.items():
            total_branches[name] += count
        LIVE['stage'] = 'HYBRID_FRESH_POSITIVE_REPLAY'
        before = len(CALLS)
        verification = verify_hybrid_certificate(json.loads(json.dumps(certificate)),
                                                 replay_capture=LIVE['replay_capture'])
        assert len(LIVE['replay_capture']) == 1
        replay_calls = len(CALLS)-before
        production_cost = cost(certificate)
        output['cases'].append({'inputs': {'g': g, 'k': k, 'R': R},
            'values': values, 'all_residues_equal': True, 'certificate': certificate,
            'verification': verification, 'branch_counts': branch_counts,
            'production_cost': production_cost, 'positive_replay_cost': cost(verification['replay_certificate']),
            'production_native_core_calls_delta': production_calls,
            'replay_native_core_calls_delta': replay_calls,
            'history_reference': {'case_index': index, 'values': prior['values'],
                'certificate_pointer': f'cases/{index}/certificate',
                'recorded_pure_direct_stats': prior['new_production_arithmetic_stats']}})
        certificates.append(certificate)
        print(json.dumps({'stage': 'CASE_COMPLETE', 'tuple': (g, k, R), 'values': values,
            'branches': branch_counts, 'hybrid_digits': production_cost['arithmetic_totals']['adder_digit_replays'],
            'historical_direct_digits': prior['new_production_arithmetic_stats']['adder_digit_replays']}), flush=True)
    assert all(total_branches[name] > 0 for name in total_branches)
    assert output['cases'][7]['values'] == [0]
    LIVE['stage'] = 'HYBRID_CERTIFICATE_NEGATIVES'
    output['negative_checks'] = negative_checks(certificates)
    assert sources == {name: sha(ROOT/name) for name in SOURCE_NAMES}
    assert sha(guard_path) == LIVE['guard']['sha256']
    assert sha(DIRECT_DIR/'DIRECT_RESULTS.json.gz') == HISTORY_GZIP_SHA
    # A fresh process shares one actual full-adder column observation globally.
    assert len(CALLS) == 1
    output.update(status='PASS', branch_counts=total_branches,
        actual_core_calls=deepcopy(CALLS), actual_core_call_count=len(CALLS),
        elapsed_seconds_before_serialization=time.perf_counter()-started,
        completed_utc_before_serialization=datetime.now(timezone.utc).isoformat())
    LIVE['stage'] = 'SERIALIZE_SUCCESS'
    raw = json.dumps(output, sort_keys=True, separators=(',', ':')).encode()+b'\n'
    destination = ROOT/OUTPUT_NAMES[0]
    with destination.open('xb') as stream:
        stream.write(gzip.compress(raw, compresslevel=6, mtime=0))
    production = [case['production_cost']['arithmetic_totals'] for case in output['cases']]
    replay = [case['positive_replay_cost']['arithmetic_totals'] for case in output['cases']]
    negatives = [row['arithmetic_totals'] for case in output['negative_checks'] for row in case['replay_costs']]
    summary = {'status': 'PASS', 'source_sha256': sources, 'cases': len(CASES),
        'residue_equalities': sum(len(case['values']) for case in output['cases']),
        'input_rejections': len(output['input_rejections']), 'negative_checks': len(output['negative_checks']),
        'paid_negative_replays': len(negatives), 'branch_counts': total_branches,
        'actual_core_call_count': len(CALLS),
        'production_totals': {key: sum(row[key] for row in production) for key in production[0]},
        'positive_replay_totals': {key: sum(row[key] for row in replay) for key in replay[0]},
        'negative_replay_totals': {key: sum(row[key] for row in negatives) for key in production[0]},
        'per_case': [{'inputs': c['inputs'], 'values': c['values'], 'branch_counts': c['branch_counts'],
            'routing_digits': c['production_cost']['routing']['arithmetic_stats']['adder_digit_replays'],
            'endpoint_digits': c['production_cost']['endpoint']['arithmetic_stats']['adder_digit_replays'],
            'direct_digits': c['production_cost']['direct']['arithmetic_stats']['adder_digit_replays'],
            'total_digits': c['production_cost']['arithmetic_totals']['adder_digit_replays'],
            'historical_direct_digits': c['history_reference']['recorded_pure_direct_stats']['adder_digit_replays']}
            for c in output['cases']],
        'historical_science_reexecuted': False, 'aligned_route_implemented': False,
        'two_bit_query_implemented': False, 'comparison_is_timing_benchmark': False,
        'quantum_phase_propagation_performed': False, 'order_discovery_performed': False,
        'full_gram_integration_performed': False,
        'elapsed_seconds_before_serialization': output['elapsed_seconds_before_serialization'],
        'raw_bytes': len(raw), 'gzip_bytes': destination.stat().st_size,
        'payload_sha256': hashlib.sha256(raw).hexdigest(), 'artifact_sha256': sha(destination)}
    with (ROOT/OUTPUT_NAMES[1]).open('x', encoding='utf-8') as stream:
        stream.write(json.dumps(summary, indent=2)+'\n')
    LIVE['stage'] = 'COMPLETE'
    print(json.dumps(summary), flush=True)


def preserve_failure(error):
    """Available metadata/arrays only; capture failures cannot erase global CALLS."""
    failure = {'status': 'FAILED_EXECUTION', 'stage': LIVE['stage'],
        'error_type': type(error).__name__, 'error': str(error), 'traceback': traceback.format_exc(),
        'actual_core_calls': deepcopy(CALLS), 'capture_errors': {},
        'scope': 'available constructed objects only; not arbitrary pre-import/constructor recovery'}
    fields = {'sources': lambda: {name: sha(ROOT/name) for name in SOURCE_NAMES},
        'startup_guard': lambda: LIVE['guard'], 'current_tuple': lambda: LIVE['current_tuple'],
        'completed_output': lambda: LIVE['output'],
        'current_observer': lambda: None if LIVE['observer'] is None else LIVE['observer'].incomplete_snapshot(),
        'current_replay_capture': lambda: LIVE['replay_capture'],
        'completed_tamper_attempts': lambda: LIVE['tamper_attempts'],
        'current_tamper': lambda: LIVE['current_tamper']}
    for name, capture in fields.items():
        try:
            # Freeze detached JSON so a malformed field is isolated before final serialization.
            failure[name] = json.loads(json.dumps(capture()))
        except BaseException as capture_error:
            failure['capture_errors'][name] = {'type': type(capture_error).__name__, 'error': str(capture_error)}
    raw = json.dumps(failure, sort_keys=True, separators=(',', ':')).encode()+b'\n'
    target = ROOT/OUTPUT_NAMES[2]
    with target.open('xb') as stream:
        stream.write(gzip.compress(raw, compresslevel=6, mtime=0))
    print(json.dumps({'status': 'FAILED_EXECUTION', 'stage': LIVE['stage'],
        'path': str(target), 'payload_sha256': hashlib.sha256(raw).hexdigest()}), flush=True)


if __name__ == '__main__':
    # A refused rerun does not create a new failure file next to old success evidence.
    if any((ROOT/name).exists() for name in OUTPUT_NAMES):
        raise FileExistsError('do not restart over existing hybrid success or failure evidence')
    try:
        main()
    except BaseException as error:
        preserve_failure(error)
        raise
