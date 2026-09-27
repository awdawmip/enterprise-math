"""Read-only accounting of the frozen execution artifact; no scientific replay."""
from collections import defaultdict
from pathlib import Path
from fractions import Fraction
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
STREAMING = Path('D:/em/TEMP/sep26-shor-general/optimization/streaming/lazy_streaming.py')
LAZY = Path('D:/em/TEMP/sep26-shor-general/optimization/lazy_modular/lazy_modular.py')


def main():
    compressed = (ROOT/'PROJECTED_ROWS_RESULTS.json.gz').read_bytes()
    raw = gzip.decompress(compressed)
    result = json.loads(raw)
    summary = json.loads((ROOT/'PROJECTED_ROWS_SUMMARY.json').read_text(encoding='utf-8'))
    assert hashlib.sha256(raw).hexdigest() == summary['payload_sha256']
    assert hashlib.sha256(compressed).hexdigest() == summary['gzip_sha256']
    entries = result['complete_modular_table_instances']
    assert len(entries) == len({e['instance_name'] for e in entries}) == 24
    groups = defaultdict(lambda: defaultdict(int))
    rows = []
    for entry in entries:
        name, cert = entry['instance_name'], entry['certificate']
        stats, cost = cert['stats'], cert['permutation']['inverse_certificate']['cost']
        assert stats['setup_adder_digit_replays'] == cost['adder_digit_replays']
        # The frozen constructor verifies each distinct factory table once.
        # inverse() creates separate instances but does not call that verifier.
        forward = not name.endswith(':inverse')
        owner = name.split(':')[0]
        values = {'instances':1, 'constructor_verifications':int(forward),
            **{k:stats[k] for k in ('column_requests','computed_columns','cache_hits',
                'setup_adder_digit_replays','column_adder_digit_replays',
                'setup_host_bit_wiring_operations','column_host_bit_wiring_operations',
                'setup_host_bit_length_calls_in_arithmetic','column_host_bit_length_calls_in_arithmetic')},
            'constructor_verification_adder_digits_derived':cost['adder_digit_replays'] if forward else 0,
            'constructor_verification_host_bit_wiring_derived':cost['host_bit_wiring_operations'] if forward else 0,
            'constructor_verification_host_bit_length_calls_derived':cost['host_bit_length_calls_in_arithmetic'] if forward else 0}
        for key, value in values.items():
            groups[owner][key] += value
        rows.append({'instance_name':name,'N':entry['N'],'b':entry['b'],**values})
    total = defaultdict(int)
    for group in groups.values():
        for key, value in group.items():
            total[key] += value
    total['setup_plus_columns_plus_constructor_verification_adder_digits'] = sum(total[k] for k in
        ('setup_adder_digit_replays','column_adder_digit_replays','constructor_verification_adder_digits_derived'))
    attempts = []
    for label, outer in (
        ('N35_cap5',result['outer_runner_positive']),
        ('N35_cap1_failed',result['outer_runner_failed_test_exact_fallback']),
        ('N33_cap4',result['odd_order_contrast']['outer_runner'])):
        train, holdout = outer['training'], outer['holdout']
        report = outer['sample']['oracle_report']
        attempts.append({'label':label,'route':outer['route'],
            'training_paths':len(train['training_paths']),
            'holdout_paths':len(holdout['validation_paths']),
            'training_random_draws':train['training_random_draws'],
            'holdout_random_draws':holdout['validation_random_draws'],
            'training_generation_column_lookups':sum(sum(p['coins']) for p in train['training_paths']),
            'holdout_generation_column_lookups':sum(sum(p['coins']) for p in holdout['validation_paths']),
            'exact_initial_coverage_column_lookups':train['exact_initial_column_queries'],
            'native_call_stage_cumulative':[{'stage':s['stage'],'core_calls':s['core_calls_since_outer_start']}
                for s in outer['resource_stages']],
            'sample_row_and_native_action_metrics':{k:report[k] for k in (
                'row_lookup_queries','projected_row_inputs','peak_retained_rows','peak_candidate_rows',
                'retained_scalar_slots','distinct_queries','cached_row_scalar_slots',
                'query_requests','query_cache_hits','native_phase_vector_applications') if k in report},
            'status':outer['sample']['status'], 'sample_history':outer['sample']['history']})
    accounting = {
        'schema':'FROZEN_PROJECTED_ROW_RESOURCE_ACCOUNTING_V1',
        'status':'OFFLINE_ACCOUNTING_ONLY_NO_NEW_SCIENTIFIC_EXECUTION',
        'payload_sha256':summary['payload_sha256'],'gzip_sha256':summary['gzip_sha256'],
        'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in
            (Path(__file__), STREAMING, LAZY)},
        'instance_count':len(entries),'instance_rows':rows,'owner_totals':dict(groups),'totals':dict(total),
        'one_shot_attempts':attempts,'actual_BRC_core_calls_whole_checker':result['actual_BRC_core_calls'],
        'whole_checker_elapsed_seconds':result['seconds'],
        'odd_fixture_joint_TV_exact':result['odd_order_contrast']['contract_check']['terminal_joint_TV'],
        'odd_fixture_joint_TV_display_decimal':str(float(Fraction(result['odd_order_contrast']['contract_check']['terminal_joint_TV']))),
        'counting_notes':[
            'Native kernel calls, catalog digit replays and host bit wiring are distinct costs; do not add them as one common operation unit.',
            'Constructor verification costs are source-derived from saved exact certificates: LazyStreamingProgram verifies every forward factory instance once; verify_lazy_permutation rebuilds the same inverse certificate. They are not an extra measured replay.',
            'All 24 actual instances count, including separate inverse caches with equal N,b. Do not deduplicate by modulus and multiplier.',
            'Whole-unit totals include three outer attempts, negative controls, interruption/resume, full-history reference checks and replay work. They are not a per-output cost.',
            'Training/holdout generation lookup counts exclude later certificate replay, whose cost is included in whole-unit tables and native calls.',
            'Inherited program_metrics branch counters stay zero because this row/proposal route does not use the old branch evaluator; zero is not a claim of zero arithmetic cost.',
            'Stored candidate maps, parent maps and observer/certificate traces coexist. A lower retained-row count is not a measured total peak-memory reduction.',
            'Elapsed time is a single local wall-clock observation, not a matched benchmark or asymptotic bound.'
        ]}
    (ROOT/'PROJECTED_ROWS_ACCOUNTING.json').write_text(json.dumps(accounting,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'totals':dict(total),'attempts':attempts,'joint_TV_decimal':accounting['odd_fixture_joint_TV_display_decimal']},indent=2))


if __name__ == '__main__':
    main()
