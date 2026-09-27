"""Read-only accounting of frozen execution receipts; no scientific re-execution.

Uses only the Python standard library. Integer sums/hash checks below account for
recorded costs; they do not implement or replace native scientific arithmetic.
"""
from collections import Counter
from pathlib import Path
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parents[1]
EXPECTED_RAW = '3e356df6befcbf201801657016f64072e2bccebbc0a877a51570f77748d7b78b'
EXPECTED_SOURCE = {
    'adaptive_feedback.py': '86263eb4a70fe53f8960aae2c1f0b8695dbca40a597b2711af90f20667ed3c45',
    'check_adaptive_feedback.py': 'cd77bc2ff17a6b2938665a622a74c332e7e24cbe362ba359225fc071716510d3',
}
ADDITIVE = (
    'native_phase_vector_applications', 'query_requests', 'query_cache_hits',
    'base_queries', 'recurrence_queries', 'actual_positive_path_observations',
    'single_term_wiring_observations', 'zero_wiring_observations',
    'zero_matrix_native_actions_skipped',
)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':')).encode()


def observer_cost(ops):
    return {
        'operations': len(ops),
        'by_label': dict(sorted(Counter(op['name'].split(':', 1)[-1] for op in ops).items())),
        'positive_graph_edges_sum': sum(len(op['positive_edges']) for op in ops),
        'graph_states_sum': sum(op['states'] for op in ops),
        'max_graph_states': max((op['states'] for op in ops), default=0),
        'max_graph_depth': max((op['depth'] for op in ops), default=0),
    }


def gram_cost(evidence, gram_source):
    assert evidence['source_sha256'] == EXPECTED_SOURCE['adaptive_feedback.py']
    inherited = evidence['inherited']
    assert inherited['source_sha256'] == gram_source
    report = inherited['report']
    rows = inherited['correlations']
    assert len(rows) == report['distinct_queries']
    assert len(inherited['observer_operations']) == report['actual_positive_path_observations']
    assert len({(c['depth'], c['residue']) for c in rows}) == len(rows)
    assert len(rows) * report['dimension'] ** 2 == report['cached_matrix_scalar_slots']
    assert [[c['depth'], c['residue']] for c in rows] == report['query_keys']
    certificates = list(evidence['certificates'])
    if evidence['pending'] is not None:
        certificates.append(evidence['pending'])
    prepared = Counter(c['decision'] for c in certificates)
    assert prepared['OMIT_OLDEST_CERTIFIED'] == evidence['policy_stats']['accepted_omissions']
    assert prepared['OMIT_OLDEST_CERTIFIED'] == sum(
        len(c['reference_ids']) - len(c['selected_ids']) for c in certificates)
    return {
        **{k: report[k] for k in ADDITIVE},
        'retained_independent_cache_matrices': len(rows),
        'retained_matrix_scalar_slots': report['cached_matrix_scalar_slots'],
        'peak_cached_matrix_scalar_slots': report['peak_cached_matrix_scalar_slots'],
        'max_correlation_numerator_bits': report['max_correlation_numerator_bits'],
        'max_correlation_denominator_bits': report['max_correlation_denominator_bits'],
        'query_attempts_not_recorded_as_hit_or_completed_matrix': report['query_requests']
            - report['query_cache_hits'] - report['base_queries'] - report['recurrence_queries'],
        'prepared_decision_occurrences': dict(sorted(prepared.items())),
        'committed_omission_occurrences': sum(c['decision'] == 'OMIT_OLDEST_CERTIFIED'
                                            for c in evidence['certificates']),
        'policy_stats': evidence['policy_stats'],
        'observer': observer_cost(inherited['observer_operations']),
        'committed_history': evidence['cursor']['history'],
        'interruption_events': evidence['interruption_events'],
    }


def route_cost(route, gram_source):
    leaves = [gram_cost(g, gram_source) for g in route['gram_executions']]
    unique_matrices, unique_decisions = {}, {}
    for g in route['gram_executions']:
        history = g['cursor']['history']
        for c in g['inherited']['correlations']:
            # Same fixed policy and actual history prefix imply the same earlier
            # committed words. This is only an audit union, not executed sharing.
            key = (tuple(history[:c['depth']]), c['depth'], c['residue'])
            value = digest(canonical(c))
            assert key not in unique_matrices or unique_matrices[key] == value
            unique_matrices[key] = value
        certificates = g['certificates'] + ([g['pending']] if g['pending'] is not None else [])
        for c in certificates:
            key = tuple(c['history'])
            value = (c['decision'], tuple(c['reference_ids']), tuple(c['selected_ids']))
            assert key not in unique_decisions or unique_decisions[key] == value
            unique_decisions[key] = value
    return {
        'leaf_replay_invocations': len(leaves),
        'prefix_checks': len(route['checks']),
        'sums_over_separate_leaf_objects': {
            **{k: sum(l[k] for l in leaves) for k in ADDITIVE},
            'retained_independent_cache_matrices': sum(l['retained_independent_cache_matrices'] for l in leaves),
            'retained_matrix_scalar_slots': sum(l['retained_matrix_scalar_slots'] for l in leaves),
            'accepted_omission_occurrences': sum(l['policy_stats']['accepted_omissions'] for l in leaves),
            'committed_omission_occurrences': sum(l['committed_omission_occurrences'] for l in leaves),
            'candidate_defect_tests': sum(l['policy_stats']['candidate_tests'] for l in leaves),
        },
        'max_single_leaf_cached_matrix_scalar_slots': max(l['peak_cached_matrix_scalar_slots'] for l in leaves),
        'max_correlation_numerator_bits': max(l['max_correlation_numerator_bits'] for l in leaves),
        'max_correlation_denominator_bits': max(l['max_correlation_denominator_bits'] for l in leaves),
        'audit_union_of_history_specific_query_matrices': len(unique_matrices),
        'audit_union_of_accepted_prefix_decisions': sum(v[0] == 'OMIT_OLDEST_CERTIFIED' for v in unique_decisions.values()),
        'union_is_not_an_executed_shared_cache': True,
        'explicit_full_state_checker_observer': observer_cost(route['explicit_observer_operations']),
        'whole_route_actual_core_calls_delta': route['actual_core_calls_delta'],
        'explicit_checker_phase_vector_actions': None,
        'explicit_checker_phase_action_note': 'Not separately instrumented in frozen checker; do not infer from core-call count.',
        'leaf_replays': leaves,
    }


def collect_program_tables(record, index):
    """Recover final per-object snapshots, never sum cumulative per-leaf reports.

    Lazy factory has one object per b inside this program. Each has a distinct
    cached inverse object, even if that inverse b also exists in the factory.
    Initial sampler tables are factory order, then used inverse objects append.
    Counter monotonicity and column-record inclusion are verified across snapshots.
    """
    program = record['programs'][index]
    factory = program['tables']
    factory_bs = [t['permutation']['b'] for t in factory]
    assert len(set(factory_bs)) == len(factory_bs)
    groups = {('factory', b): [] for b in factory_bs}
    evidence = []
    for route in ('low', 'reference'):
        evidence.extend(record['cases'][index][route]['gram_executions'])
    if index == 0:
        evidence += [record['resume']['original'], record['resume']['resumed']]
        evidence += [n['actual_failed_replay_evidence'] for n in record['negative_controls']
                     if n.get('actual_failed_replay_evidence') is not None]
        evidence += [record['interruption_recovery']['retried'], record['interruption_recovery']['fresh']]
    for g in evidence:
        tables = g['inherited']['typed_modular_certificates']
        assert [t['permutation']['b'] for t in tables[:len(factory)]] == factory_bs
        inverse_parents = []
        for j, table in enumerate(tables):
            if j < len(factory):
                key = ('factory', factory_bs[j])
            else:
                parent = table['permutation']['inverse_certificate']['inverse_multiplier']
                assert parent in factory_bs
                inverse_parents.append(parent)
                key = ('inverse_of_factory', parent)
            groups.setdefault(key, []).append(table)
        assert len(set(inverse_parents)) == len(inverse_parents)
    for table in factory:
        groups[('factory', table['permutation']['b'])].append(table)
    instances = []
    for key, snapshots in sorted(groups.items()):
        final = max(snapshots, key=lambda t: t['stats']['column_requests'])
        st = final['stats']
        columns = {c['source']: c for c in final['queried_columns']}
        assert len(columns) == st['computed_columns']
        assert st['column_requests'] == st['computed_columns'] + st['cache_hits']
        for old in snapshots:
            assert old['permutation_sha256'] == final['permutation_sha256']
            assert all(v <= st[k] for k, v in old['stats'].items())
            assert all(columns[c['source']] == c for c in old['queried_columns'])
        setup = final['permutation']['inverse_certificate']['cost']
        for metric in ('adder_digit_replays', 'host_bit_wiring_operations',
                       'host_bit_length_calls_in_arithmetic'):
            assert st['setup_' + metric] == setup[metric]
            assert st['column_' + metric] == sum(c['arithmetic_cost'][metric] for c in columns.values())
        instances.append({
            'instance_role': key[0], 'factory_parent_multiplier': key[1],
            'N': final['permutation']['N'], 'multiplier': final['permutation']['b'],
            'permutation_sha256': final['permutation_sha256'],
            'snapshots_examined': len(snapshots), 'final_snapshot_sha256': digest(canonical(final)),
            'final_stats': st, 'setup_typed_operations': setup['typed_operations'],
            'column_typed_operations': sum(c['arithmetic_cost']['typed_operations'] for c in columns.values()),
        })
    proofs = {}
    for p in program['permutation_verifications']:
        assert p['verified'] is True
        b = p['b']
        assert b not in proofs or proofs[b] == p
        proofs[b] = p
    assert set(proofs) == set(factory_bs)
    totals = {k: sum(x['final_stats'][k] for x in instances) for k in instances[0]['final_stats']}
    totals['verification_adder_digit_replays'] = sum(p['replayed_adder_digits'] for p in proofs.values())
    totals['setup_plus_columns_plus_verification_adder_digit_replays'] = (
        totals['setup_adder_digit_replays'] + totals['column_adder_digit_replays']
        + totals['verification_adder_digit_replays'])
    return {
        'program_case': index, 'N': record['cases'][index]['summary']['N'],
        'a': record['cases'][index]['summary']['a'],
        'scope': 'One shared program, both full laws and all later resume/negative/retry uses; not allocated by route.',
        'instances': instances, 'distinct_table_instances': len(instances),
        'distinct_setup_verifications': list(proofs.values()),
        'verification_entries_in_raw_schedule': len(program['permutation_verifications']),
        'totals_counting_each_actual_table_once': totals,
        'complete_host_bit_cost_claimed': False,
    }


def main():
    zipped = (ROOT / 'ADAPTIVE_FEEDBACK_RESULTS.json.gz').read_bytes()
    raw = gzip.decompress(zipped)
    assert digest(raw) == EXPECTED_RAW
    record = json.loads(raw)
    summary = json.loads((ROOT / 'ADAPTIVE_FEEDBACK_SUMMARY.json').read_bytes())
    assert digest(zipped) == summary['gzip_sha256']
    assert digest(raw) == summary['raw_sha256']
    assert len(raw) == summary['raw_bytes'] and len(zipped) == summary['gzip_bytes']
    assert record['source_hashes'] == summary['source_hashes'] == EXPECTED_SOURCE
    for name, expected in EXPECTED_SOURCE.items():
        assert digest((ROOT / name).read_bytes()) == expected
    gram_path = BASE / 'sep26-shor-general/optimization/collision_analysis/gram_sampler.py'
    gram_source = digest(gram_path.read_bytes())
    assert gram_source == '468de944518fbc6afa81a17555676436376da63921a784c810ffe8fab3ca17e9'
    cases = []
    for case in record['cases']:
        routes = {route: route_cost(case[route], gram_source) for route in ('low', 'reference')}
        cases.append({'fixture': case['summary'], **routes, 'tv_observer': observer_cost(case['tv_observer'])})
    resume = {name: gram_cost(record['resume'][name], gram_source) for name in ('original', 'resumed')}
    negatives = []
    for n in record['negative_controls']:
        e = n.get('actual_failed_replay_evidence')
        negatives.append({'case': n['case'], 'rejected': n['rejected'], 'reason': n['reason'],
                          'failed_replay': None if e is None else gram_cost(e, gram_source),
                          'no_saved_replay_reason': None if e is not None else
                          'Strict bit schema or immutable-program/history check rejects before Gram/observer work, as source-audited.'})
    recovery = {name: gram_cost(record['interruption_recovery'][name], gram_source) for name in ('retried', 'fresh')}
    programs = [collect_program_tables(record, i) for i in range(len(record['programs']))]
    all_grams = [leaf for case in cases for route in ('low', 'reference') for leaf in case[route]['leaf_replays']]
    all_grams += list(resume.values()) + [n['failed_replay'] for n in negatives if n['failed_replay'] is not None] + list(recovery.values())
    gram_observers = sum(g['actual_positive_path_observations'] for g in all_grams)
    explicit_observers = sum(c[r]['explicit_full_state_checker_observer']['operations'] for c in cases for r in ('low', 'reference'))
    tv_observers = sum(c['tv_observer']['operations'] for c in cases)
    core = record['actual_native_core_calls']
    assert len(core) == summary['actual_native_core_calls'] == 20725
    # Each saved positive-path evaluation calls core_power once. Remaining calls
    # include vendor/bank/codec/native two-H4 and shared arithmetic setup; no
    # unsupported fine attribution is manufactured from aggregate timings.
    remainder = len(core) - gram_observers - explicit_observers - tv_observers
    assert remainder >= 0
    output = {
        'schema': 'ADAPTIVE_FEEDBACK_RECORDED_COST_AUDIT_V1',
        'method': 'Offline extraction of final second-run evidence; no scientific source imported or executed.',
        'input': {'raw_sha256': digest(raw), 'raw_bytes': len(raw), 'gzip_sha256': digest(zipped),
                  'gzip_bytes': len(zipped), 'source_hashes': EXPECTED_SOURCE,
                  'inherited_gram_sha256': gram_source},
        'extractor_sha256': digest(Path(__file__).read_bytes()),
        'cases': cases, 'shared_program_modular_costs': programs,
        'serialized_resume': {'original': resume['original'], 'restored_new_object': resume['resumed'],
                              'scope': 'Two distinct real executions; replay recomputes, no cache/RNG restoration.'},
        'negative_controls': negatives,
        'budget_interruption_and_retry': {**recovery,
            'interrupted_cursor': record['interruption_recovery']['interrupted_cursor'],
            'scope': 'Retried counter includes failed attempt and successful same-bit retry. Fresh is separate. No pre-failure cost snapshot was saved.'},
        'whole_run': {
            'actual_native_core_calls': len(core),
            'actual_core_entrypoints': dict(Counter(c['entrypoint'] for c in core)),
            'core_elapsed_ns_sum': sum(c['elapsed_ns'] for c in core),
            'recorded_checker_elapsed_seconds': record['elapsed_seconds'],
            'gram_observer_operations_all_routes_and_controls': gram_observers,
            'explicit_checker_observer_operations': explicit_observers,
            'joint_tv_comparison_observer_operations': tv_observers,
            'other_native_core_calls_not_finely_attributed': remainder,
            'phase_vector_actions_gram_routes_and_controls': sum(g['native_phase_vector_applications'] for g in all_grams),
            'shared_modular_adder_digit_replays': sum(p['totals_counting_each_actual_table_once']['setup_plus_columns_plus_verification_adder_digit_replays'] for p in programs),
        },
        'limitations': [
            'All 16 proposed histories are replayed from a fresh Gram object per law; impossible histories stop early. Not independent random trials.',
            'Phase action counter is an admitted word-boundary vector-adapter call, not an additional native-kernel invocation. D=6 has certified full-D=61 provenance.',
            'Candidate-defect construction is included in Gram phase counters; explicit full-state checker vector actions were not instrumented.',
            'Sum of separately retained cache matrices is executed storage/work across objects, not peak process memory. Audit union is descriptive and was not used as a shared cache.',
            'Core nanoseconds exclude Python, rational arithmetic, hashing, allocations, serialization and scheduling; whole checker time is not a single-sample timing.',
            'Typed table host-wiring counters cover their documented subset only; no complete host-bit or total bit-complexity measurement.',
            'Both laws use the same program tables; their modular cumulative report fields must not be added. Different programs and factory/inverse objects remain separate.',
            'Current finite results show greater low-route Gram work, not a demonstrated speedup or general Shor dequantization.',
        ],
    }
    (ROOT / 'COST_ACCOUNTING.json').write_text(json.dumps(output, sort_keys=True, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'accounting_sha256': digest((ROOT / 'COST_ACCOUNTING.json').read_bytes()),
                      'whole_run': output['whole_run'],
                      'program_costs': [{k: p[k] for k in ('N', 'a', 'distinct_table_instances', 'totals_counting_each_actual_table_once')} for p in programs]}, indent=2))


if __name__ == '__main__':
    main()
