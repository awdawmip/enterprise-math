"""Read, verify and summarize frozen matched-prefix evidence; no native imports."""
from datetime import datetime, timezone
from pathlib import Path
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
RAW_SHA = '99694be587cfc2eacbe53ad2759a15f6d0d885b74c8b7ad85e1f5d27344176da'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def packed(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':')).encode()


def metadata(path):
    stat = path.stat()
    return {'path': str(path), 'bytes': stat.st_size,
        'creation_time_utc': datetime.fromtimestamp(stat.st_ctime, timezone.utc).isoformat(),
        'last_write_time_utc': datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat()}


def run_summary(run):
    counters = run['counters_before_evidence']
    evidence = run['evidence']['inherited']
    assert len(evidence['observer_operations']) == run['calculation_actual_core_calls']
    assert run['calculation_actual_core_calls'] == run['total_actual_core_calls']
    assert run['core_call_interval'][1]-run['core_call_interval'][0] == run['total_actual_core_calls']
    return {'implementation': run['implementation'],
        'calculation_seconds': run['calculation_seconds'],
        'evidence_capture_seconds': run['evidence_capture_seconds'],
        'counter_and_inventory_gap_seconds': run['counter_and_inventory_gap_seconds'],
        'total_seconds_through_evidence': run['total_seconds_through_evidence'],
        'core_call_interval': run['core_call_interval'], 'core_calls': run['total_actual_core_calls'],
        'native_phase_vector_applications': counters['gram']['native_phase_vector_applications'],
        'query_requests': counters['gram']['query_requests'],
        'distinct_matrices': len(evidence['correlations']),
        'cached_matrix_scalar_slots': evidence['report']['cached_matrix_scalar_slots'],
        'observer_operations': len(evidence['observer_operations']),
        'accepted_omissions': counters['policy']['accepted_omissions'],
        'bank_checks_before_evidence': counters['policy']['certificate_binding_checks'],
        'guard_stats_before_evidence': counters['guard']['stats']}


def main():
    compressed = (ROOT/'SO_TRACE_MATCHED_PREFIX_RESULTS.json.gz').read_bytes()
    raw = gzip.decompress(compressed)
    assert sha(raw) == RAW_SHA
    record = json.loads(raw)
    assert record['status'] == 'PASSED'
    for path, expected in record['source_hashes'].items():
        assert sha(Path(path).read_bytes()) == expected
    calls = record['actual_native_core_calls']
    assert len(calls) == record['actual_native_core_call_count']
    intervals = [record['native_admission_call_interval']]
    cold = []
    for item in record['separate_cold_banks']:
        setup = item['evidence']['setup']
        first, last = item['call_interval']
        assert calls[first:last] == setup['actual_core_calls']
        assert item['actual_core_calls'] == setup['core_call_count'] == last-first
        cold.append({'label': item['label'], 'call_interval': [first, last],
            'core_calls': item['actual_core_calls'], 'elapsed_seconds': item['elapsed_seconds'],
            'logical_serialized_bytes': setup['logical_serialized_bytes'],
            'stored_complete_column_scalar_entries': setup['stored_complete_column_scalar_entries']})
        intervals.append([first, last])
    warmups, pairs = [], []
    for item in record['paid_warmups']:
        summary = run_summary(item['run'])
        warmups.append({'N': item['N'], 'a': item['a'], 'run': summary})
        intervals.append(summary['core_call_interval'])
    for pair in record['pairs']:
        summaries = [run_summary(run) for run in pair['runs']]
        for summary in summaries:
            intervals.append(summary['core_call_interval'])
        old = next(run for run in pair['runs'] if run['implementation'] == 'BoundaryCheckedUniform')
        new = next(run for run in pair['runs'] if run['implementation'] == 'BoundaryCheckedSOTrace')
        assert old['plans'] == new['plans'] and old['numeric_ledger'] == new['numeric_ledger']
        for field in ('correlations', 'observer_operations'):
            assert old['evidence']['inherited'][field] == new['evidence']['inherited'][field]
        for run in pair['runs']:
            before, after = run['table_instances_before'], run['table_instances_after']
            assert len(before) == len(after)
            for left, right in zip(before, after):
                assert (left['role'],left['parent_factory_index']) == (right['role'],right['parent_factory_index'])
                for key in ('computed_columns', 'column_adder_digit_replays'):
                    assert left['stats'][key] == right['stats'][key]
        pairs.append({'summary': pair['summary'], 'runs': summaries,
            'new_over_old_calculation_ratio': new['calculation_seconds']/old['calculation_seconds'],
            'new_minus_old_calculation_seconds': new['calculation_seconds']-old['calculation_seconds']})
    intervals.sort()
    assert intervals[0][0] == 0 and intervals[-1][1] == len(calls)
    assert all(left[1] == right[0] for left,right in zip(intervals, intervals[1:]))
    grouped = []
    for N,a in ((21,2),(21,4),(65,3)):
        selected = [pair for pair in pairs if (pair['summary']['N'],pair['summary']['a']) == (N,a)]
        assert len(selected) == 2
        old_times = [pair['summary']['old_seconds'] for pair in selected]
        new_times = [pair['summary']['new_seconds'] for pair in selected]
        grouped.append({'N':N,'a':a,'old_calculation_seconds':old_times,'new_calculation_seconds':new_times,
            'old_mean_seconds':sum(old_times)/2,'new_mean_seconds':sum(new_times)/2,
            'ratio_of_two_pair_means':sum(new_times)/sum(old_times),
            'both_new_runs_slower':all(new>old for old,new in zip(old_times,new_times))})
    instances = []
    for index, program in enumerate(record['programs']):
        for j, table in enumerate(program['factory_tables']):
            instances.append({'program_index':index,'N':program['N'],'a':program['a'],
                'role':'factory','parent_factory_index':j,'stats':table['stats']})
        for inverse in program['inverse_tables']:
            instances.append({'program_index':index,'N':program['N'],'a':program['a'],
                'role':'inverse','parent_factory_index':inverse['parent_factory_index'],
                'stats':inverse['certificate']['stats']})
    table_totals = {key:sum(item['stats'][key] for item in instances) for key in (
        'setup_adder_digit_replays','column_adder_digit_replays','computed_columns','column_requests','cache_hits')}
    table_totals['permutation_verification_digit_replays'] = sum(
        item['replayed_adder_digits'] for program in record['programs']
        for item in program['permutation_verifications'])
    admission = record['native_admission_call_interval']
    decomposition = {'initial_native_program_admission':admission[1]-admission[0],
        'old_cold_bank':cold[0]['core_calls'],'new_cold_bank':cold[1]['core_calls'],
        'paid_warmups':sum(item['run']['core_calls'] for item in warmups),
        'twelve_measured_engines':sum(run['core_calls'] for pair in pairs for run in pair['runs'])}
    assert sum(decomposition.values()) == len(calls)
    sibling_summary = ROOT.parents[1]/'sep27-qft-signedgap/signed_gap/ONE_WINDOW_SUMMARY.json'
    timing_metadata = [metadata(ROOT/'SO_TRACE_MATCHED_EXECUTION_LOG.txt'),
                       metadata(ROOT/'SO_TRACE_MATCHED_PREFIX_SUMMARY.json')]
    if sibling_summary.exists():
        timing_metadata.append(metadata(sibling_summary))
    result = {'schema':'SO_TRACE_MATCHED_PREFIX_OFFLINE_ACCOUNTING_V1',
        'extractor_sha256':sha(Path(__file__).read_bytes()),'raw_sha256':sha(raw),
        'gzip_sha256':sha(compressed),'source_hashes':record['source_hashes'],
        'whole_checker':{'core_calls':len(calls),'elapsed_seconds':record['elapsed_seconds'],
            'decomposition':decomposition},'cold_banks':cold,'paid_warmups':warmups,
        'pairs':pairs,'grouped_descriptive_times':grouped,
        'program_table_instances':instances,'shared_table_totals':table_totals,
        'filesystem_timing_metadata':timing_metadata,
        'interference_note':'The already-started run was retained. The sibling one-window raw/summary '
            'last writes were around 05:03:33 UTC, overlapping the beginning of this run. '
            'No controlled isolation or per-phase UTC timestamps were recorded; the overlap cannot '
            'be quantitatively attributed to a policy. The sibling reported no later large-file reading '
            'until this run completed. No rerun or result selection was performed.',
        'limitations':['Only two alternating paired orders per fixed fixture; no random independent trials.',
            'New bank checks use stricter host serialization; timings do not isolate its causal cost.',
            'Cold banks run sequentially once and are outside the warm comparison.',
            'Full Gram matrices, signed residuals, and actual observer streams are retained.',
            'Shared table snapshots counted by explicit instance role; never charged once per route.',
            'No complete host bit-cost, RSS, primitive-loop count, asymptotic or overall factorization speed claim.'],
        'unexpected_failed_execution_artifacts':[path.name for path in ROOT.glob('FAILED_EXECUTION_*.json.gz')]}
    (ROOT/'SO_TRACE_MATCHED_COST_ACCOUNTING.json').write_bytes(packed(result)+b'\n')
    print(json.dumps({'whole_checker':result['whole_checker'], 'groups':grouped,
                      'table_instances':len(instances),'table_totals':table_totals},sort_keys=True))


if __name__ == '__main__':
    main()
