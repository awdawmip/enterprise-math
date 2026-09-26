"""Bounded same-native-word comparisons, not an ideal-reference experiment."""
from __future__ import annotations
import gzip
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
import sys
from time import perf_counter

ROOT = Path(__file__).resolve().parent
PACKAGE = ROOT.parents[1]
for p in (PACKAGE / 'new_word_compiler', PACKAGE / 'direct_word_integration',
          ROOT.parent / 'streaming', ROOT.parent / 'carrier_codec'):
    sys.path.insert(0, str(p))
from gram_sampler import GramSampler, QueryBudgetExhausted
from lazy_streaming import SelectedStreamingProgram, LazyStreamingProgram
from carrier_codec import ExactCarrierCodec
from compiled_streaming import bank_from_compilation
from check_direct_word_integration import bound_sources
from certified_word_compiler import PositivePathObserver, packed
from stage45.brc_loop_recheck import CALLS, verify_vendor
from stage80.fixed_phase import norm


def load_bank():
    source = PACKAGE / 'direct_word_integration/DIRECT_WORD_INTEGRATION_RESULTS.json.gz'
    raw = gzip.decompress(source.read_bytes())
    expected = '79491e65feec104f2cdc9de510263efef749d8a1174f9cab4c20146a0171615c'
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError('direct phase archive changed')
    compilation = json.loads(raw)['phase_compilation']
    admitted = bank_from_compilation(compilation, t=4, epsilon=F(1))
    return admitted['bank'], {'payload_sha256': expected,
                              'complete_error_certificate': admitted['error_certificate']}


def observed_zero_shift(state, den, dim, observer):
    rows = tuple(state.values())
    matrix = []
    for i in range(dim):
        row = []
        for j in range(dim):
            terms = tuple((F(v[i], den), F(v[j], den)) for v in rows if v[i] and v[j])
            if terms:
                value = observer.evaluate('explicit_state_zero_shift_gram', terms)
            else:
                value = F(0)  # structural absence of contributing signed paths
            row.append(value)
        matrix.append(tuple(row))
    return tuple(matrix)


def main():
    files = [ROOT / 'gram_sampler.py', Path(__file__),
             ROOT.parent / 'streaming/lazy_streaming.py',
             ROOT.parent / 'lazy_modular/lazy_modular.py',
             ROOT.parent / 'carrier_codec/carrier_codec.py']
    source_hashes = {str(p.relative_to(PACKAGE)): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in files}
    first = len(CALLS)
    sources = bound_sources()
    kernel = verify_vendor()
    bank, source_bank = load_bank()
    cases = []
    for N, history, use_codec in (
            (15, (0, 0, 0, 0), True), (15, (0, 0, 1, 1), True),
            (21, (0, 0, 0, 0), True), (21, (1, 0, 1, 0), True),
            (21, (1, 1, 1, 1), True), (21, (1, 0, 1, 0), False)):
        codec = ExactCarrierCodec(61, tuple(range(6))) if use_codec else None
        gram_program = LazyStreamingProgram(N, 2, 4, bank, 61, codec=codec)
        explicit = SelectedStreamingProgram(N, 2, 4, bank, 61, codec=codec)
        gram = GramSampler(gram_program)
        state, den = explicit.initial()
        observed = PositivePathObserver()
        checks = []
        gram_seconds = explicit_seconds = 0.0
        for depth, bit in enumerate(history):
            tic = perf_counter()
            conditional = gram.probabilities()
            gram_seconds += perf_counter()-tic
            tic = perf_counter()
            plan = explicit.branch_plan(state, den, history[:depth])
            explicit_seconds += perf_counter()-tic
            assert conditional['parent_mass'] == norm(state, den)
            assert conditional['child_masses'] == plan.masses
            assert conditional['probabilities'] == tuple(m/norm(state, den) for m in plan.masses)
            tic = perf_counter()
            gram.advance(bit)
            gram_seconds += perf_counter()-tic
            tic = perf_counter()
            state, den = explicit.materialize(plan, bit)
            explicit_seconds += perf_counter()-tic
            assert gram.mass() == norm(state, den)
            gamma = gram.gamma(depth+1, 1)
            actual = tuple(tuple(F(x, gamma.den) for x in row) for row in gamma.rows)
            expected = observed_zero_shift(state, den, explicit.dim, observed)
            assert actual == expected
            checks.append({'depth': depth, 'selected_bit': bit,
                'parent_mass': conditional['parent_mass'],
                'child_masses': conditional['child_masses'],
                'conditional_probabilities': conditional['probabilities'],
                'selected_mass': gram.mass(), 'explicit_selected_rows': len(state),
                'all_zero_shift_correlation_entries_equal': True,
                'gram_distinct_queries': len(gram.cache)})
        report = gram.report()
        explicit_metrics = explicit.report_metrics()
        case = {'N': N, 'a': 2, 't': 4, 'declared_history': history,
                'dimension': explicit.dim, 'fixed_history_not_random_sample': True,
                'all_conditions_and_selected_masses_equal': True,
                'checks': checks, 'gram': gram.evidence(),
                'explicit_metrics': explicit_metrics,
                'same_actual_state_gram_observer': observed.operations,
                'gram_round_seconds': gram_seconds,
                'explicit_round_seconds': explicit_seconds,
                'timing_scope': 'one local warm-cache run; native admission and matrix comparison excluded; no general speedup claim'}
        cases.append(case)
        print(json.dumps({'N': N, 'history': history, 'dim': explicit.dim,
                          'queries': report['distinct_queries'],
                          'gram_slots': report['cached_matrix_scalar_slots'],
                          'explicit_peak_rows': explicit_metrics['selected_child']['peak_materialized_child_rows'],
                          'native_observer_calls': report['actual_positive_path_observations']}), flush=True)

    # A bounded query stop is honest and resumable only in this live object.
    budget_program = LazyStreamingProgram(21, 2, 4, bank, 61,
                                         codec=ExactCarrierCodec(61, tuple(range(6))))
    budget = GramSampler(budget_program, query_budget=0)
    try:
        budget.probabilities()
    except QueryBudgetExhausted:
        assert not budget.cache and not budget.history
    else:
        raise AssertionError('zero query budget accepted a fresh query')
    budget.query_budget = 1000
    recovered = budget.probabilities()
    assert recovered['parent_mass'] == 1
    rejected = []
    for name, operation in (
            ('boolean_bit', lambda: budget.advance(True)),
            ('future_prefix', lambda: budget.gamma(1, 1)),
            ('out_of_domain_residue', lambda: budget.gamma(0, 0))):
        try:
            operation()
        except ValueError:
            rejected.append(name)
        else:
            raise AssertionError('invalid query/control accepted: '+name)
    current_hashes = {str(p.relative_to(PACKAGE)): hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in files}
    if source_hashes != current_hashes:
        raise RuntimeError('scientific dependency source changed during bounded execution')
    payload = {'status': 'AUTHOR_ACTUAL_BOUNDED_GRAM_PROTOTYPE_SHARED_CONTEXT_NOT_ADMITTED',
        'activity': 'RA-CAAAC604CB513AEA8BBC1DFC', 'kernel': kernel,
        'prior_sources': sources, 'source_bank': source_bank,
        'source_sha256': source_hashes,
        'dependency_sources_unchanged_during_execution': True,
        'cases': cases, 'zero_budget_stopped_then_live_object_resumed': True,
        'negative_controls_rejected': rejected,
        'budget_case_evidence': budget.evidence(),
        'native_core_call_receipts': CALLS[first:], 'actual_BRC_core_calls': len(CALLS)-first,
        'unknown_order_or_factor_supplied': False,
        'new_ideal_reference_execution': False,
        'scope': 'exact same-native-word conditional masses; memoized correlation representation; no polynomial query bound or durable cursor claimed'}
    raw = packed(payload)
    target = ROOT / 'GRAM_SAMPLER_RESULTS.json.gz'
    target.write_bytes(gzip.compress(raw, mtime=0))
    assert gzip.decompress(target.read_bytes()) == raw
    summary = {k: v for k, v in payload.items() if k not in
               ('cases', 'native_core_call_receipts', 'budget_case_evidence')}
    summary['cases'] = []
    for case in cases:
        entry = {k: case[k] for k in ('N', 'a', 't', 'declared_history', 'dimension',
            'all_conditions_and_selected_masses_equal', 'gram_round_seconds', 'explicit_round_seconds')}
        entry['gram_report'] = case['gram']['report']
        entry['explicit_selected_metrics'] = case['explicit_metrics']['selected_child']
        entry['zero_shift_matrices_checked'] = len(case['checks'])
        summary['cases'].append(entry)
    summary['payload_sha256'] = hashlib.sha256(raw).hexdigest()
    summary['gzip_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
    (ROOT / 'GRAM_SAMPLER_SUMMARY.json').write_text(
        json.dumps(json.loads(packed(summary)), indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': payload['status'], 'actual_BRC_core_calls': payload['actual_BRC_core_calls'],
                      'payload_sha256': summary['payload_sha256']}), flush=True)


if __name__ == '__main__':
    main()
