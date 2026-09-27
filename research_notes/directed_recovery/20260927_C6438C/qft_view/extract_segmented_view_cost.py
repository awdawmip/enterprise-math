"""Pure readback/accounting; deliberately imports no native/scientific module."""
from pathlib import Path
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
RAW_SHA = '12f5528102c5c6f84ff35d2fa6bef1c601ccb09111129365114a67622b4cfbf3'


def sha(value):
    return hashlib.sha256(value).hexdigest()


def encode(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False,
                      allow_nan=False).encode('utf-8')


def execution(label, evidence):
    inherited, guard = evidence['inherited'], evidence['boundary_guard']
    report, operations = inherited['report'], inherited['observer_operations']
    assert len(operations) == report['actual_positive_path_observations']
    assert guard['active_depth'] == 0 and guard['owner_active'] is False
    result = {'label': label, 'history': report['history'],
        'native_phase_vector_applications': report['native_phase_vector_applications'],
        'query_requests': report['query_requests'], 'distinct_queries': report['distinct_queries'],
        'cached_matrix_scalar_slots': report['cached_matrix_scalar_slots'],
        'peak_cached_matrix_scalar_slots': report['peak_cached_matrix_scalar_slots'],
        'max_correlation_numerator_bits': report['max_correlation_numerator_bits'],
        'max_correlation_denominator_bits': report['max_correlation_denominator_bits'],
        'positive_path_observations': len(operations),
        'observer_graph_states_sum': sum(op['states'] for op in operations),
        'policy_stats_at_snapshot': evidence['policy_stats'],
        'guard_stats_at_snapshot': guard['stats']}
    if 'view_stats' in guard:
        result.update({'view_stats_at_snapshot': guard['view_stats'],
            'segment_bytes': guard['segment_bytes'],
            'persistent_segment_payload_bytes': sum(guard['segment_bytes']),
            'actual_frozen_bank_check_invocations': guard['frozen_bank_check_invocations']})
    else:
        result['actual_frozen_bank_check_invocations'] = guard['stats']['bank_check_attempts']
    return result


def main():
    compressed = (ROOT/'SEGMENTED_VIEW_RESULTS.json.gz').read_bytes()
    raw = gzip.decompress(compressed)
    assert sha(raw) == RAW_SHA
    data = json.loads(raw)
    summary = json.loads((ROOT/'SEGMENTED_VIEW_SUMMARY.json').read_bytes())
    assert data['status'] == summary['status'] == 'PASSED'
    assert summary['raw_sha256'] == sha(raw) and summary['gzip_sha256'] == sha(compressed)
    for path, expected in data['source_hashes'].items():
        assert sha(Path(path).read_bytes()) == expected
    assert sha((ROOT/'STARTUP_GUARD.json').read_bytes()) == data['startup_guard_sha256']
    calls = data['actual_core_calls']
    assert len(calls) == data['core_call_count']
    start, admitted = data['initial_program_admission_call_interval']
    assert start == 0  # saved intervals are absolute CALLS offsets in this run
    cold = data['unchanged_cold_SO_bank']['setup']
    left, right = cold['call_interval']
    assert calls[left:right] == cold['actual_core_calls']
    assert right-left == cold['core_call_count'] == 36

    unique, fixtures = [], []
    for index, fixture in enumerate(data['fixtures']):
        routes = {}
        for route in ('old_SO_boundary', 'segmented_boundary'):
            item = execution(f'fixture{index}:{route}', fixture[route])
            routes[route] = item; unique.append(item)
        assert fixture['same_native_and_policy_counters']
        assert fixture['same_complete_saved_covariances_and_observer_streams']
        assert routes['old_SO_boundary']['guard_stats_at_snapshot'] == routes['segmented_boundary']['guard_stats_at_snapshot']
        assert sum(item['positive_path_observations'] for item in routes.values()) == (
            fixture['call_interval'][1]-fixture['call_interval'][0])
        fixtures.append({'N': fixture['N'], 'a': fixture['a'], 'history': fixture['history'],
            'routes': routes, 'whole_observer_and_correlation_equality_checked': True})

    resume = {name: execution('restore:'+name, value) for name, value in
              data['pending_restore'].items() if name in
              ('pending_snapshot', 'after_runtime_rejections', 'original', 'restored')}
    unique.extend(resume[name] for name in ('original', 'restored'))
    negatives = []
    for category in ('runtime_negative_controls', 'cursor_negative_controls'):
        for item in data[category]:
            row = {key: item[key] for key in ('case', 'reason', 'actual_core_calls', 'call_interval')}
            row['category'] = category
            if item['failed_replay_evidence'] is not None:
                replay = execution('failed:'+item['case'], item['failed_replay_evidence'])
                assert replay['positive_path_observations'] == item['actual_core_calls']
                row['fresh_replay'] = replay; unique.append(replay)
            else:
                row['fresh_replay'] = None
            if item['guard_after'] is not None:
                row['guard_after'] = item['guard_after']
                assert item['guard_after']['active_depth'] == 0 and not item['guard_after']['owner_active']
            if category == 'runtime_negative_controls':
                assert item['actual_core_calls'] == 0 and item['zero_new_observer_when_required']
            negatives.append(row)
    retry = {name: execution('retry:'+name, data['budget_recovery'][name])
             for name in ('failed_attempt', 'retried', 'fresh')}
    unique.extend(retry[name] for name in ('retried', 'fresh'))
    prefix = data['budget_recovery']['failed_attempt']['inherited']['observer_operations']
    assert prefix == data['budget_recovery']['retried']['inherited']['observer_operations'][:len(prefix)]

    decomposition = {'actual_native_program_admission': admitted-start,
        'unchanged_cold_SO_bank': cold['core_call_count'],
        'four_fixed_prefix_engine_objects': sum(route['positive_path_observations']
            for fixture in fixtures for route in fixture['routes'].values()),
        'restore_original_and_replayed_objects': sum(resume[name]['positive_path_observations']
            for name in ('original', 'restored')),
        'cursor_negative_fresh_replays': sum(item['actual_core_calls'] for item in negatives),
        'interrupted_retried_plus_fresh_object': sum(retry[name]['positive_path_observations']
            for name in ('retried', 'fresh'))}
    assert sum(decomposition.values()) == len(calls)
    segmented = [item for item in unique if 'view_stats_at_snapshot' in item]
    view_totals = {key: sum(item['view_stats_at_snapshot'][key] for item in segmented)
                   for key in segmented[0]['view_stats_at_snapshot']}
    # Final captured snapshots cover all successful outer calls. Pre-identity
    # and metadata rejects on the original restore object remain in its totals.
    assert view_totals['segmented_check_attempts'] == (
        view_totals['fast_accepts']+view_totals['compatibility_checks'])
    assert view_totals['compatibility_checks'] == (
        view_totals['compatibility_accepts']+view_totals['compatibility_rejections'])

    table_rows = []
    for index, program in enumerate(data['program_final_table_instances']):
        identities = set()
        for entry in program['table_instances']:
            identity = (entry['factory_index'], entry['role'])
            assert identity not in identities; identities.add(identity)
            table = entry['evidence']
            table_rows.append({'program_index': index, 'N': program['N'], 'a': program['a'],
                'factory_index': entry['factory_index'], 'role': entry['role'],
                'b': table['permutation']['b'], 'permutation_sha256': table['permutation_sha256'],
                'stats': table['stats'], 'snapshot_sha256': sha(encode(table))})
    table_totals = {key: sum(row['stats'][key] for row in table_rows) for key in
        ('setup_adder_digit_replays', 'column_adder_digit_replays',
         'setup_host_bit_wiring_operations', 'column_host_bit_wiring_operations',
         'setup_host_bit_length_calls_in_arithmetic', 'column_host_bit_length_calls_in_arithmetic',
         'computed_columns', 'column_requests', 'cache_hits')}
    table_totals['program_permutation_verification_digit_replays'] = sum(
        check['replayed_adder_digits'] for program in data['program_final_table_instances']
        for check in program['permutation_verifications'])
    output = {'schema': 'SEGMENTED_VIEW_READONLY_COST_ACCOUNTING_V1',
        'extractor_sha256': sha(Path(__file__).read_bytes()), 'source_hashes': data['source_hashes'],
        'raw_sha256': sha(raw), 'raw_bytes': len(raw), 'gzip_sha256': sha(compressed),
        'gzip_bytes': len(compressed), 'elapsed_seconds_whole_checker_before_final_compression': data['elapsed_seconds'],
        'actual_core_calls': len(calls), 'core_call_decomposition': decomposition,
        'cold_bank': {'actual_observers': cold['core_call_count'], 'elapsed_seconds': cold['elapsed_seconds'],
            'basis_actions_lower_bound': 183*len(cold['word_setups']),
            'logical_serialized_bytes': cold['logical_serialized_bytes'],
            'word_setups': cold['word_setups']},
        'fixed_prefix_comparisons': fixtures, 'pending_restore': resume,
        'negative_controls': negatives, 'budget_retry': retry,
        'nonoverlapping_engine_snapshots': unique, 'segmented_engine_objects': len(segmented),
        'segmented_view_counter_totals_at_final_snapshots': view_totals,
        'actual_frozen_check_invocations_on_segmented_objects': sum(
            item['actual_frozen_bank_check_invocations'] for item in segmented),
        'three_segment_bytes_per_object': segmented[0]['segment_bytes'],
        'segment_payload_bytes_per_object': segmented[0]['persistent_segment_payload_bytes'],
        'pure_metadata_examples': data['metadata_predicate_checks'],
        'shared_program_table_instances': table_rows, 'shared_table_totals': table_totals,
        'unexpected_failure_artifacts': [path.name for path in ROOT.glob('FAILED_EXECUTION_*.json.gz')],
        'limits': [
            'This is fixed-prefix correctness, not a timing comparison or independent stochastic trials.',
            'Pending and after-rejection snapshots overlap original; failed_attempt overlaps retried.',
            'Shared factory and inverse instances are counted once, not once per engine or repeated evidence.',
            'All real compatibility invocations here reject; compatibility acceptance is a pure JSON example.',
            'Token byte count is retained segment payload only, excluding object/allocator/transient overhead.',
            'The failure collector was compiled and inspected; no unexpected-failure injection was executed.',
            'No total host bit complexity, process peak RSS, or metadata stage timing is measured.']}
    (ROOT/'SEGMENTED_VIEW_COST_ACCOUNTING.json').write_bytes(encode(output)+b'\n')
    print(json.dumps({key: output[key] for key in ('core_call_decomposition', 'segmented_engine_objects',
        'segmented_view_counter_totals_at_final_snapshots', 'actual_frozen_check_invocations_on_segmented_objects',
        'three_segment_bytes_per_object', 'segment_payload_bytes_per_object', 'shared_table_totals')}, sort_keys=True))


if __name__ == '__main__':
    main()
