"""Bind new direct-constructor phase words to the full streaming instrument.

The declared N15/a2/t4 fixture compares two executions of the same actual
native words. It does not execute an ideal propagator or claim a general
factor-success budget at this width or accuracy.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PACKAGE = ROOT.parent
WORD = PACKAGE / 'new_word_compiler'
DIRECT = PACKAGE / 'direct_word_compiler_general'
sys.path.insert(0, str(WORD))

from certified_word_compiler import compile_phase_bank, verify_phase_record
from compiled_streaming import program_from_compilation
from check_compiled_streaming import compare_complete_case, packed
from stage45.brc_loop_recheck import CALLS, verify_vendor
from stage79.phase_compiler import encode


EXPECTED_FILES = {
    WORD / 'certified_word_compiler.py':
        'e8f7048e2e73292bda230a2adad4aaa76f0b3cd5525f8f0899628bd649d1d81d',
    WORD / 'compiled_streaming.py':
        'd0f980b7ff5fb41438e9e0ad40af65a190bcd6f83660c821f8362643190a558c',
    WORD / 'check_compiled_streaming.py':
        '0cf231a238f6aa899f1cf7e86a8d7dc8dd3e1aeda33e3c1b6c371ef10804a9ce',
    DIRECT / 'construct_general_word.py':
        '830b2f0c0c206a53e2b349fe377976d369ebfb76d4dfc5aad494db88ab6e0c63',
}
IMPORTED_PHASES = {
    3: ('M3_DELTA_EIGHTH.json.gz', F(1, 8),
        '0a712b1a918aa7326785605bdbc0e30453962c897286d9e293710f41318858d6'),
    4: ('M4_DELTA_QUARTER.json.gz', F(1, 4),
        '1a4ca56447d32704376d4537da3e28550800ac4245093d6e303cef4b4918268c'),
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def bound_sources():
    sources = {}
    for path, expected in EXPECTED_FILES.items():
        actual = sha(path.read_bytes())
        if actual != expected:
            raise ValueError(f'source changed: {path.name}')
        sources[str(path.relative_to(PACKAGE))] = actual
    sources[str(Path(__file__).relative_to(PACKAGE))] = sha(Path(__file__).read_bytes())
    return sources


def load_phase(m):
    filename, tolerance, expected = IMPORTED_PHASES[m]
    path = DIRECT / filename
    compressed = path.read_bytes()
    raw = gzip.decompress(compressed)
    if sha(raw) != expected:
        raise ValueError('direct-constructor artifact hash mismatch')
    payload = json.loads(raw)
    record = payload['phase_record']
    if record['status'] != 'CERTIFIED' or record['phase_index'] != m:
        raise ValueError('imported phase has wrong status or target')
    if record['dim'] != 61 or F(record['operator_error_bound']) != tolerance:
        raise ValueError('imported phase has wrong full-carrier accuracy')
    replay = verify_phase_record(record)
    if replay['status'] != 'VERIFIED':
        raise ValueError('imported phase did not replay')
    provenance = {
        'artifact': str(path.relative_to(PACKAGE)),
        'uncompressed_payload_sha256': expected,
        'gzip_sha256': sha(compressed),
        'phase_index': m,
        'operator_error_bound': tolerance,
        'word_length': len(record['word']),
        'source_certificate_sha256': record['certificate_sha256'],
        'fresh_phase_record_replay': replay,
        'construction_receipts_scope': 'retained in the hash-bound constructor artifact; this run freshly replays the complete phase certificate',
    }
    return record, provenance


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--activity', default='RA-CAAAC604CB513AEA8BBC1DFC')
    args = parser.parse_args()
    sources = bound_sources()
    kernel = verify_vendor()
    first_call = len(CALLS)
    dense_calls = []

    def observe(frame, event, arg):
        if (event == 'call' and frame.f_code.co_name == 'modular_columns'
                and frame.f_globals.get('__name__') == 'stage78.shor_benchmark'):
            dense_calls.append({'N': frame.f_locals.get('N'), 'b': frame.f_locals.get('b')})

    sys.setprofile(observe)
    try:
        # This is the frozen exact quarter-turn word, certified afresh by the
        # unchanged compiler. It uses neither old approximate phase seeds nor
        # a newly inserted target propagator.
        quarter = compile_phase_bank(2, F(1), pair_budget=1,
                                     observer_start_bits=3, activity=args.activity)
        assert quarter['status'] == 'CERTIFIED'
        phase2 = quarter['phases']['2']
        assert F(phase2['operator_error_bound']) == 0
        assert tuple(map(tuple, phase2['word'])) == (('swap', 0, 1), ('neg', 1))
        phases, provenance = {'2': phase2}, {}
        for m in (3, 4):
            phases[str(m)], provenance[str(m)] = load_phase(m)
            print(json.dumps({'phase_index': m, 'status': 'FRESH_RECORD_VERIFIED',
                              'word_length': len(phases[str(m)]['word'])}), flush=True)

        compilation = {
            'status': 'CERTIFIED', 't': 4, 'dim': 61, 'epsilon': '1',
            'phases': phases, 'occurrence_weighted_error_bound': '1/2',
            'bound_is_for_complete_bank': True,
            'profile': 'imported independently constructed words; exact m2, m3 delta1/8, m4 delta1/4',
            'cursor': None,
        }
        # The existing importer rechecks every record (including m2), its
        # complete native action, target/source binding and occurrence sum.
        adapted = program_from_compilation(15, 2, 4, compilation, epsilon=F(1))
        assert adapted['status'] == 'CERTIFIED' and adapted['dim'] == 61
        assert F(adapted['error_certificate']['telescoping_sum']) == F(1, 2)
        assert F(adapted['error_certificate']['terminal_TV_bound']) == F(1, 2)
        case = compare_complete_case(adapted['program'])
        assert case['all_joint_amplitudes_exact_equal']
        assert case['all_original_source_amplitudes_inverse_recovered']
        assert case['all_leaf_slots'] == 16 and case['dim'] == 61
        assert not dense_calls
        print(json.dumps({'fixture': [15, 2, 4],
                          'all_joint_coordinates': case['full_joint_amplitude_coordinate_comparisons'],
                          'inverse_coordinates': case['full_inverse_coordinate_comparisons'],
                          'status': 'EXACT_EQUAL'}), flush=True)
    finally:
        sys.setprofile(None)

    payload = {
        'schema': 'DIRECT_WORD_COMPLETE_STREAMING_INTEGRATION_V1',
        'status': 'AUTHOR_ACTUAL_BOUNDED_INTEGRATION_SHARED_CONTEXT_NOT_ADMITTED',
        'activity': args.activity, 'kernel': kernel, 'source_files_sha256': sources,
        'imported_constructor_artifacts': provenance,
        'phase_compilation': compilation,
        'compiled_error_certificate': adapted['error_certificate'],
        'native_word_adapter_bindings': adapted['word_bindings'],
        'case': case,
        'native_call_receipts': CALLS[first_call:],
        'actual_BRC_core_calls': len(CALLS)-first_call,
        'dense_modular_entrypoint_observations': dense_calls,
        'whole_carrier_dimension': 61,
        'old_approximate_seed_bank_used': False,
        'new_ideal_reference_execution': False,
        'new_float_or_trigonometric_propagator': False,
        'standard_N15_t_equals_2n_claimed': False,
        'positive_general_CF_lower_bound_from_E_claimed': False,
        'retry_transcript_TV_claimed': False,
        'scope': 'new direct-constructor words admitted through the existing complete importer; same actual-word full/streaming amplitudes for declared N15/a2/t4 only',
    }
    raw = packed(payload)
    target = ROOT / 'DIRECT_WORD_INTEGRATION_RESULTS.json.gz'
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
    summary['payload_sha256'] = sha(raw)
    summary['gzip_sha256'] = sha(target.read_bytes())
    summary['uncompressed_bytes'] = len(raw)
    (ROOT / 'DIRECT_WORD_INTEGRATION_SUMMARY.json').write_text(
        json.dumps(encode(summary), ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'actual_BRC_core_calls': payload['actual_BRC_core_calls'],
                      'payload_sha256': summary['payload_sha256'], 'output': str(target)}), flush=True)


if __name__ == '__main__':
    main()
