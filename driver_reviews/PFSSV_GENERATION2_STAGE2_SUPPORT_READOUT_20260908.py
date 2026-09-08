"""Read already executed cell records; no generator, native math or null draws."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('frozen_root', type=Path)
parser.add_argument('output', type=Path)
args = parser.parse_args()
artifact = args.frozen_root.joinpath('research_artifacts/PFSSV_REVISION_20260908')
cell_path = artifact.joinpath('cell_profiles.jsonl')
summary_path = artifact.joinpath('result_summary.json')
summary = json.loads(summary_path.read_bytes())
cells = []
with cell_path.open('rb') as source:
    for line in source:
        cell = json.loads(line)
        rows = {row['p']: row for row in cell['rows']}
        positive = zero = 0
        first_positive = first_zero = None
        for stratum in cell['null_A_capacity_audit']['strata']:
            origin = rows[stratum['source_maximum_p']]
            positive_group_size = sum(
                row['count'] > 0 and row['legacy_null_A_band'] == stratum['coarse_band']
                and row['p_mod_30'] == stratum['p_mod_30'] for row in cell['rows'])
            for target in stratum['targets']:
                if not target['positive_probability_violation']:
                    continue
                target_row = rows[target['p']]
                assert origin['count'] > 0
                assert stratum['source_maximum_count'] > target['integer_residue_capacity']
                survives_positive_mask = target_row['count'] > 0
                if survives_positive_mask:
                    positive += 1
                    assert positive_group_size >= 2
                else:
                    zero += 1
                witness = {
                    'coarse_band': stratum['coarse_band'], 'p_mod_30': stratum['p_mod_30'],
                    'q_mod_30': stratum['q_mod_30'], 'source_p': origin['p'],
                    'source_total_row_count': origin['count'],
                    'source_channel_count': stratum['source_maximum_count'],
                    'target_p': target['p'], 'target_total_row_count': target_row['count'],
                    'target_observed_channel_count': target['observed_count'],
                    'target_qlo': target['qlo'], 'target_qhi': target['qhi'],
                    'target_integer_residue_capacity': target['integer_residue_capacity'],
                    'specified_assignment_probability_full_support': stratum['specified_source_to_target_probability'],
                    'specified_assignment_probability_positive_subset':
                        {'numerator': 1, 'denominator': positive_group_size} if survives_positive_mask else None,
                }
                if survives_positive_mask and first_positive is None:
                    first_positive = witness
                elif not survives_positive_mask and first_zero is None:
                    first_zero = witness
        audit = cell['null_A_capacity_audit']
        assert positive + zero == audit['violating_target_channel_count']
        assert cell['corrected_profiles'] is None and cell['signed_residual_profiles'] is None
        assert cell['null_profiles'] is None and audit['random_draws'] == 0
        assert sum(sum(row) for row in cell['profiles']['prime_rank_joint']) == cell['totals']['raw']
        assert all(len(cell['profiles'][name]) == 24 for name in ('raw', 'small_trim', 'scale_trim', 'density_flat'))
        cells.append({
            'X': cell['X'], 'width': [cell['num'], cell['den']], 'upper': cell['upper'],
            'totals': cell['totals'], 'overflow_by_view': cell['overflow_by_view'],
            'geometric_rows': len(cell['rows']), 'zero_total_rows': cell['zero_prime_count_rows'],
            'geometrically_empty_windows': len(cell['geometrically_empty_rows']),
            'capacity_status': audit['status'], 'stratum_channel_count': audit['stratum_channel_count'],
            'all_violating_target_channels': positive + zero,
            'positive_total_target_violating_channels': positive,
            'zero_total_target_violating_channels': zero,
            'first_positive_subset_witness': first_positive, 'first_zero_total_target_witness': first_zero,
        })

assert len(cells) == len(summary['cells']) == 21
report = {
    'schema': 'PFSSV_STAGE2_FROZEN_OUTPUT_READOUT_V1',
    'generated_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'argv': sys.argv, 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'input_cell_profiles_sha256': hashlib.sha256(cell_path.read_bytes()).hexdigest(),
    'input_result_summary_sha256': hashlib.sha256(summary_path.read_bytes()).hexdigest(),
    'scope': 'Integer joins, count aggregation and consistency checks on immutable executed outputs; no generation or null sampling.',
    'cells': cells,
    'totals': {
        'completed_cells': len(cells),
        'model_support_failure_cells': sum(c['capacity_status'] == 'MODEL_SUPPORT_FAILURE' for c in cells),
        'cells_with_positive_subset_witness': sum(c['positive_total_target_violating_channels'] > 0 for c in cells),
        'cells_with_zero_total_target_witness': sum(c['zero_total_target_violating_channels'] > 0 for c in cells),
        'violating_cell_target_channels': sum(c['all_violating_target_channels'] for c in cells),
        'positive_subset_violating_cell_target_channels': sum(c['positive_total_target_violating_channels'] for c in cells),
        'zero_total_target_violating_cell_target_channels': sum(c['zero_total_target_violating_channels'] for c in cells),
    },
    'interpretation': [
        'A positive-subset witness has both source and target with positive total observed row count. Removing zero-total rows leaves that specified assignment reachable in the declared stratum. This is not a replay of old floating-point code or random draws.',
        'Zero-total-target witnesses require those target rows to be retained. These are reported separately, not used to explain away the positive-subset obstruction.',
        'Counts concern cell/target/residue violations and can overlap across widths; their sum is not a count of distinct primes, independent trials or a p-value.',
        'The count surrogate remains mathematically defined. Failure is of its universal factor-window occupancy interpretation, not a theorem excluding all conditional randomization or genuine residual structure.',
        'No scientific corrected/signed/null vectors were computed; unavailability is not zero. Already exposed holdouts remain post-exposure. Hard target and formal Result acceptance remain open.',
    ],
}
with args.output.open('x', encoding='utf-8', newline='\n') as output:
    output.write(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'status': 'PASS_FROZEN_OUTPUT_READOUT', 'output': str(args.output),
                  'output_sha256': hashlib.sha256(args.output.read_bytes()).hexdigest(), 'totals': report['totals'],
                  'first_positive_subset_witness': cells[0]['first_positive_subset_witness']}, ensure_ascii=False))
