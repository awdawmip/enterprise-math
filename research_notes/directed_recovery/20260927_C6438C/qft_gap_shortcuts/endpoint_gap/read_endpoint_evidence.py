"""Full payload I/O and recorded resource aggregation; no native imports."""
from copy import deepcopy
from pathlib import Path
from datetime import datetime, timezone
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
HISTORY = ROOT.parents[1]/'sep27-qft-signedgap/signed_gap/ONE_WINDOW_RESULTS.json.gz'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def costs(evidences):
    rows = list(evidences)
    keys = ('typed_operations', 'adder_digit_replays', 'host_bit_wiring_operations',
            'host_bit_length_calls_in_arithmetic', 'native_kernel_calls_delta')
    for row in rows:
        assert len(row['arithmetic_operations']) == row['arithmetic_stats']['typed_operations']
        indices = [index for operation in row['signed_operations']
                   for index in operation['typed_operation_indices']]
        assert set(indices) == set(range(len(row['arithmetic_operations'])))
        assert len(indices) == len(set(indices))
    return {'evidence_count': len(rows),
        'arithmetic_totals': {key: sum(row['arithmetic_stats'][key] for row in rows) for key in keys},
        'signed_operations': sum(len(row['signed_operations']) for row in rows),
        'moment_nodes': sum(len(row['moment_nodes']) for row in rows),
        'window_queries': sum(len(row['window_weight_queries']) for row in rows),
        'moment_requests': sum(row['stats']['moment_requests'] for row in rows),
        'cache_hits': sum(row['stats']['cache_hits'] for row in rows),
        'max_recursion_depth': max((row['stats']['max_recursion_depth'] for row in rows), default=0),
        'max_observed_integer_bits': max((row['stats']['max_observed_integer_bits'] for row in rows), default=0)}


def semantic(certificate):
    result = deepcopy(certificate)
    result['actual_integer_evidence']['arithmetic_stats']['native_kernel_calls_delta'] = 0
    return result


def main():
    artifact = ROOT/'ENDPOINT_RESULTS.json.gz'
    compressed = artifact.read_bytes()
    raw = gzip.decompress(compressed)
    summary = json.loads((ROOT/'ENDPOINT_SUMMARY.json').read_bytes())
    evidence = json.loads(raw)
    assert sha(compressed) == summary['artifact_sha256'] == 'f5e256ecb694225bef17843aa78c5adb1ae0df6205e4cf3d3e4819c2e6d6738f'
    assert sha(raw) == summary['payload_sha256'] == '799bd9c51f98f973b6f4201f5684f83c0c427359d756e4a1b7bfdef239d8002e'
    assert evidence['status'] == summary['status'] == 'PASS'
    for name, expected in summary['source_sha256'].items():
        assert sha((ROOT/name).read_bytes()) == expected == evidence['source_sha256'][name]
    assert sha((ROOT.parent/'STARTUP_GUARD.json').read_bytes()) == evidence['startup_guard']['sha256']
    assert sha((ROOT.parent/'ENDPOINT_IDENTITIES.md').read_bytes()) == evidence['endpoint_proof_sha256']
    history_bytes = HISTORY.read_bytes()
    history_raw = gzip.decompress(history_bytes)
    assert sha(history_bytes) == evidence['history']['artifact_sha256']
    assert sha(history_raw) == evidence['history']['payload_sha256']
    history = json.loads(history_raw)
    cases = evidence['cases']
    assert len(cases) == len(history['cases']) == summary['cases'] == 9
    endpoint_intervals = 0
    for index, (case, old) in enumerate(zip(cases, history['cases'])):
        assert case['inputs'] == old['inputs']
        assert case['values'] == old['values'] == case['history_reference']['values']
        assert case['history_reference']['case_index'] == index
        assert case['history_reference']['recorded_one_window_production_arithmetic_stats'] == old['certificate']['actual_integer_evidence']['arithmetic_stats']
        cert = case['certificate']
        replay = case['verification']['replay_certificate']
        assert semantic(cert) == semantic(replay)
        assert [record['value'] for record in cert['requests']] == case['values']
        assert all(record['branch'] == case['branch'] for record in cert['requests'])
        if case['branch'] != 'interior_one_window':
            assert not cert['actual_integer_evidence']['window_weight_queries']
            assert not cert['actual_integer_evidence']['moment_nodes']
            endpoint_intervals += sum(len(record['interval_receipts']) for record in cert['requests'])
        else:
            for new, frozen in zip(cert['requests'], old['certificate']['requests']):
                assert new['frozen_one_window_request'] == frozen
    assert sum(len(case['values']) for case in cases) == 31
    assert all(row['rejected'] is True for row in evidence['input_rejections'])
    assert all(row['rejected'] is True for row in evidence['negative_checks'])
    production = costs(case['certificate']['actual_integer_evidence'] for case in cases)
    replay = costs(case['verification']['replay_certificate']['actual_integer_evidence'] for case in cases)
    negative = costs(cert['actual_integer_evidence'] for row in evidence['negative_checks']
                     for cert in row['actual_replay_certificates'])
    for field, expected in ((production, 'fresh_production_adder_digit_replays'),
                            (replay, 'positive_replay_adder_digit_replays'),
                            (negative, 'negative_replay_adder_digit_replays')):
        assert field['arithmetic_totals']['adder_digit_replays'] == summary[expected]
    old_digits = sum(case['certificate']['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays'] for case in history['cases'])
    assert old_digits == summary['historical_one_window_production_adder_digit_replays']
    record = {'status': 'READBACK_PASS', 'scientific_execution_performed_by_this_reader': False,
        'reader_sha256': sha(Path(__file__).read_bytes()),
        'source_sha256': summary['source_sha256'], 'proof_sha256': evidence['endpoint_proof_sha256'],
        'payload_sha256': sha(raw), 'artifact_sha256': sha(compressed),
        'runlog_sha256': sha((ROOT/'ENDPOINT_RUN.log').read_bytes()),
        'startup_guard_sha256': evidence['startup_guard']['sha256'],
        'history_reference': evidence['history'],
        'complete_operation_index_coverage_verified': True,
        'positive_replay_semantic_full_equality_verified': True,
        'interior_requests_equal_frozen_requests': True,
        'production': production, 'positive_replay': replay, 'negative_replay': negative,
        'production_per_branch': {branch: costs(case['certificate']['actual_integer_evidence']
            for case in cases if case['branch'] == branch) for branch in summary['branch_counts']},
        'endpoint_interval_queries': endpoint_intervals,
        'historical_production_digits': old_digits,
        'digit_replay_reduction_count': old_digits-production['arithmetic_totals']['adder_digit_replays'],
        'negative_replay_capture_counts': [{'name': row['name'], 'replays': len(row['actual_replay_certificates'])}
                                          for row in evidence['negative_checks']],
        'actual_core_calls': evidence['actual_core_calls'],
        'native_source': cases[0]['certificate']['actual_integer_evidence']['native_source'],
        'per_case': summary['per_case'],
        'raw_bytes': len(raw), 'gzip_bytes': len(compressed),
        'result_last_write_utc': datetime.fromtimestamp(artifact.stat().st_mtime, timezone.utc).isoformat(),
        'failure_artifact_present': (ROOT/'ENDPOINT_FAILED_EXECUTION.json.gz').exists(),
        'cost_scope': 'recorded operation counts only; no new scientific execution or historical timing ratio'}
    with (ROOT/'ENDPOINT_READBACK.json').open('x', encoding='utf-8') as stream:
        stream.write(json.dumps(record, indent=2)+'\n')
    print(json.dumps(record))


if __name__ == '__main__':
    main()
