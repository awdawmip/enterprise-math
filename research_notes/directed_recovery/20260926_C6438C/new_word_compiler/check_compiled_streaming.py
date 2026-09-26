"""Bounded complete-amplitude integration checks for certified native words.

Both compared routes execute the same actual word bank. The full route is
never an ideal numerical QFT reference. Modular maps are sparse BRC columns.
"""
from __future__ import annotations

import gzip
import argparse
import hashlib
import json
import random
from copy import deepcopy
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
for directory in ('integration', 'sparse'):
    sys.path.insert(0, str(ROOT.parent / directory))
from general_streaming import GeneralStreamingProgram
from general_driver import sample_once
from terminal_instrument import streaming_leaves
from sparse_modular import (sparse_classical_postprocess,
                            compile_modular_permutation, digest)
from stage80.fixed_phase import h4_step, run_qft, law, norm
from stage79.phase_compiler import encode
from stage45.brc_loop_recheck import CALLS, verify_vendor
from compiled_streaming import compile_bank, bank_from_compilation, program_from_compilation


def packed(value):
    return json.dumps(encode(value), sort_keys=True,
                      separators=(',', ':')).encode('utf-8')


def stored_state(state):
    return [{'key': key, 'numerators': row} for key, row in sorted(state.items())]


def sparse_full_preparation(program):
    """Prepare all small-fixture controls with actual H4 and sparse columns."""
    state, denominator = program.initial()
    events = []
    for bit in range(program.t):
        state, denominator = h4_step(state, denominator, bit, program.dim)
        events.append({'operation': 'actual_prepare_H4', 'bit': bit,
                       'endpoints': len(state), 'mass': norm(state, denominator)})
    for bit, table in enumerate(reversed(program.tables)):
        state = {(x, table[w] if (x >> bit) & 1 else w, spectator): row
                 for (x, w, spectator), row in state.items()}
        events.append({'operation': 'sparse_controlled_modular_columns',
                       'bit': bit, 'endpoints': len(state),
                       'mass': norm(state, denominator)})
    assert norm(state, denominator) == 1
    assert all(spectator == 0 for _, _, spectator in state)
    certificates = {}
    for b in program.modular_powers:
        _, certificate = compile_modular_permutation(program.N, b)
        certificates[digest(certificate)] = certificate
    return state, denominator, events, certificates


def compare_complete_case(program):
    """Compare all joint coordinates and every terminal bin of one input."""
    source, source_den, preparation, modular_certificates = sparse_full_preparation(program)
    full, full_den, full_trace = run_qft(source, source_den, program.t,
                                       program.bank, program.dim, trace=True)
    full_nums, full_probability_den = law(full, full_den, program.t)
    restored, restored_den, _ = run_qft(full, full_den, program.t,
                                      program.bank, program.dim, inverse=True)
    inverse_comparisons = 0
    for key in set(source) | set(restored):
        left = source.get(key, (0,)*program.dim)
        right = restored.get(key, (0,)*program.dim)
        assert all(a*restored_den == b*source_den for a, b in zip(left, right))
        inverse_comparisons += program.dim

    leaves = streaming_leaves(program)
    joined = {}
    bins = [F(0)]*(1 << program.t)
    retained_leaves = []
    for history, state, denominator in leaves:
        k = sum(bit << i for i, bit in enumerate(history))
        bins[k] = norm(state, denominator)
        retained_leaves.append({'history': history, 'k': k,
                                'denominator': denominator,
                                'state': stored_state(state)})
        for (x, work, spectator), row in state.items():
            assert x == spectator == 0
            joined[k, work, spectator] = (row, denominator)
    amplitude_comparisons = 0
    for key in set(full) | set(joined):
        left = full.get(key, (0,)*program.dim)
        right, denominator = joined.get(key, ((0,)*program.dim, 1))
        assert all(a*denominator == b*full_den for a, b in zip(left, right))
        amplitude_comparisons += program.dim
    assert all(value == F(full_nums[k], full_probability_den)
               for k, value in enumerate(bins))
    assert sum(bins) == 1
    posts = {k: sparse_classical_postprocess(program.N, program.a, program.t, k)
             for k in range(1 << program.t)}
    success = sum((bins[k] for k in posts if posts[k]['factors']), F(0))
    status_law = {}
    for k, post in posts.items():
        status = post['status']
        status_law[status] = status_law.get(status, F(0)) + bins[k]
    sample = sample_once(program, random.Random(20260927),
                         postprocess=sparse_classical_postprocess)
    assert F(sample['history_probability']) == bins[sample['k']]
    assert sample['postprocessing'] == posts[sample['k']]
    return {'N': program.N, 'a': program.a, 't': program.t, 'dim': program.dim,
        'full_joint_amplitude_coordinate_comparisons': amplitude_comparisons,
        'full_inverse_coordinate_comparisons': inverse_comparisons,
        'all_joint_amplitudes_exact_equal': True,
        'all_control_bins_exact_equal': True,
        'all_original_source_amplitudes_inverse_recovered': True,
        'all_modes_retained': True, 'all_leaf_slots': len(leaves),
        'zero_leaf_slots': sum(not state for _, state, _ in leaves),
        'control_law': bins, 'postprocessing': posts,
        'success_probability': success, 'status_law': status_law,
        'software_sample': sample,
        'software_sample_is_not_a_uniform_frequency_validation': True,
        'full_preparation_events': preparation,
        'complete_sparse_modular_certificates': modular_certificates,
        'full_source_state': stored_state(source),
        'full_source_denominator': source_den,
        'full_terminal_state': stored_state(full),
        'full_terminal_denominator': full_den,
        'all_streaming_terminal_leaves': retained_leaves,
        'full_actual_word_circuit_trace': full_trace,
        'streaming_metrics': program.report_metrics(),
        'ideal_reference_execution': False,
        'scope': 'all joint output coordinates for this declared input; both routes use the same certified words'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--activity', required=True)
    args = parser.parse_args()
    kernel = verify_vendor()
    first_call = len(CALLS)
    dense_calls = []
    def observe(frame, event, arg):
        if (event == 'call' and frame.f_code.co_name == 'modular_columns'
                and frame.f_globals.get('__name__') == 'stage78.shor_benchmark'):
            dense_calls.append({'N': frame.f_locals.get('N'),
                                'b': frame.f_locals.get('b')})
    sys.setprofile(observe)
    try:
        # Seed words are existing actual fixed-bank words. Their new target
        # error certificates are obtained by the new compiler, not inherited
        # from a label or an old per-word error figure.
        from terminal_instrument import load_frozen_bank
        oldbank, _, dim = load_frozen_bank(6)
        assert dim == 61
        seeds = {m: [oldbank[m].inverse_phase_word] for m in range(3, 7)}
        epsilon = F(1, 1_000_000)
        options = {'seed_words': seeds, 'observer_start_bits': 64,
                   'activity': args.activity}
        partial = compile_bank(4, epsilon, pair_budget=1, **options)
        assert partial['status'] == 'PARTIAL' and partial['bank'] is None
        blocked = program_from_compilation(15, 2, 4, partial['compilation'],
                                           epsilon=epsilon)
        assert blocked['status'] == 'PARTIAL' and blocked['program'] is None
        assert blocked['bank'] is None
        print('PARTIAL bank retained; no program constructed', flush=True)
        ready4 = compile_bank(4, epsilon, cursor=partial['cursor'],
                              pair_budget=8, **options)
        ready6 = compile_bank(6, epsilon, pair_budget=8, **options)
        assert ready4['status'] == ready6['status'] == 'CERTIFIED'
        negative_controls = []
        # Both forged records are internally well shaped. For the false bound,
        # also adjust the advertised bank sum so that a mere arithmetic budget
        # check would accept it. The source-bound phase verifier must reject it.
        changed_word = deepcopy(ready4['compilation'])
        changed_word['phases']['3']['word'].append(['neg', 60])
        changed_bound = deepcopy(ready4['compilation'])
        old_bound = F(changed_bound['phases']['3']['operator_error_bound'])
        changed_bound['phases']['3']['operator_error_bound'] = '0'
        changed_bound['occurrence_weighted_error_bound'] = str(
            F(changed_bound['occurrence_weighted_error_bound'])-2*old_bound)
        for label, changed in (('changed_word_original_certificate', changed_word),
                                ('false_bound_consistent_bank_sum', changed_bound)):
            try:
                bank_from_compilation(changed, t=4, epsilon=epsilon)
            except ValueError as error:
                negative_controls.append({'case': label, 'rejected': True,
                                          'reason': str(error)})
            else:
                raise AssertionError('tampered phase record was accepted')
        cases, compilation_records = [], {}
        for N, a, t, result in ((15, 2, 4, ready4), (21, 2, 6, ready6)):
            bound = program_from_compilation(N, a, t, result['compilation'],
                                              epsilon=epsilon)
            assert bound['status'] == 'CERTIFIED'
            record = compare_complete_case(bound['program'])
            record['compiled_error_certificate'] = bound['error_certificate']
            record['native_word_adapter_bindings'] = bound['word_bindings']
            cases.append(record)
            compilation_records[str(t)] = result['compilation']
            print(json.dumps({'case': [N, a, t],
                'all_joint_coordinates': record['full_joint_amplitude_coordinate_comparisons'],
                'success_probability': str(record['success_probability'])}), flush=True)
        assert not dense_calls
    finally:
        sys.setprofile(None)
    payload = {'schema': 'BRC_CERTIFIED_WORD_STREAMING_INTEGRATION_V1',
        'activity': args.activity,
        'status': 'AUTHOR_EXECUTED_BOUNDED_INTEGRATION_UNREVIEWED_NOT_ADMITTED',
        'kernel': kernel, 'cases': cases,
        'phase_compilations': compilation_records,
        'partial_compilation': partial['compilation'],
        'partial_bank_prevented_program_construction': True,
        'partial_compilation_resumed_to_complete': True,
        'tampered_certificate_binding_negative_controls': negative_controls,
        'dense_modular_entrypoint_observations': dense_calls,
        'actual_BRC_core_calls': len(CALLS)-first_call,
        'native_call_receipts': CALLS[first_call:],
        'whole_carrier_dimension': 61,
        'new_target_observer_start_bits': 64,
        'old_target32_vector64_word_seeds_unchanged': True,
        'new_ideal_reference_execution': False,
        'new_float_or_trigonometric_propagator': False,
        'retry_transcript_TV_claimed': False,
        'scope': 'exact same-actual-word full/streaming replay for two small inputs; single-terminal error budgets only'}
    raw = packed(payload)
    target = ROOT/'COMPILED_STREAMING_RESULTS.json.gz'
    target.write_bytes(gzip.compress(raw, mtime=0))
    assert gzip.decompress(target.read_bytes()) == raw
    summary = {key: value for key, value in payload.items()
               if key not in ('cases', 'phase_compilations', 'partial_compilation',
                              'native_call_receipts')}
    summary['payload_sha256'] = hashlib.sha256(raw).hexdigest()
    summary['case_summaries'] = [{key: case[key] for key in (
        'N', 'a', 't', 'dim', 'all_leaf_slots', 'zero_leaf_slots',
        'full_joint_amplitude_coordinate_comparisons',
        'full_inverse_coordinate_comparisons',
        'all_joint_amplitudes_exact_equal', 'all_control_bins_exact_equal',
        'all_original_source_amplitudes_inverse_recovered',
        'success_probability', 'compiled_error_certificate')} for case in cases]
    (ROOT/'COMPILED_STREAMING_SUMMARY.json').write_text(
        json.dumps(encode(summary), ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(encode(summary), ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
