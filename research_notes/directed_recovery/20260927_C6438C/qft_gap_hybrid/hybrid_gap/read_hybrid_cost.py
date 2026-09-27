"""Full saved-evidence accounting; standard-library I/O only, no scientific imports."""
from pathlib import Path
from copy import deepcopy
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
STAGES = ROOT.parents[1]
GZIP_PIN = '036242b07b480d05937b6a72ffc375dc33eea48283647964ca020b78bdb3f962'
RAW_PIN = '76efccc284001219b2ecde3523557f66e55e828125e4132a83814f25df80398b'
KEYS = ('typed_operations', 'adder_digit_replays', 'host_bit_wiring_operations',
        'host_bit_length_calls_in_arithmetic', 'native_kernel_calls_delta')
RUNNERS = ('routing', 'endpoint', 'direct')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def runners(certificate):
    return {'routing': certificate['routing_integer_evidence'],
            'endpoint': certificate['endpoint_certificate']['actual_integer_evidence'],
            'direct': certificate['direct_certificate']['actual_integer_evidence']}


def semantic(certificate):
    out = deepcopy(certificate)
    for evidence in runners(out).values():
        stats = evidence['arithmetic_stats']
        assert type(stats['native_kernel_calls_delta']) is int and stats['native_kernel_calls_delta'] >= 0
        stats['native_kernel_calls_delta'] = 0
    return canonical(out)


def trace_counts(trace):
    """Count stored cells/steps only. No value, carry, product or remainder evaluation."""
    result = {'adder_digit_replays': 0, 'host_bit_wiring_operations': 0,
              'host_bit_length_calls_in_arithmetic': 0}
    def visit(item):
        if isinstance(item, dict):
            if 'cells' in item and 'low' in item and 'carry' in item:
                count = len(item['cells'])
                result['adder_digit_replays'] += count
                result['host_bit_wiring_operations'] += 10*count
                return
            operation = item.get('operation')
            if operation == 'BRC_UNSIGNED_COMPARE':
                result['host_bit_wiring_operations'] += 3
                result['host_bit_length_calls_in_arithmetic'] += 2
            elif operation == 'BRC_UNSIGNED_SHIFT_ADD':
                result['host_bit_wiring_operations'] += 3*len(item['steps'])
                result['host_bit_length_calls_in_arithmetic'] += 3
            elif operation == 'BRC_UNSIGNED_LONG_DIVISION':
                result['host_bit_wiring_operations'] += 6*len(item['steps'])
                result['host_bit_length_calls_in_arithmetic'] += 1
            for child in item.values():
                visit(child)
        elif isinstance(item, list):
            for child in item:
                visit(child)
    visit(trace)
    return result


def validate_evidence(evidence):
    operations, stats = evidence['arithmetic_operations'], evidence['arithmetic_stats']
    assert len(operations) == stats['typed_operations']
    indices = [index for row in evidence['signed_operations'] for index in row['typed_operation_indices']]
    assert indices == list(range(len(operations)))
    recounted = {'adder_digit_replays': 0, 'host_bit_wiring_operations': 0,
                 'host_bit_length_calls_in_arithmetic': 0}
    for operation in operations:
        counts = trace_counts(operation['trace'])
        if operation['operation'] == 'add':
            counts['host_bit_length_calls_in_arithmetic'] += 2
        for key, value in counts.items():
            recounted[key] += value
    assert recounted == {key: stats[key] for key in recounted}


def aggregate(evidences):
    rows = list(evidences)
    for row in rows:
        validate_evidence(row)
    return {'evidence_count': len(rows),
        'arithmetic_totals': {key: sum(row['arithmetic_stats'][key] for row in rows) for key in KEYS},
        'signed_operations': sum(len(row['signed_operations']) for row in rows),
        'moment_nodes': sum(len(row['moment_nodes']) for row in rows),
        'moment_requests': sum(row['stats']['moment_requests'] for row in rows),
        'cache_hits': sum(row['stats']['cache_hits'] for row in rows),
        'window_queries': sum(len(row['window_weight_queries']) for row in rows),
        'max_recursion_depth': max((row['stats']['max_recursion_depth'] for row in rows), default=0),
        'max_observed_integer_bits': max((row['stats']['max_observed_integer_bits'] for row in rows), default=0)}


def group(certificates):
    records = list(certificates)
    detail = {name: aggregate(runners(c)[name] for c in records) for name in RUNNERS}
    detail['arithmetic_totals'] = {key: sum(detail[name]['arithmetic_totals'][key] for name in RUNNERS)
                                   for key in KEYS}
    detail['execution_count'] = len(records)
    return detail


def validate_request_links(certificate):
    position = 0
    consumed = {'endpoint': 0, 'direct': 0}
    for request in certificate['requests']:
        assert request['routing_operations_start'] == position
        position = request['routing_operations_stop']
        kind = request['nested_kind']
        if kind is not None:
            assert request['nested_request_index'] == consumed[kind]
            nested = certificate[kind+'_certificate']['requests'][consumed[kind]]
            assert canonical(request['nested_request']) == canonical(nested)
            assert type(request['value']) is int and request['value'] == nested['value']
            consumed[kind] += 1
        elif request['branch'] == 'interior_divisible_zero':
            proof = request['divisibility']
            operation = certificate['routing_integer_evidence']['signed_operations'][
                proof['division_signed_operation_index']]
            assert operation['operation'] == 'signed_euclidean_division'
            assert operation['inputs'] == [proof['U'], proof['R']]
            assert operation['result'] == [proof['quotient'], 0] and proof['remainder'] == 0
            zero = certificate['routing_integer_evidence']['signed_operations'][
                request['zero_proof']['zero_signed_operation_index']]
            assert zero['inputs'] == [proof['U'], -proof['U']]
            assert zero['operation'] == 'signed_add' and type(zero['result']) is int and zero['result'] == 0
            assert type(request['value']) is int and request['value'] == 0
        else:
            raise AssertionError('unknown unlinked route')
        if request['branch'] == 'endpoint':
            assert request['routing_operations_start'] == request['routing_operations_stop']
    assert position == len(certificate['routing_integer_evidence']['signed_operations'])
    for kind, count in consumed.items():
        assert count == len(certificate[kind+'_certificate']['requests'])


def main():
    compressed = (ROOT/'HYBRID_RESULTS.json.gz').read_bytes()
    raw = gzip.decompress(compressed)
    assert sha(compressed) == GZIP_PIN and sha(raw) == RAW_PIN
    data = json.loads(raw)
    summary = json.loads((ROOT/'HYBRID_SUMMARY.json').read_bytes())
    assert data['status'] == summary['status'] == 'PASS'
    assert summary['raw_bytes'] == len(raw) and summary['gzip_bytes'] == len(compressed)
    for name, pin in data['source_sha256'].items():
        assert sha((ROOT/name).read_bytes()) == pin == summary['source_sha256'][name]
    paths = {'endpoint_signed_gap.py': STAGES/'sep27-qft-gap-shortcuts/endpoint_gap/endpoint_signed_gap.py',
        'direct_signed_gap.py': STAGES/'sep27-qft-gap-direct/direct_gap/direct_signed_gap.py',
        'signed_gap.py': STAGES/'sep27-qft-signedgap/signed_gap/signed_gap.py',
        'typed_floor_moments.py': STAGES/'sep27-qft-adaptive/nonzero_structure/typed_floor_moments.py',
        'DESIGN.md': ROOT.parent/'DESIGN.md'}
    for name, pin in data['dependency_sha256'].items():
        assert sha(paths[name].read_bytes()) == pin
    guard = data['startup_guard']
    assert sha((ROOT.parent/'STARTUP_GUARD.json').read_bytes()) == guard['sha256']
    assert guard['receipt']['activity_allowed'] is True and guard['receipt']['sync_debt_events'] == []
    old_compressed = (STAGES/'sep27-qft-gap-direct/direct_gap/DIRECT_RESULTS.json.gz').read_bytes()
    old_raw = gzip.decompress(old_compressed)
    assert sha(old_compressed) == data['history']['artifact_sha256']
    assert sha(old_raw) == data['history']['payload_sha256']
    history = json.loads(old_raw)
    assert history['status'] == 'PASS' and len(history['cases']) == len(data['cases']) == 9
    cases = data['cases']
    common_native = None
    for case, old in zip(cases, history['cases']):
        cert, replay = case['certificate'], case['verification']['replay_certificate']
        assert semantic(cert) == semantic(replay)
        assert case['inputs'] == old['inputs']
        assert case['values'] == old['values'] == case['history_reference']['values']
        assert case['values'] == [request['value'] for request in cert['requests']]
        assert case['history_reference']['recorded_pure_direct_stats'] == old['new_production_arithmetic_stats']
        assert cert['source_sha256'] == data['source_sha256']['hybrid_signed_gap.py']
        assert cert['dependency_sha256'] == data['dependency_sha256']
        validate_request_links(cert)
        for evidence in runners(cert).values():
            native = canonical(evidence['native_source'])
            common_native = common_native or native
            assert native == common_native
    negatives = data['negative_checks']
    negative_rows = []
    for row in negatives:
        assert row['rejected'] is True and row['native_core_calls_delta'] == 0
        original = cases[row['case_index']]['certificate']
        assert semantic(row['attempted_certificate']) != semantic(original)
        for replay in row['actual_replay_certificates']:
            assert semantic(replay) == semantic(original)
        negative_rows.append({'name': row['name'], 'case_index': row['case_index'],
            'executed_replay_count': len(row['actual_replay_certificates']),
            'runner_costs': group(row['actual_replay_certificates']),
            'native_core_calls_delta': row['native_core_calls_delta']})
    scopes = {
        'production': group(case['certificate'] for case in cases),
        'positive_replay': group(case['verification']['replay_certificate'] for case in cases),
        'negative_replay': group(cert for row in negatives for cert in row['actual_replay_certificates'])}
    for name, scope in scopes.items():
        assert scope['arithmetic_totals'] == summary[name+'_totals']
    assert sum(scope['arithmetic_totals']['native_kernel_calls_delta'] for scope in scopes.values()) == 1
    assert data['actual_core_call_count'] == len(data['actual_core_calls']) == summary['actual_core_call_count'] == 1
    assert summary['input_rejections'] == len(data['input_rejections']) == 8
    assert summary['negative_checks'] == len(negatives) == 15
    assert summary['paid_negative_replays'] == scopes['negative_replay']['execution_count'] == 11
    actual_branches = {name: 0 for name in data['branch_counts']}
    per_case = []
    for case, expected in zip(cases, summary['per_case']):
        own = runners(case['certificate'])
        branches = {name: 0 for name in actual_branches}
        for request in case['certificate']['requests']:
            branches[request['branch']] += 1
            actual_branches[request['branch']] += 1
        assert branches == case['branch_counts'] == expected['branch_counts']
        assert expected['values'] == case['values'] and expected['inputs'] == case['inputs']
        for name in RUNNERS:
            assert expected[name+'_digits'] == own[name]['arithmetic_stats']['adder_digit_replays']
        assert expected['total_digits'] == sum(own[name]['arithmetic_stats']['adder_digit_replays'] for name in RUNNERS)
        per_case.append(expected)
    assert actual_branches == data['branch_counts'] == summary['branch_counts']
    assert sum(len(case['values']) for case in cases) == summary['residue_equalities'] == 31
    output = {'status': 'FULL_SAVED_COST_READBACK_PASS', 'scientific_execution_performed': False,
        'reader_sha256': sha(Path(__file__).read_bytes()), 'source_sha256': data['source_sha256'],
        'dependency_sha256': data['dependency_sha256'], 'payload_sha256': sha(raw),
        'artifact_sha256': sha(compressed), 'raw_bytes': len(raw), 'gzip_bytes': len(compressed),
        'startup_guard_sha256': guard['sha256'], **scopes,
        'all_scopes_arithmetic_totals': {key: sum(scope['arithmetic_totals'][key] for scope in scopes.values()) for key in KEYS},
        'per_case': per_case, 'branch_counts': actual_branches, 'negative_details': negative_rows,
        'actual_core_calls': data['actual_core_calls'], 'global_actual_core_calls_retained_once': True,
        'full_history_artifact_hash_checked': True, 'strict_positive_semantic_equality_checked': True,
        'all_failed_paid_replays_equal_honest_fresh_certificate': True,
        'signed_to_typed_indices_cover_operations_once_in_order': True,
        'digit_wiring_bitlength_counts_recounted_from_stored_trace_shapes': True,
        'mixed_route_sequence_in_one_observer_executed': False,
        'started_utc': data['started_utc'],
        'completed_utc_before_serialization': data['completed_utc_before_serialization'],
        'elapsed_seconds_before_serialization': data['elapsed_seconds_before_serialization'],
        'log_sha256': sha((ROOT/'HYBRID_EXECUTION_LOG.txt').read_bytes()),
        'failure_artifact_present': (ROOT/'HYBRID_FAILED_EXECUTION.json.gz').exists(),
        'scope': 'metadata-only complete saved-resource audit; no arithmetic values recomputed and no scientific module imported'}
    with (ROOT/'HYBRID_COST_READBACK.json').open('x', encoding='utf-8') as stream:
        stream.write(json.dumps(output, indent=2)+'\n')
    print(json.dumps({key: value for key, value in output.items()
                      if key not in ('actual_core_calls', 'per_case', 'negative_details')}))


if __name__ == '__main__':
    main()
