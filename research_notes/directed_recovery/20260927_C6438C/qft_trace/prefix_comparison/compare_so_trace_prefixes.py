"""Alternating matched prefixes for two actual typed certificate policies.

Compile-only candidate until separately authorized. No ideal reference, no
full-law claim, and no assumption that fewer cold observers means warm speedup.
"""
from copy import deepcopy
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter
from uuid import uuid4
import gzip
import hashlib
import json
import sys
import traceback

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parents[1]
POLICY = ROOT.parent/'policy_execution'
TEMPLATE = BASE/'sep27-qft-boundary/prefix_comparison/compare_guarded_prefixes.py'
TEMPLATE_SHA = '78e70a1a27273ae3651cd3e7807d5774e4168e3c51119f26853634b52fd3aa6b'
POLICY_SHA = '62121d7c1e1a7eafff452990b991ddfe027e65ada5e980881aa4d716de92bd20'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


assert sha(TEMPLATE) == TEMPLATE_SHA
assert sha(POLICY/'so_trace_feedback.py') == POLICY_SHA
sys.path.insert(0, str(POLICY))
sys.path.insert(0, str(BASE/'sep26-shor-general/optimization/collision_analysis'))
from so_trace_feedback import BoundaryCheckedSOTrace, SOTraceBank, FrozenBoundary, packed
from boundary_uniform import WordCertificateBank
from check_gram_sampler import load_bank, ExactCarrierCodec, LazyStreamingProgram, CALLS, verify_vendor

CONTEXT = {'stage': 'imported_not_started', 'active_engine': None,
           'cold_banks': [], 'paid_warmups': [], 'pairs': []}


def sources():
    paths = [Path(__file__), TEMPLATE, POLICY/'so_trace_feedback.py',
        ROOT.parent/'trace_bank/so_trace_certificates.py',
        BASE/'sep27-qft-boundary/boundary_execution/boundary_uniform.py',
        BASE/'sep27-qft-uniform/word_certificates/word_certificates.py',
        BASE/'sep27-qft-uniform/uniform_execution/uniform_feedback.py',
        BASE/'sep27-qft-adaptive/adaptive_execution/adaptive_feedback.py']
    return {str(path): sha(path) for path in paths}


def table_inventory(program):
    """Stable instance roles, including inverse caches; no native computation."""
    result = []
    for index, table in enumerate(program.lazy_factory.tables.values()):
        result.append({'role': 'factory', 'parent_factory_index': index,
                       'stats': deepcopy(table.report_metrics())})
        if table._inverse is not None:
            result.append({'role': 'inverse', 'parent_factory_index': index,
                           'stats': deepcopy(table._inverse.report_metrics())})
    return result


def numeric_ledger(engine):
    return [{'history': step.history, 'reference_ids': step.reference_ids,
        'selected_ids': step.selected_ids, 'charge': step.charge, 'bit': step.bit}
        for step in engine.steps]


def run_prefix(cls, program, certificates, history):
    before = table_inventory(program)
    first, started = len(CALLS), perf_counter()
    engine = cls(program, F(1, 3), certificate_bank=certificates)
    CONTEXT['active_engine'] = engine
    plans = [engine.advance(bit) for bit in history]
    terminal_mass = engine.mass()
    calculation_seconds = perf_counter()-started
    calculation_core_calls = len(CALLS)-first
    assert engine._guard_depth == 0 and engine._guard_owner is None
    counters = {'gram': deepcopy(engine.stats), 'policy': deepcopy(engine.policy_stats),
                'guard': engine._guard_diagnostics()}
    after = table_inventory(program)
    ledger = numeric_ledger(engine)
    capture_started = perf_counter()
    evidence = engine.evidence()
    evidence_seconds = perf_counter()-capture_started
    evidence_end = perf_counter()
    total_calls = len(CALLS)-first
    # Detachment and JSON serialization are outside both reported timings.
    evidence = deepcopy(evidence)
    assert evidence['boundary_guard']['active_depth'] == 0
    assert not evidence['boundary_guard']['owner_active']
    receipt = {'implementation': cls.__name__, 'history': history,
        'calculation_seconds': calculation_seconds, 'evidence_capture_seconds': evidence_seconds,
        'total_seconds_through_evidence': evidence_end-started,
        'counter_and_inventory_gap_seconds': evidence_end-started-calculation_seconds-evidence_seconds,
        'calculation_actual_core_calls': calculation_core_calls,
        'total_actual_core_calls': total_calls, 'core_call_interval': [first, len(CALLS)],
        'table_instances_before': before, 'table_instances_after': after,
        'counters_before_evidence': counters, 'plans': plans, 'terminal_mass': terminal_mass,
        'numeric_ledger': ledger, 'evidence': evidence,
        'timing_scope': 'constructor, four advances, final mass; evidence separate; no JSON output timing'}
    CONTEXT['active_engine'] = None
    return receipt


def assert_warm(before, after):
    assert [(x['role'], x['parent_factory_index']) for x in before] == [
        (x['role'], x['parent_factory_index']) for x in after]
    for old, new in zip(before, after):
        assert old['stats']['computed_columns'] == new['stats']['computed_columns']
        assert old['stats']['column_adder_digit_replays'] == new['stats']['column_adder_digit_replays']


def main():
    target = ROOT/'SO_TRACE_MATCHED_PREFIX_RESULTS.json.gz'
    summary_path = ROOT/'SO_TRACE_MATCHED_PREFIX_SUMMARY.json'
    if target.exists() or summary_path.exists():
        raise ValueError('refusing to overwrite completed experiment evidence')
    guard_path = ROOT.parent/'STARTUP_GUARD.json'
    guard = json.loads(guard_path.read_bytes())
    assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True
    assert guard['mode'] == 'TASK_RESEARCH' and guard['boundary'] == 'startup'
    assert guard['activity_id'] == 'RA-CAAAC604CB513AEA8BBC1DFC' and guard['sync_debt_events'] == []
    source = sources()
    first, started = len(CALLS), perf_counter()
    CONTEXT['stage'] = 'actual_native_bank_and_program_admission'
    vendor = verify_vendor()
    native_bank, native_source = load_bank()
    programs = [LazyStreamingProgram(N, a, 4, native_bank, 61,
        codec=ExactCarrierCodec(61, tuple(range(6)))) for N, a in ((21, 2), (21, 4), (65, 3))]
    admission_stop = len(CALLS)
    banks = {}
    for name, cls in (('old_rank_two', WordCertificateBank), ('new_so_trace', SOTraceBank)):
        CONTEXT['stage'] = 'cold_bank:'+name
        cold_first, cold_started = len(CALLS), perf_counter()
        bank = cls(programs[0])
        cold_seconds = perf_counter()-cold_started
        banks[name] = bank
        CONTEXT['cold_banks'].append({'label': name, 'elapsed_seconds': cold_seconds,
            'actual_core_calls': len(CALLS)-cold_first,
            'call_interval': [cold_first, len(CALLS)], 'evidence': bank.evidence()})
    history = (1, 0, 0, 0)
    for program in programs:
        CONTEXT['fixture'] = {'N': program.N, 'a': program.a, 't': program.t}
        banks['old_rank_two'].check(program)
        banks['new_so_trace'].check(program)
        # Paid preconditioning of the common program tables and native caches.
        # Each warmup/measured engine has its own empty Gram cache.
        CONTEXT['stage'] = 'paid_warmup'
        warmup = run_prefix(FrozenBoundary, program, banks['old_rank_two'], history)
        CONTEXT['paid_warmups'].append({'N': program.N, 'a': program.a, 'run': warmup})
        for repetition, order in enumerate(((FrozenBoundary, BoundaryCheckedSOTrace),
                                            (BoundaryCheckedSOTrace, FrozenBoundary))):
            CONTEXT['stage'] = 'matched_pair:'+str(repetition)
            runs = []
            CONTEXT['current_pair_runs'] = runs
            for cls in order:
                selected_bank = banks['old_rank_two' if cls is FrozenBoundary else 'new_so_trace']
                runs.append(run_prefix(cls, program, selected_bank, history))
            old = next(run for run in runs if run['implementation'] == FrozenBoundary.__name__)
            new = next(run for run in runs if run['implementation'] == BoundaryCheckedSOTrace.__name__)
            assert old['plans'] == new['plans'] and old['numeric_ledger'] == new['numeric_ledger']
            assert old['terminal_mass'] == new['terminal_mass'] > 0
            assert old['calculation_actual_core_calls'] == new['calculation_actual_core_calls']
            assert old['counters_before_evidence']['gram'] == new['counters_before_evidence']['gram']
            assert old['counters_before_evidence']['policy'] == new['counters_before_evidence']['policy']
            for run in runs:
                assert_warm(run['table_instances_before'], run['table_instances_after'])
            for key in ('correlations', 'observer_operations'):
                assert old['evidence']['inherited'][key] == new['evidence']['inherited'][key]
            # Certificate hashes and cursor schemas intentionally differ.
            summary = {'N': program.N, 'a': program.a, 'repetition': repetition,
                'order': [run['implementation'] for run in runs],
                'old_seconds': old['calculation_seconds'], 'new_seconds': new['calculation_seconds'],
                'old_evidence_seconds': old['evidence_capture_seconds'],
                'new_evidence_seconds': new['evidence_capture_seconds'],
                'old_total_seconds': old['total_seconds_through_evidence'],
                'new_total_seconds': new['total_seconds_through_evidence'],
                'core_calls_each': old['calculation_actual_core_calls'],
                'old_full_binding_checks': old['counters_before_evidence']['policy']['certificate_binding_checks'],
                'new_full_binding_checks': new['counters_before_evidence']['policy']['certificate_binding_checks'],
                'old_guard_stats': old['counters_before_evidence']['guard']['stats'],
                'new_guard_stats': new['counters_before_evidence']['guard']['stats'],
                'new_factory_and_inverse_columns_each': 0,
                'new_column_digit_replays_each': 0,
                'full_covariances_observer_streams_numeric_ledger_and_native_counters_equal': True,
                'strict_cross_version_cursor_equality_claimed': False}
            CONTEXT['pairs'].append({'summary': summary, 'runs': runs})
            print(json.dumps(summary), flush=True)
    assert source == sources()
    CONTEXT['stage'] = 'serialize_success_evidence'
    record = {'schema': 'BRC_SO_TRACE_MATCHED_PREFIX_COMPARISON_V1', 'status': 'PASSED',
        'source_hashes': source, 'startup_guard': {'sha256': sha(guard_path), 'receipt': guard},
        'vendor': vendor, 'native_bank_source': native_source,
        'native_admission_call_interval': [first, admission_stop],
        'separate_cold_banks': CONTEXT['cold_banks'], 'paid_warmups': CONTEXT['paid_warmups'],
        'pairs': CONTEXT['pairs'], 'actual_native_core_calls': CALLS[first:],
        'actual_native_core_call_count': len(CALLS)-first, 'elapsed_seconds': perf_counter()-started,
        'programs': [{'N': p.N, 'a': p.a, 'phase_bindings': p.phase_bindings,
            'codec_binding': p.codec_binding, 'factory_tables': [t.export_certificate()
                for t in p.lazy_factory.tables.values()], 'inverse_tables': [
                    {'parent_factory_index': j, 'certificate': t._inverse.export_certificate()}
                    for j, t in enumerate(p.lazy_factory.tables.values()) if t._inverse is not None],
            'permutation_verifications': p.lazy_permutation_verifications} for p in programs],
        'scope': 'Three fixed positive prefixes; two alternating paired orders each; one process; '
            'fresh Gram engines, shared warmed modular instances. Cold banks and paid warmups separate. '
            'System load uncontrolled. No full law, independent random trial, cold-start speedup or asymptotic claim.'}
    raw = packed(record)
    with target.open('xb') as handle:
        handle.write(gzip.compress(raw, mtime=0))
    summary = {'schema': record['schema'], 'status': record['status'], 'source_hashes': source,
        'pairs': [item['summary'] for item in record['pairs']],
        'actual_native_core_call_count': record['actual_native_core_call_count'],
        'elapsed_seconds': record['elapsed_seconds'], 'raw_bytes': len(raw),
        'raw_sha256': hashlib.sha256(raw).hexdigest(), 'gzip_bytes': target.stat().st_size,
        'gzip_sha256': sha(target)}
    with summary_path.open('xb') as handle:
        handle.write(packed(summary))
    CONTEXT['stage'] = 'complete'
    print(packed(summary).decode(), flush=True)


def incomplete_engine_snapshot(engine):
    if engine is None:
        return None
    return {'history': engine.history, 'numeric_ledger': numeric_ledger(engine),
        'pending': engine.pending, 'certificates': engine.certificates,
        'interruption_events': engine.interruptions, 'policy_stats': engine.policy_stats,
        'gram_stats': engine.stats, 'observer_operations': engine.observer.operations,
        'correlations': [{'depth': key[0], 'residue': key[1], 'rows': value.rows, 'den': value.den}
            for key, value in sorted(engine.cache.items())],
        'guard_depth': engine._guard_depth, 'guard_owner_active': engine._guard_owner is not None,
        'incomplete_not_revalidated': True}


if __name__ == '__main__':
    first = len(CALLS)
    initial_sources = sources()
    try:
        main()
    except BaseException as error:
        failure = {'status': 'FAILED_EXECUTION', 'known_stage': CONTEXT['stage'],
            'source_hashes_at_start': initial_sources, 'source_hashes_at_failure': sources(),
            'exception_type': type(error).__name__, 'exception_message': str(error),
            'traceback': traceback.format_exc(), 'fixture': CONTEXT.get('fixture'),
            'cold_banks': CONTEXT['cold_banks'], 'completed_warmups': CONTEXT['paid_warmups'],
            'completed_pairs': CONTEXT['pairs'], 'current_pair_runs': CONTEXT.get('current_pair_runs'),
            'incomplete_current_engine': incomplete_engine_snapshot(CONTEXT['active_engine']),
            'attached_exception_evidence': getattr(error, 'evidence', None),
            'actual_native_core_calls': CALLS[first:]}
        path = ROOT/('FAILED_EXECUTION_'+uuid4().hex+'.json.gz')
        with path.open('xb') as handle:
            handle.write(gzip.compress(packed(failure), mtime=0))
        print('Failed execution evidence saved: '+str(path), file=sys.stderr, flush=True)
        raise
