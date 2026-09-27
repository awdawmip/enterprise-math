"""Metadata accounting only; reads frozen evidence, performs no scientific replay."""
from pathlib import Path
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
raw = gzip.decompress((ROOT / 'PERIOD_AGGREGATION_RESULTS.json.gz').read_bytes())
data = json.loads(raw)


def cycle_cost(record):
    stats = record['actual_cycle_table']['stats']
    return {
        'setup_adder_digits': stats['setup_adder_digit_replays'],
        'column_adder_digits': stats['column_adder_digit_replays'],
        'permutation_replay_adder_digits': sum(record[k]['replayed_adder_digits']
            for k in ('inherited_permutation_replay', 'fresh_permutation_replay')),
        'column_requests': stats['column_requests'],
        'computed_columns': stats['computed_columns'],
    }


def total(records):
    return {k: sum(r[k] for r in records) for k in records[0]} if records else {}


positive_replays = [q['period_verification']['replay']
    for evidence in data['aggregation_evidence'] for q in evidence['aggregation_queries']]
failed_replays = [x['failed_replay_evidence']['replay'] for x in data['negative_controls']
                  if x['failed_replay_evidence'] is not None]
groups = {
    'initial_complete_cycle_discoveries': data['certified_cycles'],
    'positive_query_full_cycle_replays': positive_replays,
    'failed_certificate_full_cycle_replays': failed_replays,
    'partial_cycle_discovery': [data['partial_period_certificate']],
}
cycle_groups = {name: {'fresh_instances': len(records), 'cost': total(list(map(cycle_cost, records)))}
                for name, records in groups.items()}
index_stats = [q['index_arithmetic_stats'] for e in data['aggregation_evidence']
               for q in e['aggregation_queries']]
program_tables = [t['stats'] for p in data['programs'] for t in p['program_table_instances']]
program_cost = {
    'table_instances': len(program_tables),
    'setup_adder_digits': sum(x['setup_adder_digit_replays'] for x in program_tables),
    'column_adder_digits': sum(x['column_adder_digit_replays'] for x in program_tables),
    'permutation_replay_adder_digits': sum(v['replayed_adder_digits']
        for p in data['programs'] for v in p['program_permutation_verifications']),
}
alias_digits = sum(x['metrics']['total_adder_digit_replays'] for x in data['alias_discovery_evidence'])
all_cycle_cost = total([group['cost'] for group in cycle_groups.values()])
typed_digits = (sum(program_cost[k] for k in ('setup_adder_digits', 'column_adder_digits',
                'permutation_replay_adder_digits')) + alias_digits +
                sum(all_cycle_cost[k] for k in ('setup_adder_digits', 'column_adder_digits',
                    'permutation_replay_adder_digits')) + sum(x['adder_digit_replays'] for x in index_stats))
answer = {
    'schema': 'PERIOD_AGGREGATION_METADATA_ACCOUNTING_V1',
    'metadata_only_no_new_scientific_execution': True,
    'source_payload_sha256': hashlib.sha256(raw).hexdigest(),
    'cycle_groups': cycle_groups, 'all_cycle_cost': all_cycle_cost,
    'program_initialization': program_cost,
    'independent_alias_discovery_adder_digits': alias_digits,
    'aggregation_index_arithmetic': total(index_stats),
    'total_counted_typed_adder_digit_replays': typed_digits,
    'digit_scope': 'program modular setup/columns/verifications, all executed independent cycles including negative replay and partial discovery, alias discovery, aggregation routing; excludes phase/native observer work counted separately below',
    'native_phase_vector_applications': {
        'aggregation': [e['inherited_action_stats']['native_phase_vector_applications'] for e in data['aggregation_evidence']],
        'alias_sum': [e['inherited_action_stats']['native_phase_vector_applications'] for e in data['baseline_evidence']],
    },
    'signed_observer_operation_counts': {
        'aggregation': [len(e['observer_operations']) for e in data['aggregation_evidence']],
        'alias_sum': [len(e['observer_operations']) for e in data['baseline_evidence']],
    },
    'actual_native_core_call_receipts': data['actual_native_core_calls'],
    'receipt_count_verified': len(data['native_core_call_receipts']) == data['actual_native_core_calls'],
    'core_call_deltas_include_query_period_replay': {
        'aggregation': sum(x['aggregation_cost']['native_core_calls'] for x in data['cases']),
        'alias_sum': sum(x['alias_sum_cost']['native_core_calls'] for x in data['cases']),
    },
    'not_a_total_bit_operation_count': True,
    'phase_application_counters_exclude_initial_full_column_admission': True,
    'no_program_or_cycle_table_instances_deduplicated_by_equal_modulus_multiplier': True,
    'live_matrix_slots_are_not_total_peak_bytes': True,
}
(ROOT / 'PERIOD_RESOURCE_ACCOUNTING.json').write_text(json.dumps(answer, sort_keys=True, indent=2)+'\n')
print(json.dumps(answer, sort_keys=True))
