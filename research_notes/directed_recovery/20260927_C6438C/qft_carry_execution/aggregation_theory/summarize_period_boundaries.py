"""Count frozen boundary evidence metadata; no native/scientific execution."""
from pathlib import Path
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
raw = gzip.decompress((ROOT / 'PERIOD_BOUNDARY_RESULTS.json.gz').read_bytes())
data = json.loads(raw)
cycles = [x['period_certificate'] for x in data['inputs']]
replays = [q['period_verification']['replay'] for x in data['inputs']
           for q in x['aggregation_evidence']['aggregation_queries']]
all_cycles = cycles+replays
cycle_cost = {
    'fresh_initial_instances': len(cycles), 'fresh_positive_replay_instances': len(replays),
    'setup_adder_digits': sum(x['actual_cycle_table']['stats']['setup_adder_digit_replays'] for x in all_cycles),
    'column_adder_digits': sum(x['actual_cycle_table']['stats']['column_adder_digit_replays'] for x in all_cycles),
    'permutation_replay_adder_digits': sum(x[k]['replayed_adder_digits'] for x in all_cycles
        for k in ('inherited_permutation_replay', 'fresh_permutation_replay')),
    'column_requests': sum(x['actual_cycle_table']['stats']['column_requests'] for x in all_cycles),
}
tables = [t['stats'] for x in data['inputs'] for t in x['program_table_instances']]
program_cost = {
    'table_instances': len(tables),
    'setup_adder_digits': sum(x['setup_adder_digit_replays'] for x in tables),
    'column_adder_digits': sum(x['column_adder_digit_replays'] for x in tables),
    'permutation_replay_adder_digits': sum(v['replayed_adder_digits']
        for x in data['inputs'] for v in x['program_permutation_verifications']),
}
index_stats = [q['index_arithmetic_stats'] for x in data['inputs']
               for q in x['aggregation_evidence']['aggregation_queries']]
index_cost = {k: sum(x[k] for x in index_stats) for k in index_stats[0]}
alias_digits = sum(x['alias_discovery']['metrics']['total_adder_digit_replays'] for x in data['inputs'])
digits = sum(record[k] for record in (cycle_cost, program_cost)
             for k in ('setup_adder_digits', 'column_adder_digits', 'permutation_replay_adder_digits'))
digits += alias_digits+index_cost['adder_digit_replays']
answer = {'schema': 'PERIOD_BOUNDARY_METADATA_ACCOUNTING_V1',
    'metadata_only_no_new_scientific_execution': True,
    'source_payload_sha256': hashlib.sha256(raw).hexdigest(),
    'cycle_cost': cycle_cost, 'program_initialization': program_cost,
    'index_arithmetic': index_cost, 'independent_alias_discovery_adder_digits': alias_digits,
    'total_counted_typed_adder_digit_replays': digits,
    'native_phase_vector_applications': {
        'aggregation': [x['aggregation_evidence']['inherited_action_stats']['native_phase_vector_applications'] for x in data['inputs']],
        'alias_sum': [x['baseline_evidence']['inherited_action_stats']['native_phase_vector_applications'] for x in data['inputs']]},
    'signed_observer_operation_counts': {
        'aggregation': [len(x['aggregation_evidence']['observer_operations']) for x in data['inputs']],
        'alias_sum': [len(x['baseline_evidence']['observer_operations']) for x in data['inputs']]},
    'actual_native_core_call_receipts': data['actual_native_core_calls'],
    'receipt_count_verified': len(data['native_core_call_receipts']) == data['actual_native_core_calls'],
    'not_a_total_bit_operation_count': True,
    'phase_admission_and_observer_work_excluded_from_typed_digit_count': True,
    'equal_modulus_multiplier_instances_not_deduplicated': True}
(ROOT / 'PERIOD_BOUNDARY_ACCOUNTING.json').write_text(json.dumps(answer, sort_keys=True, indent=2)+'\n')
print(json.dumps(answer, sort_keys=True))
