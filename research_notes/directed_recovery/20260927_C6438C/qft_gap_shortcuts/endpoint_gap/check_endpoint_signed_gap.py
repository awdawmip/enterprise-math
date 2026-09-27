"""Declared 31-residue endpoint run; no rerun of historical comparators.

Do not execute until this stage has its own actual startup guard and review.
"""
from copy import deepcopy
from pathlib import Path
import gzip
import hashlib
import json
import time
import traceback

from endpoint_signed_gap import (EndpointSignedGapObserver, verify_endpoint_certificate,
    FROZEN, ONE_WINDOW_PIN, BASELINE_PIN, ENDPOINT_PROOF_PIN, sha)
from stage45.brc_loop_recheck import CALLS

ROOT = Path(__file__).resolve().parent
CASES = ((1, 0, 3), (2, 0, 3), (2, 1, 3), (3, 0, 6), (3, 1, 3),
         (3, 2, 2), (4, 1, 7), (4, 2, 1), (5, 4, 3))
BRANCHES = ('highest_bit', 'lowest_odd_modulus', 'highest_bit', 'lowest_even_modulus',
            'interior_one_window', 'highest_bit', 'interior_one_window',
            'interior_one_window', 'highest_bit')
HISTORY_ARTIFACT = 'ONE_WINDOW_RESULTS.json.gz'
HISTORY_ARTIFACT_SHA = 'd465513608449d40b081a6ae62acff51f75ef5990f7bc911cec632a5b705e3de'
HISTORY_PAYLOAD_SHA = '37ec0d4b7939a70d9157239bfebec7c88a387ff6a2f046a2701f87641d5d78f9'
LIVE = {'stage': 'IMPORTED_NOT_STARTED', 'guard': None, 'output': None, 'observer': None,
        'replay_capture': [], 'tamper_attempts': [], 'current_tamper': None}


def read_history():
    compressed = (FROZEN/HISTORY_ARTIFACT).read_bytes()
    assert hashlib.sha256(compressed).hexdigest() == HISTORY_ARTIFACT_SHA
    raw = gzip.decompress(compressed)
    assert hashlib.sha256(raw).hexdigest() == HISTORY_PAYLOAD_SHA
    evidence = json.loads(raw)
    assert evidence['status'] == 'PASS'
    assert evidence['source_sha256'] == {
        'one_window_signed_gap.py': ONE_WINDOW_PIN,
        'check_one_window_signed_gap.py': '6594ebf9495dfabf1ce2878f4a9bc5cde80d45d0747e92d71e1e27e096e1a87e'}
    assert evidence['baseline']['artifact_sha256'] == '2b7ff5fe1cd62fbabe3f48fbaf157aeccdc6614f46a5c6d284edff3a412dbc9b'
    assert evidence['baseline']['payload_sha256'] == '76d1087ef58144303b624c2935a045eb15dcd9264f32dd1c09378431e9663110'
    assert evidence['baseline']['whole_payload_read_and_hash_checked'] is True
    assert len(evidence['cases']) == len(CASES)
    for case, (g, k, R) in zip(evidence['cases'], CASES):
        assert case['inputs'] == {'g': g, 'k': k, 'R': R}
        assert len(case['values']) == R and case['all_residues_equal'] is True
        assert case['verification']['verified'] is True
        assert case['values'] == case['baseline_reference']['values']
        assert case['certificate']['source_sha256'] == ONE_WINDOW_PIN
        assert case['certificate']['baseline_helper_source_sha256'] == BASELINE_PIN
    return evidence


def negative_checks(certificates):
    attempts = []
    LIVE['tamper_attempts'] = attempts
    changes = (
        ('wrong_branch', 0, lambda c: c['requests'][0].__setitem__('branch', 'lowest_odd_modulus')),
        ('wrong_half_residue', 1, lambda c: c['requests'][1]['half_residue'].__setitem__('value', 0)),
        ('wrong_parity_sign', 3, lambda c: c['requests'][1].__setitem__('sign', 1)),
        ('altered_interval', 0, lambda c: c['requests'][0]['interval_receipts'][0].__setitem__('value', 999)),
        ('boolean_input', 0, lambda c: c['requests'][0]['inputs'].__setitem__('g', True)),
        ('wrong_source', 0, lambda c: c.__setitem__('source_sha256', '0'*64)),
        ('altered_fallback', 4, lambda c: c['requests'][0]['frozen_one_window_request']['weights'].__setitem__('J_zero', 999)),
        ('wrong_denominator', 0, lambda c: c['requests'][0].__setitem__('raw_denominator_exponent', 999)))
    for name, index, update in changes:
        forged = deepcopy(certificates[index])
        update(forged)
        capture = []
        LIVE['replay_capture'] = capture
        LIVE['current_tamper'] = {'name': name, 'source_case_index': index,
                                 'attempted_certificate': forged}
        try:
            verify_endpoint_certificate(forged, replay_capture=capture)
        except ValueError as error:
            attempts.append({'name': name, 'source_case_index': index,
                'attempted_certificate': forged, 'rejected': True, 'error': str(error),
                'actual_replay_certificates': capture})
        else:
            raise AssertionError('forged endpoint certificate accepted: '+name)
    LIVE['current_tamper'] = None
    return attempts


def input_rejections():
    observer = EndpointSignedGapObserver()
    LIVE['observer'] = observer
    inputs = ((True, 0, 3, 0, 1), (0, 0, 3, 0, 1), (2, -1, 3, 0, 1),
              (2, 2, 3, 0, 1), (2, 0, 0, 0, 1), (2, 0, 3, -1, 1),
              (2, 0, 3, 3, 1), (2, 0, 3, 0, 2))
    records = []
    before_calls = len(CALLS)
    for g, k, R, r, stride in inputs:
        try:
            observer.one_negative(g, k, R, r, stride=stride)
        except ValueError as error:
            records.append({'inputs': {'g': g, 'k': k, 'R': R, 'r': r, 'stride': stride},
                            'rejected': True, 'error': str(error)})
        else:
            raise AssertionError('invalid endpoint input accepted')
    assert not observer.runner.arithmetic.operations and len(CALLS) == before_calls
    return records


def main():
    started = time.perf_counter()
    LIVE['stage'] = 'CHECK_STARTUP_GUARD'
    guard_path = ROOT.parent/'STARTUP_GUARD.json'
    guard = json.loads(guard_path.read_text(encoding='utf-8'))
    assert guard.get('activity_allowed') is True and guard.get('persistence_allowed') is True
    assert guard.get('activity_id') == 'RA-CAAAC604CB513AEA8BBC1DFC'
    assert guard.get('boundary') == 'startup' and guard.get('mode') == 'TASK_RESEARCH'
    assert guard.get('sync_debt_events') == []
    LIVE['guard'] = {'sha256': sha(guard_path), 'receipt': guard}
    targets = [ROOT/'ENDPOINT_RESULTS.json.gz', ROOT/'ENDPOINT_SUMMARY.json']
    prior_artifacts = [*targets, ROOT/'ENDPOINT_FAILED_EXECUTION.json.gz']
    assert not any(path.exists() for path in prior_artifacts), 'do not restart over existing success or failure evidence'
    names = ('endpoint_signed_gap.py', 'check_endpoint_signed_gap.py')
    sources = {name: sha(ROOT/name) for name in names}
    assert sha(ROOT.parent/'ENDPOINT_IDENTITIES.md') == ENDPOINT_PROOF_PIN
    LIVE['stage'] = 'READ_FROZEN_HISTORY'
    history = read_history()
    output = {'status': 'RUNNING', 'source_sha256': sources, 'startup_guard': LIVE['guard'],
        'endpoint_proof_sha256': ENDPOINT_PROOF_PIN,
        'history': {'artifact': HISTORY_ARTIFACT, 'artifact_sha256': HISTORY_ARTIFACT_SHA,
            'payload_sha256': HISTORY_PAYLOAD_SHA, 'whole_payload_read_and_hash_checked': True,
            'source_commit': '56b191519b036c6890cae328c3b3812fbc1debb7',
            'one_window_reexecuted': False, 'three_window_or_exhaustive_reexecuted': False},
        'scope': 'stride-one signed integer observer; 31 historical residues; no new propagator or full Gram integration',
        'cases': []}
    LIVE['output'] = output
    output['input_rejections'] = input_rejections()
    new_digits = old_digits = replay_digits = 0
    certificates = []
    for index, (g, k, R) in enumerate(CASES):
        LIVE.update(stage='FRESH_ENDPOINT_COUNTS', current_tuple=(g, k, R), replay_capture=[])
        observer = EndpointSignedGapObserver()
        LIVE['observer'] = observer
        requests = [observer.one_negative(g, k, R, r) for r in range(R)]
        values = [request['value'] for request in requests]
        prior = history['cases'][index]
        assert values == prior['values']
        assert all(request['branch'] == BRANCHES[index] for request in requests)
        certificate = observer.export_certificate()
        if BRANCHES[index] != 'interior_one_window':
            assert not certificate['actual_integer_evidence']['window_weight_queries']
            assert not certificate['actual_integer_evidence']['moment_nodes']
        LIVE['stage'] = 'FRESH_CERTIFICATE_REPLAY'
        verification = verify_endpoint_certificate(json.loads(json.dumps(certificate)),
                                                    replay_capture=LIVE['replay_capture'])
        actual_stats = certificate['actual_integer_evidence']['arithmetic_stats']
        prior_stats = prior['certificate']['actual_integer_evidence']['arithmetic_stats']
        new_digits += actual_stats['adder_digit_replays']
        old_digits += prior_stats['adder_digit_replays']
        replay_digits += verification['replay_arithmetic_stats']['adder_digit_replays']
        output['cases'].append({'inputs': {'g': g, 'k': k, 'R': R}, 'branch': BRANCHES[index],
            'values': values, 'all_residues_equal': True, 'certificate': certificate,
            'verification': verification,
            'history_reference': {'case_index': index, 'values': prior['values'],
                'certificate_pointer': f'cases/{index}/certificate',
                'recorded_one_window_production_arithmetic_stats': prior_stats,
                'recorded_three_window_reference': prior['baseline_reference']},
            'new_production_arithmetic_stats': actual_stats})
        certificates.append(certificate)
        print(json.dumps({'stage': 'CASE_COMPLETE', 'tuple': (g, k, R), 'branch': BRANCHES[index],
            'values': values, 'fresh_digits': actual_stats['adder_digit_replays'],
            'historical_one_window_digits': prior_stats['adder_digit_replays']}), flush=True)
    assert output['cases'][0]['values'][1] == -1
    assert output['cases'][3]['values'][1] == -11
    assert output['cases'][7]['values'] == [0]
    LIVE['stage'] = 'BRANCH_TAMPER_REJECTIONS'
    output['negative_checks'] = negative_checks(certificates)
    negative_digits = sum(c['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays']
        for row in output['negative_checks'] for c in row['actual_replay_certificates'])
    assert sources == {name: sha(ROOT/name) for name in names}
    assert sha(guard_path) == LIVE['guard']['sha256']
    assert sha(FROZEN/HISTORY_ARTIFACT) == HISTORY_ARTIFACT_SHA
    output.update(status='PASS', actual_core_calls=deepcopy(CALLS), actual_core_call_count=len(CALLS),
                  elapsed_seconds_before_serialization=time.perf_counter()-started)
    LIVE['stage'] = 'SERIALIZE_SUCCESS'
    raw = json.dumps(output, sort_keys=True, separators=(',', ':')).encode()+b'\n'
    with targets[0].open('xb') as stream:
        stream.write(gzip.compress(raw, compresslevel=6, mtime=0))
    summary = {'status': 'PASS', 'source_sha256': sources, 'cases': len(CASES),
        'residue_equalities': sum(len(case['values']) for case in output['cases']),
        'branch_counts': {branch: sum(len(case['values']) for case in output['cases'] if case['branch'] == branch)
                          for branch in dict.fromkeys(BRANCHES)},
        'input_rejections': len(output['input_rejections']),
        'negative_checks': len(output['negative_checks']), 'actual_core_call_count': len(CALLS),
        'fresh_production_adder_digit_replays': new_digits,
        'historical_one_window_production_adder_digit_replays': old_digits,
        'positive_replay_adder_digit_replays': replay_digits,
        'negative_replay_adder_digit_replays': negative_digits,
        'per_case': [{'inputs': case['inputs'], 'branch': case['branch'], 'values': case['values'],
            'fresh_digits': case['new_production_arithmetic_stats']['adder_digit_replays'],
            'historical_digits': case['history_reference']['recorded_one_window_production_arithmetic_stats']['adder_digit_replays']}
            for case in output['cases']],
        'historical_science_reexecuted': False, 'comparison_is_timing_benchmark': False,
        'quantum_phase_propagation_performed': False, 'order_discovery_performed': False,
        'full_gram_integration_performed': False,
        'boundary_coverage': 'g=1 highest priority, lowest odd/even, highest even, negative counts; R=1 is an interior case only',
        'elapsed_seconds_before_serialization': output['elapsed_seconds_before_serialization'],
        'raw_bytes': len(raw), 'gzip_bytes': targets[0].stat().st_size,
        'payload_sha256': hashlib.sha256(raw).hexdigest(), 'artifact_sha256': sha(targets[0])}
    with targets[1].open('x', encoding='utf-8') as stream:
        stream.write(json.dumps(summary, indent=2)+'\n')
    LIVE['stage'] = 'COMPLETE'
    print(json.dumps(summary))


def preserve_failure(error):
    observer = LIVE.get('observer')
    failure = {'status': 'FAILED_EXECUTION', 'stage': LIVE['stage'],
        'error_type': type(error).__name__, 'error': str(error), 'traceback': traceback.format_exc(),
        'source_sha256': {name: sha(ROOT/name) for name in ('endpoint_signed_gap.py', 'check_endpoint_signed_gap.py')},
        'startup_guard': LIVE['guard'], 'current_tuple': LIVE.get('current_tuple'),
        'completed_output': LIVE['output'],
        'current_observer': None if observer is None else observer.incomplete_snapshot(),
        'current_replay_capture': LIVE['replay_capture'], 'actual_core_calls': CALLS,
        'completed_tamper_attempts': LIVE['tamper_attempts'], 'current_tamper': LIVE['current_tamper'],
        'scope': 'incomplete available typed integer work; not admitted'}
    raw = json.dumps(failure, sort_keys=True, separators=(',', ':')).encode()+b'\n'
    target = ROOT/'ENDPOINT_FAILED_EXECUTION.json.gz'
    with target.open('xb') as stream:
        stream.write(gzip.compress(raw, compresslevel=6, mtime=0))
    print(json.dumps({'status': 'FAILED_EXECUTION', 'stage': LIVE['stage'],
                     'path': str(target), 'payload_sha256': hashlib.sha256(raw).hexdigest()}), flush=True)


if __name__ == '__main__':
    try:
        main()
    except BaseException as error:
        preserve_failure(error)
        raise
