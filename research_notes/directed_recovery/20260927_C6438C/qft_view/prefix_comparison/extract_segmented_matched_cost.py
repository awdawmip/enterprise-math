"""Read-only timing/cost extraction from the one completed matched experiment."""
from pathlib import Path
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
RAW_SHA = '461f1c84cafdee8b8d38ae9577f4d9a6472737d9f292aef9c7fdf606921fc80d'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def packed(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False,
                      allow_nan=False).encode()


def run_record(run):
    operations = run['evidence']['inherited']['observer_operations']
    assert len(operations) == run['total_actual_core_calls']
    assert len(operations) == run['calculation_actual_core_calls']
    for before, after in zip(run['table_instances_before'], run['table_instances_after']):
        assert (before['role'], before['parent_factory_index']) == (after['role'], after['parent_factory_index'])
        assert before['stats']['computed_columns'] == after['stats']['computed_columns']
        assert before['stats']['column_adder_digit_replays'] == after['stats']['column_adder_digit_replays']
    return {key: run[key] for key in ('label', 'implementation', 'calculation_seconds',
        'evidence_capture_seconds', 'total_seconds_through_evidence',
        'counter_inventory_and_UTC_gap_seconds', 'calculation_actual_core_calls',
        'total_actual_core_calls', 'core_call_interval', 'counters_before_evidence',
        'wall_started_utc', 'wall_calculation_end_utc', 'wall_evidence_end_utc')} | {
        'observer_graph_states_sum': sum(op['states'] for op in operations),
        'final_guard_snapshot': run['evidence']['boundary_guard']}


def main():
    compressed = (ROOT/'SEGMENTED_MATCHED_RESULTS.json.gz').read_bytes()
    raw = gzip.decompress(compressed)
    assert sha(raw) == RAW_SHA
    data = json.loads(raw)
    summary = json.loads((ROOT/'SEGMENTED_MATCHED_SUMMARY.json').read_bytes())
    assert data['status'] == summary['status'] == 'PASSED'
    assert summary['raw_sha256'] == sha(raw) and summary['gzip_sha256'] == sha(compressed)
    for path, expected in data['source_hashes'].items():
        assert sha(Path(path).read_bytes()) == expected
    assert sha((ROOT.parent/'STARTUP_GUARD.json').read_bytes()) == data['startup_guard']['sha256']
    calls = data['actual_native_core_calls']
    assert len(calls) == data['actual_native_core_call_count']
    admission = data['native_admission_call_interval']
    assert admission[0] == 0
    cold = data['shared_cold_SO_bank']
    left, right = cold['call_interval']
    assert calls[left:right] == cold['evidence']['setup']['actual_core_calls']
    assert right-left == cold['actual_core_calls'] == 36
    assert data['standalone_token_derivation']['actual_core_calls'] == 0
    intervals = [admission, cold['call_interval']]

    pairs = []
    groups = {}
    all_runs = []
    for pair in data['pairs']:
        old = next(run for run in pair['runs'] if run['implementation'] == 'BoundaryCheckedSOTrace')
        new = next(run for run in pair['runs'] if run['implementation'] == 'SegmentedBoundarySOTrace')
        for key in ('plans', 'numeric_ledger', 'terminal_mass'):
            assert old[key] == new[key]
        for key in ('correlations', 'observer_operations'):
            assert old['evidence']['inherited'][key] == new['evidence']['inherited'][key]
        for key in ('gram', 'policy'):
            assert old['counters_before_evidence'][key] == new['counters_before_evidence'][key]
        assert old['counters_before_evidence']['guard']['stats'] == new['counters_before_evidence']['guard']['stats']
        records = [run_record(run) for run in pair['runs']]
        intervals.extend(run['core_call_interval'] for run in pair['runs'])
        all_runs.extend(records)
        item = dict(pair['summary'])
        item['new_over_old_calculation_ratio'] = new['calculation_seconds']/old['calculation_seconds']
        item['new_over_old_through_evidence_ratio'] = new['total_seconds_through_evidence']/old['total_seconds_through_evidence']
        item['runs'] = records
        pairs.append(item)
        groups.setdefault((item['N'], item['a']), []).append(item)
    aggregates = []
    for (N, a), rows in groups.items():
        item = {'N': N, 'a': a, 'pairs': len(rows), 'independent_random_trials': False}
        for suffix in ('seconds', 'evidence_seconds', 'total_seconds'):
            old = sum(row['old_'+suffix] for row in rows)/len(rows)
            new = sum(row['new_'+suffix] for row in rows)/len(rows)
            item['mean_old_'+suffix], item['mean_new_'+suffix] = old, new
            item['new_over_old_'+suffix] = new/old
            item['observed_relative_reduction_'+suffix] = 1-new/old
        aggregates.append(item)
    warmups = []
    for item in data['paid_warmups']:
        run = item['run']
        # Warmups intentionally incur new columns; do not apply the measured
        # assert_warm predicate used by run_record above.
        assert len(run['evidence']['inherited']['observer_operations']) == run['total_actual_core_calls']
        warmups.append({'N': item['N'], 'a': item['a'],
            'core_call_interval': run['core_call_interval'],
            'actual_core_calls': run['total_actual_core_calls'],
            'counters_before_evidence': run['counters_before_evidence']})
        intervals.append(run['core_call_interval'])
    frontier = 0
    for start, stop in sorted(intervals):
        assert start == frontier
        frontier = stop
    assert frontier == len(calls)
    decomposition = {'actual_native_program_admission': admission[1]-admission[0],
        'one_shared_cold_SO_bank': cold['actual_core_calls'],
        'three_paid_modular_warmups': sum(item['actual_core_calls'] for item in warmups),
        'twelve_measured_fresh_Gram_engines': sum(run['total_actual_core_calls'] for run in all_runs),
        'standalone_token_derivation': 0}
    assert sum(decomposition.values()) == len(calls)

    table_rows = []
    for index, program in enumerate(data['program_final_table_instances']):
        for entry in program['table_instances']:
            cert = entry['evidence']
            table_rows.append({'program_index': index, 'N': program['N'], 'a': program['a'],
                'factory_index': entry['factory_index'], 'role': entry['role'],
                'b': cert['permutation']['b'], 'stats': cert['stats'],
                'permutation_sha256': cert['permutation_sha256'], 'certificate_sha256': sha(packed(cert))})
    table_totals = {key: sum(row['stats'][key] for row in table_rows) for key in
        ('setup_adder_digit_replays', 'column_adder_digit_replays',
         'setup_host_bit_wiring_operations', 'column_host_bit_wiring_operations',
         'setup_host_bit_length_calls_in_arithmetic', 'column_host_bit_length_calls_in_arithmetic',
         'computed_columns', 'column_requests', 'cache_hits')}
    table_totals['program_permutation_verification_digit_replays'] = sum(
        item['replayed_adder_digits'] for p in data['program_final_table_instances']
        for item in p['permutation_verifications'])
    result = {'schema': 'SEGMENTED_MATCHED_READONLY_COST_V1',
        'extractor_sha256': sha(Path(__file__).read_bytes()), 'source_hashes': data['source_hashes'],
        'raw_sha256': sha(raw), 'raw_bytes': len(raw), 'gzip_sha256': sha(compressed), 'gzip_bytes': len(compressed),
        'whole_elapsed_seconds_before_final_serialization': data['elapsed_seconds'],
        'wall_start_utc': data['wall_start_utc'], 'wall_before_serialization_utc': data['wall_before_serialization_utc'],
        'actual_native_core_calls': len(calls), 'core_call_decomposition': decomposition,
        'cold_SO_bank': {key: cold[key] for key in ('elapsed_seconds', 'actual_core_calls', 'call_interval')},
        'standalone_token_derivation': data['standalone_token_derivation'],
        'all_pairs': pairs, 'three_fixture_aggregates': aggregates, 'paid_warmups': warmups,
        'shared_program_table_instances': table_rows, 'shared_table_totals': table_totals,
        'unexpected_failed_execution_artifacts': [p.name for p in ROOT.glob('FAILED_EXECUTION_*.json.gz')],
        'scope': 'one predeclared six-pair run; no rerun, no sample selection; descriptive ratios only',
        'limits': ['No statistical confidence interval or independent-trials model.',
            'Parent/siblings reported a quiet scientific/I/O window; unrelated OS load was not monitored.',
            'Constructor includes source checks, bank check and fresh token derivation; nothing was subtracted.',
            'Through-evidence includes diagnostic gap; final deep copy/JSON/gzip excluded from measured windows.',
            'Token segment lengths measure payload only, not peak process memory.',
            'Cumulative typed-table costs counted once per actual instance.',
            'This bounded metadata binding improvement does not reduce native Gram work or prove general Shor efficiency.']}
    (ROOT/'SEGMENTED_MATCHED_COST_ACCOUNTING.json').write_bytes(packed(result)+b'\n')
    print(json.dumps({key: result[key] for key in ('core_call_decomposition', 'three_fixture_aggregates',
        'standalone_token_derivation', 'shared_table_totals')}, sort_keys=True))


if __name__ == '__main__':
    main()
