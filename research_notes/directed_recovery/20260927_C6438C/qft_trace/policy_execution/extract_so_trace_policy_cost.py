"""Read-only accounting of existing evidence; no scientific/native imports."""
from pathlib import Path
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parents[1]
RAW_SHA = 'a677ebc559534e9b9aa469e69ffce0615290de1f289b257a5ccc947083c07280'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def packed(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':')).encode()


def execution(label, evidence):
    report = evidence['inherited']['report']
    operations = evidence['inherited']['observer_operations']
    assert len(operations) == report['actual_positive_path_observations']
    guard = evidence['boundary_guard']
    assert guard['active_depth'] == 0 and guard['owner_active'] is False
    return {'label': label, 'history': report['history'],
        'query_requests': report['query_requests'],
        'distinct_queries': report['distinct_queries'],
        'native_phase_vector_applications': report['native_phase_vector_applications'],
        'actual_positive_path_observations': len(operations),
        'observer_graph_states_sum': sum(op['states'] for op in operations),
        'cached_matrix_scalar_slots': report['cached_matrix_scalar_slots'],
        'peak_cached_matrix_scalar_slots': report['peak_cached_matrix_scalar_slots'],
        'max_correlation_numerator_bits': report['max_correlation_numerator_bits'],
        'max_correlation_denominator_bits': report['max_correlation_denominator_bits'],
        'policy_stats_at_snapshot': evidence['policy_stats'],
        'guard_stats_at_snapshot': guard['stats'],
        'cumulative_table_report_not_added_to_execution_totals': True}


def bank(label, evidence, all_calls):
    setup = evidence['setup']
    start, stop = setup['call_interval']
    assert all_calls[start:stop] == setup['actual_core_calls']
    words = evidence['logical']['words']
    ops = [op for word in words.values() for op in word['observer_operations']]
    assert len(ops) == setup['core_call_count'] == stop-start
    return {'label': label, 'call_interval': [start, stop],
        'native_core_calls': setup['core_call_count'],
        'observer_operations': len(ops),
        'elapsed_seconds': setup['elapsed_seconds'],
        'observer_graph_states_sum': sum(op['states'] for op in ops),
        'logical_serialized_bytes': setup['logical_serialized_bytes'],
        'stored_complete_column_scalar_entries': setup['stored_complete_column_scalar_entries'],
        'stored_trace_nodes': setup.get('stored_trace_nodes'),
        'stored_full_matrix_scalar_entries': setup.get('stored_full_matrix_scalar_entries'),
        'mandatory_first_replay_basis_actions_lower_bound': 183*len(words),
        'word_setups': setup['word_setups']}


def main():
    compressed = (ROOT/'SO_TRACE_POLICY_RESULTS.json.gz').read_bytes()
    raw = gzip.decompress(compressed)
    assert sha(raw) == RAW_SHA
    data = json.loads(raw)
    paths = {'check_so_trace_policy.py': ROOT/'check_so_trace_policy.py',
        'so_trace_feedback.py': ROOT/'so_trace_feedback.py',
        'so_trace_certificates.py': ROOT.parent/'trace_bank/so_trace_certificates.py',
        'boundary_uniform.py': BASE/'sep27-qft-boundary/boundary_execution/boundary_uniform.py'}
    for name, expected in data['source_hashes'].items():
        assert sha(paths[name].read_bytes()) == expected
    assert data['status'] == 'PASSED'
    all_calls = data['actual_core_calls']
    assert len(all_calls) == data['core_call_count']

    fixtures, all_snapshots = [], []
    for program_index, fixture in enumerate(data['fixtures']):
        routes = {}
        for route in ('old_boundary', 'so_boundary'):
            evidence = fixture[route]
            label = f'program{program_index}:{route}'
            routes[route] = execution(label, evidence)
            all_snapshots.append((program_index, label, evidence))
        fixtures.append({'N': fixture['N'], 'a': fixture['a'], 'history': fixture['history'],
            'routes': routes, 'observer_streams_equal': fixture['entire_policy_gram_observer_stream_equal'],
            'all_retained_covariances_equal': fixture['all_retained_covariances_equal'],
            'post_snapshot_public_cursor_checks_per_route': 1})

    resume = {}
    for name in ('pending_snapshot', 'original', 'restored'):
        evidence = data['pending_restore'][name]
        resume[name] = execution('resume:'+name, evidence)
        all_snapshots.append((0, 'resume:'+name, evidence))
    negatives = []
    for item in data['cursor_negative_controls']+data['new_exact_bank_type_controls']:
        record = {k: item[k] for k in ('case', 'actual_core_calls', 'call_interval', 'reason')}
        evidence = item['failed_replay_evidence']
        record['replay'] = None if evidence is None else execution('failed:'+item['case'], evidence)
        if evidence is not None:
            assert record['replay']['actual_positive_path_observations'] == item['actual_core_calls']
            all_snapshots.append((0, 'failed:'+item['case'], evidence))
        negatives.append(record)
    retry = {}
    for name in ('failed_attempt', 'retried', 'fresh'):
        evidence = data['budget_recovery'][name]
        retry[name] = execution('retry:'+name, evidence)
        all_snapshots.append((0, 'retry:'+name, evidence))
    before, after = data['budget_recovery']['failed_attempt'], data['budget_recovery']['retried']
    before_ops = before['inherited']['observer_operations']
    assert before_ops == after['inherited']['observer_operations'][:len(before_ops)]
    retry['new_observers_after_interruption'] = (
        retry['retried']['actual_positive_path_observations']-
        retry['failed_attempt']['actual_positive_path_observations'])

    cold = [bank(name, data[name], all_calls) for name in ('old_cold_bank', 'new_cold_bank')]
    admission_start, admission_stop = data['initial_program_admission_call_interval']
    assert admission_start == 0
    decomposition = {'native_bank_and_program_admission': admission_stop-admission_start,
        'old_cold_bank': cold[0]['native_core_calls'], 'new_cold_bank': cold[1]['native_core_calls'],
        'four_matched_prefix_execution_objects': sum(
            route['actual_positive_path_observations'] for item in fixtures for route in item['routes'].values()),
        'restore_original_and_fresh_replay': resume['original']['actual_positive_path_observations']+
            resume['restored']['actual_positive_path_observations'],
        'negative_control_replays': sum(item['actual_core_calls'] for item in negatives),
        'interrupted_then_retried_plus_fresh_comparator': retry['retried']['actual_positive_path_observations']+
            retry['fresh']['actual_positive_path_observations']}
    assert sum(decomposition.values()) == data['core_call_count']

    # Instance identities are derived from the pinned constructor: one factory
    # table per program/b, and one distinct cached inverse object per factory
    # table. A factory and an inverse remain different even with identical b.
    # We never merge same-N/b instances across programs or these two roles.
    instances = {}
    def retain(identity, label, table):
        previous = instances.get(identity)
        if previous is None or table['stats']['column_requests'] >= previous['table']['stats']['column_requests']:
            chosen, other = (label, table), previous
        else:
            chosen, other = (previous['snapshot'], previous['table']), {'table': table}
        if other is not None:
            for key, value in other['table']['stats'].items():
                if type(value) is int:
                    assert chosen[1]['stats'][key] >= value, (identity, key)
        instances[identity] = {'snapshot': chosen[0], 'table': chosen[1]}

    for index, program in enumerate(data['program_final_tables']):
        for j, table in enumerate(program['factory_tables']):
            retain((index, 'factory', j), 'program_final_tables', table)
    for program_index, label, evidence in all_snapshots:
        factories = data['program_final_tables'][program_index]['factory_tables']
        tables = evidence['inherited']['typed_modular_certificates']
        assert len(tables) >= len(factories)
        for j, table in enumerate(tables[:len(factories)]):
            assert table['permutation_sha256'] == factories[j]['permutation_sha256']
            retain((program_index, 'factory', j), label, table)
        for table in tables[len(factories):]:
            owners = [j for j, parent in enumerate(factories) if
                parent['permutation']['inverse_certificate']['inverse_multiplier'] == table['permutation']['b']]
            assert len(owners) == 1
            retain((program_index, 'inverse', owners[0]), label, table)
    instance_rows = []
    for identity, selected in sorted(instances.items()):
        table = selected['table']
        instance_rows.append({'program_index': identity[0], 'role': identity[1],
            'parent_factory_index': identity[2], 'snapshot': selected['snapshot'],
            'N': table['permutation']['N'], 'b': table['permutation']['b'],
            'permutation_sha256': table['permutation_sha256'], 'stats': table['stats'],
            'complete_snapshot_sha256': sha(packed(table))})
    table_totals = {key: sum(row['stats'][key] for row in instance_rows) for key in (
        'setup_adder_digit_replays', 'column_adder_digit_replays',
        'setup_host_bit_wiring_operations', 'column_host_bit_wiring_operations',
        'setup_host_bit_length_calls_in_arithmetic', 'column_host_bit_length_calls_in_arithmetic',
        'computed_columns', 'column_requests', 'cache_hits')}
    table_totals['program_permutation_verification_digit_replays'] = sum(
        verification['replayed_adder_digits'] for program in data['program_final_tables']
        for verification in program['permutation_verifications'])
    result = {'schema': 'SO_TRACE_POLICY_READONLY_COST_ACCOUNTING_V1',
        'extractor_sha256': sha(Path(__file__).read_bytes()), 'source_hashes': data['source_hashes'],
        'raw_sha256': sha(raw), 'gzip_sha256': sha(compressed),
        'whole_checker': {'native_core_calls': data['core_call_count'],
            'elapsed_seconds': data['elapsed_seconds'], 'core_call_decomposition': decomposition},
        'cold_banks': cold, 'fixed_prefix_comparisons': fixtures,
        'pending_restore': resume, 'negative_controls': negatives, 'budget_retry': retry,
        'shared_program_table_instances': instance_rows, 'shared_table_totals': table_totals,
        'accounting_boundaries': [
            'The two fixed positive histories are neither random independent trials nor full-law enumeration.',
            'Initial program admission and cold banks are paid separately from prefix work.',
            'Cold bank elapsed observations are sequential one-offs, not a matched performance benchmark.',
            'The exact-type SO bank performs strict host metadata serialization; no warm speedup was measured.',
            'Pending snapshot overlaps original; failed_attempt overlaps retried. Neither is added twice.',
            'Fixture snapshots exclude one later public cursor check per route; guard counts are labelled snapshots.',
            'Tables are shared across old/new routes and replays. Factory and inverse instances are charged once.',
            'Inverse identity uses the pinned inverse-cache construction, not equality of certificate contents.',
            'Native primitive cache was warm during complete bank replay; zero new kernel calls is not zero loop cost.',
            'Complete host bit complexity, primitive loop work, peak RSS and total metadata serialization work were not measured.'],
        'unexpected_failed_execution_artifacts': [path.name for path in ROOT.glob('FAILED_EXECUTION_*.json.gz')]}
    (ROOT/'SO_TRACE_POLICY_COST_ACCOUNTING.json').write_bytes(packed(result)+b'\n')
    print(json.dumps({'whole_checker': result['whole_checker'], 'shared_table_totals': table_totals,
                      'table_instances': len(instance_rows)}, sort_keys=True))


if __name__ == '__main__':
    main()
