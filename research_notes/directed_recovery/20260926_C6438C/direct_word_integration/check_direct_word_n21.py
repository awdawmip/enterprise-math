"""N21/t4 complete comparison using the already certified direct-word bank.

This adds an input on which actual residual coordinates become occupied.
No approximate phase is recompiled and no ideal propagator is executed.
"""
from __future__ import annotations

import gzip
import json
import sys
from fractions import Fraction as F
from pathlib import Path

import check_direct_word_integration as previous


ROOT = Path(__file__).resolve().parent
N15_PAYLOAD = '79491e65feec104f2cdc9de510263efef749d8a1174f9cab4c20146a0171615c'


def main():
    sources = previous.bound_sources()
    sources[str(Path(__file__).relative_to(previous.PACKAGE))] = previous.sha(Path(__file__).read_bytes())
    source_path = ROOT / 'DIRECT_WORD_INTEGRATION_RESULTS.json.gz'
    raw_source = gzip.decompress(source_path.read_bytes())
    if previous.sha(raw_source) != N15_PAYLOAD:
        raise ValueError('certified direct-word bank archive changed')
    saved = json.loads(raw_source)
    compilation = saved['phase_compilation']
    assert compilation['t'] == 4 and compilation['dim'] == 61
    assert compilation['occurrence_weighted_error_bound'] == '1/2'
    kernel = previous.verify_vendor()
    first_call = len(previous.CALLS)
    dense_calls = []

    def observe(frame, event, arg):
        if (event == 'call' and frame.f_code.co_name == 'modular_columns'
                and frame.f_globals.get('__name__') == 'stage78.shor_benchmark'):
            dense_calls.append({'N': frame.f_locals.get('N'), 'b': frame.f_locals.get('b')})

    sys.setprofile(observe)
    try:
        # This is fresh complete record/native/target replay by the importer,
        # not trust in the archive's previous verification status.
        adapted = previous.program_from_compilation(21, 2, 4, compilation, epsilon=F(1))
        assert adapted['status'] == 'CERTIFIED' and adapted['dim'] == 61
        assert F(adapted['error_certificate']['telescoping_sum']) == F(1, 2)
        case = previous.compare_complete_case(adapted['program'])
        residual_numerator = sum(x*x for row in case['full_terminal_state']
                                 for x in row['numerators'][2:])
        residual_mass = F(residual_numerator, case['full_terminal_denominator']**2)
        assert residual_mass > 0
        assert case['all_joint_amplitudes_exact_equal']
        assert case['all_original_source_amplitudes_inverse_recovered']
        assert case['all_leaf_slots'] == 16
        assert not dense_calls
    finally:
        sys.setprofile(None)

    payload = {
        'schema': 'DIRECT_WORD_RESIDUAL_STREAMING_INTEGRATION_V1',
        'status': 'AUTHOR_ACTUAL_BOUNDED_INTEGRATION_SHARED_CONTEXT_NOT_ADMITTED',
        'activity': saved['activity'], 'kernel': kernel, 'source_files_sha256': sources,
        'bank_archive': {'artifact': source_path.name, 'payload_sha256': N15_PAYLOAD},
        'imported_constructor_artifacts': saved['imported_constructor_artifacts'],
        'phase_compilation': compilation,
        'compiled_error_certificate': adapted['error_certificate'],
        'native_word_adapter_bindings': adapted['word_bindings'],
        'case': case, 'full_terminal_residual_mass': residual_mass,
        'actual_residual_mass_strictly_positive': True,
        'native_call_receipts': previous.CALLS[first_call:],
        'actual_BRC_core_calls': len(previous.CALLS)-first_call,
        'dense_modular_entrypoint_observations': dense_calls,
        'whole_carrier_dimension': 61,
        'new_approximate_phase_compilation': False,
        'new_ideal_reference_execution': False,
        'new_float_or_trigonometric_propagator': False,
        'standard_N21_t_equals_2n_claimed': False,
        'positive_general_CF_lower_bound_from_E_claimed': False,
        'retry_transcript_TV_claimed': False,
        'scope': 'same actual direct words on declared N21/a2/t4; full/streaming equality includes positive retained residual mass, not a default-width strong factorization budget',
    }
    raw = previous.packed(payload)
    target = ROOT / 'DIRECT_WORD_N21_RESULTS.json.gz'
    target.write_bytes(gzip.compress(raw, mtime=0))
    assert gzip.decompress(target.read_bytes()) == raw
    summary = {key: value for key, value in payload.items() if key not in
               ('case', 'phase_compilation', 'native_word_adapter_bindings', 'native_call_receipts')}
    summary['case_summary'] = {key: case[key] for key in (
        'N', 'a', 't', 'dim', 'all_leaf_slots', 'zero_leaf_slots',
        'full_joint_amplitude_coordinate_comparisons',
        'full_inverse_coordinate_comparisons', 'all_joint_amplitudes_exact_equal',
        'all_control_bins_exact_equal', 'all_original_source_amplitudes_inverse_recovered',
        'all_modes_retained', 'success_probability', 'streaming_metrics')}
    summary['payload_sha256'] = previous.sha(raw)
    summary['gzip_sha256'] = previous.sha(target.read_bytes())
    summary['uncompressed_bytes'] = len(raw)
    (ROOT / 'DIRECT_WORD_N21_SUMMARY.json').write_text(
        json.dumps(previous.encode(summary), ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'fixture': [21, 2, 4],
        'joint_coordinates': case['full_joint_amplitude_coordinate_comparisons'],
        'inverse_coordinates': case['full_inverse_coordinate_comparisons'],
        'residual_mass_positive': True, 'all_leaves': case['all_leaf_slots'],
        'actual_BRC_core_calls': payload['actual_BRC_core_calls'],
        'payload_sha256': summary['payload_sha256']}), flush=True)


if __name__ == '__main__':
    main()
