"""Bounded actual joint-law, same-tape and live-resume composition checks."""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
from collections import defaultdict
import gzip
import hashlib
import json
import random
import sys

ROOT = Path(__file__).resolve().parent
for path in (ROOT.parent / 'gram_research', ROOT.parent / 'point_queries'):
    sys.path.insert(0, str(path))
from character_walker import CharacterWalker
from single_walker import SingleWalker
from checkpoint_row_oracle import CheckpointRowOracle
from check_single_walker import (load_bank, serializable, observed, state_row_norms,
    LazyStreamingProgram, SelectedStreamingProgram, ExactCarrierCodec,
    PositivePathObserver, packed, CALLS, verify_vendor, PREVIOUS)


class DesiredStepRandom:
    """A declared possible two-coin fixture, never a randomness claim."""
    def __init__(self, auxiliary, bit):
        self.values = iter((auxiliary, bit))
        self.calls = []

    def randrange(self, stop):
        desired = next(self.values)
        value = 0 if desired == 0 else stop-1
        self.calls.append({'stop': stop, 'value': value})
        return value


class RecordedRandom:
    def __init__(self, seed):
        self.generator = random.Random(seed)
        self.calls = []

    def randrange(self, stop):
        value = self.generator.randrange(stop)
        self.calls.append({'stop': stop, 'value': value})
        return value


class FiniteRandom:
    def __init__(self, values):
        self.values = iter(values)

    def randrange(self, stop):
        return 0 if next(self.values) == 0 else stop-1


def program_for(bank, N=21, a=2):
    return LazyStreamingProgram(N, a, 4, bank, 61,
        codec=ExactCarrierCodec(61, tuple(range(6))))


def prior_reachable_witnesses():
    source = ROOT.parent / 'gram_research/SINGLE_WALKER_RESULTS.json.gz'
    raw = gzip.decompress(source.read_bytes())
    expected = '0c50447c0697d1d0ec66356ac5225f55494de60d0877a6e5d48bd66cf45f597a'
    assert hashlib.sha256(raw).hexdigest() == expected
    case = json.loads(raw)['cases'][0]
    lookup = {(tuple(prefix['history']), plan['latent_before'], plan['auxiliary_bit']): plan
              for prefix in case['prefix_evidence'] for plan in prefix['transitions']}
    witnesses = {((), 1): ()}
    for depth in range(3):
        following = {}
        for (history, latent), tape in witnesses.items():
            for auxiliary in (0, 1):
                plan = lookup[(history, latent, auxiliary)]
                p0 = F(plan['bit_probability_given_proposed_label'])
                for bit in (0, 1):
                    if (p0 if bit == 0 else 1-p0) > 0:
                        key = (history+(bit,), plan['candidate'])
                        following.setdefault(key, tape+((auxiliary, bit),))
        witnesses = following
    return witnesses, {'payload_sha256': expected,
        'reuse_scope': 'previous actual positive-transition witnesses; every chosen prefix is replayed here'}


def replay_prefix(walker, tape):
    for auxiliary, bit in tape:
        event = walker.step(DesiredStepRandom(auxiliary, bit))
        assert event['selected_bit'] == bit and event['auxiliary_bit'] == auxiliary


def check_full_final_joint(bank):
    program = program_for(bank)
    explicit = SelectedStreamingProgram(21, 2, 4, bank, 61,
        codec=ExactCarrierCodec(61, tuple(range(6))))
    state, den = explicit.initial()
    frontier = {(): (state, den)}
    for depth in range(3):
        following = {}
        for history, (state, den) in frontier.items():
            for bit, (child, child_den) in enumerate(explicit.branches(state, den, history)):
                if child:
                    following[history+(bit,)] = (child, child_den)
        frontier = following
    witnesses, prior_binding = prior_reachable_witnesses()
    observer = PositivePathObserver()
    trials, comparisons = [], []
    for history, (state, den) in sorted(frontier.items()):
        parent_norms = state_row_norms(state, den, observer)
        terms = defaultdict(list)
        for latent, mass in sorted(parent_norms.items()):
            tape = witnesses[(history, latent)]
            for auxiliary in (0, 1):
                walker = CharacterWalker(program)
                replay_prefix(walker, tape)
                assert walker.history == history and walker.latent == latent
                before = walker.oracle.report()
                # No point-query allowance remains. The typed character proof
                # has its own separately recorded construction/replay cost.
                walker.oracle.query_budget = before['operation_units_used']
                event = walker.step(DesiredStepRandom(auxiliary, 0))
                after = walker.oracle.report()
                assert event['mode'] == 'CERTIFIED_FINAL_CHARACTER'
                assert event['row_query_performed'] is False
                assert after['query_requests'] == before['query_requests']
                assert after['operation_units_used'] == before['operation_units_used']
                for bit in (0, 1):
                    terms[(bit, event['candidate'])].append((mass, F(1, 2), F(1, 2)))
                trials.append({'history': history, 'latent': latent,
                    'auxiliary_bit': auxiliary, 'witness_tape': tape,
                    'event': event, 'before_oracle_report': before,
                    'after_oracle_report': after, 'evidence': walker.evidence()})
        children = explicit.branches(state, den, history)
        for bit, (child, child_den) in enumerate(children):
            predicted = {label: observed(observer, 'certified_character_joint_mass', value)
                         for (b, label), value in terms.items() if b == bit}
            expected = state_row_norms(child, child_den, observer)
            assert predicted == expected
            comparisons.append({'history': history+(bit,), 'all_joint_label_masses_equal': True,
                                'joint_label_masses': sorted(predicted.items())})
    return {'N': 21, 'a': 2, 't': 4, 'dim': 6, 'prior_witness_source': prior_binding,
        'positive_final_parent_histories': len(frontier), 'live_replayed_shortcut_trials': len(trials),
        'child_histories_compared': len(comparisons),
        'all_joint_branch_work_label_masses_equal': True,
        'all_final_row_query_counts_zero': True, 'trials': trials,
        'comparisons': comparisons, 'comparison_observer': observer.operations,
        'explicit_metrics': explicit.report_metrics()}


def comparable_events(events):
    fields = ('history', 'latent_before', 'auxiliary_bit', 'candidate',
              'selected_bit', 'selected_local_probability')
    return [tuple(event[key] for key in fields) for event in events]


def compare_same_tape(bank, N):
    program = program_for(bank, N)
    baseline = SingleWalker(program, oracle=CheckpointRowOracle(program))
    optimized = CharacterWalker(program)
    left, right = RecordedRandom(927271), RecordedRandom(927271)
    first, second = baseline.run(left), optimized.run(right)
    assert first['status'] == second['status'] == 'COMPLETE_READOUT'
    assert first['history'] == second['history'] and first['latent_work_label'] == second['latent_work_label']
    assert comparable_events(first['events']) == comparable_events(second['events'])
    assert left.calls == right.calls
    if N == 21:
        assert optimized.shortcut_rounds == 1
    else:
        assert optimized.character_certificate['status'] == 'UNAVAILABLE'
        assert optimized.shortcut_rounds == 0
        assert first['oracle_report']['operation_units_used'] == second['oracle_report']['operation_units_used']
    return {'N': N, 'a': 2, 'same_tape_and_selected_trajectory': True,
        'baseline': first, 'optimized': second, 'random_tape': left.calls,
        'baseline_oracle': baseline.oracle.evidence(), 'optimized_evidence': optimized.evidence(),
        'saved_root_point_queries': first['oracle_report']['root_query_calls']-second['oracle_report']['root_query_calls'],
        'saved_recursive_nodes': first['oracle_report']['point_node_visits']-second['oracle_report']['point_node_visits'],
        'saved_oracle_operation_units': first['oracle_report']['operation_units_used']-second['oracle_report']['operation_units_used'],
        'runtime_speedup_claimed': False, 'typed_tables_are_shared_and_warm': True}


def boundary_checks(bank):
    program = program_for(bank)
    walker = CharacterWalker(program, query_budget=0)
    stopped = walker.run(FiniteRandom([0]))
    assert stopped['status'] == 'INCOMPLETE_POINT_QUERY_BUDGET'
    assert not walker.history and walker.latent == 1 and walker.pending_auxiliary_bit == 0
    walker.oracle.query_budget = 100000
    for _ in range(3):
        walker.step(FiniteRandom([0, 0]))
    assert len(walker.history) == 3
    before = walker.oracle.report()
    walker.oracle.query_budget = before['operation_units_used']
    interrupted = walker.run(FiniteRandom([1]))
    assert interrupted['status'] == 'INCOMPLETE_RANDOM_SOURCE'
    assert len(walker.history) == 3 and walker.pending_auxiliary_bit == 1
    assert walker.pending_plan['mode'] == 'CERTIFIED_FINAL_CHARACTER'
    preserved = (walker.latent, walker.pending_plan['candidate'])
    resumed = walker.run(FiniteRandom([1]))
    assert resumed['status'] == 'COMPLETE_READOUT' and walker.history[-1] == 1
    assert walker.latent == preserved[1]
    assert walker.oracle.report()['operation_units_used'] == before['operation_units_used']
    assert not stopped['events'] and len(interrupted['events']) == 3

    rejected = []
    for label, mutate in (
            ('external_history', lambda w: setattr(w.oracle, 'history', (0,))),
            ('external_latent', lambda w: setattr(w, 'latent', 2))):
        invalid = CharacterWalker(program)
        mutate(invalid)
        try:
            invalid.step(FiniteRandom([0, 0]))
        except ValueError:
            rejected.append(label)
        else:
            raise AssertionError('uncertified initial trajectory accepted')
    forged = CharacterWalker(program)
    forged.character_certificate['schedule_witness']['jacobi']['value'] = 1
    fallback = forged.run(RecordedRandom(927271))
    assert fallback['status'] == 'COMPLETE_READOUT' and forged.shortcut_rounds == 0
    assert forged.verification_receipts and forged.verification_receipts[-1]['verified'] is False
    return {'budget_then_final_rng_pause_resumed': True,
        'zero_remaining_row_query_budget_final_shortcut_completed': True,
        'stopped': stopped, 'interrupted': interrupted, 'resumed': resumed,
        'recovery_evidence': walker.evidence(), 'external_trajectory_controls_rejected': rejected,
        'forged_certificate_replay_rejected_and_original_sampler_completed': True,
        'forged_fallback': fallback, 'forged_evidence': forged.evidence()}


def main():
    files = [Path(__file__), ROOT / 'character_walker.py',
        ROOT.parent / 'gram_research/single_walker.py',
        ROOT.parent / 'point_queries/checkpoint_row_oracle.py',
        ROOT.parent / 'character_certificates/typed_jacobi.py',
        PREVIOUS / 'optimization/streaming/lazy_streaming.py',
        PREVIOUS / 'optimization/lazy_modular/lazy_modular.py',
        PREVIOUS / 'optimization/carrier_codec/carrier_codec.py',
        PREVIOUS / 'new_word_compiler/certified_word_compiler.py']
    sources = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    first = len(CALLS)
    kernel = verify_vendor()
    bank, bank_binding = load_bank()
    joint = check_full_final_joint(bank)
    print('joint law passed', flush=True)
    cases = [compare_same_tape(bank, N) for N in (21, 15)]
    boundary = boundary_checks(bank)
    assert sources == {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    output = {'status': 'AUTHOR_ACTUAL_CHARACTER_CHECKPOINT_COMPOSITION_SHARED_CONTEXT_NOT_ADMITTED',
        'activity': 'RA-CAAAC604CB513AEA8BBC1DFC', 'kernel': kernel,
        'source_bank': bank_binding, 'source_sha256': sources, 'sources_unchanged_during_execution': True,
        'final_joint_law': joint, 'same_tape_cases': cases, 'boundary_checks': boundary,
        'actual_BRC_core_calls': len(CALLS)-first, 'actual_BRC_core_receipts': CALLS[first:],
        'ideal_reference_run': False, 'hidden_order_or_factor_input': False,
        'scope': 'one certified final bit avoids row queries; no whole-algorithm complexity or runtime-speedup claim'}
    raw = packed(serializable(output))
    target = ROOT / 'CHARACTER_WALKER_RESULTS.json.gz'
    target.write_bytes(gzip.compress(raw, mtime=0))
    assert gzip.decompress(target.read_bytes()) == raw
    summary = {key: output[key] for key in ('status', 'activity', 'source_bank', 'source_sha256',
        'sources_unchanged_during_execution', 'actual_BRC_core_calls', 'ideal_reference_run',
        'hidden_order_or_factor_input', 'scope')}
    summary['final_joint_law'] = {key: joint[key] for key in ('N', 'a', 't', 'dim',
        'positive_final_parent_histories', 'live_replayed_shortcut_trials',
        'child_histories_compared', 'all_joint_branch_work_label_masses_equal',
        'all_final_row_query_counts_zero')}
    summary['same_tape_cases'] = [{key: case[key] for key in ('N', 'a',
        'same_tape_and_selected_trajectory', 'saved_root_point_queries', 'saved_recursive_nodes',
        'saved_oracle_operation_units', 'runtime_speedup_claimed', 'typed_tables_are_shared_and_warm')}
        | {'character_report': case['optimized']['character_optimization'],
           'baseline_oracle_report': case['baseline']['oracle_report'],
           'optimized_oracle_report': case['optimized']['oracle_report']} for case in cases]
    summary['boundary_checks'] = {key: boundary[key] for key in (
        'budget_then_final_rng_pause_resumed', 'zero_remaining_row_query_budget_final_shortcut_completed',
        'external_trajectory_controls_rejected', 'forged_certificate_replay_rejected_and_original_sampler_completed')}
    summary['payload_sha256'] = hashlib.sha256(raw).hexdigest()
    summary['gzip_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
    (ROOT / 'CHARACTER_WALKER_SUMMARY.json').write_text(
        json.dumps(json.loads(packed(serializable(summary))), indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': output['status'], 'calls': output['actual_BRC_core_calls'],
        'payload_sha256': summary['payload_sha256'], 'cases': [
            {'N': case['N'], 'saved_root_queries': case['saved_root_point_queries'],
             'saved_nodes': case['saved_recursive_nodes']} for case in cases]}), flush=True)


if __name__ == '__main__':
    main()
