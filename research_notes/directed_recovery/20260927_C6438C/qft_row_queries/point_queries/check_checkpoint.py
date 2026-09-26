"""Bounded comparisons with actual explicit native rows, including zeros."""
from pathlib import Path
from fractions import Fraction as F
import gzip
import hashlib
import json
import random
import sys
from time import perf_counter

ROOT = Path(__file__).resolve().parent
PREVIOUS = ROOT.parents[1] / 'sep26-shor-general'
sys.path.insert(0, str(ROOT.parent / 'gram_research'))
sys.path.insert(0, str(PREVIOUS / 'phases'))
from checkpoint_row_oracle import CheckpointRowOracle
from check_single_walker import (load_bank, ExactCarrierCodec, SelectedStreamingProgram,
    LazyStreamingProgram, PointRowOracle, SingleWalker, serializable, packed,
    ScriptedRandom, CALLS, verify_vendor)
from closed_phase_bank import load_certified_bank


def equal_row(row, state, den, label, dim):
    expected = state.get((0, label, 0), (0,)*dim)
    assert all(x*den == y*row.den for x, y in zip(row.values, expected))


def small_exact(bank):
    cases = []
    for use_codec in (True, False):
        codec = ExactCarrierCodec(61, tuple(range(6))) if use_codec else None
        program = LazyStreamingProgram(21, 2, 4, bank, 61, codec=codec)
        explicit = SelectedStreamingProgram(21, 2, 4, bank, 61, codec=codec)
        initial, initial_den = explicit.initial()
        frontier = [((), initial, initial_den)]
        reports, comparisons = [], 0
        for depth in range(5):
            following = []
            for history, state, den in frontier:
                oracle = CheckpointRowOracle(program, history)
                # Every work-carrier label including unreachable/outside-N labels.
                for label in range(32):
                    equal_row(oracle.query(depth, label), state, den, label, program.dim)
                    comparisons += 1
                equal_row(oracle.query(0, 1), initial, initial_den, 1, program.dim)
                if depth:
                    assert oracle.report()['checkpoint_depth'] == depth//2
                reports.append({'history': history, 'oracle': oracle.evidence()})
                if depth < 4:
                    for bit, (child, cd) in enumerate(explicit.branches(state, den, history)):
                        following.append((history+(bit,), child, cd))
            frontier = following
        # Both exact point oracles must consume the same auxiliary/local coins.
        p1 = LazyStreamingProgram(21, 2, 4, bank, 61, codec=codec)
        p2 = LazyStreamingProgram(21, 2, 4, bank, 61, codec=codec)
        memo = SingleWalker(p1)
        checkpoint = SingleWalker(p2, oracle=CheckpointRowOracle(p2))
        a, b = memo.run(random.Random(927271)), checkpoint.run(random.Random(927271))
        assert a['status'] == b['status'] == 'COMPLETE_READOUT'
        for key in ('history', 'latent_work_label', 'events', 'k'):
            assert a[key] == b[key], key
        cases.append({'dimension': program.dim, 'queried_rows_exact': comparisons,
            'all_31_prefixes_including_zero_mass_checked': True,
            'all_32_carrier_labels_checked_at_each_prefix': True,
            'oracle_evidence': reports, 'single_sample': b,
            'single_sample_evidence': checkpoint.oracle.evidence(),
            'same_random_tape_matches_memoized_walker': True})
    return cases


def tradeoff_case():
    bank, _, dim, binding = load_certified_bank(8, cutoff=33,
        expected_payload_sha256='feecbc02808991f6d7b1e2c3179c8da2018b76901ef34c26ef0d28b65729dd5c')
    history = (1, 0, 1, 1, 0, 1, 0)
    explicit = SelectedStreamingProgram(251, 6, 8, bank, dim)
    state, den = explicit.initial()
    for depth, bit in enumerate(history):
        plan = explicit.branch_plan(state, den, history[:depth])
        state, den = explicit.materialize(plan, bit)
    # A predetermined label, not selected from a precomputed order or factors.
    label = 1
    trials = []
    rows = []
    for cap in (0, 1, 2, 3):
        program = LazyStreamingProgram(251, 6, 8, bank, dim)
        oracle = CheckpointRowOracle(program, history, checkpoint_depth_cap=cap)
        began = perf_counter()
        row = oracle.query(7, label)
        seconds = perf_counter()-began
        equal_row(row, state, den, label, dim)
        rows.append(row)
        report = oracle.report()
        assert report['point_node_visits'] == (1 << (8-cap))-1
        trials.append({'depth_cap': cap, 'row': row, 'seconds': seconds,
                       'oracle': oracle.evidence()})
    assert all(row == rows[0] for row in rows)
    return {'N': 251, 'a': 6, 't': 8, 'queried_prefix_depth': 7,
        'fixed_history': history, 'queried_label': label, 'bank_binding': binding,
        'scope': 'eight-round exact native instrument; not default t=16 Shor factoring',
        'explicit_current_state_rows_for_validation_only': len(state),
        'trials': trials, 'same_exact_full61_row_all_caps': True,
        'total_memory_reduction_claimed': False,
        'runtime_comparison_is_one_fixture_not_asymptotic': True}


def main():
    began = perf_counter()
    sources = [Path(__file__), ROOT/'checkpoint_row_oracle.py',
        ROOT.parent/'gram_research/single_walker.py']
    before = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    first = len(CALLS)
    kernel = verify_vendor()
    bank, binding = load_bank()
    cases = small_exact(bank)
    print('small rows verified', flush=True)
    tradeoff = tradeoff_case()
    program = LazyStreamingProgram(21, 2, 4, bank, 61, codec=ExactCarrierCodec(61, tuple(range(6))))
    oracle = CheckpointRowOracle(program, query_budget=0)
    walker = SingleWalker(program, oracle=oracle)
    paused = walker.run(ScriptedRandom([0]))
    assert paused['status'] == 'INCOMPLETE_POINT_QUERY_BUDGET' and not paused['history']
    assert walker.pending_auxiliary_bit == 0
    oracle.query_budget = 100000
    resumed = walker.run(random.Random(917))
    assert resumed['status'] == 'COMPLETE_READOUT'
    # Budget abort during construction keeps the previous checkpoint consistent.
    partial = CheckpointRowOracle(program, (1, 0, 1, 1), query_budget=1)
    try:
        partial.query(4, 1)
    except RuntimeError as exc:
        assert type(exc).__name__ == 'QueryBudgetExhausted'
    else:
        raise AssertionError('missing budget interruption')
    assert partial.checkpoint_depth == 1
    partial.query_budget = 100000
    reference = PointRowOracle(program, (1, 0, 1, 1))
    assert partial.query(4, 1) == reference.query(4, 1)
    negative = []
    for name, call in (
        ('negative_cap', lambda: CheckpointRowOracle(program, checkpoint_depth_cap=-1)),
        ('boolean_cap', lambda: CheckpointRowOracle(program, checkpoint_depth_cap=True)),
        ('future_depth', lambda: CheckpointRowOracle(program).query(1, 1)),
        ('outside_carrier', lambda: CheckpointRowOracle(program).query(0, 32))):
        try: call()
        except ValueError: negative.append(name)
        else: raise AssertionError(name)
    after = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    assert before == after
    result = {'status': 'AUTHOR_ACTUAL_BOUNDED_CHECKPOINT_ROW_ORACLE_NOT_ADMITTED',
        'activity': 'RA-CAAAC604CB513AEA8BBC1DFC', 'source_sha256': before,
        'kernel': kernel, 'small_bank': binding, 'cases': cases, 'tradeoff': tradeoff,
        'interruption': paused, 'live_resume': resumed,
        'checkpoint_build_abort_then_resume_exact': True, 'negative_controls': negative,
        'actual_BRC_core_calls': len(CALLS)-first, 'actual_BRC_core_receipts': CALLS[first:],
        'order_or_factors_supplied': False, 'ideal_reference_run': False,
        'global_polynomial_QFT_or_factoring_claimed': False, 'seconds': perf_counter()-began}
    raw = packed(serializable(result))
    target = ROOT/'CHECKPOINT_RESULTS.json.gz'
    target.write_bytes(gzip.compress(raw, mtime=0))
    brief = {k: result[k] for k in ('status', 'activity', 'source_sha256', 'actual_BRC_core_calls',
        'checkpoint_build_abort_then_resume_exact', 'negative_controls', 'seconds')}
    brief.update({'small_exact_row_comparisons': [c['queried_rows_exact'] for c in cases],
        'tradeoff': {k: v for k, v in tradeoff.items() if k != 'trials'},
        'trials': [{'depth_cap': x['depth_cap'], 'seconds': x['seconds'],
                    'report': x['oracle']['report']} for x in tradeoff['trials']],
        'payload_sha256': hashlib.sha256(raw).hexdigest(),
        'gzip_sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
    (ROOT/'CHECKPOINT_SUMMARY.json').write_text(json.dumps(json.loads(packed(serializable(brief))), indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'actual_BRC_core_calls': result['actual_BRC_core_calls'],
        'row_comparisons': brief['small_exact_row_comparisons'], 'seconds': result['seconds'],
        'tradeoff_nodes': [x['oracle']['report']['point_node_visits'] for x in tradeoff['trials']]}), flush=True)


if __name__ == '__main__':
    main()
