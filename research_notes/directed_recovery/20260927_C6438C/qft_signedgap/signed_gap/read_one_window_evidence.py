"""Pure I/O readback and recorded-cost aggregation; no native imports."""
from pathlib import Path
import gzip
import hashlib
import json

from read_signed_gap_evidence import costs

ROOT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    artifact = ROOT/'ONE_WINDOW_RESULTS.json.gz'
    raw = gzip.decompress(artifact.read_bytes())
    evidence = json.loads(raw)
    summary = json.loads((ROOT/'ONE_WINDOW_SUMMARY.json').read_bytes())
    assert evidence['status'] == summary['status'] == 'PASS'
    assert hashlib.sha256(raw).hexdigest() == summary['payload_sha256']
    assert sha(artifact) == summary['artifact_sha256']
    for name, expected in summary['source_sha256'].items():
        assert sha(ROOT/name) == expected
    old = evidence['baseline']
    assert sha(ROOT/old['artifact']) == old['artifact_sha256']
    cases = evidence['cases']
    production = costs(c['certificate']['actual_integer_evidence'] for c in cases)
    replay = costs(c['verification']['replay_certificate']['actual_integer_evidence'] for c in cases)
    negative = costs(c['actual_integer_evidence'] for row in evidence['negative_checks']
                     for c in row['actual_replay_certificates'])
    assert production['arithmetic_totals']['adder_digit_replays'] == summary['fresh_production_adder_digit_replays']
    assert replay['arithmetic_totals']['adder_digit_replays'] == summary['positive_replay_adder_digit_replays']
    assert negative['arithmetic_totals']['adder_digit_replays'] == summary['negative_replay_adder_digit_replays']
    historical_digits = sum(c['baseline_reference']['recorded_production_arithmetic_stats']['adder_digit_replays'] for c in cases)
    assert historical_digits == summary['historical_three_window_production_adder_digit_replays']
    record = {'status': 'READBACK_PASS', 'scientific_execution_performed_by_this_reader': False,
        'reader_sha256': sha(__file__), 'metadata_reader_dependency_sha256': sha(ROOT/'read_signed_gap_evidence.py'),
        'source_sha256': summary['source_sha256'],
        'payload_sha256': summary['payload_sha256'], 'artifact_sha256': summary['artifact_sha256'],
        'startup_guard_sha256': evidence['startup_guard']['sha256'], 'baseline_reference': old,
        'production': production, 'positive_replay': replay, 'negative_replay': negative,
        'historical_production_digits': historical_digits,
        'digit_replay_reduction_count': historical_digits-production['arithmetic_totals']['adder_digit_replays'],
        'digit_replay_reduction_fraction': {
            'numerator': historical_digits-production['arithmetic_totals']['adder_digit_replays'],
            'denominator': historical_digits},
        'negative_replay_capture_counts': [{'name': row['name'], 'replays': len(row['actual_replay_certificates'])}
                                          for row in evidence['negative_checks']],
        'actual_core_calls': evidence['actual_core_calls'],
        'per_case': summary['per_case'],
        'failure_artifact_present': (ROOT/'ONE_WINDOW_FAILED_EXECUTION.json.gz').exists(),
        'cost_scope': 'recorded typed operation counts; no historical wall-time or CPU-work equivalence claim'}
    with (ROOT/'ONE_WINDOW_READBACK.json').open('x', encoding='utf-8') as stream:
        json.dump(record, stream, indent=2)
        stream.write('\n')
    print(json.dumps(record))


if __name__ == '__main__':
    main()
