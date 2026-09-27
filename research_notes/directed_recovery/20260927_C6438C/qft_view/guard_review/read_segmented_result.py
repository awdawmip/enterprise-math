"""Pure I/O review of saved segmented-view evidence; no native import/replay."""
from collections import Counter
from pathlib import Path
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
SOURCE = '90c773c74a81ed239e32fcc12fa8d238032d6fbcfef3f4d6eb2056856666ed99'
PROFILE = 'SEGMENTED_STRICT_SO_VIEW_WITH_FROZEN_FALLBACK_V1'


def encode(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False,
                      allow_nan=False).encode('utf-8')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def same(a, b):
    assert encode(a) == encode(b)


def core_signature(call):
    return (call['entrypoint'], call['states'], call['depth'])


def observer_signature(op):
    return (op['kernel'], op['states'], op['depth'])


def inspect_engine(evidence, bank, *, segmented=True):
    cursor = evidence['cursor']
    inherited = evidence['inherited']
    report, guard = inherited['report'], evidence['boundary_guard']
    same(cursor['history'], report['history'])
    assert all(type(bit) is int and bit in (0, 1) for bit in cursor['history'])
    assert guard['active_depth'] == 0 and guard['owner_active'] is False
    assert evidence['certificate_bank_sha256'] == cursor['certificate_bank_sha256'] == bank['binding_sha256']
    if segmented:
        assert cursor['schema'] == 'BRC_SEGMENTED_SO_TRACE_CURSOR_V1'
        assert cursor['source_sha256'] == evidence['source_sha256'] == SOURCE
        assert evidence['view_profile'] == cursor['view_profile'] == PROFILE
        assert cursor['view_token_sha256'] == evidence['view_token_sha256'] == guard['view_token_sha256']
        assert cursor['query_cache_or_random_tape_restored'] is False
        view = guard['view_stats']
        assert view['constructor_frozen_checks'] == view['token_derivations'] == 1
        assert view['segmented_check_attempts'] == view['fast_accepts'] + view['compatibility_checks']
        assert view['compatibility_checks'] == view['compatibility_accepts'] + view['compatibility_rejections']
        assert guard['frozen_bank_check_invocations'] == 1 + view['compatibility_checks']
        assert guard['view_comparison_is_full_bytes_not_hash_only'] is True
        assert guard['logical_bank_check_counters_include_segmented_checks'] is True
    assert cursor['restore_mode'] == 'REEXECUTE_COMMITTED_PREFIX_AND_PENDING_DECISION'
    assert len(cursor['steps']) == len(cursor['history'])
    assert len(evidence['certificates']) == len(cursor['steps'])
    for depth, step in enumerate(cursor['steps']):
        cert = evidence['certificates'][depth]
        assert step['certificate_sha256'] == sha(encode(cert))
        same(step['history'], cursor['history'][:depth])
        same(cert['history'], step['history'])
        assert type(step['bit']) is int and step['bit'] == cursor['history'][depth]
        for key in ('reference_ids', 'selected_ids', 'charge'):
            same(step[key], cert[key])
    pending = evidence['pending']
    assert cursor['pending_certificate_sha256'] == (None if pending is None else sha(encode(pending)))
    if pending is not None:
        same(pending['history'], cursor['history'])
    words_by_hash = {sha(encode(word)): word for word in bank['logical']['words'].values()}
    for cert in evidence['certificates'] + ([] if pending is None else [pending]):
        assert cert['certificate_bank_sha256'] == bank['binding_sha256']
        assert cert['certificate_interface'] == 'BRC_SO_TRACE_BANK_V1'
        assert cert['prefix_covariance_defect_observed'] is False
        assert cert['prefix_mass_observed_for_policy'] is False
        key = cert['word_certificate_sha256']
        if key is not None:
            word = words_by_hash[key]
            same(cert['uniform_s'], word['s'])
            same(cert['bound_method'], word['bound_method'])
            same(cert['bound_is_exact'], word['bound_is_exact'])
    correlations = inherited['correlations']
    assert len(correlations) == report['distinct_queries']
    for correlation in correlations:
        assert type(correlation['denominator']) is int and correlation['denominator'] > 0
        rows = correlation['numerator_rows']
        assert len(rows) == report['dimension'] == 6
        assert all(len(row) == 6 and all(type(x) is int for x in row) for row in rows)
    ops = inherited['observer_operations']
    assert len(ops) == report['actual_positive_path_observations']
    return {'history': cursor['history'], 'correlations': len(correlations), 'observers': len(ops),
            'native_phase_vector_applications': report['native_phase_vector_applications'],
            'query_requests': report['query_requests'], 'policy_stats': evidence['policy_stats'],
            'token_sha256': cursor.get('view_token_sha256')}


def main():
    zipped = (ROOT / 'SEGMENTED_VIEW_RESULTS.json.gz').read_bytes()
    raw = gzip.decompress(zipped)
    data = json.loads(raw)
    summary = json.loads((ROOT / 'SEGMENTED_VIEW_SUMMARY.json').read_bytes())
    cost_raw = (ROOT / 'SEGMENTED_VIEW_COST_ACCOUNTING.json').read_bytes()
    cost = json.loads(cost_raw)
    assert data['status'] == summary['status'] == 'PASSED'
    assert len(raw) == summary['raw_bytes'] == 15658784
    assert len(zipped) == summary['gzip_bytes'] == 594656
    assert sha(raw) == summary['raw_sha256'] == cost['raw_sha256'] == '12f5528102c5c6f84ff35d2fa6bef1c601ccb09111129365114a67622b4cfbf3'
    assert sha(zipped) == summary['gzip_sha256'] == '3578a052c1fda612f854fe2f0a479ccdca4f0feb6b42d48f0100b84eaee79b8a'
    same(data['source_hashes'], summary['source_hashes'])
    for path, expected in data['source_hashes'].items():
        assert sha(Path(path).read_bytes()) == expected
    guard_bytes = (ROOT / 'STARTUP_GUARD.json').read_bytes()
    assert sha(guard_bytes) == data['startup_guard_sha256']
    guard = json.loads(guard_bytes)
    assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True
    assert guard['sync_debt_events'] == [] and guard['required_action'] == 'CONTINUE_ACTIVITY'
    bank = data['unchanged_cold_SO_bank']
    assert sha(encode(bank['logical'])) == bank['binding_sha256']
    assert bank['logical']['full_dimension'] == 61 and bank['logical']['encoded_dimension'] == 6
    for m, word in bank['logical']['words'].items():
        assert word['phase_index'] == int(m) and word['bound_valid'] is True
        assert word['full_dimension'] == 61
        for key in ('complete_forward_columns', 'complete_inverse_columns'):
            assert len(word[key]) == 61 and all(len(column) == 61 for column in word[key])
    core = data['actual_core_calls']
    assert len(core) == data['core_call_count'] == summary['core_call_count'] == 1116
    cold = bank['setup']
    lo, hi = cold['call_interval']
    same(core[lo:hi], cold['actual_core_calls'])
    assert hi - lo == cold['core_call_count'] == 36
    unique, fixtures = [], []
    for fixture in data['fixtures']:
        old, new = fixture['old_SO_boundary'], fixture['segmented_boundary']
        old_counts = inspect_engine(old, bank, segmented=False)
        new_counts = inspect_engine(new, bank)
        for field in ('correlations', 'observer_operations', 'phase_bindings', 'codec_binding', 'native_two_H4_binding'):
            same(old['inherited'][field], new['inherited'][field])
        for field in ('certificates', 'pending', 'policy_stats', 'interruption_events'):
            same(old[field], new[field])
        same({k:v for k,v in old['inherited']['report'].items() if k != 'boundary_guard'},
             {k:v for k,v in new['inherited']['report'].items() if k != 'boundary_guard'})
        same(old['boundary_guard']['stats'], new['boundary_guard']['stats'])
        changed_cursor_fields = {'schema', 'view_token_sha256', 'source_sha256',
                                 'so_policy_parent_source_sha256', 'policy', 'view_profile'}
        same({k:v for k,v in old['cursor'].items() if k not in changed_cursor_fields},
             {k:v for k,v in new['cursor'].items() if k not in changed_cursor_fields})
        assert old['cursor']['schema'] != new['cursor']['schema']
        same(fixture['history'], [1, 0, 0, 0])
        assert len(fixture['steps']) == 4
        for depth, step in enumerate(fixture['steps']):
            assert step['depth'] == depth and step['bit'] == fixture['history'][depth]
            assert step['full_covariance_equal'] is True and step['pending_and_ledger_equal'] is True
        left, right = fixture['call_interval']
        same(sorted(Counter(core_signature(c) for c in core[left:right]).items()),
             sorted(Counter(observer_signature(op) for e in (old,new)
                            for op in e['inherited']['observer_operations']).items()))
        assert new['boundary_guard']['view_stats']['compatibility_checks'] == 0
        fixtures.append({'N': fixture['N'], 'a': fixture['a'], 'old': old_counts, 'new': new_counts,
                         'complete_matrices_observer_ledger_report_equality': True})
        unique.extend((old, new))
    assert len(fixtures) == summary['fixtures'] == 2
    resume = data['pending_restore']
    for key in ('pending_snapshot', 'after_runtime_rejections', 'original', 'restored'):
        inspect_engine(resume[key], bank)
    same(resume['input_cursor'], resume['pending_snapshot']['cursor'])
    same(resume['pending_snapshot']['cursor'], resume['after_runtime_rejections']['cursor'])
    same(resume['pending_snapshot']['inherited']['correlations'], resume['after_runtime_rejections']['inherited']['correlations'])
    same(resume['pending_snapshot']['inherited']['observer_operations'], resume['after_runtime_rejections']['inherited']['observer_operations'])
    same(resume['original']['cursor'], resume['restored']['cursor'])
    same(resume['original']['inherited']['correlations'], resume['restored']['inherited']['correlations'])
    same(resume['original']['inherited']['observer_operations'], resume['restored']['inherited']['observer_operations'])
    assert resume['strict_new_cursor_equal'] is True and resume['query_cache_or_rng_restored'] is False
    unique.extend((resume['original'], resume['restored']))
    runtime = data['runtime_negative_controls']
    assert len(runtime) == summary['runtime_negative_controls'] == 15
    runtime_names = ['phase_metadata_at_'+s for s in
        ('gamma','mass','probabilities','advance','prepare_next','cursor','evidence','report')]
    runtime_names += ['codec_metadata_mismatch','forged_equal_content_token','wrong_bank_object_type',
        'distinct_same_content_SO_bank_identity','wrong_type_at_constructor',
        'ordered_native_word_replacement','native_column_replacement']
    same([n['case'] for n in runtime], runtime_names)
    for n in runtime:
        assert n['rejected'] is True and n['actual_core_calls'] == 0
        assert n['call_interval'][0] == n['call_interval'][1]
        assert n['failed_replay_evidence'] is None and n['zero_new_observer_when_required'] is True
        if n['guard_after'] is not None:
            assert n['guard_after']['active_depth'] == 0 and n['guard_after']['owner_active'] is False
    negatives = []
    assert len(data['cursor_negative_controls']) == summary['cursor_negative_controls'] == 8
    for n in data['cursor_negative_controls']:
        assert n['rejected'] is True
        left, right = n['call_interval']
        assert right - left == n['actual_core_calls']
        e = n['failed_replay_evidence']
        if n['case'] == 'bool_history':
            assert e is None and n['actual_core_calls'] == 0
        else:
            inspect_engine(e, bank)
            target = resume['original'] if n['case'] == 'old_SO_cursor' else resume['pending_snapshot']
            same(e['cursor'], target['cursor'])
            same(e['inherited']['correlations'], target['inherited']['correlations'])
            same(e['inherited']['observer_operations'], target['inherited']['observer_operations'])
            same([core_signature(c) for c in core[left:right]],
                 [observer_signature(op) for op in e['inherited']['observer_operations']])
            unique.append(e)
        negatives.append({'case': n['case'], 'reason': n['reason'], 'calls': n['actual_core_calls'],
                          'saved_complete_replay': e is not None})
    retry = data['budget_recovery']
    for key in ('failed_attempt', 'retried', 'fresh'):
        inspect_engine(retry[key], bank)
    failed, retried, fresh = (retry[k] for k in ('failed_attempt', 'retried', 'fresh'))
    same(failed['cursor']['history'], []); same(failed['cursor']['steps'], [])
    assert failed['pending'] is not None and len(failed['interruption_events']) == 1
    interruption = failed['interruption_events'][0]
    assert interruption['selected_bit'] == 1 and interruption['history_committed'] is False
    assert interruption['same_selected_bit_may_be_retried'] is True
    same(retried['cursor'], fresh['cursor']); same(retried['cursor']['history'], [1])
    same(retried['inherited']['correlations'], fresh['inherited']['correlations'])
    same(retried['inherited']['observer_operations'], fresh['inherited']['observer_operations'])
    prefix = failed['inherited']['observer_operations']
    same(prefix, retried['inherited']['observer_operations'][:len(prefix)])
    assert len(prefix) == 1 and len(retried['inherited']['observer_operations']) == 2
    unique.extend((retried, fresh))
    admission = data['initial_program_admission_call_interval']
    assert admission == [0, 244]
    allocated = Counter(observer_signature(op) for e in unique for op in e['inherited']['observer_operations'])
    allocated.update(core_signature(c) for c in cold['actual_core_calls'])
    same(sorted(allocated.items()), sorted(Counter(core_signature(c) for c in core[244:]).items()))
    assert sum(cost['core_call_decomposition'].values()) == 1116
    segmented = [e for e in unique if 'view_profile' in e]
    assert len(segmented) == cost['segmented_engine_objects'] == 13
    view_totals = {k: sum(e['boundary_guard']['view_stats'][k] for e in segmented)
                   for k in segmented[0]['boundary_guard']['view_stats']}
    same(view_totals, cost['segmented_view_counter_totals_at_final_snapshots'])
    tokens = {e['view_token_sha256'] for e in segmented}
    assert len(tokens) == 1
    table_rows = []
    for i, program in enumerate(data['program_final_table_instances']):
        ids = set()
        for entry in program['table_instances']:
            key = (entry['factory_index'], entry['role'])
            assert key not in ids; ids.add(key)
            saved = next(row for row in cost['shared_program_table_instances'] if
                         row['program_index'] == i and (row['factory_index'],row['role']) == key)
            assert sha(encode(entry['evidence'])) == saved['snapshot_sha256']
            same(entry['evidence']['stats'], saved['stats'])
            table_rows.append(saved)
    assert len(table_rows) == len(cost['shared_program_table_instances']) == 10
    for key, value in cost['shared_table_totals'].items():
        if key == 'program_permutation_verification_digit_replays':
            observed = sum(c['replayed_adder_digits'] for p in data['program_final_table_instances']
                           for c in p['permutation_verifications'])
        else:
            observed = sum(row['stats'][key] for row in table_rows)
        assert observed == value
    toys = data['metadata_predicate_checks']
    assert len(toys) == summary['metadata_toy_checks'] == 8
    assert all(toy['native_scientific_execution'] is False and toy['matches_whole_JSON_predicate'] is True for toy in toys)
    assert toys[1]['route'] == 'FROZEN_COMPATIBILITY_ACCEPT' and toys[1]['fallback_calls'] == 1
    assert view_totals['compatibility_accepts'] == 0 and view_totals['compatibility_rejections'] == 9
    output = {'status': 'PASS_COMPLETE_SAVED_RECORD_REVIEW',
        'admission': 'SHARED_CONTEXT_AUTHOR_REVIEW_NOT_FORMAL_ADMISSION',
        'scientific_modules_imported': False, 'scientific_arithmetic_recomputed': False,
        'reader_sha256': sha(Path(__file__).read_bytes()), 'source_hashes': data['source_hashes'],
        'raw_sha256': sha(raw), 'raw_bytes': len(raw), 'gzip_sha256': sha(zipped), 'gzip_bytes': len(zipped),
        'cost_accounting_sha256': sha(cost_raw),
        'execution_note_sha256': sha((ROOT/'SEGMENTED_VIEW_EXECUTION_NOTE.md').read_bytes()),
        'implementation_scope_sha256': sha((ROOT/'IMPLEMENTATION_SCOPE.md').read_bytes()),
        'startup_guard_sha256': sha(guard_bytes), 'bank_binding_sha256': bank['binding_sha256'],
        'fixed_prefix_comparisons': fixtures, 'runtime_rejections': len(runtime),
        'cursor_rejections': negatives, 'strict_pending_restore': True, 'rollback_same_bit_retry': True,
        'full_core_signature_and_nonoverlap_accounting_checked': True,
        'core_call_decomposition': cost['core_call_decomposition'], 'core_calls': len(core),
        'segmented_objects': len(segmented), 'view_counter_totals': view_totals,
        'shared_tables': len(table_rows), 'table_totals': cost['shared_table_totals'],
        'segment_payload_bytes_per_object': cost['segment_payload_bytes_per_object'],
        'toy_metadata_compatibility_acceptance_is_not_native_admission': True,
        'unexpected_failure_artifacts': [p.name for p in ROOT.glob('FAILED_EXECUTION_*.json.gz')],
        'reader_development_note': 'Initial pure-I/O draft incorrectly expected the pending certificate in committed certificates; source confirms append only after successful advance. Corrected before this PASS output; no scientific re-execution.',
        'limits': ['Per-step plan is saved once with checker equality assertions, not two independent plan copies.',
                   'Complete matrix/observer/ledger comparisons use both saved route records.',
                   'Actual compatibility success only tested by pure JSON example.',
                   'Fixed canonical admitted bank predicate only; stricter constructor/identity contract.',
                   'No native replay, full-law test, new timing or RSS measurement by this reader.']}
    target = ROOT/'guard_review/SEGMENTED_VIEW_RECORD_REVIEW.json'
    with target.open('x', encoding='utf-8') as out:
        json.dump(output, out, indent=2); out.write('\n')
    print(json.dumps({'status': output['status'], 'reader_sha256': output['reader_sha256'],
        'record_sha256': sha(target.read_bytes()), 'calls': len(core), 'view_totals': view_totals}))


if __name__ == '__main__':
    main()
