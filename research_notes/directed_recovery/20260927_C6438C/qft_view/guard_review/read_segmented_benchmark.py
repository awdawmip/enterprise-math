"""Pure-I/O review of the frozen six-pair benchmark; never imports science.

Re-encodes saved records, compares all saved matrix entries/observer records,
and accounts for recorded timing/call metadata. It does not replay arithmetic.
"""
from collections import Counter
from datetime import datetime
from pathlib import Path
import gzip
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'prefix_comparison'
RAW_SHA = '461f1c84cafdee8b8d38ae9577f4d9a6472737d9f292aef9c7fdf606921fc80d'
GZIP_SHA = '2d19cac21d4f18f885b161d06bbf16e686b733a71c4cea95b140641eccd83ba3'
OLD, NEW = 'BoundaryCheckedSOTrace', 'SegmentedBoundarySOTrace'


def packed(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'),
                      ensure_ascii=False, allow_nan=False).encode('utf-8')


def sha(x):
    return hashlib.sha256(x).hexdigest()


def unique_object(pairs):
    answer = {}
    for k, v in pairs:
        if k in answer:
            raise ValueError('duplicate JSON key: ' + k)
        answer[k] = v
    return answer


def decode(b):
    return json.loads(b, object_pairs_hook=unique_object,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def same(a, b):
    # Canonical JSON equality preserves bool/int and string/number distinctions.
    assert packed(a) == packed(b)


def positive_recorded_rational(s):
    # Only checks the sign of a recorded mass; never evaluates a scientific law.
    n, separator, d = s.partition('/')
    assert int(n) > 0 and (not separator or int(d) > 0)


def run_check(run, calls, measured):
    start, stop = run['core_call_interval']
    assert type(start) is int and type(stop) is int and 0 <= start < stop <= len(calls)
    inherited = run['evidence']['inherited']
    ops = inherited['observer_operations']
    assert len(ops) == stop-start == run['total_actual_core_calls'] == run['calculation_actual_core_calls']
    for op, call in zip(ops, calls[start:stop]):
        same([op['kernel'], op['states'], op['depth']],
             [call['entrypoint'], call['states'], call['depth']])
    assert run['history'] == [1, 0, 0, 0]
    assert len(run['plans']) == len(run['numeric_ledger']) == 4
    positive_recorded_rational(run['terminal_mass'])
    correlations = inherited['correlations']
    assert len(correlations) == inherited['report']['distinct_queries']
    keys = [(c['depth'], c['residue']) for c in correlations]
    assert len(set(keys)) == len(keys)
    for c in correlations:
        assert type(c['denominator']) is int and c['denominator'] > 0
        assert len(c['numerator_rows']) == 6
        assert all(len(row) == 6 and all(type(v) is int for v in row)
                   for row in c['numerator_rows'])
    before, after = run['table_instances_before'], run['table_instances_after']
    ids = lambda rows: [(x['parent_factory_index'], x['role']) for x in rows]
    if measured:
        same(ids(before), ids(after))
        assert len(ids(before)) == len(set(ids(before)))
        for x, y in zip(before, after):
            for field in ('computed_columns', 'column_adder_digit_replays',
                          'setup_adder_digit_replays', 'column_host_bit_wiring_operations',
                          'column_host_bit_length_calls_in_arithmetic'):
                same(x['stats'][field], y['stats'][field])
    for field in ('calculation_seconds', 'evidence_capture_seconds',
                  'total_seconds_through_evidence', 'counter_inventory_and_UTC_gap_seconds'):
        assert type(run[field]) in (int, float) and math.isfinite(run[field]) and run[field] >= 0
    assert abs(run['total_seconds_through_evidence'] - run['calculation_seconds']
               - run['evidence_capture_seconds'] - run['counter_inventory_and_UTC_gap_seconds']) < 1e-12
    stamps = [datetime.fromisoformat(run[k]) for k in
              ('wall_started_utc', 'wall_calculation_end_utc', 'wall_evidence_end_utc')]
    assert stamps == sorted(stamps)
    # UTC includes a small timestamp gap; perf_counter is the actual timer.
    assert abs((stamps[1]-stamps[0]).total_seconds()-run['calculation_seconds']) < .01
    assert abs((stamps[2]-stamps[0]).total_seconds()-run['total_seconds_through_evidence']) < .01
    final_guard = run['evidence']['boundary_guard']
    assert final_guard['active_depth'] == 0 and final_guard['owner_active'] is False
    assert final_guard['stats']['bank_check_attempts'] == 7
    assert final_guard['stats']['exception_events'] == []
    return {'label': run['label'], 'core_call_interval': [start, stop],
            'native_calls': stop-start, 'correlation_matrices': len(correlations),
            'matrix_scalar_entries_compared': 36*len(correlations),
            'observer_records': len(ops), 'correlations_sha256': sha(packed(correlations)),
            'observers_sha256': sha(packed(ops)), 'plans_sha256': sha(packed(run['plans'])),
            'numeric_ledger_sha256': sha(packed(run['numeric_ledger'])),
            'calculation_seconds': run['calculation_seconds'],
            'evidence_seconds': run['evidence_capture_seconds'],
            'through_evidence_seconds': run['total_seconds_through_evidence'],
            'diagnostic_gap_seconds': run['counter_inventory_and_UTC_gap_seconds'],
            'wall_start_utc': run['wall_started_utc'], 'wall_end_utc': run['wall_evidence_end_utc']}


def token_check(data):
    """Reassemble existing saved fields only: no multiplication/application."""
    bank = data['shared_cold_SO_bank']['evidence']
    logical = bank['logical']
    assert sha(packed(logical)) == bank['binding_sha256']
    rows = []
    for key, word in logical['words'].items():
        binding, codec = word['native_binding'], word['exact_codec']
        same(binding, logical['phase_bindings'][key])
        assert codec['full_forward_inverse_blocks_and_identity_complement_checked'] is True
        # These are exactly the fields of frozen RestrictedNativeWord and
        # _program_view; its three missing optional attributes are None.
        rows.append([int(key), 6, word['denominator'], binding['word'],
                     codec['forward_columns'], codec['inverse_columns'],
                     binding['H4_count'], binding['sign_count'], binding['swap_count'],
                     None, binding['actual_complete_columns_sha256'], None, None])
    rows.sort()
    view = {'native_fields': [61, 6, [61, list(range(6))], rows],
            'phase_bindings': logical['phase_bindings'], 'codec_binding': logical['codec_binding']}
    segments = [packed(view[key]) for key in ('native_fields', 'phase_bindings', 'codec_binding')]
    receipt = data['standalone_token_derivation']
    same([len(x) for x in segments], receipt['segment_bytes'])
    assert sum(map(len, segments)) == receipt['segment_payload_bytes'] == 707035
    assert len(packed(view)) == receipt['existing_admitted_view_bytes'] == 707088
    sources = data['source_hashes']
    names = ('so_trace_feedback.py', 'so_trace_certificates.py', 'word_certificates.py')
    adapter = sources[str(ROOT/'segmented_so_view.py')]
    payload = {'profile': 'SEGMENTED_STRICT_SO_VIEW_WITH_FROZEN_FALLBACK_V1',
               'bank_binding_sha256': bank['binding_sha256'], 'adapter_source_sha256': adapter,
               'source_pins': {Path(k).name: v for k, v in sources.items() if Path(k).name in names},
               'segments': [x.decode('utf-8') for x in segments]}
    assert sha(packed(payload)) == receipt['token_sha256']
    assert receipt['actual_core_calls'] == 0
    return {'segment_bytes': list(map(len, segments)), 'segment_payload_bytes': 707035,
            'admitted_wrapper_bytes': 707088, 'token_sha256': sha(packed(payload)),
            'all_three_segments_reconstructed_from_saved_records': True,
            'claim': 'encoded payload lengths, not RSS or allocator/peak memory'}


def main():
    blob = (DATA/'SEGMENTED_MATCHED_RESULTS.json.gz').read_bytes()
    raw = gzip.decompress(blob)
    assert sha(blob) == GZIP_SHA and sha(raw) == RAW_SHA
    data = decode(raw)
    summary = decode((DATA/'SEGMENTED_MATCHED_SUMMARY.json').read_bytes())
    assert data['status'] == summary['status'] == 'PASSED'
    assert len(blob) == summary['gzip_bytes'] == 733837
    assert len(raw) == summary['raw_bytes'] == 16546526
    assert summary['gzip_sha256'] == GZIP_SHA and summary['raw_sha256'] == RAW_SHA
    same(data['source_hashes'], summary['source_hashes'])
    for path, expected in data['source_hashes'].items():
        assert sha(Path(path).read_bytes()) == expected
    codec_path = ROOT.parent/'sep26-shor-general/optimization/carrier_codec/carrier_codec.py'
    codec_sha = 'c25149e0ab4ce92a59d2ca40cb697fe6505cd1dc8d406e9c5a2d92cb2b28c953'
    assert sha(codec_path.read_bytes()) == codec_sha
    guard_bytes = (ROOT/'STARTUP_GUARD.json').read_bytes()
    assert sha(guard_bytes) == data['startup_guard']['sha256']
    same(decode(guard_bytes), data['startup_guard']['receipt'])
    assert data['startup_guard']['receipt']['activity_allowed'] is True
    assert data['startup_guard']['receipt']['persistence_allowed'] is True
    calls = data['actual_native_core_calls']
    assert len(calls) == data['actual_native_core_call_count'] == summary['actual_native_core_call_count'] == 1495
    assert all(c['entrypoint'] == 'recurrent_mass_power' and type(c['elapsed_ns']) is int
               and c['elapsed_ns'] >= 0 for c in calls)
    cold = data['shared_cold_SO_bank']
    same(calls[cold['call_interval'][0]:cold['call_interval'][1]], cold['evidence']['setup']['actual_core_calls'])
    assert cold['actual_core_calls'] == cold['evidence']['setup']['core_call_count'] == 36
    same(cold['call_interval'], cold['evidence']['setup']['call_interval'])
    assert cold['shared_by_both_implementations'] is True
    token = token_check(data)
    assert len(data['pairs']) == len(summary['pairs']) == 6
    assert len(data['paid_warmups']) == 3
    intervals = [('admission', data['native_admission_call_interval']), ('cold_bank', cold['call_interval'])]
    pairs, warmups, all_timed = [], [], []
    fixtures = [(21, 2), (21, 4), (65, 3)]
    for idx, pair in enumerate(data['pairs']):
        sm, runs = pair['summary'], pair['runs']
        same(sm, summary['pairs'][idx])
        assert (sm['N'], sm['a']) == fixtures[idx//2] and sm['repetition'] == idx % 2
        expected_order = [OLD, NEW] if idx % 2 == 0 else [NEW, OLD]
        same([r['implementation'] for r in runs], expected_order)
        same(sm['order'], expected_order)
        old = next(r for r in runs if r['implementation'] == OLD)
        new = next(r for r in runs if r['implementation'] == NEW)
        for prefix, run in (('old', old), ('new', new)):
            same(sm[prefix+'_seconds'], run['calculation_seconds'])
            same(sm[prefix+'_evidence_seconds'], run['evidence_capture_seconds'])
            same(sm[prefix+'_total_seconds'], run['total_seconds_through_evidence'])
        assert sm['core_calls_each'] == old['total_actual_core_calls']
        assert sm['new_factory_and_inverse_columns_each'] == sm['new_column_digit_replays_each'] == 0
        assert sm['logical_binding_checks_each'] == sm['old_frozen_bank_method_calls'] == 6
        assert sm['new_frozen_bank_method_calls'] == 1
        for key in ('plans', 'numeric_ledger', 'terminal_mass', 'calculation_actual_core_calls', 'total_actual_core_calls'):
            same(old[key], new[key])
        for key in ('correlations', 'observer_operations', 'phase_bindings', 'codec_binding', 'native_two_H4_binding'):
            same(old['evidence']['inherited'][key], new['evidence']['inherited'][key])
        for key in ('gram', 'policy'):
            same(old['counters_before_evidence'][key], new['counters_before_evidence'][key])
        same(old['counters_before_evidence']['guard']['stats'], new['counters_before_evidence']['guard']['stats'])
        same(old['evidence']['boundary_guard']['stats'], new['evidence']['boundary_guard']['stats'])
        same(old['evidence']['policy_stats'], new['evidence']['policy_stats'])
        for run in runs:
            assert run['evidence']['certificate_bank_sha256'] == cold['evidence']['binding_sha256']
            assert run['counters_before_evidence']['guard']['stats']['bank_check_attempts'] == 6
        bg, fg = new['counters_before_evidence']['guard'], new['evidence']['boundary_guard']
        for guard, accepts in ((bg, 5), (fg, 6)):
            st = guard['view_stats']
            assert st['fast_accepts'] == st['segmented_check_attempts'] == accepts
            assert st['token_derivations'] == st['constructor_frozen_checks'] == guard['frozen_bank_check_invocations'] == 1
            for k in ('compatibility_checks', 'compatibility_accepts', 'compatibility_rejections',
                      'bank_identity_rejections', 'token_identity_rejections', 'raw_view_construction_failures'):
                assert st[k] == 0
            assert guard['view_comparison_is_full_bytes_not_hash_only'] is True
            assert guard['view_token_sha256'] == token['token_sha256']
            same(guard['segment_bytes'], token['segment_bytes'])
        same(sm['new_segmented_view_stats'], bg['view_stats'])
        assert sm['full_covariances_observer_streams_numeric_ledger_native_counters_equal'] is True
        assert sm['guard_topology_equal'] is True
        assert sm['strict_cross_version_cursor_equality_claimed'] is False
        records = [run_check(run, calls, True) for run in runs]
        all_timed.extend(records)
        intervals.extend((r['label'], r['core_call_interval']) for r in runs)
        pairs.append({'N': sm['N'], 'a': sm['a'], 'repetition': sm['repetition'], 'order': expected_order,
                      'all_saved_numeric_records_strictly_equal': True,
                      'runs': records, 'new_over_old_calculation': new['calculation_seconds']/old['calculation_seconds'],
                      'new_over_old_through_evidence': new['total_seconds_through_evidence']/old['total_seconds_through_evidence']})
    for idx, item in enumerate(data['paid_warmups']):
        assert (item['N'], item['a']) == fixtures[idx]
        run = item['run']
        assert run['implementation'] == OLD
        warmups.append(run_check(run, calls, False))
        intervals.append((run['label'], run['core_call_interval']))
    intervals.sort(key=lambda x: x[1][0])
    frontier = 0
    for label, (start, stop) in intervals:
        assert start == frontier and stop > start
        frontier = stop
    assert frontier == len(calls)
    decomposition = {'native_program_admission': 244, 'shared_cold_SO_bank': 36,
                     'paid_warmups': sum(x['native_calls'] for x in warmups),
                     'measured_runs': sum(x['native_calls'] for x in all_timed), 'standalone_token': 0}
    assert decomposition['paid_warmups'] == 243 and decomposition['measured_runs'] == 972
    assert data['native_admission_call_interval'] == [0, 244]
    assert sum(decomposition.values()) == len(calls)
    chronological = sorted(all_timed+warmups, key=lambda r: r['core_call_interval'][0])
    assert all(datetime.fromisoformat(a['wall_end_utc']) <= datetime.fromisoformat(b['wall_start_utc'])
               for a, b in zip(chronological, chronological[1:]))
    instances, ids = [], set()
    for i, p in enumerate(data['program_final_table_instances']):
        assert (p['N'], p['a']) == fixtures[i]
        for table in p['table_instances']:
            identity = (i, table['factory_index'], table['role'])
            assert identity not in ids
            ids.add(identity)
            cert = table['evidence']
            assert sha(packed(cert['permutation'])) == cert['permutation_sha256']
            instances.append({'program': i, 'factory_index': table['factory_index'], 'role': table['role'],
                              'certificate_sha256': sha(packed(cert)), 'stats': cert['stats']})
    assert len(instances) == 18 and Counter(x['role'] for x in instances) == {'factory': 9, 'created_inverse': 9}
    table_totals = {k: sum(x['stats'][k] for x in instances) for k in
                    ('setup_adder_digit_replays', 'column_adder_digit_replays', 'computed_columns',
                     'column_requests', 'cache_hits', 'setup_host_bit_wiring_operations',
                     'column_host_bit_wiring_operations')}
    table_totals['permutation_verification_digit_replays'] = sum(
        v['replayed_adder_digits'] for p in data['program_final_table_instances'] for v in p['permutation_verifications'])
    same([table_totals[k] for k in ('setup_adder_digit_replays', 'column_adder_digit_replays',
                                  'computed_columns', 'column_requests', 'cache_hits', 'permutation_verification_digit_replays')],
         [9032, 11077, 88, 502, 414, 5494])
    accounting = decode((DATA/'SEGMENTED_MATCHED_COST_ACCOUNTING.json').read_bytes())
    assert accounting['actual_native_core_calls'] == 1495
    for key in table_totals:
        other = 'program_permutation_verification_digit_replays' if key == 'permutation_verification_digit_replays' else key
        same(table_totals[key], accounting['shared_table_totals'][other])
    assert not list(DATA.glob('FAILED_EXECUTION_*.json.gz'))
    result = {'schema': 'SEGMENTED_MATCHED_SHARED_CONTEXT_IO_REVIEW_V1', 'status': 'PASS',
              'scientific_execution_performed_by_this_reader': False,
              'reader_sha256': sha(Path(__file__).read_bytes()), 'source_hashes': data['source_hashes'],
              'additional_static_source_pin': {str(codec_path): codec_sha},
              'input_gzip_sha256': GZIP_SHA, 'input_raw_sha256': RAW_SHA,
              'input_gzip_bytes': len(blob), 'input_raw_bytes': len(raw),
              'startup_guard_sha256': data['startup_guard']['sha256'],
              'six_pairs': pairs, 'paid_warmups': warmups, 'native_call_decomposition': decomposition,
              'disjoint_complete_call_intervals': [{'label': k, 'interval': v} for k, v in intervals],
              'segmented_token_reconstruction': token, 'shared_table_instances_counted_once': instances,
              'shared_table_totals': table_totals,
              'whole_recorded_elapsed_seconds': data['elapsed_seconds'],
              'whole_wall_start_utc': data['wall_start_utc'], 'whole_wall_before_serialization_utc': data['wall_before_serialization_utc'],
              'scope': 'all saved samples checked; static/source-bound pure I/O, not fresh native replay or independent admission',
              'limits': ['Six pairs comprise three fixed fixtures with two deterministic alternating orders each in one process.',
                         'No independent-trial confidence interval, full-law performance or asymptotic claim.',
                         'Timers exclude per-run deep detachment/final JSON/gzip; whole elapsed also ends before final capture_tables.',
                         'Quiet-window coordination is testimony; this reader cannot prove absence of OS load or unrecorded runs.',
                         'Token byte lengths are payload lengths, not peak process memory.',
                         'Shared typed table counters are counted once per concrete instance; inherited cumulative reports are not added.',
                         'Exact cross-version cursor equality is not claimed; implementation metadata intentionally differs.']}
    path = Path(__file__).with_name('SEGMENTED_BENCHMARK_RECORD_REVIEW.json')
    path.write_bytes(packed(result)+b'\n')
    print(json.dumps({'status': result['status'], 'pairs': len(pairs), 'timed_samples': len(all_timed),
                      'native_calls': decomposition, 'token_payload_bytes': 707035,
                      'output_sha256': sha(path.read_bytes())}, sort_keys=True))


if __name__ == '__main__':
    main()
