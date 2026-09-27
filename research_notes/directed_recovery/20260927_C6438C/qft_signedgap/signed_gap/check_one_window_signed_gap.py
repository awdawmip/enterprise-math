"""Bounded fresh one-window execution versus frozen three-window evidence.

The existing typed exhaustive comparison is read as historical evidence and
is not executed again. This is a digit-cost comparison, not a timing benchmark.
"""
from copy import deepcopy
from pathlib import Path
import gzip
import hashlib
import json
import time
import traceback

from one_window_signed_gap import OneWindowSignedGapObserver, verify_one_window_certificate
from signed_gap import sha
from stage45.brc_loop_recheck import CALLS

ROOT = Path(__file__).resolve().parent
CASES = ((1, 0, 3), (2, 0, 3), (2, 1, 3), (3, 0, 6), (3, 1, 3),
         (3, 2, 2), (4, 1, 7), (4, 2, 1), (5, 4, 3))
BASELINE_ARTIFACT = 'SIGNED_GAP_RESULTS.json.gz'
BASELINE_ARTIFACT_SHA = '2b7ff5fe1cd62fbabe3f48fbaf157aeccdc6614f46a5c6d284edff3a412dbc9b'
BASELINE_PAYLOAD_SHA = '76d1087ef58144303b624c2935a045eb15dcd9264f32dd1c09378431e9663110'
LIVE = {'stage': 'IMPORTED_NOT_STARTED', 'guard': None, 'output': None, 'observer': None,
        'replay_capture': [], 'tamper_attempts': [], 'current_tamper': None}


def read_baseline():
    compressed = (ROOT/BASELINE_ARTIFACT).read_bytes()
    assert hashlib.sha256(compressed).hexdigest() == BASELINE_ARTIFACT_SHA
    raw = gzip.decompress(compressed)
    assert hashlib.sha256(raw).hexdigest() == BASELINE_PAYLOAD_SHA
    evidence = json.loads(raw)
    assert evidence['status'] == 'PASS'
    assert evidence['source_sha256'] == {
        'signed_gap.py': '86ea28956fa7ac9c41fb38a8c63f4ba00b0377f3264b5a525c46c5335faff90a',
        'check_signed_gap.py': '83bd08d2345246754ab9da2453d84af2ef2b70ccf7546dd5d9efb2c8badf5eff'}
    assert len(evidence['cases']) == len(CASES)
    for case, (g, k, R) in zip(evidence['cases'], CASES):
        assert case['inputs'] == {'g': g, 'k': k, 'R': R}
        assert len(case['values']) == R and case['all_residues_equal'] is True
        assert case['verification']['verified'] is True
    return evidence


def negative_checks(certificate):
    attempts = []
    LIVE['tamper_attempts'] = attempts
    changes = (
        ('value', lambda c: c['requests'][0].__setitem__('value', 999)),
        ('window_weight', lambda c: c['requests'][0]['weights'].__setitem__('J_zero', 999)),
        ('interval_weight', lambda c: c['requests'][0]['weights'].__setitem__('total_unsigned', 999)),
        ('identity', lambda c: c.__setitem__('identity', 'K=3J-T')),
        ('boolean_input', lambda c: c['requests'][0]['inputs'].__setitem__('g', True)),
        ('source', lambda c: c.__setitem__('source_sha256', '0'*64)))
    for name, update in changes:
        forged = deepcopy(certificate)
        update(forged)
        capture = []
        LIVE['replay_capture'] = capture
        LIVE['current_tamper'] = {'name': name, 'attempted_certificate': forged}
        try:
            verify_one_window_certificate(forged, replay_capture=capture)
        except ValueError as error:
            attempts.append({'name': name, 'attempted_certificate': forged,
                'rejected': True, 'error': str(error), 'actual_replay_certificates': capture})
        else:
            raise AssertionError('forged one-window certificate accepted')
    return attempts


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
    targets = [ROOT/'ONE_WINDOW_RESULTS.json.gz', ROOT/'ONE_WINDOW_SUMMARY.json']
    assert not any(path.exists() for path in targets), 'do not overwrite existing evidence'
    names = ('one_window_signed_gap.py', 'check_one_window_signed_gap.py')
    sources = {name: sha(ROOT/name) for name in names}
    LIVE['stage'] = 'READ_FROZEN_BASELINE'
    baseline = read_baseline()
    output = {'status': 'RUNNING', 'source_sha256': sources, 'startup_guard': LIVE['guard'],
        'baseline': {'artifact': BASELINE_ARTIFACT, 'artifact_sha256': BASELINE_ARTIFACT_SHA,
                     'payload_sha256': BASELINE_PAYLOAD_SHA, 'whole_payload_read_and_hash_checked': True,
                     'reexecuted': False},
        'scope': 'V=1 one-window integer observer; historical value/trace comparison; no full Gram integration',
        'cases': []}
    LIVE['output'] = output
    first_certificate = None
    new_digits = old_digits = replay_digits = 0
    for index, (g, k, R) in enumerate(CASES):
        LIVE.update(stage='FRESH_ONE_WINDOW_COUNTS', current_tuple=(g, k, R), replay_capture=[])
        observer = OneWindowSignedGapObserver()
        LIVE['observer'] = observer
        values = [observer.one_negative(g, k, R, r)['value'] for r in range(R)]
        prior = baseline['cases'][index]
        assert values == prior['values']
        certificate = observer.export_certificate()
        LIVE['stage'] = 'FRESH_CERTIFICATE_REPLAY'
        verification = verify_one_window_certificate(json.loads(json.dumps(certificate)),
                                                       replay_capture=LIVE['replay_capture'])
        actual_stats = certificate['actual_integer_evidence']['arithmetic_stats']
        prior_stats = prior['certificate']['actual_integer_evidence']['arithmetic_stats']
        new_digits += actual_stats['adder_digit_replays']
        old_digits += prior_stats['adder_digit_replays']
        replay_digits += verification['replay_arithmetic_stats']['adder_digit_replays']
        output['cases'].append({'inputs': {'g': g, 'k': k, 'R': R}, 'values': values,
            'all_residues_equal': True, 'certificate': certificate, 'verification': verification,
            'baseline_reference': {'case_index': index, 'values': prior['values'],
                'certificate_pointer': f'cases/{index}/certificate',
                'typed_enumeration_pointer': f'cases/{index}/typed_enumeration',
                'recorded_production_arithmetic_stats': prior_stats,
                'recorded_pair_count': len(prior['typed_enumeration']['pair_observations'])},
            'new_production_arithmetic_stats': actual_stats})
        if first_certificate is None:
            first_certificate = certificate
        print(json.dumps({'stage': 'CASE_COMPLETE', 'tuple': (g, k, R), 'values': values,
            'fresh_digits': actual_stats['adder_digit_replays'],
            'recorded_baseline_digits': prior_stats['adder_digit_replays']}), flush=True)
    assert output['cases'][0]['values'][1] == -1
    assert output['cases'][7]['values'] == [0]
    LIVE['stage'] = 'NEW_FORMULA_TAMPER_REJECTIONS'
    output['negative_checks'] = negative_checks(first_certificate)
    negative_digits = sum(c['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays']
        for row in output['negative_checks'] for c in row['actual_replay_certificates'])
    assert sources == {name: sha(ROOT/name) for name in names}
    assert sha(guard_path) == LIVE['guard']['sha256']
    assert sha(ROOT/BASELINE_ARTIFACT) == BASELINE_ARTIFACT_SHA
    output.update(status='PASS', actual_core_calls=deepcopy(CALLS), actual_core_call_count=len(CALLS),
                  elapsed_seconds_before_serialization=time.perf_counter()-started)
    LIVE['stage'] = 'SERIALIZE_SUCCESS'
    raw = json.dumps(output, sort_keys=True, separators=(',', ':')).encode()+b'\n'
    targets[0].write_bytes(gzip.compress(raw, compresslevel=6, mtime=0))
    summary = {'status': 'PASS', 'source_sha256': sources, 'cases': len(CASES),
        'residue_equalities': sum(len(case['values']) for case in output['cases']),
        'negative_checks': len(output['negative_checks']), 'actual_core_call_count': len(CALLS),
        'fresh_production_adder_digit_replays': new_digits,
        'historical_three_window_production_adder_digit_replays': old_digits,
        'positive_replay_adder_digit_replays': replay_digits, 'negative_replay_adder_digit_replays': negative_digits,
        'per_case': [{'inputs': case['inputs'], 'values': case['values'],
            'fresh_digits': case['new_production_arithmetic_stats']['adder_digit_replays'],
            'historical_digits': case['baseline_reference']['recorded_production_arithmetic_stats']['adder_digit_replays']}
            for case in output['cases']],
        'baseline_reexecuted': False, 'comparison_is_timing_benchmark': False,
        'quantum_phase_propagation_performed': False, 'order_discovery_performed': False,
        'full_gram_integration_performed': False,
        'elapsed_seconds_before_serialization': output['elapsed_seconds_before_serialization'],
        'raw_bytes': len(raw), 'gzip_bytes': targets[0].stat().st_size,
        'payload_sha256': hashlib.sha256(raw).hexdigest(), 'artifact_sha256': sha(targets[0])}
    targets[1].write_text(json.dumps(summary, indent=2)+'\n', encoding='utf-8')
    LIVE['stage'] = 'COMPLETE'
    print(json.dumps(summary))


def preserve_failure(error):
    observer = LIVE.get('observer')
    failure = {'status': 'FAILED_EXECUTION', 'stage': LIVE['stage'],
        'error_type': type(error).__name__, 'error': str(error), 'traceback': traceback.format_exc(),
        'source_sha256': {name: sha(ROOT/name) for name in ('one_window_signed_gap.py', 'check_one_window_signed_gap.py')},
        'startup_guard': LIVE['guard'], 'current_tuple': LIVE.get('current_tuple'),
        'completed_output': LIVE['output'],
        'current_observer': None if observer is None else observer.incomplete_snapshot(),
        'current_replay_capture': LIVE['replay_capture'], 'actual_core_calls': CALLS,
        'completed_tamper_attempts': LIVE['tamper_attempts'], 'current_tamper': LIVE['current_tamper'],
        'scope': 'incomplete available typed integer work; not admitted'}
    raw = json.dumps(failure, sort_keys=True, separators=(',', ':')).encode()+b'\n'
    target = ROOT/'ONE_WINDOW_FAILED_EXECUTION.json.gz'
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
