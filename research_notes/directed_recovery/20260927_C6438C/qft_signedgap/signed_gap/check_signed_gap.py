"""Bounded actual typed comparison of three-floor signed-gap certificates."""
from copy import deepcopy
from pathlib import Path
import gzip
import hashlib
import json
import time
import traceback

from signed_gap import (SignedGapObserver, TypedFloorMoments, typed_two_power,
                        verify_certificate, sha)
from stage45.brc_loop_recheck import CALLS

ROOT = Path(__file__).resolve().parent
CASES = ((1, 0, 3), (2, 0, 3), (2, 1, 3), (3, 0, 6), (3, 1, 3),
         (3, 2, 2), (4, 1, 7), (4, 2, 1), (5, 4, 3))
LIVE = {'stage': 'IMPORTED_NOT_STARTED', 'output': None, 'observer': None,
        'brute_runner': None, 'brute_digits': [], 'brute_pairs': [],
        'brute_values': None, 'replay_capture': [], 'guard': None,
        'tamper_attempts': [], 'attempted_tamper': None}


def typed_pair_histogram(g, k, R):
    """Enumerate once per public tuple; every difference/residue/sum is typed."""
    runner = TypedFloorMoments()
    LIVE['brute_runner'] = runner
    length = typed_two_power(runner, g)
    U = typed_two_power(runner, k)
    digits, digit_rows = [], []
    LIVE['brute_digits'] = digit_rows
    for x in range(length):
        start = len(runner.signed_operations)
        quotient, low = runner.floor_div(x, U)
        _, bit = runner.floor_div(quotient, 2)
        assert bit in (0, 1)
        digits.append(bit)
        digit_rows.append({'label': x, 'quotient': quotient, 'low': low, 'negative_bit': bit,
                           'signed_operations_start': start,
                           'signed_operations_stop': len(runner.signed_operations)})
    values = [0 for _ in range(R)]
    pairs = []
    LIVE['brute_pairs'], LIVE['brute_values'] = pairs, values
    for x in range(length):
        for y in range(length):
            start = len(runner.signed_operations)
            difference = runner.sub(y, x)
            quotient, residue = runner.floor_div(difference, R)
            # Two already observed bit labels route the scalar sign; no host sum.
            sign = 1 if digits[x] == digits[y] else -1
            before = values[residue]
            after = runner.add(before, sign)
            values[residue] = after
            pairs.append({'x': x, 'y': y, 'difference': difference,
                          'quotient': quotient, 'residue': residue, 'sign': sign,
                          'bucket_before': before, 'bucket_after': after,
                          'signed_operations_start': start,
                          'signed_operations_stop': len(runner.signed_operations)})
    return values, {'digit_observations': digit_rows, 'pair_observations': pairs,
                    'actual_integer_evidence': runner.evidence()}


def rejection_checks():
    invalid = ((True, 0, 3, 0, 1), (1.0, 0, 3, 0, 1), ('1', 0, 3, 0, 1),
               (0, 0, 3, 0, 1), (-1, 0, 3, 0, 1), (2, -1, 3, 0, 1),
               (2, 2, 3, 0, 1), (2, 0, 0, 0, 1), (2, 0, 3, -1, 1),
               (2, 0, 3, 3, 1), (2, 0, 3, 0, 2), (2, False, 3, 0, 1),
               (2, 0, True, 0, 1), (2, 0, 3, False, 1), (2, 0, 3, 0, True))
    output = []
    for args in invalid:
        observer = SignedGapObserver()
        LIVE['observer'] = observer
        try:
            observer.one_negative(*args[:4], stride=args[4])
        except ValueError as error:
            assert not observer.runner.arithmetic.operations
            assert not observer.requests
            output.append({'inputs': args, 'rejected': True, 'error': str(error),
                           'typed_operations': 0})
        else:
            raise AssertionError('invalid input accepted')
    return output


def tamper_checks(original):
    attempts = []
    LIVE['tamper_attempts'] = attempts
    def typed_key_encoding(item):
        if type(item) is dict:
            return {'object_entries': [
                {'key_type': type(key).__name__, 'key': key, 'value': typed_key_encoding(value)}
                for key, value in item.items()]}
        if type(item) in (list, tuple):
            return [typed_key_encoding(child) for child in item]
        return item
    def retain(name, update):
        forged = deepcopy(original)
        update(forged)
        encoded = typed_key_encoding(forged)
        LIVE['attempted_tamper'] = {'name': name, 'typed_key_encoding': encoded}
        captured = []
        LIVE['replay_capture'] = captured
        try:
            verify_certificate(forged, replay_capture=captured)
        except ValueError as error:
            attempts.append({'name': name, 'rejected': True, 'error': str(error),
                'attempted_certificate_typed_key_encoding': encoded,
                'actual_replay_certificates': captured})
        else:
            raise AssertionError('forged certificate accepted: '+name)
    # Constants intentionally alter one field; these are corruption fixtures,
    # not alternative scientific reference computations.
    retain('signed_value', lambda c: c['requests'][0].__setitem__('value', 999))
    retain('component_weight', lambda c: c['requests'][0]['weights'].__setitem__('J_zero', 999))
    retain('negative_bit', lambda c: c['requests'][0]['inputs'].__setitem__('k', 1))
    retain('modulus', lambda c: c['requests'][0]['inputs'].__setitem__('R', 2))
    retain('residue', lambda c: c['requests'][0]['inputs'].__setitem__('r', 1))
    retain('source', lambda c: c.__setitem__('source_sha256', '0'*64))
    retain('bool_integer', lambda c: c['requests'][0]['inputs'].__setitem__('g', True))
    retain('nonstring_key', lambda c: c['requests'][0]['weights'].__setitem__(0, 0))
    retain('trace_value', lambda c: c['actual_integer_evidence']['signed_operations'][0].__setitem__('result', 999))
    return attempts


def main():
    started = time.perf_counter()
    LIVE['stage'] = 'CHECK_STARTUP_GUARD'
    guard_path = ROOT.parent / 'STARTUP_GUARD.json'
    guard = json.loads(guard_path.read_text(encoding='utf-8'))
    assert guard.get('activity_allowed') is True and guard.get('persistence_allowed') is True
    assert guard.get('activity_id') == 'RA-CAAAC604CB513AEA8BBC1DFC'
    assert guard.get('boundary') == 'startup' and guard.get('mode') == 'TASK_RESEARCH'
    assert guard.get('sync_debt_events') == []
    LIVE['guard'] = {'sha256': sha(guard_path), 'receipt': guard}
    targets = [ROOT / 'SIGNED_GAP_RESULTS.json.gz', ROOT / 'SIGNED_GAP_SUMMARY.json']
    assert not any(path.exists() for path in targets), 'do not overwrite existing evidence'
    source_names = ('signed_gap.py', 'check_signed_gap.py')
    sources = {name: sha(ROOT/name) for name in source_names}
    output = {'status': 'RUNNING', 'source_sha256': sources, 'cases': [],
              'startup_guard': LIVE['guard'],
              'scope': 'V=1 integer observer; no phase propagation, order discovery or full Gram integration'}
    LIVE['output'] = output
    optimized_digits = brute_digits = replay_digits = 0
    equalities = pair_count = 0
    first_certificate = None
    for g, k, R in CASES:
        LIVE.update(stage='THREE_FLOOR_COUNTS', current_tuple=(g, k, R),
                    brute_runner=None, brute_digits=[], brute_pairs=[],
                    brute_values=None, replay_capture=[])
        observer = SignedGapObserver()
        LIVE['observer'] = observer
        values = [observer.one_negative(g, k, R, r)['value'] for r in range(R)]
        LIVE['stage'] = 'TYPED_EXHAUSTIVE_COMPARATOR'
        explicit, brute = typed_pair_histogram(g, k, R)
        assert values == explicit
        certificate = observer.export_certificate()
        LIVE['stage'] = 'POSITIVE_CERTIFICATE_REPLAY'
        replay = verify_certificate(json.loads(json.dumps(certificate)), replay_capture=LIVE['replay_capture'])
        optimized_digits += certificate['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays']
        brute_digits += brute['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays']
        replay_digits += replay['replay_arithmetic_stats']['adder_digit_replays']
        equalities += len(values)
        pair_count += len(brute['pair_observations'])
        output['cases'].append({'inputs': {'g': g, 'k': k, 'R': R}, 'values': values,
            'all_residues_equal': True, 'certificate': certificate,
            'typed_enumeration': brute, 'verification': replay})
        if first_certificate is None:
            first_certificate = certificate
        print(json.dumps({'stage': 'CASE_COMPLETE', 'tuple': (g, k, R),
                          'values': values, 'actual_core_calls': len(CALLS)}), flush=True)
    assert output['cases'][0]['values'][1] == -1
    assert output['cases'][7]['values'] == [0]
    LIVE['stage'] = 'INPUT_REJECTIONS'
    output['input_rejections'] = rejection_checks()
    LIVE['stage'] = 'TAMPER_REJECTIONS'
    output['tamper_rejections'] = tamper_checks(first_certificate)
    negative_replay_digits = sum(certificate['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays']
        for attempt in output['tamper_rejections'] for certificate in attempt['actual_replay_certificates'])
    assert sources == {name: sha(ROOT/name) for name in source_names}
    assert sha(guard_path) == LIVE['guard']['sha256'], 'startup guard changed during execution'
    output.update(status='PASS', actual_core_calls=deepcopy(CALLS),
                  actual_core_call_count=len(CALLS), elapsed_seconds=time.perf_counter()-started)
    LIVE['stage'] = 'SERIALIZE_SUCCESS_EVIDENCE'
    raw = json.dumps(output, sort_keys=True, separators=(',', ':')).encode()+b'\n'
    targets[0].write_bytes(gzip.compress(raw, compresslevel=6, mtime=0))
    summary = {'status': 'PASS', 'source_sha256': sources, 'case_count': len(CASES),
        'all_residue_equalities': equalities, 'values': [case['values'] for case in output['cases']],
        'typed_pair_observations': pair_count, 'input_rejections': len(output['input_rejections']),
        'tamper_rejections': len(output['tamper_rejections']),
        'actual_core_call_count': len(CALLS), 'optimized_adder_digit_replays': optimized_digits,
        'typed_enumeration_adder_digit_replays': brute_digits, 'positive_replay_adder_digit_replays': replay_digits,
        'negative_replay_adder_digit_replays': negative_replay_digits,
        'raw_bytes': len(raw), 'gzip_bytes': targets[0].stat().st_size,
        'payload_sha256': hashlib.sha256(raw).hexdigest(), 'artifact_sha256': sha(targets[0]),
        'elapsed_seconds': output['elapsed_seconds'],
        'quantum_phase_propagation_performed': False, 'order_discovery_performed': False,
        'full_gram_integration_performed': False,
        'resource_scope': 'digit counts separate optimized/enumeration/positive replay/negative replay; core calls are process total; host serialization/index cost excluded'}
    targets[1].write_text(json.dumps(summary, indent=2)+'\n', encoding='utf-8')
    LIVE['stage'] = 'COMPLETE'
    print(json.dumps(summary))


def preserve_failure(error):
    observer = LIVE.get('observer')
    runner = LIVE.get('brute_runner')
    brute = None if runner is None else {
        'arithmetic_operations': runner.arithmetic.operations,
        'arithmetic_stats': runner.arithmetic.stats,
        'signed_operations': runner.signed_operations, 'moment_nodes': runner.nodes,
        'window_weight_queries': runner.weight_queries, 'stats': runner.stats}
    failure = {'status': 'FAILED_EXECUTION', 'stage': LIVE['stage'],
        'error_type': type(error).__name__, 'error': str(error), 'traceback': traceback.format_exc(),
        'source_sha256': {name: sha(ROOT/name) for name in ('signed_gap.py', 'check_signed_gap.py')},
        'startup_guard': LIVE.get('guard'), 'current_tuple': LIVE.get('current_tuple'),
        'completed_output': LIVE.get('output'),
        'current_observer': None if observer is None else observer.incomplete_snapshot(),
        'current_brute_evidence': brute, 'current_brute_digits': LIVE['brute_digits'],
        'current_brute_pairs': LIVE['brute_pairs'], 'current_brute_values': LIVE['brute_values'],
        'current_replay_capture': LIVE['replay_capture'], 'actual_core_calls': CALLS,
        'completed_tamper_attempts': LIVE['tamper_attempts'],
        'current_attempted_tamper': LIVE['attempted_tamper'],
        'scientific_scope': 'available exact integer work only; incomplete and not admitted'}
    raw = json.dumps(failure, sort_keys=True, separators=(',', ':')).encode()+b'\n'
    target = ROOT / 'SIGNED_GAP_FAILED_EXECUTION.json.gz'
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
