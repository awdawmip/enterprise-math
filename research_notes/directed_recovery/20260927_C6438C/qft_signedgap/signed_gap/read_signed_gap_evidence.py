"""Pure I/O integrity and resource-metadata readback; no scientific execution."""
from pathlib import Path
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def costs(evidences):
    rows = list(evidences)
    metrics = ('typed_operations', 'adder_digit_replays', 'host_bit_wiring_operations',
               'host_bit_length_calls_in_arithmetic', 'native_kernel_calls_delta')
    return {'evidence_count': len(rows),
        'arithmetic_totals': {key: sum(row['arithmetic_stats'][key] for row in rows) for key in metrics},
        'signed_operations': sum(len(row['signed_operations']) for row in rows),
        'moment_nodes': sum(len(row['moment_nodes']) for row in rows),
        'window_queries': sum(len(row['window_weight_queries']) for row in rows),
        'moment_requests': sum(row['stats']['moment_requests'] for row in rows),
        'cache_hits': sum(row['stats']['cache_hits'] for row in rows),
        'max_recursion_depth': max((row['stats']['max_recursion_depth'] for row in rows), default=0),
        'max_observed_integer_bits': max((row['stats']['max_observed_integer_bits'] for row in rows), default=0)}


def main():
    compressed = (ROOT/'SIGNED_GAP_RESULTS.json.gz').read_bytes()
    raw = gzip.decompress(compressed)
    evidence = json.loads(raw)
    summary = json.loads((ROOT/'SIGNED_GAP_SUMMARY.json').read_text(encoding='utf-8'))
    assert evidence['status'] == summary['status'] == 'PASS'
    assert sha(raw) == summary['payload_sha256']
    assert sha(compressed) == summary['artifact_sha256']
    for name, expected in summary['source_sha256'].items():
        assert sha((ROOT/name).read_bytes()) == expected
    cases = evidence['cases']
    negative = [certificate['actual_integer_evidence']
                for item in evidence['tamper_rejections']
                for certificate in item['actual_replay_certificates']]
    record = {'status': 'READBACK_PASS', 'scientific_execution_performed_by_this_reader': False,
        'reader_sha256': sha(Path(__file__).read_bytes()),
        'payload_sha256': sha(raw), 'artifact_sha256': sha(compressed),
        'source_sha256': summary['source_sha256'],
        'startup_guard_sha256': evidence['startup_guard']['sha256'],
        'native_source': cases[0]['certificate']['actual_integer_evidence']['native_source'],
        'optimized': costs(case['certificate']['actual_integer_evidence'] for case in cases),
        'enumeration': costs(case['typed_enumeration']['actual_integer_evidence'] for case in cases),
        'positive_replay': costs(case['verification']['replay_certificate']['actual_integer_evidence'] for case in cases),
        'negative_replay': costs(negative),
        'per_case': [{'inputs': case['inputs'], 'values': case['values'],
            'optimized_digits': case['certificate']['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays'],
            'enumeration_digits': case['typed_enumeration']['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays'],
            'pair_count': len(case['typed_enumeration']['pair_observations'])} for case in cases],
        'tamper_replay_capture_counts': [{'name': item['name'], 'replays': len(item['actual_replay_certificates'])}
                                       for item in evidence['tamper_rejections']],
        'actual_core_calls': evidence['actual_core_calls'],
        'failed_execution_artifact_present': (ROOT/'SIGNED_GAP_FAILED_EXECUTION.json.gz').exists()}
    for field, summary_field in (('optimized', 'optimized_adder_digit_replays'),
                                ('enumeration', 'typed_enumeration_adder_digit_replays'),
                                ('positive_replay', 'positive_replay_adder_digit_replays'),
                                ('negative_replay', 'negative_replay_adder_digit_replays')):
        assert record[field]['arithmetic_totals']['adder_digit_replays'] == summary[summary_field]
    target = ROOT/'SIGNED_GAP_READBACK.json'
    with target.open('x', encoding='utf-8') as stream:
        json.dump(record, stream, indent=2)
        stream.write('\n')
    print(json.dumps(record))


if __name__ == '__main__':
    main()
