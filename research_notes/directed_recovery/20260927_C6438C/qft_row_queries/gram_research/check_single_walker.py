"""Actual small joint-law enumeration; never an ideal-QFT reference."""
from __future__ import annotations
from dataclasses import asdict, is_dataclass
from fractions import Fraction as F
from pathlib import Path
from collections import defaultdict
import gzip
import hashlib
import json
import random
import sys

ROOT = Path(__file__).resolve().parent
PREVIOUS = ROOT.parents[1] / 'sep26-shor-general'
for path in (PREVIOUS / 'optimization/collision_analysis',
             PREVIOUS / 'optimization/carrier_codec',
             PREVIOUS / 'optimization/lazy_modular'):
    sys.path.insert(0, str(path))
from single_walker import (RawRow, PointRowOracle, SingleWalker,
                           QueryBudgetExhausted, transition_plan)
from check_gram_sampler import load_bank
from lazy_streaming import LazyStreamingProgram, SelectedStreamingProgram
from carrier_codec import ExactCarrierCodec
from certified_word_compiler import PositivePathObserver, packed
from stage45.brc_loop_recheck import CALLS, verify_vendor
from stage80.fixed_phase import norm
from lazy_postprocess import lazy_classical_postprocess


def serializable(obj):
    if is_dataclass(obj):
        return serializable(asdict(obj))
    if isinstance(obj, dict):
        return {k: serializable(v) for k, v in obj.items()}
    if isinstance(obj, (tuple, list)):
        return [serializable(v) for v in obj]
    return obj


def observed(observer, name, terms):
    terms = tuple(tuple(term) for term in terms if all(term))
    return observer.evaluate(name, terms) if terms else F(0)


def state_row_norms(state, den, observer):
    return {key[1]: observed(observer, 'actual_explicit_row_squared_norm',
                            ((F(v, den), F(v, den)) for v in row if v))
            for key, row in state.items() if any(row)}


def check_joint_law(bank, use_codec):
    codec = ExactCarrierCodec(61, tuple(range(6))) if use_codec else None
    program = LazyStreamingProgram(21, 2, 4, bank, 61, codec=codec)
    explicit = SelectedStreamingProgram(21, 2, 4, bank, 61, codec=codec)
    state, den = explicit.initial()
    frontier = {(): (state, den, {1: F(1)})}
    observer = PositivePathObserver()
    checks = []
    prefix_evidence = []
    terminal = []
    residue_nonzero = False
    for depth in range(4):
        following = {}
        for history, (state, den, joint) in frontier.items():
            expected = state_row_norms(state, den, observer)
            assert joint == expected
            oracle = PointRowOracle(program, history)
            transitions = []
            terms_by_child = defaultdict(list)
            for latent, mass in sorted(joint.items()):
                assert mass > 0
                for auxiliary in (0, 1):
                    plan = transition_plan(oracle, latent, auxiliary)
                    # These rational masses are actual positive-path observers
                    # of the enumerated sampler kernel, not state propagation.
                    for bit in (0, 1):
                        p = plan['bit_probability_given_proposed_label']
                        if bit:
                            p = 1-p
                        if p:
                            terms_by_child[(bit, plan['candidate'])].append((mass, F(1, 2), p))
                    transitions.append(plan)
            actual_children = explicit.branches(state, den, history)
            for bit, (child, child_den) in enumerate(actual_children):
                child_joint = {label: observed(observer, 'single_walker_joint_transition', terms)
                               for (b, label), terms in terms_by_child.items() if b == bit}
                child_expected = state_row_norms(child, child_den, observer)
                assert child_joint == child_expected
                child_history = history+(bit,)
                child_mass = norm(child, child_den)
                assert sum(child_joint.values(), F(0)) == child_mass
                for row in child.values():
                    residue_nonzero |= any(row[j] for j in range(2, len(row)))
                checks.append({'history': child_history, 'joint_label_count': len(child_joint),
                    'raw_child_mass': child_mass, 'all_joint_label_masses_equal': True,
                    'joint_label_masses': [[label, mass] for label, mass in sorted(child_joint.items())]})
                if child_mass:
                    if depth == 3:
                        terminal.append({'history': child_history, 'joint': child_joint})
                    else:
                        following[child_history] = (child, child_den, child_joint)
            prefix_evidence.append({'history': history, 'transitions': transitions, 'oracle': oracle.evidence()})
        frontier = following
    assert sum((mass for item in terminal for mass in item['joint'].values()), F(0)) == 1
    assert residue_nonzero
    sampler = SingleWalker(program)
    sampled = sampler.run(random.Random(927271), postprocess=lazy_classical_postprocess)
    assert sampled['status'] == 'COMPLETE_READOUT'
    chosen = next(item for item in terminal if item['history'] == tuple(sampled['history']))
    assert chosen['joint'][sampled['latent_work_label']] > 0
    metrics = [item['oracle']['report'] for item in prefix_evidence]
    return {'N': 21, 'a': 2, 't': 4, 'dimension': program.dim,
        'positive_parent_prefixes_checked': len(prefix_evidence),
        'child_history_edges_checked': len(checks),
        'all_joint_branch_and_work_masses_equal': True,
        'retained_residual_nonzero': residue_nonzero,
        'checks': checks, 'prefix_evidence': prefix_evidence,
        'joint_comparison_observer': observer.operations,
        'terminal_joint_law': terminal,
        'seeded_execution_not_frequency_test': sampled, 'sample_oracle': sampler.oracle.evidence(),
        'explicit_metrics': explicit.report_metrics(),
        'prefix_oracle_distinct_queries_sum': sum(m['distinct_queries'] for m in metrics),
        'peak_one_prefix_cached_row_slots': max(m['cached_row_scalar_slots'] for m in metrics),
        'query_count_scope': 'fresh memo per exhaustive checker prefix; a sampled trajectory is separately reported',
        'prototype_program_phase_and_modular_admission_shared_across_prefixes': True}


class ScriptedRandom:
    def __init__(self, choices):
        self.choices = iter(choices)
        self.calls = []

    def randrange(self, stop):
        choice = next(self.choices)
        value = 0 if choice == 0 else stop-1
        self.calls.append({'stop': stop, 'value': value})
        return value


def main():
    files = [Path(__file__), ROOT / 'single_walker.py',
        PREVIOUS / 'optimization/streaming/lazy_streaming.py',
        PREVIOUS / 'optimization/lazy_modular/lazy_modular.py',
        PREVIOUS / 'optimization/lazy_modular/lazy_gcd.py',
        PREVIOUS / 'optimization/lazy_modular/lazy_postprocess.py',
        PREVIOUS / 'optimization/carrier_codec/carrier_codec.py',
        PREVIOUS / 'new_word_compiler/certified_word_compiler.py']
    before = {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in files}
    first = len(CALLS)
    kernel = verify_vendor()
    bank, bank_binding = load_bank()
    cases = [check_joint_law(bank, use_codec) for use_codec in (True, False)]
    assert cases[0]['terminal_joint_law'] == cases[1]['terminal_joint_law']
    assert cases[0]['seeded_execution_not_frequency_test']['history'] == cases[1]['seeded_execution_not_frequency_test']['history']
    assert cases[0]['seeded_execution_not_frequency_test']['latent_work_label'] == cases[1]['seeded_execution_not_frequency_test']['latent_work_label']

    program = LazyStreamingProgram(21, 2, 4, bank, 61, codec=ExactCarrierCodec(61, tuple(range(6))))
    walker = SingleWalker(program, query_budget=0)
    first_rng = ScriptedRandom([0])
    stopped = walker.run(first_rng)
    assert stopped['status'] == 'INCOMPLETE_POINT_QUERY_BUDGET'
    assert not walker.history and walker.latent == 1 and walker.pending_auxiliary_bit == 0
    walker.oracle.query_budget = 1000
    rng_stop = walker.run(ScriptedRandom([]))
    assert rng_stop['status'] == 'INCOMPLETE_RANDOM_SOURCE'
    assert walker.pending_plan is not None and not walker.history
    recovered = walker.run(random.Random(927271))
    assert recovered['status'] == 'COMPLETE_READOUT'
    assert not stopped['events'] and not rng_stop['events']
    assert len(recovered['events']) == 4
    negative = []
    oracle = PointRowOracle(program)
    for label, operation in (
            ('boolean_auxiliary', lambda: transition_plan(oracle, 1, True)),
            ('zero_row_latent', lambda: transition_plan(oracle, 2, 0)),
            ('future_depth', lambda: oracle.query(1, 1)),
            ('boolean_history_bit', lambda: oracle.append(True)),
            ('outside_carrier', lambda: oracle.query(0, 32))):
        try:
            operation()
        except ValueError:
            negative.append(label)
        else:
            raise AssertionError('invalid oracle/control accepted: '+label)

    after = {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in files}
    assert before == after
    result = {'status': 'AUTHOR_ACTUAL_BOUNDED_SINGLE_WALKER_SHARED_CONTEXT_NOT_ADMITTED',
        'activity': 'RA-CAAAC604CB513AEA8BBC1DFC', 'kernel': kernel, 'source_bank': bank_binding,
        'source_sha256': before, 'sources_unchanged_during_execution': True,
        'cases': cases, 'full61_and_codec6_joint_laws_equal': True,
        'budget_interruption': stopped, 'random_interruption': rng_stop,
        'live_object_recovered': recovered, 'recovery_oracle': walker.oracle.evidence(),
        'negative_controls_rejected': negative,
        'actual_BRC_core_calls': len(CALLS)-first, 'actual_BRC_core_receipts': CALLS[first:],
        'order_or_factors_supplied': False, 'ideal_reference_run': False,
        'polynomial_point_query_bound_claimed': False,
        'random_contract': 'software randrange fixture and exhaustive rational joint-law test; no physical randomness claim'}
    raw = packed(serializable(result))
    target = ROOT / 'SINGLE_WALKER_RESULTS.json.gz'
    target.write_bytes(gzip.compress(raw, mtime=0))
    assert gzip.decompress(target.read_bytes()) == raw
    summary = {key: result[key] for key in ('status', 'activity', 'source_bank', 'source_sha256',
        'sources_unchanged_during_execution', 'full61_and_codec6_joint_laws_equal',
        'negative_controls_rejected', 'actual_BRC_core_calls', 'order_or_factors_supplied',
        'ideal_reference_run', 'polynomial_point_query_bound_claimed', 'random_contract')}
    summary['cases'] = [{key: case[key] for key in ('N', 'a', 't', 'dimension',
        'positive_parent_prefixes_checked', 'child_history_edges_checked',
        'all_joint_branch_and_work_masses_equal', 'retained_residual_nonzero',
        'prefix_oracle_distinct_queries_sum', 'peak_one_prefix_cached_row_slots')} | {
            'sample': case['seeded_execution_not_frequency_test'],
            'sample_oracle_report': case['sample_oracle']['report']} for case in cases]
    summary['budget_then_rng_interruption_live_resumed'] = True
    summary['payload_sha256'] = hashlib.sha256(raw).hexdigest()
    summary['gzip_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
    (ROOT / 'SINGLE_WALKER_SUMMARY.json').write_text(
        json.dumps(json.loads(packed(serializable(summary))), indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'actual_BRC_core_calls': result['actual_BRC_core_calls'],
        'payload_sha256': summary['payload_sha256'], 'cases': [
            {'dim': case['dimension'], 'edges': case['child_history_edges_checked'],
             'sample_queries': case['sample_oracle']['report']['distinct_queries'],
             'sample_slots': case['sample_oracle']['report']['cached_row_scalar_slots']}
            for case in cases]}), flush=True)


if __name__ == '__main__':
    main()
